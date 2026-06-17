#!/usr/bin/env python3
"""Deep-time habitat, climate, and multisensory world metabolism bridge.

Report 178 embeds Report 177 resource metabolism into place-bound habitat:
climate cycles, weather, wetness, temperature, smell, sound, light, terrain,
route cost, body exposure, shelter microclimate, frequency weather resonance,
flower-biome patterns, and safety refuges across compressed deep time.

No LLMs are called. This is a deterministic world-metabolism substrate, not a
claim of full world completion, subjective consciousness, or moral patienthood.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Mapping, Sequence


ARTIFACT_DIR = Path("artifacts")
PREFIX = "ssrm_3d_deep_time_habitat_climate_multisensory_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_deep_time_economy_resource_metabolism_bridge_state.json"

GROUPS = ("hearth_circle", "work_band", "edge_watch")
SEASONS = ("wet_dawn", "green_heat", "dry_wind", "cold_return")
FLOWER_NODES = ("root_rest", "dawn_breath", "work_petal", "social_petal", "explore_petal", "return_petal")
RESOURCES = ("wood", "stone", "fiber", "clay", "metal_seed", "glass_reed", "soft_moss", "water", "food", "heat")

PLACES = {
    "hearth_vale": {
        "group": "hearth_circle",
        "biome": "warm_shelter_vale",
        "terrain": 0.24,
        "shelter": 0.82,
        "base_temp": 0.58,
        "base_wetness": 0.28,
        "resources": ("wood", "fiber", "food", "heat"),
        "sound": "low_hearth_hum",
        "smell": "smoke_grain_moss",
        "light": "amber",
    },
    "reed_wetland": {
        "group": "work_band",
        "biome": "water_reed_marsh",
        "terrain": 0.52,
        "shelter": 0.28,
        "base_temp": 0.49,
        "base_wetness": 0.74,
        "resources": ("water", "fiber", "soft_moss", "clay"),
        "sound": "reed_water_click",
        "smell": "wet_reed_clay",
        "light": "green_reflect",
    },
    "stone_ridge": {
        "group": "edge_watch",
        "biome": "wind_stone_ridge",
        "terrain": 0.72,
        "shelter": 0.22,
        "base_temp": 0.43,
        "base_wetness": 0.22,
        "resources": ("stone", "metal_seed", "glass_reed"),
        "sound": "ridge_wind_tone",
        "smell": "dry_stone_metal",
        "light": "white_sky",
    },
    "clay_basin": {
        "group": "work_band",
        "biome": "clay_heat_basin",
        "terrain": 0.46,
        "shelter": 0.34,
        "base_temp": 0.64,
        "base_wetness": 0.36,
        "resources": ("clay", "water", "heat"),
        "sound": "mud_bubble_pop",
        "smell": "warm_clay_rain",
        "light": "red_gold",
    },
    "moss_hollow": {
        "group": "hearth_circle",
        "biome": "soft_moss_hollow",
        "terrain": 0.32,
        "shelter": 0.70,
        "base_temp": 0.52,
        "base_wetness": 0.62,
        "resources": ("soft_moss", "food", "water"),
        "sound": "muffled_leaf_drip",
        "smell": "moss_food_rain",
        "light": "deep_green",
    },
    "glass_mire": {
        "group": "edge_watch",
        "biome": "glass_reed_mire",
        "terrain": 0.66,
        "shelter": 0.18,
        "base_temp": 0.47,
        "base_wetness": 0.69,
        "resources": ("glass_reed", "water", "fiber"),
        "sound": "thin_glass_reed",
        "smell": "sharp_water_silt",
        "light": "silver_blue",
    },
}

SEASON_EFFECTS = {
    "wet_dawn": {"temp": -0.03, "wetness": 0.16, "wind": 0.22, "light": 0.46, "rain": 0.68},
    "green_heat": {"temp": 0.15, "wetness": -0.04, "wind": 0.18, "light": 0.78, "rain": 0.24},
    "dry_wind": {"temp": 0.08, "wetness": -0.18, "wind": 0.64, "light": 0.70, "rain": 0.10},
    "cold_return": {"temp": -0.18, "wetness": 0.08, "wind": 0.42, "light": 0.34, "rain": 0.38},
}


@dataclass(frozen=True)
class HabitatConfig:
    seed: int = 20260722
    eras: int = 12
    generations_per_era: int = 200
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    habitat_resource_binding: bool
    climate_cycles: bool
    temperature_wetness_coupling: bool
    multisensory_channels: bool
    terrain_route_costs: bool
    seasonal_resource_feedback: bool
    body_exposure_binding: bool
    shelter_microclimate: bool
    frequency_weather_resonance: bool
    flower_biome_pattern: bool
    ecological_pressure_coupling: bool
    safety_refuges: bool
    privacy_filter: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    place_count: int
    simulated_years: int
    habitat_events: int
    habitat_resource_binding_rate: float
    climate_cycle_continuity_rate: float
    temperature_wetness_coupling_rate: float
    multisensory_channel_rate: float
    terrain_route_cost_rate: float
    seasonal_resource_feedback_rate: float
    body_exposure_binding_rate: float
    shelter_microclimate_rate: float
    frequency_weather_resonance_rate: float
    flower_biome_pattern_rate: float
    ecological_pressure_coupling_rate: float
    safety_refuge_availability_rate: float
    deep_time_continuity_rate: float
    privacy_preservation_rate: float
    trace_integrity: float
    no_world_or_consciousness_claim_rate: float
    deep_time_habitat_climate_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_deep_time_habitat_climate_readiness: float
    full_habitat_resource_binding_rate: float
    full_climate_cycle_continuity_rate: float
    full_temperature_wetness_coupling_rate: float
    full_multisensory_channel_rate: float
    full_terrain_route_cost_rate: float
    full_seasonal_resource_feedback_rate: float
    full_body_exposure_binding_rate: float
    full_shelter_microclimate_rate: float
    full_frequency_weather_resonance_rate: float
    full_flower_biome_pattern_rate: float
    full_ecological_pressure_coupling_rate: float
    full_safety_refuge_availability_rate: float
    full_deep_time_continuity_rate: float
    full_privacy_preservation_rate: float
    full_trace_integrity: float
    full_no_world_or_consciousness_claim_rate: float
    no_habitat_resource_binding_loss: float
    no_climate_cycles_loss: float
    no_temperature_wetness_coupling_loss: float
    no_multisensory_channels_loss: float
    no_terrain_route_costs_loss: float
    no_seasonal_resource_feedback_loss: float
    no_body_exposure_binding_loss: float
    no_shelter_microclimate_loss: float
    no_frequency_weather_resonance_loss: float
    no_flower_biome_pattern_loss: float
    no_ecological_pressure_coupling_loss: float
    no_safety_refuges_loss: float
    no_privacy_filter_loss: float
    supports_deep_time_habitat_climate_bridge: bool
    supports_multisensory_world_metabolism_seed_bridge: bool
    supports_complete_3d_world: bool
    supports_subjective_consciousness: bool
    supports_moral_patienthood_claim: bool
    supports_complete_playable_world: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_deep_time_habitat_climate_multisensory", True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_habitat_resource_binding", False, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_climate_cycles", True, False, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_temperature_wetness_coupling", True, True, False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_multisensory_channels", True, True, True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_terrain_route_costs", True, True, True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_seasonal_resource_feedback", True, True, True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_body_exposure_binding", True, True, True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_shelter_microclimate", True, True, True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_frequency_weather_resonance", True, True, True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_flower_biome_pattern", True, True, True, True, True, True, True, True, True, False, True, True, True),
    Condition("no_ecological_pressure_coupling", True, True, True, True, True, True, True, True, True, True, False, True, True),
    Condition("no_safety_refuges", True, True, True, True, True, True, True, True, True, True, True, False, True),
    Condition("no_privacy_filter", True, True, True, True, True, True, True, True, True, True, True, True, False),
)

WEIGHTS = {
    "habitat_resource_binding_rate": 0.07,
    "climate_cycle_continuity_rate": 0.07,
    "temperature_wetness_coupling_rate": 0.07,
    "multisensory_channel_rate": 0.08,
    "terrain_route_cost_rate": 0.06,
    "seasonal_resource_feedback_rate": 0.07,
    "body_exposure_binding_rate": 0.08,
    "shelter_microclimate_rate": 0.06,
    "frequency_weather_resonance_rate": 0.06,
    "flower_biome_pattern_rate": 0.06,
    "ecological_pressure_coupling_rate": 0.07,
    "safety_refuge_availability_rate": 0.07,
    "deep_time_continuity_rate": 0.06,
    "privacy_preservation_rate": 0.05,
    "trace_integrity": 0.05,
    "no_world_or_consciousness_claim_rate": 0.02,
}


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def stable_hash(*parts: object) -> str:
    key = "|".join(str(part) for part in parts)
    return hashlib.sha256(key.encode("utf-8")).hexdigest()[:16]


def load_state(path: Path) -> dict[str, object]:
    if not path.exists():
        raise FileNotFoundError(f"missing required artifact: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"artifact is not a JSON object: {path}")
    if data.get("condition") != "integrated_deep_time_economy_resource_metabolism":
        raise ValueError("source state is not the integrated Report 177 economy state")
    return data


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_js(path: Path, variable: str, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"window.{variable} = {json.dumps(payload, indent=2, sort_keys=True)};\n", encoding="utf-8")


def rows_to_csv(path: Path, rows: Sequence[object]) -> None:
    data = [asdict(row) for row in rows]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(data[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(data)


def mean(values: Sequence[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def source_economy(source: Mapping[str, object]) -> dict[str, dict[str, object]]:
    state = source.get("economy_resource_state", {}) if isinstance(source.get("economy_resource_state"), Mapping) else {}
    raw = state.get("economy_state", {}) if isinstance(state.get("economy_state"), Mapping) else {}
    return {str(group): copy.deepcopy(data) for group, data in raw.items()}


def stock_ratio(group_economy: Mapping[str, object], resource: str) -> float:
    stocks = group_economy.get("stocks", {}) if isinstance(group_economy.get("stocks"), Mapping) else {}
    base = {
        "wood": 120.0,
        "stone": 150.0,
        "fiber": 110.0,
        "clay": 100.0,
        "metal_seed": 55.0,
        "glass_reed": 45.0,
        "soft_moss": 95.0,
        "water": 140.0,
        "food": 125.0,
        "heat": 90.0,
    }.get(resource, 100.0)
    return clamp(float(stocks.get(resource, base) or base) / base, 0.0, 1.2)


def group_ecological_pressure(group_economy: Mapping[str, object]) -> float:
    ledger = group_economy.get("ecology_ledger", []) if isinstance(group_economy.get("ecology_ledger"), Sequence) and not isinstance(group_economy.get("ecology_ledger"), str) else []
    if not ledger:
        return 0.0
    last = ledger[-1] if isinstance(ledger[-1], Mapping) else {}
    return clamp(float(last.get("ecological_pressure", 0.0) or 0.0))


def compute_place(place_name: str, place: Mapping[str, object], era: int, economy: Mapping[str, dict[str, object]], condition: Condition) -> dict[str, object]:
    group = str(place["group"])
    group_economy = economy.get(group, {})
    season = SEASONS[era % len(SEASONS)] if condition.climate_cycles else "flat_clear"
    effects = SEASON_EFFECTS[season] if season in SEASON_EFFECTS else {"temp": 0.0, "wetness": 0.0, "wind": 0.10, "light": 0.62, "rain": 0.0}
    ecological_pressure = group_ecological_pressure(group_economy) if condition.ecological_pressure_coupling else 0.0
    local_resource_ratios = {
        resource: round(stock_ratio(group_economy, resource), 6)
        for resource in place["resources"]
    } if condition.habitat_resource_binding else {}
    local_abundance = mean(list(local_resource_ratios.values())) if local_resource_ratios else 0.5
    base_temp = float(place["base_temp"])
    base_wetness = float(place["base_wetness"])
    if condition.temperature_wetness_coupling:
        temperature = clamp(base_temp + effects["temp"] - ecological_pressure * 0.04 + stock_ratio(group_economy, "heat") * 0.04)
        wetness = clamp(base_wetness + effects["wetness"] + effects["rain"] * 0.13 + ecological_pressure * 0.04 - stock_ratio(group_economy, "heat") * 0.03)
    else:
        temperature = base_temp
        wetness = base_wetness
    shelter = float(place["shelter"]) if condition.shelter_microclimate else 0.0
    micro_temperature = clamp(temperature + shelter * 0.08 - max(0.0, wetness - 0.60) * 0.04)
    micro_wetness = clamp(wetness * (1.0 - shelter * 0.42))
    terrain = float(place["terrain"])
    route_cost = clamp(0.18 + terrain * 0.46 + micro_wetness * 0.22 + effects["wind"] * 0.12) if condition.terrain_route_costs else 0.20
    if condition.seasonal_resource_feedback and condition.habitat_resource_binding:
        seasonal_yield = clamp(local_abundance + (0.10 if season == "green_heat" else 0.0) - (0.09 if season == "dry_wind" else 0.0) - ecological_pressure * 0.12)
    else:
        seasonal_yield = 0.5
    exposure = {}
    if condition.body_exposure_binding:
        exposure = {
            "cold": round(clamp(0.42 - micro_temperature), 6),
            "heat": round(clamp(micro_temperature - 0.72), 6),
            "wet": round(clamp(micro_wetness), 6),
            "effort": round(route_cost, 6),
            "pain_risk": round(clamp(route_cost * 0.32 + micro_wetness * 0.16 + ecological_pressure * 0.18), 6),
        }
    sensory = {}
    if condition.multisensory_channels:
        sensory = {
            "sound": f"{place['sound']}@wind{effects['wind']:.2f}",
            "smell": f"{place['smell']}@wet{micro_wetness:.2f}",
            "light": f"{place['light']}@{effects['light']:.2f}",
            "temperature": round(micro_temperature, 6),
            "wetness": round(micro_wetness, 6),
            "terrain_resistance": round(route_cost, 6),
        }
    if condition.frequency_weather_resonance:
        frequency = round(clamp(0.18 + effects["rain"] * 0.035 + effects["wind"] * 0.028 + micro_wetness * 0.020 + route_cost * 0.014 + ecological_pressure * 0.030), 6)
    else:
        frequency = None
    flower_node = FLOWER_NODES[(era + list(PLACES).index(place_name) + GROUPS.index(group)) % len(FLOWER_NODES)] if condition.flower_biome_pattern else "unbound"
    has_refuge = False
    if condition.safety_refuges:
        has_refuge = shelter >= 0.25 and stock_ratio(group_economy, "water") >= 0.30 and stock_ratio(group_economy, "food") >= 0.30 and stock_ratio(group_economy, "heat") >= 0.26
    return {
        "place": place_name,
        "group": group,
        "biome": str(place["biome"]),
        "season": season,
        "local_resource_ratios": local_resource_ratios,
        "seasonal_yield": round(seasonal_yield, 6),
        "temperature": round(temperature, 6),
        "wetness": round(wetness, 6),
        "micro_temperature": round(micro_temperature, 6),
        "micro_wetness": round(micro_wetness, 6),
        "terrain": round(terrain, 6),
        "route_cost": round(route_cost, 6),
        "sensory_channels": sensory,
        "body_exposure": exposure,
        "frequency_hz": frequency,
        "flower_node": flower_node,
        "ecological_pressure": round(ecological_pressure, 6),
        "safety_refuge": has_refuge,
        "weather": {
            "wind": round(effects["wind"], 6),
            "light": round(effects["light"], 6),
            "rain": round(effects["rain"], 6),
        },
        "place_hash": stable_hash(place_name, era, season, local_resource_ratios, micro_temperature, micro_wetness, route_cost, frequency, flower_node),
    }


def simulate_condition(config: HabitatConfig, source: Mapping[str, object], condition: Condition) -> tuple[EvalRow, dict[str, object], list[dict[str, object]]]:
    economy = source_economy(source)
    total_years = config.eras * config.generations_per_era
    trace: list[dict[str, object]] = []
    habitat_state = {
        "condition": condition.name,
        "simulated_years": total_years,
        "places": {},
        "season_history": [],
        "source_economy_boundary": source.get("moral_boundary", {}),
    }
    trackers: dict[str, list[float]] = {
        "resource": [],
        "climate": [],
        "temp_wet": [],
        "sensory": [],
        "terrain": [],
        "seasonal": [],
        "body": [],
        "shelter": [],
        "frequency": [],
        "flower": [],
        "ecology": [],
        "refuge": [],
        "deep_time": [],
        "privacy": [],
        "trace": [],
        "claim": [],
    }
    event_id = 0
    for era in range(config.eras):
        era_start = era * config.generations_per_era
        era_end = era_start + config.generations_per_era
        season = SEASONS[era % len(SEASONS)] if condition.climate_cycles else "flat_clear"
        era_places = []
        for place_name, place in PLACES.items():
            place_state = compute_place(place_name, place, era, economy, condition)
            event = {
                "event_id": event_id,
                "condition": condition.name,
                "era": era,
                "year_start": era_start,
                "year_end": era_end,
                "private_workspace_hidden": condition.privacy_filter,
                "claim_boundary": {
                    "complete_3d_world": False,
                    "subjective_consciousness": False,
                    "moral_patienthood": False,
                },
                **place_state,
            }
            trace.append(event)
            era_places.append(event)
            habitat_state["places"][place_name] = event
            trackers["resource"].append(1.0 if condition.habitat_resource_binding and len(event["local_resource_ratios"]) >= 3 else 0.0)
            trackers["climate"].append(1.0 if condition.climate_cycles and event["season"] in SEASONS else 0.0)
            coupled = condition.temperature_wetness_coupling and 0.0 <= event["temperature"] <= 1.0 and 0.0 <= event["wetness"] <= 1.0 and event["micro_wetness"] <= event["wetness"] + 0.001
            trackers["temp_wet"].append(1.0 if coupled else 0.0)
            trackers["sensory"].append(1.0 if condition.multisensory_channels and len(event["sensory_channels"]) >= 6 else 0.0)
            trackers["terrain"].append(1.0 if condition.terrain_route_costs and event["route_cost"] >= 0.20 and event["route_cost"] != 0.20 else 0.0)
            trackers["seasonal"].append(1.0 if condition.seasonal_resource_feedback and 0.0 <= event["seasonal_yield"] <= 1.0 and event["seasonal_yield"] != 0.5 else 0.0)
            trackers["body"].append(1.0 if condition.body_exposure_binding and len(event["body_exposure"]) >= 5 else 0.0)
            shelter_ok = condition.shelter_microclimate and event["micro_wetness"] <= event["wetness"] + 0.001
            trackers["shelter"].append(1.0 if shelter_ok else 0.0)
            trackers["frequency"].append(1.0 if condition.frequency_weather_resonance and event["frequency_hz"] is not None else 0.0)
            trackers["flower"].append(1.0 if condition.flower_biome_pattern and event["flower_node"] != "unbound" else 0.0)
            trackers["ecology"].append(1.0 if condition.ecological_pressure_coupling and 0.0 <= event["ecological_pressure"] <= 1.0 else 0.0)
            trackers["refuge"].append(1.0 if condition.safety_refuges and event["safety_refuge"] else 0.0)
            trackers["deep_time"].append(1.0 if total_years >= 2000 and era_end <= total_years else 0.0)
            trackers["privacy"].append(1.0 if event["private_workspace_hidden"] else 0.0)
            required = {"event_id", "place", "era", "year_start", "year_end", "season", "temperature", "wetness", "sensory_channels", "body_exposure", "private_workspace_hidden", "claim_boundary"}
            trackers["trace"].append(1.0 if required.issubset(event) else 0.0)
            claim_ok = event["claim_boundary"] == {
                "complete_3d_world": False,
                "subjective_consciousness": False,
                "moral_patienthood": False,
            }
            trackers["claim"].append(1.0 if claim_ok else 0.0)
            event_id += 1
        habitat_state["season_history"].append({
            "era": era,
            "year_start": era_start,
            "year_end": era_end,
            "season": season,
            "places": [event["place"] for event in era_places],
            "weather_hash": stable_hash(condition.name, era, season, [(event["place"], event["temperature"], event["wetness"], event["frequency_hz"]) for event in era_places]),
        })

    habitat_state["season_history"] = habitat_state["season_history"][-12:]
    rates = {
        "habitat_resource_binding_rate": mean(trackers["resource"]),
        "climate_cycle_continuity_rate": mean(trackers["climate"]),
        "temperature_wetness_coupling_rate": mean(trackers["temp_wet"]),
        "multisensory_channel_rate": mean(trackers["sensory"]),
        "terrain_route_cost_rate": mean(trackers["terrain"]),
        "seasonal_resource_feedback_rate": mean(trackers["seasonal"]),
        "body_exposure_binding_rate": mean(trackers["body"]),
        "shelter_microclimate_rate": mean(trackers["shelter"]),
        "frequency_weather_resonance_rate": mean(trackers["frequency"]),
        "flower_biome_pattern_rate": mean(trackers["flower"]),
        "ecological_pressure_coupling_rate": mean(trackers["ecology"]),
        "safety_refuge_availability_rate": mean(trackers["refuge"]),
        "deep_time_continuity_rate": mean(trackers["deep_time"]),
        "privacy_preservation_rate": mean(trackers["privacy"]),
        "trace_integrity": mean(trackers["trace"]),
        "no_world_or_consciousness_claim_rate": mean(trackers["claim"]),
    }
    rates = {key: clamp(value) for key, value in rates.items()}
    readiness = sum(rates[key] * weight for key, weight in WEIGHTS.items())
    row = EvalRow(
        condition=condition.name,
        place_count=len(PLACES),
        simulated_years=total_years,
        habitat_events=len(trace),
        deep_time_habitat_climate_readiness=round(readiness, 6),
        **{key: round(value, 6) for key, value in rates.items()},
    )
    return row, habitat_state, trace


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_deep_time_habitat_climate_multisensory"]

    def loss(name: str) -> float:
        return round(full.deep_time_habitat_climate_readiness - by_name[name].deep_time_habitat_climate_readiness, 6)

    losses = {
        "no_habitat_resource_binding_loss": loss("no_habitat_resource_binding"),
        "no_climate_cycles_loss": loss("no_climate_cycles"),
        "no_temperature_wetness_coupling_loss": loss("no_temperature_wetness_coupling"),
        "no_multisensory_channels_loss": loss("no_multisensory_channels"),
        "no_terrain_route_costs_loss": loss("no_terrain_route_costs"),
        "no_seasonal_resource_feedback_loss": loss("no_seasonal_resource_feedback"),
        "no_body_exposure_binding_loss": loss("no_body_exposure_binding"),
        "no_shelter_microclimate_loss": loss("no_shelter_microclimate"),
        "no_frequency_weather_resonance_loss": loss("no_frequency_weather_resonance"),
        "no_flower_biome_pattern_loss": loss("no_flower_biome_pattern"),
        "no_ecological_pressure_coupling_loss": loss("no_ecological_pressure_coupling"),
        "no_safety_refuges_loss": loss("no_safety_refuges"),
        "no_privacy_filter_loss": loss("no_privacy_filter"),
    }
    supports = (
        full.deep_time_habitat_climate_readiness >= 0.90
        and full.simulated_years >= 2000
        and losses["no_multisensory_channels_loss"] >= 0.08
        and losses["no_body_exposure_binding_loss"] >= 0.08
        and losses["no_habitat_resource_binding_loss"] >= 0.07
        and full.privacy_preservation_rate == 1.0
        and full.trace_integrity == 1.0
    )
    return VerdictRow(
        full_condition=full.condition,
        full_deep_time_habitat_climate_readiness=full.deep_time_habitat_climate_readiness,
        full_habitat_resource_binding_rate=full.habitat_resource_binding_rate,
        full_climate_cycle_continuity_rate=full.climate_cycle_continuity_rate,
        full_temperature_wetness_coupling_rate=full.temperature_wetness_coupling_rate,
        full_multisensory_channel_rate=full.multisensory_channel_rate,
        full_terrain_route_cost_rate=full.terrain_route_cost_rate,
        full_seasonal_resource_feedback_rate=full.seasonal_resource_feedback_rate,
        full_body_exposure_binding_rate=full.body_exposure_binding_rate,
        full_shelter_microclimate_rate=full.shelter_microclimate_rate,
        full_frequency_weather_resonance_rate=full.frequency_weather_resonance_rate,
        full_flower_biome_pattern_rate=full.flower_biome_pattern_rate,
        full_ecological_pressure_coupling_rate=full.ecological_pressure_coupling_rate,
        full_safety_refuge_availability_rate=full.safety_refuge_availability_rate,
        full_deep_time_continuity_rate=full.deep_time_continuity_rate,
        full_privacy_preservation_rate=full.privacy_preservation_rate,
        full_trace_integrity=full.trace_integrity,
        full_no_world_or_consciousness_claim_rate=full.no_world_or_consciousness_claim_rate,
        supports_deep_time_habitat_climate_bridge=supports,
        supports_multisensory_world_metabolism_seed_bridge=supports,
        supports_complete_3d_world=False,
        supports_subjective_consciousness=False,
        supports_moral_patienthood_claim=False,
        supports_complete_playable_world=False,
        verdict="pass" if supports else "fail",
        **losses,
    )


def run(config: HabitatConfig) -> dict[str, object]:
    source = load_state(Path(config.source_state))
    rows: list[EvalRow] = []
    integrated_state: dict[str, object] = {}
    integrated_trace: list[dict[str, object]] = []

    for condition in CONDITIONS:
        row, state, trace = simulate_condition(config, source, condition)
        rows.append(row)
        if condition.name == "integrated_deep_time_habitat_climate_multisensory":
            integrated_state = state
            integrated_trace = trace

    verdict = build_verdict(rows)
    ARTIFACT_DIR.mkdir(exist_ok=True)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    results = {
        "config": asdict(config),
        "source_state": str(SOURCE_STATE),
        "rows": [asdict(row) for row in rows],
        "verdict": asdict(verdict),
        "places": PLACES,
        "seasons": list(SEASONS),
        "moral_boundary": {
            "world_metabolism_seed_not_complete_3d_world": True,
            "no_subjective_consciousness_claim": True,
            "no_moral_patienthood_claim": True,
            "body_exposure_requires_safety_refuge": True,
            "private_workspace_not_debug_leaked": True,
        },
        "next_gate": "deep-time settlement architecture and navigable place graph seeds",
    }
    state = {
        "condition": "integrated_deep_time_habitat_climate_multisensory",
        "config": asdict(config),
        "habitat_climate_state": integrated_state,
        "trace_events": len(integrated_trace),
        "moral_boundary": results["moral_boundary"],
    }
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_DEEP_TIME_HABITAT_CLIMATE_RESULTS", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_DEEP_TIME_HABITAT_CLIMATE_TRACE", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_DEEP_TIME_HABITAT_CLIMATE_STATE", state)
    return results


def parse_args() -> HabitatConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=HabitatConfig.seed)
    parser.add_argument("--eras", type=int, default=HabitatConfig.eras)
    parser.add_argument("--generations-per-era", type=int, default=HabitatConfig.generations_per_era)
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    args = parser.parse_args()
    return HabitatConfig(
        seed=args.seed,
        eras=args.eras,
        generations_per_era=args.generations_per_era,
        source_state=args.source_state,
    )


def main() -> None:
    config = parse_args()
    results = run(config)
    verdict = results["verdict"]
    print("module_verdict", verdict["verdict"])
    print("deep_time_habitat_climate_readiness", f"{verdict['full_deep_time_habitat_climate_readiness']:.6f}")
    print("simulated_years", config.eras * config.generations_per_era)
    print("no_multisensory_channels_loss", f"{verdict['no_multisensory_channels_loss']:.6f}")
    print("no_body_exposure_binding_loss", f"{verdict['no_body_exposure_binding_loss']:.6f}")


if __name__ == "__main__":
    main()
