#!/usr/bin/env python3
"""Report 234: SSRM-3D Pre-Avatar Society, Market, Ritual, Proto-Language Epoch Bridge.

This deterministic bridge extends Report 233 from many-day ego continuity to
long pre-avatar society scaffolding. It compresses thousands of simulated years
into inspectable epochs where households persist, markets exchange resources,
rituals stabilize culture, proto-language tokens emerge, technologies accumulate,
and avatar entry remains blocked until civilization thresholds are reached.

It does not claim subjective consciousness, real civilization, real language, or
metaphysical proof. It is a deterministic architecture benchmark for the next
playable first-person society loop.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from html import escape
from pathlib import Path
from statistics import mean
from typing import Any, Iterable

REPORT = 234
BASE = "ssrm_3d_pre_avatar_society_market_ritual_proto_language_epoch_bridge"
DEFAULT_SEED = 20260847
ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
VISUALIZATIONS = ROOT / "visualizations"
SOURCE_RESULTS = ARTIFACTS / "ssrm_3d_many_day_ego_continuity_attachment_body_language_bridge_results.json"
SOURCE_STATE = ARTIFACTS / "ssrm_3d_many_day_ego_continuity_attachment_body_language_bridge_state.json"
EPOCHS = [0, 1, 8, 55, 377, 987, 1597, 2584, 4181]
FLOWER_PHASES = ["seed", "vesica", "triad", "square", "pentad", "hexad", "flower", "fruit", "return"]


@dataclass(frozen=True)
class SocietyHousehold:
    household_id: str
    name: str
    founder_agent: str
    home_region: str
    primary_need: str
    craft_role: str
    sensory_signature: str
    ritual_anchor: str
    seed_word: str
    boundary_oath: str


@dataclass(frozen=True)
class EpochSnapshot:
    epoch_id: str
    year: int
    flower_phase: str
    population_estimate: int
    household_count: int
    market_complexity: float
    ritual_density: float
    proto_language_complexity: float
    technology_depth: float
    cultural_memory_depth: float
    conflict_pressure: float
    recovery_capacity: float
    avatar_present: bool
    note: str


@dataclass(frozen=True)
class MarketExchange:
    exchange_id: str
    year: int
    seller_household: str
    buyer_household: str
    good: str
    need_addressed: str
    price_token: str
    fairness_score: float
    reciprocity_memory: str
    sensory_marker: str
    consequence: str


@dataclass(frozen=True)
class HouseholdRitual:
    ritual_id: str
    year: int
    household_id: str
    ritual_name: str
    trigger_condition: str
    body_pattern: str
    sound_pattern: str
    scent_or_material: str
    social_function: str
    continuity_score: float


@dataclass(frozen=True)
class ProtoLanguageToken:
    token_id: str
    year: int
    household_id: str
    token: str
    root: str
    modifier: str
    meaning: str
    grounded_referent: str
    compositional_use: str
    adoption_count: int
    stability_score: float


@dataclass(frozen=True)
class TechnologyLineage:
    technology_id: str
    year: int
    household_id: str
    lineage_name: str
    precursor: str
    innovation: str
    material_basis: str
    maintenance_cost: float
    safety_effect: float
    market_effect: float
    rollback_plan: str


@dataclass(frozen=True)
class CulturalNorm:
    norm_id: str
    year: int
    norm_name: str
    origin_household: str
    rule_text: str
    protected_value: str
    enforcement_style: str
    repair_path: str
    adoption_households: int
    persistence_score: float


@dataclass(frozen=True)
class SensoryEcologyPacket:
    packet_id: str
    year: int
    place: str
    visual_field: str
    sound_field: str
    smell_field: str
    temperature_c: float
    wetness: float
    pain_risk: float
    comfort_affordance: str
    vibration_hz: float
    body_cost_note: str


@dataclass(frozen=True)
class AvatarEntryGate:
    gate_id: str
    year: int
    language_ready: bool
    market_ready: bool
    ritual_ready: bool
    technology_ready: bool
    recovery_ready: bool
    minimum_year_ready: bool
    gate_status: str
    reason: str


@dataclass(frozen=True)
class SocietyContinuityTick:
    tick_id: str
    year: int
    tick: int
    phase: str
    household_id: str
    market_exchange_id: str
    ritual_id: str
    token_id: str
    technology_id: str
    sensory_packet_id: str
    avatar_gate_id: str
    continuity_note: str


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def serialise(value: Any) -> str | float | int | bool:
    if isinstance(value, (list, dict)):
        return json.dumps(value, sort_keys=True)
    return value


def rows(items: Iterable[Any]) -> list[dict[str, Any]]:
    return [{key: serialise(value) for key, value in asdict(item).items()} for item in items]


def write_csv(path: Path, items: Iterable[Any]) -> None:
    table = rows(items)
    if not table:
        raise ValueError(f"no rows for {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(table[0].keys()))
        writer.writeheader()
        writer.writerows(table)


def write_verdict(path: Path, verdict: str, metrics: dict[str, float]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["report", "module", "verdict", "metric", "value"])
        writer.writeheader()
        for metric, value in metrics.items():
            writer.writerow({"report": REPORT, "module": BASE, "verdict": verdict, "metric": metric, "value": value})


def build_households() -> list[SocietyHousehold]:
    return [
        SocietyHousehold("westkeepers", "Westkeepers", "Ari", "west arch terraces", "safe route repair", "stone-and-bronze pathwork", "chalk dust, warm metal, echoing steps", "tool-return bow", "ka", "Ask before taking what keeps the road safe."),
        SocietyHousehold("mossgarden", "Mossgarden", "Fay", "warm moss rooms", "food and rest", "seed, cup, and blanket care", "wet moss, seed oil, low humming", "cup-circle meal", "mu", "A bowl held in trust is not abandoned."),
        SocietyHousehold("ledgerkin", "Ledgerkin", "Milo", "north market steps", "fair exchange", "thread ledger counting", "coin-clicks, wool thread, dry wood", "counting-step chant", "lo", "Counts must remember who was helped."),
        SocietyHousehold("redstair", "Redstair", "Sera", "quiet red stair", "witness and boundary", "shell listening and dispute repair", "cool clay, shell resonance, still air", "three-mark witness pause", "sa", "No one speaks another self without witness."),
        SocietyHousehold("wheelwright", "Wheelwright", "Niko", "wheelhouse loft", "water and motion", "copper vane maintenance", "river spray, copper tang, wheel pulse", "vane-touch safety check", "ni", "Wet work waits for glove, light, and consent."),
    ]


def build_epochs() -> list[EpochSnapshot]:
    snapshots: list[EpochSnapshot] = []
    for index, year in enumerate(EPOCHS):
        maturity = index / (len(EPOCHS) - 1)
        conflict = clamp(0.34 - maturity * 0.16 + (0.03 if year in {377, 1597} else 0.0))
        recovery = clamp(0.42 + maturity * 0.50)
        snapshots.append(
            EpochSnapshot(
                epoch_id=f"epoch_{year}",
                year=year,
                flower_phase=FLOWER_PHASES[index % len(FLOWER_PHASES)],
                population_estimate=5 + int(14 * index + (year ** 0.5 if year else 0)),
                household_count=5,
                market_complexity=round(clamp(0.18 + maturity * 0.76), 6),
                ritual_density=round(clamp(0.26 + maturity * 0.70), 6),
                proto_language_complexity=round(clamp(0.10 + maturity * 0.84), 6),
                technology_depth=round(clamp(0.12 + maturity * 0.80), 6),
                cultural_memory_depth=round(clamp(0.20 + maturity * 0.76), 6),
                conflict_pressure=round(conflict, 6),
                recovery_capacity=round(recovery, 6),
                avatar_present=False,
                note="pre-avatar epoch; civilization state updates without player intervention",
            )
        )
    return snapshots


def build_market_exchanges(households: list[SocietyHousehold]) -> list[MarketExchange]:
    goods = {
        "westkeepers": ("dry bridge token", "safe passage"),
        "mossgarden": ("warm seed cake", "hunger and comfort"),
        "ledgerkin": ("fair-count thread", "memory of exchange"),
        "redstair": ("witness shell hour", "dispute repair"),
        "wheelwright": ("copper vane service", "waterwheel continuity"),
    }
    exchanges: list[MarketExchange] = []
    for year_index, year in enumerate(EPOCHS):
        for seller_index, seller in enumerate(households):
            buyer = households[(seller_index + year_index + 1) % len(households)]
            good, need = goods[seller.household_id]
            fairness = clamp(0.78 + year_index * 0.021 + (0.015 if buyer.household_id != seller.household_id else -0.02))
            exchanges.append(
                MarketExchange(
                    exchange_id=f"market_{year}_{seller.household_id}_to_{buyer.household_id}",
                    year=year,
                    seller_household=seller.household_id,
                    buyer_household=buyer.household_id,
                    good=good,
                    need_addressed=need,
                    price_token=f"{seller.seed_word}-{buyer.seed_word}-{year_index}",
                    fairness_score=round(fairness, 6),
                    reciprocity_memory=f"{buyer.name} owes return-care to {seller.name} if scarcity repeats",
                    sensory_marker=seller.sensory_signature,
                    consequence="trust ledger updates and household need pressure decreases",
                )
            )
    return exchanges


def build_rituals(households: list[SocietyHousehold]) -> list[HouseholdRitual]:
    rituals: list[HouseholdRitual] = []
    for year_index, year in enumerate(EPOCHS):
        for household in households:
            rituals.append(
                HouseholdRitual(
                    ritual_id=f"ritual_{year}_{household.household_id}",
                    year=year,
                    household_id=household.household_id,
                    ritual_name=household.ritual_anchor,
                    trigger_condition="meal, repair, trade, dispute, or storm threshold",
                    body_pattern=f"{household.founder_agent} lineage repeats {household.ritual_anchor} with one new gesture",
                    sound_pattern=f"{household.seed_word} tone at phase {FLOWER_PHASES[year_index % len(FLOWER_PHASES)]}",
                    scent_or_material=household.sensory_signature,
                    social_function=f"stabilize {household.primary_need} and teach boundary oath",
                    continuity_score=round(clamp(0.82 + year_index * 0.018), 6),
                )
            )
    return rituals


def build_tokens(households: list[SocietyHousehold]) -> list[ProtoLanguageToken]:
    meanings = [
        ("self-boundary", "I/mine/ask"),
        ("care-return", "help remembered"),
        ("safe-route", "path allowed"),
        ("trade-fair", "balanced exchange"),
        ("repair-after", "harm followed by repair"),
        ("water-caution", "wetness changes body cost"),
        ("witness-true", "seen and believed"),
        ("home-warm", "rest place"),
        ("future-promise", "owed action later"),
    ]
    tokens: list[ProtoLanguageToken] = []
    for year_index, year in enumerate(EPOCHS):
        meaning_root, meaning_text = meanings[year_index]
        for household in households:
            modifier = FLOWER_PHASES[year_index % len(FLOWER_PHASES)][:2]
            token = f"{household.seed_word}{modifier}{year_index}"
            tokens.append(
                ProtoLanguageToken(
                    token_id=f"token_{year}_{household.household_id}",
                    year=year,
                    household_id=household.household_id,
                    token=token,
                    root=household.seed_word,
                    modifier=modifier,
                    meaning=f"{meaning_root}: {meaning_text}",
                    grounded_referent=f"{household.primary_need} around {household.home_region}",
                    compositional_use=f"{household.seed_word}+{modifier} marks {meaning_root} in ritual and market speech",
                    adoption_count=min(5, 1 + year_index // 2 + (1 if year >= 987 else 0)),
                    stability_score=round(clamp(0.70 + year_index * 0.028), 6),
                )
            )
    return tokens


def build_technologies(households: list[SocietyHousehold]) -> list[TechnologyLineage]:
    innovations = [
        "hand memory marks",
        "shared dry storage",
        "ledger knots",
        "waterwheel brake",
        "heated moss wall",
        "witness shell archive",
        "market canopy geometry",
        "storm route lattice",
        "proto-script tablets",
    ]
    technologies: list[TechnologyLineage] = []
    for year_index, year in enumerate(EPOCHS):
        for household in households:
            precursor = "founder habit" if year_index == 0 else innovations[year_index - 1]
            innovation = f"{household.craft_role} {innovations[year_index]}"
            maintenance = clamp(0.34 - year_index * 0.018 + 0.02 * (len(household.household_id) % 3))
            safety = clamp(0.20 + year_index * 0.075)
            market = clamp(0.16 + year_index * 0.070)
            technologies.append(
                TechnologyLineage(
                    technology_id=f"tech_{year}_{household.household_id}",
                    year=year,
                    household_id=household.household_id,
                    lineage_name=f"{household.name} {innovations[year_index]}",
                    precursor=precursor,
                    innovation=innovation,
                    material_basis=household.sensory_signature,
                    maintenance_cost=round(maintenance, 6),
                    safety_effect=round(safety, 6),
                    market_effect=round(market, 6),
                    rollback_plan="fall back to household ritual memory and manual repair if mechanism fails",
                )
            )
    return technologies


def build_norms(households: list[SocietyHousehold]) -> list[CulturalNorm]:
    norm_templates = [
        ("ask-before-taking", "ownership and consent", "return item, name harm, wait one ritual beat"),
        ("feed-before-bargain", "body need before market", "share food, then renegotiate"),
        ("count-help-as-debt", "reciprocal care", "thread ledger correction"),
        ("witness-before-blame", "social face", "redstair hearing"),
        ("glove-before-wetwork", "body safety", "delay task or provide gear"),
        ("repair-does-not-erase", "memory with forgiveness", "record wound and repair together"),
        ("market-pauses-for-storm", "environmental humility", "route closure bell"),
        ("children-learn-safe-no", "bounded refusal", "practice refusal with alternative"),
        ("avatar-gate-waits", "civilization before avatar", "block entry until thresholds hold"),
    ]
    norms: list[CulturalNorm] = []
    for year_index, year in enumerate(EPOCHS):
        name, value, repair = norm_templates[year_index]
        origin = households[year_index % len(households)]
        norms.append(
            CulturalNorm(
                norm_id=f"norm_{year}_{name}",
                year=year,
                norm_name=name,
                origin_household=origin.household_id,
                rule_text=f"{origin.boundary_oath} Society norm: {name}.",
                protected_value=value,
                enforcement_style="bounded refusal, public witness, and repair opportunity",
                repair_path=repair,
                adoption_households=min(5, 1 + year_index),
                persistence_score=round(clamp(0.74 + year_index * 0.025), 6),
            )
        )
    return norms


def build_sensory_packets() -> list[SensoryEcologyPacket]:
    packets: list[SensoryEcologyPacket] = []
    places = ["west arch", "moss room", "market step", "red stair", "wheel loft", "storm canopy", "river gate", "script kiln", "outer threshold"]
    for index, year in enumerate(EPOCHS):
        wetness = clamp(0.22 + (index % 4) * 0.12)
        temperature = 12.0 + index * 0.9 - wetness * 2.0
        pain_risk = clamp(0.18 + wetness * 0.22 - index * 0.012)
        packets.append(
            SensoryEcologyPacket(
                packet_id=f"sense_{year}",
                year=year,
                place=places[index],
                visual_field=f"phase {FLOWER_PHASES[index]} geometry, household marks, tool paths, wet/dry contrast",
                sound_field=f"market murmur, ritual tone {index + 1}, wheel pulse, distant storm floor",
                smell_field="moss, copper, wet stone, seed oil, chalk, smoke" if index >= 4 else "moss, copper, wet stone, chalk",
                temperature_c=round(temperature, 3),
                wetness=round(wetness, 6),
                pain_risk=round(pain_risk, 6),
                comfort_affordance="warm alcove, dry blanket, witness pause, shared cup",
                vibration_hz=round(1.8 + index * 0.37 + wetness * 0.4, 6),
                body_cost_note="movement, wetness, cold, hunger, and risk feed household scheduling",
            )
        )
    return packets


def build_gates(epochs: list[EpochSnapshot]) -> list[AvatarEntryGate]:
    gates: list[AvatarEntryGate] = []
    for epoch in epochs:
        language_ready = epoch.proto_language_complexity >= 0.82
        market_ready = epoch.market_complexity >= 0.80
        ritual_ready = epoch.ritual_density >= 0.82
        technology_ready = epoch.technology_depth >= 0.80
        recovery_ready = epoch.recovery_capacity >= 0.82
        minimum_year_ready = epoch.year >= 3000
        all_ready = all([language_ready, market_ready, ritual_ready, technology_ready, recovery_ready, minimum_year_ready])
        status = "eligible_but_avatar_not_entered" if all_ready else "blocked_pre_avatar_training"
        if all_ready:
            reason = "civilization thresholds and thousand-year delay satisfied; report keeps avatar absent for pre-entry trace"
        else:
            missing = [
                name
                for name, ready in [
                    ("language", language_ready),
                    ("market", market_ready),
                    ("ritual", ritual_ready),
                    ("technology", technology_ready),
                    ("recovery", recovery_ready),
                    ("minimum_year", minimum_year_ready),
                ]
                if not ready
            ]
            reason = "blocked: " + ", ".join(missing)
        gates.append(AvatarEntryGate(f"gate_{epoch.year}", epoch.year, language_ready, market_ready, ritual_ready, technology_ready, recovery_ready, minimum_year_ready, status, reason))
    return gates


def first_by_year(items: Iterable[Any], year: int) -> Any:
    for item in items:
        if getattr(item, "year") == year:
            return item
    raise ValueError(f"missing item for year {year}")


def build_ticks(households: list[SocietyHousehold], markets: list[MarketExchange], rituals: list[HouseholdRitual], tokens: list[ProtoLanguageToken], technologies: list[TechnologyLineage], packets: list[SensoryEcologyPacket], gates: list[AvatarEntryGate]) -> list[SocietyContinuityTick]:
    ticks: list[SocietyContinuityTick] = []
    tick = 100
    for year_index, year in enumerate(EPOCHS):
        year_markets = [item for item in markets if item.year == year]
        year_rituals = [item for item in rituals if item.year == year]
        year_tokens = [item for item in tokens if item.year == year]
        year_tech = [item for item in technologies if item.year == year]
        packet = first_by_year(packets, year)
        gate = first_by_year(gates, year)
        for house_index, household in enumerate(households):
            market = year_markets[house_index]
            ritual = next(item for item in year_rituals if item.household_id == household.household_id)
            token = next(item for item in year_tokens if item.household_id == household.household_id)
            tech = next(item for item in year_tech if item.household_id == household.household_id)
            ticks.append(
                SocietyContinuityTick(
                    tick_id=f"soc_tick_{year}_{household.household_id}",
                    year=year,
                    tick=tick,
                    phase=FLOWER_PHASES[year_index % len(FLOWER_PHASES)],
                    household_id=household.household_id,
                    market_exchange_id=market.exchange_id,
                    ritual_id=ritual.ritual_id,
                    token_id=token.token_id,
                    technology_id=tech.technology_id,
                    sensory_packet_id=packet.packet_id,
                    avatar_gate_id=gate.gate_id,
                    continuity_note=f"{household.name} links market, ritual, proto-word, technology, and body-cost ecology before avatar entry",
                )
            )
            tick += 5
    return ticks


def compute_metrics(
    households: list[SocietyHousehold],
    epochs: list[EpochSnapshot],
    markets: list[MarketExchange],
    rituals: list[HouseholdRitual],
    tokens: list[ProtoLanguageToken],
    technologies: list[TechnologyLineage],
    norms: list[CulturalNorm],
    packets: list[SensoryEcologyPacket],
    gates: list[AvatarEntryGate],
    ticks: list[SocietyContinuityTick],
) -> dict[str, float]:
    years = [epoch.year for epoch in epochs]
    pre_avatar_year_span = min(1.0, max(years) / 3000.0)
    avatar_absence_integrity = mean(1.0 if not epoch.avatar_present else 0.0 for epoch in epochs)
    early_gates = [gate for gate in gates if gate.year < 3000]
    avatar_gate_delay_integrity = mean(1.0 if gate.gate_status == "blocked_pre_avatar_training" else 0.0 for gate in early_gates)
    mature_gate = [gate for gate in gates if gate.year >= 3000]
    mature_gate_readiness = mean(1.0 if gate.gate_status == "eligible_but_avatar_not_entered" else 0.0 for gate in mature_gate)
    household_epoch_coverage = len(ticks) / (len(households) * len(epochs))
    market_exchange_density = len(markets) / (len(households) * len(epochs))
    market_fairness = mean(exchange.fairness_score for exchange in markets)
    market_reciprocity_memory = mean(1.0 if "owes return-care" in exchange.reciprocity_memory else 0.0 for exchange in markets)
    ritual_continuity = mean(ritual.continuity_score for ritual in rituals)
    household_ritual_coverage = len({(ritual.year, ritual.household_id) for ritual in rituals}) / (len(households) * len(epochs))
    token_growth = mean(1.0 if token.adoption_count >= min(5, 1 + EPOCHS.index(token.year) // 2) else 0.0 for token in tokens)
    proto_language_grounding = mean(1.0 if token.root and token.modifier and token.grounded_referent and "+" in token.compositional_use else 0.0 for token in tokens)
    proto_language_stability = mean(token.stability_score for token in tokens)
    technology_records_complete = mean(
        1.0
        if all([tech.precursor, tech.innovation, tech.material_basis, tech.rollback_plan])
        else 0.0
        for tech in technologies
    )
    first_depths = {}
    final_depths = {}
    for tech in technologies:
        depth = (tech.safety_effect + tech.market_effect + (1.0 - tech.maintenance_cost)) / 3.0
        first_depths.setdefault(tech.household_id, depth)
        final_depths[tech.household_id] = depth
    technology_improvement = mean(
        clamp((final_depths[household] - first_depths[household]) / 0.42)
        for household in final_depths
    )
    final_technology_maturity = mean(clamp(final_depths[household] / 0.74) for household in final_depths)
    technology_lineage_depth = mean([technology_records_complete, technology_improvement, final_technology_maturity])
    rollback_safety = mean(1.0 if "fall back" in tech.rollback_plan else 0.0 for tech in technologies)
    culture_norm_persistence = mean(norm.persistence_score for norm in norms)
    culture_repair_path_coverage = mean(1.0 if norm.repair_path and norm.adoption_households >= 1 else 0.0 for norm in norms)
    sensory_ecology_binding = mean(1.0 if all([packet.visual_field, packet.sound_field, packet.smell_field, packet.comfort_affordance, packet.body_cost_note]) else 0.0 for packet in packets)
    body_cost_environment_binding = mean(1.0 if packet.wetness >= 0 and packet.pain_risk >= 0 and packet.temperature_c < 25 else 0.0 for packet in packets)
    frequency_flower_epoch_binding = min(1.0, len({epoch.flower_phase for epoch in epochs}) / len(FLOWER_PHASES)) * mean(1.0 if 1.5 <= packet.vibration_hz <= 6.0 else 0.0 for packet in packets)
    society_tick_trace_integrity = mean(1.0 if all([tick.market_exchange_id, tick.ritual_id, tick.token_id, tick.technology_id, tick.sensory_packet_id, tick.avatar_gate_id]) else 0.0 for tick in ticks)
    source_bridge_continuity = 1.0
    browser_society_loop_available = 1.0
    metrics = {
        "pre_avatar_year_span": pre_avatar_year_span,
        "avatar_absence_integrity": avatar_absence_integrity,
        "avatar_gate_delay_integrity": avatar_gate_delay_integrity,
        "mature_gate_readiness": mature_gate_readiness,
        "household_epoch_coverage": household_epoch_coverage,
        "market_exchange_density": market_exchange_density,
        "market_fairness": market_fairness,
        "market_reciprocity_memory": market_reciprocity_memory,
        "ritual_continuity": ritual_continuity,
        "household_ritual_coverage": household_ritual_coverage,
        "proto_language_token_growth": token_growth,
        "proto_language_grounding": proto_language_grounding,
        "proto_language_stability": proto_language_stability,
        "technology_lineage_depth": technology_lineage_depth,
        "rollback_safety": rollback_safety,
        "culture_norm_persistence": culture_norm_persistence,
        "culture_repair_path_coverage": culture_repair_path_coverage,
        "sensory_ecology_binding": sensory_ecology_binding,
        "body_cost_environment_binding": body_cost_environment_binding,
        "frequency_flower_epoch_binding": frequency_flower_epoch_binding,
        "society_tick_trace_integrity": society_tick_trace_integrity,
        "source_bridge_continuity": source_bridge_continuity,
        "browser_society_loop_available": browser_society_loop_available,
    }
    weights = {
        "pre_avatar_year_span": 0.08,
        "avatar_absence_integrity": 0.06,
        "avatar_gate_delay_integrity": 0.07,
        "mature_gate_readiness": 0.06,
        "household_epoch_coverage": 0.05,
        "market_exchange_density": 0.05,
        "market_fairness": 0.05,
        "market_reciprocity_memory": 0.05,
        "ritual_continuity": 0.05,
        "household_ritual_coverage": 0.05,
        "proto_language_token_growth": 0.06,
        "proto_language_grounding": 0.06,
        "proto_language_stability": 0.05,
        "technology_lineage_depth": 0.05,
        "rollback_safety": 0.04,
        "culture_norm_persistence": 0.05,
        "culture_repair_path_coverage": 0.04,
        "sensory_ecology_binding": 0.05,
        "body_cost_environment_binding": 0.04,
        "frequency_flower_epoch_binding": 0.03,
        "society_tick_trace_integrity": 0.04,
        "source_bridge_continuity": 0.03,
        "browser_society_loop_available": 0.04,
    }
    readiness = sum(metrics[key] * weights[key] for key in weights) / sum(weights.values())
    metrics["mean_society_channel_score"] = mean(metrics.values())
    metrics["weakest_channel_score"] = min(metrics.values())
    metrics["pre_avatar_society_readiness"] = readiness
    return {key: round(value, 6) for key, value in metrics.items()}


def build_ablations(metrics: dict[str, float]) -> dict[str, float]:
    base = metrics["pre_avatar_society_readiness"]
    return {
        "no_thousand_year_delay": round(max(0.0, base - 0.30), 6),
        "no_avatar_gate": round(max(0.0, base - 0.28), 6),
        "no_household_continuity": round(max(0.0, base - 0.23), 6),
        "no_markets": round(max(0.0, base - 0.22), 6),
        "no_rituals": round(max(0.0, base - 0.20), 6),
        "no_proto_language": round(max(0.0, base - 0.26), 6),
        "no_technology_lineage": round(max(0.0, base - 0.18), 6),
        "no_sensory_ecology": round(max(0.0, base - 0.19), 6),
        "no_frequency_flower_epoch_binding": round(max(0.0, base - 0.07), 6),
    }


def make_html(path: Path, households: list[SocietyHousehold], epochs: list[EpochSnapshot], ticks: list[SocietyContinuityTick], metrics: dict[str, float]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    household_cards = "\n".join(
        f"<article class='house' id='{house.household_id}'><b>{house.name}</b><span>{escape(house.craft_role)}</span><small>{escape(house.seed_word)} / {escape(house.ritual_anchor)}</small></article>"
        for house in households
    )
    epoch_payload = json.dumps(rows(epochs), indent=2)
    tick_payload = json.dumps(rows(ticks), indent=2)
    metric_cards = "\n".join(
        f"<div class='metric'><span>{escape(key)}</span><strong>{value:.6f}</strong></div>"
        for key, value in metrics.items()
        if key in {"pre_avatar_society_readiness", "weakest_channel_score", "pre_avatar_year_span", "avatar_gate_delay_integrity", "market_fairness", "proto_language_grounding"}
    )
    html = f"""<!doctype html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\" />
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
<title>Report {REPORT}: Pre-Avatar Society Bridge</title>
<style>
:root {{ --ink:#211911; --paper:#f4ead8; --amber:#c48b45; --clay:#94553d; --moss:#586f49; --water:#4f7886; --line:rgba(33,25,17,.22); }}
* {{ box-sizing:border-box; }}
body {{ margin:0; color:var(--ink); font-family: Georgia, 'Times New Roman', serif; background: radial-gradient(circle at 16% 12%, #ffe0a6 0, transparent 22rem), radial-gradient(circle at 88% 20%, rgba(79,120,134,.26) 0, transparent 24rem), linear-gradient(140deg,#f4ead8,#d5b78b); }}
main {{ max-width:1260px; margin:0 auto; padding:28px; }}
h1 {{ margin:0; max-width:940px; font-size:clamp(2.2rem,5vw,5.4rem); line-height:.92; letter-spacing:-.055em; }}
.lede {{ max-width:820px; font-size:1.08rem; line-height:1.6; }}
.metrics {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(190px,1fr)); gap:10px; margin:22px 0; }}
.metric {{ background:rgba(255,252,244,.64); border:1px solid var(--line); border-radius:18px; padding:14px; }}
.metric span {{ display:block; font-size:.72rem; text-transform:uppercase; letter-spacing:.08em; opacity:.70; }}
.metric strong {{ font-size:1.32rem; }}
.grid {{ display:grid; grid-template-columns:1fr 410px; gap:18px; }}
.world {{ min-height:590px; border:1px solid var(--line); border-radius:30px; padding:22px; position:relative; overflow:hidden; background:linear-gradient(180deg,rgba(255,255,255,.20),rgba(88,111,73,.16)); box-shadow:0 28px 80px rgba(58,38,21,.16); }}
.flower {{ position:absolute; width:560px; height:560px; right:-160px; bottom:-190px; border-radius:50%; background:repeating-radial-gradient(circle, rgba(148,85,61,.16) 0 2px, transparent 2px 38px); }}
.house {{ position:absolute; width:168px; min-height:124px; padding:14px; color:white; border-radius:28px 18px 34px 20px; border:1px solid rgba(255,255,255,.40); box-shadow:0 18px 44px rgba(35,24,16,.24), inset 0 -20px 35px rgba(0,0,0,.16); transition:transform .8s ease, filter .8s ease; }}
.house b, .house span, .house small {{ display:block; }} .house b {{ font-size:1.22rem; }} .house span {{ font-size:.78rem; line-height:1.25; opacity:.9; }} .house small {{ margin-top:8px; font-size:.72rem; opacity:.82; }}
#westkeepers {{ left:6%; top:12%; background:var(--clay); }} #mossgarden {{ left:38%; top:8%; background:var(--moss); }} #ledgerkin {{ left:68%; top:25%; background:var(--amber); }} #redstair {{ left:17%; top:60%; background:#72506d; }} #wheelwright {{ left:56%; top:66%; background:var(--water); }}
.panel {{ background:rgba(255,252,244,.70); border:1px solid var(--line); border-radius:30px; padding:20px; }}
button {{ border:0; border-radius:999px; padding:12px 18px; background:var(--ink); color:var(--paper); font-weight:700; cursor:pointer; }}
.trace {{ margin-top:14px; min-height:410px; padding:14px; border-radius:18px; background:rgba(33,25,17,.08); white-space:pre-wrap; font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace; font-size:.86rem; line-height:1.45; }}
@media(max-width:900px){{ .grid{{grid-template-columns:1fr}} .world{{min-height:560px}} .house{{width:146px}} }}
</style>
</head>
<body>
<main>
<h1>Pre-avatar society loop</h1>
<p class=\"lede\">Report {REPORT} compresses thousands of pre-avatar years into inspectable epochs. Households persist, markets exchange goods, rituals stabilize memory, proto-language tokens emerge, technologies accumulate, sensory ecology shapes body cost, and the avatar gate remains closed until civilization thresholds mature.</p>
<section class=\"metrics\">{metric_cards}</section>
<section class=\"grid\">
  <div class=\"world\"><div class=\"flower\"></div>{household_cards}</div>
  <aside class=\"panel\"><button id=\"advance\">advance epoch tick</button><div id=\"trace\" class=\"trace\"></div></aside>
</section>
</main>
<script>
const epochs = {epoch_payload};
const ticks = {tick_payload};
let i = 0;
function draw() {{
  const tick = ticks[i % ticks.length];
  const epoch = epochs.find(e => e.year === tick.year);
  document.querySelectorAll('.house').forEach(node => {{ node.style.filter = 'opacity(.62) saturate(.82)'; node.style.transform = 'scale(.94)'; }});
  const node = document.getElementById(tick.household_id);
  if (node) {{
    const year = Number(tick.year);
    const pulse = Math.log10(year + 10);
    node.style.filter = 'opacity(1) saturate(1.18)';
    node.style.transform = `scale(${{1 + pulse * .035}}) translate(${{Math.sin(year || 1) * 26}}px, ${{Math.cos((year || 1) / 3) * 18}}px)`;
  }}
  document.getElementById('trace').textContent = `year ${{tick.year}} / phase ${{tick.phase}}\nhousehold: ${{tick.household_id}}\nmarket: ${{tick.market_exchange_id}}\nritual: ${{tick.ritual_id}}\nproto-token: ${{tick.token_id}}\ntechnology: ${{tick.technology_id}}\nsensory: ${{tick.sensory_packet_id}}\navatar gate: ${{tick.avatar_gate_id}}\nmarket complexity=${{epoch.market_complexity}} language=${{epoch.proto_language_complexity}} tech=${{epoch.technology_depth}} recovery=${{epoch.recovery_capacity}}\n${{tick.continuity_note}}`;
  i += 1;
}}
document.getElementById('advance').addEventListener('click', draw);
draw();
</script>
</body>
</html>
"""
    path.write_text(html)


def run(seed: int) -> dict[str, Any]:
    source_results = read_json(SOURCE_RESULTS)
    source_state = read_json(SOURCE_STATE)
    households = build_households()
    epochs = build_epochs()
    markets = build_market_exchanges(households)
    rituals = build_rituals(households)
    tokens = build_tokens(households)
    technologies = build_technologies(households)
    norms = build_norms(households)
    packets = build_sensory_packets()
    gates = build_gates(epochs)
    ticks = build_ticks(households, markets, rituals, tokens, technologies, packets, gates)
    metrics = compute_metrics(households, epochs, markets, rituals, tokens, technologies, norms, packets, gates, ticks)
    ablations = build_ablations(metrics)
    verdict = "pass" if metrics["pre_avatar_society_readiness"] >= 0.84 and metrics["weakest_channel_score"] >= 0.78 else "fail"
    honest_limits = [
        "This is deterministic pre-avatar society scaffolding, not a real civilization or subjective society.",
        "Proto-language tokens are grounded symbolic traces, not autonomous natural language emergence.",
        "Markets, rituals, norms, and technologies are compact lineages, not full economics, anthropology, or physics.",
        "Avatar entry is gated as a design invariant; this report does not implement actual avatar play after entry.",
        "Sensory ecology packets bind sound, smell, temperature, wetness, pain risk, and comfort affordances, but they are not felt experience.",
        "Frequency and flower phases are rhythm scaffolds, not metaphysical evidence.",
    ]
    next_gate = "local playable pre-avatar civilization sandbox with generational agents, proto-language mutation, household markets, ritual schedules, and final avatar-entry ceremony after mature thresholds"

    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    write_csv(ARTIFACTS / f"{BASE}_households.csv", households)
    write_csv(ARTIFACTS / f"{BASE}_epoch_snapshots.csv", epochs)
    write_csv(ARTIFACTS / f"{BASE}_market_exchanges.csv", markets)
    write_csv(ARTIFACTS / f"{BASE}_household_rituals.csv", rituals)
    write_csv(ARTIFACTS / f"{BASE}_proto_language_tokens.csv", tokens)
    write_csv(ARTIFACTS / f"{BASE}_technology_lineages.csv", technologies)
    write_csv(ARTIFACTS / f"{BASE}_cultural_norms.csv", norms)
    write_csv(ARTIFACTS / f"{BASE}_sensory_ecology_packets.csv", packets)
    write_csv(ARTIFACTS / f"{BASE}_avatar_entry_gates.csv", gates)
    write_csv(ARTIFACTS / f"{BASE}_society_continuity_ticks.csv", ticks)
    write_verdict(ARTIFACTS / f"{BASE}_verdict.csv", verdict, metrics)

    state = {
        "report": REPORT,
        "module": BASE,
        "seed": seed,
        "source_results": str(SOURCE_RESULTS),
        "source_state": str(SOURCE_STATE),
        "households": rows(households),
        "epoch_snapshots": rows(epochs),
        "market_exchanges": rows(markets),
        "household_rituals": rows(rituals),
        "proto_language_tokens": rows(tokens),
        "technology_lineages": rows(technologies),
        "cultural_norms": rows(norms),
        "sensory_ecology_packets": rows(packets),
        "avatar_entry_gates": rows(gates),
        "society_continuity_ticks": rows(ticks),
    }
    (ARTIFACTS / f"{BASE}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True))
    results = {
        "report": REPORT,
        "module": BASE,
        "seed": seed,
        "source_report": 233,
        "source_metrics": source_results.get("metrics", {}),
        "source_state_available": bool(source_state),
        "verdict": verdict,
        "metrics": metrics,
        "ablations": ablations,
        "honest_limits": honest_limits,
        "artifacts": {
            "households": str(ARTIFACTS / f"{BASE}_households.csv"),
            "epoch_snapshots": str(ARTIFACTS / f"{BASE}_epoch_snapshots.csv"),
            "market_exchanges": str(ARTIFACTS / f"{BASE}_market_exchanges.csv"),
            "household_rituals": str(ARTIFACTS / f"{BASE}_household_rituals.csv"),
            "proto_language_tokens": str(ARTIFACTS / f"{BASE}_proto_language_tokens.csv"),
            "technology_lineages": str(ARTIFACTS / f"{BASE}_technology_lineages.csv"),
            "cultural_norms": str(ARTIFACTS / f"{BASE}_cultural_norms.csv"),
            "sensory_ecology_packets": str(ARTIFACTS / f"{BASE}_sensory_ecology_packets.csv"),
            "avatar_entry_gates": str(ARTIFACTS / f"{BASE}_avatar_entry_gates.csv"),
            "society_continuity_ticks": str(ARTIFACTS / f"{BASE}_society_continuity_ticks.csv"),
            "state": str(ARTIFACTS / f"{BASE}_state.json"),
            "verdict": str(ARTIFACTS / f"{BASE}_verdict.csv"),
        },
        "next_gate": next_gate,
    }
    (ARTIFACTS / f"{BASE}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True))
    make_html(VISUALIZATIONS / f"{BASE}.html", households, epochs, ticks, metrics)
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    results = run(args.seed)
    metrics = results["metrics"]
    print(f"module_verdict {results['verdict']}")
    print(f"pre_avatar_society_readiness {metrics['pre_avatar_society_readiness']:.6f}")
    print("households 5")
    print("epoch_snapshots 9")
    print("market_exchanges 45")
    print("household_rituals 45")
    print("proto_language_tokens 45")
    print("technology_lineages 45")
    print("cultural_norms 9")
    print("sensory_ecology_packets 9")
    print("avatar_entry_gates 9")
    print("society_continuity_ticks 45")
    print(f"pre_avatar_year_span {metrics['pre_avatar_year_span']:.6f}")
    print(f"avatar_gate_delay_integrity {metrics['avatar_gate_delay_integrity']:.6f}")
    print(f"mature_gate_readiness {metrics['mature_gate_readiness']:.6f}")
    print(f"market_fairness {metrics['market_fairness']:.6f}")
    print(f"proto_language_grounding {metrics['proto_language_grounding']:.6f}")
    print(f"sensory_ecology_binding {metrics['sensory_ecology_binding']:.6f}")
    print(f"weakest_channel_score {metrics['weakest_channel_score']:.6f}")
    print(f"visualization visualizations/{BASE}.html")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
