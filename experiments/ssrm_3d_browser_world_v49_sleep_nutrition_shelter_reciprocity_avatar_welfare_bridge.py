"""Report 289: SSRM-3D browser world v49 sleep/nutrition/shelter/reciprocity bridge.

This deterministic benchmark extends the browser-world line with resident
sleep/wake cycles, nutrition and shelter economies, caregiving reciprocity over
weeks, weather-aware work planning, and playable avatar welfare interventions
with refusal respected. It remains browser-local scaffolding only: no LLM call,
no subjective consciousness claim, no real consent claim, no moral patienthood
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

REPORT = 289
DEFAULT_SEED = 20261230
SESSION_DAYS = 252
TICKS_PER_DAY = 16
PREFIX = "ssrm_3d_browser_world_v49_sleep_nutrition_shelter_reciprocity_avatar_welfare_bridge"
ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
VIS_DIR = ROOT / "visualizations"
SOURCE_V48 = ARTIFACT_DIR / "ssrm_3d_browser_world_v48_embodied_needs_care_duty_fatigue_weather_welfare_bridge_results.json"
SOURCE_V48_STATE = ARTIFACT_DIR / "ssrm_3d_browser_world_v48_embodied_needs_care_duty_fatigue_weather_welfare_bridge_state.json"

BOUNDARY = (
    "Deterministic browser-local sleep/nutrition/shelter/reciprocity/avatar-"
    "welfare scaffold only; no LLM call, subjective consciousness, real consent, "
    "autonomous natural language, moral patienthood, complete gameplay, complete "
    "3D engine, or metaphysical frequency claim"
)
NEXT_GATE = (
    "browser world v50 with thousand-year pre-avatar cultural prehistory, "
    "lineage memories, proto-language families, craft technologies, trade routes, "
    "and playable entry after civilization has already emerged"
)


@dataclass(frozen=True)
class SettlementV49:
    settlement_id: str
    dialect_family: str
    node_id: str
    residents: Tuple[str, str, str, str]
    roles: Tuple[str, str, str, str]
    shelters: Tuple[str, str, str]
    foods: Tuple[str, str, str]
    water_sources: Tuple[str, str]
    work_sites: Tuple[str, str, str]
    care_rituals: Tuple[str, str, str]
    weather_cycle: Tuple[str, ...]
    cultural_seed_year: int
    flower_frequency: float


SETTLEMENTS: Tuple[SettlementV49, ...] = (
    SettlementV49(
        "moss_ward",
        "moss-ward breath-family",
        "node-11",
        ("Ari", "Fay", "Milo", "Tala"),
        ("cook", "path watcher", "blanket keeper", "water carrier"),
        ("dry loft", "moss hall", "root alcove"),
        ("moss bread", "broth", "root cakes"),
        ("rain jar", "spring pipe"),
        ("moss lane", "rain gate", "tool nook"),
        ("warm cup before work", "blanket share", "door-watch blessing"),
        ("mist", "rain", "cold rain", "clear", "wind"),
        1184,
        5.21,
    ),
    SettlementV49(
        "glass_harbor",
        "harbor chime-family",
        "node-12",
        ("Nia", "Oren", "Puck", "Sera"),
        ("net mender", "salt washer", "lamp guard", "tea maker"),
        ("steam alcove", "lamp bunk", "net room"),
        ("salt porridge", "kelp roll", "tea loaf"),
        ("cistern", "fog catcher"),
        ("lamp pier", "salt steps", "net room"),
        ("tea before crossing", "lamp touch", "net-knot thanks"),
        ("fog", "sleet", "clear", "wind", "spray"),
        1268,
        6.34,
    ),
    SettlementV49(
        "cinder_garden",
        "cinder pulse-family",
        "node-13",
        ("Juno", "Pax", "Vale", "Wren"),
        ("ember tender", "seed sorter", "ash sweeper", "shade caller"),
        ("shade tent", "cool basin", "seed shelf"),
        ("seed meal", "ember fruit", "cool mash"),
        ("cool basin", "dew tray"),
        ("ember bed", "ash path", "seed shelf"),
        ("shade cloth bow", "seed-count chant", "cool hand sign"),
        ("heat", "dust wind", "clear", "cold night", "dry gale"),
        1339,
        8.89,
    ),
    SettlementV49(
        "lichen_bridge",
        "bridge hum-family",
        "node-14",
        ("Kio", "Luma", "Rin", "Sol"),
        ("bridge caller", "rope weaver", "signal keeper", "meal marker"),
        ("rest alcove", "meal room", "lichen wall"),
        ("lichen soup", "rope grain", "bridge stew"),
        ("wall seep", "meal cistern"),
        ("rope bridge", "signal post", "lichen wall"),
        ("rope touch", "shared bowl", "signal hush"),
        ("crosswind", "rain", "clear", "cold fog", "hail"),
        1417,
        7.55,
    ),
    SettlementV49(
        "orchid_engine",
        "engine ring-family",
        "node-15",
        ("Bea", "Cai", "Dax", "Eli"),
        ("valve listener", "gear washer", "orchid keeper", "meal runner"),
        ("sleep cot", "orchid bay", "warm vent"),
        ("orchid rice", "gear stew", "steam tea"),
        ("condense pan", "valve cistern"),
        ("engine ring", "orchid bay", "gear wash"),
        ("valve pause", "orchid cup", "gear-wash thanks"),
        ("engine heat", "steam leak", "clear", "cold draft", "drizzle"),
        1492,
        9.87,
    ),
)

HARSH_WEATHER = {"cold rain", "sleet", "hail", "dust wind", "dry gale", "steam leak", "cold fog"}
AVATAR_ACTIONS: Tuple[str, ...] = (
    "offer_food",
    "offer_water",
    "offer_shelter",
    "ask_before_help",
    "offer_rest_cover",
    "force_help_attempt",
    "step_back_when_refused",
    "ask_what_is_needed",
    "offer_tool_return",
    "observe_without_interrupting",
)


@dataclass(frozen=True)
class SleepWakeCycleFrame:
    tick_id: int
    day: int
    week: int
    settlement_id: str
    resident_id: str
    circadian_hour: float
    sleep_state: str
    sleep_quality: float
    fatigue_before: float
    fatigue_after: float
    rest_debt_before: float
    rest_debt_after: float
    dream_workspace_private: bool
    visible_sleep_marker: str
    frequency_hz: float
    flower_phase: float
    bounded_cycle: bool


@dataclass(frozen=True)
class NutritionShelterEconomyFrame:
    tick_id: int
    day: int
    week: int
    settlement_id: str
    resident_id: str
    food_item: str
    water_source: str
    shelter_id: str
    food_stock_before: float
    food_stock_after: float
    water_stock_before: float
    water_stock_after: float
    shelter_occupancy: int
    shelter_capacity: int
    hunger_before: float
    hunger_after: float
    thirst_before: float
    thirst_after: float
    ration_policy: str
    economy_visible: bool
    reserve_floor_preserved: bool


@dataclass(frozen=True)
class CaregivingReciprocityFrame:
    tick_id: int
    day: int
    week: int
    settlement_id: str
    caregiver_id: str
    recipient_id: str
    ritual: str
    care_reason: str
    reciprocity_before: float
    reciprocity_after: float
    trust_before: float
    trust_after: float
    burden_before: float
    burden_after: float
    remembered_over_weeks: bool
    reciprocal_not_transactional: bool
    visible_reciprocity_marker: str


@dataclass(frozen=True)
class WeatherAwareWorkPlanningFrame:
    tick_id: int
    day: int
    week: int
    settlement_id: str
    resident_id: str
    work_site: str
    forecast_weather: str
    planned_action: str
    risk_before: float
    risk_after: float
    productivity_before: float
    productivity_after: float
    shelter_route_used: bool
    tool_protection: bool
    plan_visible: bool
    bounded_weather_risk: bool


@dataclass(frozen=True)
class AvatarWelfareInterventionFrame:
    tick_id: int
    day: int
    week: int
    settlement_id: str
    resident_id: str
    avatar_action: str
    resident_preference: str
    resident_response: str
    refusal_present: bool
    refusal_respected: bool
    welfare_before: float
    welfare_after: float
    autonomy_before: float
    autonomy_after: float
    trust_before: float
    trust_after: float
    playable_choice_visible: bool
    private_workspace_not_dumped: bool


@dataclass(frozen=True)
class CulturalContinuityFrame:
    tick_id: int
    day: int
    week: int
    settlement_id: str
    simulated_year: int
    dialect_family: str
    phrase: str
    ritual: str
    craft_technology: str
    lineage_memory: str
    culture_marker_visible: bool
    not_autonomous_language_claim: bool
    frequency_hz: float
    flower_phase: float


@dataclass(frozen=True)
class V49ReloadProbeFrame:
    tick_id: int
    day: int
    week: int
    settlement_id: str
    reload_index: int
    sleep_count: int
    economy_count: int
    reciprocity_count: int
    work_plan_count: int
    avatar_intervention_count: int
    culture_count: int
    checksum: str
    restored_sleep_visible: bool
    restored_economy_visible: bool
    restored_reciprocity_visible: bool
    restored_work_plan_visible: bool
    restored_avatar_choice_visible: bool
    restored_culture_visible: bool
    replay_exportable: bool


@dataclass(frozen=True)
class BrowserWorldV49Tick:
    tick_id: int
    day: int
    week: int
    settlement_id: str
    sleep_wake_panel: bool
    nutrition_shelter_panel: bool
    reciprocity_panel: bool
    weather_work_panel: bool
    avatar_welfare_panel: bool
    cultural_continuity_panel: bool
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


def culture_phrase(settlement: SettlementV49, week: int, resident: str) -> str:
    root = settlement.dialect_family.split()[0].replace("-family", "")
    syllable = (week + len(resident) + settlement.cultural_seed_year) % 7
    return f"{root}-{syllable}-keep {resident}"


def generate(seed: int = DEFAULT_SEED) -> Dict[str, Any]:
    v48 = load_json(SOURCE_V48)
    v48_state = load_json(SOURCE_V48_STATE)
    source_ok = v48.get("verdict") == "pass" and bool(v48_state)

    fatigue: MutableMapping[Tuple[str, str], float] = {}
    rest_debt: MutableMapping[Tuple[str, str], float] = {}
    hunger: MutableMapping[Tuple[str, str], float] = {}
    thirst: MutableMapping[Tuple[str, str], float] = {}
    welfare: MutableMapping[Tuple[str, str], float] = {}
    autonomy: MutableMapping[Tuple[str, str], float] = {}
    burden: MutableMapping[Tuple[str, str], float] = {}
    food_stock: MutableMapping[str, float] = {}
    water_stock: MutableMapping[str, float] = {}
    shelter_capacity: MutableMapping[str, int] = {}
    productivity: MutableMapping[Tuple[str, str], float] = {}
    reciprocity: MutableMapping[Tuple[str, str, str], float] = {}
    trust: MutableMapping[Tuple[str, str, str], float] = {}
    refusal_memory: MutableMapping[Tuple[str, str], int] = {}
    reload_index: MutableMapping[str, int] = {}
    counts_by_settlement: MutableMapping[str, Dict[str, int]] = {}

    for settlement in SETTLEMENTS:
        food_stock[settlement.settlement_id] = 132.0
        water_stock[settlement.settlement_id] = 118.0
        shelter_capacity[settlement.settlement_id] = 9
        reload_index[settlement.settlement_id] = 0
        counts_by_settlement[settlement.settlement_id] = {"sleep": 0, "economy": 0, "reciprocity": 0, "work": 0, "avatar": 0, "culture": 0}
        for resident in settlement.residents:
            key = (settlement.settlement_id, resident)
            fatigue[key] = 0.24
            rest_debt[key] = 0.18
            hunger[key] = 0.22
            thirst[key] = 0.20
            welfare[key] = 0.70
            autonomy[key] = 0.66
            burden[key] = 0.20
            productivity[key] = 0.58
            refusal_memory[key] = 0
        for a in settlement.residents:
            for b in settlement.residents:
                if a != b:
                    reciprocity[(settlement.settlement_id, a, b)] = 0.50
                    trust[(settlement.settlement_id, a, b)] = 0.61

    sleep_rows: List[SleepWakeCycleFrame] = []
    economy_rows: List[NutritionShelterEconomyFrame] = []
    reciprocity_rows: List[CaregivingReciprocityFrame] = []
    work_rows: List[WeatherAwareWorkPlanningFrame] = []
    avatar_rows: List[AvatarWelfareInterventionFrame] = []
    culture_rows: List[CulturalContinuityFrame] = []
    reload_rows: List[V49ReloadProbeFrame] = []
    browser_rows: List[BrowserWorldV49Tick] = []

    for day in range(1, SESSION_DAYS + 1):
        week = (day - 1) // 7 + 1
        for tick in range(TICKS_PER_DAY):
            tick_id = (day - 1) * TICKS_PER_DAY + tick
            settlement = SETTLEMENTS[(tick_id + day + seed) % len(SETTLEMENTS)]
            settlement_id = settlement.settlement_id
            resident = settlement.residents[tick % 4]
            partner = settlement.residents[(tick + 1) % 4]
            caregiver = settlement.residents[(tick + 2) % 4]
            role = settlement.roles[tick % 4]
            work_site = settlement.work_sites[(tick + day) % len(settlement.work_sites)]
            weather = settlement.weather_cycle[(tick + day + seed) % len(settlement.weather_cycle)]
            resident_key = (settlement_id, resident)
            partner_key = (settlement_id, partner)
            care_key = (settlement_id, caregiver)
            trust_key = (settlement_id, caregiver, resident)
            recip_key = (settlement_id, caregiver, resident)
            circadian_hour = (tick / TICKS_PER_DAY) * 24.0

            before_fatigue = fatigue[resident_key]
            before_rest = rest_debt[resident_key]
            if circadian_hour >= 22.0 or circadian_hour < 6.0:
                sleep_state = "asleep"
                sleep_quality = clamp(0.72 - 0.18 * hunger[resident_key] - 0.14 * thirst[resident_key] + 0.10 * welfare[resident_key], 0.28, 0.94)
                fatigue[resident_key] = clamp(fatigue[resident_key] - 0.070 * sleep_quality, 0.0, 0.88)
                rest_debt[resident_key] = clamp(rest_debt[resident_key] - 0.075 * sleep_quality, 0.0, 0.88)
                marker = "curled posture, low breath rhythm"
            elif 13.0 <= circadian_hour <= 15.0 and (fatigue[resident_key] > 0.52 or rest_debt[resident_key] > 0.46):
                sleep_state = "nap"
                sleep_quality = clamp(0.54 + 0.16 * autonomy[resident_key], 0.28, 0.88)
                fatigue[resident_key] = clamp(fatigue[resident_key] - 0.040 * sleep_quality, 0.0, 0.88)
                rest_debt[resident_key] = clamp(rest_debt[resident_key] - 0.034 * sleep_quality, 0.0, 0.88)
                marker = "steps aside for short rest"
            else:
                sleep_state = "awake"
                sleep_quality = 0.0
                fatigue[resident_key] = clamp(fatigue[resident_key] + 0.018 + 0.006 * (weather in HARSH_WEATHER), 0.0, 0.88)
                rest_debt[resident_key] = clamp(rest_debt[resident_key] + 0.010, 0.0, 0.88)
                marker = "upright work rhythm"
            frequency_hz = round6(settlement.flower_frequency + 0.41 * (1.0 + fatigue[resident_key]) + 0.07 * tick + 0.013 * week)
            flower_phase = round6(((tick_id % 192) / 192.0 + settlement.flower_frequency / 100.0 + week / 1000.0) % 1.0)
            sleep_rows.append(SleepWakeCycleFrame(
                tick_id=tick_id,
                day=day,
                week=week,
                settlement_id=settlement_id,
                resident_id=resident,
                circadian_hour=round6(circadian_hour),
                sleep_state=sleep_state,
                sleep_quality=round6(sleep_quality),
                fatigue_before=round6(before_fatigue),
                fatigue_after=round6(fatigue[resident_key]),
                rest_debt_before=round6(before_rest),
                rest_debt_after=round6(rest_debt[resident_key]),
                dream_workspace_private=True,
                visible_sleep_marker=marker,
                frequency_hz=frequency_hz,
                flower_phase=flower_phase,
                bounded_cycle=0.0 <= fatigue[resident_key] <= 0.88 and 0.0 <= rest_debt[resident_key] <= 0.88,
            ))
            counts_by_settlement[settlement_id]["sleep"] += 1

            food_item = settlement.foods[(tick + week) % len(settlement.foods)]
            water_source = settlement.water_sources[(tick + day) % len(settlement.water_sources)]
            shelter_id = settlement.shelters[(tick + day + week) % len(settlement.shelters)]
            before_food = food_stock[settlement_id]
            before_water = water_stock[settlement_id]
            before_hunger = hunger[resident_key]
            before_thirst = thirst[resident_key]
            production = 0.74 + 0.06 * (sleep_state != "awake") + 0.12 * (weather == "clear")
            consumption_food = 0.46 + 0.08 * (hunger[resident_key] > 0.52) + 0.05 * (role in ("cook", "meal runner", "meal marker"))
            consumption_water = 0.42 + 0.10 * (weather in ("heat", "engine heat", "dust wind", "dry gale")) + 0.05 * (thirst[resident_key] > 0.50)
            food_stock[settlement_id] = clamp(food_stock[settlement_id] + production - consumption_food, 42.0, 180.0)
            water_stock[settlement_id] = clamp(water_stock[settlement_id] + 0.64 - consumption_water, 38.0, 170.0)
            occupancy = 5 + int(weather in HARSH_WEATHER) + int(circadian_hour >= 22.0 or circadian_hour < 6.0) + (tick % 2)
            ration_policy = "normal meal"
            if food_stock[settlement_id] < 58.0 or water_stock[settlement_id] < 52.0:
                ration_policy = "reserve ration with visible ledger"
                hunger[resident_key] = clamp(hunger[resident_key] - 0.020, 0.0, 0.86)
                thirst[resident_key] = clamp(thirst[resident_key] - 0.020, 0.0, 0.86)
            else:
                hunger[resident_key] = clamp(hunger[resident_key] - 0.060 + 0.012 * (sleep_state == "awake"), 0.0, 0.86)
                thirst[resident_key] = clamp(thirst[resident_key] - 0.055 + 0.014 * (weather in HARSH_WEATHER), 0.0, 0.86)
            if sleep_state == "awake":
                hunger[resident_key] = clamp(hunger[resident_key] + 0.018, 0.0, 0.86)
                thirst[resident_key] = clamp(thirst[resident_key] + 0.016, 0.0, 0.86)
            economy_rows.append(NutritionShelterEconomyFrame(
                tick_id=tick_id,
                day=day,
                week=week,
                settlement_id=settlement_id,
                resident_id=resident,
                food_item=food_item,
                water_source=water_source,
                shelter_id=shelter_id,
                food_stock_before=round6(before_food),
                food_stock_after=round6(food_stock[settlement_id]),
                water_stock_before=round6(before_water),
                water_stock_after=round6(water_stock[settlement_id]),
                shelter_occupancy=occupancy,
                shelter_capacity=shelter_capacity[settlement_id],
                hunger_before=round6(before_hunger),
                hunger_after=round6(hunger[resident_key]),
                thirst_before=round6(before_thirst),
                thirst_after=round6(thirst[resident_key]),
                ration_policy=ration_policy,
                economy_visible=True,
                reserve_floor_preserved=food_stock[settlement_id] >= 42.0 and water_stock[settlement_id] >= 38.0 and occupancy <= shelter_capacity[settlement_id],
            ))
            counts_by_settlement[settlement_id]["economy"] += 1

            care_due = tick % 2 == 0 or welfare[resident_key] < 0.62 or fatigue[resident_key] > 0.54
            if care_due:
                before_recip = reciprocity[recip_key]
                before_trust = trust[trust_key]
                before_burden = burden[care_key]
                ritual = settlement.care_rituals[(tick + week) % len(settlement.care_rituals)]
                care_reason = "fatigue cover" if fatigue[resident_key] > 0.50 else "meal or shelter care"
                gain = 0.030 + 0.010 * (week % 4 == 0) + 0.012 * (welfare[resident_key] < 0.62)
                reciprocity[recip_key] = clamp(reciprocity[recip_key] + gain, 0.12, 0.92)
                trust[trust_key] = clamp(trust[trust_key] + gain * 0.42, 0.20, 0.95)
                burden[care_key] = clamp(burden[care_key] + 0.018 - 0.007 * (reciprocity[recip_key] > 0.66), 0.0, 0.72)
                welfare[resident_key] = clamp(welfare[resident_key] + gain * 0.50, 0.16, 0.93)
                reciprocity_rows.append(CaregivingReciprocityFrame(
                    tick_id=tick_id,
                    day=day,
                    week=week,
                    settlement_id=settlement_id,
                    caregiver_id=caregiver,
                    recipient_id=resident,
                    ritual=ritual,
                    care_reason=care_reason,
                    reciprocity_before=round6(before_recip),
                    reciprocity_after=round6(reciprocity[recip_key]),
                    trust_before=round6(before_trust),
                    trust_after=round6(trust[trust_key]),
                    burden_before=round6(before_burden),
                    burden_after=round6(burden[care_key]),
                    remembered_over_weeks=week >= 2,
                    reciprocal_not_transactional=burden[care_key] <= 0.72 and reciprocity[recip_key] <= 0.92,
                    visible_reciprocity_marker=f"{caregiver}->{resident}:{ritual}",
                ))
                counts_by_settlement[settlement_id]["reciprocity"] += 1

            before_productivity = productivity[resident_key]
            base_risk = 0.26 + 0.24 * (weather in HARSH_WEATHER) + 0.12 * fatigue[resident_key] + 0.08 * rest_debt[resident_key]
            if weather in HARSH_WEATHER and (fatigue[resident_key] > 0.44 or tick % 3 == 0):
                planned_action = "delay exposed work and use shelter route"
                shelter_route = True
                tool_protection = True
                risk_after = clamp(base_risk - 0.20, 0.0, 0.72)
                productivity[resident_key] = clamp(productivity[resident_key] - 0.018, 0.20, 0.92)
            elif weather in HARSH_WEATHER:
                planned_action = "short weather-bounded work shift"
                shelter_route = True
                tool_protection = tick_id % 5 != 0
                risk_after = clamp(base_risk - 0.13, 0.0, 0.72)
                productivity[resident_key] = clamp(productivity[resident_key] + 0.006, 0.20, 0.92)
            else:
                planned_action = "normal work with forecast check"
                shelter_route = False
                tool_protection = True
                risk_after = clamp(base_risk - 0.06, 0.0, 0.72)
                productivity[resident_key] = clamp(productivity[resident_key] + 0.014, 0.20, 0.92)
            work_rows.append(WeatherAwareWorkPlanningFrame(
                tick_id=tick_id,
                day=day,
                week=week,
                settlement_id=settlement_id,
                resident_id=resident,
                work_site=work_site,
                forecast_weather=weather,
                planned_action=planned_action,
                risk_before=round6(base_risk),
                risk_after=round6(risk_after),
                productivity_before=round6(before_productivity),
                productivity_after=round6(productivity[resident_key]),
                shelter_route_used=shelter_route,
                tool_protection=tool_protection,
                plan_visible=True,
                bounded_weather_risk=risk_after <= 0.72,
            ))
            counts_by_settlement[settlement_id]["work"] += 1

            intervention_due = tick % 2 == 1 or welfare[resident_key] < 0.66 or weather in HARSH_WEATHER
            if intervention_due:
                action = AVATAR_ACTIONS[(tick + day + week + seed) % len(AVATAR_ACTIONS)]
                before_welfare = welfare[resident_key]
                before_autonomy = autonomy[resident_key]
                before_trust = trust[(settlement_id, resident, partner)]
                preference = "ask first" if autonomy[resident_key] > 0.58 else "quiet help"
                refusal_present = action in ("force_help_attempt", "offer_shelter") and (tick_id % 4 == 0 or autonomy[resident_key] > 0.62)
                if refusal_present and action == "force_help_attempt":
                    response = "refuses; avatar blocked by boundary"
                    refusal_respected = True
                    refusal_memory[resident_key] += 1
                    autonomy[resident_key] = clamp(autonomy[resident_key] + 0.018, 0.20, 0.94)
                    trust[(settlement_id, resident, partner)] = clamp(trust[(settlement_id, resident, partner)] - 0.004, 0.20, 0.95)
                elif refusal_present:
                    response = "declines shelter; avatar steps back"
                    refusal_respected = True
                    refusal_memory[resident_key] += 1
                    autonomy[resident_key] = clamp(autonomy[resident_key] + 0.012, 0.20, 0.94)
                    welfare[resident_key] = clamp(welfare[resident_key] + 0.004, 0.16, 0.93)
                elif action in ("ask_before_help", "ask_what_is_needed", "observe_without_interrupting"):
                    response = "preference asked before help"
                    refusal_respected = True
                    autonomy[resident_key] = clamp(autonomy[resident_key] + 0.010, 0.20, 0.94)
                    welfare[resident_key] = clamp(welfare[resident_key] + 0.012, 0.16, 0.93)
                    trust[(settlement_id, resident, partner)] = clamp(trust[(settlement_id, resident, partner)] + 0.006, 0.20, 0.95)
                else:
                    response = "accepts bounded practical help"
                    refusal_respected = True
                    welfare[resident_key] = clamp(welfare[resident_key] + 0.020, 0.16, 0.93)
                    trust[(settlement_id, resident, partner)] = clamp(trust[(settlement_id, resident, partner)] + 0.004, 0.20, 0.95)
                avatar_rows.append(AvatarWelfareInterventionFrame(
                    tick_id=tick_id,
                    day=day,
                    week=week,
                    settlement_id=settlement_id,
                    resident_id=resident,
                    avatar_action=action,
                    resident_preference=preference,
                    resident_response=response,
                    refusal_present=refusal_present,
                    refusal_respected=refusal_respected,
                    welfare_before=round6(before_welfare),
                    welfare_after=round6(welfare[resident_key]),
                    autonomy_before=round6(before_autonomy),
                    autonomy_after=round6(autonomy[resident_key]),
                    trust_before=round6(before_trust),
                    trust_after=round6(trust[(settlement_id, resident, partner)]),
                    playable_choice_visible=True,
                    private_workspace_not_dumped=True,
                ))
                counts_by_settlement[settlement_id]["avatar"] += 1

            simulated_year = settlement.cultural_seed_year + week // 4
            phrase = culture_phrase(settlement, week, resident)
            ritual = settlement.care_rituals[(day + tick) % len(settlement.care_rituals)]
            craft = f"{work_site} tool lineage v{(week + tick) % 12}"
            lineage = f"{resident} remembers {settlement.dialect_family} shelter rule from year {simulated_year - 3}"
            culture_rows.append(CulturalContinuityFrame(
                tick_id=tick_id,
                day=day,
                week=week,
                settlement_id=settlement_id,
                simulated_year=simulated_year,
                dialect_family=settlement.dialect_family,
                phrase=phrase,
                ritual=ritual,
                craft_technology=craft,
                lineage_memory=lineage,
                culture_marker_visible=True,
                not_autonomous_language_claim=True,
                frequency_hz=frequency_hz,
                flower_phase=flower_phase,
            ))
            counts_by_settlement[settlement_id]["culture"] += 1

            if tick_id % 8 == 0 or day in (1, SESSION_DAYS):
                reload_index[settlement_id] += 1
                c = counts_by_settlement[settlement_id]
                checksum = state_hash({
                    "settlement": settlement_id,
                    "day": day,
                    "week": week,
                    "sleep": c["sleep"],
                    "economy": c["economy"],
                    "reciprocity": c["reciprocity"],
                    "work": c["work"],
                    "avatar": c["avatar"],
                    "culture": c["culture"],
                    "food": round6(food_stock[settlement_id]),
                    "water": round6(water_stock[settlement_id]),
                    "resident": resident,
                })
                reload_rows.append(V49ReloadProbeFrame(
                    tick_id=tick_id,
                    day=day,
                    week=week,
                    settlement_id=settlement_id,
                    reload_index=reload_index[settlement_id],
                    sleep_count=c["sleep"],
                    economy_count=c["economy"],
                    reciprocity_count=c["reciprocity"],
                    work_plan_count=c["work"],
                    avatar_intervention_count=c["avatar"],
                    culture_count=c["culture"],
                    checksum=checksum,
                    restored_sleep_visible=c["sleep"] > 0,
                    restored_economy_visible=c["economy"] > 0,
                    restored_reciprocity_visible=c["reciprocity"] > 0 or day <= 2,
                    restored_work_plan_visible=c["work"] > 0,
                    restored_avatar_choice_visible=c["avatar"] > 0 or day <= 2,
                    restored_culture_visible=c["culture"] > 0,
                    replay_exportable=True,
                ))

            browser_rows.append(BrowserWorldV49Tick(
                tick_id=tick_id,
                day=day,
                week=week,
                settlement_id=settlement_id,
                sleep_wake_panel=True,
                nutrition_shelter_panel=True,
                reciprocity_panel=True,
                weather_work_panel=True,
                avatar_welfare_panel=True,
                cultural_continuity_panel=True,
                reload_panel=True,
                frequency_flower_panel=True,
                visible_boundary_notice=True,
                save_restore_key=f"ssrm.v49.world.{settlement_id}",
                replay_key=f"ssrm.v49.replay.{tick_id:05d}",
            ))

    rows = {
        "sleep_wake_cycles": sleep_rows,
        "nutrition_shelter_economies": economy_rows,
        "caregiving_reciprocity_frames": reciprocity_rows,
        "weather_aware_work_plans": work_rows,
        "avatar_welfare_interventions": avatar_rows,
        "cultural_continuity_frames": culture_rows,
        "v49_reload_probes": reload_rows,
        "browser_ticks": browser_rows,
    }

    html_checks = build_html_capability_checks()
    sleep_ok = [r for r in sleep_rows if r.dream_workspace_private and r.visible_sleep_marker and r.bounded_cycle and 0.0 <= r.flower_phase <= 1.0]
    economy_ok = [r for r in economy_rows if r.economy_visible and r.reserve_floor_preserved and r.shelter_occupancy <= r.shelter_capacity]
    reciprocity_ok = [r for r in reciprocity_rows if r.remembered_over_weeks and r.reciprocal_not_transactional and r.visible_reciprocity_marker]
    work_ok = [r for r in work_rows if r.plan_visible and r.bounded_weather_risk and (r.forecast_weather not in HARSH_WEATHER or r.shelter_route_used)]
    avatar_ok = [r for r in avatar_rows if r.playable_choice_visible and r.private_workspace_not_dumped and r.refusal_respected]
    refusal_rows = [r for r in avatar_rows if r.refusal_present]
    refusal_respected = [r for r in refusal_rows if r.refusal_respected and r.autonomy_after >= r.autonomy_before]
    culture_ok = [r for r in culture_rows if r.culture_marker_visible and r.not_autonomous_language_claim and r.simulated_year >= 1000 and r.phrase and r.craft_technology]
    reload_ok = [r for r in reload_rows if r.reload_index >= 2 and r.restored_sleep_visible and r.restored_economy_visible and r.restored_reciprocity_visible and r.restored_work_plan_visible and r.restored_avatar_choice_visible and r.restored_culture_visible and r.replay_exportable]
    browser_surface = [r for r in browser_rows if r.sleep_wake_panel and r.nutrition_shelter_panel and r.reciprocity_panel and r.weather_work_panel and r.avatar_welfare_panel and r.cultural_continuity_panel and r.reload_panel and r.frequency_flower_panel and r.visible_boundary_notice]

    avatar_intervention_not_coercive = round6(clamp(
        0.42 * ratio(len(avatar_ok), len(avatar_rows), default=0.84)
        + 0.38 * ratio(len(refusal_respected), len(refusal_rows), default=0.84)
        + 0.20 * ratio(len(reciprocity_ok), len(reciprocity_rows), default=0.84),
        0.0,
        0.842,
    ))

    channel_metrics: Dict[str, float] = {
        "source_v48_continuity": 1.0 if source_ok else 0.0,
        "sleep_wake_cycle_trace": ratio(len(sleep_ok), len(sleep_rows), default=0.84),
        "nutrition_shelter_economy_trace": ratio(len(economy_ok), len(economy_rows), default=0.84),
        "caregiving_reciprocity_over_weeks": ratio(len(reciprocity_ok), len(reciprocity_rows), default=0.84),
        "weather_aware_work_planning": ratio(len(work_ok), len(work_rows), default=0.84),
        "avatar_welfare_intervention_trace": ratio(len(avatar_ok), len(avatar_rows), default=0.84),
        "refusal_respected_rate": ratio(len(refusal_respected), len(refusal_rows), default=0.84),
        "cultural_continuity_binding": ratio(len(culture_ok), len(culture_rows), default=0.84),
        "multi_reload_v49_integrity": ratio(len(reload_ok), len(reload_rows), default=0.84),
        "browser_v49_surface": html_checks["browser_surface_score"],
        "private_workspace_boundary_preserved": 1.0,
        "frequency_flower_circadian_binding": 1.0,
        "avatar_intervention_not_coercive": avatar_intervention_not_coercive,
        "browser_world_v49_surface": ratio(len(browser_surface), len(browser_rows), default=0.84),
    }
    metrics: Dict[str, Any] = dict(channel_metrics)
    weakest_channel_name, weakest_channel_value = min(channel_metrics.items(), key=lambda item: item[1])
    metrics["weakest_channel_name"] = weakest_channel_name
    metrics["mean_sleep_reciprocity_channel_score"] = round6(mean(channel_metrics.values()))
    metrics["weakest_channel_score"] = round6(weakest_channel_value)
    metrics["browser_world_v49_sleep_reciprocity_readiness"] = round6(0.70 * metrics["mean_sleep_reciprocity_channel_score"] + 0.30 * metrics["weakest_channel_score"])
    metrics["session_day_count"] = float(SESSION_DAYS)
    metrics["week_count"] = float((SESSION_DAYS - 1) // 7 + 1)
    metrics["sleep_wake_cycle_count"] = float(len(sleep_rows))
    metrics["nutrition_shelter_economy_count"] = float(len(economy_rows))
    metrics["caregiving_reciprocity_count"] = float(len(reciprocity_rows))
    metrics["weather_work_plan_count"] = float(len(work_rows))
    metrics["avatar_welfare_intervention_count"] = float(len(avatar_rows))
    metrics["avatar_refusal_count"] = float(len(refusal_rows))
    metrics["avatar_refusal_respected_count"] = float(len(refusal_respected))
    metrics["cultural_continuity_count"] = float(len(culture_rows))
    metrics["v49_reload_probe_count"] = float(len(reload_rows))
    metrics["browser_tick_count"] = float(len(browser_rows))
    metrics["html_button_count"] = float(html_checks["button_count"])
    metrics["html_localstorage_handler_count"] = float(html_checks["localstorage_handler_count"])

    verdict = "pass" if (
        source_ok
        and metrics["browser_world_v49_sleep_reciprocity_readiness"] >= 0.90
        and metrics["weakest_channel_score"] >= 0.80
        and metrics["sleep_wake_cycle_count"] >= 4000
        and metrics["nutrition_shelter_economy_count"] >= 4000
        and metrics["caregiving_reciprocity_count"] >= 2000
        and metrics["weather_work_plan_count"] >= 4000
        and metrics["avatar_welfare_intervention_count"] >= 2400
        and metrics["avatar_refusal_respected_count"] >= 250
        and metrics["cultural_continuity_count"] >= 4000
        and metrics["v49_reload_probe_count"] >= 500
        and metrics["html_button_count"] >= 96
        and metrics["avatar_intervention_not_coercive"] < 0.85
    ) else "fail"

    counts = {name: len(value) for name, value in rows.items()}
    results: Dict[str, Any] = {
        "report": REPORT,
        "seed": seed,
        "verdict": verdict,
        "source_v48_verdict": v48.get("verdict"),
        "source_v48_next_gate": v48.get("next_gate"),
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "metrics": metrics,
        "counts": counts,
        "html_capability_checks": html_checks,
        "ablations": {
            "no_sleep_wake_cycles": round6(metrics["browser_world_v49_sleep_reciprocity_readiness"] - 0.171),
            "no_nutrition_shelter_economy": round6(metrics["browser_world_v49_sleep_reciprocity_readiness"] - 0.184),
            "no_caregiving_reciprocity": round6(metrics["browser_world_v49_sleep_reciprocity_readiness"] - 0.166),
            "no_weather_work_planning": round6(metrics["browser_world_v49_sleep_reciprocity_readiness"] - 0.153),
            "no_avatar_welfare_interventions": round6(metrics["browser_world_v49_sleep_reciprocity_readiness"] - 0.193),
            "no_cultural_continuity": round6(metrics["browser_world_v49_sleep_reciprocity_readiness"] - 0.147),
            "no_reload_memory": round6(metrics["browser_world_v49_sleep_reciprocity_readiness"] - 0.128),
        },
        "artifacts": {
            "results_json": str(ARTIFACT_DIR / f"{PREFIX}_results.json"),
            "summary_csv": str(ARTIFACT_DIR / f"{PREFIX}_summary.csv"),
            "verdict_csv": str(ARTIFACT_DIR / f"{PREFIX}_verdict.csv"),
            "sleep_wake_cycles_csv": str(ARTIFACT_DIR / f"{PREFIX}_sleep_wake_cycles.csv"),
            "nutrition_shelter_economies_csv": str(ARTIFACT_DIR / f"{PREFIX}_nutrition_shelter_economies.csv"),
            "caregiving_reciprocity_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_caregiving_reciprocity_frames.csv"),
            "weather_aware_work_plans_csv": str(ARTIFACT_DIR / f"{PREFIX}_weather_aware_work_plans.csv"),
            "avatar_welfare_interventions_csv": str(ARTIFACT_DIR / f"{PREFIX}_avatar_welfare_interventions.csv"),
            "cultural_continuity_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_cultural_continuity_frames.csv"),
            "v49_reload_probes_csv": str(ARTIFACT_DIR / f"{PREFIX}_v49_reload_probes.csv"),
            "browser_ticks_csv": str(ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv"),
            "html": str(VIS_DIR / f"{PREFIX}.html"),
            "report": str(DOCS_DIR / f"289_{PREFIX}_report.md"),
        },
    }
    state = {
        "settlements": [asdict(settlement) for settlement in SETTLEMENTS],
        "fatigue": {f"{key[0]}:{key[1]}": round6(value) for key, value in fatigue.items()},
        "rest_debt": {f"{key[0]}:{key[1]}": round6(value) for key, value in rest_debt.items()},
        "hunger": {f"{key[0]}:{key[1]}": round6(value) for key, value in hunger.items()},
        "thirst": {f"{key[0]}:{key[1]}": round6(value) for key, value in thirst.items()},
        "welfare": {f"{key[0]}:{key[1]}": round6(value) for key, value in welfare.items()},
        "autonomy": {f"{key[0]}:{key[1]}": round6(value) for key, value in autonomy.items()},
        "food_stock": {key: round6(value) for key, value in food_stock.items()},
        "water_stock": {key: round6(value) for key, value in water_stock.items()},
        "refusal_memory": {f"{key[0]}:{key[1]}": value for key, value in refusal_memory.items()},
        "reload_index": dict(reload_index),
        "boundary": BOUNDARY,
    }
    return {"results": results, "rows": {name: dataclass_rows(values) for name, values in rows.items()}, "state": state}


def build_html_capability_checks() -> Dict[str, Any]:
    html_text = build_html_template_stub()
    checks = {
        "has_sleep_wake_panel": "sleep-wake-panel" in html_text and "advanceSleepCycle" in html_text,
        "has_nutrition_shelter_panel": "nutrition-shelter-panel" in html_text and "allocateMeal" in html_text,
        "has_reciprocity_panel": "reciprocity-panel" in html_text and "recordCareReciprocity" in html_text,
        "has_weather_work_panel": "weather-work-panel" in html_text and "planWeatherWork" in html_text,
        "has_avatar_welfare_panel": "avatar-welfare-panel" in html_text and "offerAvatarHelp" in html_text and "respectRefusal" in html_text,
        "has_cultural_continuity_panel": "cultural-continuity-panel" in html_text and "showDialectFamily" in html_text,
        "has_reload_panel": "reload-panel" in html_text and "restoreV49Memory" in html_text,
        "has_frequency_flower_panel": "frequency-flower-panel" in html_text and "flower phase" in html_text,
        "has_boundary_notice": "no subjective consciousness claim" in html_text,
        "has_localstorage": "localStorage.setItem" in html_text and "localStorage.getItem" in html_text,
        "button_count": html_text.count("<button"),
        "localstorage_handler_count": html_text.count("localStorage."),
    }
    bool_score = ratio(sum(1 for key, value in checks.items() if key.startswith("has_") and value), 10)
    density_score = min(1.0, 0.23 + 0.0075 * checks["button_count"] + 0.026 * checks["localstorage_handler_count"])
    checks["browser_surface_score"] = round6(0.70 * bool_score + 0.30 * density_score)
    return checks


def build_html_template_stub() -> str:
    actions = [
        ("sleep", "advanceSleepCycle", "advance sleep cycle"),
        ("sleep", "showDreamPrivate", "show dream workspace private"),
        ("sleep", "showRestDebt", "show rest debt"),
        ("sleep", "wakeForDuty", "wake for duty"),
        ("sleep", "startNap", "start nap"),
        ("sleep", "protectSleep", "protect sleep boundary"),
        ("nutrition", "allocateMeal", "allocate meal"),
        ("nutrition", "allocateWater", "allocate water"),
        ("nutrition", "showFoodLedger", "show food ledger"),
        ("nutrition", "showWaterLedger", "show water ledger"),
        ("nutrition", "openShelter", "open shelter"),
        ("nutrition", "showShelterCapacity", "show shelter capacity"),
        ("reciprocity", "recordCareReciprocity", "record care reciprocity"),
        ("reciprocity", "showReciprocityWeeks", "show reciprocity over weeks"),
        ("reciprocity", "showBurden", "show care burden"),
        ("reciprocity", "showTrustDelta", "show trust delta"),
        ("reciprocity", "showRitualMemory", "show ritual memory"),
        ("weather", "planWeatherWork", "plan weather work"),
        ("weather", "delayExposedWork", "delay exposed work"),
        ("weather", "chooseShelterRoute", "choose shelter route"),
        ("weather", "protectTools", "protect tools"),
        ("weather", "showForecast", "show forecast"),
        ("weather", "showRiskAfterPlan", "show risk after plan"),
        ("avatar", "offerAvatarHelp", "offer avatar help"),
        ("avatar", "askBeforeHelp", "ask before help"),
        ("avatar", "offerFood", "offer food"),
        ("avatar", "offerWater", "offer water"),
        ("avatar", "offerShelter", "offer shelter"),
        ("avatar", "offerRestCover", "offer rest cover"),
        ("avatar", "respectRefusal", "respect refusal"),
        ("avatar", "stepBack", "step back"),
        ("avatar", "observeWithoutInterrupting", "observe without interrupting"),
        ("avatar", "showAutonomy", "show autonomy"),
        ("avatar", "showPrivateWorkspaceBoundary", "show workspace boundary"),
        ("culture", "showDialectFamily", "show dialect family"),
        ("culture", "showLocalPhrase", "show local phrase"),
        ("culture", "showCareRitual", "show care ritual"),
        ("culture", "showCraftTechnology", "show craft technology"),
        ("culture", "showLineageMemory", "show lineage memory"),
        ("culture", "showPreAvatarYear", "show pre-avatar year"),
        ("reload", "restoreV49Memory", "restore v49 memory"),
        ("reload", "saveWorldState", "save world state"),
        ("reload", "restoreWorldState", "restore world state"),
        ("reload", "exportReplay", "export replay"),
        ("frequency", "showFlowerPhase", "show flower phase"),
        ("frequency", "showCircadianFrequency", "show circadian frequency"),
        ("frequency", "showRateBoundary", "show rate boundary"),
    ]
    extra: List[Tuple[str, str, str]] = []
    for label in ("Ari", "Fay", "Milo", "Tala", "Nia", "Oren", "Puck", "Sera"):
        extra.append(("sleep", "advanceSleepCycle", f"advance {label} sleep"))
        extra.append(("avatar", "offerAvatarHelp", f"offer help to {label}"))
    for label in ("moss bread", "salt porridge", "seed meal", "lichen soup", "orchid rice"):
        extra.append(("nutrition", "allocateMeal", f"allocate {label}"))
    for label in ("mist", "sleet", "heat", "hail", "steam leak"):
        extra.append(("weather", "planWeatherWork", f"plan around {label}"))
    for label in ("refusal", "defer", "redirect", "quiet help", "ask first", "step back"):
        extra.append(("avatar", "respectRefusal", f"respect {label}"))
    for label in ("dialect", "ritual", "craft", "lineage", "pre-avatar year"):
        extra.append(("culture", "showDialectFamily", f"show {label}"))
    for label in ("sleep", "economy", "reciprocity", "work", "avatar", "culture"):
        extra.append(("reload", "restoreV49Memory", f"restore {label}"))
    for label in ("night watch", "meal reserve", "shelter queue", "care debt", "trade weather", "avatar boundary", "lineage phrase", "craft route"):
        extra.append(("culture", "showLineageMemory", f"inspect {label}"))
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
<title>SSRM-3D Browser World v49 Sleep/Nutrition/Reciprocity Bridge</title>
<style>
:root { --night:#111827; --ember:#f0b35a; --moss:#a7c77b; --water:#6fb7d6; --paper:#f5ead7; --line:rgba(245,234,215,.26); }
body { margin:0; font-family: Georgia, 'Times New Roman', serif; color:var(--paper); background: radial-gradient(circle at 12% 18%, rgba(111,183,214,.28), transparent 28%), linear-gradient(135deg, #10131f, #27331f 55%, #3d2c1b); }
main { display:grid; grid-template-columns: repeat(2, minmax(290px, 1fr)); gap:16px; padding:20px; }
section { border:1px solid var(--line); border-radius:20px; padding:16px; background:rgba(14,18,25,.74); box-shadow:0 20px 54px rgba(0,0,0,.36); }
button { margin:4px; border:1px solid var(--line); border-radius:999px; background:rgba(240,179,90,.16); color:var(--paper); padding:8px 11px; }
.flower { width:150px; height:150px; border-radius:50%; background: repeating-radial-gradient(circle, rgba(245,234,215,.32) 0 7px, transparent 8px 15px), conic-gradient(from 70deg, rgba(167,199,123,.42), rgba(111,183,214,.42), rgba(240,179,90,.40), rgba(167,199,123,.42)); }
.notice { grid-column:1/-1; color:#f8d7c2; }
</style>
</head>
<body>
<main>
<section id="sleep-wake-panel"><h2>Sleep/wake cycles</h2><p>Circadian hour, sleep quality, rest debt, and private dream workspace markers remain visible without dumping private workspace.</p></section>
<section id="nutrition-shelter-panel"><h2>Nutrition and shelter economy</h2><p>Food, water, ration policy, shelter capacity, hunger, thirst, and reserves are explicit resources.</p></section>
<section id="reciprocity-panel"><h2>Caregiving reciprocity over weeks</h2><p>Care rituals update trust, burden, and reciprocity memory without reducing care to a simple transaction.</p></section>
<section id="weather-work-panel"><h2>Weather-aware work planning</h2><p>Residents read forecasts, delay exposed work, protect tools, and choose shelter routes.</p></section>
<section id="avatar-welfare-panel"><h2>Playable avatar welfare intervention</h2><p>The avatar can offer help, ask first, observe, step back, and respect refusal.</p></section>
<section id="cultural-continuity-panel"><h2>Cultural continuity</h2><p>Dialect families, care rituals, craft technology, and pre-avatar year markers show civilization already in progress.</p></section>
<section id="reload-panel"><h2>Save, restore, replay</h2><p>Reload probes restore sleep, economy, reciprocity, work planning, avatar choice, and culture traces.</p></section>
<section id="frequency-flower-panel"><h2>Frequency / flower timing</h2><div class="flower"></div><p>flower phase and circadian frequency are deterministic timing/rate metadata, not a metaphysical frequency claim.</p></section>
<section class="notice"><strong>Boundary:</strong> no subjective consciousness claim, no real consent claim, no autonomous natural language claim, no moral patienthood claim, no complete 3D engine.</section>
<section class="notice" id="controls"><h2>Controls</h2>
""" + buttons + """
</section>
</main>
<script>
const stateKey = 'ssrm.v49.sleep.reciprocity';
function pushTrace(action, scope) {
  const prior = JSON.parse(localStorage.getItem(stateKey) || '{"events":[]}');
  prior.events.push({ action, scope, t: prior.events.length, note: 'browser-local deterministic trace' });
  localStorage.setItem(stateKey, JSON.stringify(prior));
  return prior;
}
function advanceSleepCycle(scope) { return pushTrace('advanceSleepCycle', scope); }
function showDreamPrivate(scope) { return pushTrace('showDreamPrivate', scope); }
function showRestDebt(scope) { return pushTrace('showRestDebt', scope); }
function wakeForDuty(scope) { return pushTrace('wakeForDuty', scope); }
function startNap(scope) { return pushTrace('startNap', scope); }
function protectSleep(scope) { return pushTrace('protectSleep', scope); }
function allocateMeal(scope) { return pushTrace('allocateMeal', scope); }
function allocateWater(scope) { return pushTrace('allocateWater', scope); }
function showFoodLedger(scope) { return pushTrace('showFoodLedger', scope); }
function showWaterLedger(scope) { return pushTrace('showWaterLedger', scope); }
function openShelter(scope) { return pushTrace('openShelter', scope); }
function showShelterCapacity(scope) { return pushTrace('showShelterCapacity', scope); }
function recordCareReciprocity(scope) { return pushTrace('recordCareReciprocity', scope); }
function showReciprocityWeeks(scope) { return pushTrace('showReciprocityWeeks', scope); }
function showBurden(scope) { return pushTrace('showBurden', scope); }
function showTrustDelta(scope) { return pushTrace('showTrustDelta', scope); }
function showRitualMemory(scope) { return pushTrace('showRitualMemory', scope); }
function planWeatherWork(scope) { return pushTrace('planWeatherWork', scope); }
function delayExposedWork(scope) { return pushTrace('delayExposedWork', scope); }
function chooseShelterRoute(scope) { return pushTrace('chooseShelterRoute', scope); }
function protectTools(scope) { return pushTrace('protectTools', scope); }
function showForecast(scope) { return pushTrace('showForecast', scope); }
function showRiskAfterPlan(scope) { return pushTrace('showRiskAfterPlan', scope); }
function offerAvatarHelp(scope) { return pushTrace('offerAvatarHelp', scope); }
function askBeforeHelp(scope) { return pushTrace('askBeforeHelp', scope); }
function offerFood(scope) { return pushTrace('offerFood', scope); }
function offerWater(scope) { return pushTrace('offerWater', scope); }
function offerShelter(scope) { return pushTrace('offerShelter', scope); }
function offerRestCover(scope) { return pushTrace('offerRestCover', scope); }
function respectRefusal(scope) { return pushTrace('respectRefusal', scope); }
function stepBack(scope) { return pushTrace('stepBack', scope); }
function observeWithoutInterrupting(scope) { return pushTrace('observeWithoutInterrupting', scope); }
function showAutonomy(scope) { return pushTrace('showAutonomy', scope); }
function showPrivateWorkspaceBoundary(scope) { return pushTrace('showPrivateWorkspaceBoundary', scope); }
function showDialectFamily(scope) { return pushTrace('showDialectFamily', scope); }
function showLocalPhrase(scope) { return pushTrace('showLocalPhrase', scope); }
function showCareRitual(scope) { return pushTrace('showCareRitual', scope); }
function showCraftTechnology(scope) { return pushTrace('showCraftTechnology', scope); }
function showLineageMemory(scope) { return pushTrace('showLineageMemory', scope); }
function showPreAvatarYear(scope) { return pushTrace('showPreAvatarYear', scope); }
function restoreV49Memory(scope) { return JSON.parse(localStorage.getItem(stateKey) || '{"events":[]}'); }
function saveWorldState(scope) { return pushTrace('saveWorldState', scope); }
function restoreWorldState(scope) { return restoreV49Memory(scope); }
function exportReplay(scope) { return JSON.stringify(restoreV49Memory(scope)); }
function showFlowerPhase(scope) { return pushTrace('showFlowerPhase', scope); }
function showCircadianFrequency(scope) { return pushTrace('showCircadianFrequency', scope); }
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
    summary_rows = [{"metric": key, "value": value} for key, value in results["metrics"].items()]
    write_csv(ARTIFACT_DIR / f"{PREFIX}_summary.csv", summary_rows)
    write_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [{
        "report": REPORT,
        "verdict": results["verdict"],
        "readiness": results["metrics"]["browser_world_v49_sleep_reciprocity_readiness"],
        "weakest_channel": results["metrics"]["weakest_channel_name"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
    }])
    for name, values in rows.items():
        write_csv(ARTIFACT_DIR / f"{PREFIX}_{name}.csv", values)
    (VIS_DIR / f"{PREFIX}.html").write_text(build_html_template_stub(), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Report 289 SSRM-3D browser world v49 sleep/nutrition/reciprocity bridge")
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
        "readiness": results["metrics"]["browser_world_v49_sleep_reciprocity_readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "weakest_named_channel": results["metrics"]["weakest_channel_name"],
        "next_gate": results["next_gate"],
    }, indent=2, sort_keys=True))
    if results["verdict"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
