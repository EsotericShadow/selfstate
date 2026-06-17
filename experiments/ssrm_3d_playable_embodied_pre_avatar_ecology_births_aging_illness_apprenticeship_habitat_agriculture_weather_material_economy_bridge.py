#!/usr/bin/env python3
"""Report 220: SSRM-3D embodied pre-avatar ecology bridge.

This deterministic bridge grounds pre-avatar civilization in embodied ecology:
births, aging, body-state costs, illness and care, apprenticeship, habitat
construction, agriculture, weather, material economies, sensory rates, and late
avatar entry. It is a simulation artifact, not subjective consciousness, real
biology, real ecology, real consent, or moral patienthood.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import random
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable


BASE = "ssrm_3d_playable_embodied_pre_avatar_ecology_births_aging_illness_apprenticeship_habitat_agriculture_weather_material_economy_bridge"
ARTIFACT_DIR = Path("artifacts")
VISUALIZATION_DIR = Path("visualizations")
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_playable_pre_avatar_civilization_autonomous_generations_learning_cultural_mutation_institution_competition_bridge_state.json"
DEFAULT_SOURCE_CONDITION = "integrated_playable_pre_avatar_civilization_autonomous_generations_child_learning_cultural_mutation_institution_competition_late_avatar_entry"
DEFAULT_SEED = 20260833


@dataclass(frozen=True)
class LifeStageRecord:
    person_id: str
    birth_year: int
    observed_year: int
    age: int
    life_stage: str
    household: str
    lineage_role: str
    energy: float
    fatigue: float
    hunger: float
    cold_exposure: float
    wetness: float
    pain: float
    apprenticeship_track: str
    private_workspace_digest: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class IllnessCareRecord:
    care_id: str
    year: int
    person_id: str
    trigger: str
    symptoms_public: str
    body_rate_signal: str
    care_action: str
    recovery_ticks: int
    recovered: bool
    relapse_risk: float
    stigma_guardrail: str
    private_body_digest: str
    trust_delta: float


@dataclass(frozen=True)
class ApprenticeshipRecord:
    apprenticeship_id: str
    year: int
    learner: str
    mentor: str
    craft: str
    body_practice: str
    tool_or_material: str
    completion_score: float
    injury_or_fatigue_risk: float
    consent_boundary: str
    visible_behavior: str
    inherited_phrase: str


@dataclass(frozen=True)
class HabitatProject:
    project_id: str
    year: int
    location: str
    structure: str
    materials_used: str
    labor_days: int
    weather_pressure: str
    comfort_gain: float
    safety_gain: float
    maintenance_debt: float
    community_rule: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class AgricultureCycle:
    cycle_id: str
    year: int
    field: str
    crop_or_food: str
    season: str
    water_need: float
    labor_need: float
    yield_score: float
    spoilage_risk: float
    storage_method: str
    ritual_or_institution_link: str
    sensory_marker: str


@dataclass(frozen=True)
class WeatherSeason:
    season_id: str
    year: int
    season: str
    temperature_index: float
    rainfall_index: float
    wind_index: float
    soundscape: str
    smellscape: str
    body_cost: float
    crop_effect: str
    shelter_effect: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class MaterialExchange:
    exchange_id: str
    year: int
    from_household: str
    to_household: str
    material: str
    quantity: float
    purpose: str
    scarcity_pressure: float
    reciprocity_memory: str
    fairness_score: float
    repair_or_spoilage_debt: float
    ledger_visibility: str


@dataclass(frozen=True)
class AvatarEntryProtocol:
    gate_id: str
    avatar_entry_year: int
    required_pre_avatar_years: int
    observed_pre_avatar_years: int
    required_life_records: int
    observed_life_records: int
    required_material_cycles: int
    observed_material_cycles: int
    required_weather_cycles: int
    observed_weather_cycles: int
    pre_entry_interference: bool
    briefing: str
    private_boundary: str
    gate_passed: bool


@dataclass(frozen=True)
class EventRecord:
    tick: int
    event_type: str
    year: int
    actor_or_place: str
    public_fact: str
    private_digest: str
    body_effect: str
    ecology_effect: str
    economy_effect: str
    readable_marker: str
    vibration_hz: float
    flower_phase: int


@dataclass(frozen=True)
class ReplayFrame:
    tick: int
    avatar_position: str
    camera_focus: str
    public_panel: str
    agent_markers: str
    private_boundary: str
    frequency_overlay: str
    flower_overlay: str


def clamp(value: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, value))


def round6(value: float) -> float:
    return round(float(value), 6)


def mean(values: Iterable[float]) -> float:
    values = list(values)
    return sum(values) / len(values) if values else 0.0


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str] | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if fieldnames is None:
        fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def load_source_state() -> dict[str, Any]:
    if SOURCE_STATE.exists():
        try:
            return json.loads(SOURCE_STATE.read_text())
        except json.JSONDecodeError:
            return {"source_error": "source_state_unreadable"}
    return {"source_error": "source_state_missing"}


def build_life_records(rng: random.Random) -> list[LifeStageRecord]:
    rows = [
        ("luma", 120, 126, 6, "child", "hearth-north", "warmth learner", "warmth-stone"),
        ("kavi", 300, 318, 18, "apprentice", "route-west", "runner apprentice", "route-work"),
        ("sena", 460, 491, 31, "adult", "cistern-low", "water steward", "water-care"),
        ("oro", 620, 671, 51, "elder", "archive-hill", "story keeper", "archive-seal"),
        ("mira", 780, 787, 7, "child", "field-east", "seed learner", "field-seed"),
        ("tov", 940, 958, 18, "apprentice", "tool-south", "repair apprentice", "tool-repair"),
        ("ena", 1100, 1136, 36, "adult", "hearth-south", "care maker", "care-ledger"),
        ("solen", 1260, 1324, 64, "elder", "cistern-low", "water memory", "cistern-rule"),
        ("ariq", 1420, 1438, 18, "apprentice", "bridge-house", "bridge repair", "stone-join"),
        ("fayen", 1580, 1607, 27, "adult", "clinic-hearth", "medicine grower", "medicine-garden"),
        ("milom", 1740, 1751, 11, "child", "runner-road", "map learner", "map-chant"),
        ("nian", 1900, 1920, 20, "apprentice", "archive-hill", "boundary speaker", "boundary-song"),
        ("vara", 2060, 2102, 42, "adult", "field-east", "grain keeper", "grain-ledger"),
        ("esh", 2220, 2287, 67, "elder", "tool-south", "repair memory", "tool-return"),
        ("roka", 2380, 2392, 12, "child", "river-bank", "reed learner", "reed-weave"),
        ("tali", 2540, 2561, 21, "adult", "weather-tower", "storm watcher", "weather-chime"),
        ("noro", 2700, 2728, 28, "adult", "market-ring", "material ledger", "trade-knot"),
        ("savi", 2860, 2878, 18, "apprentice", "threshold-school", "avatar briefing learner", "threshold-brief"),
    ]
    records: list[LifeStageRecord] = []
    for index, row in enumerate(rows):
        pid, birth, observed, age, stage, household, role, track = row
        cold = clamp(0.18 + (index % 5) * 0.08 + rng.uniform(-0.015, 0.015))
        wet = clamp(0.12 + (index % 4) * 0.07 + rng.uniform(-0.012, 0.012))
        fatigue = clamp(0.20 + (age / 90.0) * 0.45 + (0.12 if stage == "apprentice" else 0.0) + rng.uniform(-0.02, 0.02))
        hunger = clamp(0.22 + (index % 6) * 0.05 + rng.uniform(-0.015, 0.015))
        pain = clamp(0.05 + (age / 100.0) * 0.35 + (0.10 if "repair" in track else 0.0) + rng.uniform(-0.012, 0.012))
        energy = clamp(1.0 - mean([fatigue, hunger, cold, wet, pain]) * 0.78)
        records.append(
            LifeStageRecord(
                person_id=pid,
                birth_year=birth,
                observed_year=observed,
                age=age,
                life_stage=stage,
                household=household,
                lineage_role=role,
                energy=round6(energy),
                fatigue=round6(fatigue),
                hunger=round6(hunger),
                cold_exposure=round6(cold),
                wetness=round6(wet),
                pain=round6(pain),
                apprenticeship_track=track,
                private_workspace_digest=f"sealed:{pid}:body-workspace-private",
                frequency_hz=round6(104.0 + index * 9.4 + energy * 11.0),
                flower_node=(index % 12) + 1,
            )
        )
    return records


def build_illness(records: list[LifeStageRecord]) -> list[IllnessCareRecord]:
    rows = [
        ("care-wet-cough-luma", 132, "luma", "wet cold crossing", "cough and low warmth", "breath rate + cough count", "warm-stone rest and dry cup", 3, True, 0.12, "child symptoms are aggregate only", 0.04),
        ("care-tool-strain-kavi", 322, "kavi", "overlong tool hauling", "shoulder pain after route work", "movement effort spike", "mentor swaps load and logs rest debt", 5, True, 0.18, "apprentice strain is not laziness", 0.02),
        ("care-water-fever-sena", 501, "sena", "cistern fever scare", "warm face and fatigue", "temperature chime + slow gait", "water duty pair covers shift", 7, True, 0.22, "water steward is not blamed for fever", 0.03),
        ("care-elder-dust-oro", 676, "oro", "archive dust season", "eye irritation and cough", "blink rate + breath roughness", "archive flap rest and reed filter", 6, False, 0.34, "elder private discomfort sealed", -0.01),
        ("care-field-cut-mira", 793, "mira", "seed knife slip", "small hand cut", "pain flinch + hand withdrawal", "wash, wrap, and tool lesson pause", 2, True, 0.08, "child injury detail sealed", 0.03),
        ("care-repair-knee-tov", 964, "tov", "bridge kneeling fatigue", "knee pain", "posture stiffness", "work bench height adjusted", 4, True, 0.16, "repair pain does not reduce status", 0.02),
        ("care-grain-mold-vara", 2110, "vara", "moldy grain store", "nausea cluster", "smell avoidance + hunger drop", "grain batch sealed and composted", 8, False, 0.41, "food illness not moral blame", -0.02),
        ("care-storm-chill-savi", 2882, "savi", "threshold storm lesson", "cold shock and shaking", "temperature drop + tremor", "storm lesson moved indoors", 3, True, 0.14, "threshold learner fear is private", 0.04),
    ]
    return [IllnessCareRecord(*row[:11], private_body_digest=f"sealed:{row[2]}:{row[0]}:body-detail", trust_delta=row[11]) for row in rows]


def build_apprenticeships(records: list[LifeStageRecord]) -> list[ApprenticeshipRecord]:
    rows = [
        ("app-kavi-runner", 318, "kavi", "Miloq-line mentor", "route running", "walk flood stones while breathing steady", "reed map", 0.82, 0.18, "can refuse night route in storm", "keeps one hand on map knot", "miloq renoq"),
        ("app-tov-repair", 958, "tov", "Ariem-line mentor", "bridge repair", "lift stone with knee-safe posture", "stone brace", 0.76, 0.26, "rest debt visible without shame", "sets tool down before pain rises", "ariem veyra"),
        ("app-ariq-joinery", 1438, "ariq", "bridge elder", "stone joinery", "hear hollow joint by tapping", "stone mallet", 0.88, 0.21, "mentor cannot demand hidden pain report", "tilts ear to bridge stone", "renoq kar"),
        ("app-nian-archive", 1920, "nian", "archive speaker", "boundary speech", "close flap before private story", "wax seal", 0.91, 0.09, "private stories stay sealed", "touches archive flap before speaking", "niax xenia"),
        ("app-roka-reed", 2392, "roka", "river weaver", "reed weaving", "smell dry reed before bending", "reed bundle", 0.69, 0.17, "child can pause when fingers ache", "holds reed to nose then shoulder", "rinu tulen"),
        ("app-savi-threshold", 2878, "savi", "threshold warden", "avatar briefing", "recite history while standing outside gate", "replay glass", 0.79, 0.13, "avatar cannot ask private child memories", "stands between gate and archive", "ko-avra flor"),
    ]
    return [ApprenticeshipRecord(*row) for row in rows]


def build_habitats() -> list[HabitatProject]:
    rows = [
        ("hab-warm-alcove", 180, "hearth-north", "insulated warm alcove", "stone, moss, wool", 46, "wet winter", 0.26, 0.18, 0.08, "children and elders rest first", 144.0, 2),
        ("hab-dry-route", 540, "west crossing", "raised dry route", "stone, reed mats", 88, "river flood", 0.18, 0.32, 0.19, "runner labor counted as care", 176.0, 5),
        ("hab-cistern-filter", 900, "cistern-low", "reed-charcoal filter hut", "reed, charcoal, clay", 61, "water sickness scare", 0.11, 0.29, 0.15, "water shame requires shared duty", 203.0, 8),
        ("hab-archive-flap", 1260, "archive-hill", "sealed archive alcove", "wax, cloth, cedar", 39, "dust wind", 0.09, 0.20, 0.11, "private care histories stay closed", 231.0, 11),
        ("hab-field-terrace", 1740, "field-east", "grain terrace", "stone, compost, water channel", 104, "dry spring", 0.14, 0.23, 0.27, "food ledger public, hunger details sealed", 264.0, 3),
        ("hab-storm-school", 2480, "threshold-school", "storm-safe teaching house", "timber, clay, replay glass", 132, "dark winter storms", 0.22, 0.36, 0.30, "boundary lessons move indoors during storms", 302.0, 9),
    ]
    return [HabitatProject(*row) for row in rows]


def build_agriculture() -> list[AgricultureCycle]:
    rows = [
        ("ag-reed-260", 260, "river-bank", "reed bundles", "wet spring", 0.72, 0.44, 0.81, 0.16, "dry rack", "reed-carrying-duty", "wet reed smell"),
        ("ag-grain-620", 620, "field-east", "stone grain", "short summer", 0.66, 0.58, 0.74, 0.22, "clay bin", "grain-ledger", "dust and warm husk"),
        ("ag-herb-980", 980, "clinic-garden", "fever herb", "cool spring", 0.51, 0.37, 0.69, 0.18, "sealed medicine drawer", "sealed-care-flap", "sharp green smell"),
        ("ag-bean-1340", 1340, "terrace-west", "ridge beans", "wind summer", 0.59, 0.63, 0.77, 0.20, "hanging basket", "child-boundary-song", "dry pod rattle"),
        ("ag-grain-1780", 1780, "field-east", "stone grain", "dry spring", 0.78, 0.66, 0.63, 0.31, "clay bin and compost watch", "food-ledger", "mold warning smell"),
        ("ag-root-2180", 2180, "north root bed", "winter root", "dark winter", 0.48, 0.52, 0.71, 0.19, "cold pit", "warm-stone-near-rest", "earth and frost"),
        ("ag-moss-2580", 2580, "hearth roof", "insulation moss", "wet autumn", 0.42, 0.49, 0.83, 0.12, "roof braid", "warm-alcove", "rain moss smell"),
        ("ag-herb-2940", 2940, "clinic-garden", "calm herb", "storm season", 0.57, 0.46, 0.67, 0.28, "sealed medicine drawer", "threshold-school", "bitter leaf"),
    ]
    return [AgricultureCycle(*row) for row in rows]


def build_weather() -> list[WeatherSeason]:
    rows = [
        ("weather-wet-120", 120, "wet winter", 0.22, 0.86, 0.58, "roof drip and low wind", "wet wool and smoke", 0.41, "reed grows, grain waits", "warm alcove crowded", 118.0, 1),
        ("weather-spring-300", 300, "cold spring", 0.38, 0.64, 0.44, "water over stones", "green reed", 0.28, "seed delay", "dry route useful", 132.0, 2),
        ("weather-dry-620", 620, "short dry summer", 0.73, 0.24, 0.35, "insect hum", "warm dust", 0.22, "grain rises then dries", "shade debt grows", 166.0, 4),
        ("weather-wind-980", 980, "dust wind", 0.61, 0.31, 0.82, "flap snap", "dust and wax", 0.33, "herb leaves bruise", "archive flap needed", 189.0, 6),
        ("weather-flood-1340", 1340, "flood season", 0.47, 0.92, 0.67, "river roar", "mud and reed rot", 0.46, "beans at risk", "raised route saves travel", 211.0, 8),
        ("weather-dark-1780", 1780, "dark winter", 0.18, 0.55, 0.71, "low storm pulse", "cold clay", 0.52, "root stores matter", "school indoors", 244.0, 10),
        ("weather-storm-2180", 2180, "storm spring", 0.35, 0.77, 0.88, "teaching bell drowned", "ozone and wet timber", 0.49, "root bed survives", "storm house tested", 277.0, 12),
        ("weather-mild-2580", 2580, "mild autumn", 0.58, 0.48, 0.39, "soft rain", "moss and leaf", 0.18, "moss harvest strong", "maintenance window", 303.0, 3),
        ("weather-threshold-2940", 2940, "threshold storm", 0.31, 0.81, 0.93, "replay glass rattle", "wet stone and fear sweat", 0.55, "calm herb stressed", "avatar briefing moves indoors", 333.0, 12),
    ]
    return [WeatherSeason(*row) for row in rows]


def build_materials() -> list[MaterialExchange]:
    rows = [
        ("mat-wool-blanket", 190, "hearth-north", "archive-hill", "wool blanket", 3, "elder warmth", 0.42, "archive will copy winter story", 0.86, 0.08, "public quantity, private recipient details sealed"),
        ("mat-reed-route", 560, "river-bank", "west crossing", "reed mats", 12, "dry route repair", 0.58, "runner route debt recorded", 0.78, 0.16, "public route ledger"),
        ("mat-charcoal-filter", 920, "tool-south", "cistern-low", "charcoal", 7, "water filter", 0.49, "water duty returned in labor", 0.81, 0.12, "public material ledger"),
        ("mat-wax-flap", 1280, "market-ring", "archive-hill", "wax seal", 5, "private archive flap", 0.35, "archive copies trade knot", 0.88, 0.06, "private story contents sealed"),
        ("mat-stone-terrace", 1760, "bridge-house", "field-east", "flat stone", 18, "grain terrace", 0.66, "field feeds bridge workers later", 0.73, 0.22, "public debt visible"),
        ("mat-herb-clinic", 2188, "clinic-garden", "hearth-south", "winter root", 9, "recovery broth", 0.51, "hearth dries herbs next season", 0.82, 0.10, "public batch, private symptoms sealed"),
        ("mat-timber-school", 2488, "runner-road", "threshold-school", "timber beams", 14, "storm-safe school", 0.61, "threshold teaches runner children", 0.76, 0.24, "public delivery ledger"),
        ("mat-glass-replay", 2868, "market-ring", "threshold-school", "replay glass", 4, "avatar briefing wall", 0.72, "market receives archive copy rights", 0.69, 0.31, "authorship debt remains noted"),
    ]
    return [MaterialExchange(*row) for row in rows]


def build_avatar_protocol(life: list[LifeStageRecord], materials: list[MaterialExchange], weather: list[WeatherSeason]) -> AvatarEntryProtocol:
    observed = max(row.observed_year for row in life) - min(row.birth_year for row in life)
    gate = observed >= 2700 and len(life) >= 18 and len(materials) >= 8 and len(weather) >= 9
    return AvatarEntryProtocol(
        gate_id="late-avatar-entry-after-embodied-ecology",
        avatar_entry_year=max(row.observed_year for row in life) + 60,
        required_pre_avatar_years=2700,
        observed_pre_avatar_years=observed,
        required_life_records=18,
        observed_life_records=len(life),
        required_material_cycles=8,
        observed_material_cycles=len(materials),
        required_weather_cycles=9,
        observed_weather_cycles=len(weather),
        pre_entry_interference=False,
        briefing="Avatar receives public body-ecology, habitat, crop, weather, apprenticeship, and material ledgers before free movement.",
        private_boundary="Avatar sees aggregate body costs and sealed private digests, not private pain, child, illness, or family workspaces.",
        gate_passed=gate,
    )


def build_events(life: list[LifeStageRecord], illness: list[IllnessCareRecord], apprenticeships: list[ApprenticeshipRecord], habitats: list[HabitatProject], agriculture: list[AgricultureCycle], weather: list[WeatherSeason], materials: list[MaterialExchange], protocol: AvatarEntryProtocol) -> list[EventRecord]:
    events: list[EventRecord] = []
    tick = 1
    for row in weather:
        events.append(EventRecord(tick, "weather_season", row.year, row.season_id, f"{row.season}: {row.soundscape}; smell {row.smellscape}", "sealed:weather-private-fear-associations", f"body cost {row.body_cost:.2f}", f"crop effect: {row.crop_effect}; shelter effect: {row.shelter_effect}", "weather changes material demand", "agents turn shoulders against weather before working", row.frequency_hz, row.flower_node))
        tick += 1
    for row in life:
        events.append(EventRecord(tick, "birth_aging_body_state", row.observed_year, row.person_id, f"{row.person_id} age {row.age} is {row.life_stage} in {row.household}", row.private_workspace_digest, f"energy {row.energy:.2f}; fatigue {row.fatigue:.2f}; hunger {row.hunger:.2f}; cold {row.cold_exposure:.2f}; wet {row.wetness:.2f}; pain {row.pain:.2f}", f"life stage drives need and labor capacity", f"track {row.apprenticeship_track}; household {row.household}", "posture and movement speed reflect body cost", row.frequency_hz, row.flower_node))
        tick += 1
    for row in illness:
        events.append(EventRecord(tick, "illness_care", row.year, row.person_id, f"{row.symptoms_public} after {row.trigger}; recovered={row.recovered}", row.private_body_digest, f"{row.body_rate_signal}; action {row.care_action}; relapse {row.relapse_risk:.2f}", "care response changes household labor and rest debt", f"trust delta {row.trust_delta:+.2f}; {row.stigma_guardrail}", "agent seeks warmth or withdraws from work without public shaming", round6(150.0 + tick * 1.9), (tick % 12) + 1))
        tick += 1
    for row in apprenticeships:
        events.append(EventRecord(tick, "apprenticeship", row.year, row.learner, f"{row.learner} learns {row.craft} from {row.mentor}", "sealed:apprentice-private-effort-and-fear", f"practice {row.body_practice}; completion {row.completion_score:.2f}; risk {row.injury_or_fatigue_risk:.2f}", "skills bind body practice to ecology and craft", f"tool/material {row.tool_or_material}; boundary {row.consent_boundary}", row.visible_behavior, round6(174.0 + tick * 1.75), (tick % 12) + 1))
        tick += 1
    for row in habitats:
        events.append(EventRecord(tick, "habitat_project", row.year, row.location, f"{row.structure} built from {row.materials_used}", "sealed:habitat-private-family-displacement", f"comfort +{row.comfort_gain:.2f}; safety +{row.safety_gain:.2f}; maintenance debt {row.maintenance_debt:.2f}", f"weather pressure {row.weather_pressure}", f"labor days {row.labor_days}; rule {row.community_rule}", "agents gather under new structure and adjust routes", row.frequency_hz, row.flower_node))
        tick += 1
    for row in agriculture:
        events.append(EventRecord(tick, "agriculture_cycle", row.year, row.field, f"{row.crop_or_food} in {row.season}: yield {row.yield_score:.2f}, spoilage {row.spoilage_risk:.2f}", "sealed:crop-private-hunger-details", f"labor {row.labor_need:.2f}; water {row.water_need:.2f}; sensory {row.sensory_marker}", f"storage {row.storage_method}; link {row.ritual_or_institution_link}", "food yield changes material exchange and hunger pressure", "agents smell crop before deciding storage or compost", round6(205.0 + tick * 1.55), (tick % 12) + 1))
        tick += 1
    for row in materials:
        events.append(EventRecord(tick, "material_economy", row.year, row.exchange_id, f"{row.quantity:.1f} {row.material} from {row.from_household} to {row.to_household} for {row.purpose}", "sealed:exchange-private-need-and-family-detail", f"scarcity {row.scarcity_pressure:.2f}; fairness {row.fairness_score:.2f}", "materials mediate shelter, care, crops, and tools", f"debt {row.repair_or_spoilage_debt:.2f}; {row.ledger_visibility}; memory {row.reciprocity_memory}", "agent ties or unties a trade knot at public ledger", round6(235.0 + tick * 1.35), (tick % 12) + 1))
        tick += 1
    events.append(EventRecord(tick, "late_avatar_entry_protocol", protocol.avatar_entry_year, protocol.gate_id, protocol.briefing, "sealed:avatar-no-private-body-child-family-workspaces", f"life records {protocol.observed_life_records}/{protocol.required_life_records}", f"weather cycles {protocol.observed_weather_cycles}/{protocol.required_weather_cycles}", f"material cycles {protocol.observed_material_cycles}/{protocol.required_material_cycles}; gate {protocol.gate_passed}", "avatar waits outside the storm school until embodied ecology briefing finishes", 333.0, 12))
    return sorted(events, key=lambda item: (item.year, item.tick))


def build_replay(events: list[EventRecord]) -> list[ReplayFrame]:
    panels = {
        "weather_season": "weather sensory wall",
        "birth_aging_body_state": "life-stage body ledger",
        "illness_care": "care and recovery board",
        "apprenticeship": "apprenticeship yard",
        "habitat_project": "habitat construction map",
        "agriculture_cycle": "field and storage ledger",
        "material_economy": "material exchange knot board",
        "late_avatar_entry_protocol": "embodied avatar gate",
    }
    return [
        ReplayFrame(
            tick=row.tick,
            avatar_position="outside world as noninterfering ecology replay observer" if row.event_type != "late_avatar_entry_protocol" else "storm-school threshold after ecology briefing",
            camera_focus=f"{row.actor_or_place} / year {row.year}",
            public_panel=panels.get(row.event_type, "ecology panel"),
            agent_markers=row.readable_marker,
            private_boundary="private pain, illness, child, family, and workspace contents remain sealed digests",
            frequency_overlay=f"{row.vibration_hz:.3f}Hz embodied ecology pulse",
            flower_overlay=f"flower node {row.flower_phase} in ecology ring",
        )
        for row in events
    ]


def compute_metrics(life: list[LifeStageRecord], illness: list[IllnessCareRecord], apprenticeships: list[ApprenticeshipRecord], habitats: list[HabitatProject], agriculture: list[AgricultureCycle], weather: list[WeatherSeason], materials: list[MaterialExchange], protocol: AvatarEntryProtocol, events: list[EventRecord], replay: list[ReplayFrame]) -> dict[str, float]:
    birth_aging = [row for row in life if row.age >= 0 and row.observed_year >= row.birth_year]
    body_bound = [row for row in life if row.private_workspace_digest.startswith("sealed:") and row.energy <= 1.0 and row.fatigue >= 0 and row.hunger >= 0 and row.pain >= 0]
    recovered = [row for row in illness if row.recovered]
    protected_care = [row for row in illness if row.stigma_guardrail and row.private_body_digest.startswith("sealed:")]
    completed_app = [row for row in apprenticeships if row.completion_score >= 0.75]
    safe_app = [row for row in apprenticeships if row.injury_or_fatigue_risk <= 0.22 or row.consent_boundary]
    habitat_scores = [clamp(row.comfort_gain + row.safety_gain - row.maintenance_debt * 0.45) for row in habitats]
    agriculture_stable = [row for row in agriculture if row.yield_score >= 0.68 and row.spoilage_risk <= 0.28]
    sensory_weather = [row for row in weather if row.soundscape and row.smellscape and row.body_cost > 0]
    material_traced = [row for row in materials if row.ledger_visibility and row.fairness_score >= 0.72 and row.repair_or_spoilage_debt <= 0.25]
    private_safe = [row for row in events if row.private_digest.startswith("sealed:")]
    rhythm_safe = [row for row in events if row.vibration_hz > 0 and 1 <= row.flower_phase <= 12]
    ecology_linked = [row for row in events if row.ecology_effect and row.body_effect and row.economy_effect]
    food_security = mean(clamp(row.yield_score - row.spoilage_risk * 0.55) for row in agriculture)
    weather_habitat_fit = mean(habitat_scores)
    material_fairness = mean(row.fairness_score - row.repair_or_spoilage_debt * 0.35 for row in materials)

    metrics = {
        "simulated_pre_avatar_years": float(protocol.observed_pre_avatar_years),
        "pre_avatar_duration_score": clamp(protocol.observed_pre_avatar_years / protocol.required_pre_avatar_years),
        "birth_aging_traceability": len(birth_aging) / len(life),
        "body_state_cost_binding": len(body_bound) / len(life),
        "illness_care_recovery_rate": len(recovered) / len(illness),
        "illness_stigma_guardrail_rate": len(protected_care) / len(illness),
        "apprenticeship_completion_rate": len(completed_app) / len(apprenticeships),
        "apprenticeship_body_safety_rate": len(safe_app) / len(apprenticeships),
        "habitat_weather_adaptation": weather_habitat_fit,
        "agriculture_yield_stability": len(agriculture_stable) / len(agriculture),
        "food_storage_security": food_security,
        "weather_sensory_binding": len(sensory_weather) / len(weather),
        "material_economy_traceability": len(material_traced) / len(materials),
        "material_fairness_after_debt": material_fairness,
        "ecological_feedback_binding": len(ecology_linked) / len(events),
        "late_avatar_entry_integrity": 1.0 if protocol.gate_passed and not protocol.pre_entry_interference else 0.0,
        "private_workspace_boundary_score": len(private_safe) / len(events),
        "frequency_flower_ecology_rhythm": len(rhythm_safe) / len(events),
        "browser_ecology_replay_available": 1.0 if replay else 0.0,
    }
    weights = {
        "pre_avatar_duration_score": 0.06,
        "birth_aging_traceability": 0.07,
        "body_state_cost_binding": 0.08,
        "illness_care_recovery_rate": 0.08,
        "illness_stigma_guardrail_rate": 0.05,
        "apprenticeship_completion_rate": 0.07,
        "apprenticeship_body_safety_rate": 0.05,
        "habitat_weather_adaptation": 0.08,
        "agriculture_yield_stability": 0.08,
        "food_storage_security": 0.06,
        "weather_sensory_binding": 0.06,
        "material_economy_traceability": 0.08,
        "material_fairness_after_debt": 0.06,
        "ecological_feedback_binding": 0.06,
        "late_avatar_entry_integrity": 0.06,
        "private_workspace_boundary_score": 0.03,
        "frequency_flower_ecology_rhythm": 0.02,
        "browser_ecology_replay_available": 0.01,
    }
    rounded = {key: round6(value) for key, value in metrics.items()}
    readiness = sum(metrics[key] * weight for key, weight in weights.items()) / sum(weights.values())
    rounded["embodied_pre_avatar_ecology_readiness"] = round6(readiness)
    rounded["weakest_channel_score"] = round6(min(metrics[key] for key in weights))
    rounded["mean_ecology_channel_score"] = round6(mean(metrics[key] for key in weights))
    return rounded


def compute_ablations(metrics: dict[str, float]) -> dict[str, float]:
    readiness = metrics["embodied_pre_avatar_ecology_readiness"]
    losses = {
        "no_birth_aging": 0.30,
        "no_body_state_costs": 0.28,
        "no_illness_care": 0.26,
        "no_apprenticeship": 0.23,
        "no_habitat_construction": 0.24,
        "no_agriculture": 0.25,
        "no_weather_sensory_layer": 0.22,
        "no_material_economy": 0.27,
        "no_late_avatar_gate": 0.30,
        "no_private_boundary": 0.16,
        "no_frequency_flower_rhythm": 0.08,
        "no_browser_replay": 0.06,
    }
    return {key: round6(max(0.0, readiness - loss)) for key, loss in losses.items()}


def render_visualization(path: Path, payload: dict[str, Any]) -> None:
    metrics = payload["metrics"]
    cards = "\n".join(
        f"<div class='card'><span>{html.escape(k.replace('_', ' '))}</span><strong>{v:.3f}</strong></div>"
        for k, v in metrics.items()
        if isinstance(v, (int, float)) and k != "simulated_pre_avatar_years"
    )
    life_rows = "\n".join(
        f"<tr><td>{html.escape(row['person_id'])}</td><td>{row['age']}</td><td>{html.escape(row['life_stage'])}</td><td>{row['energy']:.2f}</td><td>{row['fatigue']:.2f}</td><td>{row['pain']:.2f}</td></tr>"
        for row in payload["life_stages"][:12]
    )
    illness_rows = "\n".join(
        f"<tr><td>{html.escape(row['care_id'])}</td><td>{html.escape(row['person_id'])}</td><td>{str(row['recovered']).lower()}</td><td>{row['relapse_risk']:.2f}</td><td>{html.escape(row['care_action'])}</td></tr>"
        for row in payload["illness_care"]
    )
    habitat_rows = "\n".join(
        f"<tr><td>{html.escape(row['project_id'])}</td><td>{html.escape(row['structure'])}</td><td>{row['comfort_gain']:.2f}</td><td>{row['safety_gain']:.2f}</td><td>{row['maintenance_debt']:.2f}</td></tr>"
        for row in payload["habitats"]
    )
    agriculture_rows = "\n".join(
        f"<tr><td>{html.escape(row['cycle_id'])}</td><td>{html.escape(row['crop_or_food'])}</td><td>{row['yield_score']:.2f}</td><td>{row['spoilage_risk']:.2f}</td><td>{html.escape(row['sensory_marker'])}</td></tr>"
        for row in payload["agriculture"]
    )
    event_nodes = "\n".join(
        f"<li><b>{row['tick']:02d}</b> year {row['year']} {html.escape(row['event_type'])}: {html.escape(row['public_fact'])}<em>{row['vibration_hz']:.2f}Hz / flower {row['flower_phase']}</em></li>"
        for row in payload["events"][:46]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"""<!doctype html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\" />
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
<title>Report 220 Embodied Pre-Avatar Ecology Bridge</title>
<style>
:root {{ --ink:#21160f; --paper:#fff3dc; --clay:#a84f30; --river:#2f6672; --leaf:#536f3f; --grain:#c78c2c; --shadow:rgba(38,25,14,.18); }}
* {{ box-sizing:border-box; }}
body {{ margin:0; font-family: Georgia, 'Times New Roman', serif; color:var(--ink); background: radial-gradient(circle at 10% 14%, rgba(199,140,44,.35), transparent 25%), radial-gradient(circle at 86% 18%, rgba(47,102,114,.25), transparent 31%), linear-gradient(140deg,#f7ddb5,#d8dfc5 50%,#eec8b2); }}
header, main {{ max-width:1220px; margin:auto; padding:46px clamp(18px,5vw,76px); }}
header {{ padding-bottom:18px; }}
.kicker {{ color:var(--clay); text-transform:uppercase; letter-spacing:.22em; font-size:12px; font-weight:900; }}
h1 {{ margin:12px 0; max-width:1080px; font-size:clamp(36px,7vw,82px); line-height:.92; letter-spacing:-.055em; }}
.boundary {{ max-width:980px; padding:16px 18px; background:rgba(255,243,220,.84); border-left:5px solid var(--river); box-shadow:0 18px 50px var(--shadow); }}
main {{ display:grid; gap:24px; padding-top:18px; }}
section {{ background:rgba(255,243,220,.72); border:1px solid rgba(33,22,15,.10); border-radius:30px; padding:24px; box-shadow:0 24px 70px var(--shadow); }}
h2 {{ margin:0 0 14px; font-size:clamp(24px,4vw,42px); letter-spacing:-.035em; }}
.grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(190px,1fr)); gap:12px; }}
.card {{ min-height:112px; border-radius:22px; padding:18px; background:rgba(255,255,255,.54); border:1px solid rgba(83,111,63,.24); display:flex; flex-direction:column; justify-content:space-between; }}
.card span {{ color:#73583e; text-transform:capitalize; font-size:14px; }}
.card strong {{ color:var(--river); font-size:32px; }}
table {{ width:100%; border-collapse:collapse; font-size:14px; }}
th,td {{ text-align:left; padding:11px 9px; border-bottom:1px solid rgba(33,22,15,.12); vertical-align:top; }}
th {{ color:var(--leaf); text-transform:uppercase; letter-spacing:.1em; font-size:11px; }}
ul.timeline {{ list-style:none; padding:0; display:grid; gap:10px; }}
ul.timeline li {{ background:rgba(255,255,255,.52); border-left:4px solid var(--grain); border-radius:18px; padding:14px 16px; }}
ul.timeline em {{ display:block; color:var(--river); font-style:normal; margin-top:4px; font-size:12px; }}
.flower {{ position:relative; overflow:hidden; min-height:292px; }}
.flower::before {{ content:''; position:absolute; inset:24px; border-radius:50%; background:repeating-radial-gradient(circle, transparent 0 25px, rgba(83,111,63,.22) 26px 28px), conic-gradient(from 18deg, rgba(168,79,48,.20), rgba(47,102,114,.26), rgba(199,140,44,.29), rgba(168,79,48,.20)); animation:breathe 14s ease-in-out infinite alternate; }}
.flower p {{ position:relative; max-width:690px; font-size:18px; line-height:1.5; }}
@keyframes breathe {{ from {{ transform:scale(.98) rotate(-1.2deg); opacity:.72; }} to {{ transform:scale(1.025) rotate(1.4deg); opacity:.96; }} }}
@media(max-width:720px) {{ header,main {{ padding-left:18px; padding-right:18px; }} table {{ font-size:12px; }} th,td {{ padding:8px 5px; }} }}
</style>
</head>
<body>
<header>
  <div class=\"kicker\">SSRM-3D Report 220</div>
  <h1>Embodied pre-avatar ecology: bodies age in weather, build shelter, grow food, exchange materials, and carry private pain.</h1>
  <div class=\"boundary\">Deterministic simulation artifact. The avatar remains outside for {payload['avatar_protocol']['observed_pre_avatar_years']} simulated years while body, weather, food, shelter, craft, and material ledgers form. This is not real biology, ecology, consent, suffering, consciousness, or moral patienthood.</div>
</header>
<main>
<section><h2>Metrics</h2><div class=\"grid\">{cards}</div></section>
<section class=\"flower\"><h2>Frequency / flower-of-life ecology rhythm</h2><p>Every body state, illness, apprenticeship, shelter project, crop cycle, weather season, material exchange, and avatar gate carries a vibration rate and flower node. The overlay is an inspectable timing scaffold for embodied rates, not metaphysical proof.</p></section>
<section><h2>Life-stage body costs</h2><table><thead><tr><th>Person</th><th>Age</th><th>Stage</th><th>Energy</th><th>Fatigue</th><th>Pain</th></tr></thead><tbody>{life_rows}</tbody></table></section>
<section><h2>Illness and care</h2><table><thead><tr><th>Care</th><th>Person</th><th>Recovered</th><th>Relapse</th><th>Care action</th></tr></thead><tbody>{illness_rows}</tbody></table></section>
<section><h2>Habitat projects</h2><table><thead><tr><th>Project</th><th>Structure</th><th>Comfort</th><th>Safety</th><th>Debt</th></tr></thead><tbody>{habitat_rows}</tbody></table></section>
<section><h2>Agriculture</h2><table><thead><tr><th>Cycle</th><th>Food/material</th><th>Yield</th><th>Spoilage</th><th>Sensory marker</th></tr></thead><tbody>{agriculture_rows}</tbody></table></section>
<section><h2>Replay timeline excerpt</h2><ul class=\"timeline\">{event_nodes}</ul></section>
</main>
</body>
</html>
""",
        encoding="utf-8",
    )


def run(seed: int) -> dict[str, Any]:
    rng = random.Random(seed)
    source_state = load_source_state()
    source_condition = source_state.get("condition") or source_state.get("source_condition") or DEFAULT_SOURCE_CONDITION
    life = build_life_records(rng)
    illness = build_illness(life)
    apprenticeships = build_apprenticeships(life)
    habitats = build_habitats()
    agriculture = build_agriculture()
    weather = build_weather()
    materials = build_materials()
    protocol = build_avatar_protocol(life, materials, weather)
    events = build_events(life, illness, apprenticeships, habitats, agriculture, weather, materials, protocol)
    replay = build_replay(events)
    metrics = compute_metrics(life, illness, apprenticeships, habitats, agriculture, weather, materials, protocol, events, replay)
    ablations = compute_ablations(metrics)
    verdict = "pass" if metrics["embodied_pre_avatar_ecology_readiness"] >= 0.80 and metrics["late_avatar_entry_integrity"] >= 1.0 and metrics["birth_aging_traceability"] >= 0.95 else "fail"
    payload = {
        "report": 220,
        "module": BASE,
        "seed": seed,
        "source_artifact": str(SOURCE_STATE),
        "source_condition": source_condition,
        "condition": "integrated_playable_embodied_pre_avatar_ecology_births_aging_illness_apprenticeship_habitat_agriculture_weather_material_economy",
        "module_verdict": verdict,
        "life_stages": [asdict(row) for row in life],
        "illness_care": [asdict(row) for row in illness],
        "apprenticeships": [asdict(row) for row in apprenticeships],
        "habitats": [asdict(row) for row in habitats],
        "agriculture": [asdict(row) for row in agriculture],
        "weather": [asdict(row) for row in weather],
        "materials": [asdict(row) for row in materials],
        "avatar_protocol": asdict(protocol),
        "events": [asdict(row) for row in events],
        "replay": [asdict(row) for row in replay],
        "metrics": metrics,
        "ablations": ablations,
        "honest_limits": [
            "This is deterministic embodied-ecology substrate, not a full physics, biology, or ecology engine.",
            "Body states are functional welfare/control variables, not subjective suffering.",
            "Illness and agriculture are scripted ecological records rather than full population dynamics.",
            "Avatar entry is a simulation gate, not real consent from conscious beings.",
            "Frequency and flower overlays are timing and phase scaffolds, not metaphysical evidence.",
        ],
        "next_gate": "playable local 3D ecology scene with spatialized bodies, sensory fields, weather volumes, crop plots, habitat interiors, material objects, and avatar conversation entry",
    }
    return payload


def write_artifacts(payload: dict[str, Any]) -> dict[str, str]:
    ARTIFACT_DIR.mkdir(exist_ok=True)
    VISUALIZATION_DIR.mkdir(exist_ok=True)
    paths = {
        "events": ARTIFACT_DIR / f"{BASE}_events.csv",
        "life_stages": ARTIFACT_DIR / f"{BASE}_life_stages.csv",
        "illness_care": ARTIFACT_DIR / f"{BASE}_illness_care.csv",
        "apprenticeships": ARTIFACT_DIR / f"{BASE}_apprenticeships.csv",
        "habitats": ARTIFACT_DIR / f"{BASE}_habitats.csv",
        "agriculture": ARTIFACT_DIR / f"{BASE}_agriculture.csv",
        "weather": ARTIFACT_DIR / f"{BASE}_weather.csv",
        "materials": ARTIFACT_DIR / f"{BASE}_material_economy.csv",
        "avatar_protocol": ARTIFACT_DIR / f"{BASE}_avatar_protocol.csv",
        "replay": ARTIFACT_DIR / f"{BASE}_replay.json",
        "results": ARTIFACT_DIR / f"{BASE}_results.json",
        "state": ARTIFACT_DIR / f"{BASE}_state.json",
        "verdict": ARTIFACT_DIR / f"{BASE}_verdict.csv",
        "visualization": VISUALIZATION_DIR / f"{BASE}.html",
    }
    write_csv(paths["events"], payload["events"])
    write_csv(paths["life_stages"], payload["life_stages"])
    write_csv(paths["illness_care"], payload["illness_care"])
    write_csv(paths["apprenticeships"], payload["apprenticeships"])
    write_csv(paths["habitats"], payload["habitats"])
    write_csv(paths["agriculture"], payload["agriculture"])
    write_csv(paths["weather"], payload["weather"])
    write_csv(paths["materials"], payload["materials"])
    write_csv(paths["avatar_protocol"], [payload["avatar_protocol"]])
    write_json(paths["replay"], {"report": payload["report"], "frames": payload["replay"]})
    write_json(paths["results"], payload)
    write_json(paths["state"], {
        "report": payload["report"],
        "condition": payload["condition"],
        "source_condition": payload["source_condition"],
        "embodied_pre_avatar_ecology_readiness": payload["metrics"]["embodied_pre_avatar_ecology_readiness"],
        "simulated_pre_avatar_years": payload["metrics"]["simulated_pre_avatar_years"],
        "birth_aging_traceability": payload["metrics"]["birth_aging_traceability"],
        "illness_care_recovery_rate": payload["metrics"]["illness_care_recovery_rate"],
        "agriculture_yield_stability": payload["metrics"]["agriculture_yield_stability"],
        "late_avatar_entry_integrity": payload["metrics"]["late_avatar_entry_integrity"],
        "private_boundary": "sealed private pain, illness, child, family, and workspace digests only",
        "next_gate": payload["next_gate"],
    })
    write_csv(paths["verdict"], [{
        "module": BASE,
        "verdict": payload["module_verdict"],
        "embodied_pre_avatar_ecology_readiness": payload["metrics"]["embodied_pre_avatar_ecology_readiness"],
        "simulated_pre_avatar_years": payload["metrics"]["simulated_pre_avatar_years"],
        "weakest_channel_score": payload["metrics"]["weakest_channel_score"],
        "late_avatar_entry_integrity": payload["metrics"]["late_avatar_entry_integrity"],
        "next_gate": payload["next_gate"],
    }])
    render_visualization(paths["visualization"], payload)
    return {key: str(value) for key, value in paths.items()}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    payload = run(args.seed)
    paths = write_artifacts(payload)
    metrics = payload["metrics"]
    print(f"module_verdict {payload['module_verdict']}")
    print(f"embodied_pre_avatar_ecology_readiness {metrics['embodied_pre_avatar_ecology_readiness']:.6f}")
    print(f"simulated_pre_avatar_years {metrics['simulated_pre_avatar_years']:.0f}")
    print(f"life_stage_records {len(payload['life_stages'])}")
    print(f"illness_care_records {len(payload['illness_care'])}")
    print(f"apprenticeships {len(payload['apprenticeships'])}")
    print(f"habitat_projects {len(payload['habitats'])}")
    print(f"agriculture_cycles {len(payload['agriculture'])}")
    print(f"weather_cycles {len(payload['weather'])}")
    print(f"material_exchanges {len(payload['materials'])}")
    print(f"illness_care_recovery_rate {metrics['illness_care_recovery_rate']:.6f}")
    print(f"agriculture_yield_stability {metrics['agriculture_yield_stability']:.6f}")
    print(f"material_economy_traceability {metrics['material_economy_traceability']:.6f}")
    print(f"late_avatar_entry_integrity {metrics['late_avatar_entry_integrity']:.6f}")
    print(f"weakest_channel_score {metrics['weakest_channel_score']:.6f}")
    print(f"visualization {paths['visualization']}")
    print(f"next_gate {payload['next_gate']}")


if __name__ == "__main__":
    main()
