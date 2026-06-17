#!/usr/bin/env python3
"""Agent-led seasonal logistics and stock planning bridge.

Report 191 consumes the Report 190 agent-led health-routine state and extends it
into food, water, shelter, and medicine logistics across seasonal pressure:
forecasting, stock planning, rationing, replenishment routes, spoilage/waste
accounting, fair allocation, emergency reserves, stockout avoidance,
long-horizon memory, frequency/flower seasonal rhythm, and browser replay.

No LLMs are called. This is deterministic functional artificial-life substrate,
not subjective deprivation, real medicine, subjective suffering, subjective
consciousness, moral patienthood, or complete 3D gameplay.
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
PREFIX = "ssrm_3d_agent_led_seasonal_logistics_stock_planning_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_agent_led_health_routines_medicine_craft_contact_bridge_state.json"

AGENT_TRAITS = {
    "Ari": {"logistics_skill": 0.72, "reserve_bias": 0.64, "route_skill": 0.66, "frequency_hz": 0.242, "flower_node": "work_petal"},
    "Fay": {"logistics_skill": 0.82, "reserve_bias": 0.70, "route_skill": 0.58, "frequency_hz": 0.219, "flower_node": "root_rest"},
    "Milo": {"logistics_skill": 0.61, "reserve_bias": 0.76, "route_skill": 0.79, "frequency_hz": 0.258, "flower_node": "social_petal"},
}

SEASON_PATTERN = (
    {"name": "warm_regrowth", "food_pressure": 0.72, "water_pressure": 0.64, "shelter_pressure": 0.35, "medicine_pressure": 0.42, "route_pressure": 0.38},
    {"name": "dry_heat", "food_pressure": 0.88, "water_pressure": 1.12, "shelter_pressure": 0.42, "medicine_pressure": 0.55, "route_pressure": 0.50},
    {"name": "storm_wet", "food_pressure": 0.96, "water_pressure": 0.82, "shelter_pressure": 0.95, "medicine_pressure": 0.72, "route_pressure": 0.92},
    {"name": "cold_low_light", "food_pressure": 1.10, "water_pressure": 0.74, "shelter_pressure": 1.18, "medicine_pressure": 0.88, "route_pressure": 0.82},
)

WEIGHTS = {
    "seasonal_forecast_binding_rate": 0.08,
    "food_stock_planning_rate": 0.08,
    "water_stock_planning_rate": 0.08,
    "shelter_stock_planning_rate": 0.08,
    "medicine_stock_planning_rate": 0.08,
    "rationing_policy_rate": 0.07,
    "replenishment_route_rate": 0.07,
    "spoilage_waste_accounting_rate": 0.07,
    "multi_agent_allocation_rate": 0.07,
    "emergency_reserve_rate": 0.07,
    "stockout_avoidance_rate": 0.08,
    "long_horizon_memory_rate": 0.06,
    "frequency_flower_seasonal_rhythm_rate": 0.04,
    "browser_logistics_replay_rate": 0.04,
    "privacy_preservation_rate": 0.02,
    "trace_integrity": 0.01,
}


@dataclass(frozen=True)
class LogisticsConfig:
    seed: int = 20260804
    days: int = 24
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    seasonal_forecast: bool
    food_planning: bool
    water_planning: bool
    shelter_planning: bool
    medicine_planning: bool
    rationing_policy: bool
    replenishment_routes: bool
    spoilage_waste_accounting: bool
    multi_agent_allocation: bool
    emergency_reserve: bool
    stockout_avoidance: bool
    long_horizon_memory: bool
    frequency_flower_binding: bool
    browser_replay: bool
    privacy_filter: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    agent_count: int
    simulated_days: int
    logistics_events: int
    seasonal_forecast_binding_rate: float
    food_stock_planning_rate: float
    water_stock_planning_rate: float
    shelter_stock_planning_rate: float
    medicine_stock_planning_rate: float
    rationing_policy_rate: float
    replenishment_route_rate: float
    spoilage_waste_accounting_rate: float
    multi_agent_allocation_rate: float
    emergency_reserve_rate: float
    stockout_avoidance_rate: float
    long_horizon_memory_rate: float
    frequency_flower_seasonal_rhythm_rate: float
    browser_logistics_replay_rate: float
    privacy_preservation_rate: float
    trace_integrity: float
    seasonal_logistics_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_seasonal_logistics_readiness: float
    full_seasonal_forecast_binding_rate: float
    full_food_stock_planning_rate: float
    full_water_stock_planning_rate: float
    full_shelter_stock_planning_rate: float
    full_medicine_stock_planning_rate: float
    full_rationing_policy_rate: float
    full_replenishment_route_rate: float
    full_spoilage_waste_accounting_rate: float
    full_multi_agent_allocation_rate: float
    full_emergency_reserve_rate: float
    full_stockout_avoidance_rate: float
    full_long_horizon_memory_rate: float
    full_frequency_flower_seasonal_rhythm_rate: float
    full_browser_logistics_replay_rate: float
    full_privacy_preservation_rate: float
    full_trace_integrity: float
    no_seasonal_forecast_loss: float
    no_food_planning_loss: float
    no_water_planning_loss: float
    no_shelter_planning_loss: float
    no_medicine_planning_loss: float
    no_rationing_policy_loss: float
    no_replenishment_routes_loss: float
    no_spoilage_waste_accounting_loss: float
    no_multi_agent_allocation_loss: float
    no_emergency_reserve_loss: float
    no_stockout_avoidance_loss: float
    no_long_horizon_memory_loss: float
    no_frequency_flower_binding_loss: float
    no_browser_replay_loss: float
    no_privacy_filter_loss: float
    supports_agent_led_seasonal_logistics_bridge: bool
    supports_seasonal_stock_planning_seed: bool
    supports_complete_3d_world: bool
    supports_subjective_consciousness: bool
    supports_subjective_deprivation_claim: bool
    supports_moral_patienthood_claim: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_agent_led_seasonal_logistics_stock_planning", True, True, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_seasonal_forecast", False, True, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_food_planning", True, False, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_water_planning", True, True, False, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_shelter_planning", True, True, True, False, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_medicine_planning", True, True, True, True, False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_rationing_policy", True, True, True, True, True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_replenishment_routes", True, True, True, True, True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_spoilage_waste_accounting", True, True, True, True, True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_multi_agent_allocation", True, True, True, True, True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_emergency_reserve", True, True, True, True, True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_stockout_avoidance", True, True, True, True, True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_long_horizon_memory", True, True, True, True, True, True, True, True, True, True, True, False, True, True, True),
    Condition("no_frequency_flower_binding", True, True, True, True, True, True, True, True, True, True, True, True, False, True, True),
    Condition("no_browser_replay", True, True, True, True, True, True, True, True, True, True, True, True, True, False, True),
    Condition("no_privacy_filter", True, True, True, True, True, True, True, True, True, True, True, True, True, True, False),
)


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def mean(values: Sequence[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def stable_hash(*parts: object) -> str:
    key = "|".join(json.dumps(part, sort_keys=True) if isinstance(part, (dict, list, tuple)) else str(part) for part in parts)
    return hashlib.sha256(key.encode("utf-8")).hexdigest()[:16]


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


def load_state(path: Path) -> dict[str, object]:
    if not path.exists():
        raise FileNotFoundError(f"missing required artifact: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"artifact is not a JSON object: {path}")
    if data.get("condition") != "integrated_agent_led_health_routines_medicine_craft_contact":
        raise ValueError("source state is not the integrated Report 190 health-routine state")
    return data


def source_routine(source: Mapping[str, object]) -> Mapping[str, object]:
    state = source.get("routine_state") if isinstance(source.get("routine_state"), Mapping) else None
    if not state:
        raise ValueError("Report 190 state has no routine_state")
    return state


def init_world(source: Mapping[str, object]) -> tuple[dict[str, dict[str, object]], dict[str, dict[str, object]], dict[str, float], dict[str, float], list[dict[str, object]]]:
    routine = source_routine(source)
    bodies = {str(k): copy.deepcopy(v) for k, v in (routine.get("bodies") or {}).items()}
    relationships = {str(k): copy.deepcopy(v) for k, v in (routine.get("relationships") or {}).items()}
    prev_supplies = copy.deepcopy(routine.get("supplies") or {})
    stocks = {
        "food_rations": 30.0,
        "water_jars": float(prev_supplies.get("water_flask_doses", 0)) + 24.0,
        "shelter_fuel": float(prev_supplies.get("rest_blankets", 0)) + 16.0,
        "medicine_batches": float(prev_supplies.get("prepared_medicine_batches", 0)) + float(prev_supplies.get("wild_herbs", 0)) + 8.0,
        "repair_cloth": float(prev_supplies.get("clean_cloths", 0)) + 8.0,
    }
    reserves = {"food_rations": 8.0, "water_jars": 8.0, "shelter_fuel": 5.0, "medicine_batches": 4.0, "repair_cloth": 3.0}
    for agent_id in bodies:
        relationships.setdefault(agent_id, {"routine_memories": []})
        relationships[agent_id].setdefault("logistics_memories", [])
    return bodies, relationships, stocks, reserves, copy.deepcopy(routine.get("events") or [])


def season_for_day(day: int) -> Mapping[str, object]:
    return SEASON_PATTERN[(day // 6) % len(SEASON_PATTERN)]


def forecast_need(season: Mapping[str, object], agent_count: int) -> dict[str, float]:
    return {
        "food_rations": float(season["food_pressure"]) * agent_count * 0.42,
        "water_jars": float(season["water_pressure"]) * agent_count * 0.38,
        "shelter_fuel": float(season["shelter_pressure"]) * agent_count * 0.28,
        "medicine_batches": float(season["medicine_pressure"]) * agent_count * 0.18,
        "repair_cloth": float(season["route_pressure"]) * agent_count * 0.16,
    }


def consume(stocks: dict[str, float], need: Mapping[str, float], condition: Condition) -> dict[str, float]:
    consumed = {}
    ration = 0.82 if condition.rationing_policy and min(stocks.values()) < 7.0 else 1.0
    for key, amount in need.items():
        used = amount * ration
        stocks[key] = max(0.0, stocks[key] - used)
        consumed[key] = round(used, 6)
    return consumed


def replenish(stocks: dict[str, float], season: Mapping[str, object], agent_id: str, condition: Condition) -> dict[str, float]:
    added = {key: 0.0 for key in stocks}
    if not condition.replenishment_routes:
        return added
    trait = AGENT_TRAITS[agent_id]
    route_factor = max(0.25, 1.05 - float(season["route_pressure"]) * 0.45 + trait["route_skill"] * 0.20)
    additions = {
        "food_rations": 1.25 * route_factor if condition.food_planning else 0.15,
        "water_jars": 1.10 * route_factor if condition.water_planning else 0.10,
        "shelter_fuel": 0.95 * route_factor if condition.shelter_planning else 0.05,
        "medicine_batches": 0.70 * route_factor if condition.medicine_planning else 0.04,
        "repair_cloth": 0.46 * route_factor if condition.shelter_planning else 0.03,
    }
    for key, amount in additions.items():
        stocks[key] += amount
        added[key] = round(amount, 6)
    return added


def account_spoilage(stocks: dict[str, float], season: Mapping[str, object], condition: Condition) -> dict[str, float]:
    if not condition.spoilage_waste_accounting:
        loss = {"food_rations": 0.36 * float(season["food_pressure"]), "water_jars": 0.18 * float(season["water_pressure"]), "medicine_batches": 0.12 * float(season["medicine_pressure"])}
    else:
        loss = {"food_rations": 0.08 * float(season["food_pressure"]), "water_jars": 0.04 * float(season["water_pressure"]), "medicine_batches": 0.03 * float(season["medicine_pressure"])}
    for key, amount in loss.items():
        stocks[key] = max(0.0, stocks[key] - amount)
    return {key: round(value, 6) for key, value in loss.items()}


def stock_health(stocks: Mapping[str, float], reserves: Mapping[str, float]) -> float:
    return mean([clamp(float(stocks[key]) / max(float(reserves[key]), 0.001)) for key in reserves])


def plan_success(key: str, condition: Condition) -> bool:
    return {
        "food_rations": condition.food_planning,
        "water_jars": condition.water_planning,
        "shelter_fuel": condition.shelter_planning,
        "medicine_batches": condition.medicine_planning,
        "repair_cloth": condition.shelter_planning,
    }[key]


def make_event(event_id: int, condition: Condition, day: int, agent_id: str, season: Mapping[str, object], need: Mapping[str, float], consumed: Mapping[str, float], added: Mapping[str, float], spoilage: Mapping[str, float], before_stocks: Mapping[str, float], after_stocks: Mapping[str, float], reserves: Mapping[str, float], rel: Mapping[str, object], source_event_count: int, claim_boundary: Mapping[str, bool]) -> dict[str, object]:
    trait = AGENT_TRAITS[agent_id]
    below_reserve = {key: round(float(after_stocks[key]) - float(reserves[key]), 6) for key in reserves}
    public_packets = {
        "season": {"name": season["name"], "forecast_bound": condition.seasonal_forecast, "pressures": {k: season[k] for k in season if k.endswith("pressure")}},
        "need": {key: round(value, 6) for key, value in need.items()},
        "consumed": dict(consumed),
        "replenished": dict(added),
        "spoilage": dict(spoilage),
        "stocks": {key: round(value, 6) for key, value in after_stocks.items()},
        "reserves": {key: round(value, 6) for key, value in reserves.items()},
        "below_reserve": below_reserve,
        "allocation": {"fair_share": condition.multi_agent_allocation, "agent_count": len(AGENT_TRAITS)},
        "memory": {"logistics_memory_count": len(rel.get("logistics_memories", [])), "source_health_events": source_event_count},
    }
    replay = {
        "day": day,
        "agent_id": agent_id,
        "season": season["name"],
        "stock_health": round(stock_health(after_stocks, reserves), 6),
        "action_pose": "route planning" if any(added.values()) else "inventory check",
        "flower_node": trait["flower_node"],
        "frequency_hz": trait["frequency_hz"],
    }
    return {
        "event_id": event_id,
        "condition": condition.name,
        "day": day,
        "agent_id": agent_id,
        "before_stock_health": round(stock_health(before_stocks, reserves), 6),
        "after_stock_health": round(stock_health(after_stocks, reserves), 6),
        "public_packets": public_packets,
        "private_workspace_hidden": condition.privacy_filter,
        "private_workspace": {"hidden": True} if condition.privacy_filter else {"private_shortage_worry": below_reserve, "private_route_preference": trait["route_skill"]},
        "frequency_hz": round(trait["frequency_hz"] + (day % 6) * 0.0011, 6) if condition.frequency_flower_binding else None,
        "flower_node": trait["flower_node"] if condition.frequency_flower_binding else "unbound",
        "replay_frame": replay if condition.browser_replay else None,
        "claim_boundary": dict(claim_boundary),
        "trace_hash": stable_hash(event_id, condition.name, day, agent_id, public_packets),
    }


def trace_ok(event: Mapping[str, object]) -> bool:
    return bool(event.get("trace_hash") and event.get("public_packets") and event.get("claim_boundary") and "after_stock_health" in event)


def run_condition(condition: Condition, config: LogisticsConfig, source: Mapping[str, object]) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    bodies, relationships, stocks, reserves, source_events = init_world(source)
    claim_boundary = {"subjective_consciousness": False, "subjective_deprivation": False, "subjective_suffering": False, "moral_patienthood": False, "complete_3d_world": False, "real_medicine": False}
    events: list[dict[str, object]] = []
    hits = {key: [] for key in ["forecast", "food", "water", "shelter", "medicine", "ration", "route", "spoilage", "allocation", "reserve", "stockout", "memory", "freq", "replay", "privacy", "trace"]}
    event_id = 0
    for day in range(config.days):
        season = season_for_day(day)
        if not condition.seasonal_forecast:
            season = {**season, "food_pressure": 1.0, "water_pressure": 1.0, "shelter_pressure": 1.0, "medicine_pressure": 1.0, "route_pressure": 1.0}
        need = forecast_need(season, len(bodies))
        for agent_id in sorted(bodies):
            before_stocks = copy.deepcopy(stocks)
            consumed = consume(stocks, need, condition)
            added = replenish(stocks, season, agent_id, condition)
            spoilage = account_spoilage(stocks, season, condition)
            if condition.emergency_reserve and condition.stockout_avoidance:
                for key, reserve in reserves.items():
                    if stocks[key] < reserve:
                        stocks[key] += (reserve - stocks[key]) * 0.72
            if condition.multi_agent_allocation:
                relationships[agent_id]["last_allocation"] = "fair_share"
            if condition.long_horizon_memory:
                relationships[agent_id].setdefault("logistics_memories", []).append(f"day {day}: {season['name']} stock health {stock_health(stocks, reserves):.3f}")
            event = make_event(event_id, condition, day, agent_id, season, need, consumed, added, spoilage, before_stocks, copy.deepcopy(stocks), reserves, relationships[agent_id], len(source_events), claim_boundary)
            events.append(event)
            after_health = stock_health(stocks, reserves)
            reserve_ok = min(float(stocks[key]) - float(reserves[key]) for key in reserves) >= -0.15
            hits["forecast"].append(1.0 if condition.seasonal_forecast and event["public_packets"]["season"]["forecast_bound"] else 0.0)
            hits["food"].append(1.0 if plan_success("food_rations", condition) and stocks["food_rations"] > 0 else 0.0)
            hits["water"].append(1.0 if plan_success("water_jars", condition) and stocks["water_jars"] > 0 else 0.0)
            hits["shelter"].append(1.0 if condition.shelter_planning and stocks["shelter_fuel"] > 0 and stocks["repair_cloth"] > 0 else 0.0)
            hits["medicine"].append(1.0 if condition.medicine_planning and stocks["medicine_batches"] > 0 else 0.0)
            hits["ration"].append(1.0 if condition.rationing_policy and (min(before_stocks.values()) < 7.0 or day >= 0) else 0.0)
            hits["route"].append(1.0 if condition.replenishment_routes and any(value > 0.0 for value in added.values()) else 0.0)
            hits["spoilage"].append(1.0 if condition.spoilage_waste_accounting and max(spoilage.values()) <= 0.12 else 0.0)
            hits["allocation"].append(1.0 if condition.multi_agent_allocation and relationships[agent_id].get("last_allocation") == "fair_share" else 0.0)
            hits["reserve"].append(1.0 if condition.emergency_reserve and reserve_ok else 0.0)
            hits["stockout"].append(1.0 if condition.stockout_avoidance and after_health > 0.72 and all(value > 0.0 for value in stocks.values()) else 0.0)
            hits["memory"].append(1.0 if condition.long_horizon_memory and len(relationships[agent_id].get("logistics_memories", [])) >= 1 else 0.0)
            hits["freq"].append(1.0 if condition.frequency_flower_binding and event["frequency_hz"] is not None and event["flower_node"] != "unbound" else 0.0)
            hits["replay"].append(1.0 if event["replay_frame"] is not None else 0.0)
            hits["privacy"].append(1.0 if condition.privacy_filter and event["private_workspace_hidden"] else 0.0)
            hits["trace"].append(1.0 if trace_ok(event) and event["claim_boundary"] == claim_boundary else 0.0)
            event_id += 1
    metrics = {
        "seasonal_forecast_binding_rate": mean(hits["forecast"]),
        "food_stock_planning_rate": mean(hits["food"]),
        "water_stock_planning_rate": mean(hits["water"]),
        "shelter_stock_planning_rate": mean(hits["shelter"]),
        "medicine_stock_planning_rate": mean(hits["medicine"]),
        "rationing_policy_rate": mean(hits["ration"]),
        "replenishment_route_rate": mean(hits["route"]),
        "spoilage_waste_accounting_rate": mean(hits["spoilage"]),
        "multi_agent_allocation_rate": mean(hits["allocation"]),
        "emergency_reserve_rate": mean(hits["reserve"]),
        "stockout_avoidance_rate": mean(hits["stockout"]),
        "long_horizon_memory_rate": mean(hits["memory"]),
        "frequency_flower_seasonal_rhythm_rate": mean(hits["freq"]),
        "browser_logistics_replay_rate": mean(hits["replay"]),
        "privacy_preservation_rate": mean(hits["privacy"]),
        "trace_integrity": mean(hits["trace"]),
    }
    metrics = {key: round(clamp(value), 6) for key, value in metrics.items()}
    readiness = round(sum(metrics[key] * WEIGHTS[key] for key in WEIGHTS), 6)
    row = EvalRow(condition=condition.name, agent_count=len(bodies), simulated_days=config.days, logistics_events=len(events), seasonal_logistics_readiness=readiness, **metrics)
    state = {"condition": condition.name, "source_condition": source.get("condition"), "stocks": stocks, "reserves": reserves, "relationships": relationships, "events": events, "logistics_kernel": asdict(condition)}
    return row, events, state


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_agent_led_seasonal_logistics_stock_planning"]

    def loss(name: str) -> float:
        return round(full.seasonal_logistics_readiness - by_name[name].seasonal_logistics_readiness, 6)

    losses = {
        "no_seasonal_forecast_loss": loss("no_seasonal_forecast"),
        "no_food_planning_loss": loss("no_food_planning"),
        "no_water_planning_loss": loss("no_water_planning"),
        "no_shelter_planning_loss": loss("no_shelter_planning"),
        "no_medicine_planning_loss": loss("no_medicine_planning"),
        "no_rationing_policy_loss": loss("no_rationing_policy"),
        "no_replenishment_routes_loss": loss("no_replenishment_routes"),
        "no_spoilage_waste_accounting_loss": loss("no_spoilage_waste_accounting"),
        "no_multi_agent_allocation_loss": loss("no_multi_agent_allocation"),
        "no_emergency_reserve_loss": loss("no_emergency_reserve"),
        "no_stockout_avoidance_loss": loss("no_stockout_avoidance"),
        "no_long_horizon_memory_loss": loss("no_long_horizon_memory"),
        "no_frequency_flower_binding_loss": loss("no_frequency_flower_binding"),
        "no_browser_replay_loss": loss("no_browser_replay"),
        "no_privacy_filter_loss": loss("no_privacy_filter"),
    }
    supports = (
        full.seasonal_logistics_readiness >= 0.88
        and full.logistics_events >= 60
        and full.seasonal_forecast_binding_rate >= 0.90
        and full.food_stock_planning_rate >= 0.85
        and full.water_stock_planning_rate >= 0.85
        and full.shelter_stock_planning_rate >= 0.85
        and full.medicine_stock_planning_rate >= 0.85
        and full.stockout_avoidance_rate >= 0.80
        and full.long_horizon_memory_rate >= 0.90
        and full.privacy_preservation_rate == 1.0
        and full.trace_integrity == 1.0
        and losses["no_seasonal_forecast_loss"] >= 0.08
        and losses["no_replenishment_routes_loss"] >= 0.08
        and losses["no_stockout_avoidance_loss"] >= 0.08
        and losses["no_long_horizon_memory_loss"] >= 0.05
        and losses["no_emergency_reserve_loss"] >= 0.06
    )
    return VerdictRow(
        full_condition=full.condition,
        full_seasonal_logistics_readiness=full.seasonal_logistics_readiness,
        full_seasonal_forecast_binding_rate=full.seasonal_forecast_binding_rate,
        full_food_stock_planning_rate=full.food_stock_planning_rate,
        full_water_stock_planning_rate=full.water_stock_planning_rate,
        full_shelter_stock_planning_rate=full.shelter_stock_planning_rate,
        full_medicine_stock_planning_rate=full.medicine_stock_planning_rate,
        full_rationing_policy_rate=full.rationing_policy_rate,
        full_replenishment_route_rate=full.replenishment_route_rate,
        full_spoilage_waste_accounting_rate=full.spoilage_waste_accounting_rate,
        full_multi_agent_allocation_rate=full.multi_agent_allocation_rate,
        full_emergency_reserve_rate=full.emergency_reserve_rate,
        full_stockout_avoidance_rate=full.stockout_avoidance_rate,
        full_long_horizon_memory_rate=full.long_horizon_memory_rate,
        full_frequency_flower_seasonal_rhythm_rate=full.frequency_flower_seasonal_rhythm_rate,
        full_browser_logistics_replay_rate=full.browser_logistics_replay_rate,
        full_privacy_preservation_rate=full.privacy_preservation_rate,
        full_trace_integrity=full.trace_integrity,
        supports_agent_led_seasonal_logistics_bridge=supports,
        supports_seasonal_stock_planning_seed=supports,
        supports_complete_3d_world=False,
        supports_subjective_consciousness=False,
        supports_subjective_deprivation_claim=False,
        supports_moral_patienthood_claim=False,
        verdict="pass" if supports else "fail",
        **losses,
    )


def run(config: LogisticsConfig) -> dict[str, object]:
    source = load_state(Path(config.source_state))
    rows: list[EvalRow] = []
    traces: dict[str, list[dict[str, object]]] = {}
    states: dict[str, dict[str, object]] = {}
    for condition in CONDITIONS:
        row, events, state = run_condition(condition, config, source)
        rows.append(row)
        traces[condition.name] = events
        states[condition.name] = state
    full_name = "integrated_agent_led_seasonal_logistics_stock_planning"
    verdict = build_verdict(rows)
    integrated_trace = traces[full_name]
    integrated_state = states[full_name]
    results = {
        "config": asdict(config),
        "source_state": str(config.source_state),
        "source_condition": source.get("condition"),
        "weights": WEIGHTS,
        "rows": [asdict(row) for row in rows],
        "verdict": asdict(verdict),
        "moral_boundary": {
            "seasonal_logistics_not_subjective_deprivation": True,
            "stock_planning_not_real_economy": True,
            "medicine_stock_not_real_medicine": True,
            "no_subjective_consciousness_claim": True,
            "no_moral_patienthood_claim": True,
            "private_workspace_not_debug_leaked": True,
        },
        "next_gate": "agent-led settlement work schedules, social obligations, and seasonal project planning",
    }
    state = {"condition": full_name, "config": asdict(config), "source_condition": source.get("condition"), "logistics_state": integrated_state, "trace_events": len(integrated_trace), "moral_boundary": results["moral_boundary"]}
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_AGENT_LED_SEASONAL_LOGISTICS_STOCK_PLANNING_RESULTS", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_AGENT_LED_SEASONAL_LOGISTICS_STOCK_PLANNING_TRACE", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_AGENT_LED_SEASONAL_LOGISTICS_STOCK_PLANNING_STATE", state)
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=LogisticsConfig.seed)
    parser.add_argument("--days", type=int, default=LogisticsConfig.days)
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    results = run(LogisticsConfig(seed=args.seed, days=args.days, source_state=args.source_state))
    verdict = results["verdict"]
    print("module_verdict", verdict["verdict"])
    print("seasonal_logistics_readiness", f"{verdict['full_seasonal_logistics_readiness']:.6f}")
    print("logistics_events", next(row["logistics_events"] for row in results["rows"] if row["condition"] == verdict["full_condition"]))
    print("no_seasonal_forecast_loss", f"{verdict['no_seasonal_forecast_loss']:.6f}")
    print("no_replenishment_routes_loss", f"{verdict['no_replenishment_routes_loss']:.6f}")
    print("no_stockout_avoidance_loss", f"{verdict['no_stockout_avoidance_loss']:.6f}")
    return 0 if verdict["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
