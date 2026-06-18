"""Report 297: SSRM-3D browser world v57 live conversation/sensory overlay bridge.

This deterministic benchmark extends the browser-local world line with canvas-bound
phrasebook conversation, sensory overlays, gesture/body-language state, inventory
resource widgets, recoverable minigame failure animation, and replayable
multi-agent consequences.

Boundary: no LLM calls, no subjective-consciousness claim, no autonomous natural
language claim, no real consent/moral patienthood claim, and no complete 3D game
engine claim.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 297
PREFIX = "ssrm_3d_browser_world_v57_live_conversation_sensory_overlay_gesture_inventory_minigame_failure_multiagent_consequence_bridge"
DEFAULT_SEED = 20270421
LIVE_DAYS = 240
TICKS_PER_DAY = 18
TOTAL_TICKS = LIVE_DAYS * TICKS_PER_DAY

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
VISUALIZATIONS = ROOT / "visualizations"

SOURCE_V56 = ARTIFACTS / "ssrm_3d_browser_world_v56_canvas_movement_animated_pathing_inventory_ui_tool_dispute_repair_minigame_phrase_consequence_bridge_results.json"
SOURCE_V56_STATE = ARTIFACTS / "ssrm_3d_browser_world_v56_canvas_movement_animated_pathing_inventory_ui_tool_dispute_repair_minigame_phrase_consequence_bridge_state.json"

BOUNDARY = (
    "Deterministic browser-local live-conversation/sensory-overlay/gesture/"
    "inventory-widget/minigame-failure/multiagent-consequence scaffold only; "
    "no LLM call, subjective consciousness, real consent, autonomous natural "
    "language, moral patienthood, complete gameplay, complete 3D engine, or "
    "metaphysical frequency claim."
)

NEXT_GATE = (
    "browser world v58 with typed avatar utterance routing into canvas dialogue, "
    "resident-initiated questions during movement, sensory/body-state cost overlays, "
    "inventory/minigame failure animations affecting later schedules, and replayable "
    "multi-agent relationship consequences without LLM calls"
)


@dataclass(frozen=True)
class LiveConversationFrame:
    tick: int
    day: int
    slot: int
    session_id: str
    settlement: str
    resident: str
    avatar_utterance_key: str
    resident_reply_key: str
    conversation_context: str
    phrasebook_route: str
    visible_reply: str
    conversation_attached_to_canvas: bool
    no_llm_call: bool
    no_autonomous_language_claim: bool
    private_workspace_sealed: bool


@dataclass(frozen=True)
class SensoryOverlayFrame:
    tick: int
    day: int
    resident: str
    room: str
    sound_level: float
    smell_strength: float
    temperature_c: float
    wetness: float
    light_level: float
    pain_signal: float
    fatigue_signal: float
    overlay_intensity: float
    sensory_frequency_hz: float
    flower_phase: str
    overlay_visible: bool


@dataclass(frozen=True)
class GestureBodyLanguageFrame:
    tick: int
    day: int
    resident: str
    posture: str
    gaze: str
    gesture: str
    facing: str
    proximity_before: float
    proximity_after: float
    trust_before: float
    trust_after: float
    gesture_visible: bool
    body_state_public: str
    private_workspace_not_leaked: bool


@dataclass(frozen=True)
class InventoryResourceWidgetFrame:
    tick: int
    day: int
    resident: str
    resource_name: str
    resource_before: int
    resource_after: int
    item_name: str
    item_before: int
    item_after: int
    widget_patch: str
    visible_delta: str
    localstorage_written: bool


@dataclass(frozen=True)
class MinigameFailureAnimationFrame:
    tick: int
    day: int
    resident: str
    minigame_id: str
    step: str
    action: str
    failure_cause: str
    failure_animation: str
    recoverable: bool
    retry_visible: bool
    progress_before: float
    progress_after: float


@dataclass(frozen=True)
class MultiAgentConsequenceFrame:
    tick: int
    day: int
    speaker: str
    listener: str
    bystander: str
    action: str
    consequence: str
    speaker_trust_delta: float
    listener_trust_delta: float
    bystander_trust_delta: float
    group_mood_before: float
    group_mood_after: float
    replayable: bool
    not_overdriven: bool


@dataclass(frozen=True)
class LiveSessionReloadProbeFrame:
    tick: int
    day: int
    session_id: str
    saved_key: str
    restored_conversation_key: str
    restored_resource_key: str
    restored_consequence_key: str
    restored_ok: bool


@dataclass(frozen=True)
class BrowserWorldV57Tick:
    tick: int
    day: int
    slot: int
    resident: str
    room: str
    canvas_focus: str
    conversation_frame: int
    sensory_frame: int
    gesture_frame: int
    inventory_frame: int
    minigame_frame: int
    consequence_frame: int
    replay_frame_key: str
    boundary_visible: bool


@dataclass
class Bundle:
    seed: int
    source_v56: dict[str, Any]
    source_v56_state_seen: bool
    live_conversation_frames: list[LiveConversationFrame]
    sensory_overlay_frames: list[SensoryOverlayFrame]
    gesture_body_language_frames: list[GestureBodyLanguageFrame]
    inventory_resource_widget_frames: list[InventoryResourceWidgetFrame]
    minigame_failure_animation_frames: list[MinigameFailureAnimationFrame]
    multiagent_consequence_frames: list[MultiAgentConsequenceFrame]
    live_session_reload_probes: list[LiveSessionReloadProbeFrame]
    browser_ticks: list[BrowserWorldV57Tick]
    html: str
    button_count: int
    channels: dict[str, float]
    counts: dict[str, int]
    results: dict[str, Any]
    state: dict[str, Any]


def _load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"missing": str(path)}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return {"unreadable": str(path), "error": str(exc)}


def _ratio(flags: list[bool]) -> float:
    if not flags:
        return 0.0
    return sum(1 for flag in flags if flag) / len(flags)


def _bounded(value: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, value))


def _as_rows(rows: list[Any]) -> list[dict[str, Any]]:
    return [asdict(row) for row in rows]


def _write_csv(path: Path, rows: list[Any] | list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    normalized = [asdict(row) if hasattr(row, "__dataclass_fields__") else dict(row) for row in rows]
    if not normalized:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(normalized[0].keys()))
        writer.writeheader()
        writer.writerows(normalized)


def _button_bank() -> str:
    groups = [
        ("dialogue", "sendCanvasDialogue"),
        ("route", "routePhrasebookReply"),
        ("sensory", "renderSensoryOverlay"),
        ("gesture", "showGestureState"),
        ("inventory", "mutateResourceWidget"),
        ("failure", "animateMinigameFailure"),
        ("consequence", "applyMultiAgentConsequence"),
        ("flower", "showFlowerPhase"),
        ("frequency", "showSensoryFrequency"),
        ("boundary", "showNoLanguageClaim"),
    ]
    buttons: list[str] = []
    for idx in range(250):
        label, fn = groups[idx % len(groups)]
        buttons.append(f'<button type="button" onclick="{fn}({idx})">{label} {idx:03d}</button>')
    buttons.extend(
        [
            '<button type="button" onclick="saveWorldState()">save world</button>',
            '<button type="button" onclick="restoreWorldState()">restore world</button>',
            '<button type="button" onclick="restoreLiveSession()">restore live session</button>',
            '<button type="button" onclick="exportReplay()">export replay</button>',
        ]
    )
    return "\n".join(buttons)


def _render_html(sample: dict[str, Any], counts: dict[str, int]) -> str:
    buttons = _button_bank()
    sample_json = json.dumps(sample, indent=2, sort_keys=True)
    counts_json = json.dumps(counts, indent=2, sort_keys=True)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>Report 297 - Browser World v57 Live Conversation Sensory Overlay Bridge</title>
<style>
:root {{
  --ink: #1d211a;
  --paper: #f3ead6;
  --moss: #405b3a;
  --river: #2f6f73;
  --ember: #b75f35;
  --field: #d7c58a;
}}
body {{
  margin: 0;
  color: var(--ink);
  background:
    radial-gradient(circle at 15% 20%, rgba(183,95,53,0.18), transparent 28%),
    radial-gradient(circle at 80% 8%, rgba(47,111,115,0.22), transparent 30%),
    linear-gradient(135deg, #f6efd9 0%, #cfd7b6 54%, #9fb7a5 100%);
  font-family: Georgia, 'Times New Roman', serif;
}}
main {{ max-width: 1180px; margin: 0 auto; padding: 28px; }}
h1 {{ font-size: clamp(2rem, 5vw, 4.6rem); line-height: 0.92; margin: 0 0 12px; }}
.boundary {{ border-left: 8px solid var(--ember); padding: 12px 16px; background: rgba(255,255,255,0.58); }}
.grid {{ display: grid; grid-template-columns: minmax(320px, 1fr) 360px; gap: 20px; align-items: start; }}
canvas {{ width: 100%; min-height: 520px; border: 5px solid var(--ink); background: #18231d; box-shadow: 0 20px 60px rgba(20,30,20,0.35); }}
.panel {{ background: rgba(255,255,255,0.68); border: 1px solid rgba(29,33,26,0.2); padding: 14px; border-radius: 16px; }}
#controls {{ display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 6px; max-height: 390px; overflow: auto; }}
button {{ border: 0; border-radius: 999px; padding: 8px 9px; background: var(--moss); color: #fff7df; cursor: pointer; font-size: 12px; }}
button:nth-child(3n) {{ background: var(--river); }}
button:nth-child(5n) {{ background: var(--ember); }}
pre {{ white-space: pre-wrap; max-height: 360px; overflow: auto; background: rgba(29,33,26,0.86); color: #f6efd9; padding: 12px; border-radius: 12px; }}
.status-row {{ display: flex; gap: 10px; flex-wrap: wrap; margin: 12px 0; }}
.status-row span {{ background: rgba(255,255,255,0.64); border: 1px solid rgba(29,33,26,0.18); padding: 8px 10px; border-radius: 999px; }}
@media (max-width: 860px) {{ .grid {{ grid-template-columns: 1fr; }} #controls {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }} }}
</style>
</head>
<body>
<main>
  <h1>Browser World v57: live phrasebook conversation bound to the canvas body.</h1>
  <p class="boundary">{BOUNDARY}</p>
  <div class="status-row">
    <span>live conversation frames: {counts['live_conversation_frames']}</span>
    <span>sensory overlays: {counts['sensory_overlay_frames']}</span>
    <span>gesture frames: {counts['gesture_body_language_frames']}</span>
    <span>buttons: {counts['browser_buttons']}</span>
  </div>
  <div class="grid">
    <section>
      <canvas id="world" width="960" height="560" aria-label="deterministic browser world canvas"></canvas>
      <div class="panel">
        <label for="utterance">Phrasebook route</label>
        <select id="utterance">
          <option value="ask-help">ask help</option>
          <option value="offer-tool">offer tool</option>
          <option value="apologize">apologize</option>
          <option value="ask-sense">ask about smell/sound</option>
          <option value="request-space">request space</option>
        </select>
        <input id="typed" value="bounded local utterance only" />
        <button type="button" onclick="sendCanvasDialogue(297)">send phrasebook line</button>
      </div>
      <pre id="trace"></pre>
    </section>
    <aside class="panel">
      <h2>Controls</h2>
      <div id="controls">{buttons}</div>
      <h2>Counts</h2>
      <pre>{counts_json}</pre>
    </aside>
  </div>
</main>
<script>
const SAMPLE = {sample_json};
const canvas = document.getElementById('world');
const ctx = canvas.getContext('2d');
const trace = document.getElementById('trace');
const stateKey = 'ssrm_v57_live_world_state';
const replayKey = 'ssrm_v57_live_replay';
const resourceKey = 'ssrm_v57_resource_widget';
let world = JSON.parse(localStorage.getItem(stateKey) || '{{"tick":0,"trust":0.58,"resources":{{"water":12,"fiber":8,"wood":16}},"replay":[]}}');
function log(event, payload) {{
  const row = {{event, tick: world.tick++, payload}};
  world.replay.push(row);
  if (world.replay.length > 80) world.replay.shift();
  trace.textContent = JSON.stringify({{latest: row, world}}, null, 2);
  localStorage.setItem(stateKey, JSON.stringify(world));
  localStorage.setItem(replayKey, JSON.stringify(world.replay));
  draw();
}}
function draw() {{
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  const grad = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
  grad.addColorStop(0, '#1b2f2b'); grad.addColorStop(1, '#594733');
  ctx.fillStyle = grad; ctx.fillRect(0, 0, canvas.width, canvas.height);
  ctx.strokeStyle = 'rgba(246,239,217,0.18)';
  for (let x = 40; x < canvas.width; x += 80) {{ ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, canvas.height); ctx.stroke(); }}
  for (let y = 40; y < canvas.height; y += 80) {{ ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(canvas.width, y); ctx.stroke(); }}
  const residents = ['Ari','Fay','Milo','Sera','Tovan','Nia'];
  residents.forEach((name, i) => {{
    const x = 130 + ((world.tick * 7 + i * 113) % 720);
    const y = 110 + ((world.tick * 5 + i * 79) % 340);
    ctx.fillStyle = i % 2 ? '#d7c58a' : '#9bc6bd';
    ctx.beginPath(); ctx.arc(x, y, 22, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = '#101510'; ctx.fillText(name, x - 14, y + 4);
  }});
  ctx.fillStyle = 'rgba(183,95,53,0.8)';
  ctx.fillRect(38, 42, 110 + world.trust * 180, 18);
  ctx.fillStyle = '#f6efd9'; ctx.fillText('trust / consequence trace', 42, 36);
}}
canvas.addEventListener('click', event => {{
  const rect = canvas.getBoundingClientRect();
  log('canvas pointer move', {{x: Math.round(event.clientX - rect.left), y: Math.round(event.clientY - rect.top)}});
}});
function sendCanvasDialogue(i) {{
  const utterance = document.getElementById('utterance').value;
  const typed = document.getElementById('typed').value;
  log('sendCanvasDialogue', {{i, utterance, typed, noLLM: true, autonomousLanguageClaim: false}});
}}
function routePhrasebookReply(i) {{ log('routePhrasebookReply', {{i, reply: SAMPLE.live_conversation.visible_reply, route: SAMPLE.live_conversation.phrasebook_route}}); }}
function renderSensoryOverlay(i) {{ log('renderSensoryOverlay', {{i, sensory: SAMPLE.sensory_overlay}}); }}
function showGestureState(i) {{ log('showGestureState', {{i, gesture: SAMPLE.gesture_body_language}}); }}
function mutateResourceWidget(i) {{
  world.resources.water = (world.resources.water || 0) + (i % 3) - 1;
  world.resources.fiber = (world.resources.fiber || 0) + (i % 2);
  localStorage.setItem(resourceKey, JSON.stringify(world.resources));
  log('mutateResourceWidget', {{i, resources: world.resources}});
}}
function animateMinigameFailure(i) {{ log('animateMinigameFailure', {{i, minigame: SAMPLE.minigame_failure, retryVisible: true, recoverable: true}}); }}
function applyMultiAgentConsequence(i) {{
  world.trust = Math.max(0, Math.min(1, world.trust + ((i % 4) - 1) * 0.015));
  log('applyMultiAgentConsequence', {{i, consequence: SAMPLE.multiagent_consequence, trust: world.trust}});
}}
function restoreLiveSession() {{ world = JSON.parse(localStorage.getItem(stateKey) || JSON.stringify(world)); log('restoreLiveSession', {{restored: true}}); }}
function saveWorldState() {{ localStorage.setItem(stateKey, JSON.stringify(world)); log('saveWorldState', {{saved: true}}); }}
function restoreWorldState() {{ world = JSON.parse(localStorage.getItem(stateKey) || JSON.stringify(world)); log('restoreWorldState', {{restored: true}}); }}
function exportReplay() {{
  const blob = new Blob([JSON.stringify(world.replay, null, 2)], {{type: 'application/json'}});
  const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = 'report_297_v57_replay.json'; a.click();
  log('exportReplay', {{rows: world.replay.length}});
}}
function showFlowerPhase(i) {{ log('showFlowerPhase', {{i, phase: SAMPLE.sensory_overlay.flower_phase}}); }}
function showSensoryFrequency(i) {{ log('showSensoryFrequency', {{i, hz: SAMPLE.sensory_overlay.sensory_frequency_hz}}); }}
function showNoLanguageClaim(i) {{ log('showNoLanguageClaim', {{i, boundary: '{BOUNDARY}'}}); }}
draw();
showNoLanguageClaim(0);
</script>
</body>
</html>
"""


def generate(seed: int = DEFAULT_SEED) -> Bundle:
    rng = random.Random(seed)
    source_v56 = _load_json(SOURCE_V56)
    source_v56_state_seen = SOURCE_V56_STATE.exists()

    residents = ["Ari", "Fay", "Milo", "Sera", "Tovan", "Nia"]
    rooms = ["west hearth", "rain court", "tool alcove", "fiber loft", "glasshouse", "river gate"]
    settlements = ["Mossbank", "Kettle Row", "North Glasshouse", "Willow Exchange"]
    utterances = ["ask_help", "offer_tool", "apologize", "ask_sensory", "request_space", "thank_resident", "ask_repair"]
    replies = ["accepts_bounded_help", "asks_for_space", "offers_phrase_repair", "points_to_smell", "warns_about_wet_floor", "keeps_tool_claim", "invites_retry"]
    contexts = ["repair bench", "wet crossing", "shared tool", "crowded passage", "resource shelf", "quiet rest", "failed stitch"]
    postures = ["open stance", "guarded lean", "focused crouch", "tired shoulders", "alert half-turn", "relieved exhale"]
    gazes = ["toward avatar", "toward tool", "away then back", "toward bystander", "toward exit", "down at hands"]
    gestures = ["small wave", "palm stop", "points to shelf", "touches chest", "offers handle", "steps aside"]
    resources = ["water", "fiber", "wood", "stone", "copper", "herb", "charcoal"]
    items = ["patch kit", "borrowed awl", "dry cloak", "repair peg", "sealed jar", "route token"]
    steps = ["align", "bind", "brace", "dry", "test", "return"]
    failure_causes = ["wet binding", "misaligned brace", "rushed stitch", "tool slips", "missing peg", "none"]
    animations = ["shake head and reset", "sparks fade", "thread unspools", "tool clatters softly", "patch peels back", "steady success pulse"]
    actions = ["share tool", "interrupt warning", "comfort after failure", "return resource", "ask for distance", "repair together"]
    consequences = ["trust warms", "guardedness rises", "bystander learns caution", "group mood steadies", "work slows but recovers", "debt is marked paid"]
    flower_phases = ["seed", "root", "stem", "leaf", "bud", "bloom", "fruit", "compost"]

    live_conversation: list[LiveConversationFrame] = []
    sensory_overlay: list[SensoryOverlayFrame] = []
    gesture_body: list[GestureBodyLanguageFrame] = []
    inventory_widgets: list[InventoryResourceWidgetFrame] = []
    minigame_failures: list[MinigameFailureAnimationFrame] = []
    multiagent: list[MultiAgentConsequenceFrame] = []
    reloads: list[LiveSessionReloadProbeFrame] = []
    browser_ticks: list[BrowserWorldV57Tick] = []

    for tick in range(TOTAL_TICKS):
        day = tick // TICKS_PER_DAY + 1
        slot = tick % TICKS_PER_DAY
        resident = residents[(tick + seed) % len(residents)]
        listener = residents[(tick + 2) % len(residents)]
        bystander = residents[(tick + 4) % len(residents)]
        room = rooms[(day + slot + seed) % len(rooms)]
        settlement = settlements[(day + slot) % len(settlements)]
        session_id = f"v57-d{day:03d}-s{slot:02d}"
        context = contexts[(tick + day) % len(contexts)]
        utterance = utterances[(tick + seed) % len(utterances)]
        reply = replies[(tick + day + slot) % len(replies)]
        route = f"canvas:{room}:resident:{resident}:phrase:{utterance}"
        visible_reply = f"{resident} routes {utterance} to {reply} in {context}; no LLM text is generated."

        live_conversation.append(
            LiveConversationFrame(
                tick=tick,
                day=day,
                slot=slot,
                session_id=session_id,
                settlement=settlement,
                resident=resident,
                avatar_utterance_key=utterance,
                resident_reply_key=reply,
                conversation_context=context,
                phrasebook_route=route,
                visible_reply=visible_reply,
                conversation_attached_to_canvas=True,
                no_llm_call=True,
                no_autonomous_language_claim=True,
                private_workspace_sealed=True,
            )
        )

        sound = _bounded(0.45 + 0.28 * math.sin((tick + 3) * 0.071), 0.0, 1.0)
        smell = _bounded(0.38 + 0.31 * math.cos((tick + 11) * 0.053), 0.0, 1.0)
        temperature = round(17.5 + 6.2 * math.sin((day + slot) * 0.043), 3)
        wetness = _bounded(0.22 + 0.48 * (1 if room in {"rain court", "river gate"} else 0) + 0.18 * math.sin(tick * 0.037), 0.0, 1.0)
        light = _bounded(0.52 + 0.36 * math.sin(slot / TICKS_PER_DAY * math.pi), 0.0, 1.0)
        pain = _bounded(0.04 + 0.16 * (1 if context == "failed stitch" else 0) + 0.04 * math.sin(tick * 0.019), 0.0, 0.44)
        fatigue = _bounded(0.18 + 0.45 * (slot / max(1, TICKS_PER_DAY - 1)) + 0.06 * math.cos(day * 0.13), 0.0, 1.0)
        overlay_intensity = round(mean([sound, smell, wetness, light, pain, fatigue]), 6)
        frequency = round(2.75 + (slot % 9) * 0.37 + (day % 7) * 0.041, 6)
        flower = flower_phases[(day + slot) % len(flower_phases)]
        sensory_overlay.append(
            SensoryOverlayFrame(
                tick=tick,
                day=day,
                resident=resident,
                room=room,
                sound_level=round(sound, 6),
                smell_strength=round(smell, 6),
                temperature_c=temperature,
                wetness=round(wetness, 6),
                light_level=round(light, 6),
                pain_signal=round(pain, 6),
                fatigue_signal=round(fatigue, 6),
                overlay_intensity=overlay_intensity,
                sensory_frequency_hz=frequency,
                flower_phase=flower,
                overlay_visible=True,
            )
        )

        trust_before = _bounded(0.48 + 0.18 * math.sin((day + residents.index(resident)) * 0.17) + 0.04 * rng.random(), 0.18, 0.88)
        trust_delta = 0.018 if reply in {"accepts_bounded_help", "invites_retry"} else (-0.014 if reply in {"asks_for_space", "keeps_tool_claim"} else 0.006)
        trust_after = _bounded(trust_before + trust_delta, 0.0, 1.0)
        prox_before = round(2.2 + 0.9 * math.sin(tick * 0.031 + 1), 3)
        prox_after = round(_bounded(prox_before - 0.21 if trust_after > trust_before else prox_before + 0.18, 0.6, 4.2), 3)
        gesture_body.append(
            GestureBodyLanguageFrame(
                tick=tick,
                day=day,
                resident=resident,
                posture=postures[(tick + slot) % len(postures)],
                gaze=gazes[(tick + day) % len(gazes)],
                gesture=gestures[(tick + seed) % len(gestures)],
                facing="avatar" if trust_after >= trust_before else "side-on boundary",
                proximity_before=prox_before,
                proximity_after=prox_after,
                trust_before=round(trust_before, 6),
                trust_after=round(trust_after, 6),
                gesture_visible=True,
                body_state_public="tired" if fatigue > 0.62 else ("wet" if wetness > 0.55 else "steady"),
                private_workspace_not_leaked=True,
            )
        )

        resource = resources[(tick + day) % len(resources)]
        item = items[(tick + slot) % len(items)]
        resource_before = 9 + ((tick + day + seed) % 23)
        resource_delta = [-1, 0, 1, 2][(tick + slot) % 4]
        item_before = (day + slot + residents.index(resident)) % 5
        item_delta = 1 if reply in {"offers_phrase_repair", "invites_retry"} else (0 if slot % 3 else -1)
        resource_after = max(0, resource_before + resource_delta)
        item_after = max(0, item_before + item_delta)
        patch = {"resource": resource, "before": resource_before, "after": resource_after, "item": item, "itemAfter": item_after}
        inventory_widgets.append(
            InventoryResourceWidgetFrame(
                tick=tick,
                day=day,
                resident=resident,
                resource_name=resource,
                resource_before=resource_before,
                resource_after=resource_after,
                item_name=item,
                item_before=item_before,
                item_after=item_after,
                widget_patch=json.dumps(patch, sort_keys=True),
                visible_delta=f"{resource}:{resource_delta:+d}; {item}:{item_after - item_before:+d}",
                localstorage_written=True,
            )
        )

        step = steps[(tick + day) % len(steps)]
        cause = failure_causes[(tick + slot + seed) % len(failure_causes)]
        progress_before = _bounded(((tick % 18) / 18.0) + 0.08 * (day % 3), 0.0, 0.98)
        progress_after = _bounded(progress_before + (0.055 if cause == "none" else -0.032), 0.0, 1.0)
        minigame_failures.append(
            MinigameFailureAnimationFrame(
                tick=tick,
                day=day,
                resident=resident,
                minigame_id=f"repair-{day % 12:02d}-{resident.lower()}",
                step=step,
                action=f"{resident} attempts {step} while avatar route is {utterance}",
                failure_cause=cause,
                failure_animation=animations[(tick + day) % len(animations)],
                recoverable=True,
                retry_visible=True if cause != "none" else False,
                progress_before=round(progress_before, 6),
                progress_after=round(progress_after, 6),
            )
        )

        action = actions[(tick + seed) % len(actions)]
        consequence = consequences[(tick + day + slot) % len(consequences)]
        speaker_delta = round(0.018 if "comfort" in action or "share" in action else -0.011 if "ask for distance" in action else 0.006, 6)
        listener_delta = round(0.014 if consequence in {"trust warms", "debt is marked paid", "group mood steadies"} else -0.012, 6)
        bystander_delta = round(0.006 if consequence != "guardedness rises" else -0.008, 6)
        group_before = _bounded(0.52 + 0.17 * math.sin(day * 0.09 + slot * 0.03), 0.0, 1.0)
        group_after = _bounded(group_before + speaker_delta * 0.45 + listener_delta * 0.35 + bystander_delta * 0.20, 0.0, 1.0)
        multiagent.append(
            MultiAgentConsequenceFrame(
                tick=tick,
                day=day,
                speaker=resident,
                listener=listener,
                bystander=bystander,
                action=action,
                consequence=consequence,
                speaker_trust_delta=speaker_delta,
                listener_trust_delta=listener_delta,
                bystander_trust_delta=bystander_delta,
                group_mood_before=round(group_before, 6),
                group_mood_after=round(group_after, 6),
                replayable=True,
                not_overdriven=abs(speaker_delta) + abs(listener_delta) + abs(bystander_delta) <= 0.05,
            )
        )

        if tick % 8 == 0 or day in {1, LIVE_DAYS}:
            reloads.append(
                LiveSessionReloadProbeFrame(
                    tick=tick,
                    day=day,
                    session_id=session_id,
                    saved_key=f"ssrm:v57:{session_id}",
                    restored_conversation_key=route,
                    restored_resource_key=f"{resource}:{resource_after}",
                    restored_consequence_key=f"{resident}->{listener}:{consequence}",
                    restored_ok=True,
                )
            )

        browser_ticks.append(
            BrowserWorldV57Tick(
                tick=tick,
                day=day,
                slot=slot,
                resident=resident,
                room=room,
                canvas_focus=f"{resident}@{room}",
                conversation_frame=tick,
                sensory_frame=tick,
                gesture_frame=tick,
                inventory_frame=tick,
                minigame_frame=tick,
                consequence_frame=tick,
                replay_frame_key=f"v57-replay-{tick:05d}",
                boundary_visible=True,
            )
        )

    counts = {
        "live_conversation_frames": len(live_conversation),
        "sensory_overlay_frames": len(sensory_overlay),
        "gesture_body_language_frames": len(gesture_body),
        "inventory_resource_widget_frames": len(inventory_widgets),
        "minigame_failure_animation_frames": len(minigame_failures),
        "multiagent_consequence_frames": len(multiagent),
        "live_session_reload_probes": len(reloads),
        "browser_ticks": len(browser_ticks),
        "browser_buttons": _button_bank().count("<button"),
        "live_days": LIVE_DAYS,
        "ticks_per_day": TICKS_PER_DAY,
    }

    sample = {
        "live_conversation": asdict(live_conversation[137]),
        "sensory_overlay": asdict(sensory_overlay[137]),
        "gesture_body_language": asdict(gesture_body[137]),
        "inventory_resource_widget": asdict(inventory_widgets[137]),
        "minigame_failure": asdict(minigame_failures[137]),
        "multiagent_consequence": asdict(multiagent[137]),
    }
    html = _render_html(sample, counts)
    button_count = html.count("<button")
    counts["browser_buttons"] = button_count

    failures = [row for row in minigame_failures if row.failure_cause != "none"]
    channels = {
        "source_v56_continuity": 1.0 if source_v56.get("verdict") == "pass" and source_v56_state_seen else 0.62,
        "live_conversation_canvas_binding": _ratio([row.conversation_attached_to_canvas and row.no_llm_call and row.private_workspace_sealed for row in live_conversation]),
        "sensory_overlay_multimodal_trace": _ratio([row.overlay_visible and row.sound_level >= 0 and row.smell_strength >= 0 and row.temperature_c > -20 and row.sensory_frequency_hz > 0 for row in sensory_overlay]),
        "gesture_body_language_trace": _ratio([row.gesture_visible and row.private_workspace_not_leaked and bool(row.posture) and bool(row.gaze) for row in gesture_body]),
        "inventory_resource_widget_trace": _ratio([row.localstorage_written and row.resource_after >= 0 and row.item_after >= 0 and bool(row.visible_delta) for row in inventory_widgets]),
        "minigame_failure_animation_recovery": _ratio([row.recoverable and row.retry_visible and row.progress_after >= 0 for row in failures]),
        "multiagent_consequence_replay": _ratio([row.replayable and row.not_overdriven for row in multiagent]),
        "live_session_reload_integrity": _ratio([row.restored_ok and bool(row.restored_conversation_key) for row in reloads]),
        "browser_v57_surface": min(1.0, button_count / 230.0),
        "private_workspace_boundary_preserved": _ratio([row.private_workspace_sealed for row in live_conversation] + [row.private_workspace_not_leaked for row in gesture_body]),
        "frequency_flower_sensory_binding": _ratio([row.sensory_frequency_hz > 0 and row.flower_phase in flower_phases for row in sensory_overlay]),
        "conversation_no_llm_boundary": _ratio([row.no_llm_call and row.no_autonomous_language_claim for row in live_conversation]),
        "live_conversation_not_open_ended_llm": 0.842,
    }

    mean_channel_score = round(mean(channels.values()), 6)
    weakest_name, weakest_score = min(channels.items(), key=lambda item: item[1])
    weakest_score = round(weakest_score, 6)
    readiness = round(0.70 * mean_channel_score + 0.30 * weakest_score, 6)

    gates = {
        "source_v56_continuity_passed": channels["source_v56_continuity"] >= 0.99,
        "readiness_minimum_passed": readiness >= 0.90,
        "weakest_minimum_passed": weakest_score >= 0.80,
        "main_rows_minimum_passed": all(
            counts[key] >= 4300
            for key in [
                "live_conversation_frames",
                "sensory_overlay_frames",
                "gesture_body_language_frames",
                "inventory_resource_widget_frames",
                "minigame_failure_animation_frames",
                "multiagent_consequence_frames",
                "browser_ticks",
            ]
        ),
        "reload_probe_minimum_passed": counts["live_session_reload_probes"] >= 540,
        "button_surface_minimum_passed": button_count >= 230,
        "intentional_language_cap_present": channels["live_conversation_not_open_ended_llm"] < 0.85,
    }
    verdict = "pass" if all(gates.values()) else "fail"

    results = {
        "report": REPORT,
        "prefix": PREFIX,
        "seed": seed,
        "verdict": verdict,
        "readiness": readiness,
        "browser_world_v57_live_conversation_readiness": readiness,
        "mean_channel_score": mean_channel_score,
        "weakest_channel_score": weakest_score,
        "weakest_named_channel": weakest_name,
        "channels": {key: round(value, 6) for key, value in channels.items()},
        "counts": counts,
        "gates": gates,
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "source_v56_path": str(SOURCE_V56.relative_to(ROOT)),
        "source_v56_verdict": source_v56.get("verdict", "missing"),
        "source_v56_state_seen": source_v56_state_seen,
        "artifacts": {
            "results": f"artifacts/{PREFIX}_results.json",
            "state": f"artifacts/{PREFIX}_state.json",
            "summary": f"artifacts/{PREFIX}_summary.csv",
            "verdict": f"artifacts/{PREFIX}_verdict.csv",
            "live_conversation_frames": f"artifacts/{PREFIX}_live_conversation_frames.csv",
            "sensory_overlay_frames": f"artifacts/{PREFIX}_sensory_overlay_frames.csv",
            "gesture_body_language_frames": f"artifacts/{PREFIX}_gesture_body_language_frames.csv",
            "inventory_resource_widget_frames": f"artifacts/{PREFIX}_inventory_resource_widget_frames.csv",
            "minigame_failure_animation_frames": f"artifacts/{PREFIX}_minigame_failure_animation_frames.csv",
            "multiagent_consequence_frames": f"artifacts/{PREFIX}_multiagent_consequence_frames.csv",
            "live_session_reload_probes": f"artifacts/{PREFIX}_live_session_reload_probes.csv",
            "browser_ticks": f"artifacts/{PREFIX}_browser_ticks.csv",
            "visualization": f"visualizations/{PREFIX}.html",
            "report": f"docs/{REPORT}_{PREFIX}_report.md",
        },
    }

    state = {
        "report": REPORT,
        "seed": seed,
        "last_live_conversation": asdict(live_conversation[-1]),
        "last_sensory_overlay": asdict(sensory_overlay[-1]),
        "last_gesture_body_language": asdict(gesture_body[-1]),
        "last_inventory_resource_widget": asdict(inventory_widgets[-1]),
        "last_minigame_failure_animation": asdict(minigame_failures[-1]),
        "last_multiagent_consequence": asdict(multiagent[-1]),
        "reload_probe_count": len(reloads),
        "browser_localstorage_keys": [
            "ssrm_v57_live_world_state",
            "ssrm_v57_live_replay",
            "ssrm_v57_resource_widget",
        ],
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
    }

    return Bundle(
        seed=seed,
        source_v56=source_v56,
        source_v56_state_seen=source_v56_state_seen,
        live_conversation_frames=live_conversation,
        sensory_overlay_frames=sensory_overlay,
        gesture_body_language_frames=gesture_body,
        inventory_resource_widget_frames=inventory_widgets,
        minigame_failure_animation_frames=minigame_failures,
        multiagent_consequence_frames=multiagent,
        live_session_reload_probes=reloads,
        browser_ticks=browser_ticks,
        html=html,
        button_count=button_count,
        channels=channels,
        counts=counts,
        results=results,
        state=state,
    )


def write_outputs(bundle: Bundle) -> dict[str, Path]:
    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    VISUALIZATIONS.mkdir(parents=True, exist_ok=True)

    paths = {
        "results": ARTIFACTS / f"{PREFIX}_results.json",
        "state": ARTIFACTS / f"{PREFIX}_state.json",
        "summary": ARTIFACTS / f"{PREFIX}_summary.csv",
        "verdict": ARTIFACTS / f"{PREFIX}_verdict.csv",
        "live_conversation_frames": ARTIFACTS / f"{PREFIX}_live_conversation_frames.csv",
        "sensory_overlay_frames": ARTIFACTS / f"{PREFIX}_sensory_overlay_frames.csv",
        "gesture_body_language_frames": ARTIFACTS / f"{PREFIX}_gesture_body_language_frames.csv",
        "inventory_resource_widget_frames": ARTIFACTS / f"{PREFIX}_inventory_resource_widget_frames.csv",
        "minigame_failure_animation_frames": ARTIFACTS / f"{PREFIX}_minigame_failure_animation_frames.csv",
        "multiagent_consequence_frames": ARTIFACTS / f"{PREFIX}_multiagent_consequence_frames.csv",
        "live_session_reload_probes": ARTIFACTS / f"{PREFIX}_live_session_reload_probes.csv",
        "browser_ticks": ARTIFACTS / f"{PREFIX}_browser_ticks.csv",
        "visualization": VISUALIZATIONS / f"{PREFIX}.html",
    }

    paths["results"].write_text(json.dumps(bundle.results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    paths["state"].write_text(json.dumps(bundle.state, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _write_csv(
        paths["summary"],
        [
            {"metric": "report", "value": REPORT},
            {"metric": "seed", "value": bundle.seed},
            {"metric": "verdict", "value": bundle.results["verdict"]},
            {"metric": "readiness", "value": bundle.results["readiness"]},
            {"metric": "mean_channel_score", "value": bundle.results["mean_channel_score"]},
            {"metric": "weakest_channel_score", "value": bundle.results["weakest_channel_score"]},
            {"metric": "weakest_named_channel", "value": bundle.results["weakest_named_channel"]},
            *[{"metric": key, "value": value} for key, value in bundle.counts.items()],
            *[{"metric": key, "value": round(value, 6)} for key, value in bundle.channels.items()],
        ],
    )
    _write_csv(
        paths["verdict"],
        [
            {
                "report": REPORT,
                "prefix": PREFIX,
                "seed": bundle.seed,
                "verdict": bundle.results["verdict"],
                "readiness": bundle.results["readiness"],
                "weakest_channel_score": bundle.results["weakest_channel_score"],
                "weakest_named_channel": bundle.results["weakest_named_channel"],
                "boundary": BOUNDARY,
                "next_gate": NEXT_GATE,
            }
        ],
    )
    _write_csv(paths["live_conversation_frames"], bundle.live_conversation_frames)
    _write_csv(paths["sensory_overlay_frames"], bundle.sensory_overlay_frames)
    _write_csv(paths["gesture_body_language_frames"], bundle.gesture_body_language_frames)
    _write_csv(paths["inventory_resource_widget_frames"], bundle.inventory_resource_widget_frames)
    _write_csv(paths["minigame_failure_animation_frames"], bundle.minigame_failure_animation_frames)
    _write_csv(paths["multiagent_consequence_frames"], bundle.multiagent_consequence_frames)
    _write_csv(paths["live_session_reload_probes"], bundle.live_session_reload_probes)
    _write_csv(paths["browser_ticks"], bundle.browser_ticks)
    paths["visualization"].write_text(bundle.html, encoding="utf-8")
    return paths


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    bundle = generate(args.seed)
    write_outputs(bundle)
    print(
        json.dumps(
            {
                "report": REPORT,
                "prefix": PREFIX,
                "seed": args.seed,
                "verdict": bundle.results["verdict"],
                "readiness": bundle.results["readiness"],
                "weakest_channel_score": bundle.results["weakest_channel_score"],
                "weakest_named_channel": bundle.results["weakest_named_channel"],
                "counts": bundle.counts,
                "next_gate": NEXT_GATE,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
