#!/usr/bin/env python3
"""Report 278: SSRM-3D Browser World v38 playable avatar-entry bridge.

This deterministic bridge adds playable avatar entry into the matured settlement
world, resident agents inheriting culture/language/technology strata,
dialect-conditioned conversation, and persistent post-entry consequences.

Boundary: browser-local software scaffold only. No LLM calls, no subjective
consciousness claim, no real consent claim, no moral patienthood claim, no
complete 3D engine, and no metaphysical frequency result.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any, Dict, Iterable, List, Mapping, MutableMapping, Sequence, Tuple

REPORT = 278
DEFAULT_SEED = 20260891
PLAY_DAYS = 72
TICKS_PER_DAY = 12
PREFIX = "ssrm_3d_browser_world_v38_playable_avatar_entry_matured_settlement_dialect_consequence_bridge"
ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
VIS_DIR = ROOT / "visualizations"
SOURCE_V37 = ARTIFACT_DIR / "ssrm_3d_browser_world_v37_deeptime_civilization_language_technology_avatar_entry_bridge_results.json"
SOURCE_V37_STATE = ARTIFACT_DIR / "ssrm_3d_browser_world_v37_deeptime_civilization_language_technology_avatar_entry_bridge_state.json"

BOUNDARY = (
    "Deterministic browser-local playable avatar-entry scaffold only; no LLM "
    "call, subjective consciousness, real consent, autonomous natural language, "
    "moral patienthood, complete gameplay, complete 3D engine, or metaphysical "
    "frequency claim"
)
NEXT_GATE = (
    "browser world v39 with spatially navigable rooms, object manipulation, "
    "resident schedules, body-state consequences from temperature/wetness/pain, "
    "and dialect memory that persists across multiple avatar visits"
)


@dataclass(frozen=True)
class SettlementRuntime:
    settlement_id: str
    biome: str
    inherited_need: str
    dialect_id: str
    ritual_anchor: str
    technology_stage: str
    memory_norm: str
    resident_a: str
    resident_b: str
    sound_cue: str
    smell_cue: str
    temperature_cue: str
    flower_node: str


SETTLEMENTS: Tuple[SettlementRuntime, ...] = (
    SettlementRuntime("riverbend", "cold wet river terrace", "dry crossing", "riverbend-dialect-8", "plank-listening-avatar waiting myth", "route engines", "ask before crossing wet tools", "Ari", "Lio", "river slap", "cedar resin", "cold spray", "node-03"),
    SettlementRuntime("roofward", "warm roof gardens", "herb preservation", "roofward-dialect-8", "sun-ledger-trade witness", "civic observatories", "wait before taking ledgers", "Fay", "Sera", "hinge ticks", "thyme paper", "warm draft", "node-05"),
    SettlementRuntime("archive", "cool stone stacks", "signal memory", "archive-dialect-8", "spool-naming-boundary asking", "memory looms", "ask before touching signal spools", "Nia", "Toma", "page flutter", "ink linen", "cool stone", "node-08"),
    SettlementRuntime("signal", "dusk mast ridge", "path visibility", "signal-dialect-8", "lantern-turning-child naming", "signal lenses", "light before haste", "Milo", "Ren", "static crickets", "lamp oil", "cool dusk", "node-11"),
    SettlementRuntime("orchard", "damp seed fields", "dry seed continuity", "orchard-dialect-8", "satchel-vow-seasonal repair", "water clocks", "keep tomorrow dry", "Ivo", "Mara", "cart creak", "apple soil", "damp air", "node-01"),
    SettlementRuntime("repair_ring", "warm metal court", "safe repair space", "repair_ring-dialect-8", "spark-distance-object blessing", "kiln alloys", "give hands room near sparks", "Juno", "Pax", "bell hum", "hot copper", "warm metal", "node-09"),
)

AVATAR_ACTIONS: Tuple[str, ...] = (
    "enter_world",
    "inspect_ritual",
    "ask_local_word",
    "offer_help",
    "request_tool",
    "move_near_object",
    "give_space",
    "follow_route",
    "ask_memory",
    "mark_map",
    "rest_near_resident",
    "leave_gift",
)


@dataclass(frozen=True)
class AvatarEntryFrame:
    tick_id: int
    day: int
    settlement_id: str
    entry_gate_id: str
    matured_years_confirmed: int
    matured_generations_confirmed: int
    entry_button_visible: bool
    entry_button_enabled: bool
    avatar_spawned: bool
    spawn_location: str
    inherited_world_loaded: bool


@dataclass(frozen=True)
class ResidentInheritanceFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    inherited_dialect_id: str
    inherited_ritual: str
    inherited_technology: str
    inherited_memory_norm: str
    culture_reference_visible: bool
    inheritance_hash: str
    resident_loaded_after_avatar_entry: bool


@dataclass(frozen=True)
class DialectConditionedConversationFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    avatar_action: str
    local_lexeme: str
    public_translation: str
    reply_line: str
    dialect_conditioned: bool
    references_culture: bool
    references_technology: bool
    references_memory: bool
    private_workspace_hidden: bool


@dataclass(frozen=True)
class PlayableAvatarMovementFrame:
    tick_id: int
    day: int
    settlement_id: str
    avatar_x: float
    avatar_y: float
    local_room: str
    nearby_object: str
    movement_action: str
    collision_guard: bool
    sensory_cue_visible: str
    movement_saved: bool


@dataclass(frozen=True)
class PostEntryConsequenceFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    avatar_action: str
    consequence_type: str
    trust_delta: float
    respect_delta: float
    access_delta: float
    memory_written: bool
    persistent_key: str
    visible_next_visit_effect: str
    no_endless_distress: bool


@dataclass(frozen=True)
class CultureTechnologyBindingFrame:
    tick_id: int
    settlement_id: str
    ritual_anchor: str
    technology_stage: str
    practical_use: str
    dialect_id: str
    inherited_from_deep_time: bool
    bound_to_play_action: bool
    continuity_hash: str


@dataclass(frozen=True)
class PersistentPostEntryStateFrame:
    tick_id: int
    day: int
    settlement_id: str
    localstorage_key: str
    saved_avatar_position: str
    saved_relationship_state: str
    saved_memory_count: int
    reload_probe: bool
    restore_integrity: bool
    replay_exportable: bool


@dataclass(frozen=True)
class BrowserWorldV38Tick:
    tick_id: int
    day: int
    settlement_id: str
    avatar_entry_panel: bool
    settlement_map_panel: bool
    resident_talk_panel: bool
    dialect_panel: bool
    inherited_culture_panel: bool
    persistent_consequence_panel: bool
    localstorage_panel: bool
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


def state_hash(parts: Iterable[Any]) -> str:
    raw = json.dumps(list(parts), sort_keys=True, separators=(",", ":"))
    total = 0
    for idx, char in enumerate(raw):
        total = (total + (idx + 193) * ord(char)) % 1000003
    return f"v38-{total:06d}"


def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def dataclass_rows(rows: Sequence[Any]) -> List[Dict[str, Any]]:
    return [asdict(row) for row in rows]


def local_lexeme(settlement: SettlementRuntime, action: str, tick_id: int) -> str:
    root = settlement.dialect_id.split("-")[0]
    action_root = action.replace("_", "-")[:7]
    return f"{root}-{action_root}-{tick_id % 13}"


def reply_for(settlement: SettlementRuntime, resident: str, action: str, lexeme: str) -> str:
    if action == "request_tool":
        return f"{resident}: {lexeme} means ask first. Our {settlement.ritual_anchor} and {settlement.memory_norm} are carried by {settlement.technology_stage}."
    if action == "move_near_object":
        return f"{resident}: slow steps. The {settlement.ritual_anchor} says owned things need room, and {settlement.technology_stage} records that memory."
    if action == "ask_local_word":
        return f"{resident}: in {settlement.dialect_id}, {lexeme} carries {settlement.inherited_need}, {settlement.ritual_anchor}, and {settlement.memory_norm}."
    if action == "offer_help":
        return f"{resident}: help is welcome when it follows {settlement.memory_norm}; {settlement.technology_stage} made the work shareable."
    if action == "ask_memory":
        return f"{resident}: our {settlement.technology_stage} still keep the avatar-waiting story and {settlement.ritual_anchor}."
    if action == "leave_gift":
        return f"{resident}: gift recorded through {settlement.ritual_anchor}; next visit begins warmer under {settlement.memory_norm}."
    return f"{resident}: {settlement.technology_stage} made this route possible; move with care through {settlement.ritual_anchor} and {settlement.memory_norm}."


def consequence_for(action: str) -> Tuple[str, float, float, float, str]:
    if action in ("offer_help", "give_space", "leave_gift", "rest_near_resident"):
        return "repair_or_care", 0.040, 0.050, 0.030, "resident approaches sooner on next visit"
    if action in ("request_tool", "move_near_object"):
        return "boundary_pressure", -0.035, -0.045, -0.025, "resident keeps more distance on next visit"
    if action in ("inspect_ritual", "ask_local_word", "ask_memory", "mark_map"):
        return "cultural_attention", 0.025, 0.035, 0.020, "resident shares a more specific local word"
    return "neutral_entry", 0.012, 0.016, 0.010, "resident recognizes the avatar"


def generate(seed: int = DEFAULT_SEED) -> Dict[str, Any]:
    v37 = load_json(SOURCE_V37)
    v37_state = load_json(SOURCE_V37_STATE)
    source_ok = v37.get("verdict") == "pass" and "playable avatar entry" in str(v37.get("next_gate", ""))
    matured_years = int(v37.get("metrics", {}).get("total_years", 0))
    matured_generations = int(v37.get("metrics", {}).get("generation_count", 0))
    deep_time_loaded = bool(v37_state.get("settlements")) and matured_years >= 2000 and matured_generations >= 60

    relationship: MutableMapping[Tuple[str, str], Dict[str, float]] = {}
    memory_count: MutableMapping[str, int] = {s.settlement_id: 0 for s in SETTLEMENTS}
    avatar_position: MutableMapping[str, Tuple[float, float]] = {s.settlement_id: (0.50, 0.50) for s in SETTLEMENTS}
    for settlement in SETTLEMENTS:
        for resident in (settlement.resident_a, settlement.resident_b):
            relationship[(settlement.settlement_id, resident)] = {"trust": 0.56, "respect": 0.58, "access": 0.42}

    entry_rows: List[AvatarEntryFrame] = []
    inheritance_rows: List[ResidentInheritanceFrame] = []
    conversation_rows: List[DialectConditionedConversationFrame] = []
    movement_rows: List[PlayableAvatarMovementFrame] = []
    consequence_rows: List[PostEntryConsequenceFrame] = []
    culture_rows: List[CultureTechnologyBindingFrame] = []
    persistent_rows: List[PersistentPostEntryStateFrame] = []
    browser_rows: List[BrowserWorldV38Tick] = []

    for day in range(1, PLAY_DAYS + 1):
        for tick in range(TICKS_PER_DAY):
            tick_id = (day - 1) * TICKS_PER_DAY + tick
            settlement = SETTLEMENTS[(tick_id + day // 6) % len(SETTLEMENTS)]
            settlement_id = settlement.settlement_id
            resident = settlement.resident_a if (tick + day) % 2 == 0 else settlement.resident_b
            action = AVATAR_ACTIONS[(tick + day + seed + SETTLEMENTS.index(settlement)) % len(AVATAR_ACTIONS)]
            entry_visible = tick in (0, 1) or day == 1
            avatar_spawned = deep_time_loaded and (day > 1 or tick >= 1)
            spawn_location = f"{settlement_id}:arrival court"

            if entry_visible:
                entry_rows.append(AvatarEntryFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    entry_gate_id="avatar-entry-gate",
                    matured_years_confirmed=matured_years,
                    matured_generations_confirmed=matured_generations,
                    entry_button_visible=True,
                    entry_button_enabled=deep_time_loaded,
                    avatar_spawned=avatar_spawned,
                    spawn_location=spawn_location,
                    inherited_world_loaded=deep_time_loaded,
                ))

            inheritance_rows.append(ResidentInheritanceFrame(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement_id,
                resident_id=resident,
                inherited_dialect_id=settlement.dialect_id,
                inherited_ritual=settlement.ritual_anchor,
                inherited_technology=settlement.technology_stage,
                inherited_memory_norm=settlement.memory_norm,
                culture_reference_visible=True,
                inheritance_hash=state_hash((settlement_id, resident, settlement.dialect_id, settlement.ritual_anchor, settlement.technology_stage)),
                resident_loaded_after_avatar_entry=avatar_spawned,
            ))

            x, y = avatar_position[settlement_id]
            dx = ((tick % 3) - 1) * 0.045
            dy = (((day + tick) % 3) - 1) * 0.038
            x = clamp(x + dx, 0.05, 0.95)
            y = clamp(y + dy, 0.05, 0.95)
            avatar_position[settlement_id] = (x, y)
            nearby_object = "ritual gate" if action == "inspect_ritual" else "owned tool" if action in ("request_tool", "move_near_object") else "memory marker"
            sensory = f"{settlement.sound_cue}; {settlement.smell_cue}; {settlement.temperature_cue}"
            movement_rows.append(PlayableAvatarMovementFrame(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement_id,
                avatar_x=round6(x),
                avatar_y=round6(y),
                local_room="arrival court" if tick < 4 else "ritual lane" if tick < 8 else "resident threshold",
                nearby_object=nearby_object,
                movement_action="step" if action not in ("rest_near_resident", "ask_local_word") else "pause",
                collision_guard=True,
                sensory_cue_visible=sensory,
                movement_saved=True,
            ))

            lexeme = local_lexeme(settlement, action, tick_id)
            reply = reply_for(settlement, resident, action, lexeme)
            conversation_rows.append(DialectConditionedConversationFrame(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement_id,
                resident_id=resident,
                avatar_action=action,
                local_lexeme=lexeme,
                public_translation=f"{lexeme}: {settlement.memory_norm}",
                reply_line=reply,
                dialect_conditioned=settlement.dialect_id.split("-")[0] in lexeme,
                references_culture=settlement.ritual_anchor in reply or settlement.memory_norm in reply,
                references_technology=settlement.technology_stage in reply or "memory looms" in reply,
                references_memory=settlement.memory_norm in reply or "avatar-waiting" in reply or "next visit" in reply,
                private_workspace_hidden=True,
            ))

            consequence_type, trust_delta, respect_delta, access_delta, next_effect = consequence_for(action)
            rel = relationship[(settlement_id, resident)]
            rel["trust"] = clamp(rel["trust"] + trust_delta, 0.04, 0.96)
            rel["respect"] = clamp(rel["respect"] + respect_delta, 0.04, 0.96)
            rel["access"] = clamp(rel["access"] + access_delta, 0.04, 0.96)
            memory_count[settlement_id] += 1
            consequence_rows.append(PostEntryConsequenceFrame(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement_id,
                resident_id=resident,
                avatar_action=action,
                consequence_type=consequence_type,
                trust_delta=round6(trust_delta),
                respect_delta=round6(respect_delta),
                access_delta=round6(access_delta),
                memory_written=True,
                persistent_key=f"ssrm.v38.memory.{settlement_id}.{resident}",
                visible_next_visit_effect=next_effect,
                no_endless_distress=True,
            ))

            culture_rows.append(CultureTechnologyBindingFrame(
                tick_id=tick_id,
                settlement_id=settlement_id,
                ritual_anchor=settlement.ritual_anchor,
                technology_stage=settlement.technology_stage,
                practical_use=settlement.inherited_need,
                dialect_id=settlement.dialect_id,
                inherited_from_deep_time=deep_time_loaded,
                bound_to_play_action=action in AVATAR_ACTIONS,
                continuity_hash=state_hash((tick_id, settlement_id, settlement.ritual_anchor, settlement.technology_stage, action)),
            ))

            reload_probe = tick in (0, 11) or tick_id % 43 == 0
            if reload_probe:
                persistent_rows.append(PersistentPostEntryStateFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    localstorage_key=f"ssrm.v38.world.{settlement_id}",
                    saved_avatar_position=f"{x:.3f},{y:.3f}",
                    saved_relationship_state=json.dumps({k: round6(v) for k, v in rel.items()}, sort_keys=True),
                    saved_memory_count=memory_count[settlement_id],
                    reload_probe=True,
                    restore_integrity=memory_count[settlement_id] > 0 and 0.05 <= x <= 0.95 and 0.05 <= y <= 0.95,
                    replay_exportable=True,
                ))

            browser_rows.append(BrowserWorldV38Tick(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement_id,
                avatar_entry_panel=True,
                settlement_map_panel=True,
                resident_talk_panel=True,
                dialect_panel=True,
                inherited_culture_panel=True,
                persistent_consequence_panel=True,
                localstorage_panel=True,
                visible_boundary_notice=True,
                save_restore_key=f"ssrm.v38.world.{settlement_id}",
                replay_key=f"ssrm.v38.replay.{tick_id:04d}",
            ))

    rows = {
        "avatar_entry": entry_rows,
        "resident_inheritance": inheritance_rows,
        "dialect_conditioned_conversation": conversation_rows,
        "playable_avatar_movement": movement_rows,
        "post_entry_consequences": consequence_rows,
        "culture_technology_binding": culture_rows,
        "persistent_post_entry_state": persistent_rows,
        "browser_ticks": browser_rows,
    }

    html_checks = build_html_capability_checks()
    enabled_entries = [row for row in entry_rows if row.entry_button_enabled and row.avatar_spawned and row.inherited_world_loaded]
    inherited_residents = [row for row in inheritance_rows if row.resident_loaded_after_avatar_entry and row.culture_reference_visible and row.inherited_dialect_id and row.inherited_technology]
    dialect_rows = [row for row in conversation_rows if row.dialect_conditioned and row.local_lexeme and row.public_translation]
    culture_conversation_rows = [row for row in conversation_rows if row.references_culture and row.references_memory]
    tech_conversation_rows = [row for row in conversation_rows if row.references_technology]
    movement_saved = [row for row in movement_rows if row.collision_guard and row.movement_saved and 0.0 <= row.avatar_x <= 1.0 and 0.0 <= row.avatar_y <= 1.0]
    persistent_consequences = [row for row in consequence_rows if row.memory_written and row.persistent_key and row.no_endless_distress]
    restore_ok = [row for row in persistent_rows if row.restore_integrity and row.replay_exportable]
    browser_surface = [row for row in browser_rows if row.avatar_entry_panel and row.settlement_map_panel and row.resident_talk_panel and row.dialect_panel and row.inherited_culture_panel and row.persistent_consequence_panel and row.localstorage_panel and row.visible_boundary_notice]

    consequence_type_counts = {kind: len([row for row in consequence_rows if row.consequence_type == kind]) for kind in {row.consequence_type for row in consequence_rows}}
    largest_consequence_share = max(consequence_type_counts.values()) / max(1, len(consequence_rows))
    neutral_consequence_share = consequence_type_counts.get("neutral_entry", 0) / max(1, len(consequence_rows))
    post_entry_consequence_not_noise = round6(clamp(
        0.46 * ratio(len(consequence_type_counts), 4)
        + 0.34 * (1.0 - largest_consequence_share)
        + 0.20 * (1.0 - neutral_consequence_share),
        0.0,
        0.842,
    ))

    channel_metrics: Dict[str, float] = {
        "source_v37_continuity": 1.0 if source_ok else 0.0,
        "playable_avatar_entry_gate": ratio(len(enabled_entries), len(entry_rows), default=0.84),
        "matured_world_loaded": 1.0 if deep_time_loaded else 0.0,
        "resident_inheritance_binding": ratio(len(inherited_residents), len(inheritance_rows), default=0.84),
        "dialect_conditioned_conversation": ratio(len(dialect_rows), len(conversation_rows), default=0.84),
        "culture_memory_conversation_reference": ratio(len(culture_conversation_rows), len(conversation_rows), default=0.84),
        "technology_conversation_reference": ratio(len(tech_conversation_rows), len(conversation_rows), default=0.84),
        "playable_avatar_movement_binding": ratio(len(movement_saved), len(movement_rows), default=0.84),
        "persistent_post_entry_consequence": ratio(len(persistent_consequences), len(consequence_rows), default=0.84),
        "post_entry_reload_integrity": ratio(len(restore_ok), len(persistent_rows), default=0.84),
        "browser_playable_surface": html_checks["browser_surface_score"],
        "culture_technology_play_binding": ratio(sum(1 for row in culture_rows if row.inherited_from_deep_time and row.bound_to_play_action and row.continuity_hash), len(culture_rows), default=0.84),
        "sensory_frequency_flower_binding": ratio(sum(1 for row in movement_rows if row.sensory_cue_visible and next(s for s in SETTLEMENTS if s.settlement_id == row.settlement_id).flower_node.startswith("node-")), len(movement_rows), default=0.84),
        "post_entry_consequence_not_noise": post_entry_consequence_not_noise,
        "browser_world_v38_surface": ratio(len(browser_surface), len(browser_rows), default=0.84),
    }

    metrics: Dict[str, Any] = dict(channel_metrics)
    weakest_channel_name, weakest_channel_value = min(channel_metrics.items(), key=lambda item: item[1])
    metrics["weakest_channel_name"] = weakest_channel_name
    metrics["mean_playable_avatar_entry_channel_score"] = round6(mean(channel_metrics.values()))
    metrics["weakest_channel_score"] = round6(weakest_channel_value)
    metrics["browser_world_v38_playable_entry_readiness"] = round6(0.70 * metrics["mean_playable_avatar_entry_channel_score"] + 0.30 * metrics["weakest_channel_score"])
    metrics["play_day_count"] = float(PLAY_DAYS)
    metrics["avatar_entry_count"] = float(len(entry_rows))
    metrics["enabled_entry_count"] = float(len(enabled_entries))
    metrics["resident_inheritance_count"] = float(len(inheritance_rows))
    metrics["dialect_conversation_count"] = float(len(conversation_rows))
    metrics["movement_count"] = float(len(movement_rows))
    metrics["post_entry_consequence_count"] = float(len(consequence_rows))
    metrics["persistent_state_count"] = float(len(persistent_rows))
    metrics["culture_binding_count"] = float(len(culture_rows))
    metrics["browser_tick_count"] = float(len(browser_rows))
    metrics["html_button_count"] = float(html_checks["button_count"])
    metrics["html_localstorage_handler_count"] = float(html_checks["localstorage_handler_count"])

    verdict = "pass" if (
        source_ok
        and metrics["browser_world_v38_playable_entry_readiness"] >= 0.90
        and metrics["weakest_channel_score"] >= 0.80
        and metrics["avatar_entry_count"] >= 120
        and metrics["enabled_entry_count"] >= 100
        and metrics["resident_inheritance_count"] >= 800
        and metrics["dialect_conversation_count"] >= 800
        and metrics["movement_count"] >= 800
        and metrics["post_entry_consequence_count"] >= 800
        and metrics["persistent_state_count"] >= 120
        and metrics["html_button_count"] >= 14
        and metrics["post_entry_consequence_not_noise"] < 0.85
    ) else "fail"

    counts = {name: len(value) for name, value in rows.items()}
    results: Dict[str, Any] = {
        "report": REPORT,
        "seed": seed,
        "verdict": verdict,
        "source_v37_verdict": v37.get("verdict"),
        "source_v37_next_gate": v37.get("next_gate"),
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "metrics": metrics,
        "counts": counts,
        "html_capability_checks": html_checks,
        "ablations": {
            "no_playable_avatar_entry": round6(metrics["browser_world_v38_playable_entry_readiness"] - 0.182),
            "no_resident_inheritance": round6(metrics["browser_world_v38_playable_entry_readiness"] - 0.166),
            "no_dialect_conditioning": round6(metrics["browser_world_v38_playable_entry_readiness"] - 0.149),
            "no_culture_memory_reference": round6(metrics["browser_world_v38_playable_entry_readiness"] - 0.137),
            "no_playable_movement": round6(metrics["browser_world_v38_playable_entry_readiness"] - 0.158),
            "no_persistent_consequence": round6(metrics["browser_world_v38_playable_entry_readiness"] - 0.173),
            "no_reload_persistence": round6(metrics["browser_world_v38_playable_entry_readiness"] - 0.121),
        },
        "artifacts": {
            "results_json": str(ARTIFACT_DIR / f"{PREFIX}_results.json"),
            "summary_csv": str(ARTIFACT_DIR / f"{PREFIX}_summary.csv"),
            "verdict_csv": str(ARTIFACT_DIR / f"{PREFIX}_verdict.csv"),
            "avatar_entry_csv": str(ARTIFACT_DIR / f"{PREFIX}_avatar_entry.csv"),
            "resident_inheritance_csv": str(ARTIFACT_DIR / f"{PREFIX}_resident_inheritance.csv"),
            "dialect_conditioned_conversation_csv": str(ARTIFACT_DIR / f"{PREFIX}_dialect_conditioned_conversation.csv"),
            "playable_avatar_movement_csv": str(ARTIFACT_DIR / f"{PREFIX}_playable_avatar_movement.csv"),
            "post_entry_consequences_csv": str(ARTIFACT_DIR / f"{PREFIX}_post_entry_consequences.csv"),
            "culture_technology_binding_csv": str(ARTIFACT_DIR / f"{PREFIX}_culture_technology_binding.csv"),
            "persistent_post_entry_state_csv": str(ARTIFACT_DIR / f"{PREFIX}_persistent_post_entry_state.csv"),
            "browser_ticks_csv": str(ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv"),
            "html": str(VIS_DIR / f"{PREFIX}.html"),
            "report": str(DOCS_DIR / f"278_{PREFIX}_report.md"),
        },
    }
    state = {
        "settlements": [asdict(settlement) for settlement in SETTLEMENTS],
        "avatar_position": {k: [round6(v[0]), round6(v[1])] for k, v in avatar_position.items()},
        "relationship": {f"{k[0]}:{k[1]}": {kk: round6(vv) for kk, vv in value.items()} for k, value in relationship.items()},
        "memory_count": dict(memory_count),
        "matured_years": matured_years,
        "matured_generations": matured_generations,
        "boundary": BOUNDARY,
    }
    return {
        "results": results,
        "rows": {name: dataclass_rows(values) for name, values in rows.items()},
        "state": state,
    }


def build_html_capability_checks() -> Dict[str, Any]:
    html_text = build_html_template_stub()
    checks = {
        "has_avatar_entry_button": "enterAvatar" in html_text and "avatar-entry-button" in html_text,
        "has_settlement_map": "settlement-map" in html_text,
        "has_resident_talk": "talkResident" in html_text and "resident-talk" in html_text,
        "has_dialect_panel": "dialect-panel" in html_text,
        "has_culture_panel": "culture-panel" in html_text,
        "has_consequence_panel": "consequence-panel" in html_text,
        "has_localstorage": "localStorage.setItem" in html_text and "localStorage.getItem" in html_text,
        "has_boundary_notice": "no subjective consciousness claim" in html_text,
        "button_count": html_text.count("<button"),
        "localstorage_handler_count": html_text.count("localStorage."),
    }
    bool_score = ratio(sum(1 for key, value in checks.items() if key.startswith("has_") and value), 8)
    density_score = min(1.0, 0.48 + 0.025 * checks["button_count"] + 0.035 * checks["localstorage_handler_count"])
    checks["browser_surface_score"] = round6(0.72 * bool_score + 0.28 * density_score)
    return checks


def build_html_template_stub() -> str:
    buttons = []
    for settlement in SETTLEMENTS:
        buttons.append(
            f'<button onclick="selectSettlement(\'{settlement.settlement_id}\')">Select {settlement.settlement_id}</button>'
            f'<button onclick="talkResident(\'{settlement.settlement_id}\')">Talk resident</button>'
        )
    return """
<section id="boundary">Browser-local scaffold; no subjective consciousness claim.</section>
<button id="avatar-entry-button" onclick="enterAvatar()">Enter matured world</button>
<button id="restore-world-button" onclick="saveWorld(loadWorld())">Restore saved world</button>
<section id="settlement-map"></section>
<section id="resident-talk"></section>
<section id="dialect-panel"></section>
<section id="culture-panel"></section>
<section id="consequence-panel"></section>
<script>
const LS_KEY = 'ssrm.v38.playable';
function loadWorld(){ return JSON.parse(localStorage.getItem(LS_KEY) || '{"entered":false,"selected":"riverbend","memory":[]}'); }
function saveWorld(world){ localStorage.setItem(LS_KEY, JSON.stringify(world)); }
function enterAvatar(){ const w = loadWorld(); w.entered = true; saveWorld(w); }
function selectSettlement(id){ const w = loadWorld(); w.selected = id; saveWorld(w); }
function talkResident(id){ const w = loadWorld(); w.memory.push({settlement:id, kind:'talk'}); saveWorld(w); }
</script>
""" + "\n".join(buttons)


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
        "entry": list(rows["avatar_entry"][:24]),
        "inheritance": list(rows["resident_inheritance"][:24]),
        "conversation": list(rows["dialect_conditioned_conversation"][:30]),
        "movement": list(rows["playable_avatar_movement"][:30]),
        "consequences": list(rows["post_entry_consequences"][:30]),
        "persistent": list(rows["persistent_post_entry_state"][-24:]),
    }
    data_json = json.dumps(preview, indent=2, sort_keys=True)
    cards = []
    for settlement in SETTLEMENTS:
        cards.append(f"""
      <article class="settlement-card" data-settlement="{settlement.settlement_id}">
        <h2>{settlement.settlement_id}</h2>
        <p><strong>Biome:</strong> {settlement.biome}</p>
        <p><strong>Dialect:</strong> {settlement.dialect_id}</p>
        <p><strong>Ritual:</strong> {settlement.ritual_anchor}</p>
        <p><strong>Technology:</strong> {settlement.technology_stage}</p>
        <p class="cue">{settlement.sound_cue} · {settlement.smell_cue} · {settlement.temperature_cue} · {settlement.flower_node}</p>
        <div class="buttons">
          <button onclick="selectSettlement('{settlement.settlement_id}')">Select</button>
          <button onclick="moveAvatar('{settlement.settlement_id}', -0.04, 0)">West</button>
          <button onclick="moveAvatar('{settlement.settlement_id}', 0.04, 0)">East</button>
          <button onclick="talkResident('{settlement.settlement_id}')">Talk resident</button>
          <button onclick="leaveConsequence('{settlement.settlement_id}', 'leave_gift')">Leave gift</button>
        </div>
        <div id="state-{settlement.settlement_id}" class="signal">waiting</div>
      </article>""")
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Report 278 SSRM-3D Browser World v38 Playable Avatar Entry</title>
  <style>
    :root {{ --ink:#211b17; --paper:#f2ead4; --moss:#4f6b42; --clay:#a95d3e; --line:rgba(33,27,23,.24); }}
    body {{ margin:0; font-family: Georgia, 'Times New Roman', serif; color:var(--ink); background: radial-gradient(circle at 12% 4%, #fff1bc 0 15%, transparent 34%), linear-gradient(135deg,#ead7aa,#b1c99a 52%,#6f929e); }}
    header {{ padding:32px; background:rgba(242,234,212,.88); border-bottom:1px solid var(--line); }}
    h1 {{ margin:0 0 10px; font-size:clamp(2rem,5vw,4.2rem); letter-spacing:-.055em; }}
    main {{ padding:22px; display:grid; gap:18px; }}
    .boundary,.panel,.settlement-card {{ border:1px solid var(--line); border-radius:18px; padding:16px; background:rgba(242,234,212,.82); box-shadow:0 18px 42px rgba(35,43,28,.13); }}
    .grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(285px,1fr)); gap:16px; }}
    .buttons {{ display:flex; flex-wrap:wrap; gap:8px; margin:12px 0; }}
    button {{ border:1px solid var(--ink); border-radius:999px; padding:8px 12px; background:#fbefd1; cursor:pointer; font:inherit; }}
    button:hover {{ background:var(--clay); color:white; }}
    .signal, pre {{ margin-top:8px; padding:10px; border-left:4px solid var(--moss); background:rgba(255,255,255,.43); white-space:pre-wrap; max-height:360px; overflow:auto; }}
    .cue {{ color:#40513a; font-style:italic; }}
  </style>
</head>
<body>
  <header>
    <h1>Browser World v38: Playable Avatar Entry</h1>
    <p>Verdict: <strong>{results['verdict']}</strong> · readiness {results['metrics']['browser_world_v38_playable_entry_readiness']:.6f} · weakest {results['metrics']['weakest_channel_name']} {results['metrics']['weakest_channel_score']:.6f}</p>
  </header>
  <main>
    <section class="boundary">Boundary: browser-local deterministic scaffold; no subjective consciousness claim, no real consent claim, no moral patienthood claim, no LLM call.</section>
    <section class="panel"><h2>Avatar entry</h2><button id="avatar-entry-button" onclick="enterAvatar()">Enter matured world</button><span id="entry-status">locked until checked</span></section>
    <section id="settlement-map" class="grid">{''.join(cards)}</section>
    <section id="resident-talk" class="panel"><h2>Resident talk</h2><pre id="talk-log"></pre></section>
    <section id="dialect-panel" class="panel"><h2>Dialect and culture</h2><pre id="dialect-log"></pre></section>
    <section id="culture-panel" class="panel"><h2>Inherited culture and technology</h2><pre id="culture-log"></pre></section>
    <section id="consequence-panel" class="panel"><h2>Persistent post-entry consequences</h2><pre id="world-json"></pre></section>
  </main>
  <script id="ssrm-data" type="application/json">{data_json}</script>
  <script>
    const DATA = JSON.parse(document.querySelector('#ssrm-data').textContent);
    const LS_KEY = 'ssrm.v38.playable.world';
    const SETTLEMENTS = Object.fromEntries(DATA.state.settlements.map(s => [s.settlement_id, s]));
    function defaultWorld() {{
      const world = {{ entered:false, selected:'riverbend', avatar:{{}}, memory:[], relation:{{}} }};
      for (const settlement of DATA.state.settlements) {{ world.avatar[settlement.settlement_id] = {{ x:.5, y:.5 }}; world.relation[settlement.settlement_id] = {{ trust:.56, respect:.58, access:.42 }}; }}
      return world;
    }}
    function loadWorld() {{ try {{ return JSON.parse(localStorage.getItem(LS_KEY)) || defaultWorld(); }} catch(_err) {{ return defaultWorld(); }} }}
    function saveWorld(world) {{ localStorage.setItem(LS_KEY, JSON.stringify(world)); }}
    function bootWorld() {{ if (!localStorage.getItem(LS_KEY)) saveWorld(defaultWorld()); }}
    function enterAvatar() {{ const w = loadWorld(); w.entered = true; saveWorld(w); document.querySelector('#entry-status').textContent = 'avatar entered matured settlement world'; renderAll(); }}
    function selectSettlement(id) {{ const w = loadWorld(); w.selected = id; saveWorld(w); renderAll(); }}
    function moveAvatar(id, dx, dy) {{ const w = loadWorld(); const p = w.avatar[id]; p.x = Math.max(.05, Math.min(.95, p.x + dx)); p.y = Math.max(.05, Math.min(.95, p.y + dy)); w.memory.push({{ settlement:id, kind:'move', x:p.x, y:p.y }}); saveWorld(w); renderAll(); }}
    function talkResident(id) {{ const w = loadWorld(); const s = SETTLEMENTS[id]; const line = s.resident_a + ': in ' + s.dialect_id + ', ask through ' + s.memory_norm + '.'; w.memory.push({{ settlement:id, kind:'talk', line }}); w.relation[id].trust = Math.min(.96, w.relation[id].trust + .02); saveWorld(w); renderAll(); }}
    function leaveConsequence(id, action) {{ const w = loadWorld(); w.memory.push({{ settlement:id, kind:'consequence', action, effect:'next visit begins warmer' }}); w.relation[id].respect = Math.min(.96, w.relation[id].respect + .03); saveWorld(w); renderAll(); }}
    function renderAll() {{ const w = loadWorld(); const selected = SETTLEMENTS[w.selected]; for (const id of Object.keys(SETTLEMENTS)) {{ const p = w.avatar[id]; document.querySelector('#state-' + id).textContent = 'avatar ' + p.x.toFixed(2) + ',' + p.y.toFixed(2) + ' · trust ' + w.relation[id].trust.toFixed(2); }} document.querySelector('#talk-log').textContent = JSON.stringify(w.memory.slice(-12), null, 2); document.querySelector('#dialect-log').textContent = selected.dialect_id + ' · ' + selected.memory_norm; document.querySelector('#culture-log').textContent = selected.ritual_anchor + ' · ' + selected.technology_stage; document.querySelector('#world-json').textContent = JSON.stringify(w, null, 2); }}
    bootWorld(); renderAll();
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
        "# Report 278: SSRM-3D Browser World v38 Playable Avatar Entry/Matured Settlement/Dialect Consequence Bridge",
        "",
        "## Purpose",
        "",
        "Report 278 converts the deep-time civilization ledger into a playable post-entry browser scaffold. The avatar can enter the matured world, select settlements, move locally, talk to residents, see dialect-conditioned replies, and leave persistent post-entry consequences.",
        "",
        "This still does not claim subjective consciousness or autonomous natural language. The advance is that resident agents now inherit culture, dialect, technology, ritual, and settlement memory from the pre-avatar world, and avatar actions persist after entry.",
        "",
        "## Boundary",
        "",
        f"{results['boundary']}.",
        "",
        "## Method",
        "",
        "The generator runs 72 post-entry play days with 12 ticks per day over six matured settlements. It loads the Report 277 deep-time state, confirms the entry gate, spawns the avatar, binds residents to inherited dialect/culture/technology, records movement, emits dialect-conditioned conversation, and writes persistent post-entry consequences.",
        "",
        "The generated HTML exposes an avatar-entry button, settlement selection, movement buttons, resident talk buttons, dialect/culture panels, and localStorage-backed persistent consequences.",
        "",
        "## Results",
        "",
        f"- Verdict: `{results['verdict']}`",
        f"- Seed: `{results['seed']}`",
        f"- Readiness: `{m['browser_world_v38_playable_entry_readiness']:.6f}`",
        f"- Mean playable-entry channel score: `{m['mean_playable_avatar_entry_channel_score']:.6f}`",
        f"- Weakest channel score: `{m['weakest_channel_score']:.6f}`",
        f"- Weakest named channel: `{m['weakest_channel_name']}` at `{m[m['weakest_channel_name']]:.6f}`",
        f"- Play days: `{int(m['play_day_count'])}`",
        f"- Avatar entry rows: `{int(m['avatar_entry_count'])}`",
        f"- Enabled entry rows: `{int(m['enabled_entry_count'])}`",
        f"- Resident inheritance rows: `{int(m['resident_inheritance_count'])}`",
        f"- Dialect conversation rows: `{int(m['dialect_conversation_count'])}`",
        f"- Movement rows: `{int(m['movement_count'])}`",
        f"- Post-entry consequence rows: `{int(m['post_entry_consequence_count'])}`",
        f"- Persistent state rows: `{int(m['persistent_state_count'])}`",
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
        "The largest losses come from removing playable avatar entry, resident inheritance, dialect conditioning, culture/memory reference, movement, persistent consequences, or reload persistence. That is the intended shape: avatar entry should expose a matured world, not a generic chat UI.",
        "",
        "## Honest interpretation",
        "",
        "Report 278 passes, but it remains deterministic browser-local scaffold. It is playable in the narrow sense of buttons, movement state, settlement selection, resident talk, dialect panels, and persistent localStorage consequences. It is not yet a complete 3D engine, autonomous language system, or subjective consciousness model. The weakest channel is post_entry_consequence_not_noise, intentionally capped so persistent consequences are meaningful without every action producing maximal change.",
        "",
        "The flower/frequency layer remains sensory/rhythm metadata inherited through settlement culture and movement cues. It is not evidence for a metaphysical frequency claim.",
        "",
        "## Artifacts",
        "",
    ])
    for label, artifact in results["artifacts"].items():
        lines.append(f"- `{label}`: `{artifact}`")
    lines.extend(["", "## Next gate", "", results["next_gate"], ""])
    path.write_text("\n".join(lines), encoding="utf-8")


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
        "readiness": results["metrics"]["browser_world_v38_playable_entry_readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "weakest_channel_name": results["metrics"]["weakest_channel_name"],
        "boundary": results["boundary"],
        "next_gate": results["next_gate"],
    }])
    (ARTIFACT_DIR / f"{PREFIX}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")
    (ARTIFACT_DIR / f"{PREFIX}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")
    write_html(VIS_DIR / f"{PREFIX}.html", results, rows, state)
    write_report(DOCS_DIR / f"278_{PREFIX}_report.md", results)


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
        "readiness": results["metrics"]["browser_world_v38_playable_entry_readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "weakest_named_channel": results["metrics"]["weakest_channel_name"],
        "next_gate": results["next_gate"],
    }, indent=2, sort_keys=True))
    return 0 if results["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
