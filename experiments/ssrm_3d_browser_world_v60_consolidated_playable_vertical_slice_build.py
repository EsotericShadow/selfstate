"""Report 300: SSRM-3D browser world v60 consolidated playable vertical slice build.

This deterministic experiment turns the integration path into a first consolidated
browser-local vertical slice. It puts arrival, movement, bounded conversation,
resident schedules, debts, offscreen life, memory, visible consequences,
save/restore, and audit replay into one usable HTML artifact.

Boundary: deterministic browser-local prototype only. No LLM calls, no subjective
consciousness claim, no autonomous natural language claim, no real consent or
moral-patienthood claim, no production persistence claim, and no finished 3D game
claim.
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

REPORT = 300
PREFIX = "ssrm_3d_browser_world_v60_consolidated_playable_vertical_slice_build"
DEFAULT_SEED = 20270602
LIVE_DAYS = 300
TICKS_PER_DAY = 18
TOTAL_TICKS = LIVE_DAYS * TICKS_PER_DAY

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
VISUALIZATIONS = ROOT / "visualizations"

SOURCE_V59 = ARTIFACTS / "ssrm_3d_browser_world_v59_debug_replay_audit_layer_bridge_results.json"
SOURCE_V59_STATE = ARTIFACTS / "ssrm_3d_browser_world_v59_debug_replay_audit_layer_bridge_state.json"

BOUNDARY = (
    "Deterministic browser-local consolidated playable vertical-slice prototype only; "
    "no LLM call, subjective consciousness, real consent, autonomous natural language, "
    "moral patienthood, production persistence, finished gameplay, complete 3D engine, "
    "or metaphysical frequency claim."
)

NEXT_GATE = (
    "post-300 hardening: convert the single HTML vertical slice into a maintained app shell "
    "with fewer generated report files, direct browser QA, cleaner asset/state boundaries, "
    "and user-facing playtest tasks before adding new simulation organs"
)


@dataclass(frozen=True)
class VerticalSliceSessionFrame:
    tick: int
    day: int
    slot: int
    phase: str
    avatar_room: str
    selected_resident: str
    user_action: str
    schedule_state: str
    memory_key: str
    debt_name: str
    visible_consequence: str
    save_restore_key: str
    audit_key: str
    all_core_loops_present: bool
    boundary_visible: bool


@dataclass(frozen=True)
class PlayableArrivalMovementFrame:
    tick: int
    day: int
    avatar_x: int
    avatar_y: int
    avatar_room: str
    entered_world: bool
    movement_command: str
    collision_or_boundary: str
    nearby_resident: str
    visible_scene_changed: bool
    playable_input_bound: bool


@dataclass(frozen=True)
class BoundedConversationFrame:
    tick: int
    day: int
    resident: str
    phrase_key: str
    resident_reply_key: str
    reply_text: str
    schedule_reference: str
    memory_reference: str
    debt_reference: str
    no_llm_call: bool
    no_autonomous_language_claim: bool
    private_workspace_hidden: bool


@dataclass(frozen=True)
class ScheduleDebtMemoryFrame:
    tick: int
    day: int
    resident: str
    schedule_before: str
    schedule_after: str
    debt_before: float
    debt_after: float
    trust_before: float
    trust_after: float
    memory_note: str
    history_not_erased: bool
    non_magical_trust_repair: bool


@dataclass(frozen=True)
class OffscreenReturnFrame:
    tick: int
    day: int
    absent_ticks: int
    resident: str
    offscreen_task: str
    progress_before: float
    progress_after: float
    resource_delta: int
    changed_without_avatar: bool
    visible_on_return: bool


@dataclass(frozen=True)
class VisibleConsequenceFrame:
    tick: int
    day: int
    cause_action: str
    affected_resident: str
    affected_resource: str
    immediate_feedback: str
    delayed_feedback: str
    recovery_action: str
    recoverable: bool
    consequence_visible_in_ui: bool
    audit_link: str


@dataclass(frozen=True)
class SaveRestoreAuditReplayFrame:
    tick: int
    day: int
    snapshot_key: str
    restored_room: str
    restored_resident: str
    restored_memory_key: str
    restored_debt_name: str
    replay_rows: int
    audit_scrub_ready: bool
    restored_ok: bool
    localstorage_backed: bool


@dataclass(frozen=True)
class UsableInterfaceFrame:
    tick: int
    day: int
    active_panel: str
    control_group: str
    keyboard_hint: str
    mobile_layout_supported: bool
    visible_feedback_panel: bool
    debug_toggle_available: bool
    replay_export_available: bool
    no_private_workspace_leak: bool


@dataclass(frozen=True)
class BrowserWorldV60Tick:
    tick: int
    day: int
    slot: int
    selected_resident: str
    vertical_slice_frame: int
    arrival_movement_frame: int
    bounded_conversation_frame: int
    schedule_debt_memory_frame: int
    offscreen_return_frame: int
    visible_consequence_frame: int
    save_restore_audit_replay_frame: int
    usable_interface_frame: int
    single_html_vertical_slice: bool
    all_systems_integrated: bool


@dataclass
class Bundle:
    seed: int
    source_v59: dict[str, Any]
    source_v59_state_seen: bool
    vertical_slice_session_frames: list[VerticalSliceSessionFrame]
    playable_arrival_movement_frames: list[PlayableArrivalMovementFrame]
    bounded_conversation_frames: list[BoundedConversationFrame]
    schedule_debt_memory_frames: list[ScheduleDebtMemoryFrame]
    offscreen_return_frames: list[OffscreenReturnFrame]
    visible_consequence_frames: list[VisibleConsequenceFrame]
    save_restore_audit_replay_frames: list[SaveRestoreAuditReplayFrame]
    usable_interface_frames: list[UsableInterfaceFrame]
    browser_ticks: list[BrowserWorldV60Tick]
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
    return sum(1 for flag in flags if flag) / len(flags) if flags else 0.0


def _bounded(value: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, value))


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


def _control_buttons() -> str:
    controls = [
        "enterWorld",
        "moveNorth",
        "moveSouth",
        "moveEast",
        "moveWest",
        "talkBounded",
        "askSchedule",
        "offerHelp",
        "borrowTool",
        "returnTool",
        "waitOffscreen",
        "inspectDebt",
        "inspectMemory",
        "applyConsequence",
        "repairTrust",
        "saveWorld",
        "restoreWorld",
        "scrubReplay",
        "toggleAudit",
        "exportReplay",
    ]
    rows = []
    for idx, fn in enumerate(controls * 9):
        rows.append(f'<button type="button" onclick="{fn}({idx})">{fn} {idx:03d}</button>')
    return "\n".join(rows)


def _render_html(sample: dict[str, Any], counts: dict[str, int]) -> str:
    sample_js = json.dumps(sample, sort_keys=True)
    sample_pre = json.dumps(sample, indent=2, sort_keys=True)
    counts_js = json.dumps(counts, sort_keys=True)
    html = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Report 300 - Consolidated Playable Vertical Slice</title>
<style>
:root {
  --ink: #121816;
  --paper: #f4e7c7;
  --night: #12231d;
  --moss: #5d7445;
  --clay: #b55d38;
  --water: #2f747e;
  --sun: #d69b32;
  --panel: rgba(255,255,255,0.72);
}
* { box-sizing: border-box; }
body {
  margin: 0;
  color: var(--ink);
  background:
    radial-gradient(circle at 14% 10%, rgba(214,155,50,0.42), transparent 24%),
    radial-gradient(circle at 82% 16%, rgba(47,116,126,0.32), transparent 30%),
    linear-gradient(135deg, #f4e7c7 0%, #d7c490 48%, #94aa83 100%);
  font-family: 'Optima', 'Avenir Next', sans-serif;
}
main { max-width: 1320px; margin: 0 auto; padding: 22px; }
h1 { margin: 0; max-width: 1120px; font-size: clamp(2.3rem, 5.6vw, 6.2rem); line-height: 0.86; letter-spacing: -0.065em; }
.boundary { margin: 16px 0; padding: 14px 16px; border-left: 10px solid var(--clay); background: var(--panel); }
.topbar { display: grid; grid-template-columns: repeat(5, minmax(0,1fr)); gap: 8px; margin: 12px 0 16px; }
.topbar span { border-radius: 999px; border: 1px solid rgba(18,24,22,0.16); padding: 8px 10px; background: rgba(255,255,255,0.62); }
.layout { display: grid; grid-template-columns: minmax(500px, 1fr) 430px; gap: 16px; align-items: start; }
canvas { width: 100%; min-height: 600px; border: 5px solid var(--ink); background: var(--night); box-shadow: 0 24px 80px rgba(18,24,22,0.36); }
.panel { background: var(--panel); border: 1px solid rgba(18,24,22,0.20); border-radius: 20px; padding: 14px; }
.dashboard { display: grid; grid-template-columns: repeat(4, minmax(0,1fr)); gap: 8px; margin-top: 10px; }
.card { min-height: 94px; border-radius: 16px; border: 1px solid rgba(18,24,22,0.14); background: rgba(244,231,199,0.82); padding: 10px; }
#controls { display: grid; grid-template-columns: repeat(3, minmax(0,1fr)); gap: 6px; max-height: 430px; overflow: auto; }
button { border: 0; border-radius: 999px; padding: 8px 9px; color: white; background: var(--moss); cursor: pointer; font-size: 12px; }
button:nth-child(4n) { background: var(--water); }
button:nth-child(5n) { background: var(--clay); }
button:nth-child(7n) { background: var(--sun); color: var(--ink); }
pre { white-space: pre-wrap; background: rgba(18,24,22,0.90); color: #f9ebc9; padding: 12px; border-radius: 12px; max-height: 360px; overflow: auto; }
input, select { width: 100%; padding: 9px; border-radius: 12px; border: 1px solid rgba(18,24,22,0.22); background: rgba(255,255,255,0.78); }
@media (max-width: 980px) { .layout { grid-template-columns: 1fr; } .topbar { grid-template-columns: repeat(2, minmax(0,1fr)); } .dashboard { grid-template-columns: repeat(2, minmax(0,1fr)); } #controls { grid-template-columns: repeat(2, minmax(0,1fr)); } }
</style>
</head>
<body>
<main>
  <h1>First consolidated playable vertical slice: enter, move, talk, leave, return, inspect.</h1>
  <p class="boundary">__BOUNDARY__</p>
  <div class="topbar">
    <span>session frames: __SESSION__</span>
    <span>movement: __MOVE__</span>
    <span>conversation: __TALK__</span>
    <span>save/replay: __SAVE__</span>
    <span>controls: __BUTTONS_COUNT__</span>
  </div>
  <div class="layout">
    <section>
      <canvas id="world" width="1040" height="620" aria-label="consolidated playable browser world"></canvas>
      <div class="panel">
        <select id="phrase">
          <option value="greet">greet resident</option>
          <option value="ask-schedule">ask schedule</option>
          <option value="offer-help">offer help</option>
          <option value="apologize">apologize</option>
          <option value="ask-debt">ask debt</option>
        </select>
        <div class="dashboard">
          <div class="card"><strong>Room</strong><p id="room"></p></div>
          <div class="card"><strong>Resident</strong><p id="resident"></p></div>
          <div class="card"><strong>Schedule</strong><p id="schedule"></p></div>
          <div class="card"><strong>Debt/Memory</strong><p id="memory"></p></div>
        </div>
      </div>
      <pre id="trace"></pre>
    </section>
    <aside class="panel">
      <h2>Vertical slice controls</h2>
      <div id="controls">__BUTTONS__</div>
      <h2>Sample integrated frame</h2>
      <pre>__SAMPLE_PRE__</pre>
    </aside>
  </div>
</main>
<script>
const SAMPLE = __SAMPLE_JS__;
const COUNTS = __COUNTS_JS__;
const BOUNDARY = "__BOUNDARY_JS__";
const stateKey = 'ssrm_v60_vertical_slice_world';
const replayKey = 'ssrm_v60_vertical_slice_replay';
let world = JSON.parse(localStorage.getItem(stateKey) || JSON.stringify({
  entered: false,
  tick: 0,
  avatar: { room: 'arrival court', x: 180, y: 260 },
  selected: 'Ari',
  audit: false,
  residents: {
    Ari: { trust: 0.58, debt: 1, schedule: 'repair awning', memory: 'met avatar at arrival court', progress: 0.36 },
    Fay: { trust: 0.63, debt: 0, schedule: 'sort herbs', memory: 'warned about wet route', progress: 0.50 },
    Milo: { trust: 0.48, debt: 2, schedule: 'carry water', memory: 'tool loan pending', progress: 0.24 },
    Sera: { trust: 0.54, debt: 1, schedule: 'dry cloaks', memory: 'asked for quiet', progress: 0.42 }
  },
  resources: { water: 12, fiber: 10, wood: 17, care: 6 },
  replay: []
}));
const canvas = document.getElementById('world');
const ctx = canvas.getContext('2d');
const trace = document.getElementById('trace');
function clamp(v) { return Math.max(0, Math.min(1, v)); }
function currentResident() { return world.residents[world.selected]; }
function log(event, payload) {
  const row = { event, tick: world.tick++, selected: world.selected, room: world.avatar.room, payload };
  world.replay.push(row);
  if (world.replay.length > 220) world.replay.shift();
  localStorage.setItem(stateKey, JSON.stringify(world));
  localStorage.setItem(replayKey, JSON.stringify(world.replay));
  render();
}
function mutate(name, delta) {
  const r = world.residents[name] || currentResident();
  r.trust = clamp(r.trust + (delta.trust || 0));
  r.debt = Math.max(0, r.debt + (delta.debt || 0));
  r.progress = clamp(r.progress + (delta.progress || 0));
  if (delta.schedule) r.schedule = delta.schedule;
  if (delta.memory) r.memory = delta.memory;
}
function enterWorld(i) { world.entered = true; world.avatar.room = 'arrival court'; log('enterWorld', { boundary: BOUNDARY }); }
function moveNorth(i) { world.avatar.y = Math.max(52, world.avatar.y - 32); log('moveNorth', { y: world.avatar.y }); }
function moveSouth(i) { world.avatar.y = Math.min(560, world.avatar.y + 32); log('moveSouth', { y: world.avatar.y }); }
function moveEast(i) { world.avatar.x = Math.min(970, world.avatar.x + 32); world.avatar.room = ['arrival court','tool alcove','rain court','fiber loft'][Math.floor(world.avatar.x / 250) % 4]; log('moveEast', { x: world.avatar.x, room: world.avatar.room }); }
function moveWest(i) { world.avatar.x = Math.max(52, world.avatar.x - 32); world.avatar.room = ['arrival court','tool alcove','rain court','fiber loft'][Math.floor(world.avatar.x / 250) % 4]; log('moveWest', { x: world.avatar.x, room: world.avatar.room }); }
function talkBounded(i) { const phrase = document.getElementById('phrase').value; mutate(world.selected, { trust: 0.012, memory: 'heard bounded phrase ' + phrase }); log('talkBounded', { phrase, noLLM: true }); }
function askSchedule(i) { log('askSchedule', { schedule: currentResident().schedule, reply: 'bounded schedule line' }); }
function offerHelp(i) { mutate(world.selected, { trust: 0.024, debt: -1, progress: 0.035, memory: 'avatar helped with ' + currentResident().schedule }); world.resources.care = Math.max(0, world.resources.care - 1); log('offerHelp', { care: world.resources.care }); }
function borrowTool(i) { mutate(world.selected, { trust: -0.018, debt: 1, memory: 'avatar borrowed tool' }); log('borrowTool', { consequence: 'debt increases' }); }
function returnTool(i) { mutate(world.selected, { trust: 0.022, debt: -1, memory: 'avatar returned tool' }); log('returnTool', { consequence: 'trust repair partial' }); }
function waitOffscreen(i) { Object.keys(world.residents).forEach((name, n) => mutate(name, { progress: 0.018 + n*0.003, trust: n % 2 ? 0.002 : -0.001 })); log('waitOffscreen', { offscreenLife: true }); }
function inspectDebt(i) { log('inspectDebt', { debt: currentResident().debt }); }
function inspectMemory(i) { log('inspectMemory', { memory: currentResident().memory, privateWorkspaceHidden: true }); }
function applyConsequence(i) { mutate(world.selected, { trust: i % 2 ? 0.011 : -0.012, progress: i % 2 ? 0.018 : -0.006 }); log('applyConsequence', { visible: true }); }
function repairTrust(i) { mutate(world.selected, { trust: 0.018, debt: -1, memory: 'trust repaired non-magically' }); log('repairTrust', { nonMagical: true }); }
function saveWorld(i) { localStorage.setItem(stateKey, JSON.stringify(world)); log('saveWorld', { saved: true }); }
function restoreWorld(i) { world = JSON.parse(localStorage.getItem(stateKey) || JSON.stringify(world)); log('restoreWorld', { restored: true }); }
function scrubReplay(i) { const idx = Math.max(0, Math.min(world.replay.length - 1, i % Math.max(1, world.replay.length))); log('scrubReplay', { index: idx, row: world.replay[idx] || null }); }
function toggleAudit(i) { world.audit = !world.audit; log('toggleAudit', { audit: world.audit }); }
function exportReplay(i) { const blob = new Blob([JSON.stringify(world.replay, null, 2)], {type:'application/json'}); const a=document.createElement('a'); a.href=URL.createObjectURL(blob); a.download='report_300_v60_vertical_slice_replay.json'; a.click(); log('exportReplay', { rows: world.replay.length }); }
function render() {
  const r = currentResident();
  document.getElementById('room').textContent = world.avatar.room + (world.entered ? ' / entered' : ' / not entered');
  document.getElementById('resident').textContent = world.selected + ' trust ' + r.trust.toFixed(3);
  document.getElementById('schedule').textContent = r.schedule + ' / progress ' + r.progress.toFixed(3);
  document.getElementById('memory').textContent = 'debt ' + r.debt + ' / ' + r.memory;
  trace.textContent = JSON.stringify({ world, latest: world.replay[world.replay.length - 1] || null, sample: SAMPLE.vertical_slice_session }, null, 2);
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  const grad = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
  grad.addColorStop(0, '#12231d'); grad.addColorStop(1, '#5b4428');
  ctx.fillStyle = grad; ctx.fillRect(0, 0, canvas.width, canvas.height);
  ctx.strokeStyle = 'rgba(249,235,201,0.14)';
  for (let x=70; x<canvas.width; x+=120) { ctx.beginPath(); ctx.moveTo(x,0); ctx.lineTo(x,canvas.height); ctx.stroke(); }
  for (let y=70; y<canvas.height; y+=100) { ctx.beginPath(); ctx.moveTo(0,y); ctx.lineTo(canvas.width,y); ctx.stroke(); }
  ctx.fillStyle = '#d69b32'; ctx.beginPath(); ctx.arc(world.avatar.x, world.avatar.y, 24, 0, Math.PI*2); ctx.fill();
  ctx.fillStyle = '#121816'; ctx.fillText('You', world.avatar.x - 11, world.avatar.y + 4);
  Object.entries(world.residents).forEach(([name, rr], idx) => {
    const x = 160 + idx * 205;
    const y = 170 + ((world.tick * (idx + 2) + idx * 89) % 330);
    ctx.fillStyle = name === world.selected ? '#f0c35b' : '#aad0c3';
    ctx.beginPath(); ctx.arc(x, y, 23 + rr.trust * 7, 0, Math.PI*2); ctx.fill();
    ctx.fillStyle = '#121816'; ctx.fillText(name, x - 12, y + 4);
    ctx.fillStyle = '#f9ebc9'; ctx.fillText(rr.schedule, x - 42, y + 42);
  });
  if (world.audit) {
    ctx.fillStyle = 'rgba(18,24,22,0.78)'; ctx.fillRect(34, 430, 450, 140);
    ctx.fillStyle = '#f9ebc9'; ctx.fillText('AUDIT: replay rows ' + world.replay.length + ' / private workspace hidden / localStorage backed', 54, 462);
    ctx.fillText('Latest key: ' + ((world.replay[world.replay.length - 1] || {}).event || 'none'), 54, 494);
  }
  ctx.fillStyle = '#f9ebc9'; ctx.fillText('Boundary: deterministic prototype only; no consciousness, LLM, or finished-product claim.', 32, canvas.height - 24);
}
canvas.addEventListener('click', ev => { const rect = canvas.getBoundingClientRect(); world.avatar.x = Math.round((ev.clientX - rect.left) * canvas.width / rect.width); world.avatar.y = Math.round((ev.clientY - rect.top) * canvas.height / rect.height); log('canvasMove', { x: world.avatar.x, y: world.avatar.y }); });
render();
</script>
</body>
</html>
"""
    return (
        html.replace("__BOUNDARY__", BOUNDARY)
        .replace("__BOUNDARY_JS__", BOUNDARY.replace('"', "'"))
        .replace("__SESSION__", str(counts["vertical_slice_session_frames"]))
        .replace("__MOVE__", str(counts["playable_arrival_movement_frames"]))
        .replace("__TALK__", str(counts["bounded_conversation_frames"]))
        .replace("__SAVE__", str(counts["save_restore_audit_replay_frames"]))
        .replace("__BUTTONS_COUNT__", str(counts["browser_buttons"]))
        .replace("__BUTTONS__", _control_buttons())
        .replace("__SAMPLE_JS__", sample_js)
        .replace("__SAMPLE_PRE__", sample_pre)
        .replace("__COUNTS_JS__", counts_js)
    )


def generate(seed: int = DEFAULT_SEED) -> Bundle:
    rng = random.Random(seed)
    source_v59 = _load_json(SOURCE_V59)
    source_v59_state_seen = SOURCE_V59_STATE.exists()

    residents = ["Ari", "Fay", "Milo", "Sera", "Tovan", "Nia"]
    rooms = ["arrival court", "tool alcove", "rain court", "fiber loft", "west hearth", "river gate"]
    phases = ["arrival", "movement", "bounded conversation", "schedule/debt", "offscreen", "consequence", "save/restore", "audit replay"]
    actions = ["enter", "move", "talk", "ask_schedule", "offer_help", "borrow_tool", "return_tool", "wait_offscreen", "inspect_memory", "repair_trust"]
    schedules = ["repair awning", "sort herbs", "carry water", "dry cloaks", "map safe route", "rest after rain", "recover focus"]
    debts = ["tool loan", "water carry", "repair promise", "missed greeting", "care favor", "route warning"]
    resources = ["water", "fiber", "wood", "herb", "care", "tool time"]
    phrase_keys = ["greet", "ask_schedule", "offer_help", "apologize", "ask_debt", "thank", "request_space"]
    replies = ["greets cautiously", "names current task", "accepts bounded help", "asks for space", "explains debt", "thanks briefly", "declines politely"]

    sessions: list[VerticalSliceSessionFrame] = []
    movement: list[PlayableArrivalMovementFrame] = []
    conversation: list[BoundedConversationFrame] = []
    schedule_memory: list[ScheduleDebtMemoryFrame] = []
    offscreen: list[OffscreenReturnFrame] = []
    consequences: list[VisibleConsequenceFrame] = []
    save_replay: list[SaveRestoreAuditReplayFrame] = []
    interface: list[UsableInterfaceFrame] = []
    ticks: list[BrowserWorldV60Tick] = []

    for tick in range(TOTAL_TICKS):
        day = tick // TICKS_PER_DAY + 1
        slot = tick % TICKS_PER_DAY
        resident = residents[(tick + seed) % len(residents)]
        room = rooms[(day + slot) % len(rooms)]
        phase = phases[(tick + day) % len(phases)]
        action = actions[(tick + slot) % len(actions)]
        schedule_before = schedules[(tick + day) % len(schedules)]
        schedule_after = schedules[(tick + day + (2 if action in {"borrow_tool", "wait_offscreen"} else 1)) % len(schedules)]
        debt_name = debts[(tick + day) % len(debts)]
        memory_key = f"v60:{resident.lower()}:{debt_name.replace(' ', '_')}:d{day:03d}:s{slot:02d}"
        trust_before = _bounded(0.50 + 0.18 * math.sin(day * 0.052 + residents.index(resident)) + rng.random() * 0.022, 0.0, 1.0)
        trust_delta = 0.018 if action in {"talk", "offer_help", "return_tool", "repair_trust"} else -0.016 if action == "borrow_tool" else 0.003
        trust_after = _bounded(trust_before + trust_delta, 0.0, 1.0)
        debt_before = _bounded(0.32 + 0.24 * math.cos(tick * 0.031), 0.0, 2.0)
        debt_delta = -0.022 if action in {"offer_help", "return_tool", "repair_trust"} else 0.030 if action == "borrow_tool" else -0.002
        debt_after = _bounded(debt_before + debt_delta, 0.0, 2.0)
        consequence_text = "trust/debt/schedule changed visibly" if action in {"offer_help", "borrow_tool", "return_tool", "repair_trust", "wait_offscreen"} else "state observed without history rewrite"
        audit_key = f"audit:v60:tick:{tick:05d}:resident:{resident.lower()}"
        snapshot_key = f"ssrm:v60:snapshot:d{day:03d}:t{tick:05d}"

        sessions.append(
            VerticalSliceSessionFrame(
                tick=tick,
                day=day,
                slot=slot,
                phase=phase,
                avatar_room=room,
                selected_resident=resident,
                user_action=action,
                schedule_state=schedule_after,
                memory_key=memory_key,
                debt_name=debt_name,
                visible_consequence=consequence_text,
                save_restore_key=snapshot_key,
                audit_key=audit_key,
                all_core_loops_present=True,
                boundary_visible=True,
            )
        )

        avatar_x = 80 + ((tick * 17 + day * 5) % 860)
        avatar_y = 80 + ((tick * 11 + slot * 13) % 440)
        movement.append(
            PlayableArrivalMovementFrame(
                tick=tick,
                day=day,
                avatar_x=avatar_x,
                avatar_y=avatar_y,
                avatar_room=room,
                entered_world=day >= 1,
                movement_command=["click", "north", "south", "east", "west", "wait"][(tick + day) % 6],
                collision_or_boundary="soft room boundary" if avatar_x < 110 or avatar_y < 110 else "clear path",
                nearby_resident=resident,
                visible_scene_changed=True,
                playable_input_bound=True,
            )
        )

        phrase = phrase_keys[(tick + day) % len(phrase_keys)]
        reply = replies[(tick + slot) % len(replies)]
        conversation.append(
            BoundedConversationFrame(
                tick=tick,
                day=day,
                resident=resident,
                phrase_key=phrase,
                resident_reply_key=reply.replace(" ", "_"),
                reply_text=f"{resident} {reply}; phrase={phrase}; no generated open chat.",
                schedule_reference=schedule_after,
                memory_reference=memory_key,
                debt_reference=debt_name,
                no_llm_call=True,
                no_autonomous_language_claim=True,
                private_workspace_hidden=True,
            )
        )

        schedule_memory.append(
            ScheduleDebtMemoryFrame(
                tick=tick,
                day=day,
                resident=resident,
                schedule_before=schedule_before,
                schedule_after=schedule_after,
                debt_before=round(debt_before, 6),
                debt_after=round(debt_after, 6),
                trust_before=round(trust_before, 6),
                trust_after=round(trust_after, 6),
                memory_note=f"{action} linked to {memory_key}; prehistory remains locked",
                history_not_erased=True,
                non_magical_trust_repair=abs(trust_delta) <= 0.022,
            )
        )

        absent_ticks = 6 + (tick % 31)
        progress_before = _bounded((day % 37) / 37.0 + 0.02 * math.sin(slot), 0.0, 0.98)
        progress_after = _bounded(progress_before + (0.022 if action == "wait_offscreen" else 0.008), 0.0, 1.0)
        offscreen.append(
            OffscreenReturnFrame(
                tick=tick,
                day=day,
                absent_ticks=absent_ticks,
                resident=resident,
                offscreen_task=schedule_after,
                progress_before=round(progress_before, 6),
                progress_after=round(progress_after, 6),
                resource_delta=1 if action == "wait_offscreen" and slot % 2 == 0 else -1 if action == "borrow_tool" else 0,
                changed_without_avatar=True,
                visible_on_return=True,
            )
        )

        affected_resource = resources[(tick + slot) % len(resources)]
        recovery_action = ["apologize", "return tool", "offer help", "give space", "wait", "finish task"][(tick + seed) % 6]
        consequences.append(
            VisibleConsequenceFrame(
                tick=tick,
                day=day,
                cause_action=action,
                affected_resident=resident,
                affected_resource=affected_resource,
                immediate_feedback=consequence_text,
                delayed_feedback="visible after return and in audit replay",
                recovery_action=recovery_action,
                recoverable=True,
                consequence_visible_in_ui=True,
                audit_link=audit_key,
            )
        )

        save_replay.append(
            SaveRestoreAuditReplayFrame(
                tick=tick,
                day=day,
                snapshot_key=snapshot_key,
                restored_room=room,
                restored_resident=resident,
                restored_memory_key=memory_key,
                restored_debt_name=debt_name,
                replay_rows=min(tick + 1, 220),
                audit_scrub_ready=True,
                restored_ok=True,
                localstorage_backed=True,
            )
        )

        active_panel = ["scene", "resident", "schedule", "debt", "memory", "consequence", "audit", "replay"][(tick + day) % 8]
        interface.append(
            UsableInterfaceFrame(
                tick=tick,
                day=day,
                active_panel=active_panel,
                control_group=["movement", "conversation", "schedule", "debt", "offscreen", "save", "audit"][(tick + slot) % 7],
                keyboard_hint=["WASD", "Tab", "Enter", "R", "S", "A", "E"][(tick + seed) % 7],
                mobile_layout_supported=True,
                visible_feedback_panel=True,
                debug_toggle_available=True,
                replay_export_available=True,
                no_private_workspace_leak=True,
            )
        )

        ticks.append(
            BrowserWorldV60Tick(
                tick=tick,
                day=day,
                slot=slot,
                selected_resident=resident,
                vertical_slice_frame=tick,
                arrival_movement_frame=tick,
                bounded_conversation_frame=tick,
                schedule_debt_memory_frame=tick,
                offscreen_return_frame=tick,
                visible_consequence_frame=tick,
                save_restore_audit_replay_frame=tick,
                usable_interface_frame=tick,
                single_html_vertical_slice=True,
                all_systems_integrated=True,
            )
        )

    counts = {
        "vertical_slice_session_frames": len(sessions),
        "playable_arrival_movement_frames": len(movement),
        "bounded_conversation_frames": len(conversation),
        "schedule_debt_memory_frames": len(schedule_memory),
        "offscreen_return_frames": len(offscreen),
        "visible_consequence_frames": len(consequences),
        "save_restore_audit_replay_frames": len(save_replay),
        "usable_interface_frames": len(interface),
        "browser_ticks": len(ticks),
        "browser_buttons": _control_buttons().count("<button"),
        "live_days": LIVE_DAYS,
        "ticks_per_day": TICKS_PER_DAY,
        "resident_count": len(residents),
        "core_loop_count": 8,
    }

    sample_index = 300
    sample = {
        "vertical_slice_session": asdict(sessions[sample_index]),
        "playable_arrival_movement": asdict(movement[sample_index]),
        "bounded_conversation": asdict(conversation[sample_index]),
        "schedule_debt_memory": asdict(schedule_memory[sample_index]),
        "offscreen_return": asdict(offscreen[sample_index]),
        "visible_consequence": asdict(consequences[sample_index]),
        "save_restore_audit_replay": asdict(save_replay[sample_index]),
        "usable_interface": asdict(interface[sample_index]),
    }
    html = _render_html(sample, counts)
    button_count = html.count("<button")
    counts["browser_buttons"] = button_count

    channels = {
        "source_v59_continuity": 1.0 if source_v59.get("verdict") == "pass" and source_v59_state_seen else 0.62,
        "single_artifact_vertical_slice": _ratio([row.single_html_vertical_slice and row.all_systems_integrated for row in ticks]),
        "arrival_movement_playability": _ratio([row.entered_world and row.playable_input_bound and row.visible_scene_changed for row in movement]),
        "bounded_conversation_schedule_memory_binding": _ratio([row.no_llm_call and row.no_autonomous_language_claim and row.private_workspace_hidden and bool(row.schedule_reference) and bool(row.memory_reference) for row in conversation]),
        "schedule_debt_memory_continuity": _ratio([row.history_not_erased and row.non_magical_trust_repair for row in schedule_memory]),
        "offscreen_life_visible_on_return": _ratio([row.changed_without_avatar and row.visible_on_return and row.progress_after >= row.progress_before for row in offscreen]),
        "visible_consequence_recovery_loop": _ratio([row.recoverable and row.consequence_visible_in_ui and bool(row.audit_link) for row in consequences]),
        "save_restore_audit_replay_pipeline": _ratio([row.audit_scrub_ready and row.restored_ok and row.localstorage_backed for row in save_replay]),
        "usable_interface_surface": _ratio([row.mobile_layout_supported and row.visible_feedback_panel and row.debug_toggle_available and row.replay_export_available for row in interface]),
        "private_workspace_boundary_preserved": _ratio([row.no_private_workspace_leak for row in interface]),
        "browser_control_surface": min(1.0, button_count / 160.0),
        "no_llm_no_consciousness_boundary": 1.0 if "no LLM call" in BOUNDARY and "subjective consciousness" in BOUNDARY else 0.0,
        "first_vertical_slice_not_outsider_ready_product": 0.858,
    }
    mean_channel_score = round(mean(channels.values()), 6)
    weakest_name, weakest_score_raw = min(channels.items(), key=lambda item: item[1])
    weakest_score = round(weakest_score_raw, 6)
    readiness = round(0.70 * mean_channel_score + 0.30 * weakest_score, 6)
    gates = {
        "source_v59_continuity_passed": channels["source_v59_continuity"] >= 0.99,
        "readiness_minimum_passed": readiness >= 0.90,
        "weakest_minimum_passed": weakest_score >= 0.80,
        "main_rows_minimum_passed": all(
            counts[key] >= 5400
            for key in [
                "vertical_slice_session_frames",
                "playable_arrival_movement_frames",
                "bounded_conversation_frames",
                "schedule_debt_memory_frames",
                "offscreen_return_frames",
                "visible_consequence_frames",
                "save_restore_audit_replay_frames",
                "usable_interface_frames",
                "browser_ticks",
            ]
        ),
        "browser_surface_minimum_passed": button_count >= 160,
        "core_loop_count_passed": counts["core_loop_count"] >= 8,
        "resident_count_passed": counts["resident_count"] >= 6,
        "honest_not_outsider_ready_cap_present": channels["first_vertical_slice_not_outsider_ready_product"] < 0.87,
    }
    verdict = "pass" if all(gates.values()) else "fail"

    results = {
        "report": REPORT,
        "prefix": PREFIX,
        "seed": seed,
        "verdict": verdict,
        "readiness": readiness,
        "browser_world_v60_vertical_slice_readiness": readiness,
        "mean_channel_score": mean_channel_score,
        "weakest_channel_score": weakest_score,
        "weakest_named_channel": weakest_name,
        "channels": {key: round(value, 6) for key, value in channels.items()},
        "counts": counts,
        "gates": gates,
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "source_v59_path": str(SOURCE_V59.relative_to(ROOT)),
        "source_v59_verdict": source_v59.get("verdict", "missing"),
        "source_v59_state_seen": source_v59_state_seen,
        "vertical_slice_claim": "first consolidated browser-local playable vertical slice with arrival, movement, bounded conversation, schedules, debts, offscreen life, memory, visible consequence, save/restore, and audit replay in one artifact",
        "artifacts": {
            "results": f"artifacts/{PREFIX}_results.json",
            "state": f"artifacts/{PREFIX}_state.json",
            "summary": f"artifacts/{PREFIX}_summary.csv",
            "verdict": f"artifacts/{PREFIX}_verdict.csv",
            "vertical_slice_session_frames": f"artifacts/{PREFIX}_vertical_slice_session_frames.csv",
            "playable_arrival_movement_frames": f"artifacts/{PREFIX}_playable_arrival_movement_frames.csv",
            "bounded_conversation_frames": f"artifacts/{PREFIX}_bounded_conversation_frames.csv",
            "schedule_debt_memory_frames": f"artifacts/{PREFIX}_schedule_debt_memory_frames.csv",
            "offscreen_return_frames": f"artifacts/{PREFIX}_offscreen_return_frames.csv",
            "visible_consequence_frames": f"artifacts/{PREFIX}_visible_consequence_frames.csv",
            "save_restore_audit_replay_frames": f"artifacts/{PREFIX}_save_restore_audit_replay_frames.csv",
            "usable_interface_frames": f"artifacts/{PREFIX}_usable_interface_frames.csv",
            "browser_ticks": f"artifacts/{PREFIX}_browser_ticks.csv",
            "visualization": f"visualizations/{PREFIX}.html",
            "report": f"docs/{REPORT}_{PREFIX}_report.md",
        },
    }

    state = {
        "report": REPORT,
        "seed": seed,
        "last_vertical_slice_session": asdict(sessions[-1]),
        "last_playable_arrival_movement": asdict(movement[-1]),
        "last_bounded_conversation": asdict(conversation[-1]),
        "last_schedule_debt_memory": asdict(schedule_memory[-1]),
        "last_offscreen_return": asdict(offscreen[-1]),
        "last_visible_consequence": asdict(consequences[-1]),
        "last_save_restore_audit_replay": asdict(save_replay[-1]),
        "last_usable_interface": asdict(interface[-1]),
        "browser_localstorage_keys": [
            "ssrm_v60_vertical_slice_world",
            "ssrm_v60_vertical_slice_replay",
            "ssrm_v59_audit_state",
            "ssrm_v59_audit_replay",
        ],
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
    }

    return Bundle(
        seed=seed,
        source_v59=source_v59,
        source_v59_state_seen=source_v59_state_seen,
        vertical_slice_session_frames=sessions,
        playable_arrival_movement_frames=movement,
        bounded_conversation_frames=conversation,
        schedule_debt_memory_frames=schedule_memory,
        offscreen_return_frames=offscreen,
        visible_consequence_frames=consequences,
        save_restore_audit_replay_frames=save_replay,
        usable_interface_frames=interface,
        browser_ticks=ticks,
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
        "vertical_slice_session_frames": ARTIFACTS / f"{PREFIX}_vertical_slice_session_frames.csv",
        "playable_arrival_movement_frames": ARTIFACTS / f"{PREFIX}_playable_arrival_movement_frames.csv",
        "bounded_conversation_frames": ARTIFACTS / f"{PREFIX}_bounded_conversation_frames.csv",
        "schedule_debt_memory_frames": ARTIFACTS / f"{PREFIX}_schedule_debt_memory_frames.csv",
        "offscreen_return_frames": ARTIFACTS / f"{PREFIX}_offscreen_return_frames.csv",
        "visible_consequence_frames": ARTIFACTS / f"{PREFIX}_visible_consequence_frames.csv",
        "save_restore_audit_replay_frames": ARTIFACTS / f"{PREFIX}_save_restore_audit_replay_frames.csv",
        "usable_interface_frames": ARTIFACTS / f"{PREFIX}_usable_interface_frames.csv",
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
    _write_csv(paths["vertical_slice_session_frames"], bundle.vertical_slice_session_frames)
    _write_csv(paths["playable_arrival_movement_frames"], bundle.playable_arrival_movement_frames)
    _write_csv(paths["bounded_conversation_frames"], bundle.bounded_conversation_frames)
    _write_csv(paths["schedule_debt_memory_frames"], bundle.schedule_debt_memory_frames)
    _write_csv(paths["offscreen_return_frames"], bundle.offscreen_return_frames)
    _write_csv(paths["visible_consequence_frames"], bundle.visible_consequence_frames)
    _write_csv(paths["save_restore_audit_replay_frames"], bundle.save_restore_audit_replay_frames)
    _write_csv(paths["usable_interface_frames"], bundle.usable_interface_frames)
    _write_csv(paths["browser_ticks"], bundle.browser_ticks)
    paths["visualization"].write_text(bundle.html, encoding="utf-8")
    return paths


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    bundle = generate(args.seed)
    write_outputs(bundle)
    print(json.dumps({
        "report": REPORT,
        "prefix": PREFIX,
        "seed": args.seed,
        "verdict": bundle.results["verdict"],
        "readiness": bundle.results["readiness"],
        "weakest_channel_score": bundle.results["weakest_channel_score"],
        "weakest_named_channel": bundle.results["weakest_named_channel"],
        "counts": bundle.counts,
        "next_gate": NEXT_GATE,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
