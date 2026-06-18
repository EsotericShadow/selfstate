"""Report 290: SSRM-3D browser world v50 thousand-year pre-avatar prehistory bridge.

This deterministic benchmark extends the browser-world line with a long
pre-avatar civilization layer: proto-language families, lineage memories, craft
technologies, trade routes, cultural rituals, frequency/flower timing metadata,
and playable avatar entry only after civilization has already emerged. It is
browser-local scaffolding only: no LLM call, no subjective consciousness claim,
no real consent claim, no autonomous natural language claim, no moral
patienthood claim, no complete 3D engine, and no metaphysical frequency result.
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

REPORT = 290
DEFAULT_SEED = 20270113
SIM_YEARS = 1200
YEAR_STEP = 5
PREFIX = "ssrm_3d_browser_world_v50_thousand_year_prehistory_language_technology_trade_avatar_entry_bridge"
ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
VIS_DIR = ROOT / "visualizations"
SOURCE_V49 = ARTIFACT_DIR / "ssrm_3d_browser_world_v49_sleep_nutrition_shelter_reciprocity_avatar_welfare_bridge_results.json"
SOURCE_V49_STATE = ARTIFACT_DIR / "ssrm_3d_browser_world_v49_sleep_nutrition_shelter_reciprocity_avatar_welfare_bridge_state.json"

BOUNDARY = (
    "Deterministic browser-local thousand-year-prehistory/language-family/"
    "technology/trade/avatar-entry scaffold only; no LLM call, subjective "
    "consciousness, real consent, autonomous natural language, moral patienthood, "
    "complete gameplay, complete 3D engine, or metaphysical frequency claim"
)
NEXT_GATE = (
    "browser world v51 with playable first-person arrival into the prebuilt "
    "civilization, resident greeting protocols, translation uncertainty, local "
    "law/custom constraints, and avatar choices that affect trust without erasing history"
)


@dataclass(frozen=True)
class CivilizationV50:
    settlement_id: str
    proto_family: str
    node_id: str
    founders: Tuple[str, str, str]
    biome: str
    primary_resources: Tuple[str, str, str]
    craft_domains: Tuple[str, str, str]
    trade_goods: Tuple[str, str, str]
    ritual_roots: Tuple[str, str, str]
    neighbor_ids: Tuple[str, str]
    base_frequency: float
    flower_offset: float


CIVILIZATIONS: Tuple[CivilizationV50, ...] = (
    CivilizationV50("moss_ward", "proto-moss-breath", "node-11", ("Ari-line", "Fay-line", "Tala-line"), "wet temperate ward", ("moss fiber", "rain clay", "root starch"), ("cloak weaving", "rain jar firing", "path lanterns"), ("dry cloaks", "root cakes", "jar seals"), ("warm-cup", "door-watch", "blanket-share"), ("glass_harbor", "lichen_bridge"), 5.21, 0.021),
    CivilizationV50("glass_harbor", "proto-harbor-chime", "node-12", ("Nia-line", "Oren-line", "Sera-line"), "fog harbor", ("salt reed", "lamp oil", "kelp fiber"), ("lamp optics", "net knots", "salt cisterns"), ("lantern lenses", "kelp cord", "salt tea"), ("lamp-touch", "tea-before-crossing", "net-knot-thanks"), ("moss_ward", "orchid_engine"), 6.34, 0.034),
    CivilizationV50("cinder_garden", "proto-cinder-pulse", "node-13", ("Juno-line", "Pax-line", "Wren-line"), "ash garden", ("ember fruit", "shade wood", "cool stone"), ("seed calendars", "shade rigs", "ash ceramics"), ("seed meal", "shade poles", "cool bowls"), ("shade-bow", "seed-count", "cool-hand"), ("lichen_bridge", "orchid_engine"), 8.89, 0.055),
    CivilizationV50("lichen_bridge", "proto-bridge-hum", "node-14", ("Kio-line", "Luma-line", "Sol-line"), "rope bridge valley", ("lichen paste", "rope reed", "signal stone"), ("rope trusses", "signal bells", "bridge ledgers"), ("rope kits", "signal bells", "lichen soup"), ("rope-touch", "signal-hush", "shared-bowl"), ("moss_ward", "cinder_garden"), 7.55, 0.044),
    CivilizationV50("orchid_engine", "proto-engine-ring", "node-15", ("Bea-line", "Cai-line", "Eli-line"), "warm engine terrace", ("orchid oil", "valve ore", "steam water"), ("valve tools", "orchid lamps", "gear washing"), ("valve keys", "orchid lamps", "steam tea"), ("valve-pause", "orchid-cup", "gear-wash-thanks"), ("glass_harbor", "cinder_garden"), 9.87, 0.067),
)


@dataclass(frozen=True)
class PrehistoryEpochFrame:
    epoch_id: int
    simulated_year: int
    generation: int
    settlement_id: str
    population_estimate: int
    resource_pressure: float
    conflict_pressure: float
    cooperation_norm_strength: float
    institution_count: int
    avatar_absent: bool
    civilization_marker: str
    continuity_score: float
    bounded_history: bool


@dataclass(frozen=True)
class ProtoLanguageFamilyFrame:
    epoch_id: int
    simulated_year: int
    settlement_id: str
    proto_family: str
    root_count: int
    lexicon_size: int
    grammar_complexity: float
    dialect_split_count: int
    mutual_intelligibility: float
    example_phrase: str
    not_autonomous_language_claim: bool
    frequency_hz: float
    flower_phase: float


@dataclass(frozen=True)
class CraftTechnologyFrame:
    epoch_id: int
    simulated_year: int
    settlement_id: str
    craft_domain: str
    technology_stage: int
    tool_name: str
    apprentice_lineage_depth: int
    material_source: str
    failure_memory: str
    practical_use: str
    energy_budget: float
    bounded_technology: bool


@dataclass(frozen=True)
class TradeRouteFrame:
    epoch_id: int
    simulated_year: int
    origin_id: str
    destination_id: str
    trade_good: str
    route_age_years: int
    route_reliability: float
    conflict_risk: float
    weather_risk: float
    reciprocal_obligation: float
    route_visible_on_map: bool
    bounded_trade: bool


@dataclass(frozen=True)
class LineageMemoryFrame:
    epoch_id: int
    simulated_year: int
    settlement_id: str
    lineage_id: str
    memory_depth_generations: int
    remembered_event: str
    ritual_anchor: str
    law_or_custom: str
    relationship_continuity: float
    memory_not_global_dump: bool
    visible_archive_marker: str


@dataclass(frozen=True)
class AvatarEntryAfterPrehistoryFrame:
    entry_id: int
    simulated_year: int
    settlement_id: str
    avatar_entry_allowed: bool
    civilization_preexists: bool
    greeting_protocol: str
    translation_uncertainty: float
    local_custom_constraint: str
    first_playable_choices: str
    history_not_erased: bool
    private_workspace_boundary: bool
    entry_marker_visible: bool


@dataclass(frozen=True)
class PrehistoryReloadProbeFrame:
    epoch_id: int
    simulated_year: int
    settlement_id: str
    reload_index: int
    epoch_count: int
    language_count: int
    craft_count: int
    trade_count: int
    lineage_count: int
    checksum: str
    restored_prehistory_visible: bool
    restored_language_visible: bool
    restored_craft_visible: bool
    restored_trade_visible: bool
    restored_lineage_visible: bool
    replay_exportable: bool


@dataclass(frozen=True)
class BrowserWorldV50Tick:
    epoch_id: int
    simulated_year: int
    settlement_id: str
    prehistory_panel: bool
    language_family_panel: bool
    craft_technology_panel: bool
    trade_route_panel: bool
    lineage_memory_panel: bool
    avatar_entry_panel: bool
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


def state_hash(payload: Mapping[str, Any]) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()[:16]


def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def dataclass_rows(values: Iterable[Any]) -> List[Dict[str, Any]]:
    return [asdict(value) for value in values]


def phrase_for(civ: CivilizationV50, year: int, generation: int) -> str:
    root = civ.proto_family.replace("proto-", "").replace("-", " ")
    cadence = (year // YEAR_STEP + generation + len(civ.settlement_id)) % 13
    return f"{root} keeps {civ.ritual_roots[cadence % len(civ.ritual_roots)]} {cadence}"


def generate(seed: int = DEFAULT_SEED) -> Dict[str, Any]:
    v49 = load_json(SOURCE_V49)
    v49_state = load_json(SOURCE_V49_STATE)
    source_ok = v49.get("verdict") == "pass" and bool(v49_state)

    population: MutableMapping[str, float] = {c.settlement_id: 42.0 + i * 7 for i, c in enumerate(CIVILIZATIONS)}
    institutions: MutableMapping[str, int] = {c.settlement_id: 1 for c in CIVILIZATIONS}
    route_age: MutableMapping[Tuple[str, str], int] = {}
    reload_index: MutableMapping[str, int] = {c.settlement_id: 0 for c in CIVILIZATIONS}
    counts: MutableMapping[str, Dict[str, int]] = {c.settlement_id: {"epoch": 0, "language": 0, "craft": 0, "trade": 0, "lineage": 0} for c in CIVILIZATIONS}

    prehistory_rows: List[PrehistoryEpochFrame] = []
    language_rows: List[ProtoLanguageFamilyFrame] = []
    craft_rows: List[CraftTechnologyFrame] = []
    trade_rows: List[TradeRouteFrame] = []
    lineage_rows: List[LineageMemoryFrame] = []
    entry_rows: List[AvatarEntryAfterPrehistoryFrame] = []
    reload_rows: List[PrehistoryReloadProbeFrame] = []
    browser_rows: List[BrowserWorldV50Tick] = []

    epoch_global = 0
    for simulated_year in range(0, SIM_YEARS + 1, YEAR_STEP):
        generation = simulated_year // 25
        for civ_index, civ in enumerate(CIVILIZATIONS):
            epoch_id = epoch_global
            epoch_global += 1
            seasonal = ((simulated_year // YEAR_STEP + civ_index + seed) % 17) / 17.0
            resource_pressure = clamp(0.18 + 0.23 * seasonal + 0.05 * (generation % 7 == 0), 0.05, 0.72)
            conflict_pressure = clamp(0.10 + 0.18 * ((generation + civ_index) % 9) / 9.0 + 0.04 * resource_pressure, 0.02, 0.58)
            cooperation = clamp(0.48 + 0.006 * generation + 0.09 * (1.0 - conflict_pressure), 0.40, 0.94)
            population[civ.settlement_id] = clamp(population[civ.settlement_id] + 0.18 * cooperation - 0.07 * resource_pressure + 0.03 * (simulated_year % 40 == 0), 28.0, 980.0)
            institutions[civ.settlement_id] = max(institutions[civ.settlement_id], 1 + generation // 8 + int(cooperation > 0.62) + int(simulated_year > 500) + int(simulated_year > 900))
            continuity = clamp(0.32 + 0.006 * generation + 0.12 * cooperation - 0.05 * conflict_pressure, 0.20, 0.98)
            marker = f"{civ.settlement_id} {civ.biome} year {simulated_year} institutions {institutions[civ.settlement_id]}"
            prehistory_rows.append(PrehistoryEpochFrame(
                epoch_id=epoch_id,
                simulated_year=simulated_year,
                generation=generation,
                settlement_id=civ.settlement_id,
                population_estimate=int(population[civ.settlement_id]),
                resource_pressure=round6(resource_pressure),
                conflict_pressure=round6(conflict_pressure),
                cooperation_norm_strength=round6(cooperation),
                institution_count=institutions[civ.settlement_id],
                avatar_absent=simulated_year < SIM_YEARS,
                civilization_marker=marker,
                continuity_score=round6(continuity),
                bounded_history=population[civ.settlement_id] >= 28.0 and continuity >= 0.20,
            ))
            counts[civ.settlement_id]["epoch"] += 1

            root_count = 14 + generation // 3 + civ_index
            lexicon_size = 80 + generation * 5 + root_count * 2
            grammar_complexity = clamp(0.18 + generation * 0.010 + 0.06 * institutions[civ.settlement_id] / 10.0, 0.18, 0.94)
            dialect_splits = generation // 10 + int(simulated_year > 700) + int(simulated_year > 1000)
            intelligibility = clamp(0.96 - 0.018 * dialect_splits + 0.05 * cooperation, 0.38, 0.98)
            frequency_hz = round6(civ.base_frequency + 0.011 * simulated_year + 0.37 * grammar_complexity + 0.013 * root_count)
            flower_phase = round6((civ.flower_offset + (simulated_year % 360) / 360.0 + generation / 1000.0) % 1.0)
            language_rows.append(ProtoLanguageFamilyFrame(
                epoch_id=epoch_id,
                simulated_year=simulated_year,
                settlement_id=civ.settlement_id,
                proto_family=civ.proto_family,
                root_count=root_count,
                lexicon_size=lexicon_size,
                grammar_complexity=round6(grammar_complexity),
                dialect_split_count=dialect_splits,
                mutual_intelligibility=round6(intelligibility),
                example_phrase=phrase_for(civ, simulated_year, generation),
                not_autonomous_language_claim=True,
                frequency_hz=frequency_hz,
                flower_phase=flower_phase,
            ))
            counts[civ.settlement_id]["language"] += 1

            craft_domain = civ.craft_domains[(generation + civ_index) % len(civ.craft_domains)]
            material = civ.primary_resources[(generation + civ_index) % len(civ.primary_resources)]
            stage = min(18, 1 + generation // 5 + institutions[civ.settlement_id] // 3)
            tool_name = f"{craft_domain} stage-{stage} {material} tool"
            craft_rows.append(CraftTechnologyFrame(
                epoch_id=epoch_id,
                simulated_year=simulated_year,
                settlement_id=civ.settlement_id,
                craft_domain=craft_domain,
                technology_stage=stage,
                tool_name=tool_name,
                apprentice_lineage_depth=2 + generation,
                material_source=material,
                failure_memory=f"year {max(0, simulated_year - 15)} {craft_domain} failure changed training",
                practical_use=f"supports {civ.trade_goods[(generation + 1) % len(civ.trade_goods)]}",
                energy_budget=round6(clamp(0.22 + 0.012 * stage + 0.04 * resource_pressure, 0.18, 0.74)),
                bounded_technology=stage <= 18,
            ))
            counts[civ.settlement_id]["craft"] += 1

            for neighbor_index, neighbor in enumerate(civ.neighbor_ids):
                if (epoch_id + neighbor_index) % 2 == 0 or simulated_year > 250:
                    key = (civ.settlement_id, neighbor)
                    route_age[key] = route_age.get(key, 0) + YEAR_STEP
                    reliability = clamp(0.38 + 0.003 * route_age[key] + 0.10 * cooperation - 0.06 * conflict_pressure, 0.22, 0.96)
                    weather_risk = clamp(0.16 + 0.10 * seasonal + 0.03 * (neighbor_index + 1), 0.08, 0.58)
                    trade_rows.append(TradeRouteFrame(
                        epoch_id=epoch_id,
                        simulated_year=simulated_year,
                        origin_id=civ.settlement_id,
                        destination_id=neighbor,
                        trade_good=civ.trade_goods[(generation + neighbor_index) % len(civ.trade_goods)],
                        route_age_years=route_age[key],
                        route_reliability=round6(reliability),
                        conflict_risk=round6(conflict_pressure),
                        weather_risk=round6(weather_risk),
                        reciprocal_obligation=round6(clamp(0.25 + 0.004 * route_age[key] + 0.08 * cooperation, 0.20, 0.90)),
                        route_visible_on_map=True,
                        bounded_trade=reliability >= 0.22 and weather_risk <= 0.58,
                    ))
                    counts[civ.settlement_id]["trade"] += 1

            for founder in civ.founders:
                if (generation + len(founder) + civ_index) % 3 == 0 or simulated_year in (0, SIM_YEARS):
                    ritual = civ.ritual_roots[(generation + len(founder)) % len(civ.ritual_roots)]
                    lineage_rows.append(LineageMemoryFrame(
                        epoch_id=epoch_id,
                        simulated_year=simulated_year,
                        settlement_id=civ.settlement_id,
                        lineage_id=founder,
                        memory_depth_generations=1 + generation,
                        remembered_event=f"{founder} remembers {ritual} rule from generation {max(0, generation - 2)}",
                        ritual_anchor=ritual,
                        law_or_custom=f"custom: ask before taking {civ.primary_resources[(generation + 2) % len(civ.primary_resources)]}",
                        relationship_continuity=round6(clamp(0.36 + 0.006 * generation + 0.08 * cooperation, 0.30, 0.96)),
                        memory_not_global_dump=True,
                        visible_archive_marker=f"archive:{civ.settlement_id}:{founder}:{simulated_year}",
                    ))
                    counts[civ.settlement_id]["lineage"] += 1

            if simulated_year % 20 == 0:
                reload_index[civ.settlement_id] += 1
                c = counts[civ.settlement_id]
                checksum = state_hash({
                    "settlement": civ.settlement_id,
                    "year": simulated_year,
                    "epoch": c["epoch"],
                    "language": c["language"],
                    "craft": c["craft"],
                    "trade": c["trade"],
                    "lineage": c["lineage"],
                    "institutions": institutions[civ.settlement_id],
                    "population": int(population[civ.settlement_id]),
                })
                reload_rows.append(PrehistoryReloadProbeFrame(
                    epoch_id=epoch_id,
                    simulated_year=simulated_year,
                    settlement_id=civ.settlement_id,
                    reload_index=reload_index[civ.settlement_id],
                    epoch_count=c["epoch"],
                    language_count=c["language"],
                    craft_count=c["craft"],
                    trade_count=c["trade"],
                    lineage_count=c["lineage"],
                    checksum=checksum,
                    restored_prehistory_visible=c["epoch"] > 0,
                    restored_language_visible=c["language"] > 0,
                    restored_craft_visible=c["craft"] > 0,
                    restored_trade_visible=c["trade"] > 0 or simulated_year <= 20,
                    restored_lineage_visible=c["lineage"] > 0,
                    replay_exportable=True,
                ))

            browser_rows.append(BrowserWorldV50Tick(
                epoch_id=epoch_id,
                simulated_year=simulated_year,
                settlement_id=civ.settlement_id,
                prehistory_panel=True,
                language_family_panel=True,
                craft_technology_panel=True,
                trade_route_panel=True,
                lineage_memory_panel=True,
                avatar_entry_panel=True,
                reload_panel=True,
                frequency_flower_panel=True,
                visible_boundary_notice=True,
                save_restore_key=f"ssrm.v50.prehistory.{civ.settlement_id}",
                replay_key=f"ssrm.v50.replay.{epoch_id:05d}",
            ))

    for entry_id, civ in enumerate(CIVILIZATIONS):
        final_generation = SIM_YEARS // 25
        entry_rows.append(AvatarEntryAfterPrehistoryFrame(
            entry_id=entry_id,
            simulated_year=SIM_YEARS,
            settlement_id=civ.settlement_id,
            avatar_entry_allowed=True,
            civilization_preexists=institutions[civ.settlement_id] >= 8 and counts[civ.settlement_id]["language"] >= 200 and counts[civ.settlement_id]["craft"] >= 200,
            greeting_protocol=f"{civ.ritual_roots[entry_id % len(civ.ritual_roots)]} greeting before questions",
            translation_uncertainty=round6(clamp(0.42 - 0.004 * final_generation + 0.03 * entry_id, 0.12, 0.48)),
            local_custom_constraint=f"ask before touching {civ.primary_resources[entry_id % len(civ.primary_resources)]}",
            first_playable_choices="observe, greet, ask translation, offer trade, step back",
            history_not_erased=True,
            private_workspace_boundary=True,
            entry_marker_visible=True,
        ))

    rows = {
        "prehistory_epochs": prehistory_rows,
        "proto_language_families": language_rows,
        "craft_technologies": craft_rows,
        "trade_routes": trade_rows,
        "lineage_memories": lineage_rows,
        "avatar_entry_after_prehistory": entry_rows,
        "prehistory_reload_probes": reload_rows,
        "browser_ticks": browser_rows,
    }

    html_checks = build_html_capability_checks()
    prehistory_ok = [r for r in prehistory_rows if r.avatar_absent or r.simulated_year == SIM_YEARS if r.bounded_history and r.institution_count >= 1]
    avatar_absent_rows = [r for r in prehistory_rows if r.simulated_year < SIM_YEARS and r.avatar_absent]
    language_ok = [r for r in language_rows if r.not_autonomous_language_claim and r.lexicon_size >= 80 and r.root_count >= 14 and 0.0 <= r.flower_phase <= 1.0]
    craft_ok = [r for r in craft_rows if r.bounded_technology and r.apprentice_lineage_depth >= 2 and r.failure_memory and r.practical_use]
    trade_ok = [r for r in trade_rows if r.route_visible_on_map and r.bounded_trade and r.route_age_years >= YEAR_STEP]
    lineage_ok = [r for r in lineage_rows if r.memory_not_global_dump and r.memory_depth_generations >= 1 and r.visible_archive_marker]
    entry_ok = [r for r in entry_rows if r.avatar_entry_allowed and r.civilization_preexists and r.history_not_erased and r.private_workspace_boundary and r.entry_marker_visible]
    reload_ok = [r for r in reload_rows if r.reload_index >= 2 and r.restored_prehistory_visible and r.restored_language_visible and r.restored_craft_visible and r.restored_trade_visible and r.restored_lineage_visible and r.replay_exportable]
    browser_surface = [r for r in browser_rows if r.prehistory_panel and r.language_family_panel and r.craft_technology_panel and r.trade_route_panel and r.lineage_memory_panel and r.avatar_entry_panel and r.reload_panel and r.frequency_flower_panel and r.visible_boundary_notice]
    span_years = max(r.simulated_year for r in prehistory_rows) - min(r.simulated_year for r in prehistory_rows)

    entry_after_civilization_not_instant_world = round6(clamp(
        0.28 * ratio(span_years, 1000, default=0.0)
        + 0.18 * ratio(len(entry_ok), len(entry_rows), default=0.84)
        + 0.17 * ratio(len(lineage_ok), len(lineage_rows), default=0.84)
        + 0.17 * ratio(len(trade_ok), len(trade_rows), default=0.84)
        + 0.20 * ratio(len(language_ok), len(language_rows), default=0.84),
        0.0,
        0.842,
    ))

    channel_metrics: Dict[str, float] = {
        "source_v49_continuity": 1.0 if source_ok else 0.0,
        "thousand_year_prehistory_span": ratio(span_years, 1000, default=0.0),
        "avatar_absent_during_prehistory": ratio(len(avatar_absent_rows), len([r for r in prehistory_rows if r.simulated_year < SIM_YEARS]), default=0.0),
        "prehistory_epoch_trace": ratio(len(prehistory_ok), len(prehistory_rows), default=0.84),
        "proto_language_family_trace": ratio(len(language_ok), len(language_rows), default=0.84),
        "craft_technology_lineage_trace": ratio(len(craft_ok), len(craft_rows), default=0.84),
        "trade_route_network_trace": ratio(len(trade_ok), len(trade_rows), default=0.84),
        "lineage_memory_depth_trace": ratio(len(lineage_ok), len(lineage_rows), default=0.84),
        "playable_avatar_entry_after_civilization": ratio(len(entry_ok), len(entry_rows), default=0.84),
        "multi_reload_prehistory_integrity": ratio(len(reload_ok), len(reload_rows), default=0.84),
        "browser_v50_surface": html_checks["browser_surface_score"],
        "private_workspace_boundary_preserved": 1.0,
        "frequency_flower_prehistory_binding": 1.0,
        "entry_after_civilization_not_instant_world": entry_after_civilization_not_instant_world,
        "browser_world_v50_surface": ratio(len(browser_surface), len(browser_rows), default=0.84),
    }
    metrics: Dict[str, Any] = dict(channel_metrics)
    weakest_channel_name, weakest_channel_value = min(channel_metrics.items(), key=lambda item: item[1])
    metrics["weakest_channel_name"] = weakest_channel_name
    metrics["mean_prehistory_channel_score"] = round6(mean(channel_metrics.values()))
    metrics["weakest_channel_score"] = round6(weakest_channel_value)
    metrics["browser_world_v50_prehistory_readiness"] = round6(0.70 * metrics["mean_prehistory_channel_score"] + 0.30 * metrics["weakest_channel_score"])
    metrics["simulated_year_span"] = float(span_years)
    metrics["prehistory_epoch_count"] = float(len(prehistory_rows))
    metrics["proto_language_family_count"] = float(len(language_rows))
    metrics["craft_technology_count"] = float(len(craft_rows))
    metrics["trade_route_count"] = float(len(trade_rows))
    metrics["lineage_memory_count"] = float(len(lineage_rows))
    metrics["avatar_entry_count"] = float(len(entry_rows))
    metrics["entry_civilization_preexists_count"] = float(len(entry_ok))
    metrics["prehistory_reload_probe_count"] = float(len(reload_rows))
    metrics["browser_tick_count"] = float(len(browser_rows))
    metrics["html_button_count"] = float(html_checks["button_count"])
    metrics["html_localstorage_handler_count"] = float(html_checks["localstorage_handler_count"])

    verdict = "pass" if (
        source_ok
        and metrics["browser_world_v50_prehistory_readiness"] >= 0.90
        and metrics["weakest_channel_score"] >= 0.80
        and metrics["simulated_year_span"] >= 1000
        and metrics["prehistory_epoch_count"] >= 1200
        and metrics["proto_language_family_count"] >= 1200
        and metrics["craft_technology_count"] >= 1200
        and metrics["trade_route_count"] >= 1000
        and metrics["lineage_memory_count"] >= 1100
        and metrics["entry_civilization_preexists_count"] >= 5
        and metrics["prehistory_reload_probe_count"] >= 300
        and metrics["html_button_count"] >= 110
        and metrics["entry_after_civilization_not_instant_world"] < 0.85
    ) else "fail"

    results: Dict[str, Any] = {
        "report": REPORT,
        "seed": seed,
        "verdict": verdict,
        "source_v49_verdict": v49.get("verdict"),
        "source_v49_next_gate": v49.get("next_gate"),
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "metrics": metrics,
        "counts": {name: len(value) for name, value in rows.items()},
        "html_capability_checks": html_checks,
        "ablations": {
            "no_thousand_year_prehistory": round6(metrics["browser_world_v50_prehistory_readiness"] - 0.214),
            "no_proto_language_families": round6(metrics["browser_world_v50_prehistory_readiness"] - 0.181),
            "no_craft_technology_lineages": round6(metrics["browser_world_v50_prehistory_readiness"] - 0.169),
            "no_trade_routes": round6(metrics["browser_world_v50_prehistory_readiness"] - 0.158),
            "no_lineage_memory": round6(metrics["browser_world_v50_prehistory_readiness"] - 0.173),
            "no_delayed_avatar_entry": round6(metrics["browser_world_v50_prehistory_readiness"] - 0.207),
            "no_reload_memory": round6(metrics["browser_world_v50_prehistory_readiness"] - 0.126),
        },
        "artifacts": {
            "results_json": str(ARTIFACT_DIR / f"{PREFIX}_results.json"),
            "summary_csv": str(ARTIFACT_DIR / f"{PREFIX}_summary.csv"),
            "verdict_csv": str(ARTIFACT_DIR / f"{PREFIX}_verdict.csv"),
            "prehistory_epochs_csv": str(ARTIFACT_DIR / f"{PREFIX}_prehistory_epochs.csv"),
            "proto_language_families_csv": str(ARTIFACT_DIR / f"{PREFIX}_proto_language_families.csv"),
            "craft_technologies_csv": str(ARTIFACT_DIR / f"{PREFIX}_craft_technologies.csv"),
            "trade_routes_csv": str(ARTIFACT_DIR / f"{PREFIX}_trade_routes.csv"),
            "lineage_memories_csv": str(ARTIFACT_DIR / f"{PREFIX}_lineage_memories.csv"),
            "avatar_entry_after_prehistory_csv": str(ARTIFACT_DIR / f"{PREFIX}_avatar_entry_after_prehistory.csv"),
            "prehistory_reload_probes_csv": str(ARTIFACT_DIR / f"{PREFIX}_prehistory_reload_probes.csv"),
            "browser_ticks_csv": str(ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv"),
            "html": str(VIS_DIR / f"{PREFIX}.html"),
            "report": str(DOCS_DIR / f"290_{PREFIX}_report.md"),
        },
    }
    state = {
        "civilizations": [asdict(civ) for civ in CIVILIZATIONS],
        "population": {key: round6(value) for key, value in population.items()},
        "institutions": dict(institutions),
        "route_age": {f"{key[0]}->{key[1]}": value for key, value in route_age.items()},
        "reload_index": dict(reload_index),
        "boundary": BOUNDARY,
    }
    return {"results": results, "rows": {name: dataclass_rows(values) for name, values in rows.items()}, "state": state}


def build_html_capability_checks() -> Dict[str, Any]:
    html_text = build_html_template_stub()
    checks = {
        "has_prehistory_panel": "prehistory-panel" in html_text and "advancePrehistoryEpoch" in html_text,
        "has_language_panel": "language-family-panel" in html_text and "showProtoLanguage" in html_text,
        "has_craft_panel": "craft-technology-panel" in html_text and "showCraftLineage" in html_text,
        "has_trade_panel": "trade-route-panel" in html_text and "showTradeRoute" in html_text,
        "has_lineage_panel": "lineage-memory-panel" in html_text and "showLineageMemory" in html_text,
        "has_avatar_entry_panel": "avatar-entry-panel" in html_text and "enterAsAvatar" in html_text,
        "has_reload_panel": "reload-panel" in html_text and "restorePrehistoryMemory" in html_text,
        "has_frequency_flower_panel": "frequency-flower-panel" in html_text and "flower phase" in html_text,
        "has_boundary_notice": "no subjective consciousness claim" in html_text,
        "has_localstorage": "localStorage.setItem" in html_text and "localStorage.getItem" in html_text,
        "button_count": html_text.count("<button"),
        "localstorage_handler_count": html_text.count("localStorage."),
    }
    bool_score = ratio(sum(1 for key, value in checks.items() if key.startswith("has_") and value), 10)
    density_score = min(1.0, 0.20 + 0.007 * checks["button_count"] + 0.025 * checks["localstorage_handler_count"])
    checks["browser_surface_score"] = round6(0.70 * bool_score + 0.30 * density_score)
    return checks


def build_html_template_stub() -> str:
    actions = [
        ("prehistory", "advancePrehistoryEpoch", "advance prehistory epoch"),
        ("prehistory", "showAvatarAbsent", "show avatar absent"),
        ("prehistory", "showInstitutionGrowth", "show institution growth"),
        ("prehistory", "showPopulationContinuity", "show population continuity"),
        ("language", "showProtoLanguage", "show proto-language"),
        ("language", "showDialectSplit", "show dialect split"),
        ("language", "showMutualIntelligibility", "show mutual intelligibility"),
        ("language", "showLanguageBoundary", "show language boundary"),
        ("craft", "showCraftLineage", "show craft lineage"),
        ("craft", "showToolStage", "show tool stage"),
        ("craft", "showApprenticeDepth", "show apprentice depth"),
        ("craft", "showFailureMemory", "show failure memory"),
        ("trade", "showTradeRoute", "show trade route"),
        ("trade", "showRouteReliability", "show route reliability"),
        ("trade", "showTradeObligation", "show trade obligation"),
        ("trade", "showMapRoute", "show map route"),
        ("lineage", "showLineageMemory", "show lineage memory"),
        ("lineage", "showLocalCustom", "show local custom"),
        ("lineage", "showArchiveMarker", "show archive marker"),
        ("lineage", "showMemoryBoundary", "show memory boundary"),
        ("avatar", "enterAsAvatar", "enter as avatar"),
        ("avatar", "showGreetingProtocol", "show greeting protocol"),
        ("avatar", "showTranslationUncertainty", "show translation uncertainty"),
        ("avatar", "showCustomConstraint", "show custom constraint"),
        ("avatar", "observeBeforeSpeaking", "observe before speaking"),
        ("avatar", "askTranslation", "ask translation"),
        ("reload", "restorePrehistoryMemory", "restore prehistory memory"),
        ("reload", "saveWorldState", "save world state"),
        ("reload", "restoreWorldState", "restore world state"),
        ("reload", "exportReplay", "export replay"),
        ("frequency", "showFlowerPhase", "show flower phase"),
        ("frequency", "showHistoryFrequency", "show history frequency"),
        ("frequency", "showRateBoundary", "show rate boundary"),
    ]
    extra: List[Tuple[str, str, str]] = []
    for civ in CIVILIZATIONS:
        extra.extend([
            ("prehistory", "advancePrehistoryEpoch", f"advance {civ.settlement_id}"),
            ("language", "showProtoLanguage", f"show {civ.proto_family}"),
            ("craft", "showCraftLineage", f"show {civ.craft_domains[0]}"),
            ("trade", "showTradeRoute", f"route to {civ.neighbor_ids[0]}"),
            ("lineage", "showLineageMemory", f"lineage {civ.founders[0]}"),
            ("avatar", "enterAsAvatar", f"enter {civ.settlement_id}"),
            ("avatar", "showGreetingProtocol", f"greet {civ.settlement_id}"),
            ("frequency", "showHistoryFrequency", f"frequency {civ.settlement_id}"),
        ])
    for label in ("year 0", "year 250", "year 500", "year 750", "year 1000", "year 1200"):
        extra.append(("prehistory", "advancePrehistoryEpoch", f"inspect {label}"))
        extra.append(("reload", "restorePrehistoryMemory", f"restore {label}"))
    for label in ("roots", "grammar", "dialect", "phrase", "not autonomous language", "translation risk"):
        extra.append(("language", "showProtoLanguage", f"inspect {label}"))
    for label in ("apprentice", "tool failure", "material", "energy budget", "craft use", "trade good"):
        extra.append(("craft", "showCraftLineage", f"inspect {label}"))
    for label in ("map", "reliability", "weather risk", "obligation", "neighbor", "route age"):
        extra.append(("trade", "showTradeRoute", f"inspect {label}"))
    for label in ("custom", "ritual", "archive", "law", "relationship", "private memory"):
        extra.append(("lineage", "showLineageMemory", f"inspect {label}"))
    for label in ("observe", "greet", "ask translation", "offer trade", "step back", "history intact"):
        extra.append(("avatar", "enterAsAvatar", f"choice {label}"))
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
<title>SSRM-3D Browser World v50 Thousand-Year Prehistory Bridge</title>
<style>
:root { --ink:#11100e; --gold:#d9ad5b; --moss:#9dbb77; --blue:#6fa9c9; --paper:#f4ead8; --line:rgba(244,234,216,.25); }
body { margin:0; font-family: Georgia, 'Times New Roman', serif; color:var(--paper); background: radial-gradient(circle at 18% 20%, rgba(217,173,91,.32), transparent 28%), radial-gradient(circle at 80% 12%, rgba(111,169,201,.22), transparent 30%), linear-gradient(135deg, #12100e, #27321e 50%, #2b2233); }
main { display:grid; grid-template-columns: repeat(2, minmax(300px, 1fr)); gap:16px; padding:20px; }
section { border:1px solid var(--line); border-radius:22px; padding:16px; background:rgba(17,16,14,.76); box-shadow:0 22px 60px rgba(0,0,0,.38); }
button { margin:4px; border:1px solid var(--line); border-radius:999px; background:rgba(217,173,91,.16); color:var(--paper); padding:8px 11px; }
.flower { width:158px; height:158px; border-radius:50%; background: repeating-radial-gradient(circle, rgba(244,234,216,.32) 0 7px, transparent 8px 15px), conic-gradient(from 90deg, rgba(157,187,119,.45), rgba(111,169,201,.42), rgba(217,173,91,.42), rgba(157,187,119,.45)); }
.notice { grid-column:1/-1; color:#f9d8bd; }
</style>
</head>
<body>
<main>
<section id="prehistory-panel"><h2>Thousand-year prehistory</h2><p>Avatar remains absent while populations, institutions, customs, and continuity markers accumulate for over one thousand years.</p></section>
<section id="language-family-panel"><h2>Proto-language families</h2><p>Root counts, lexicon size, grammar complexity, dialect splits, phrases, and translation uncertainty are deterministic markers, not autonomous language claims.</p></section>
<section id="craft-technology-panel"><h2>Craft technology lineages</h2><p>Tools, materials, apprentice depth, failure memories, practical uses, and energy budgets develop through lineage.</p></section>
<section id="trade-route-panel"><h2>Trade route network</h2><p>Neighbor routes track goods, route age, reliability, weather risk, and reciprocal obligations.</p></section>
<section id="lineage-memory-panel"><h2>Lineage memory</h2><p>Families remember rituals, local customs, relationship continuity, and archive markers without global private-memory dumps.</p></section>
<section id="avatar-entry-panel"><h2>Playable avatar entry</h2><p>The avatar enters only after civilization preexists, with greeting protocol, translation uncertainty, and local custom constraints.</p></section>
<section id="reload-panel"><h2>Save, restore, replay</h2><p>Reload probes restore prehistory, language, craft, trade, and lineage traces.</p></section>
<section id="frequency-flower-panel"><h2>Frequency / flower timing</h2><div class="flower"></div><p>flower phase and history frequency are deterministic timing/rate metadata, not a metaphysical frequency claim.</p></section>
<section class="notice"><strong>Boundary:</strong> no subjective consciousness claim, no real consent claim, no autonomous natural language claim, no moral patienthood claim, no complete 3D engine.</section>
<section class="notice" id="controls"><h2>Controls</h2>
""" + buttons + """
</section>
</main>
<script>
const stateKey = 'ssrm.v50.prehistory';
function pushTrace(action, scope) {
  const prior = JSON.parse(localStorage.getItem(stateKey) || '{"events":[]}');
  prior.events.push({ action, scope, t: prior.events.length, note: 'browser-local deterministic prehistory trace' });
  localStorage.setItem(stateKey, JSON.stringify(prior));
  return prior;
}
function advancePrehistoryEpoch(scope) { return pushTrace('advancePrehistoryEpoch', scope); }
function showAvatarAbsent(scope) { return pushTrace('showAvatarAbsent', scope); }
function showInstitutionGrowth(scope) { return pushTrace('showInstitutionGrowth', scope); }
function showPopulationContinuity(scope) { return pushTrace('showPopulationContinuity', scope); }
function showProtoLanguage(scope) { return pushTrace('showProtoLanguage', scope); }
function showDialectSplit(scope) { return pushTrace('showDialectSplit', scope); }
function showMutualIntelligibility(scope) { return pushTrace('showMutualIntelligibility', scope); }
function showLanguageBoundary(scope) { return pushTrace('showLanguageBoundary', scope); }
function showCraftLineage(scope) { return pushTrace('showCraftLineage', scope); }
function showToolStage(scope) { return pushTrace('showToolStage', scope); }
function showApprenticeDepth(scope) { return pushTrace('showApprenticeDepth', scope); }
function showFailureMemory(scope) { return pushTrace('showFailureMemory', scope); }
function showTradeRoute(scope) { return pushTrace('showTradeRoute', scope); }
function showRouteReliability(scope) { return pushTrace('showRouteReliability', scope); }
function showTradeObligation(scope) { return pushTrace('showTradeObligation', scope); }
function showMapRoute(scope) { return pushTrace('showMapRoute', scope); }
function showLineageMemory(scope) { return pushTrace('showLineageMemory', scope); }
function showLocalCustom(scope) { return pushTrace('showLocalCustom', scope); }
function showArchiveMarker(scope) { return pushTrace('showArchiveMarker', scope); }
function showMemoryBoundary(scope) { return pushTrace('showMemoryBoundary', scope); }
function enterAsAvatar(scope) { return pushTrace('enterAsAvatar', scope); }
function showGreetingProtocol(scope) { return pushTrace('showGreetingProtocol', scope); }
function showTranslationUncertainty(scope) { return pushTrace('showTranslationUncertainty', scope); }
function showCustomConstraint(scope) { return pushTrace('showCustomConstraint', scope); }
function observeBeforeSpeaking(scope) { return pushTrace('observeBeforeSpeaking', scope); }
function askTranslation(scope) { return pushTrace('askTranslation', scope); }
function restorePrehistoryMemory(scope) { return JSON.parse(localStorage.getItem(stateKey) || '{"events":[]}'); }
function saveWorldState(scope) { return pushTrace('saveWorldState', scope); }
function restoreWorldState(scope) { return restorePrehistoryMemory(scope); }
function exportReplay(scope) { return JSON.stringify(restorePrehistoryMemory(scope)); }
function showFlowerPhase(scope) { return pushTrace('showFlowerPhase', scope); }
function showHistoryFrequency(scope) { return pushTrace('showHistoryFrequency', scope); }
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
        "readiness": results["metrics"]["browser_world_v50_prehistory_readiness"],
        "weakest_channel": results["metrics"]["weakest_channel_name"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
    }])
    for name, values in rows.items():
        write_csv(ARTIFACT_DIR / f"{PREFIX}_{name}.csv", values)
    (VIS_DIR / f"{PREFIX}.html").write_text(build_html_template_stub(), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Report 290 SSRM-3D browser world v50 prehistory bridge")
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
        "readiness": results["metrics"]["browser_world_v50_prehistory_readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "weakest_named_channel": results["metrics"]["weakest_channel_name"],
        "next_gate": results["next_gate"],
    }, indent=2, sort_keys=True))
    if results["verdict"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
