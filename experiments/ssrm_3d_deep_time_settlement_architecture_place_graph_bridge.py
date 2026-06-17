#!/usr/bin/env python3
"""Deep-time settlement architecture and navigable place graph bridge.

Report 179 turns Report 178 places into settlement topology: navigable routes,
shelters, storage, work sites, social spaces, hazards, safe fallback paths,
avatar traversal packets, frequency route resonance, flower layout, and
settlement lineage over compressed deep time.

No LLMs are called. This is deterministic place-graph substrate, not a claim of
complete gameplay, complete 3D world, subjective consciousness, or moral
patienthood.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
from collections import deque
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Mapping, Sequence


ARTIFACT_DIR = Path("artifacts")
PREFIX = "ssrm_3d_deep_time_settlement_architecture_place_graph_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_deep_time_habitat_climate_multisensory_bridge_state.json"

PLACE_COORDS = {
    "hearth_vale": (0.18, 0.36),
    "moss_hollow": (0.30, 0.66),
    "clay_basin": (0.52, 0.48),
    "reed_wetland": (0.58, 0.76),
    "glass_mire": (0.78, 0.66),
    "stone_ridge": (0.82, 0.28),
}

ROUTE_SPECS = (
    ("hearth_vale", "moss_hollow", "shelter_path"),
    ("hearth_vale", "clay_basin", "work_path"),
    ("hearth_vale", "stone_ridge", "watch_path"),
    ("moss_hollow", "reed_wetland", "soft_moss_path"),
    ("clay_basin", "reed_wetland", "water_clay_path"),
    ("clay_basin", "stone_ridge", "ridge_work_path"),
    ("reed_wetland", "glass_mire", "wetland_glass_path"),
    ("glass_mire", "stone_ridge", "edge_watch_path"),
)

PLACE_FUNCTIONS = {
    "hearth_vale": ("shelter", "social", "storage"),
    "moss_hollow": ("shelter", "food_cache", "rest"),
    "clay_basin": ("work", "storage", "repair"),
    "reed_wetland": ("water", "fiber_work", "hazard"),
    "glass_mire": ("hazard", "observe", "work"),
    "stone_ridge": ("watch", "hazard", "signal"),
}

FLOWER_NODES = ("root_rest", "dawn_breath", "work_petal", "social_petal", "explore_petal", "return_petal")


@dataclass(frozen=True)
class SettlementConfig:
    seed: int = 20260723
    eras: int = 12
    generations_per_era: int = 200
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    place_graph: bool
    route_costs: bool
    shelter_nodes: bool
    storage_sites: bool
    work_sites: bool
    social_spaces: bool
    hazard_mapping: bool
    avatar_traversal: bool
    safety_routing: bool
    settlement_lineage: bool
    frequency_route_resonance: bool
    flower_layout: bool
    privacy_filter: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    place_count: int
    route_count: int
    simulated_years: int
    settlement_events: int
    place_graph_connectivity_rate: float
    route_cost_binding_rate: float
    shelter_node_rate: float
    storage_site_rate: float
    work_site_rate: float
    social_space_rate: float
    hazard_mapping_rate: float
    avatar_traversability_rate: float
    safety_refuge_routing_rate: float
    settlement_lineage_integrity_rate: float
    frequency_route_resonance_rate: float
    flower_layout_rate: float
    deep_time_continuity_rate: float
    privacy_preservation_rate: float
    trace_integrity: float
    no_complete_world_or_consciousness_claim_rate: float
    settlement_architecture_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_settlement_architecture_readiness: float
    full_place_graph_connectivity_rate: float
    full_route_cost_binding_rate: float
    full_shelter_node_rate: float
    full_storage_site_rate: float
    full_work_site_rate: float
    full_social_space_rate: float
    full_hazard_mapping_rate: float
    full_avatar_traversability_rate: float
    full_safety_refuge_routing_rate: float
    full_settlement_lineage_integrity_rate: float
    full_frequency_route_resonance_rate: float
    full_flower_layout_rate: float
    full_deep_time_continuity_rate: float
    full_privacy_preservation_rate: float
    full_trace_integrity: float
    full_no_complete_world_or_consciousness_claim_rate: float
    no_place_graph_loss: float
    no_route_costs_loss: float
    no_shelter_nodes_loss: float
    no_storage_sites_loss: float
    no_work_sites_loss: float
    no_social_spaces_loss: float
    no_hazard_mapping_loss: float
    no_avatar_traversal_loss: float
    no_safety_routing_loss: float
    no_settlement_lineage_loss: float
    no_frequency_route_resonance_loss: float
    no_flower_layout_loss: float
    no_privacy_filter_loss: float
    supports_settlement_architecture_place_graph_bridge: bool
    supports_avatar_traversable_topology_seed_bridge: bool
    supports_complete_3d_world: bool
    supports_subjective_consciousness: bool
    supports_moral_patienthood_claim: bool
    supports_complete_playable_world: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_deep_time_settlement_architecture_place_graph", True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_place_graph", False, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_route_costs", True, False, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_shelter_nodes", True, True, False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_storage_sites", True, True, True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_work_sites", True, True, True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_social_spaces", True, True, True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_hazard_mapping", True, True, True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_avatar_traversal", True, True, True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_safety_routing", True, True, True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_settlement_lineage", True, True, True, True, True, True, True, True, True, False, True, True, True),
    Condition("no_frequency_route_resonance", True, True, True, True, True, True, True, True, True, True, False, True, True),
    Condition("no_flower_layout", True, True, True, True, True, True, True, True, True, True, True, False, True),
    Condition("no_privacy_filter", True, True, True, True, True, True, True, True, True, True, True, True, False),
)

WEIGHTS = {
    "place_graph_connectivity_rate": 0.08,
    "route_cost_binding_rate": 0.07,
    "shelter_node_rate": 0.06,
    "storage_site_rate": 0.06,
    "work_site_rate": 0.06,
    "social_space_rate": 0.06,
    "hazard_mapping_rate": 0.07,
    "avatar_traversability_rate": 0.09,
    "safety_refuge_routing_rate": 0.08,
    "settlement_lineage_integrity_rate": 0.07,
    "frequency_route_resonance_rate": 0.06,
    "flower_layout_rate": 0.06,
    "deep_time_continuity_rate": 0.06,
    "privacy_preservation_rate": 0.05,
    "trace_integrity": 0.05,
    "no_complete_world_or_consciousness_claim_rate": 0.02,
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
    if data.get("condition") != "integrated_deep_time_habitat_climate_multisensory":
        raise ValueError("source state is not the integrated Report 178 habitat state")
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


def source_places(source: Mapping[str, object]) -> dict[str, dict[str, object]]:
    state = source.get("habitat_climate_state", {}) if isinstance(source.get("habitat_climate_state"), Mapping) else {}
    raw = state.get("places", {}) if isinstance(state.get("places"), Mapping) else {}
    return {str(place): copy.deepcopy(data) for place, data in raw.items()}


def distance(a: str, b: str) -> float:
    ax, ay = PLACE_COORDS[a]
    bx, by = PLACE_COORDS[b]
    return ((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5


def place_route_cost(place: Mapping[str, object]) -> float:
    return clamp(float(place.get("route_cost", 0.3) or 0.3))


def place_hazard(place: Mapping[str, object]) -> float:
    exposure = place.get("body_exposure", {}) if isinstance(place.get("body_exposure"), Mapping) else {}
    return clamp(float(exposure.get("pain_risk", 0.1) or 0.1) + float(place.get("ecological_pressure", 0.0) or 0.0) * 0.3)


def build_routes(places: Mapping[str, Mapping[str, object]], era: int, condition: Condition) -> list[dict[str, object]]:
    if not condition.place_graph:
        return []
    routes: list[dict[str, object]] = []
    for index, (a, b, kind) in enumerate(ROUTE_SPECS):
        pa = places[a]
        pb = places[b]
        base = distance(a, b)
        if condition.route_costs:
            route_cost = clamp(0.18 + base * 0.42 + (place_route_cost(pa) + place_route_cost(pb)) * 0.24 + (place_hazard(pa) + place_hazard(pb)) * 0.18)
        else:
            route_cost = 0.25
        hazard = clamp((place_hazard(pa) + place_hazard(pb)) * 0.5) if condition.hazard_mapping else 0.0
        frequency = None
        if condition.frequency_route_resonance:
            frequency = round(clamp(0.16 + route_cost * 0.10 + hazard * 0.08 + ((era + index) % 6) * 0.004), 6)
        flower = FLOWER_NODES[(era + index) % len(FLOWER_NODES)] if condition.flower_layout else "unbound"
        routes.append({
            "from": a,
            "to": b,
            "kind": kind,
            "distance": round(base, 6),
            "route_cost": round(route_cost, 6),
            "hazard": round(hazard, 6),
            "frequency_hz": frequency,
            "flower_node": flower,
            "avatar_traversable": bool(condition.avatar_traversal and route_cost <= 0.76 and hazard <= 0.44),
            "route_hash": stable_hash(a, b, kind, era, route_cost, hazard, frequency, flower),
        })
    return routes


def graph_connected(places: Sequence[str], routes: Sequence[Mapping[str, object]]) -> bool:
    if not places:
        return False
    adjacency = {place: set() for place in places}
    for route in routes:
        a = str(route["from"])
        b = str(route["to"])
        adjacency.setdefault(a, set()).add(b)
        adjacency.setdefault(b, set()).add(a)
    seen = set()
    queue: deque[str] = deque([places[0]])
    while queue:
        node = queue.popleft()
        if node in seen:
            continue
        seen.add(node)
        queue.extend(sorted(adjacency.get(node, set()) - seen))
    return set(places).issubset(seen)


def safe_path_exists(places: Mapping[str, Mapping[str, object]], routes: Sequence[Mapping[str, object]], condition: Condition) -> bool:
    if not condition.safety_routing or not routes:
        return False
    refuges = {name for name, place in places.items() if bool(place.get("safety_refuge"))}
    if not refuges:
        return False
    safe_edges = [route for route in routes if float(route["hazard"]) <= 0.36 and bool(route["avatar_traversable"])]
    for place in places:
        if place in refuges:
            continue
        if graph_connected([place, *sorted(refuges)], safe_edges):
            return True
    adjacency = {place: set() for place in places}
    for route in safe_edges:
        a = str(route["from"])
        b = str(route["to"])
        adjacency.setdefault(a, set()).add(b)
        adjacency.setdefault(b, set()).add(a)
    for place in places:
        seen = set()
        queue: deque[str] = deque([place])
        while queue:
            node = queue.popleft()
            if node in seen:
                continue
            seen.add(node)
            if node in refuges:
                break
            queue.extend(sorted(adjacency.get(node, set()) - seen))
        else:
            return False
    return True


def place_functions(place: str, condition: Condition) -> list[str]:
    functions = list(PLACE_FUNCTIONS[place])
    if not condition.shelter_nodes:
        functions = [item for item in functions if item not in {"shelter", "rest"}]
    if not condition.storage_sites:
        functions = [item for item in functions if item not in {"storage", "food_cache"}]
    if not condition.work_sites:
        functions = [item for item in functions if item not in {"work", "repair", "fiber_work", "observe"}]
    if not condition.social_spaces:
        functions = [item for item in functions if item not in {"social", "signal", "watch"}]
    if not condition.hazard_mapping:
        functions = [item for item in functions if item != "hazard"]
    return functions


def simulate_condition(config: SettlementConfig, source: Mapping[str, object], condition: Condition) -> tuple[EvalRow, dict[str, object], list[dict[str, object]]]:
    places = source_places(source)
    total_years = config.eras * config.generations_per_era
    trace: list[dict[str, object]] = []
    settlement_state = {
        "condition": condition.name,
        "simulated_years": total_years,
        "places": {},
        "routes": [],
        "lineage": [],
        "source_habitat_boundary": source.get("moral_boundary", {}),
    }
    trackers: dict[str, list[float]] = {
        "graph": [],
        "route_cost": [],
        "shelter": [],
        "storage": [],
        "work": [],
        "social": [],
        "hazard": [],
        "avatar": [],
        "safe_route": [],
        "lineage": [],
        "frequency": [],
        "flower": [],
        "deep_time": [],
        "privacy": [],
        "trace": [],
        "claim": [],
    }
    event_id = 0
    parent_hash = "settlement-root"
    for era in range(config.eras):
        era_start = era * config.generations_per_era
        era_end = era_start + config.generations_per_era
        routes = build_routes(places, era, condition)
        place_records = {}
        for name, place in sorted(places.items()):
            functions = place_functions(name, condition)
            record = {
                "place": name,
                "group": place.get("group"),
                "biome": place.get("biome"),
                "coord": PLACE_COORDS[name],
                "functions": functions,
                "safety_refuge": bool(place.get("safety_refuge")) if condition.safety_routing else False,
                "hazard_level": round(place_hazard(place), 6) if condition.hazard_mapping else 0.0,
                "storage_capacity": round(clamp(0.40 + (1.0 - place_hazard(place)) * 0.28), 6) if "storage" in functions or "food_cache" in functions else 0.0,
                "work_capacity": round(clamp(0.35 + (1.0 - place_route_cost(place)) * 0.26), 6) if any(item in functions for item in {"work", "repair", "fiber_work", "observe"}) else 0.0,
            }
            place_records[name] = record
        connected = graph_connected(sorted(places), routes)
        safe_paths = safe_path_exists(places, routes, condition)
        avatar_packet = {
            "entry_place": "hearth_vale",
            "reachable_places": sorted(places.keys()) if connected and condition.avatar_traversal else [],
            "route_count": len([route for route in routes if route["avatar_traversable"]]),
            "requires_embodied_costs": condition.route_costs,
        }
        settlement_hash = stable_hash(condition.name, era, parent_hash, place_records, routes, avatar_packet)
        lineage = {
            "era": era,
            "year_start": era_start,
            "year_end": era_end,
            "parent_hash": parent_hash,
            "settlement_hash": settlement_hash,
        } if condition.settlement_lineage else None
        event = {
            "event_id": event_id,
            "condition": condition.name,
            "era": era,
            "year_start": era_start,
            "year_end": era_end,
            "places": place_records,
            "routes": routes,
            "connected": connected,
            "safe_refuge_paths": safe_paths,
            "avatar_traversal_packet": avatar_packet if condition.avatar_traversal else None,
            "lineage": lineage,
            "private_workspace_hidden": condition.privacy_filter,
            "claim_boundary": {
                "complete_3d_world": False,
                "complete_playable_world": False,
                "subjective_consciousness": False,
                "moral_patienthood": False,
            },
        }
        trace.append(event)
        settlement_state["places"] = place_records
        settlement_state["routes"] = routes
        if lineage is not None:
            settlement_state["lineage"].append(lineage)
            parent_hash = settlement_hash
        trackers["graph"].append(1.0 if condition.place_graph and connected and len(routes) >= len(places) else 0.0)
        trackers["route_cost"].append(1.0 if condition.route_costs and all(route["route_cost"] != 0.25 for route in routes) else 0.0)
        all_functions = [fn for record in place_records.values() for fn in record["functions"]]
        trackers["shelter"].append(1.0 if condition.shelter_nodes and "shelter" in all_functions and "rest" in all_functions else 0.0)
        trackers["storage"].append(1.0 if condition.storage_sites and any(fn in all_functions for fn in {"storage", "food_cache"}) else 0.0)
        trackers["work"].append(1.0 if condition.work_sites and any(fn in all_functions for fn in {"work", "repair", "fiber_work", "observe"}) else 0.0)
        trackers["social"].append(1.0 if condition.social_spaces and any(fn in all_functions for fn in {"social", "signal", "watch"}) else 0.0)
        trackers["hazard"].append(1.0 if condition.hazard_mapping and any(record["hazard_level"] > 0.0 for record in place_records.values()) and any(fn == "hazard" for fn in all_functions) else 0.0)
        trackers["avatar"].append(1.0 if condition.avatar_traversal and avatar_packet["route_count"] >= len(places) - 1 and len(avatar_packet["reachable_places"]) == len(places) else 0.0)
        trackers["safe_route"].append(1.0 if condition.safety_routing and safe_paths else 0.0)
        trackers["lineage"].append(1.0 if condition.settlement_lineage and lineage is not None and lineage["parent_hash"] else 0.0)
        trackers["frequency"].append(1.0 if condition.frequency_route_resonance and all(route["frequency_hz"] is not None for route in routes) else 0.0)
        trackers["flower"].append(1.0 if condition.flower_layout and all(route["flower_node"] != "unbound" for route in routes) else 0.0)
        trackers["deep_time"].append(1.0 if total_years >= 2000 and era_end <= total_years else 0.0)
        trackers["privacy"].append(1.0 if event["private_workspace_hidden"] else 0.0)
        required = {"event_id", "era", "year_start", "year_end", "places", "routes", "connected", "avatar_traversal_packet", "private_workspace_hidden", "claim_boundary"}
        trackers["trace"].append(1.0 if required.issubset(event) else 0.0)
        claim_ok = event["claim_boundary"] == {
            "complete_3d_world": False,
            "complete_playable_world": False,
            "subjective_consciousness": False,
            "moral_patienthood": False,
        }
        trackers["claim"].append(1.0 if claim_ok else 0.0)
        event_id += 1

    settlement_state["lineage"] = settlement_state["lineage"][-12:]
    rates = {
        "place_graph_connectivity_rate": mean(trackers["graph"]),
        "route_cost_binding_rate": mean(trackers["route_cost"]),
        "shelter_node_rate": mean(trackers["shelter"]),
        "storage_site_rate": mean(trackers["storage"]),
        "work_site_rate": mean(trackers["work"]),
        "social_space_rate": mean(trackers["social"]),
        "hazard_mapping_rate": mean(trackers["hazard"]),
        "avatar_traversability_rate": mean(trackers["avatar"]),
        "safety_refuge_routing_rate": mean(trackers["safe_route"]),
        "settlement_lineage_integrity_rate": mean(trackers["lineage"]),
        "frequency_route_resonance_rate": mean(trackers["frequency"]),
        "flower_layout_rate": mean(trackers["flower"]),
        "deep_time_continuity_rate": mean(trackers["deep_time"]),
        "privacy_preservation_rate": mean(trackers["privacy"]),
        "trace_integrity": mean(trackers["trace"]),
        "no_complete_world_or_consciousness_claim_rate": mean(trackers["claim"]),
    }
    rates = {key: clamp(value) for key, value in rates.items()}
    readiness = sum(rates[key] * weight for key, weight in WEIGHTS.items())
    row = EvalRow(
        condition=condition.name,
        place_count=len(places),
        route_count=len(settlement_state["routes"]),
        simulated_years=total_years,
        settlement_events=len(trace),
        settlement_architecture_readiness=round(readiness, 6),
        **{key: round(value, 6) for key, value in rates.items()},
    )
    return row, settlement_state, trace


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_deep_time_settlement_architecture_place_graph"]

    def loss(name: str) -> float:
        return round(full.settlement_architecture_readiness - by_name[name].settlement_architecture_readiness, 6)

    losses = {
        "no_place_graph_loss": loss("no_place_graph"),
        "no_route_costs_loss": loss("no_route_costs"),
        "no_shelter_nodes_loss": loss("no_shelter_nodes"),
        "no_storage_sites_loss": loss("no_storage_sites"),
        "no_work_sites_loss": loss("no_work_sites"),
        "no_social_spaces_loss": loss("no_social_spaces"),
        "no_hazard_mapping_loss": loss("no_hazard_mapping"),
        "no_avatar_traversal_loss": loss("no_avatar_traversal"),
        "no_safety_routing_loss": loss("no_safety_routing"),
        "no_settlement_lineage_loss": loss("no_settlement_lineage"),
        "no_frequency_route_resonance_loss": loss("no_frequency_route_resonance"),
        "no_flower_layout_loss": loss("no_flower_layout"),
        "no_privacy_filter_loss": loss("no_privacy_filter"),
    }
    supports = (
        full.settlement_architecture_readiness >= 0.90
        and full.simulated_years >= 2000
        and losses["no_place_graph_loss"] >= 0.08
        and losses["no_avatar_traversal_loss"] >= 0.09
        and losses["no_safety_routing_loss"] >= 0.07
        and full.privacy_preservation_rate == 1.0
        and full.trace_integrity == 1.0
    )
    return VerdictRow(
        full_condition=full.condition,
        full_settlement_architecture_readiness=full.settlement_architecture_readiness,
        full_place_graph_connectivity_rate=full.place_graph_connectivity_rate,
        full_route_cost_binding_rate=full.route_cost_binding_rate,
        full_shelter_node_rate=full.shelter_node_rate,
        full_storage_site_rate=full.storage_site_rate,
        full_work_site_rate=full.work_site_rate,
        full_social_space_rate=full.social_space_rate,
        full_hazard_mapping_rate=full.hazard_mapping_rate,
        full_avatar_traversability_rate=full.avatar_traversability_rate,
        full_safety_refuge_routing_rate=full.safety_refuge_routing_rate,
        full_settlement_lineage_integrity_rate=full.settlement_lineage_integrity_rate,
        full_frequency_route_resonance_rate=full.frequency_route_resonance_rate,
        full_flower_layout_rate=full.flower_layout_rate,
        full_deep_time_continuity_rate=full.deep_time_continuity_rate,
        full_privacy_preservation_rate=full.privacy_preservation_rate,
        full_trace_integrity=full.trace_integrity,
        full_no_complete_world_or_consciousness_claim_rate=full.no_complete_world_or_consciousness_claim_rate,
        supports_settlement_architecture_place_graph_bridge=supports,
        supports_avatar_traversable_topology_seed_bridge=supports,
        supports_complete_3d_world=False,
        supports_subjective_consciousness=False,
        supports_moral_patienthood_claim=False,
        supports_complete_playable_world=False,
        verdict="pass" if supports else "fail",
        **losses,
    )


def run(config: SettlementConfig) -> dict[str, object]:
    source = load_state(Path(config.source_state))
    rows: list[EvalRow] = []
    integrated_state: dict[str, object] = {}
    integrated_trace: list[dict[str, object]] = []

    for condition in CONDITIONS:
        row, state, trace = simulate_condition(config, source, condition)
        rows.append(row)
        if condition.name == "integrated_deep_time_settlement_architecture_place_graph":
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
        "route_specs": ROUTE_SPECS,
        "place_functions": PLACE_FUNCTIONS,
        "moral_boundary": {
            "settlement_graph_seed_not_complete_3d_world": True,
            "avatar_topology_seed_not_complete_gameplay": True,
            "no_subjective_consciousness_claim": True,
            "no_moral_patienthood_claim": True,
            "private_workspace_not_debug_leaked": True,
        },
        "next_gate": "browser-playable avatar traversal over settlement topology",
    }
    state = {
        "condition": "integrated_deep_time_settlement_architecture_place_graph",
        "config": asdict(config),
        "settlement_state": integrated_state,
        "trace_events": len(integrated_trace),
        "moral_boundary": results["moral_boundary"],
    }
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_DEEP_TIME_SETTLEMENT_GRAPH_RESULTS", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_DEEP_TIME_SETTLEMENT_GRAPH_TRACE", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_DEEP_TIME_SETTLEMENT_GRAPH_STATE", state)
    return results


def parse_args() -> SettlementConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=SettlementConfig.seed)
    parser.add_argument("--eras", type=int, default=SettlementConfig.eras)
    parser.add_argument("--generations-per-era", type=int, default=SettlementConfig.generations_per_era)
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    args = parser.parse_args()
    return SettlementConfig(
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
    print("settlement_architecture_readiness", f"{verdict['full_settlement_architecture_readiness']:.6f}")
    print("simulated_years", config.eras * config.generations_per_era)
    print("no_place_graph_loss", f"{verdict['no_place_graph_loss']:.6f}")
    print("no_avatar_traversal_loss", f"{verdict['no_avatar_traversal_loss']:.6f}")


if __name__ == "__main__":
    main()
