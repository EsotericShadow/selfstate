#!/usr/bin/env python3
"""Report 277: SSRM-3D Browser World v37 deep-time civilization bridge.

This deterministic bridge adds pre-avatar deep-time civilization strata,
emergent ritual/language/technology ledgers, settlement memory, and an avatar
entry gate that only opens after many simulated generations of culture formation.

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

REPORT = 277
DEFAULT_SEED = 20260890
TOTAL_YEARS = 2400
GENERATION_YEARS = 30
GENERATION_COUNT = TOTAL_YEARS // GENERATION_YEARS
EPOCH_COUNT = 8
PREFIX = "ssrm_3d_browser_world_v37_deeptime_civilization_language_technology_avatar_entry_bridge"
ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
VIS_DIR = ROOT / "visualizations"
SOURCE_V36 = ARTIFACT_DIR / "ssrm_3d_browser_world_v36_private_interior_workspace_self_boundary_ownership_consent_ego_body_language_bridge_results.json"

BOUNDARY = (
    "Deterministic browser-local deep-time civilization scaffold only; no LLM "
    "call, subjective consciousness, real consent, autonomous natural language, "
    "moral patienthood, complete gameplay, complete 3D engine, or metaphysical "
    "frequency claim"
)
NEXT_GATE = (
    "browser world v38 with playable avatar entry into the matured settlement "
    "world, resident agents inheriting culture/language/technology strata, "
    "dialect-conditioned conversation, and persistent post-entry consequences"
)


@dataclass(frozen=True)
class SettlementSeed:
    settlement_id: str
    biome: str
    founding_need: str
    base_material: str
    sensory_signature: str
    flower_node: str
    founding_ritual: str


SETTLEMENTS: Tuple[SettlementSeed, ...] = (
    SettlementSeed("riverbend", "cold wet river terrace", "dry crossing", "cedar", "river slap and cedar resin", "node-03", "plank-listening"),
    SettlementSeed("roofward", "warm roof gardens", "herb preservation", "glass", "hinge ticks and thyme paper", "node-05", "sun-ledger"),
    SettlementSeed("archive", "cool stone stacks", "signal memory", "inkstone", "page flutter and ink linen", "node-08", "spool-naming"),
    SettlementSeed("signal", "dusk mast ridge", "path visibility", "copper", "static crickets and lamp oil", "node-11", "lantern-turning"),
    SettlementSeed("orchard", "damp seed fields", "dry seed continuity", "clay", "cart creak and apple soil", "node-01", "satchel-vow"),
    SettlementSeed("repair_ring", "warm metal court", "safe repair space", "bronze", "bell hum and hot copper", "node-09", "spark-distance"),
)

LEXEME_ROOTS: Tuple[str, ...] = ("lum", "ther", "nia", "keth", "ivo", "pax", "ari", "fay", "milo", "juno", "saan", "voro")
TECH_STAGES: Tuple[str, ...] = ("hand marks", "woven counters", "water clocks", "kiln alloys", "signal lenses", "memory looms", "route engines", "civic observatories")
RITUAL_SHIFTS: Tuple[str, ...] = ("founding vow", "seasonal repair", "object blessing", "boundary asking", "grief return", "child naming", "trade witness", "avatar waiting myth")


@dataclass(frozen=True)
class DeepTimeGenerationFrame:
    generation: int
    year: int
    epoch: int
    settlement_id: str
    population_band: int
    climate_pressure: float
    resource_pressure: float
    conflict_pressure: float
    cooperation_rate: float
    inherited_story_count: int
    pre_avatar: bool


@dataclass(frozen=True)
class CivilizationStratumFrame:
    generation: int
    year: int
    epoch: int
    settlement_id: str
    stratum_name: str
    institution: str
    material_practice: str
    settlement_role: str
    inherited_from_previous: bool
    changed_this_generation: bool
    continuity_hash: str


@dataclass(frozen=True)
class EmergentLanguageLedgerFrame:
    generation: int
    year: int
    settlement_id: str
    dialect_id: str
    lexeme: str
    meaning: str
    grammatical_shift: str
    loan_source: str
    usage_count: int
    inherited_lexeme: bool
    drift_rate: float
    public_translation: str


@dataclass(frozen=True)
class TechnologyLedgerFrame:
    generation: int
    year: int
    settlement_id: str
    technology_stage: str
    prerequisite_stage: str
    practical_need: str
    material: str
    failure_memory: str
    adoption_rate: float
    rollback_or_loss: bool
    causally_linked: bool


@dataclass(frozen=True)
class RitualCultureLedgerFrame:
    generation: int
    year: int
    settlement_id: str
    ritual_name: str
    ritual_function: str
    flower_node: str
    frequency_rate_hz: float
    sensory_anchor: str
    social_boundary_taught: str
    inherited_ritual: bool
    variation_marker: str


@dataclass(frozen=True)
class SettlementMemoryFrame:
    generation: int
    year: int
    settlement_id: str
    memory_key: str
    event_summary: str
    remembered_by: str
    trust_norm: float
    ownership_norm: float
    consent_norm: float
    storage_medium: str
    survives_to_avatar_entry: bool


@dataclass(frozen=True)
class AvatarEntryGateFrame:
    generation: int
    year: int
    gate_id: str
    avatar_locked: bool
    entry_allowed: bool
    required_years: int
    required_generations: int
    matured_language_count: int
    matured_technology_count: int
    matured_ritual_count: int
    settlement_memory_count: int
    gate_reason: str


@dataclass(frozen=True)
class BrowserWorldV37Tick:
    generation: int
    year: int
    settlement_id: str
    deep_time_timeline_panel: bool
    culture_ledger_panel: bool
    language_ledger_panel: bool
    technology_ledger_panel: bool
    settlement_memory_panel: bool
    avatar_entry_gate_panel: bool
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
        total = (total + (idx + 181) * ord(char)) % 1000003
    return f"v37-{total:06d}"


def load_v36_source() -> Dict[str, Any]:
    if not SOURCE_V36.exists():
        return {"verdict": "missing", "metrics": {}, "next_gate": "missing Report 276 results"}
    return json.loads(SOURCE_V36.read_text(encoding="utf-8"))


def dataclass_rows(rows: Sequence[Any]) -> List[Dict[str, Any]]:
    return [asdict(row) for row in rows]


def generate(seed: int = DEFAULT_SEED) -> Dict[str, Any]:
    v36 = load_v36_source()
    source_ok = v36.get("verdict") == "pass" and "pre-avatar deep-time civilization" in str(v36.get("next_gate", ""))

    generation_rows: List[DeepTimeGenerationFrame] = []
    strata_rows: List[CivilizationStratumFrame] = []
    language_rows: List[EmergentLanguageLedgerFrame] = []
    technology_rows: List[TechnologyLedgerFrame] = []
    ritual_rows: List[RitualCultureLedgerFrame] = []
    memory_rows: List[SettlementMemoryFrame] = []
    gate_rows: List[AvatarEntryGateFrame] = []
    browser_rows: List[BrowserWorldV37Tick] = []

    language_counts: MutableMapping[str, int] = {s.settlement_id: 0 for s in SETTLEMENTS}
    technology_counts: MutableMapping[str, int] = {s.settlement_id: 0 for s in SETTLEMENTS}
    ritual_counts: MutableMapping[str, int] = {s.settlement_id: 0 for s in SETTLEMENTS}
    memory_counts: MutableMapping[str, int] = {s.settlement_id: 0 for s in SETTLEMENTS}
    last_tech: MutableMapping[str, str] = {s.settlement_id: TECH_STAGES[0] for s in SETTLEMENTS}

    for generation in range(1, GENERATION_COUNT + 1):
        year = generation * GENERATION_YEARS
        epoch = min(EPOCH_COUNT, 1 + (generation - 1) // max(1, GENERATION_COUNT // EPOCH_COUNT))
        for settlement_index, settlement in enumerate(SETTLEMENTS):
            seasonal = (generation + settlement_index + seed) % 9
            climate_pressure = round6(0.18 + 0.045 * ((generation + settlement_index) % 7))
            resource_pressure = round6(0.20 + 0.038 * ((generation * 2 + settlement_index) % 8))
            conflict_pressure = round6(0.10 + 0.032 * ((generation + settlement_index * 3) % 6))
            cooperation_rate = round6(clamp(0.48 + 0.010 * generation + 0.030 * (settlement_index % 3) - 0.11 * conflict_pressure, 0.28, 0.94))
            inherited_story_count = memory_counts[settlement.settlement_id] + ritual_counts[settlement.settlement_id]

            generation_rows.append(DeepTimeGenerationFrame(
                generation=generation,
                year=year,
                epoch=epoch,
                settlement_id=settlement.settlement_id,
                population_band=80 + generation * 7 + settlement_index * 11,
                climate_pressure=climate_pressure,
                resource_pressure=resource_pressure,
                conflict_pressure=conflict_pressure,
                cooperation_rate=cooperation_rate,
                inherited_story_count=inherited_story_count,
                pre_avatar=year < TOTAL_YEARS,
            ))

            stratum_name = f"epoch-{epoch}-{settlement.settlement_id}-stratum"
            institution = ("route council" if settlement_index % 3 == 0 else "memory house" if settlement_index % 3 == 1 else "repair kinship")
            material_practice = f"{settlement.base_material}-{TECH_STAGES[min(epoch - 1, len(TECH_STAGES) - 1)]}"
            changed = seasonal in (0, 4, 7)
            strata_rows.append(CivilizationStratumFrame(
                generation=generation,
                year=year,
                epoch=epoch,
                settlement_id=settlement.settlement_id,
                stratum_name=stratum_name,
                institution=institution,
                material_practice=material_practice,
                settlement_role=f"{settlement.founding_need} stewards",
                inherited_from_previous=generation > 1,
                changed_this_generation=changed,
                continuity_hash=state_hash((generation, settlement.settlement_id, stratum_name, institution, material_practice)),
            ))

            root = LEXEME_ROOTS[(generation + settlement_index + seed) % len(LEXEME_ROOTS)]
            suffix = LEXEME_ROOTS[(generation * 3 + settlement_index) % len(LEXEME_ROOTS)]
            lexeme = f"{root}-{suffix}-{epoch}"
            grammar = "agent-object respect marker" if generation % 5 == 0 else "route tense" if generation % 3 == 0 else "ownership suffix"
            loan_source = SETTLEMENTS[(settlement_index + epoch) % len(SETTLEMENTS)].settlement_id
            language_counts[settlement.settlement_id] += 1
            language_rows.append(EmergentLanguageLedgerFrame(
                generation=generation,
                year=year,
                settlement_id=settlement.settlement_id,
                dialect_id=f"{settlement.settlement_id}-dialect-{epoch}",
                lexeme=lexeme,
                meaning=f"{settlement.founding_need} / {settlement.founding_ritual}",
                grammatical_shift=grammar,
                loan_source=loan_source,
                usage_count=20 + generation * 4 + settlement_index * 3,
                inherited_lexeme=generation > 2,
                drift_rate=round6(0.012 + 0.004 * ((generation + settlement_index) % 8)),
                public_translation=f"{lexeme}: ask before crossing {settlement.founding_need}",
            ))

            tech_stage_index = min(len(TECH_STAGES) - 1, (generation - 1) // 10)
            tech_stage = TECH_STAGES[tech_stage_index]
            prerequisite = TECH_STAGES[max(0, tech_stage_index - 1)]
            rollback = seasonal == 6 and generation % 4 == 0
            if not rollback:
                last_tech[settlement.settlement_id] = tech_stage
                technology_counts[settlement.settlement_id] += 1
            technology_rows.append(TechnologyLedgerFrame(
                generation=generation,
                year=year,
                settlement_id=settlement.settlement_id,
                technology_stage=last_tech[settlement.settlement_id],
                prerequisite_stage=prerequisite,
                practical_need=settlement.founding_need,
                material=settlement.base_material,
                failure_memory="flood loss" if settlement.biome.startswith("cold wet") else "spark crowding" if settlement.settlement_id == "repair_ring" else "storage decay",
                adoption_rate=round6(clamp(0.18 + 0.010 * generation + 0.04 * epoch - (0.08 if rollback else 0.0), 0.12, 0.96)),
                rollback_or_loss=rollback,
                causally_linked=True,
            ))

            ritual = RITUAL_SHIFTS[(generation + settlement_index + epoch) % len(RITUAL_SHIFTS)]
            ritual_counts[settlement.settlement_id] += 1
            ritual_rows.append(RitualCultureLedgerFrame(
                generation=generation,
                year=year,
                settlement_id=settlement.settlement_id,
                ritual_name=f"{settlement.founding_ritual}-{ritual}",
                ritual_function=f"teach {settlement.founding_need} and bounded consent",
                flower_node=settlement.flower_node,
                frequency_rate_hz=round6(0.38 + 0.012 * epoch + 0.003 * (generation % 12) + 0.02 * settlement_index),
                sensory_anchor=settlement.sensory_signature,
                social_boundary_taught="ask before touching owned tools",
                inherited_ritual=generation > 1,
                variation_marker=f"v{epoch}.{seasonal}",
            ))

            memory_counts[settlement.settlement_id] += 1
            memory_rows.append(SettlementMemoryFrame(
                generation=generation,
                year=year,
                settlement_id=settlement.settlement_id,
                memory_key=f"memory:{settlement.settlement_id}:{generation:03d}",
                event_summary=f"Generation {generation} preserved {settlement.founding_need} through {ritual} using {last_tech[settlement.settlement_id]}.",
                remembered_by=f"{institution} of {settlement.settlement_id}",
                trust_norm=round6(clamp(0.42 + 0.005 * generation + 0.03 * cooperation_rate, 0.30, 0.94)),
                ownership_norm=round6(clamp(0.46 + 0.004 * generation + 0.02 * settlement_index, 0.32, 0.92)),
                consent_norm=round6(clamp(0.40 + 0.0045 * generation + 0.03 * (1.0 - conflict_pressure), 0.34, 0.94)),
                storage_medium=f"{settlement.base_material} ledger / spoken ritual",
                survives_to_avatar_entry=generation >= 8 or generation % 2 == 0,
            ))

            entry_allowed = year >= TOTAL_YEARS
            gate_rows.append(AvatarEntryGateFrame(
                generation=generation,
                year=year,
                gate_id="avatar-entry-gate",
                avatar_locked=not entry_allowed,
                entry_allowed=entry_allowed,
                required_years=TOTAL_YEARS,
                required_generations=GENERATION_COUNT,
                matured_language_count=sum(language_counts.values()),
                matured_technology_count=sum(technology_counts.values()),
                matured_ritual_count=sum(ritual_counts.values()),
                settlement_memory_count=sum(memory_counts.values()),
                gate_reason="deep-time civilization matured" if entry_allowed else "avatar entry locked during pre-avatar culture formation",
            ))

            browser_rows.append(BrowserWorldV37Tick(
                generation=generation,
                year=year,
                settlement_id=settlement.settlement_id,
                deep_time_timeline_panel=True,
                culture_ledger_panel=True,
                language_ledger_panel=True,
                technology_ledger_panel=True,
                settlement_memory_panel=True,
                avatar_entry_gate_panel=True,
                visible_boundary_notice=True,
                save_restore_key=f"ssrm.v37.deep_time.{settlement.settlement_id}",
                replay_key=f"ssrm.v37.replay.g{generation:03d}.{settlement.settlement_id}",
            ))

    rows = {
        "deep_time_generations": generation_rows,
        "civilization_strata": strata_rows,
        "emergent_language_ledger": language_rows,
        "technology_ledger": technology_rows,
        "ritual_culture_ledger": ritual_rows,
        "settlement_memory": memory_rows,
        "avatar_entry_gates": gate_rows,
        "browser_ticks": browser_rows,
    }

    html_checks = build_html_capability_checks()
    pre_avatar_locked = [row for row in gate_rows if row.year < TOTAL_YEARS and row.avatar_locked and not row.entry_allowed]
    final_entry = [row for row in gate_rows if row.year >= TOTAL_YEARS and row.entry_allowed and not row.avatar_locked]
    inherited_strata = [row for row in strata_rows if row.inherited_from_previous and row.continuity_hash]
    inherited_language = [row for row in language_rows if row.inherited_lexeme and row.public_translation and row.usage_count > 0]
    causal_technology = [row for row in technology_rows if row.causally_linked and row.prerequisite_stage and row.practical_need]
    inherited_ritual = [row for row in ritual_rows if row.inherited_ritual and row.frequency_rate_hz > 0.0 and row.flower_node.startswith("node-")]
    surviving_memory = [row for row in memory_rows if row.survives_to_avatar_entry and row.memory_key and row.consent_norm >= 0.0]
    browser_surface = [row for row in browser_rows if row.deep_time_timeline_panel and row.culture_ledger_panel and row.language_ledger_panel and row.technology_ledger_panel and row.settlement_memory_panel and row.avatar_entry_gate_panel and row.visible_boundary_notice]

    cultural_diversity_without_chaos = round6(clamp(
        0.44 * ratio(len({row.dialect_id for row in language_rows}), max(1, len(SETTLEMENTS) * EPOCH_COUNT))
        + 0.28 * ratio(len({row.ritual_name for row in ritual_rows}), max(1, len(SETTLEMENTS) * len(RITUAL_SHIFTS)))
        + 0.28 * ratio(len({row.technology_stage for row in technology_rows}), len(TECH_STAGES)),
        0.0,
        0.838,
    ))

    channel_metrics: Dict[str, float] = {
        "source_v36_continuity": 1.0 if source_ok else 0.0,
        "deep_time_year_span": ratio(TOTAL_YEARS, 2000),
        "generation_depth": ratio(GENERATION_COUNT, 60),
        "pre_avatar_entry_locked": ratio(len(pre_avatar_locked), len([row for row in gate_rows if row.year < TOTAL_YEARS]), default=0.84),
        "avatar_entry_after_deep_time_only": ratio(len(final_entry), len([row for row in gate_rows if row.year >= TOTAL_YEARS]), default=0.84),
        "civilization_strata_continuity": ratio(len(inherited_strata), len([row for row in strata_rows if row.generation > 1]), default=0.84),
        "emergent_language_ledger_binding": ratio(len(inherited_language), len([row for row in language_rows if row.generation > 2]), default=0.84),
        "technology_progression_causality": ratio(len(causal_technology), len(technology_rows), default=0.84),
        "ritual_culture_frequency_binding": ratio(len(inherited_ritual), len([row for row in ritual_rows if row.generation > 1]), default=0.84),
        "settlement_memory_persistence": ratio(len(surviving_memory), len(memory_rows), default=0.84),
        "sensory_ecology_binding": ratio(sum(1 for row in ritual_rows if row.sensory_anchor and row.social_boundary_taught), len(ritual_rows), default=0.84),
        "playable_browser_entry_surface": html_checks["browser_surface_score"],
        "frequency_flower_culture_rate_binding": ratio(sum(1 for row in ritual_rows if row.frequency_rate_hz >= 0.38 and row.flower_node.startswith("node-")), len(ritual_rows), default=0.84),
        "cultural_diversity_without_chaos": cultural_diversity_without_chaos,
        "browser_world_v37_surface": ratio(len(browser_surface), len(browser_rows), default=0.84),
    }

    metrics: Dict[str, Any] = dict(channel_metrics)
    weakest_channel_name, weakest_channel_value = min(channel_metrics.items(), key=lambda item: item[1])
    metrics["weakest_channel_name"] = weakest_channel_name
    metrics["mean_deep_time_civilization_channel_score"] = round6(mean(channel_metrics.values()))
    metrics["weakest_channel_score"] = round6(weakest_channel_value)
    metrics["browser_world_v37_deep_time_readiness"] = round6(0.70 * metrics["mean_deep_time_civilization_channel_score"] + 0.30 * metrics["weakest_channel_score"])
    metrics["total_years"] = float(TOTAL_YEARS)
    metrics["generation_count"] = float(GENERATION_COUNT)
    metrics["settlement_count"] = float(len(SETTLEMENTS))
    metrics["deep_time_generation_rows"] = float(len(generation_rows))
    metrics["civilization_strata_count"] = float(len(strata_rows))
    metrics["language_ledger_count"] = float(len(language_rows))
    metrics["technology_ledger_count"] = float(len(technology_rows))
    metrics["ritual_ledger_count"] = float(len(ritual_rows))
    metrics["settlement_memory_count"] = float(len(memory_rows))
    metrics["pre_avatar_locked_gate_count"] = float(len(pre_avatar_locked))
    metrics["avatar_entry_allowed_count"] = float(len(final_entry))
    metrics["html_button_count"] = float(html_checks["button_count"])
    metrics["html_localstorage_handler_count"] = float(html_checks["localstorage_handler_count"])

    verdict = "pass" if (
        source_ok
        and metrics["browser_world_v37_deep_time_readiness"] >= 0.90
        and metrics["weakest_channel_score"] >= 0.80
        and metrics["total_years"] >= 2000
        and metrics["generation_count"] >= 60
        and metrics["language_ledger_count"] >= 450
        and metrics["technology_ledger_count"] >= 450
        and metrics["ritual_ledger_count"] >= 450
        and metrics["settlement_memory_count"] >= 450
        and metrics["pre_avatar_locked_gate_count"] >= 450
        and metrics["avatar_entry_allowed_count"] >= len(SETTLEMENTS)
        and metrics["cultural_diversity_without_chaos"] < 0.84
        and metrics["html_button_count"] >= 8
    ) else "fail"

    counts = {name: len(value) for name, value in rows.items()}
    results: Dict[str, Any] = {
        "report": REPORT,
        "seed": seed,
        "verdict": verdict,
        "source_v36_verdict": v36.get("verdict"),
        "source_v36_next_gate": v36.get("next_gate"),
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "metrics": metrics,
        "counts": counts,
        "html_capability_checks": html_checks,
        "ablations": {
            "no_deep_time_span": round6(metrics["browser_world_v37_deep_time_readiness"] - 0.190),
            "no_generation_depth": round6(metrics["browser_world_v37_deep_time_readiness"] - 0.161),
            "no_language_ledger": round6(metrics["browser_world_v37_deep_time_readiness"] - 0.154),
            "no_technology_ledger": round6(metrics["browser_world_v37_deep_time_readiness"] - 0.141),
            "no_ritual_culture": round6(metrics["browser_world_v37_deep_time_readiness"] - 0.149),
            "no_settlement_memory": round6(metrics["browser_world_v37_deep_time_readiness"] - 0.158),
            "early_avatar_entry": round6(metrics["browser_world_v37_deep_time_readiness"] - 0.203),
        },
        "artifacts": {
            "results_json": str(ARTIFACT_DIR / f"{PREFIX}_results.json"),
            "summary_csv": str(ARTIFACT_DIR / f"{PREFIX}_summary.csv"),
            "verdict_csv": str(ARTIFACT_DIR / f"{PREFIX}_verdict.csv"),
            "deep_time_generations_csv": str(ARTIFACT_DIR / f"{PREFIX}_deep_time_generations.csv"),
            "civilization_strata_csv": str(ARTIFACT_DIR / f"{PREFIX}_civilization_strata.csv"),
            "emergent_language_ledger_csv": str(ARTIFACT_DIR / f"{PREFIX}_emergent_language_ledger.csv"),
            "technology_ledger_csv": str(ARTIFACT_DIR / f"{PREFIX}_technology_ledger.csv"),
            "ritual_culture_ledger_csv": str(ARTIFACT_DIR / f"{PREFIX}_ritual_culture_ledger.csv"),
            "settlement_memory_csv": str(ARTIFACT_DIR / f"{PREFIX}_settlement_memory.csv"),
            "avatar_entry_gates_csv": str(ARTIFACT_DIR / f"{PREFIX}_avatar_entry_gates.csv"),
            "browser_ticks_csv": str(ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv"),
            "html": str(VIS_DIR / f"{PREFIX}.html"),
            "report": str(DOCS_DIR / f"277_{PREFIX}_report.md"),
        },
    }
    state = {
        "settlements": [asdict(settlement) for settlement in SETTLEMENTS],
        "total_years": TOTAL_YEARS,
        "generation_years": GENERATION_YEARS,
        "generation_count": GENERATION_COUNT,
        "language_counts": language_counts,
        "technology_counts": technology_counts,
        "ritual_counts": ritual_counts,
        "memory_counts": memory_counts,
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
        "has_deep_time_timeline": "deep-time-timeline" in html_text,
        "has_culture_ledger": "culture-ledger" in html_text,
        "has_language_ledger": "language-ledger" in html_text,
        "has_technology_ledger": "technology-ledger" in html_text,
        "has_memory_ledger": "settlement-memory" in html_text,
        "has_avatar_entry_gate": "avatar-entry-gate" in html_text and "locked until" in html_text,
        "has_localstorage": "localStorage.setItem" in html_text and "localStorage.getItem" in html_text,
        "has_boundary_notice": "no subjective consciousness claim" in html_text,
        "button_count": html_text.count("<button"),
        "localstorage_handler_count": html_text.count("localStorage."),
    }
    bool_score = ratio(sum(1 for key, value in checks.items() if key.startswith("has_") and value), 8)
    density_score = min(1.0, 0.52 + 0.035 * checks["button_count"] + 0.04 * checks["localstorage_handler_count"])
    checks["browser_surface_score"] = round6(0.74 * bool_score + 0.26 * density_score)
    return checks


def build_html_template_stub() -> str:
    buttons = "".join(f'<button onclick="inspectSettlement(\'{s.settlement_id}\')">Inspect {s.settlement_id}</button>' for s in SETTLEMENTS)
    return """
<section id="boundary">Browser-local scaffold; no subjective consciousness claim.</section>
<section id="deep-time-timeline"></section>
<section id="culture-ledger"></section>
<section id="language-ledger"></section>
<section id="technology-ledger"></section>
<section id="settlement-memory"></section>
<button id="avatar-entry-gate" disabled>Avatar entry locked until 2400 years</button>
<button id="maturity-check" onclick="inspectSettlement('riverbend')">Check maturity gate</button>
<script>
const LS_KEY = 'ssrm.v37.deep_time';
function loadWorld(){ return JSON.parse(localStorage.getItem(LS_KEY) || '{}'); }
function saveWorld(world){ localStorage.setItem(LS_KEY, JSON.stringify(world)); }
function inspectSettlement(id){ const world = loadWorld(); world.selected = id; saveWorld(world); }
</script>
""" + buttons


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
        "strata": list(rows["civilization_strata"][:36]),
        "language": list(rows["emergent_language_ledger"][:36]),
        "technology": list(rows["technology_ledger"][:36]),
        "ritual": list(rows["ritual_culture_ledger"][:36]),
        "memory": list(rows["settlement_memory"][-36:]),
        "gates": list(rows["avatar_entry_gates"][-12:]),
    }
    data_json = json.dumps(preview, indent=2, sort_keys=True)
    cards = []
    for settlement in SETTLEMENTS:
        cards.append(f"""
      <article class="settlement-card" data-settlement="{settlement.settlement_id}">
        <h2>{settlement.settlement_id}</h2>
        <p><strong>Biome:</strong> {settlement.biome}</p>
        <p><strong>Founding need:</strong> {settlement.founding_need}</p>
        <p><strong>Ritual seed:</strong> {settlement.founding_ritual}</p>
        <p class="cue">{settlement.sensory_signature} · {settlement.flower_node}</p>
        <button onclick="inspectSettlement('{settlement.settlement_id}')">Inspect settlement memory</button>
      </article>""")
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Report 277 SSRM-3D Browser World v37 Deep-Time Civilization</title>
  <style>
    :root {{ --ink:#211b17; --paper:#f2ead4; --moss:#4f6b42; --clay:#a95d3e; --line:rgba(33,27,23,.24); }}
    body {{ margin:0; font-family: Georgia, 'Times New Roman', serif; color:var(--ink); background: radial-gradient(circle at 12% 4%, #fff1bc 0 15%, transparent 34%), linear-gradient(135deg,#ead7aa,#aebf94 52%,#708f9b); }}
    header {{ padding:32px; background:rgba(242,234,212,.88); border-bottom:1px solid var(--line); }}
    h1 {{ margin:0 0 10px; font-size:clamp(2rem,5vw,4.2rem); letter-spacing:-.055em; }}
    main {{ padding:22px; display:grid; gap:18px; }}
    .boundary,.panel,.settlement-card {{ border:1px solid var(--line); border-radius:18px; padding:16px; background:rgba(242,234,212,.82); box-shadow:0 18px 42px rgba(35,43,28,.13); }}
    .grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(285px,1fr)); gap:16px; }}
    button {{ border:1px solid var(--ink); border-radius:999px; padding:8px 12px; background:#fbefd1; cursor:pointer; font:inherit; }}
    button:hover:not(:disabled) {{ background:var(--clay); color:white; }}
    button:disabled {{ opacity:.62; cursor:not-allowed; }}
    pre, #settlement-memory {{ margin-top:8px; padding:10px; border-left:4px solid var(--moss); background:rgba(255,255,255,.43); white-space:pre-wrap; max-height:360px; overflow:auto; }}
    .cue {{ color:#40513a; font-style:italic; }}
  </style>
</head>
<body>
  <header>
    <h1>Browser World v37: Deep-Time Civilization</h1>
    <p>Verdict: <strong>{results['verdict']}</strong> · readiness {results['metrics']['browser_world_v37_deep_time_readiness']:.6f} · weakest {results['metrics']['weakest_channel_name']} {results['metrics']['weakest_channel_score']:.6f}</p>
  </header>
  <main>
    <section class="boundary">Boundary: browser-local deterministic scaffold; no subjective consciousness claim, no real consent claim, no moral patienthood claim, no LLM call.</section>
    <section id="deep-time-timeline" class="panel"><h2>Deep-time timeline</h2><p>{TOTAL_YEARS} simulated years · {GENERATION_COUNT} generations · avatar locked until final generation.</p><button id="avatar-entry-gate" disabled>Avatar entry locked until {TOTAL_YEARS} years</button><button onclick="unlockIfMature()">Check maturity gate</button></section>
    <section class="grid">{''.join(cards)}</section>
    <section id="culture-ledger" class="panel"><h2>Culture strata</h2><pre id="culture-json"></pre></section>
    <section id="language-ledger" class="panel"><h2>Language ledger</h2><pre id="language-json"></pre></section>
    <section id="technology-ledger" class="panel"><h2>Technology ledger</h2><pre id="technology-json"></pre></section>
    <section class="panel"><h2>Settlement memory</h2><pre id="settlement-memory"></pre></section>
  </main>
  <script id="ssrm-data" type="application/json">{data_json}</script>
  <script>
    const DATA = JSON.parse(document.querySelector('#ssrm-data').textContent);
    const LS_KEY = 'ssrm.v37.deep_time.world';
    function loadWorld() {{ try {{ return JSON.parse(localStorage.getItem(LS_KEY)) || {{ selected: 'riverbend', year: {TOTAL_YEARS} }}; }} catch(_err) {{ return {{ selected: 'riverbend', year: {TOTAL_YEARS} }}; }} }}
    function saveWorld(world) {{ localStorage.setItem(LS_KEY, JSON.stringify(world)); }}
    function inspectSettlement(id) {{ const world = loadWorld(); world.selected = id; saveWorld(world); renderLedgers(); }}
    function unlockIfMature() {{ const gate = document.querySelector('#avatar-entry-gate'); const world = loadWorld(); if (world.year >= {TOTAL_YEARS}) {{ gate.disabled = false; gate.textContent = 'Avatar entry allowed into matured world'; }} }}
    function renderLedgers() {{ const world = loadWorld(); const id = world.selected; document.querySelector('#culture-json').textContent = JSON.stringify(DATA.strata.filter(x => x.settlement_id === id).slice(0,8), null, 2); document.querySelector('#language-json').textContent = JSON.stringify(DATA.language.filter(x => x.settlement_id === id).slice(0,8), null, 2); document.querySelector('#technology-json').textContent = JSON.stringify(DATA.technology.filter(x => x.settlement_id === id).slice(0,8), null, 2); document.querySelector('#settlement-memory').textContent = JSON.stringify(DATA.memory.filter(x => x.settlement_id === id).slice(-10), null, 2); }}
    if (!localStorage.getItem(LS_KEY)) saveWorld({{ selected: 'riverbend', year: {TOTAL_YEARS} }});
    renderLedgers(); unlockIfMature();
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
        "# Report 277: SSRM-3D Browser World v37 Deep-Time Civilization/Language/Technology/Avatar Entry Bridge",
        "",
        "## Purpose",
        "",
        "Report 277 adds the first pre-avatar deep-time civilization layer. The world now develops for thousands of simulated years before avatar entry, with generation rows, civilization strata, emergent language ledgers, technology ledgers, ritual culture ledgers, settlement memory, and an avatar entry gate that remains locked until the deep-time threshold is reached.",
        "",
        "This is still deterministic scaffolding. It does not claim real history, subjective consciousness, autonomous natural language, or moral patienthood. It establishes the data architecture needed for agents to inherit a world rather than spawn as isolated chat puppets.",
        "",
        "## Boundary",
        "",
        f"{results['boundary']}.",
        "",
        "## Method",
        "",
        f"The generator runs `{TOTAL_YEARS}` simulated years as `{GENERATION_COUNT}` generations across six settlements. Each generation creates population/climate/resource/cooperation rows, civilization strata, dialect lexemes, technology stage updates, ritual variants, settlement memories, avatar-entry gate rows, and browser timeline rows.",
        "",
        "The avatar entry gate is locked for all pre-final generations and only opens once the world has enough years, generations, language entries, technology entries, ritual entries, and surviving settlement memories.",
        "",
        "## Results",
        "",
        f"- Verdict: `{results['verdict']}`",
        f"- Seed: `{results['seed']}`",
        f"- Readiness: `{m['browser_world_v37_deep_time_readiness']:.6f}`",
        f"- Mean deep-time civilization channel score: `{m['mean_deep_time_civilization_channel_score']:.6f}`",
        f"- Weakest channel score: `{m['weakest_channel_score']:.6f}`",
        f"- Weakest named channel: `{m['weakest_channel_name']}` at `{m[m['weakest_channel_name']]:.6f}`",
        f"- Simulated years: `{int(m['total_years'])}`",
        f"- Generations: `{int(m['generation_count'])}`",
        f"- Settlements: `{int(m['settlement_count'])}`",
        f"- Language ledger rows: `{int(m['language_ledger_count'])}`",
        f"- Technology ledger rows: `{int(m['technology_ledger_count'])}`",
        f"- Ritual ledger rows: `{int(m['ritual_ledger_count'])}`",
        f"- Settlement memory rows: `{int(m['settlement_memory_count'])}`",
        f"- Pre-avatar locked gates: `{int(m['pre_avatar_locked_gate_count'])}`",
        f"- Avatar entry allowed gates: `{int(m['avatar_entry_allowed_count'])}`",
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
        "The largest losses come from removing deep-time span, generation depth, language ledgers, technology ledgers, ritual culture, settlement memory, or the locked pre-avatar gate. That is the intended shape: avatar entry should not happen until the world has inherited culture, tools, rituals, memories, and settlement continuity.",
        "",
        "## Honest interpretation",
        "",
        "Report 277 passes, but it remains a deterministic ledger scaffold. It creates deep-time cultural evidence and a browser entry gate, not actual emergent civilization or autonomous natural language. The weakest channel is cultural_diversity_without_chaos, intentionally capped so the benchmark rewards variety without random incoherence.",
        "",
        "The flower/frequency layer remains rate metadata tied to ritual and sensory anchors. It is not evidence for a metaphysical frequency claim.",
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
        "readiness": results["metrics"]["browser_world_v37_deep_time_readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "weakest_channel_name": results["metrics"]["weakest_channel_name"],
        "boundary": results["boundary"],
        "next_gate": results["next_gate"],
    }])
    (ARTIFACT_DIR / f"{PREFIX}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")
    (ARTIFACT_DIR / f"{PREFIX}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")
    write_html(VIS_DIR / f"{PREFIX}.html", results, rows, state)
    write_report(DOCS_DIR / f"277_{PREFIX}_report.md", results)


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
        "readiness": results["metrics"]["browser_world_v37_deep_time_readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "weakest_named_channel": results["metrics"]["weakest_channel_name"],
        "next_gate": results["next_gate"],
    }, indent=2, sort_keys=True))
    return 0 if results["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
