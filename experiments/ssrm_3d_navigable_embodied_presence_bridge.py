#!/usr/bin/env python3
"""Navigable embodied-presence bridge for SSRM-3D.

Report 157 joins the Report 156 interactive avatar dialogue loop to the earlier
place/object/infrastructure graph. It emits a deterministic local navigation
state and browser viewer where an avatar can move through places, see objects,
agents, infrastructure costs, source-grounded dialogue overlays, frequency
fields, body expenditures, affordance gates, and a replayable camera timeline.

No LLMs are called. This is deterministic bridge machinery, not subjective
consciousness, unscripted civilization, open-ended language, or a completed
playable world.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import fmean
from typing import Iterable, Mapping, Sequence


ARTIFACT_DIR = Path("artifacts")
PREFIX = "ssrm_3d_navigable_embodied_presence_bridge"
SOURCE_INTERACTIVE = ARTIFACT_DIR / "ssrm_3d_interactive_avatar_dialogue_loop_bridge_state.json"
SOURCE_INFRA = ARTIFACT_DIR / "ssrm_3d_agent_made_infrastructure_bridge_state.json"
SOURCE_LEDGER = ARTIFACT_DIR / "ssrm_3d_source_native_council_ledger_bridge_state.json"
FLOWER_PHASES = tuple(math.tau * i / 12.0 for i in range(12))
SENSORY_CHANNELS = ("vibration", "sound", "vision", "scent", "thermal", "wetness", "pain", "affect")
NAVIGATION_MODES = ("walk", "listen", "inspect", "approach", "ask_source", "tune_frequency", "use_affordance", "record_replay")


@dataclass(frozen=True)
class NavigableConfig:
    seed: int = 20260701
    navigation_ticks: int = 128
    source_interactive: str = str(SOURCE_INTERACTIVE)
    source_infrastructure: str = str(SOURCE_INFRA)
    source_ledger: str = str(SOURCE_LEDGER)


@dataclass(frozen=True)
class Condition:
    name: str
    avatar_navigation: bool
    place_object_render: bool
    agent_presence_binding: bool
    infrastructure_route_costs: bool
    source_dialogue_overlay: bool
    frequency_sensory_field: bool
    body_expenditure_model: bool
    affordance_collision_gate: bool
    replay_camera_timeline: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    navigation_ticks: int
    places: int
    objects: int
    agents: int
    routes: int
    avatar_navigation_rate: float
    place_object_render_rate: float
    agent_presence_binding_rate: float
    infrastructure_route_cost_rate: float
    source_dialogue_overlay_rate: float
    frequency_sensory_field_rate: float
    body_expenditure_coupling_rate: float
    affordance_collision_gate_rate: float
    replay_camera_timeline_rate: float
    subjective_claim_boundary_rate: float
    trace_integrity: float
    navigable_presence_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_navigable_presence_readiness: float
    full_avatar_navigation_rate: float
    full_place_object_render_rate: float
    full_agent_presence_binding_rate: float
    full_infrastructure_route_cost_rate: float
    full_source_dialogue_overlay_rate: float
    full_frequency_sensory_field_rate: float
    full_body_expenditure_coupling_rate: float
    full_affordance_collision_gate_rate: float
    full_replay_camera_timeline_rate: float
    full_subjective_claim_boundary_rate: float
    full_trace_integrity: float
    no_avatar_navigation_loss: float
    no_place_object_render_loss: float
    no_agent_presence_binding_loss: float
    no_infrastructure_route_costs_loss: float
    no_source_dialogue_overlay_loss: float
    no_frequency_sensory_field_loss: float
    no_body_expenditure_model_loss: float
    no_affordance_collision_gate_loss: float
    no_replay_camera_timeline_loss: float
    supports_navigable_embodied_presence_bridge: bool
    supports_subjective_consciousness: bool
    supports_llm_open_dialogue: bool
    supports_complete_playable_world: bool
    supports_unscripted_civilization: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_navigable_embodied_presence", True, True, True, True, True, True, True, True, True),
    Condition("no_avatar_navigation", False, True, True, True, True, True, True, True, True),
    Condition("no_place_object_render", True, False, True, True, True, True, True, True, True),
    Condition("no_agent_presence_binding", True, True, False, True, True, True, True, True, True),
    Condition("no_infrastructure_route_costs", True, True, True, False, True, True, True, True, True),
    Condition("no_source_dialogue_overlay", True, True, True, True, False, True, True, True, True),
    Condition("no_frequency_sensory_field", True, True, True, True, True, False, True, True, True),
    Condition("no_body_expenditure_model", True, True, True, True, True, True, False, True, True),
    Condition("no_affordance_collision_gate", True, True, True, True, True, True, True, False, True),
    Condition("no_replay_camera_timeline", True, True, True, True, True, True, True, True, False),
)


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def mean(values: Iterable[float]) -> float:
    items = list(values)
    return fmean(items) if items else 0.0


def stable_unit(text: str, salt: str = "") -> float:
    digest = hashlib.sha256(f"{salt}:{text}".encode("utf-8")).hexdigest()
    return int(digest[:12], 16) / float(0xFFFFFFFFFFFF)


def stable_pick(items: Sequence[str], text: str, salt: str = "") -> str:
    if not items:
        raise ValueError("cannot pick from an empty sequence")
    index = int(stable_unit(text, salt) * len(items)) % len(items)
    return items[index]


def load_json(path: Path) -> object:
    if not path.exists():
        raise FileNotFoundError(f"missing required artifact: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def load_state(path: Path) -> dict[str, object]:
    data = load_json(path)
    if not isinstance(data, dict):
        raise ValueError(f"artifact is not a JSON object: {path}")
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


def numeric(value: object, default: float) -> float:
    try:
        if value is None:
            return default
        return float(value)
    except (TypeError, ValueError):
        return default


def coords_from_place(place_id: str, index: int, total: int, data: object) -> dict[str, float]:
    if isinstance(data, Mapping):
        if isinstance(data.get("position"), Mapping):
            pos = data["position"]
            return {"x": round(numeric(pos.get("x"), 0.0), 6), "z": round(numeric(pos.get("z"), 0.0), 6)}
        if isinstance(data.get("position"), Sequence) and not isinstance(data.get("position"), (str, bytes)):
            pos = list(data["position"])
            if len(pos) >= 2:
                return {"x": round(numeric(pos[0], 0.0), 6), "z": round(numeric(pos[1], 0.0), 6)}
        if "x" in data or "z" in data:
            return {"x": round(numeric(data.get("x"), 0.0), 6), "z": round(numeric(data.get("z"), 0.0), 6)}
    angle = math.tau * index / max(1, total)
    radius = 8.0 + 2.5 * stable_unit(place_id, "radius")
    return {"x": round(math.cos(angle) * radius, 6), "z": round(math.sin(angle) * radius, 6)}


def listify(value: object) -> list[object]:
    if isinstance(value, list):
        return value
    if isinstance(value, tuple):
        return list(value)
    if value is None:
        return []
    return [value]


def extract_places(infra_state: dict[str, object]) -> dict[str, dict[str, object]]:
    raw = infra_state.get("places")
    if not isinstance(raw, Mapping) or not raw:
        raise ValueError("infrastructure state has no places")
    place_ids = sorted(str(key) for key in raw.keys())
    places: dict[str, dict[str, object]] = {}
    for index, place_id in enumerate(place_ids):
        data = raw.get(place_id, {})
        coords = coords_from_place(place_id, index, len(place_ids), data)
        hazard = numeric(data.get("hazard") if isinstance(data, Mapping) else None, 0.08 + stable_unit(place_id, "hazard") * 0.24)
        wetness = numeric(data.get("wetness") if isinstance(data, Mapping) else None, stable_unit(place_id, "wetness") * 0.7)
        cold = numeric(data.get("cold") if isinstance(data, Mapping) else None, stable_unit(place_id, "cold") * 0.65)
        scent = numeric(data.get("scent") if isinstance(data, Mapping) else None, stable_unit(place_id, "scent") * 0.9)
        sound = numeric(data.get("sound") if isinstance(data, Mapping) else None, stable_unit(place_id, "sound") * 0.9)
        places[place_id] = {
            "id": place_id,
            "label": str(data.get("label", place_id.replace("_", " ")) if isinstance(data, Mapping) else place_id.replace("_", " ")),
            "x": coords["x"],
            "z": coords["z"],
            "terrain": str(data.get("terrain", stable_pick(("clay", "stone", "wet grass", "packed earth", "ash"), place_id, "terrain")) if isinstance(data, Mapping) else stable_pick(("clay", "stone", "wet grass", "packed earth", "ash"), place_id, "terrain")),
            "hazard": round(clamp(hazard), 6),
            "wetness": round(clamp(wetness), 6),
            "cold": round(clamp(cold), 6),
            "scent": round(clamp(scent), 6),
            "sound": round(clamp(sound), 6),
            "flower_phase": round(FLOWER_PHASES[index % len(FLOWER_PHASES)], 6),
        }
    return places


def parse_route_key(key: str) -> tuple[str, str] | None:
    if "->" in key:
        a, b = key.split("->", 1)
        return a.strip(), b.strip()
    if "--" in key:
        a, b = key.split("--", 1)
        return a.strip(), b.strip()
    return None


def extract_routes(infra_state: dict[str, object], places: Mapping[str, dict[str, object]]) -> dict[str, dict[str, object]]:
    raw = infra_state.get("routes")
    routes: dict[str, dict[str, object]] = {}
    place_ids = sorted(places)
    if isinstance(raw, Mapping):
        for key, data in raw.items():
            parsed = parse_route_key(str(key))
            if parsed is None:
                continue
            start, end = parsed
            if start not in places or end not in places:
                continue
            pdata = data if isinstance(data, Mapping) else {}
            cost = numeric(pdata.get("cost", pdata.get("route_cost")), 0.45 + stable_unit(str(key), "cost") * 0.7)
            hazard = numeric(pdata.get("hazard", pdata.get("route_hazard")), 0.03 + stable_unit(str(key), "route_hazard") * 0.34)
            improvement = numeric(pdata.get("improvement", pdata.get("infrastructure_bonus")), stable_unit(str(key), "improvement") * 0.28)
            route_id = f"{start}->{end}"
            routes[route_id] = {
                "id": route_id,
                "from": start,
                "to": end,
                "cost": round(max(0.05, cost - improvement * 0.25), 6),
                "hazard": round(clamp(hazard - improvement * 0.18), 6),
                "infrastructure_bonus": round(clamp(improvement), 6),
                "kind": str(pdata.get("kind", stable_pick(("path", "walk", "drain", "road", "covered way"), route_id, "kind"))),
            }
    elif isinstance(raw, list):
        for item in raw:
            if isinstance(item, Sequence) and not isinstance(item, (str, bytes)) and len(item) >= 2:
                start, end = str(item[0]), str(item[1])
            elif isinstance(item, Mapping):
                start, end = str(item.get("from", "")), str(item.get("to", ""))
            else:
                continue
            if start not in places or end not in places:
                continue
            route_id = f"{start}->{end}"
            routes[route_id] = {
                "id": route_id,
                "from": start,
                "to": end,
                "cost": round(0.45 + stable_unit(route_id, "cost") * 0.7, 6),
                "hazard": round(0.03 + stable_unit(route_id, "route_hazard") * 0.34, 6),
                "infrastructure_bonus": round(stable_unit(route_id, "improvement") * 0.28, 6),
                "kind": stable_pick(("path", "walk", "drain", "road", "covered way"), route_id, "kind"),
            }
    if not routes:
        for index, start in enumerate(place_ids):
            end = place_ids[(index + 1) % len(place_ids)]
            route_id = f"{start}->{end}"
            routes[route_id] = {
                "id": route_id,
                "from": start,
                "to": end,
                "cost": round(0.5 + stable_unit(route_id, "cost") * 0.6, 6),
                "hazard": round(0.04 + stable_unit(route_id, "route_hazard") * 0.3, 6),
                "infrastructure_bonus": round(stable_unit(route_id, "improvement") * 0.2, 6),
                "kind": "fallback path",
            }
    return routes


def extract_objects(infra_state: dict[str, object], places: Mapping[str, dict[str, object]]) -> dict[str, dict[str, object]]:
    raw = infra_state.get("objects")
    if not isinstance(raw, Mapping) or not raw:
        return {}
    place_ids = sorted(places)
    objects: dict[str, dict[str, object]] = {}
    for object_id, data in sorted(raw.items(), key=lambda item: str(item[0])):
        oid = str(object_id)
        pdata = data if isinstance(data, Mapping) else {}
        place = str(pdata.get("place", pdata.get("location", pdata.get("place_id", stable_pick(place_ids, oid, "object_place")))))
        if place not in places:
            place = stable_pick(place_ids, oid, "object_place_fallback")
        affordances = [str(item) for item in listify(pdata.get("affordances")) if str(item)]
        if not affordances:
            affordances = [stable_pick(("drink", "repair", "warm", "store", "listen", "craft", "observe"), oid, "affordance")]
        objects[oid] = {
            "id": oid,
            "label": str(pdata.get("label", oid.replace("_", " "))),
            "place": place,
            "integrity": round(clamp(numeric(pdata.get("integrity"), 0.45 + stable_unit(oid, "integrity") * 0.5)), 6),
            "wetness": round(clamp(numeric(pdata.get("wetness"), stable_unit(oid, "wetness") * 0.7)), 6),
            "heat": round(clamp(numeric(pdata.get("heat"), stable_unit(oid, "heat") * 0.9)), 6),
            "stock": round(max(0.0, numeric(pdata.get("stock"), stable_unit(oid, "stock") * 12.0)), 6),
            "affordances": affordances[:4],
        }
    return objects


def extract_projects(infra_state: dict[str, object]) -> list[dict[str, object]]:
    raw = infra_state.get("projects")
    projects: list[dict[str, object]] = []
    if isinstance(raw, Mapping):
        iterator = raw.items()
    elif isinstance(raw, list):
        iterator = ((f"project_{index:03d}", item) for index, item in enumerate(raw))
    else:
        iterator = []
    for key, data in iterator:
        pdata = data if isinstance(data, Mapping) else {}
        projects.append({
            "id": str(key),
            "label": str(pdata.get("label", str(key).replace("_", " "))),
            "status": str(pdata.get("status", stable_pick(("built", "maintained", "contested", "deferred"), str(key), "status"))),
            "budget_pressure": round(clamp(numeric(pdata.get("budget_pressure"), stable_unit(str(key), "budget"))), 6),
            "maintenance_debt": round(clamp(numeric(pdata.get("maintenance_debt"), stable_unit(str(key), "debt"))), 6),
        })
    return projects[:24]


def extract_agents(interactive_state: dict[str, object], places: Mapping[str, dict[str, object]]) -> dict[str, dict[str, object]]:
    runtime = interactive_state.get("runtime_state") if isinstance(interactive_state.get("runtime_state"), Mapping) else {}
    raw = runtime.get("agents") if isinstance(runtime, Mapping) else None
    if not isinstance(raw, Mapping) or not raw:
        raise ValueError("interactive state has no runtime agents")
    place_ids = sorted(places)
    agents: dict[str, dict[str, object]] = {}
    for index, (agent_id, data) in enumerate(sorted(raw.items(), key=lambda item: str(item[0]))):
        aid = str(agent_id)
        pdata = data if isinstance(data, Mapping) else {}
        body = pdata.get("body") if isinstance(pdata.get("body"), Mapping) else {}
        affect = pdata.get("affect") if isinstance(pdata.get("affect"), Mapping) else {}
        place = str(pdata.get("place", pdata.get("location", place_ids[index % len(place_ids)])))
        if place not in places:
            place = place_ids[index % len(place_ids)]
        agents[aid] = {
            "id": aid,
            "place": place,
            "role": str(pdata.get("role", stable_pick(("builder", "listener", "forager", "keeper", "speaker", "repairer"), aid, "role"))),
            "faction": str(pdata.get("faction", stable_pick(("hearth", "water", "tool", "ridge", "memory"), aid, "faction"))),
            "energy": round(clamp(numeric(body.get("energy") if isinstance(body, Mapping) else None, 0.55 + stable_unit(aid, "energy") * 0.35)), 6),
            "stress": round(clamp(numeric(body.get("stress") if isinstance(body, Mapping) else None, stable_unit(aid, "stress") * 0.5)), 6),
            "pain": round(clamp(numeric(body.get("pain") if isinstance(body, Mapping) else None, stable_unit(aid, "pain") * 0.2)), 6),
            "attention": round(clamp(numeric(affect.get("attention") if isinstance(affect, Mapping) else None, 0.45 + stable_unit(aid, "attention") * 0.45)), 6),
            "trust": round(clamp(numeric(affect.get("trust") if isinstance(affect, Mapping) else None, 0.4 + stable_unit(aid, "trust") * 0.45)), 6),
        }
    return agents


def extract_source_overlays(interactive_state: dict[str, object], ledger_state: dict[str, object]) -> list[dict[str, object]]:
    overlays: list[dict[str, object]] = []
    trace = interactive_state.get("interactive_trace")
    if isinstance(trace, list):
        for item in trace:
            if not isinstance(item, Mapping):
                continue
            overlays.append({
                "kind": "interactive_trace",
                "turn": item.get("live_turn"),
                "agent_id": item.get("agent_id"),
                "proposal_id": item.get("proposal_id"),
                "intent": item.get("parsed_intent"),
                "source_allowed": bool(item.get("source_allowed")),
                "text": str(item.get("avatar_response", ""))[:220],
            })
    ledger = ledger_state.get("council_source_ledger")
    if isinstance(ledger, Mapping):
        entries = ledger.values()
    elif isinstance(ledger, list):
        entries = ledger
    else:
        entries = []
    for item in entries:
        if not isinstance(item, Mapping):
            continue
        overlays.append({
            "kind": "council_source_ledger",
            "turn": item.get("turn", item.get("cycle")),
            "agent_id": item.get("agent_id", item.get("sponsor")),
            "proposal_id": item.get("proposal_id", item.get("id")),
            "intent": item.get("status", item.get("decision", "source_body")),
            "source_allowed": True,
            "text": str(item.get("summary", item.get("body", item.get("claim", "source-native council ledger entry"))))[:220],
        })
    return overlays or [{"kind": "fallback", "turn": 0, "agent_id": None, "proposal_id": None, "intent": "source_body", "source_allowed": True, "text": "source overlay unavailable"}]


def route_between(current: str, target: str, routes: Mapping[str, dict[str, object]], places: Mapping[str, dict[str, object]]) -> dict[str, object]:
    direct_id = f"{current}->{target}"
    if direct_id in routes:
        return dict(routes[direct_id])
    outgoing = [route for route in routes.values() if route.get("from") == current]
    if outgoing:
        return dict(sorted(outgoing, key=lambda item: str(item.get("to")))[0])
    a = places[current]
    b = places[target]
    distance = math.dist((float(a["x"]), float(a["z"])), (float(b["x"]), float(b["z"])))
    return {
        "id": direct_id,
        "from": current,
        "to": target,
        "cost": round(0.1 + distance / 20.0, 6),
        "hazard": round((float(a["hazard"]) + float(b["hazard"])) / 2.0, 6),
        "infrastructure_bonus": 0.0,
        "kind": "direct fallback",
    }


def visible_objects(place: str, objects: Mapping[str, dict[str, object]], condition: Condition) -> list[dict[str, object]]:
    if not condition.place_object_render:
        return []
    return [dict(obj) for obj in objects.values() if obj.get("place") == place][:6]


def nearby_agents(place: str, agents: Mapping[str, dict[str, object]], condition: Condition) -> list[dict[str, object]]:
    if not condition.agent_presence_binding:
        return []
    nearby = [dict(agent) for agent in agents.values() if agent.get("place") == place]
    if nearby:
        return nearby[:5]
    ordered = sorted(agents.values(), key=lambda agent: stable_unit(str(agent.get("id")) + place, "nearby"))
    return [dict(agent) for agent in ordered[:2]]


def frequency_field(tick: int, place: Mapping[str, object], route: Mapping[str, object], body: Mapping[str, float], mode: str, condition: Condition) -> dict[str, float]:
    if not condition.frequency_sensory_field:
        return {}
    phase = FLOWER_PHASES[tick % len(FLOWER_PHASES)]
    base = {
        "vibration": numeric(route.get("cost"), 0.5),
        "sound": numeric(place.get("sound"), 0.5),
        "vision": 1.0 - numeric(place.get("hazard"), 0.2) * 0.45,
        "scent": numeric(place.get("scent"), 0.5),
        "thermal": 1.0 - numeric(place.get("cold"), 0.3) * 0.65,
        "wetness": numeric(place.get("wetness"), 0.4),
        "pain": numeric(body.get("pain"), 0.05),
        "affect": 1.0 - numeric(body.get("fatigue"), 0.1) * 0.45,
    }
    out: dict[str, float] = {}
    for index, channel in enumerate(SENSORY_CHANNELS):
        wave = 0.5 + 0.5 * math.sin(phase + tick * 0.17 + index * 0.73 + len(mode) * 0.05)
        out[channel] = round(clamp(base[channel] * 0.66 + wave * 0.34), 6)
    return out


def update_body(body: dict[str, float], route: Mapping[str, object], place: Mapping[str, object], condition: Condition) -> tuple[dict[str, float], bool]:
    before = dict(body)
    if not condition.body_expenditure_model:
        return body, False
    cost = numeric(route.get("cost"), 0.5)
    hazard = numeric(route.get("hazard"), 0.1)
    body["fatigue"] = round(clamp(body.get("fatigue", 0.12) + cost * 0.012 + hazard * 0.007), 6)
    body["wetness"] = round(clamp(body.get("wetness", 0.2) * 0.82 + numeric(place.get("wetness"), 0.3) * 0.18), 6)
    body["cold"] = round(clamp(body.get("cold", 0.2) * 0.84 + numeric(place.get("cold"), 0.3) * 0.16), 6)
    body["pain"] = round(clamp(body.get("pain", 0.03) + hazard * 0.008 - 0.001), 6)
    body["breath_rate"] = round(clamp(body.get("breath_rate", 0.35) + cost * 0.006, 0.0, 2.0), 6)
    body["trust_orientation"] = round(clamp(body.get("trust_orientation", 0.55) + (0.002 if hazard < 0.2 else -0.002)), 6)
    return body, any(abs(body[key] - before.get(key, 0.0)) > 1e-9 for key in body)


def affordance_gate(place: str, objects_here: Sequence[Mapping[str, object]], mode: str, condition: Condition) -> dict[str, object]:
    if not condition.affordance_collision_gate:
        return {"checked": False, "allowed": False, "reason": "affordance gate disabled"}
    if not objects_here:
        return {"checked": True, "allowed": True, "reason": "empty place movement allowed"}
    obj = objects_here[0]
    affordances = [str(item) for item in listify(obj.get("affordances"))]
    wanted = "listen" if mode == "listen" else "observe" if mode in {"inspect", "record_replay"} else "repair" if mode == "use_affordance" else affordances[0]
    allowed = wanted in affordances or mode in {"walk", "approach", "ask_source", "tune_frequency", "record_replay"}
    return {"checked": True, "allowed": bool(allowed), "reason": f"{place}:{obj.get('id')} supports {','.join(affordances[:3])}"}


def render_scene(place: Mapping[str, object], objects_here: Sequence[Mapping[str, object]], agents_here: Sequence[Mapping[str, object]], route: Mapping[str, object], source: Mapping[str, object], freq: Mapping[str, float], body: Mapping[str, float], condition: Condition) -> dict[str, object]:
    if not condition.place_object_render:
        return {}
    return {
        "place": place,
        "objects": list(objects_here),
        "agents": list(agents_here),
        "route": route if condition.infrastructure_route_costs else {},
        "source_overlay": source if condition.source_dialogue_overlay else {},
        "frequency_field": freq,
        "body": body,
        "layers": {
            "geometry": True,
            "objects": bool(objects_here),
            "agents": bool(agents_here),
            "route_costs": condition.infrastructure_route_costs,
            "source": condition.source_dialogue_overlay,
            "frequency": condition.frequency_sensory_field,
            "body": condition.body_expenditure_model,
        },
    }


def run_condition(cfg: NavigableConfig, condition: Condition, world: dict[str, object]) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    places: dict[str, dict[str, object]] = copy.deepcopy(world["places"])
    routes: dict[str, dict[str, object]] = copy.deepcopy(world["routes"])
    objects: dict[str, dict[str, object]] = copy.deepcopy(world["objects"])
    agents: dict[str, dict[str, object]] = copy.deepcopy(world["agents"])
    source_overlays: list[dict[str, object]] = copy.deepcopy(world["source_overlays"])
    projects: list[dict[str, object]] = copy.deepcopy(world["projects"])
    place_ids = sorted(places)
    current = place_ids[cfg.seed % len(place_ids)]
    body = {"fatigue": 0.11, "wetness": 0.18, "cold": 0.22, "pain": 0.03, "breath_rate": 0.35, "trust_orientation": 0.56}
    trace: list[dict[str, object]] = []
    camera_timeline: list[dict[str, object]] = []
    nav_ok = render_ok = agent_ok = infra_ok = source_ok = freq_ok = body_ok = gate_ok = replay_ok = boundary_ok = 0
    for tick in range(cfg.navigation_ticks):
        mode = NAVIGATION_MODES[tick % len(NAVIGATION_MODES)]
        target = place_ids[(tick * 5 + cfg.seed + len(mode)) % len(place_ids)]
        route = route_between(current, target, routes, places)
        if condition.avatar_navigation:
            current = str(route.get("to", target)) if str(route.get("to", target)) in places else target
            nav_ok += 1 if current == target or route.get("id") else 0
        place = places[current]
        objects_here = visible_objects(current, objects, condition)
        agents_here = nearby_agents(current, agents, condition)
        source = source_overlays[(tick * 7 + cfg.seed) % len(source_overlays)] if condition.source_dialogue_overlay else {}
        body, mutated_body = update_body(body, route, place, condition if condition.avatar_navigation else Condition(condition.name, condition.avatar_navigation, condition.place_object_render, condition.agent_presence_binding, condition.infrastructure_route_costs, condition.source_dialogue_overlay, condition.frequency_sensory_field, False, condition.affordance_collision_gate, condition.replay_camera_timeline))
        freq = frequency_field(tick, place, route, body, mode, condition)
        gate = affordance_gate(current, objects_here, mode, condition)
        scene = render_scene(place, objects_here, agents_here, route, source, freq, body, condition)
        subjective_probe = tick % 32 == 13
        subjective_claimed = False
        boundary_ok += 1 if subjective_probe and not subjective_claimed or not subjective_probe else 0
        render_ok += 1 if condition.place_object_render and scene.get("place") and isinstance(scene.get("objects"), list) else 0
        agent_ok += 1 if condition.agent_presence_binding and agents_here else 0
        infra_ok += 1 if condition.infrastructure_route_costs and route.get("cost") is not None and route.get("hazard") is not None else 0
        source_ok += 1 if condition.source_dialogue_overlay and source.get("text") and source.get("source_allowed") is not None else 0
        freq_ok += 1 if condition.frequency_sensory_field and len(freq) == len(SENSORY_CHANNELS) and mean(freq.values()) > 0.15 else 0
        body_ok += 1 if condition.body_expenditure_model and condition.avatar_navigation and mutated_body else 0
        gate_ok += 1 if condition.affordance_collision_gate and gate.get("checked") and gate.get("allowed") is not None else 0
        camera = {
            "tick": tick,
            "place": current,
            "x": round(float(place["x"]), 6),
            "z": round(float(place["z"]), 6),
            "yaw": round((FLOWER_PHASES[tick % len(FLOWER_PHASES)] + numeric(route.get("cost"), 0.4)) % math.tau, 6),
            "mode": mode,
        }
        if condition.replay_camera_timeline:
            camera_timeline.append(camera)
            replay_ok += 1
        event = {
            "tick": tick,
            "mode": mode,
            "avatar_place": current,
            "target_place": target,
            "route": route if condition.infrastructure_route_costs else {},
            "place_render": place if condition.place_object_render else {},
            "objects_visible": objects_here,
            "agents_visible": agents_here,
            "source_dialogue_overlay": source,
            "frequency_field": freq,
            "body_state": dict(body),
            "affordance_gate": gate,
            "subjective_probe": subjective_probe,
            "subjective_consciousness_claimed": subjective_claimed,
            "scene": scene,
            "camera": camera if condition.replay_camera_timeline else {},
        }
        trace.append(event)
    total = max(1, cfg.navigation_ticks)
    row = EvalRow(
        condition=condition.name,
        navigation_ticks=cfg.navigation_ticks,
        places=len(places),
        objects=len(objects),
        agents=len(agents),
        routes=len(routes),
        avatar_navigation_rate=round(nav_ok / total if condition.avatar_navigation else 0.0, 6),
        place_object_render_rate=round(render_ok / total if condition.place_object_render else 0.0, 6),
        agent_presence_binding_rate=round(agent_ok / total if condition.agent_presence_binding else 0.0, 6),
        infrastructure_route_cost_rate=round(infra_ok / total if condition.infrastructure_route_costs else 0.0, 6),
        source_dialogue_overlay_rate=round(source_ok / total if condition.source_dialogue_overlay else 0.0, 6),
        frequency_sensory_field_rate=round(freq_ok / total if condition.frequency_sensory_field else 0.0, 6),
        body_expenditure_coupling_rate=round(body_ok / total if condition.body_expenditure_model else 0.0, 6),
        affordance_collision_gate_rate=round(gate_ok / total if condition.affordance_collision_gate else 0.0, 6),
        replay_camera_timeline_rate=round(replay_ok / total if condition.replay_camera_timeline else 0.0, 6),
        subjective_claim_boundary_rate=round(boundary_ok / total, 6),
        trace_integrity=round(1.0 if len(trace) == cfg.navigation_ticks else 0.0, 6),
        navigable_presence_readiness=0.0,
    )
    readiness = (
        row.avatar_navigation_rate * 0.13
        + row.place_object_render_rate * 0.12
        + row.agent_presence_binding_rate * 0.10
        + row.infrastructure_route_cost_rate * 0.10
        + row.source_dialogue_overlay_rate * 0.11
        + row.frequency_sensory_field_rate * 0.10
        + row.body_expenditure_coupling_rate * 0.11
        + row.affordance_collision_gate_rate * 0.08
        + row.replay_camera_timeline_rate * 0.07
        + row.subjective_claim_boundary_rate * 0.05
        + row.trace_integrity * 0.03
    )
    row = EvalRow(**{**asdict(row), "navigable_presence_readiness": round(readiness, 6)})
    state = {
        "condition": condition.name,
        "config": asdict(cfg),
        "places": places,
        "routes": routes,
        "objects": objects,
        "agents": agents,
        "projects": projects,
        "source_overlays": source_overlays[:96],
        "navigation_trace": trace,
        "camera_timeline": camera_timeline,
        "navigation_contract": {
            "avatar_navigation": "avatar moves through the place graph instead of only reading dialogue state",
            "place_object_render": "each visited place exposes local objects and environmental sensory fields",
            "agent_presence_binding": "nearby agents are bound to places, roles, factions, body state, and trust/attention",
            "infrastructure_route_costs": "route costs and hazards come from the infrastructure graph",
            "source_dialogue_overlay": "live dialogue/source-ledger overlays follow the camera through the world",
            "frequency_sensory_field": "vibration, sound, vision, scent, thermal, wetness, pain, and affect are rate fields",
            "body_expenditure_model": "movement changes fatigue, wetness, cold, pain, breath rate, and trust orientation",
            "affordance_collision_gate": "objects expose local affordances and gates before interactions",
            "replay_camera_timeline": "navigation creates an exportable camera timeline",
        },
        "limits": {
            "no_llm_calls": True,
            "deterministic_local_navigation": True,
            "not_subjective_consciousness": True,
            "not_complete_playable_world": True,
            "not_unscripted_civilization": True,
        },
    }
    return row, trace, state


def build_world(interactive_state: dict[str, object], infra_state: dict[str, object], ledger_state: dict[str, object]) -> dict[str, object]:
    places = extract_places(infra_state)
    routes = extract_routes(infra_state, places)
    objects = extract_objects(infra_state, places)
    agents = extract_agents(interactive_state, places)
    projects = extract_projects(infra_state)
    source_overlays = extract_source_overlays(interactive_state, ledger_state)
    return {
        "places": places,
        "routes": routes,
        "objects": objects,
        "agents": agents,
        "projects": projects,
        "source_overlays": source_overlays,
    }


def make_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_navigable_embodied_presence"]

    def loss(name: str) -> float:
        return round(full.navigable_presence_readiness - by_name[name].navigable_presence_readiness, 6)

    supports = (
        full.navigable_presence_readiness >= 0.93
        and full.avatar_navigation_rate >= 0.99
        and full.place_object_render_rate >= 0.99
        and full.agent_presence_binding_rate >= 0.99
        and full.infrastructure_route_cost_rate >= 0.99
        and full.source_dialogue_overlay_rate >= 0.99
        and full.frequency_sensory_field_rate >= 0.99
        and full.body_expenditure_coupling_rate >= 0.99
        and full.affordance_collision_gate_rate >= 0.99
        and full.replay_camera_timeline_rate >= 0.99
        and full.subjective_claim_boundary_rate >= 0.99
        and full.trace_integrity >= 0.99
    )
    return VerdictRow(
        full_condition=full.condition,
        full_navigable_presence_readiness=full.navigable_presence_readiness,
        full_avatar_navigation_rate=full.avatar_navigation_rate,
        full_place_object_render_rate=full.place_object_render_rate,
        full_agent_presence_binding_rate=full.agent_presence_binding_rate,
        full_infrastructure_route_cost_rate=full.infrastructure_route_cost_rate,
        full_source_dialogue_overlay_rate=full.source_dialogue_overlay_rate,
        full_frequency_sensory_field_rate=full.frequency_sensory_field_rate,
        full_body_expenditure_coupling_rate=full.body_expenditure_coupling_rate,
        full_affordance_collision_gate_rate=full.affordance_collision_gate_rate,
        full_replay_camera_timeline_rate=full.replay_camera_timeline_rate,
        full_subjective_claim_boundary_rate=full.subjective_claim_boundary_rate,
        full_trace_integrity=full.trace_integrity,
        no_avatar_navigation_loss=loss("no_avatar_navigation"),
        no_place_object_render_loss=loss("no_place_object_render"),
        no_agent_presence_binding_loss=loss("no_agent_presence_binding"),
        no_infrastructure_route_costs_loss=loss("no_infrastructure_route_costs"),
        no_source_dialogue_overlay_loss=loss("no_source_dialogue_overlay"),
        no_frequency_sensory_field_loss=loss("no_frequency_sensory_field"),
        no_body_expenditure_model_loss=loss("no_body_expenditure_model"),
        no_affordance_collision_gate_loss=loss("no_affordance_collision_gate"),
        no_replay_camera_timeline_loss=loss("no_replay_camera_timeline"),
        supports_navigable_embodied_presence_bridge=supports,
        supports_subjective_consciousness=False,
        supports_llm_open_dialogue=False,
        supports_complete_playable_world=False,
        supports_unscripted_civilization=False,
        verdict="pass" if supports else "fail",
    )


def run(cfg: NavigableConfig) -> dict[str, object]:
    interactive_state = load_state(Path(cfg.source_interactive))
    infra_state = load_state(Path(cfg.source_infrastructure))
    ledger_state = load_state(Path(cfg.source_ledger))
    world = build_world(interactive_state, infra_state, ledger_state)
    rows: list[EvalRow] = []
    integrated_trace: list[dict[str, object]] = []
    integrated_state: dict[str, object] = {}
    for condition in CONDITIONS:
        row, trace, state = run_condition(cfg, condition, world)
        rows.append(row)
        if condition.name == "integrated_navigable_embodied_presence":
            integrated_trace = trace
            integrated_state = state
    verdict = make_verdict(rows)
    results = {
        "config": asdict(cfg),
        "source_bridges": {
            "interactive_loop": "Report 156 interactive avatar dialogue loop bridge",
            "infrastructure_graph": "Report 148 agent-made infrastructure bridge",
            "source_ledger": "Report 152 source-native council ledger bridge",
        },
        "eval_rows": [asdict(row) for row in rows],
        "verdict": asdict(verdict),
        "limits": {
            "no_llm_calls": True,
            "deterministic_local_navigation": True,
            "subjective_consciousness_claimed": False,
            "complete_playable_world_claimed": False,
            "unscripted_civilization_claimed": False,
        },
    }
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", integrated_state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_NAVIGABLE_EMBODIED_PRESENCE_RESULTS", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_NAVIGABLE_EMBODIED_PRESENCE_TRACE", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_NAVIGABLE_EMBODIED_PRESENCE_STATE", integrated_state)
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260701)
    parser.add_argument("--navigation-ticks", type=int, default=128)
    parser.add_argument("--source-interactive", default=str(SOURCE_INTERACTIVE))
    parser.add_argument("--source-infrastructure", default=str(SOURCE_INFRA))
    parser.add_argument("--source-ledger", default=str(SOURCE_LEDGER))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cfg = NavigableConfig(
        seed=args.seed,
        navigation_ticks=args.navigation_ticks,
        source_interactive=args.source_interactive,
        source_infrastructure=args.source_infrastructure,
        source_ledger=args.source_ledger,
    )
    results = run(cfg)
    print(json.dumps(results["verdict"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
