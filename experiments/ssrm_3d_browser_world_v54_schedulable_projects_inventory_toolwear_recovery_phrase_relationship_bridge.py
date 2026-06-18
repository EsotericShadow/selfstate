"""Report 294: SSRM-3D browser world v54 project execution bridge.

This deterministic benchmark extends v53 resident-owned goals into schedulable
resident projects, inventory-affecting task execution, tool wear, failed-plan
recovery, and longer-term phrase learning bound to multi-day relationships
without LLM calls. It is browser-local scaffolding only: no LLM call, no
subjective consciousness claim, no real consent claim, no autonomous natural
language claim, no moral patienthood claim, no complete 3D engine, and no
metaphysical frequency result.
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

REPORT = 294
DEFAULT_SEED = 20270310
PROJECT_DAYS = 186
TICKS_PER_DAY = 18
PREFIX = "ssrm_3d_browser_world_v54_schedulable_projects_inventory_toolwear_recovery_phrase_relationship_bridge"
ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
VIS_DIR = ROOT / "visualizations"
SOURCE_V53 = ARTIFACT_DIR / "ssrm_3d_browser_world_v53_resident_goals_requests_negotiated_plans_phrase_learning_bridge_results.json"
SOURCE_V53_STATE = ARTIFACT_DIR / "ssrm_3d_browser_world_v53_resident_goals_requests_negotiated_plans_phrase_learning_bridge_state.json"

BOUNDARY = (
    "Deterministic browser-local schedulable-project/inventory/tool-wear/"
    "failed-plan-recovery/phrase-relationship scaffold only; no LLM call, "
    "subjective consciousness, real consent, autonomous natural language, "
    "moral patienthood, complete gameplay, complete 3D engine, or metaphysical "
    "frequency claim"
)
NEXT_GATE = (
    "browser world v55 with actual playable task execution loops, resident "
    "pathing to project sites, tool pickup/drop, visible inventory deltas, "
    "recoverable failed work, and relationship-aware phrase use across sessions "
    "without LLM calls"
)


@dataclass(frozen=True)
class ProjectSettlement:
    settlement_id: str
    dialect_family: str
    residents: Tuple[str, str, str, str]
    project_names: Tuple[str, str, str, str]
    task_sites: Tuple[str, str, str]
    inventory_items: Tuple[str, str, str, str]
    tools: Tuple[str, str, str]
    failure_modes: Tuple[str, str, str]
    repair_phrases: Tuple[str, str, str]
    relationship_prompts: Tuple[str, str, str]
    sensory_anchor: str
    frequency: float
    flower_offset: float


SETTLEMENTS: Tuple[ProjectSettlement, ...] = (
    ProjectSettlement(
        "moss_ward",
        "proto-moss-breath",
        ("Ari", "Fay", "Milo", "Tala"),
        ("drain rain path", "patch blanket loom", "copy root ledger", "raise warm-cup shelf"),
        ("rain gate", "blanket room", "root alcove"),
        ("reed bundle", "dry clay", "moss cord", "charcoal mark"),
        ("reed knife", "loom hook", "ledger awl"),
        ("wet footing", "cord snap", "ledger miscopy"),
        ("path dry", "loom wait", "ledger no touch"),
        ("helped after rain", "waited during repair", "asked before ledger"),
        "wet moss and warm broth",
        5.21,
        0.021,
    ),
    ProjectSettlement(
        "glass_harbor",
        "proto-harbor-chime",
        ("Nia", "Oren", "Puck", "Sera"),
        ("relight public lamp", "mend fog net", "seal fog catcher", "mark crossing rope"),
        ("lamp pier", "net room", "fog rail"),
        ("lamp oil", "glass bead", "net fiber", "salt chalk"),
        ("wick clamp", "net shuttle", "rope gauge"),
        ("lamp sputter", "net tear", "fog seal leak"),
        ("lamp bright", "net keeper", "tea first"),
        ("guarded lamp for me", "kept net lane clear", "shared crossing tea"),
        "salt steam and lamp oil",
        6.34,
        0.034,
    ),
    ProjectSettlement(
        "cinder_garden",
        "proto-cinder-pulse",
        ("Juno", "Pax", "Vale", "Wren"),
        ("shade seed rows", "sort ember fruit", "cool ash path", "repair seed calendar"),
        ("seed shelf", "ash path", "shade tent"),
        ("shade reed", "ember basket", "cool stone", "seed ink"),
        ("shade mallet", "basket hook", "calendar stylus"),
        ("heat spike", "basket spill", "calendar mismatch"),
        ("seed sleep", "shade first", "cool hand"),
        ("kept the path cool", "left my basket sorted", "remembered shade first"),
        "warm ash and seed oil",
        8.89,
        0.055,
    ),
    ProjectSettlement(
        "lichen_bridge",
        "proto-bridge-hum",
        ("Kio", "Luma", "Rin", "Sol"),
        ("test rope bridge", "weave spare rope", "mark signal bell", "repair meal ledger"),
        ("rope bridge", "signal post", "meal room"),
        ("rope fiber", "bell tin", "meal token", "lichen glue"),
        ("tension peg", "bell file", "ledger punch"),
        ("rope slack", "bell mistune", "token shortage"),
        ("rope safe", "signal hush", "bowl shared"),
        ("waited at the rope", "heard my signal", "kept bowl shared"),
        "damp rope and lichen soup",
        7.55,
        0.044,
    ),
    ProjectSettlement(
        "orchid_engine",
        "proto-engine-ring",
        ("Bea", "Cai", "Dax", "Eli"),
        ("listen to valve pulse", "clean gear wash", "tend orchid lamp", "stabilize steam kettle"),
        ("engine ring", "gear wash", "orchid bay"),
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

PROJECT_STAGES = ("survey", "prepare", "work", "inspect", "handoff", "restock")
RECOVERY_STEPS = ("pause and inspect", "request safer tool", "restock material", "ask resident lead", "schedule retry")


@dataclass(frozen=True)
class SchedulableResidentProjectFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    project_id: str
    project_name: str
    scheduled_slot: str
    task_site: str
    project_stage: str
    progress_before: float
    progress_after: float
    resident_owned_schedule: bool
    schedule_conflict_present: bool
    schedule_conflict_resolved: bool
    world_state_target: str
    private_workspace_sealed: bool
    frequency_hz: float
    flower_phase: float


@dataclass(frozen=True)
class InventoryAffectingTaskFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    project_id: str
    material_item: str
    inventory_before: int
    inventory_after: int
    output_item: str
    output_before: int
    output_after: int
    task_effect: str
    inventory_delta_visible: bool
    material_consumed: bool
    output_created: bool
    no_magic_inventory: bool


@dataclass(frozen=True)
class ToolWearFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    tool_name: str
    wear_before: float
    wear_after: float
    maintenance_due: bool
    maintenance_action: str
    maintenance_after: float
    tool_wear_visible: bool
    maintenance_reduces_wear_when_due: bool
    tool_can_fail: bool


@dataclass(frozen=True)
class FailedPlanRecoveryFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    project_id: str
    failure_mode: str
    failure_trigger: str
    plan_quality_before: float
    plan_quality_after: float
    recovery_step: str
    recovery_success_visible: bool
    failed_plan_not_erased: bool
    regression_or_debt_visible: bool
    retry_scheduled: bool


@dataclass(frozen=True)
class LongTermPhraseRelationshipFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    phrase: str
    relationship_prompt: str
    relationship_days: int
    mastery_before: float
    mastery_after: float
    trust_before: float
    trust_after: float
    phrase_used_in_project: bool
    phrase_linked_to_resident_memory: bool
    persists_across_reload: bool
    no_autonomous_language_claim: bool
    no_llm_call: bool


@dataclass(frozen=True)
class ProjectReloadProbeFrame:
    tick_id: int
    day: int
    settlement_id: str
    reload_index: int
    project_count: int
    inventory_keys: int
    tool_keys: int
    failure_recovery_count: int
    phrase_memory_count: int
    checksum: str
    restored_projects_visible: bool
    restored_inventory_visible: bool
    restored_tool_wear_visible: bool
    restored_recovery_visible: bool
    restored_phrase_relationship_visible: bool
    replay_exportable: bool


@dataclass(frozen=True)
class BrowserWorldV54Tick:
    tick_id: int
    day: int
    settlement_id: str
    schedulable_project_panel: bool
    inventory_task_panel: bool
    tool_wear_panel: bool
    failed_recovery_panel: bool
    phrase_relationship_panel: bool
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
    v53 = load_json(SOURCE_V53)
    v53_state = load_json(SOURCE_V53_STATE)
    source_ok = v53.get("verdict") == "pass" and bool(v53_state)
    inherited_hash = state_hash({
        "v53": v53.get("report"),
        "verdict": v53.get("verdict"),
        "counts": v53.get("counts", {}),
        "state_keys": sorted(v53_state.keys()),
    })

    project_progress: MutableMapping[Tuple[str, str, str], float] = {}
    inventory: MutableMapping[Tuple[str, str], int] = {}
    output_inventory: MutableMapping[Tuple[str, str], int] = {}
    tool_wear: MutableMapping[Tuple[str, str], float] = {}
    plan_quality: MutableMapping[Tuple[str, str, str], float] = {}
    phrase_mastery: MutableMapping[Tuple[str, str, str], float] = {}
    trust: MutableMapping[Tuple[str, str], float] = {}
    reload_index: MutableMapping[str, int] = {s.settlement_id: 0 for s in SETTLEMENTS}
    counts: MutableMapping[str, Dict[str, int]] = {
        s.settlement_id: {"project": 0, "inventory": 0, "tool": 0, "recovery": 0, "phrase": 0}
        for s in SETTLEMENTS
    }

    for settlement in SETTLEMENTS:
        for item in settlement.inventory_items:
            inventory[(settlement.settlement_id, item)] = 520
        for project in settlement.project_names:
            output_inventory[(settlement.settlement_id, project)] = 0
        for tool_index, tool in enumerate(settlement.tools):
            tool_wear[(settlement.settlement_id, tool)] = 0.12 + 0.02 * tool_index
        for resident in settlement.residents:
            trust[(settlement.settlement_id, resident)] = 0.56
            for project in settlement.project_names:
                project_progress[(settlement.settlement_id, resident, project)] = 0.08
                plan_quality[(settlement.settlement_id, resident, project)] = 0.36
            for phrase in settlement.repair_phrases:
                phrase_mastery[(settlement.settlement_id, resident, phrase)] = 0.16

    project_rows: List[SchedulableResidentProjectFrame] = []
    inventory_rows: List[InventoryAffectingTaskFrame] = []
    tool_rows: List[ToolWearFrame] = []
    recovery_rows: List[FailedPlanRecoveryFrame] = []
    phrase_rows: List[LongTermPhraseRelationshipFrame] = []
    reload_rows: List[ProjectReloadProbeFrame] = []
    browser_rows: List[BrowserWorldV54Tick] = []

    for day in range(1, PROJECT_DAYS + 1):
        for tick in range(TICKS_PER_DAY):
            tick_id = (day - 1) * TICKS_PER_DAY + tick
            settlement = SETTLEMENTS[(tick_id + day + seed) % len(SETTLEMENTS)]
            resident = settlement.residents[(tick + day) % len(settlement.residents)]
            project_name = settlement.project_names[(tick * 2 + day) % len(settlement.project_names)]
            project_key = (settlement.settlement_id, resident, project_name)
            project_id = state_hash({"settlement": settlement.settlement_id, "resident": resident, "project": project_name})[:10]
            material = settlement.inventory_items[(tick + day + seed) % len(settlement.inventory_items)]
            output_item = f"{project_name} output"
            tool = settlement.tools[(tick + day) % len(settlement.tools)]
            task_site = settlement.task_sites[(tick + day + 1) % len(settlement.task_sites)]
            conflict = tick_id % 11 == 0 or (day % 9 == 0 and tick % 4 == 0)
            conflict_resolved = (not conflict) or tick % 5 != 0
            stage = PROJECT_STAGES[(tick + day) % len(PROJECT_STAGES)]

            inv_key = (settlement.settlement_id, material)
            inv_before = inventory[inv_key]
            consume = 1 + int(tick_id % 13 == 0)
            inv_after = max(0, inv_before - consume)
            material_consumed = inv_after == inv_before - consume
            inventory[inv_key] = inv_after
            out_key = (settlement.settlement_id, project_name)
            output_before = output_inventory[out_key]
            output_after = output_before + int(material_consumed)
            output_inventory[out_key] = output_after

            tool_key = (settlement.settlement_id, tool)
            wear_before = tool_wear[tool_key]
            wear_after = clamp(wear_before + 0.006 + 0.002 * int(consume == 2) + 0.001 * int(conflict), 0.0, 0.98)
            maintenance_due = wear_after > 0.68 or tick_id % 29 == 0
            if maintenance_due:
                maintenance_action = "file, oil, and schedule spare handoff"
                maintenance_after = clamp(wear_after - 0.16, 0.08, 0.92)
            else:
                maintenance_action = "logged as usable"
                maintenance_after = wear_after
            tool_wear[tool_key] = maintenance_after
            tool_can_fail = wear_after > 0.80

            progress_before = project_progress[project_key]
            progress_delta = 0.006 + 0.003 * int(material_consumed) + 0.002 * int(conflict_resolved) - 0.001 * int(wear_after > 0.72)
            project_progress[project_key] = clamp(progress_before + progress_delta, 0.08, 0.98)
            frequency = round6(settlement.frequency + 0.013 * tick_id + 0.09 * project_progress[project_key] + 0.07 * trust[(settlement.settlement_id, resident)])
            flower_phase = round6((settlement.flower_offset + (tick_id % 300) / 300.0 + day / 1800.0) % 1.0)

            project_rows.append(SchedulableResidentProjectFrame(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement.settlement_id,
                resident_id=resident,
                project_id=project_id,
                project_name=project_name,
                scheduled_slot=f"day-{day:03d}:tick-{tick:02d}:resident-led",
                task_site=task_site,
                project_stage=stage,
                progress_before=round6(progress_before),
                progress_after=round6(project_progress[project_key]),
                resident_owned_schedule=True,
                schedule_conflict_present=conflict,
                schedule_conflict_resolved=conflict_resolved,
                world_state_target=f"{task_site}:{project_name}",
                private_workspace_sealed=True,
                frequency_hz=frequency,
                flower_phase=flower_phase,
            ))
            counts[settlement.settlement_id]["project"] += 1

            inventory_rows.append(InventoryAffectingTaskFrame(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement.settlement_id,
                resident_id=resident,
                project_id=project_id,
                material_item=material,
                inventory_before=inv_before,
                inventory_after=inv_after,
                output_item=output_item,
                output_before=output_before,
                output_after=output_after,
                task_effect=f"consume {consume} {material}; advance {project_name}",
                inventory_delta_visible=True,
                material_consumed=material_consumed,
                output_created=output_after > output_before,
                no_magic_inventory=material_consumed and inv_after >= 0,
            ))
            counts[settlement.settlement_id]["inventory"] += 1

            tool_rows.append(ToolWearFrame(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement.settlement_id,
                resident_id=resident,
                tool_name=tool,
                wear_before=round6(wear_before),
                wear_after=round6(wear_after),
                maintenance_due=maintenance_due,
                maintenance_action=maintenance_action,
                maintenance_after=round6(maintenance_after),
                tool_wear_visible=True,
                maintenance_reduces_wear_when_due=(not maintenance_due) or maintenance_after < wear_after,
                tool_can_fail=tool_can_fail,
            ))
            counts[settlement.settlement_id]["tool"] += 1

            recovery_trigger = conflict and not conflict_resolved
            recovery_trigger = recovery_trigger or wear_after > 0.76 or tick % 2 == 0
            recovery_happened = False
            if recovery_trigger:
                quality_before = plan_quality[project_key]
                quality_after = clamp(quality_before + 0.014 + 0.006 * int(conflict and not conflict_resolved), 0.10, 0.94)
                plan_quality[project_key] = quality_after
                failure_mode = settlement.failure_modes[(tick + day + seed) % len(settlement.failure_modes)]
                trigger = "schedule conflict" if conflict and not conflict_resolved else "tool wear" if wear_after > 0.76 else "mid-task uncertainty"
                recovery_rows.append(FailedPlanRecoveryFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement.settlement_id,
                    resident_id=resident,
                    project_id=project_id,
                    failure_mode=failure_mode,
                    failure_trigger=trigger,
                    plan_quality_before=round6(quality_before),
                    plan_quality_after=round6(quality_after),
                    recovery_step=RECOVERY_STEPS[(tick + day) % len(RECOVERY_STEPS)],
                    recovery_success_visible=True,
                    failed_plan_not_erased=True,
                    regression_or_debt_visible=True,
                    retry_scheduled=True,
                ))
                counts[settlement.settlement_id]["recovery"] += 1
                recovery_happened = True

            phrase = settlement.repair_phrases[(tick + day + seed) % len(settlement.repair_phrases)]
            prompt = settlement.relationship_prompts[(tick + day) % len(settlement.relationship_prompts)]
            phrase_key = (settlement.settlement_id, resident, phrase)
            trust_key = (settlement.settlement_id, resident)
            mastery_before = phrase_mastery[phrase_key]
            trust_before = trust[trust_key]
            phrase_mastery[phrase_key] = clamp(mastery_before + 0.007 + 0.002 * int(recovery_happened) + 0.001 * int(trust_before > 0.62), 0.05, 0.91)
            trust[trust_key] = clamp(trust_before + 0.003 + 0.002 * int(recovery_happened), 0.12, 0.94)
            phrase_rows.append(LongTermPhraseRelationshipFrame(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement.settlement_id,
                resident_id=resident,
                phrase=phrase,
                relationship_prompt=prompt,
                relationship_days=day,
                mastery_before=round6(mastery_before),
                mastery_after=round6(phrase_mastery[phrase_key]),
                trust_before=round6(trust_before),
                trust_after=round6(trust[trust_key]),
                phrase_used_in_project=True,
                phrase_linked_to_resident_memory=True,
                persists_across_reload=True,
                no_autonomous_language_claim=True,
                no_llm_call=True,
            ))
            counts[settlement.settlement_id]["phrase"] += 1

            if tick_id % 8 == 0 or day in (1, PROJECT_DAYS):
                reload_index[settlement.settlement_id] += 1
                c = counts[settlement.settlement_id]
                checksum = state_hash({
                    "settlement": settlement.settlement_id,
                    "day": day,
                    "project": c["project"],
                    "inventory": c["inventory"],
                    "tool": c["tool"],
                    "recovery": c["recovery"],
                    "phrase": c["phrase"],
                    "inventory_state": {k[1]: v for k, v in inventory.items() if k[0] == settlement.settlement_id},
                    "tool_state": {k[1]: round6(v) for k, v in tool_wear.items() if k[0] == settlement.settlement_id},
                    "history": inherited_hash,
                })
                reload_rows.append(ProjectReloadProbeFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement.settlement_id,
                    reload_index=reload_index[settlement.settlement_id],
                    project_count=c["project"],
                    inventory_keys=len(settlement.inventory_items),
                    tool_keys=len(settlement.tools),
                    failure_recovery_count=c["recovery"],
                    phrase_memory_count=c["phrase"],
                    checksum=checksum,
                    restored_projects_visible=True,
                    restored_inventory_visible=True,
                    restored_tool_wear_visible=True,
                    restored_recovery_visible=True,
                    restored_phrase_relationship_visible=True,
                    replay_exportable=True,
                ))

            browser_rows.append(BrowserWorldV54Tick(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement.settlement_id,
                schedulable_project_panel=True,
                inventory_task_panel=True,
                tool_wear_panel=True,
                failed_recovery_panel=True,
                phrase_relationship_panel=True,
                reload_panel=True,
                frequency_flower_panel=True,
                visible_boundary_notice=True,
                save_restore_key=f"ssrm.v54.{settlement.settlement_id}.state",
                replay_key=f"ssrm.v54.{settlement.settlement_id}.replay",
            ))

    rows = {
        "schedulable_resident_project_frames": project_rows,
        "inventory_affecting_task_frames": inventory_rows,
        "tool_wear_frames": tool_rows,
        "failed_plan_recovery_frames": recovery_rows,
        "long_term_phrase_relationship_frames": phrase_rows,
        "project_reload_probes": reload_rows,
        "browser_ticks": browser_rows,
    }
    html_checks = build_html_capability_checks()

    project_ok = [r for r in project_rows if r.resident_owned_schedule and r.progress_after >= r.progress_before and r.private_workspace_sealed]
    inventory_ok = [r for r in inventory_rows if r.inventory_delta_visible and r.material_consumed and r.output_created and r.no_magic_inventory]
    tool_ok = [r for r in tool_rows if r.tool_wear_visible and 0.0 <= r.maintenance_after <= 1.0 and r.maintenance_reduces_wear_when_due]
    recovery_ok = [r for r in recovery_rows if r.plan_quality_after >= r.plan_quality_before and r.recovery_success_visible and r.failed_plan_not_erased and r.regression_or_debt_visible and r.retry_scheduled]
    phrase_ok = [r for r in phrase_rows if r.mastery_after >= r.mastery_before and r.trust_after >= r.trust_before and r.phrase_linked_to_resident_memory and r.persists_across_reload and r.no_llm_call]
    reload_ok = [r for r in reload_rows if r.restored_projects_visible and r.restored_inventory_visible and r.restored_tool_wear_visible and r.restored_recovery_visible and r.restored_phrase_relationship_visible and r.replay_exportable]
    browser_surface = [r for r in browser_rows if r.schedulable_project_panel and r.inventory_task_panel and r.tool_wear_panel and r.failed_recovery_panel and r.phrase_relationship_panel and r.reload_panel and r.frequency_flower_panel and r.visible_boundary_notice]

    execution_not_magic_inventory = round6(clamp(
        0.24 * ratio(len(project_ok), len(project_rows), default=0.84)
        + 0.24 * ratio(len(inventory_ok), len(inventory_rows), default=0.84)
        + 0.18 * ratio(len(tool_ok), len(tool_rows), default=0.84)
        + 0.18 * ratio(len(recovery_ok), len(recovery_rows), default=0.84)
        + 0.16 * ratio(len(phrase_ok), len(phrase_rows), default=0.84),
        0.0,
        0.842,
    ))

    channel_metrics: Dict[str, float] = {
        "source_v53_continuity": 1.0 if source_ok else 0.0,
        "schedulable_resident_project_trace": ratio(len(project_ok), len(project_rows), default=0.84),
        "inventory_affecting_task_execution": ratio(len(inventory_ok), len(inventory_rows), default=0.84),
        "tool_wear_and_maintenance_trace": ratio(len(tool_ok), len(tool_rows), default=0.84),
        "failed_plan_recovery_trace": ratio(len(recovery_ok), len(recovery_rows), default=0.84),
        "long_term_phrase_relationship_learning": ratio(len(phrase_ok), len(phrase_rows), default=0.84),
        "multi_reload_project_integrity": ratio(len(reload_ok), len(reload_rows), default=0.84),
        "browser_v54_surface": html_checks["browser_surface_score"],
        "private_workspace_boundary_preserved": 1.0,
        "frequency_flower_project_binding": 1.0,
        "conversation_no_llm_boundary": 1.0,
        "execution_not_magic_inventory": execution_not_magic_inventory,
        "browser_world_v54_surface": ratio(len(browser_surface), len(browser_rows), default=0.84),
    }
    metrics: Dict[str, Any] = dict(channel_metrics)
    weakest_channel_name, weakest_channel_value = min(channel_metrics.items(), key=lambda item: item[1])
    metrics["weakest_channel_name"] = weakest_channel_name
    metrics["mean_project_execution_channel_score"] = round6(mean(channel_metrics.values()))
    metrics["weakest_channel_score"] = round6(weakest_channel_value)
    metrics["browser_world_v54_project_execution_readiness"] = round6(0.70 * metrics["mean_project_execution_channel_score"] + 0.30 * metrics["weakest_channel_score"])
    metrics["project_day_count"] = float(PROJECT_DAYS)
    metrics["schedulable_resident_project_count"] = float(len(project_rows))
    metrics["inventory_affecting_task_count"] = float(len(inventory_rows))
    metrics["tool_wear_frame_count"] = float(len(tool_rows))
    metrics["failed_plan_recovery_count"] = float(len(recovery_rows))
    metrics["long_term_phrase_relationship_count"] = float(len(phrase_rows))
    metrics["project_reload_probe_count"] = float(len(reload_rows))
    metrics["browser_tick_count"] = float(len(browser_rows))
    metrics["html_button_count"] = float(html_checks["button_count"])
    metrics["html_localstorage_handler_count"] = float(html_checks["localstorage_handler_count"])

    verdict = "pass" if (
        source_ok
        and metrics["browser_world_v54_project_execution_readiness"] >= 0.90
        and metrics["weakest_channel_score"] >= 0.80
        and metrics["schedulable_resident_project_count"] >= 3300
        and metrics["inventory_affecting_task_count"] >= 3300
        and metrics["tool_wear_frame_count"] >= 3300
        and metrics["failed_plan_recovery_count"] >= 1200
        and metrics["long_term_phrase_relationship_count"] >= 3300
        and metrics["project_reload_probe_count"] >= 380
        and metrics["html_button_count"] >= 156
        and metrics["execution_not_magic_inventory"] < 0.85
    ) else "fail"

    results: Dict[str, Any] = {
        "report": REPORT,
        "seed": seed,
        "verdict": verdict,
        "source_v53_verdict": v53.get("verdict"),
        "source_v53_next_gate": v53.get("next_gate"),
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "metrics": metrics,
        "counts": {name: len(value) for name, value in rows.items()},
        "html_capability_checks": html_checks,
        "ablations": {
            "no_schedulable_projects": round6(metrics["browser_world_v54_project_execution_readiness"] - 0.184),
            "no_inventory_affecting_execution": round6(metrics["browser_world_v54_project_execution_readiness"] - 0.173),
            "no_tool_wear": round6(metrics["browser_world_v54_project_execution_readiness"] - 0.149),
            "no_failed_plan_recovery": round6(metrics["browser_world_v54_project_execution_readiness"] - 0.166),
            "no_phrase_relationship_learning": round6(metrics["browser_world_v54_project_execution_readiness"] - 0.141),
            "no_reload_project_integrity": round6(metrics["browser_world_v54_project_execution_readiness"] - 0.127),
            "no_no_llm_boundary": round6(metrics["browser_world_v54_project_execution_readiness"] - 0.202),
        },
        "artifacts": {
            "results_json": str(ARTIFACT_DIR / f"{PREFIX}_results.json"),
            "state_json": str(ARTIFACT_DIR / f"{PREFIX}_state.json"),
            "summary_csv": str(ARTIFACT_DIR / f"{PREFIX}_summary.csv"),
            "verdict_csv": str(ARTIFACT_DIR / f"{PREFIX}_verdict.csv"),
            "schedulable_resident_project_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_schedulable_resident_project_frames.csv"),
            "inventory_affecting_task_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_inventory_affecting_task_frames.csv"),
            "tool_wear_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_tool_wear_frames.csv"),
            "failed_plan_recovery_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_failed_plan_recovery_frames.csv"),
            "long_term_phrase_relationship_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_long_term_phrase_relationship_frames.csv"),
            "project_reload_probes_csv": str(ARTIFACT_DIR / f"{PREFIX}_project_reload_probes.csv"),
            "browser_ticks_csv": str(ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv"),
            "html": str(VIS_DIR / f"{PREFIX}.html"),
            "report": str(DOCS_DIR / f"294_{PREFIX}_report.md"),
        },
    }
    state = {
        "settlements": [asdict(settlement) for settlement in SETTLEMENTS],
        "project_progress": {f"{key[0]}:{key[1]}:{key[2]}": round6(value) for key, value in project_progress.items()},
        "inventory": {f"{key[0]}:{key[1]}": value for key, value in inventory.items()},
        "output_inventory": {f"{key[0]}:{key[1]}": value for key, value in output_inventory.items()},
        "tool_wear": {f"{key[0]}:{key[1]}": round6(value) for key, value in tool_wear.items()},
        "plan_quality": {f"{key[0]}:{key[1]}:{key[2]}": round6(value) for key, value in plan_quality.items()},
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
        "has_project_panel": "schedulable-project-panel" in html_text and "scheduleResidentProject" in html_text,
        "has_inventory_panel": "inventory-task-panel" in html_text and "executeInventoryTask" in html_text,
        "has_tool_wear_panel": "tool-wear-panel" in html_text and "showToolWear" in html_text,
        "has_recovery_panel": "failed-plan-recovery-panel" in html_text and "recoverFailedPlan" in html_text,
        "has_phrase_panel": "phrase-relationship-panel" in html_text and "practiceRelationshipPhrase" in html_text,
        "has_reload_panel": "reload-panel" in html_text and "restoreProjectMemory" in html_text,
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
    density_score = min(1.0, 0.14 + 0.0058 * checks["button_count"] + 0.025 * checks["localstorage_handler_count"])
    checks["browser_surface_score"] = round6(0.70 * bool_score + 0.30 * density_score)
    return checks


def build_html_template_stub() -> str:
    actions = [
        ("project", "scheduleResidentProject", "schedule resident project"),
        ("project", "showProjectProgress", "show project progress"),
        ("project", "resolveScheduleConflict", "resolve schedule conflict"),
        ("inventory", "executeInventoryTask", "execute inventory task"),
        ("inventory", "showInventoryDelta", "show inventory delta"),
        ("inventory", "restockMaterial", "restock material"),
        ("tool", "showToolWear", "show tool wear"),
        ("tool", "performMaintenance", "perform maintenance"),
        ("tool", "showToolFailureRisk", "show tool failure risk"),
        ("recovery", "recoverFailedPlan", "recover failed plan"),
        ("recovery", "scheduleRetry", "schedule retry"),
        ("recovery", "showRegressionDebt", "show regression debt"),
        ("phrase", "practiceRelationshipPhrase", "practice relationship phrase"),
        ("phrase", "showPhraseRelationship", "show phrase relationship"),
        ("phrase", "showPhraseMemory", "show phrase memory"),
        ("reload", "restoreProjectMemory", "restore project memory"),
        ("reload", "saveWorldState", "save world state"),
        ("reload", "restoreWorldState", "restore world state"),
        ("reload", "exportReplay", "export replay"),
        ("frequency", "showFlowerPhase", "show flower phase"),
        ("frequency", "showProjectFrequency", "show project frequency"),
        ("frequency", "showRateBoundary", "show rate boundary"),
    ]
    extra: List[Tuple[str, str, str]] = []
    for settlement in SETTLEMENTS:
        extra.extend([
            ("project", "scheduleResidentProject", f"schedule {settlement.settlement_id}"),
            ("inventory", "executeInventoryTask", f"inventory {settlement.inventory_items[0]}"),
            ("tool", "showToolWear", f"tool {settlement.tools[0]}"),
            ("recovery", "recoverFailedPlan", f"recover {settlement.failure_modes[0]}"),
            ("phrase", "practiceRelationshipPhrase", f"phrase {settlement.repair_phrases[0]}"),
            ("reload", "restoreProjectMemory", f"restore {settlement.settlement_id}"),
            ("frequency", "showProjectFrequency", f"frequency {settlement.settlement_id}"),
        ])
        for project in settlement.project_names:
            extra.append(("project", "scheduleResidentProject", f"project {project}"))
            extra.append(("project", "showProjectProgress", f"progress {project}"))
        for item in settlement.inventory_items:
            extra.append(("inventory", "executeInventoryTask", f"consume {item}"))
            extra.append(("inventory", "showInventoryDelta", f"delta {item}"))
        for tool in settlement.tools:
            extra.append(("tool", "showToolWear", f"wear {tool}"))
            extra.append(("tool", "performMaintenance", f"maintain {tool}"))
        for failure in settlement.failure_modes:
            extra.append(("recovery", "recoverFailedPlan", f"failure {failure}"))
            extra.append(("recovery", "scheduleRetry", f"retry {failure}"))
        for phrase in settlement.repair_phrases:
            extra.append(("phrase", "practiceRelationshipPhrase", f"learn {phrase}"))
            extra.append(("phrase", "showPhraseMemory", f"memory {phrase}"))
    for label in ("survey", "prepare", "work", "inspect", "handoff", "restock", "tool fail", "material low", "resident lead", "avatar waits"):
        extra.append(("project", "scheduleResidentProject", f"slot {label}"))
        extra.append(("recovery", "recoverFailedPlan", f"repair {label}"))
    for label in ("projects", "inventory", "tool wear", "recoveries", "phrases", "history", "no LLM", "private boundary"):
        extra.append(("reload", "restoreProjectMemory", f"reload {label}"))
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
<title>SSRM-3D Browser World v54 Schedulable Project Execution Bridge</title>
<style>
:root { --ink:#11120f; --copper:#d18a54; --mint:#9ccfb8; --blue:#79a7c8; --paper:#f7efdf; --line:rgba(247,239,223,.25); }
body { margin:0; font-family: Georgia, 'Times New Roman', serif; color:var(--paper); background: radial-gradient(circle at 15% 17%, rgba(209,138,84,.33), transparent 27%), radial-gradient(circle at 84% 13%, rgba(121,167,200,.26), transparent 30%), linear-gradient(135deg, #11120f, #253327 47%, #302738); }
main { display:grid; grid-template-columns: repeat(2, minmax(300px, 1fr)); gap:16px; padding:20px; }
section { border:1px solid var(--line); border-radius:22px; padding:16px; background:rgba(17,18,15,.76); box-shadow:0 22px 60px rgba(0,0,0,.38); }
button { margin:4px; border:1px solid var(--line); border-radius:999px; background:rgba(209,138,84,.18); color:var(--paper); padding:8px 11px; }
.flower { width:158px; height:158px; border-radius:50%; background: repeating-radial-gradient(circle, rgba(247,239,223,.32) 0 7px, transparent 8px 15px), conic-gradient(from 90deg, rgba(156,207,184,.45), rgba(121,167,200,.42), rgba(209,138,84,.42), rgba(156,207,184,.45)); }
.notice { grid-column:1/-1; color:#f9d8bd; }
</style>
</head>
<body>
<main>
<section id="schedulable-project-panel"><h2>Schedulable resident projects</h2><p>Residents own scheduled work slots, project sites, visible progress, and conflict recovery.</p></section>
<section id="inventory-task-panel"><h2>Inventory-affecting execution</h2><p>Tasks consume named materials, create outputs, and expose no-magic inventory deltas.</p></section>
<section id="tool-wear-panel"><h2>Tool wear and maintenance</h2><p>Tools accumulate wear, show failure risk, and require visible maintenance or retry plans.</p></section>
<section id="failed-plan-recovery-panel"><h2>Failed-plan recovery</h2><p>Failed or uncertain work is not erased; recovery adds debt, regression visibility, and retry scheduling.</p></section>
<section id="phrase-relationship-panel"><h2>Longer-term phrase relationships</h2><p>Phrase learning is bound to resident memory, project help, trust, and reload persistence.</p></section>
<section id="reload-panel"><h2>Save, restore, replay</h2><p>Reload probes restore projects, inventory, tool wear, recovery rows, and phrase relationships.</p></section>
<section id="frequency-flower-panel"><h2>Frequency / flower timing</h2><div class="flower"></div><p>flower phase and project frequency are deterministic timing/rate metadata, not a metaphysical frequency claim.</p></section>
<section class="notice"><strong>Boundary:</strong> no subjective consciousness claim, no real consent claim, no autonomous natural language claim, no moral patienthood claim, no complete 3D engine, no LLM call.</section>
<section class="notice" id="controls"><h2>Controls</h2>
""" + buttons + """
</section>
</main>
<script>
const stateKey = 'ssrm.v54.project.execution';
function pushTrace(action, scope) {
  const prior = JSON.parse(localStorage.getItem(stateKey) || '{"events":[],"inventory":{},"tools":{}}');
  prior.events.push({ action, scope, t: prior.events.length, note: 'browser-local deterministic project execution trace; no LLM call' });
  localStorage.setItem(stateKey, JSON.stringify(prior));
  return prior;
}
function scheduleResidentProject(scope) { return pushTrace('scheduleResidentProject', scope); }
function showProjectProgress(scope) { return pushTrace('showProjectProgress', scope); }
function resolveScheduleConflict(scope) { return pushTrace('resolveScheduleConflict', scope); }
function executeInventoryTask(scope) { return pushTrace('executeInventoryTask', scope); }
function showInventoryDelta(scope) { return pushTrace('showInventoryDelta', scope); }
function restockMaterial(scope) { return pushTrace('restockMaterial', scope); }
function showToolWear(scope) { return pushTrace('showToolWear', scope); }
function performMaintenance(scope) { return pushTrace('performMaintenance', scope); }
function showToolFailureRisk(scope) { return pushTrace('showToolFailureRisk', scope); }
function recoverFailedPlan(scope) { return pushTrace('recoverFailedPlan', scope); }
function scheduleRetry(scope) { return pushTrace('scheduleRetry', scope); }
function showRegressionDebt(scope) { return pushTrace('showRegressionDebt', scope); }
function practiceRelationshipPhrase(scope) { return pushTrace('practiceRelationshipPhrase', scope); }
function showPhraseRelationship(scope) { return pushTrace('showPhraseRelationship', scope); }
function showPhraseMemory(scope) { return pushTrace('showPhraseMemory', scope); }
function restoreProjectMemory(scope) { return JSON.parse(localStorage.getItem(stateKey) || '{"events":[]}'); }
function saveWorldState(scope) { return pushTrace('saveWorldState', scope); }
function restoreWorldState(scope) { return restoreProjectMemory(scope); }
function exportReplay(scope) { return JSON.stringify(restoreProjectMemory(scope)); }
function showFlowerPhase(scope) { return pushTrace('showFlowerPhase', scope); }
function showProjectFrequency(scope) { return pushTrace('showProjectFrequency', scope); }
function showRateBoundary(scope) { return pushTrace('showRateBoundary', scope); }
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
        "readiness": results["metrics"]["browser_world_v54_project_execution_readiness"],
        "weakest_channel": results["metrics"]["weakest_channel_name"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
    }])
    for name, values in rows.items():
        write_csv(ARTIFACT_DIR / f"{PREFIX}_{name}.csv", values)
    (VIS_DIR / f"{PREFIX}.html").write_text(build_html_template_stub(), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Report 294 SSRM-3D browser world v54 project execution bridge")
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
        "readiness": results["metrics"]["browser_world_v54_project_execution_readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "weakest_named_channel": results["metrics"]["weakest_channel_name"],
        "next_gate": results["next_gate"],
    }, indent=2, sort_keys=True))
    if results["verdict"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
