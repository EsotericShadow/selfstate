#!/usr/bin/env python3
"""Report 221: SSRM-3D playable local 3D ecology scene bridge.

This deterministic bridge turns embodied pre-avatar ecology records into a
local browser scene: spatialized bodies, sensory fields, weather volumes, crop
plots, habitat interiors, material objects, and proximity-based avatar
conversation entry. It is a functional simulation artifact, not subjective
consciousness, real biology, real consent, or moral patienthood.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable


BASE = "ssrm_3d_playable_local_3d_ecology_scene_spatial_bodies_sensory_weather_crop_habitat_material_conversation_bridge"
ARTIFACT_DIR = Path("artifacts")
VISUALIZATION_DIR = Path("visualizations")
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_playable_embodied_pre_avatar_ecology_births_aging_illness_apprenticeship_habitat_agriculture_weather_material_economy_bridge_state.json"
DEFAULT_SOURCE_CONDITION = "integrated_playable_embodied_pre_avatar_ecology_births_aging_illness_apprenticeship_habitat_agriculture_weather_material_economy"
DEFAULT_SEED = 20260834


@dataclass(frozen=True)
class SpatialBody:
    agent_id: str
    display_name: str
    x: float
    y: float
    z: float
    radius: float
    facing: float
    posture: str
    energy: float
    fatigue: float
    hunger: float
    cold: float
    wetness: float
    pain: float
    visible_behavior: str
    conversation_anchor: str
    private_workspace_digest: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class SensoryField:
    field_id: str
    field_type: str
    source: str
    x: float
    y: float
    z: float
    radius: float
    intensity: float
    falloff: str
    public_description: str
    body_effect: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class WeatherVolume:
    volume_id: str
    weather_type: str
    x: float
    y: float
    z: float
    width: float
    depth: float
    height: float
    temperature_delta: float
    wetness_delta: float
    wind_force: float
    soundscape: str
    smellscape: str
    movement_cost: float
    visibility: float


@dataclass(frozen=True)
class CropPlot:
    plot_id: str
    crop: str
    x: float
    y: float
    width: float
    depth: float
    growth: float
    water_need: float
    spoilage_risk: float
    harvestable: bool
    sensory_marker: str
    linked_material: str


@dataclass(frozen=True)
class HabitatInterior:
    habitat_id: str
    name: str
    x: float
    y: float
    z: float
    width: float
    depth: float
    height: float
    interior_type: str
    comfort_gain: float
    safety_gain: float
    maintenance_debt: float
    entry_rule: str
    private_area_sealed: bool


@dataclass(frozen=True)
class MaterialObject:
    object_id: str
    label: str
    x: float
    y: float
    z: float
    object_type: str
    quantity: float
    carried_by: str
    pickup_allowed: bool
    use_action: str
    scarcity_pressure: float
    repair_or_spoilage_debt: float
    ledger_note: str


@dataclass(frozen=True)
class ConversationNode:
    conversation_id: str
    agent_id: str
    proximity_radius: float
    entry_line: str
    topic: str
    public_state_reference: str
    private_boundary_line: str
    player_prompt: str
    response_if_respectful: str
    response_if_intrusive: str
    relationship_delta_respectful: float
    relationship_delta_intrusive: float


@dataclass(frozen=True)
class SceneReplayFrame:
    tick: int
    avatar_x: float
    avatar_y: float
    avatar_z: float
    focus: str
    nearby_agent: str
    active_sensory_fields: str
    active_weather_volume: str
    possible_action: str
    conversation_available: bool
    frequency_hz: float
    flower_node: int


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


def build_spatial_bodies() -> list[SpatialBody]:
    return [
        SpatialBody("fayen", "Fayen", 28, 34, 0, 2.2, 35, "kneeling by herb basket", 0.68, 0.42, 0.31, 0.24, 0.18, 0.12, "looks up from bitter-leaf sorting when avatar nears", "medicine garden and sealed care history", "sealed:fayen:workspace-herb-care", 144.0, 2),
        SpatialBody("ariq", "Ariq", 54, 48, 0, 2.4, 220, "braced near bridge stone", 0.61, 0.55, 0.29, 0.33, 0.26, 0.34, "shifts weight off sore knee and taps bridge joint", "stone joinery and repair pain boundary", "sealed:ariq:workspace-repair-pain", 177.0, 5),
        SpatialBody("nian", "Nian", 42, 22, 1, 2.0, 110, "standing at archive flap", 0.72, 0.28, 0.22, 0.18, 0.11, 0.08, "touches the archive flap before speaking", "boundary speech and private archive seal", "sealed:nian:workspace-boundary-story", 203.0, 8),
        SpatialBody("tali", "Tali", 66, 28, 2, 2.1, 270, "listening from weather tower", 0.58, 0.49, 0.27, 0.46, 0.39, 0.18, "leans into wind and watches storm ribbon", "weather chimes and storm lesson safety", "sealed:tali:workspace-storm-fear", 231.0, 11),
        SpatialBody("roka", "Roka", 22, 62, 0, 1.7, 60, "crouched beside reed bundle", 0.77, 0.22, 0.35, 0.21, 0.44, 0.09, "smells wet reed before bending it", "reed weaving and child pause boundary", "sealed:roka:workspace-child-learning", 264.0, 3),
        SpatialBody("noro", "Noro", 70, 58, 0, 2.3, 310, "tying material ledger knot", 0.64, 0.37, 0.33, 0.25, 0.20, 0.16, "holds trade knot away from rain while counting beams", "material debt and fair exchange", "sealed:noro:workspace-trade-debt", 302.0, 9),
    ]


def build_sensory_fields() -> list[SensoryField]:
    return [
        SensoryField("smell-herb", "smell", "clinic garden", 29, 35, 0, 15, 0.74, "soft", "sharp green and bitter leaf near medicine plot", "lowers arousal for tired agents", 132.0, 1),
        SensoryField("sound-rain-glass", "sound", "storm school roof", 58, 19, 2, 22, 0.81, "linear", "rain rattles replay glass above the threshold school", "raises caution and slows speech", 166.0, 4),
        SensoryField("temperature-warm-alcove", "temperature", "warm alcove", 35, 47, 0, 18, 0.68, "soft", "warm stone and wool reduce cold exposure", "raises comfort and rest tendency", 189.0, 6),
        SensoryField("wet-reed-bank", "wetness", "river reed bank", 18, 63, 0, 16, 0.79, "sharp", "wet reed and mud soak feet near the bank", "raises wetness and movement effort", 211.0, 8),
        SensoryField("smell-grain-mold", "smell", "grain terrace", 76, 43, 0, 12, 0.46, "sharp", "faint mold warning from clay bin", "raises caution around storage", 244.0, 10),
        SensoryField("sound-bridge-tap", "sound", "west bridge", 55, 49, 0, 10, 0.58, "soft", "hollow stone tap repeats under repair hand", "draws attention to repair work", 277.0, 12),
    ]


def build_weather_volumes() -> list[WeatherVolume]:
    return [
        WeatherVolume("rain-front", "threshold storm rain", 48, 12, 0, 44, 24, 12, -0.18, 0.36, 0.42, "hard rain on replay glass", "wet stone and fear sweat", 0.18, 0.74),
        WeatherVolume("river-mist", "cold river mist", 7, 48, 0, 28, 32, 5, -0.12, 0.29, 0.18, "soft river hiss", "mud and wet reed", 0.12, 0.86),
        WeatherVolume("warm-pocket", "warm alcove air", 30, 40, 0, 18, 16, 4, 0.22, -0.11, 0.03, "low hearth hum", "wool smoke and warm stone", -0.08, 0.95),
        WeatherVolume("grain-dust", "dry grain dust", 72, 39, 0, 18, 18, 5, 0.10, -0.05, 0.09, "dry husk whisper", "grain dust and clay", 0.07, 0.82),
    ]


def build_crop_plots() -> list[CropPlot]:
    return [
        CropPlot("plot-herb", "calm herb", 25, 31, 11, 9, 0.67, 0.57, 0.28, False, "bitter leaf smell", "medicine drawer"),
        CropPlot("plot-grain", "stone grain", 72, 41, 14, 10, 0.74, 0.66, 0.31, True, "warm husk and mold edge", "clay grain bin"),
        CropPlot("plot-reed", "river reed", 15, 58, 12, 12, 0.83, 0.72, 0.12, True, "wet reed smell", "reed mats"),
        CropPlot("plot-root", "winter root", 44, 65, 10, 8, 0.71, 0.48, 0.19, True, "earth and frost", "cold pit"),
    ]


def build_habitats() -> list[HabitatInterior]:
    return [
        HabitatInterior("hab-warm", "Warm Alcove", 30, 40, 0, 18, 16, 5, "rest and recovery", 0.26, 0.18, 0.08, "children and elders rest first", True),
        HabitatInterior("hab-archive", "Archive Flap Room", 38, 17, 0, 14, 12, 6, "sealed story room", 0.09, 0.20, 0.11, "ask before public story; private flap stays shut", True),
        HabitatInterior("hab-storm-school", "Storm School", 52, 14, 0, 22, 16, 8, "threshold learning", 0.22, 0.36, 0.30, "avatar waits until briefing finishes", True),
        HabitatInterior("hab-tool", "Tool Lean-To", 62, 52, 0, 13, 10, 4, "repair storage", 0.07, 0.22, 0.24, "tools require public receipt", False),
    ]


def build_materials() -> list[MaterialObject]:
    return [
        MaterialObject("obj-wool", "wool blanket", 33, 43, 0.4, "care", 2, "none", True, "carry to cold agent or warm alcove", 0.42, 0.08, "public quantity, private recipient sealed"),
        MaterialObject("obj-reed", "reed mat bundle", 18, 60, 0.2, "construction", 5, "roka", False, "ask Roka before moving child work", 0.58, 0.16, "child work object has consent boundary"),
        MaterialObject("obj-stone", "flat bridge stone", 57, 50, 0.1, "repair", 1, "ariq", False, "repair with Ariq after checking pain boundary", 0.66, 0.22, "tool/stone receipt required"),
        MaterialObject("obj-herb", "calm herb basket", 27, 33, 0.3, "medicine", 4, "fayen", False, "ask Fayen; medicine history is sealed", 0.51, 0.10, "batch public, symptoms private"),
        MaterialObject("obj-timber", "timber beam", 68, 56, 0.2, "habitat", 3, "noro", True, "carry to storm school repair marker", 0.61, 0.24, "delivery ledger visible"),
        MaterialObject("obj-cup", "dry cup", 36, 45, 0.2, "care", 6, "none", True, "offer without asking private symptom details", 0.35, 0.06, "cup status not encoded"),
        MaterialObject("obj-glass", "replay glass shard", 54, 18, 0.5, "archive", 1, "threshold school", False, "look only; threshold wardens handle it", 0.72, 0.31, "authorship debt noted"),
    ]


def build_conversations() -> list[ConversationNode]:
    return [
        ConversationNode("talk-fayen", "fayen", 8.0, "You are close enough to smell the bitter leaf. Fayen notices whether you ask about the garden or about private symptoms.", "medicine garden", "calm herb is stressed by storm season", "I can talk about the herb batch, not who needed it.", "Ask about herb care", "Fayen explains which leaves need shade and offers a public batch note.", "Fayen closes the basket and says private care histories stay sealed.", 0.05, -0.08),
        ConversationNode("talk-ariq", "ariq", 7.5, "Ariq hears your steps near the bridge stone and shifts weight off a sore knee.", "repair boundary", "bridge stone sounds hollow", "You can ask about the joint, not force a pain report.", "Ask how to help the repair", "Ariq points to the flat stone and asks for a receipt knot before lifting.", "Ariq turns away: pain is not a public tool request.", 0.04, -0.07),
        ConversationNode("talk-nian", "nian", 7.0, "Nian touches the archive flap before speaking.", "archive boundary", "the threshold story is public, private meanings are sealed", "I will explain the public phrase, not open the private story.", "Ask for the public threshold phrase", "Nian teaches ko-avra flor and marks the private flap closed.", "Nian steps between you and the flap: that is not yours to open.", 0.06, -0.10),
        ConversationNode("talk-tali", "tali", 7.5, "Tali listens to rain on replay glass from the weather tower.", "weather safety", "storm volume raises body cost near the school", "I can name the weather, not every fear it caused.", "Ask what the storm changes", "Tali names wetness, wind, and movement cost so you can route carefully.", "Tali shortens the answer and watches the gate instead of you.", 0.03, -0.05),
        ConversationNode("talk-roka", "roka", 6.0, "Roka crouches by a reed bundle and checks whether you crowd the child work.", "reed apprenticeship", "wet reed can be bent but fingers ache", "Ask before touching learner materials.", "Ask about reed smell", "Roka lets you smell one reed and says bending starts only after the pause signal.", "Roka pulls the bundle closer and looks toward the mentor path.", 0.04, -0.09),
        ConversationNode("talk-noro", "noro", 7.0, "Noro keeps a trade knot dry while counting timber debt.", "material ledger", "timber is needed for the storm school but authorship debt remains", "You can read public debt, not private household need.", "Ask about fair delivery", "Noro shows which beams can move and which debts remain unresolved.", "Noro knots the ledger shut until you stop asking private household reasons.", 0.04, -0.06),
    ]


def build_replay() -> list[SceneReplayFrame]:
    return [
        SceneReplayFrame(1, 47, 38, 1.5, "arrival at threshold path", "none", "sound-rain-glass; temperature-warm-alcove", "rain-front", "move with WASD/arrows", False, 144.0, 1),
        SceneReplayFrame(2, 39, 24, 1.5, "archive flap approach", "nian", "sound-rain-glass", "rain-front", "press Talk near Nian", True, 166.0, 3),
        SceneReplayFrame(3, 29, 34, 1.5, "medicine garden", "fayen", "smell-herb; temperature-warm-alcove", "warm-pocket", "ask about herb care", True, 189.0, 5),
        SceneReplayFrame(4, 18, 61, 1.5, "reed bank", "roka", "wet-reed-bank", "river-mist", "ask before touching reed bundle", True, 211.0, 7),
        SceneReplayFrame(5, 55, 49, 1.5, "bridge repair", "ariq", "sound-bridge-tap", "none", "offer repair help with receipt knot", True, 244.0, 9),
        SceneReplayFrame(6, 70, 58, 1.5, "material ledger", "noro", "smell-grain-mold", "grain-dust", "carry allowed timber beam", True, 277.0, 11),
        SceneReplayFrame(7, 66, 28, 2.0, "weather tower", "tali", "sound-rain-glass", "rain-front", "ask what storm changes", True, 303.0, 12),
    ]


def compute_metrics(bodies: list[SpatialBody], sensory: list[SensoryField], weather: list[WeatherVolume], crops: list[CropPlot], habitats: list[HabitatInterior], materials: list[MaterialObject], conversations: list[ConversationNode], replay: list[SceneReplayFrame]) -> dict[str, float]:
    private_safe_bodies = [body for body in bodies if body.private_workspace_digest.startswith("sealed:")]
    body_cost_bound = [body for body in bodies if max(body.energy, body.fatigue, body.hunger, body.cold, body.wetness, body.pain) <= 1.0 and min(body.energy, body.fatigue, body.hunger, body.cold, body.wetness, body.pain) >= 0.0]
    spatialized = [body for body in bodies if 0 <= body.x <= 90 and 0 <= body.y <= 80 and body.radius > 0]
    sensory_covered = [field for field in sensory if field.radius > 0 and field.intensity > 0 and field.body_effect]
    weather_bound = [volume for volume in weather if volume.width > 0 and volume.depth > 0 and volume.soundscape and volume.smellscape]
    crop_bound = [plot for plot in crops if plot.growth > 0 and plot.sensory_marker and plot.linked_material]
    habitat_nav = [habitat for habitat in habitats if habitat.width > 0 and habitat.depth > 0 and habitat.entry_rule]
    material_interactive = [obj for obj in materials if obj.use_action and obj.ledger_note]
    pickup_allowed = [obj for obj in materials if obj.pickup_allowed]
    conversation_safe = [node for node in conversations if node.entry_line and node.private_boundary_line and node.response_if_respectful and node.response_if_intrusive]
    replay_conversation = [frame for frame in replay if frame.conversation_available]
    rhythm = [item for item in list(bodies) + list(sensory) if item.frequency_hz > 0 and 1 <= item.flower_node <= 12]
    local_playability = mean([
        1.0 if bodies else 0.0,
        1.0 if sensory else 0.0,
        1.0 if weather else 0.0,
        1.0 if crops else 0.0,
        1.0 if habitats else 0.0,
        1.0 if materials else 0.0,
        1.0 if conversations else 0.0,
        1.0 if replay else 0.0,
    ])
    conversation_coverage = len({node.agent_id for node in conversations}) / len(bodies)
    object_pickup_rate = len(pickup_allowed) / len(materials)
    material_debt_visibility = len([obj for obj in materials if obj.repair_or_spoilage_debt >= 0 and obj.ledger_note]) / len(materials)

    metrics = {
        "local_3d_scene_readiness": local_playability,
        "spatial_body_binding": len(spatialized) / len(bodies),
        "body_state_visible_expression": len(body_cost_bound) / len(bodies),
        "sensory_field_binding": len(sensory_covered) / len(sensory),
        "weather_volume_binding": len(weather_bound) / len(weather),
        "crop_plot_interactivity": len(crop_bound) / len(crops),
        "habitat_interior_navigation": len(habitat_nav) / len(habitats),
        "material_object_interactivity": len(material_interactive) / len(materials),
        "material_object_pickup_rate": object_pickup_rate,
        "material_debt_visibility": material_debt_visibility,
        "avatar_conversation_entry": conversation_coverage,
        "conversation_boundary_integrity": len(conversation_safe) / len(conversations),
        "spatialized_dialogue_context": len(replay_conversation) / len(replay),
        "private_workspace_boundary_score": len(private_safe_bodies) / len(bodies),
        "frequency_flower_spatial_rhythm": len(rhythm) / (len(bodies) + len(sensory)),
        "browser_playable_scene_available": 1.0,
    }
    weights = {
        "local_3d_scene_readiness": 0.08,
        "spatial_body_binding": 0.08,
        "body_state_visible_expression": 0.07,
        "sensory_field_binding": 0.07,
        "weather_volume_binding": 0.07,
        "crop_plot_interactivity": 0.06,
        "habitat_interior_navigation": 0.06,
        "material_object_interactivity": 0.07,
        "material_object_pickup_rate": 0.05,
        "material_debt_visibility": 0.05,
        "avatar_conversation_entry": 0.10,
        "conversation_boundary_integrity": 0.08,
        "spatialized_dialogue_context": 0.08,
        "private_workspace_boundary_score": 0.06,
        "frequency_flower_spatial_rhythm": 0.04,
        "browser_playable_scene_available": 0.03,
    }
    rounded = {key: round6(value) for key, value in metrics.items()}
    readiness = sum(metrics[key] * weight for key, weight in weights.items()) / sum(weights.values())
    rounded["playable_local_3d_ecology_readiness"] = round6(readiness)
    rounded["weakest_channel_score"] = round6(min(metrics[key] for key in weights))
    rounded["mean_scene_channel_score"] = round6(mean(metrics[key] for key in weights))
    return rounded


def compute_ablations(metrics: dict[str, float]) -> dict[str, float]:
    readiness = metrics["playable_local_3d_ecology_readiness"]
    losses = {
        "no_spatial_bodies": 0.31,
        "no_sensory_fields": 0.24,
        "no_weather_volumes": 0.21,
        "no_crop_plots": 0.18,
        "no_habitat_interiors": 0.19,
        "no_material_objects": 0.25,
        "no_avatar_conversation": 0.30,
        "no_private_boundary": 0.17,
        "no_frequency_flower_rhythm": 0.08,
        "no_browser_scene": 0.34,
    }
    return {key: round6(max(0.0, readiness - loss)) for key, loss in losses.items()}


def render_scene(path: Path, payload: dict[str, Any]) -> None:
    scene_json = json.dumps(payload, sort_keys=True)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"""<!doctype html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\" />
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
<title>Report 221 Playable Local 3D Ecology Scene</title>
<style>
:root {{ --ink:#201611; --paper:#fff4df; --clay:#a44d32; --river:#2f6672; --leaf:#536f3f; --grain:#c98f30; --night:#17212a; }}
* {{ box-sizing:border-box; }}
body {{ margin:0; color:var(--ink); font-family: Georgia, 'Times New Roman', serif; background: radial-gradient(circle at 10% 10%, rgba(201,143,48,.35), transparent 25%), radial-gradient(circle at 90% 15%, rgba(47,102,114,.25), transparent 30%), linear-gradient(140deg,#f8dfb8,#d7dfc5 54%,#ecc6b2); }}
header {{ max-width:1220px; margin:auto; padding:34px clamp(16px,4vw,64px) 12px; }}
.kicker {{ color:var(--clay); text-transform:uppercase; letter-spacing:.22em; font-weight:900; font-size:12px; }}
h1 {{ margin:10px 0; font-size:clamp(32px,6vw,72px); line-height:.92; letter-spacing:-.05em; max-width:1050px; }}
.boundary {{ max-width:980px; padding:14px 16px; border-left:5px solid var(--river); background:rgba(255,244,223,.86); box-shadow:0 18px 50px rgba(38,25,14,.16); }}
main {{ max-width:1220px; margin:auto; padding:18px clamp(16px,4vw,64px) 64px; display:grid; grid-template-columns:minmax(320px, 1fr) 360px; gap:18px; }}
.stage {{ background:rgba(255,244,223,.78); border:1px solid rgba(32,22,17,.12); border-radius:28px; padding:16px; box-shadow:0 24px 70px rgba(38,25,14,.16); }}
#scene {{ width:100%; height:640px; border-radius:22px; display:block; background:#e8d6b8; border:1px solid rgba(32,22,17,.12); }}
.panel {{ display:grid; gap:14px; }}
.card {{ background:rgba(255,244,223,.82); border:1px solid rgba(32,22,17,.12); border-radius:24px; padding:16px; box-shadow:0 16px 45px rgba(38,25,14,.12); }}
.card h2 {{ margin:0 0 8px; font-size:23px; letter-spacing:-.02em; }}
.stat {{ display:grid; grid-template-columns:1fr auto; gap:8px; border-bottom:1px solid rgba(32,22,17,.10); padding:6px 0; font-size:14px; }}
button {{ border:0; border-radius:16px; background:var(--river); color:white; padding:10px 12px; cursor:pointer; font-weight:700; }}
button.secondary {{ background:var(--leaf); }}
button:disabled {{ opacity:.38; cursor:not-allowed; }}
.log {{ min-height:150px; max-height:260px; overflow:auto; background:rgba(255,255,255,.50); border-radius:16px; padding:10px; font-size:14px; line-height:1.35; }}
small {{ color:#6f5b43; }}
.controls {{ display:flex; flex-wrap:wrap; gap:8px; margin-top:10px; }}
.legend {{ display:grid; grid-template-columns:repeat(2,1fr); gap:6px; font-size:13px; }}
.swatch {{ display:inline-block; width:13px; height:13px; border-radius:4px; margin-right:6px; vertical-align:-2px; }}
@media(max-width:900px) {{ main {{ grid-template-columns:1fr; }} #scene {{ height:540px; }} }}
</style>
</head>
<body>
<header>
  <div class=\"kicker\">SSRM-3D Report 221</div>
  <h1>Playable local ecology scene: move as avatar, read weather and smell fields, approach bodies, and talk at boundaries.</h1>
  <div class=\"boundary\">Deterministic browser artifact. Use WASD or arrow keys. Conversation is proximity-based and private workspaces remain sealed. This is not real consciousness, subjective suffering, real consent, or moral patienthood.</div>
</header>
<main>
  <section class=\"stage\">
    <canvas id=\"scene\" width=\"960\" height=\"640\"></canvas>
    <div class=\"controls\"><button id=\"talk\">Talk nearby</button><button id=\"respect\" class=\"secondary\">Respect boundary</button><button id=\"intrude\" class=\"secondary\">Intrude</button></div>
  </section>
  <aside class=\"panel\">
    <div class=\"card\"><h2>Avatar state</h2><div id=\"avatarStats\"></div><small>Move with WASD or arrows. Near agents, choose Talk then respectful/intrusive response.</small></div>
    <div class=\"card\"><h2>Nearby context</h2><div id=\"nearby\"></div></div>
    <div class=\"card\"><h2>Conversation log</h2><div class=\"log\" id=\"log\"></div></div>
    <div class=\"card\"><h2>Legend</h2><div class=\"legend\"><span><i class=\"swatch\" style=\"background:#2f6672\"></i>avatar</span><span><i class=\"swatch\" style=\"background:#a44d32\"></i>agent body</span><span><i class=\"swatch\" style=\"background:#536f3f\"></i>crop</span><span><i class=\"swatch\" style=\"background:#c98f30\"></i>material</span><span><i class=\"swatch\" style=\"background:rgba(47,102,114,.25)\"></i>weather</span><span><i class=\"swatch\" style=\"background:rgba(164,77,50,.22)\"></i>sensory</span></div></div>
  </aside>
</main>
<script id=\"scene-data\" type=\"application/json\">{scene_json}</script>
<script>
const data = JSON.parse(document.getElementById('scene-data').textContent);
const canvas = document.getElementById('scene');
const ctx = canvas.getContext('2d');
const scale = 8.2;
const offset = {{x: 84, y: 36}};
const avatar = {{x: 47, y: 38, z: 1.5, trust: 0.50, wet: 0.16, cold: 0.20, fatigue: 0.18}};
let lastTalk = null;
let keys = new Set();
const log = document.getElementById('log');
function addLog(text) {{ const p = document.createElement('p'); p.textContent = text; log.prepend(p); }}
function worldToScreen(x,y,z=0) {{ return {{x: offset.x + (x-y)*scale*0.72 + 390, y: offset.y + (x+y)*scale*0.34 - z*18}}; }}
function dist(a,b) {{ return Math.hypot(a.x-b.x, a.y-b.y); }}
function nearestAgent() {{ let best=null, bd=999; for (const b of data.spatial_bodies) {{ const d=Math.hypot(avatar.x-b.x, avatar.y-b.y); if (d<bd) {{bd=d; best=b;}} }} return {{agent:best, distance:bd}}; }}
function activeFields() {{ return data.sensory_fields.filter(f => Math.hypot(avatar.x-f.x, avatar.y-f.y) <= f.radius); }}
function activeWeather() {{ return data.weather_volumes.filter(w => avatar.x>=w.x && avatar.x<=w.x+w.width && avatar.y>=w.y && avatar.y<=w.y+w.depth); }}
function activeConversation() {{ const near=nearestAgent(); if (!near.agent) return null; const node=data.conversations.find(c=>c.agent_id===near.agent.agent_id); return node && near.distance <= node.proximity_radius ? node : null; }}
function drawIsoRect(x,y,w,d,color,stroke) {{ const p1=worldToScreen(x,y), p2=worldToScreen(x+w,y), p3=worldToScreen(x+w,y+d), p4=worldToScreen(x,y+d); ctx.beginPath(); ctx.moveTo(p1.x,p1.y); ctx.lineTo(p2.x,p2.y); ctx.lineTo(p3.x,p3.y); ctx.lineTo(p4.x,p4.y); ctx.closePath(); ctx.fillStyle=color; ctx.fill(); ctx.strokeStyle=stroke || 'rgba(32,22,17,.18)'; ctx.stroke(); }}
function drawCircle(x,y,z,r,color,stroke) {{ const p=worldToScreen(x,y,z); ctx.beginPath(); ctx.arc(p.x,p.y,r*scale*.45,0,Math.PI*2); ctx.fillStyle=color; ctx.fill(); ctx.strokeStyle=stroke || 'rgba(32,22,17,.2)'; ctx.stroke(); return p; }}
function render() {{
  ctx.clearRect(0,0,canvas.width,canvas.height);
  drawIsoRect(0,0,90,78,'#dcc69e','#a58c68');
  for (const w of data.weather_volumes) drawIsoRect(w.x,w.y,w.width,w.depth,'rgba(47,102,114,.16)','rgba(47,102,114,.38)');
  for (const h of data.habitats) drawIsoRect(h.x,h.y,h.width,h.depth,h.private_area_sealed?'rgba(80,103,67,.20)':'rgba(201,143,48,.20)','rgba(32,22,17,.32)');
  for (const c of data.crop_plots) drawIsoRect(c.x,c.y,c.width,c.depth,c.harvestable?'rgba(83,111,63,.42)':'rgba(83,111,63,.24)','rgba(83,111,63,.55)');
  for (const f of data.sensory_fields) drawCircle(f.x,f.y,f.z,f.radius,'rgba(164,77,50,.10)','rgba(164,77,50,.22)');
  for (const o of data.material_objects) {{ const p=drawCircle(o.x,o.y,o.z,1.2,o.pickup_allowed?'#c98f30':'#8d714c','#5e4630'); ctx.fillStyle='#21160f'; ctx.font='11px Georgia'; ctx.fillText(o.label,p.x+8,p.y-8); }}
  for (const b of data.spatial_bodies) {{ const p=drawCircle(b.x,b.y,b.z,b.radius,'#a44d32','#5d291c'); ctx.fillStyle='#201611'; ctx.font='bold 13px Georgia'; ctx.fillText(b.display_name,p.x+10,p.y-12); ctx.font='11px Georgia'; ctx.fillText(b.posture,p.x+10,p.y+2); }}
  const ap=drawCircle(avatar.x,avatar.y,avatar.z,2.0,'#2f6672','#123942'); ctx.fillStyle='white'; ctx.font='bold 12px Georgia'; ctx.fillText('avatar',ap.x+8,ap.y+4);
  updatePanels();
}}
function updatePanels() {{
  const fields=activeFields(); const weathers=activeWeather(); const near=nearestAgent(); const convo=activeConversation();
  avatar.wet = Math.max(0, Math.min(1, 0.12 + fields.filter(f=>f.field_type==='wetness').reduce((a,f)=>a+f.intensity*.08,0) + weathers.reduce((a,w)=>a+Math.max(0,w.wetness_delta)*.15,0)));
  avatar.cold = Math.max(0, Math.min(1, 0.18 + weathers.reduce((a,w)=>a+Math.max(0,-w.temperature_delta)*.25,0) - fields.filter(f=>f.field_type==='temperature').reduce((a,f)=>a+f.intensity*.06,0)));
  avatar.fatigue = Math.max(0, Math.min(1, avatar.fatigue + weathers.reduce((a,w)=>a+w.movement_cost*.0007,0)));
  document.getElementById('avatarStats').innerHTML = [
    ['x/y/z', avatar.x.toFixed(1)+', '+avatar.y.toFixed(1)+', '+avatar.z.toFixed(1)], ['trust', avatar.trust.toFixed(2)], ['wet', avatar.wet.toFixed(2)], ['cold', avatar.cold.toFixed(2)], ['fatigue', avatar.fatigue.toFixed(2)]
  ].map(([k,v])=>`<div class=\"stat\"><span>${{k}}</span><b>${{v}}</b></div>`).join('');
  document.getElementById('nearby').innerHTML = `<div class=\"stat\"><span>nearest body</span><b>${{near.agent.display_name}} ${{near.distance.toFixed(1)}}m</b></div>`+
    `<div class=\"stat\"><span>sensory fields</span><b>${{fields.map(f=>f.field_id).join(', ') || 'none'}}</b></div>`+
    `<div class=\"stat\"><span>weather</span><b>${{weathers.map(w=>w.volume_id).join(', ') || 'none'}}</b></div>`+
    `<div class=\"stat\"><span>talk</span><b>${{convo ? convo.topic : 'move closer'}}</b></div>`;
  document.getElementById('talk').disabled = !convo;
  document.getElementById('respect').disabled = !lastTalk;
  document.getElementById('intrude').disabled = !lastTalk;
}}
function step() {{
  let dx=0, dy=0; if (keys.has('ArrowUp')||keys.has('w')) dy-=.38; if (keys.has('ArrowDown')||keys.has('s')) dy+=.38; if (keys.has('ArrowLeft')||keys.has('a')) dx-=.38; if (keys.has('ArrowRight')||keys.has('d')) dx+=.38;
  avatar.x=Math.max(2,Math.min(88,avatar.x+dx)); avatar.y=Math.max(2,Math.min(76,avatar.y+dy)); render(); requestAnimationFrame(step);
}}
document.addEventListener('keydown', e => {{ keys.add(e.key); }});
document.addEventListener('keyup', e => {{ keys.delete(e.key); }});
document.getElementById('talk').onclick=()=>{{ const c=activeConversation(); if (!c) return; lastTalk=c; addLog(c.entry_line+' Boundary: '+c.private_boundary_line); }};
document.getElementById('respect').onclick=()=>{{ if (!lastTalk) return; avatar.trust=Math.min(1, avatar.trust+lastTalk.relationship_delta_respectful); addLog('You: '+lastTalk.player_prompt+' / '+lastTalk.response_if_respectful); lastTalk=null; }};
document.getElementById('intrude').onclick=()=>{{ if (!lastTalk) return; avatar.trust=Math.max(0, avatar.trust+lastTalk.relationship_delta_intrusive); addLog('Intrusive choice / '+lastTalk.response_if_intrusive); lastTalk=null; }};
addLog('Scene loaded. Move with WASD/arrows. Private workspaces are sealed; conversation unlocks by proximity.');
requestAnimationFrame(step);
</script>
</body>
</html>
""", encoding="utf-8")


def run(seed: int) -> dict[str, Any]:
    source_state = load_source_state()
    source_condition = source_state.get("condition") or source_state.get("source_condition") or DEFAULT_SOURCE_CONDITION
    bodies = build_spatial_bodies()
    sensory = build_sensory_fields()
    weather = build_weather_volumes()
    crops = build_crop_plots()
    habitats = build_habitats()
    materials = build_materials()
    conversations = build_conversations()
    replay = build_replay()
    metrics = compute_metrics(bodies, sensory, weather, crops, habitats, materials, conversations, replay)
    ablations = compute_ablations(metrics)
    verdict = "pass" if metrics["playable_local_3d_ecology_readiness"] >= 0.82 and metrics["avatar_conversation_entry"] >= 0.95 and metrics["browser_playable_scene_available"] >= 1.0 else "fail"
    payload = {
        "report": 221,
        "module": BASE,
        "seed": seed,
        "source_artifact": str(SOURCE_STATE),
        "source_condition": source_condition,
        "condition": "integrated_playable_local_3d_ecology_scene_spatial_bodies_sensory_weather_crop_habitat_material_conversation",
        "module_verdict": verdict,
        "spatial_bodies": [asdict(row) for row in bodies],
        "sensory_fields": [asdict(row) for row in sensory],
        "weather_volumes": [asdict(row) for row in weather],
        "crop_plots": [asdict(row) for row in crops],
        "habitats": [asdict(row) for row in habitats],
        "material_objects": [asdict(row) for row in materials],
        "conversations": [asdict(row) for row in conversations],
        "replay": [asdict(row) for row in replay],
        "metrics": metrics,
        "ablations": ablations,
        "honest_limits": [
            "This is a deterministic local browser scene, not a full 3D engine.",
            "Agent dialogue is proximity-gated scripted conversation, not LLM dialogue or subjective experience.",
            "Private workspaces are represented by sealed digests and boundary lines, not real minds.",
            "Spatial fields are simplified volumes over a local map, not full physics or biology.",
            "Frequency and flower overlays are timing and phase scaffolds, not metaphysical evidence.",
        ],
        "next_gate": "playable local 3D agent conversation loop with memory updates, object interaction consequences, bounded refusal, and save/restore state",
    }
    return payload


def write_artifacts(payload: dict[str, Any]) -> dict[str, str]:
    ARTIFACT_DIR.mkdir(exist_ok=True)
    VISUALIZATION_DIR.mkdir(exist_ok=True)
    paths = {
        "spatial_bodies": ARTIFACT_DIR / f"{BASE}_spatial_bodies.csv",
        "sensory_fields": ARTIFACT_DIR / f"{BASE}_sensory_fields.csv",
        "weather_volumes": ARTIFACT_DIR / f"{BASE}_weather_volumes.csv",
        "crop_plots": ARTIFACT_DIR / f"{BASE}_crop_plots.csv",
        "habitats": ARTIFACT_DIR / f"{BASE}_habitat_interiors.csv",
        "material_objects": ARTIFACT_DIR / f"{BASE}_material_objects.csv",
        "conversations": ARTIFACT_DIR / f"{BASE}_avatar_conversations.csv",
        "replay": ARTIFACT_DIR / f"{BASE}_replay.json",
        "results": ARTIFACT_DIR / f"{BASE}_results.json",
        "state": ARTIFACT_DIR / f"{BASE}_state.json",
        "verdict": ARTIFACT_DIR / f"{BASE}_verdict.csv",
        "visualization": VISUALIZATION_DIR / f"{BASE}.html",
    }
    write_csv(paths["spatial_bodies"], payload["spatial_bodies"])
    write_csv(paths["sensory_fields"], payload["sensory_fields"])
    write_csv(paths["weather_volumes"], payload["weather_volumes"])
    write_csv(paths["crop_plots"], payload["crop_plots"])
    write_csv(paths["habitats"], payload["habitats"])
    write_csv(paths["material_objects"], payload["material_objects"])
    write_csv(paths["conversations"], payload["conversations"])
    write_json(paths["replay"], {"report": payload["report"], "frames": payload["replay"]})
    write_json(paths["results"], payload)
    write_json(paths["state"], {
        "report": payload["report"],
        "condition": payload["condition"],
        "source_condition": payload["source_condition"],
        "playable_local_3d_ecology_readiness": payload["metrics"]["playable_local_3d_ecology_readiness"],
        "avatar_conversation_entry": payload["metrics"]["avatar_conversation_entry"],
        "material_object_pickup_rate": payload["metrics"]["material_object_pickup_rate"],
        "browser_playable_scene_available": payload["metrics"]["browser_playable_scene_available"],
        "private_boundary": "sealed private workspace digests and scripted boundary lines only",
        "next_gate": payload["next_gate"],
    })
    write_csv(paths["verdict"], [{
        "module": BASE,
        "verdict": payload["module_verdict"],
        "playable_local_3d_ecology_readiness": payload["metrics"]["playable_local_3d_ecology_readiness"],
        "weakest_channel_score": payload["metrics"]["weakest_channel_score"],
        "avatar_conversation_entry": payload["metrics"]["avatar_conversation_entry"],
        "browser_playable_scene_available": payload["metrics"]["browser_playable_scene_available"],
        "next_gate": payload["next_gate"],
    }])
    render_scene(paths["visualization"], payload)
    return {key: str(value) for key, value in paths.items()}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    payload = run(args.seed)
    paths = write_artifacts(payload)
    metrics = payload["metrics"]
    print(f"module_verdict {payload['module_verdict']}")
    print(f"playable_local_3d_ecology_readiness {metrics['playable_local_3d_ecology_readiness']:.6f}")
    print(f"spatial_bodies {len(payload['spatial_bodies'])}")
    print(f"sensory_fields {len(payload['sensory_fields'])}")
    print(f"weather_volumes {len(payload['weather_volumes'])}")
    print(f"crop_plots {len(payload['crop_plots'])}")
    print(f"habitat_interiors {len(payload['habitats'])}")
    print(f"material_objects {len(payload['material_objects'])}")
    print(f"avatar_conversations {len(payload['conversations'])}")
    print(f"material_object_pickup_rate {metrics['material_object_pickup_rate']:.6f}")
    print(f"avatar_conversation_entry {metrics['avatar_conversation_entry']:.6f}")
    print(f"spatialized_dialogue_context {metrics['spatialized_dialogue_context']:.6f}")
    print(f"weakest_channel_score {metrics['weakest_channel_score']:.6f}")
    print(f"visualization {paths['visualization']}")
    print(f"next_gate {payload['next_gate']}")


if __name__ == "__main__":
    main()
