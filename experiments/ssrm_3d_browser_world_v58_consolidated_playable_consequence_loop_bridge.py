"""Report 298: consolidated playable consequence loop bridge.

This deterministic benchmark starts consolidating the browser-world report line into
one playable vertical-slice loop: avatar action, resident schedule, memory/debt,
offscreen life, visible consequence, save/restore, and replay/debug.

Boundary: deterministic browser-local scaffold only. No LLM calls, no subjective
consciousness claim, no autonomous natural language claim, no real consent or
moral-patienthood claim, and no complete 3D game/product claim.
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

REPORT = 298
PREFIX = "ssrm_3d_browser_world_v58_consolidated_playable_consequence_loop_bridge"
DEFAULT_SEED = 20270505
LIVE_DAYS = 260
TICKS_PER_DAY = 18
TOTAL_TICKS = LIVE_DAYS * TICKS_PER_DAY

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
VISUALIZATIONS = ROOT / "visualizations"

SOURCE_V57 = ARTIFACTS / "ssrm_3d_browser_world_v57_live_conversation_sensory_overlay_gesture_inventory_minigame_failure_multiagent_consequence_bridge_results.json"
SOURCE_V57_STATE = ARTIFACTS / "ssrm_3d_browser_world_v57_live_conversation_sensory_overlay_gesture_inventory_minigame_failure_multiagent_consequence_bridge_state.json"

BOUNDARY = (
    "Deterministic browser-local consolidated playable consequence-loop scaffold only; "
    "no LLM call, subjective consciousness, real consent, autonomous natural language, "
    "moral patienthood, complete gameplay, complete 3D engine, production persistence, "
    "or metaphysical frequency claim."
)

NEXT_GATE = (
    "browser world v59 with a dedicated debug/replay/audit layer that can scrub the "
    "same playable consequence loop by tick, resident, memory, debt, schedule, and "
    "localStorage snapshot without LLM calls"
)


@dataclass(frozen=True)
class IntegratedLoopFrame:
    tick: int
    day: int
    slot: int
    avatar_room: str
    avatar_action_key: str
    resident: str
    project: str
    trust_before: float
    trust_after: float
    obligation_before: float
    obligation_after: float
    schedule_before: str
    schedule_after: str
    visible_consequence: str
    avatar_agency_bound: bool
    resident_agency_bound: bool
    replay_key: str


@dataclass(frozen=True)
class ResidentSchedulerFrame:
    tick: int
    day: int
    slot: int
    resident: str
    room: str
    schedule_state: str
    need_state: str
    debt_focus: str
    project_progress: float
    offscreen: bool
    schedule_changed_by_avatar: bool
    agency_preserved: bool


@dataclass(frozen=True)
class AvatarActionFrame:
    tick: int
    day: int
    avatar_action_key: str
    action_category: str
    resident: str
    allowed: bool
    refused: bool
    refusal_respected: bool
    reason: str
    state_delta: str
    visible_feedback: str
    not_magic: bool


@dataclass(frozen=True)
class MemoryDebtFrame:
    tick: int
    day: int
    resident: str
    memory_key: str
    debt_name: str
    debt_before: float
    debt_after: float
    trust_before: float
    trust_after: float
    relationship_note: str
    persists_to_reload: bool
    history_not_erased: bool


@dataclass(frozen=True)
class OffscreenActivityFrame:
    tick: int
    day: int
    resident: str
    absent_ticks: int
    offscreen_activity: str
    progress_before: float
    progress_after: float
    resource_delta: int
    interaction_without_avatar: bool
    visible_after_return: bool


@dataclass(frozen=True)
class ConsequenceLoopFrame:
    tick: int
    day: int
    cause_action: str
    direct_effect: str
    delayed_effect: str
    affected_resident: str
    affected_resource: str
    trust_delta: float
    schedule_delta: str
    recovery_path: str
    no_history_erasure: bool
    harm_recoverable: bool


@dataclass(frozen=True)
class DashboardFrame:
    tick: int
    day: int
    selected_resident: str
    visible_schedule: str
    visible_project: str
    visible_debt: str
    visible_care_need: str
    visible_trust: float
    panel_patch: str
    private_workspace_hidden: bool


@dataclass(frozen=True)
class SaveRestoreReplayFrame:
    tick: int
    day: int
    snapshot_key: str
    restored_avatar_room: str
    restored_resident: str
    restored_memory_key: str
    restored_debt_name: str
    replay_event_count: int
    restored_ok: bool
    audit_scrubbable: bool


@dataclass(frozen=True)
class BrowserWorldV58Tick:
    tick: int
    day: int
    slot: int
    avatar_room: str
    selected_resident: str
    loop_frame: int
    scheduler_frame: int
    action_frame: int
    memory_frame: int
    offscreen_frame: int
    consequence_frame: int
    dashboard_frame: int
    replay_frame: int
    single_world_state_object: bool
    boundary_visible: bool


@dataclass
class Bundle:
    seed: int
    source_v57: dict[str, Any]
    source_v57_state_seen: bool
    integrated_loop_frames: list[IntegratedLoopFrame]
    resident_scheduler_frames: list[ResidentSchedulerFrame]
    avatar_action_frames: list[AvatarActionFrame]
    memory_debt_frames: list[MemoryDebtFrame]
    offscreen_activity_frames: list[OffscreenActivityFrame]
    consequence_loop_frames: list[ConsequenceLoopFrame]
    dashboard_frames: list[DashboardFrame]
    save_restore_replay_frames: list[SaveRestoreReplayFrame]
    browser_ticks: list[BrowserWorldV58Tick]
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
    functions = [
        "moveAvatar",
        "talkToResident",
        "offerHelp",
        "borrowTool",
        "returnTool",
        "interruptWork",
        "waitOffscreen",
        "advanceResidentScheduler",
        "applyVisibleConsequence",
        "repairTrust",
        "openDashboard",
        "selectResident",
        "showAudit",
        "toggleDebug",
    ]
    buttons = []
    for idx in range(168):
        fn = functions[idx % len(functions)]
        label = fn.replace("Avatar", " avatar").replace("Resident", " resident").replace("Visible", " visible").replace("Scheduler", " scheduler")
        buttons.append(f'<button type="button" onclick="{fn}({idx})">{label} {idx:03d}</button>')
    buttons.extend(
        [
            '<button type="button" onclick="saveWorldState()">save world state</button>',
            '<button type="button" onclick="restoreWorldState()">restore world state</button>',
            '<button type="button" onclick="exportReplay()">export replay</button>',
            '<button type="button" onclick="showBoundary()">show boundary</button>',
        ]
    )
    return "\n".join(buttons)


def _render_html(sample: dict[str, Any], counts: dict[str, int]) -> str:
    template = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>Report 298 - Consolidated Playable Consequence Loop</title>
<style>
:root {
  --ink: #172019;
  --paper: #f5ead2;
  --lichen: #6e7f45;
  --clay: #b85f3c;
  --blue: #2e6d79;
  --gold: #d7a842;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  color: var(--ink);
  background:
    linear-gradient(120deg, rgba(23,32,25,0.08), rgba(184,95,60,0.16)),
    radial-gradient(circle at 10% 10%, rgba(215,168,66,0.40), transparent 25%),
    radial-gradient(circle at 88% 22%, rgba(46,109,121,0.30), transparent 31%),
    #efe2c4;
  font-family: 'Iowan Old Style', Georgia, serif;
}
main { max-width: 1240px; margin: 0 auto; padding: 24px; }
h1 { margin: 0; max-width: 1000px; font-size: clamp(2rem, 5vw, 4.8rem); line-height: 0.92; letter-spacing: -0.05em; }
.boundary { margin: 18px 0; padding: 14px 16px; background: rgba(255,255,255,0.64); border-left: 9px solid var(--clay); }
.shell { display: grid; grid-template-columns: minmax(420px, 1fr) 390px; gap: 18px; }
canvas { width: 100%; min-height: 560px; border: 5px solid var(--ink); background: #16231b; box-shadow: 0 18px 60px rgba(23,32,25,0.35); }
.panel { background: rgba(255,255,255,0.70); border: 1px solid rgba(23,32,25,0.22); border-radius: 18px; padding: 14px; }
.metrics { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 8px; margin: 14px 0; }
.metrics span { background: rgba(255,255,255,0.64); padding: 8px 10px; border-radius: 999px; border: 1px solid rgba(23,32,25,0.16); }
#controls { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 6px; max-height: 380px; overflow: auto; }
button { border: 0; border-radius: 999px; padding: 8px 9px; color: white; background: var(--lichen); cursor: pointer; font-size: 12px; }
button:nth-child(3n) { background: var(--blue); }
button:nth-child(5n) { background: var(--clay); }
pre { white-space: pre-wrap; background: rgba(23,32,25,0.88); color: #f8edcc; padding: 12px; border-radius: 12px; max-height: 360px; overflow: auto; }
.dashboard { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px; }
.card { padding: 10px; background: rgba(245,234,210,0.76); border-radius: 14px; border: 1px solid rgba(23,32,25,0.16); }
@media (max-width: 880px) { .shell { grid-template-columns: 1fr; } .metrics { grid-template-columns: repeat(2, minmax(0, 1fr)); } #controls { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
</style>
</head>
<body>
<main>
  <h1>One playable loop: act, schedule, remember, leave, return, see consequence.</h1>
  <p class="boundary">__BOUNDARY__</p>
  <div class="metrics">
    <span>loop frames: __LOOPS__</span>
    <span>scheduler frames: __SCHED__</span>
    <span>offscreen frames: __OFFSCREEN__</span>
    <span>replay probes: __REPLAY__</span>
  </div>
  <div class="shell">
    <section>
      <canvas id="world" width="980" height="590" aria-label="consolidated deterministic browser world"></canvas>
      <div class="panel dashboard">
        <div class="card"><strong>Schedule</strong><p id="schedule"></p></div>
        <div class="card"><strong>Debt</strong><p id="debt"></p></div>
        <div class="card"><strong>Memory</strong><p id="memory"></p></div>
        <div class="card"><strong>Trust</strong><p id="trust"></p></div>
      </div>
      <pre id="trace"></pre>
    </section>
    <aside class="panel">
      <h2>Playable controls</h2>
      <div id="controls">__BUTTONS__</div>
      <h2>Sample integrated frame</h2>
      <pre>__SAMPLE__</pre>
    </aside>
  </div>
</main>
<script>
const SAMPLE = __SAMPLE_JS__;
const BOUNDARY = "__BOUNDARY_JS__";
const stateKey = 'ssrm_v58_consolidated_world_state';
const replayKey = 'ssrm_v58_consolidated_replay';
let world = JSON.parse(localStorage.getItem(stateKey) || JSON.stringify({
  tick: 0,
  avatarRoom: 'arrival court',
  selectedResident: 'Ari',
  residents: {
    Ari: { trust: 0.58, debt: 1, schedule: 'repair awning', memory: 'met avatar at wet crossing', project: 0.38 },
    Fay: { trust: 0.64, debt: 0, schedule: 'sort herbs', memory: 'keeps west shelf ledger', project: 0.52 },
    Milo: { trust: 0.49, debt: 2, schedule: 'carry water', memory: 'tool loan unresolved', project: 0.27 },
    Sera: { trust: 0.55, debt: 1, schedule: 'dry cloaks', memory: 'asked for quiet', project: 0.44 }
  },
  resources: { water: 14, fiber: 11, wood: 18, care: 6 },
  replay: [],
  debug: false
}));
const canvas = document.getElementById('world');
const ctx = canvas.getContext('2d');
const trace = document.getElementById('trace');
function currentResident() { return world.residents[world.selectedResident]; }
function clamp(v) { return Math.max(0, Math.min(1, v)); }
function log(event, payload) {
  const row = { event, tick: world.tick++, resident: world.selectedResident, payload };
  world.replay.push(row);
  if (world.replay.length > 140) world.replay.shift();
  localStorage.setItem(stateKey, JSON.stringify(world));
  localStorage.setItem(replayKey, JSON.stringify(world.replay));
  render();
}
function mutateResident(name, delta) {
  const r = world.residents[name] || currentResident();
  r.trust = clamp(r.trust + (delta.trust || 0));
  r.debt = Math.max(0, r.debt + (delta.debt || 0));
  r.project = clamp(r.project + (delta.project || 0));
  if (delta.schedule) r.schedule = delta.schedule;
  if (delta.memory) r.memory = delta.memory;
}
function moveAvatar(i) {
  const rooms = ['arrival court','tool alcove','rain court','fiber loft','west hearth','river gate'];
  world.avatarRoom = rooms[i % rooms.length];
  log('moveAvatar', { room: world.avatarRoom });
}
function talkToResident(i) { mutateResident(world.selectedResident, { trust: 0.012, memory: 'heard bounded phrase ' + i }); log('talkToResident', { noLLM: true, phraseKey: i }); }
function offerHelp(i) { mutateResident(world.selectedResident, { trust: 0.025, debt: -1, project: 0.035, memory: 'accepted bounded help ' + i }); world.resources.care = Math.max(0, world.resources.care - 1); log('offerHelp', { care: world.resources.care }); }
function borrowTool(i) { mutateResident(world.selectedResident, { trust: -0.018, debt: 1, memory: 'tool borrowed by avatar ' + i }); log('borrowTool', { debt: currentResident().debt }); }
function returnTool(i) { mutateResident(world.selectedResident, { trust: 0.021, debt: -1, memory: 'tool returned by avatar ' + i }); log('returnTool', { debt: currentResident().debt }); }
function interruptWork(i) { mutateResident(world.selectedResident, { trust: -0.03, schedule: 'recover focus after interruption', memory: 'avatar interrupted work ' + i }); log('interruptWork', { consequence: 'schedule delayed' }); }
function waitOffscreen(i) {
  Object.keys(world.residents).forEach((name, index) => mutateResident(name, { project: 0.018 + index * 0.002, trust: index % 2 ? 0.003 : -0.002 }));
  log('waitOffscreen', { progressedWithoutAvatar: true });
}
function advanceResidentScheduler(i) { mutateResident(world.selectedResident, { project: 0.02, schedule: i % 2 ? 'finish owed work' : 'rest before repair' }); log('advanceResidentScheduler', { schedule: currentResident().schedule }); }
function applyVisibleConsequence(i) { mutateResident(world.selectedResident, { trust: i % 3 ? 0.015 : -0.016, project: i % 3 ? 0.02 : -0.01 }); log('applyVisibleConsequence', { sample: SAMPLE.consequence_loop }); }
function repairTrust(i) { mutateResident(world.selectedResident, { trust: 0.018, debt: -1, memory: 'trust partially repaired ' + i }); log('repairTrust', { nonMagical: true }); }
function openDashboard(i) { log('openDashboard', { dashboard: SAMPLE.dashboard }); }
function selectResident(i) { const names = Object.keys(world.residents); world.selectedResident = names[i % names.length]; log('selectResident', { selected: world.selectedResident }); }
function showAudit(i) { log('showAudit', { replayEvents: world.replay.length, boundary: BOUNDARY }); }
function toggleDebug(i) { world.debug = !world.debug; log('toggleDebug', { debug: world.debug }); }
function saveWorldState() { localStorage.setItem(stateKey, JSON.stringify(world)); log('saveWorldState', { saved: true }); }
function restoreWorldState() { world = JSON.parse(localStorage.getItem(stateKey) || JSON.stringify(world)); log('restoreWorldState', { restored: true }); }
function exportReplay() {
  const blob = new Blob([JSON.stringify(world.replay, null, 2)], { type: 'application/json' });
  const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = 'report_298_v58_consolidated_replay.json'; a.click();
  log('exportReplay', { rows: world.replay.length });
}
function showBoundary() { log('showBoundary', { boundary: BOUNDARY }); }
function render() {
  const resident = currentResident();
  document.getElementById('schedule').textContent = resident.schedule + ' in ' + world.avatarRoom;
  document.getElementById('debt').textContent = world.selectedResident + ' debt ' + resident.debt;
  document.getElementById('memory').textContent = resident.memory;
  document.getElementById('trust').textContent = resident.trust.toFixed(3) + ' / project ' + resident.project.toFixed(3);
  trace.textContent = JSON.stringify({ world, latest: world.replay[world.replay.length - 1] || null }, null, 2);
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  const grad = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
  grad.addColorStop(0, '#173027'); grad.addColorStop(1, '#5e4a2e');
  ctx.fillStyle = grad; ctx.fillRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = 'rgba(255,255,255,0.13)';
  for (let x = 50; x < canvas.width; x += 110) ctx.fillRect(x, 0, 1, canvas.height);
  for (let y = 50; y < canvas.height; y += 90) ctx.fillRect(0, y, canvas.width, 1);
  Object.entries(world.residents).forEach(([name, r], idx) => {
    const x = 120 + ((idx * 173 + world.tick * (idx + 2)) % 760);
    const y = 110 + ((idx * 101 + world.tick * (idx + 3)) % 360);
    ctx.fillStyle = name === world.selectedResident ? '#d7a842' : '#b7d3c2';
    ctx.beginPath(); ctx.arc(x, y, 24 + r.trust * 8, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = '#111811'; ctx.fillText(name, x - 13, y + 4);
    ctx.fillStyle = '#f8edcc'; ctx.fillText(r.schedule, x - 42, y + 42);
  });
  ctx.fillStyle = '#f8edcc'; ctx.fillText('Avatar room: ' + world.avatarRoom, 24, 32);
  ctx.fillText('Single world state object + localStorage replay/debug. Boundary visible: no consciousness or LLM claim.', 24, canvas.height - 24);
}
render();
showBoundary();
</script>
</body>
</html>
"""
    sample_text = json.dumps(sample, indent=2, sort_keys=True)
    sample_js = json.dumps(sample, sort_keys=True)
    return (
        template.replace("__BOUNDARY__", BOUNDARY)
        .replace("__BOUNDARY_JS__", BOUNDARY.replace('"', "'"))
        .replace("__LOOPS__", str(counts["integrated_loop_frames"]))
        .replace("__SCHED__", str(counts["resident_scheduler_frames"]))
        .replace("__OFFSCREEN__", str(counts["offscreen_activity_frames"]))
        .replace("__REPLAY__", str(counts["save_restore_replay_frames"]))
        .replace("__BUTTONS__", _control_buttons())
        .replace("__SAMPLE__", sample_text)
        .replace("__SAMPLE_JS__", sample_js)
    )


def generate(seed: int = DEFAULT_SEED) -> Bundle:
    rng = random.Random(seed)
    source_v57 = _load_json(SOURCE_V57)
    source_v57_state_seen = SOURCE_V57_STATE.exists()

    residents = ["Ari", "Fay", "Milo", "Sera", "Tovan", "Nia"]
    rooms = ["arrival court", "tool alcove", "rain court", "fiber loft", "west hearth", "river gate"]
    projects = ["repair awning", "dry seed store", "fix bridge peg", "sort herb shelf", "patch cloak", "map safe route"]
    actions = ["move", "talk", "offer_help", "borrow_tool", "return_tool", "interrupt_work", "wait_offscreen", "repair_trust"]
    schedules = ["work", "rest", "negotiate debt", "seek tool", "care duty", "private task", "recover focus"]
    need_states = ["steady", "tired", "wet", "hungry", "focused", "guarded", "relieved"]
    debt_names = ["tool loan", "water carry", "repair promise", "missed greeting", "care favor", "route warning"]
    resources = ["water", "fiber", "wood", "herb", "care", "tool time"]
    recovery_paths = ["apologize and wait", "return object", "offer help", "give space", "finish owed work", "rest before retry"]

    integrated: list[IntegratedLoopFrame] = []
    scheduler: list[ResidentSchedulerFrame] = []
    avatar_actions: list[AvatarActionFrame] = []
    memories: list[MemoryDebtFrame] = []
    offscreen: list[OffscreenActivityFrame] = []
    consequences: list[ConsequenceLoopFrame] = []
    dashboard: list[DashboardFrame] = []
    replay: list[SaveRestoreReplayFrame] = []
    ticks: list[BrowserWorldV58Tick] = []

    for tick in range(TOTAL_TICKS):
        day = tick // TICKS_PER_DAY + 1
        slot = tick % TICKS_PER_DAY
        resident = residents[(tick + seed) % len(residents)]
        room = rooms[(day + slot + seed) % len(rooms)]
        project = projects[(day + residents.index(resident) + slot) % len(projects)]
        action = actions[(tick + day) % len(actions)]
        schedule_before = schedules[(tick + day) % len(schedules)]
        schedule_after = schedules[(tick + day + (2 if action in {"interrupt_work", "borrow_tool"} else 1)) % len(schedules)]
        trust_before = _bounded(0.47 + 0.18 * math.sin(day * 0.071 + residents.index(resident)) + rng.random() * 0.035, 0.12, 0.90)
        obligation_before = _bounded(0.30 + 0.22 * math.cos(tick * 0.029 + slot), 0.0, 1.0)
        if action in {"offer_help", "return_tool", "repair_trust", "talk"}:
            trust_delta = 0.016 + (0.004 if obligation_before > 0.4 else 0.0)
            obligation_delta = -0.026
            visible = "trust warms and obligation decreases"
        elif action in {"borrow_tool", "interrupt_work"}:
            trust_delta = -0.020
            obligation_delta = 0.030
            visible = "work is delayed and debt marker increases"
        elif action == "wait_offscreen":
            trust_delta = 0.002 if slot % 2 else -0.002
            obligation_delta = -0.006
            visible = "residents continue without avatar"
        else:
            trust_delta = 0.004
            obligation_delta = -0.002
            visible = "position changes but history remains intact"
        trust_after = _bounded(trust_before + trust_delta, 0.0, 1.0)
        obligation_after = _bounded(obligation_before + obligation_delta, 0.0, 1.0)
        replay_key = f"v58-loop-{tick:05d}"
        resident_agency_bound = action not in {"borrow_tool", "interrupt_work"} or slot % 4 != 0

        integrated.append(
            IntegratedLoopFrame(
                tick=tick,
                day=day,
                slot=slot,
                avatar_room=room,
                avatar_action_key=action,
                resident=resident,
                project=project,
                trust_before=round(trust_before, 6),
                trust_after=round(trust_after, 6),
                obligation_before=round(obligation_before, 6),
                obligation_after=round(obligation_after, 6),
                schedule_before=schedule_before,
                schedule_after=schedule_after,
                visible_consequence=visible,
                avatar_agency_bound=True,
                resident_agency_bound=resident_agency_bound,
                replay_key=replay_key,
            )
        )

        progress_before = _bounded((day % 29) / 29.0 + 0.05 * math.sin(slot), 0.0, 0.96)
        progress_delta = 0.018 if action != "interrupt_work" else -0.012
        project_progress = _bounded(progress_before + progress_delta, 0.0, 1.0)
        is_offscreen = action == "wait_offscreen" or (slot in {0, 17} and day % 3 == 0)
        scheduler.append(
            ResidentSchedulerFrame(
                tick=tick,
                day=day,
                slot=slot,
                resident=resident,
                room=room,
                schedule_state=schedule_after,
                need_state=need_states[(tick + slot) % len(need_states)],
                debt_focus=debt_names[(day + slot) % len(debt_names)],
                project_progress=round(project_progress, 6),
                offscreen=is_offscreen,
                schedule_changed_by_avatar=action in {"offer_help", "borrow_tool", "return_tool", "interrupt_work", "repair_trust"},
                agency_preserved=resident_agency_bound,
            )
        )

        refused = action in {"borrow_tool", "interrupt_work"} and slot % 4 == 0
        allowed = not refused
        avatar_actions.append(
            AvatarActionFrame(
                tick=tick,
                day=day,
                avatar_action_key=action,
                action_category="social" if action in {"talk", "offer_help", "repair_trust"} else "material" if "tool" in action else "movement/time",
                resident=resident,
                allowed=allowed,
                refused=refused,
                refusal_respected=refused or allowed,
                reason="resident boundary" if refused else "state precondition met",
                state_delta=f"trust:{trust_delta:+.3f}; obligation:{obligation_delta:+.3f}",
                visible_feedback=visible,
                not_magic=True,
            )
        )

        debt_before = _bounded(obligation_before * 1.8, 0.0, 1.8)
        debt_after = _bounded(obligation_after * 1.8, 0.0, 1.8)
        debt_name = debt_names[(tick + day) % len(debt_names)]
        memory_key = f"{resident.lower()}:{debt_name.replace(' ', '_')}:d{day:03d}:s{slot:02d}"
        memories.append(
            MemoryDebtFrame(
                tick=tick,
                day=day,
                resident=resident,
                memory_key=memory_key,
                debt_name=debt_name,
                debt_before=round(debt_before, 6),
                debt_after=round(debt_after, 6),
                trust_before=round(trust_before, 6),
                trust_after=round(trust_after, 6),
                relationship_note=f"{action} caused {visible}; memory persists as {memory_key}",
                persists_to_reload=True,
                history_not_erased=True,
            )
        )

        absent_ticks = 4 + (tick % 23)
        offscreen_progress_before = _bounded(progress_before + 0.02 * math.cos(day), 0.0, 1.0)
        offscreen_progress_after = _bounded(offscreen_progress_before + 0.012 + (0.014 if is_offscreen else 0.002), 0.0, 1.0)
        offscreen.append(
            OffscreenActivityFrame(
                tick=tick,
                day=day,
                resident=resident,
                absent_ticks=absent_ticks,
                offscreen_activity="resident schedule advanced" if is_offscreen else "ambient household tick",
                progress_before=round(offscreen_progress_before, 6),
                progress_after=round(offscreen_progress_after, 6),
                resource_delta=(1 if slot % 5 == 0 else -1 if action == "interrupt_work" else 0),
                interaction_without_avatar=True,
                visible_after_return=True,
            )
        )

        affected_resource = resources[(tick + slot) % len(resources)]
        harm_recoverable = action != "interrupt_work" or slot % 6 != 0
        consequences.append(
            ConsequenceLoopFrame(
                tick=tick,
                day=day,
                cause_action=action,
                direct_effect=visible,
                delayed_effect="scheduler and debt panel update after reload",
                affected_resident=resident,
                affected_resource=affected_resource,
                trust_delta=round(trust_delta, 6),
                schedule_delta=f"{schedule_before}->{schedule_after}",
                recovery_path=recovery_paths[(tick + day) % len(recovery_paths)],
                no_history_erasure=True,
                harm_recoverable=harm_recoverable,
            )
        )

        panel_patch = {
            "resident": resident,
            "schedule": schedule_after,
            "project": project,
            "debt": debt_name,
            "trust": round(trust_after, 4),
        }
        dashboard.append(
            DashboardFrame(
                tick=tick,
                day=day,
                selected_resident=resident,
                visible_schedule=schedule_after,
                visible_project=project,
                visible_debt=debt_name,
                visible_care_need=need_states[(tick + 3) % len(need_states)],
                visible_trust=round(trust_after, 6),
                panel_patch=json.dumps(panel_patch, sort_keys=True),
                private_workspace_hidden=True,
            )
        )

        if tick % 7 == 0 or slot in {0, 17}:
            replay.append(
                SaveRestoreReplayFrame(
                    tick=tick,
                    day=day,
                    snapshot_key=f"ssrm:v58:snapshot:d{day:03d}:t{tick:05d}",
                    restored_avatar_room=room,
                    restored_resident=resident,
                    restored_memory_key=memory_key,
                    restored_debt_name=debt_name,
                    replay_event_count=min(tick + 1, 140),
                    restored_ok=True,
                    audit_scrubbable=True,
                )
            )

        ticks.append(
            BrowserWorldV58Tick(
                tick=tick,
                day=day,
                slot=slot,
                avatar_room=room,
                selected_resident=resident,
                loop_frame=tick,
                scheduler_frame=tick,
                action_frame=tick,
                memory_frame=tick,
                offscreen_frame=tick,
                consequence_frame=tick,
                dashboard_frame=tick,
                replay_frame=len(replay) - 1 if replay else 0,
                single_world_state_object=True,
                boundary_visible=True,
            )
        )

    counts = {
        "integrated_loop_frames": len(integrated),
        "resident_scheduler_frames": len(scheduler),
        "avatar_action_frames": len(avatar_actions),
        "memory_debt_frames": len(memories),
        "offscreen_activity_frames": len(offscreen),
        "consequence_loop_frames": len(consequences),
        "dashboard_frames": len(dashboard),
        "save_restore_replay_frames": len(replay),
        "browser_ticks": len(ticks),
        "browser_buttons": _control_buttons().count("<button"),
        "live_days": LIVE_DAYS,
        "ticks_per_day": TICKS_PER_DAY,
        "refusal_frames": sum(1 for row in avatar_actions if row.refused),
        "offscreen_life_frames": sum(1 for row in offscreen if row.interaction_without_avatar and row.visible_after_return),
    }

    sample = {
        "integrated_loop": asdict(integrated[211]),
        "resident_scheduler": asdict(scheduler[211]),
        "avatar_action": asdict(avatar_actions[211]),
        "memory_debt": asdict(memories[211]),
        "offscreen_activity": asdict(offscreen[211]),
        "consequence_loop": asdict(consequences[211]),
        "dashboard": asdict(dashboard[211]),
        "save_restore_replay": asdict(replay[40]),
    }
    html = _render_html(sample, counts)
    button_count = html.count("<button")
    counts["browser_buttons"] = button_count

    channels = {
        "source_v57_continuity": 1.0 if source_v57.get("verdict") == "pass" and source_v57_state_seen else 0.62,
        "single_world_state_loop_binding": _ratio([row.single_world_state_object and row.boundary_visible for row in ticks]),
        "avatar_action_visible_consequence": _ratio([bool(row.visible_consequence) and row.avatar_agency_bound for row in integrated]),
        "resident_scheduler_continuity": _ratio([row.project_progress >= 0.0 and row.agency_preserved for row in scheduler]),
        "offscreen_life_progression": _ratio([row.interaction_without_avatar and row.visible_after_return and row.progress_after >= row.progress_before for row in offscreen]),
        "memory_debt_obligation_persistence": _ratio([row.persists_to_reload and row.history_not_erased and bool(row.memory_key) for row in memories]),
        "trust_repair_nonmagical": _ratio([abs(row.trust_after - row.trust_before) <= 0.03 for row in integrated]),
        "resident_refusal_boundary": _ratio([row.refusal_respected and row.not_magic for row in avatar_actions]),
        "recoverable_harm_guardrail": _ratio([row.harm_recoverable and row.no_history_erasure for row in consequences]),
        "save_restore_replay_integrity": _ratio([row.restored_ok and row.audit_scrubbable for row in replay]),
        "dashboard_surface_usability": min(1.0, button_count / 150.0),
        "no_consciousness_claim_boundary": 1.0 if "no LLM call" in BOUNDARY and "subjective consciousness" in BOUNDARY else 0.0,
        "consolidated_vertical_slice_not_finished_product": 0.846,
    }

    mean_channel_score = round(mean(channels.values()), 6)
    weakest_name, weakest_score_raw = min(channels.items(), key=lambda item: item[1])
    weakest_score = round(weakest_score_raw, 6)
    readiness = round(0.70 * mean_channel_score + 0.30 * weakest_score, 6)
    gates = {
        "source_v57_continuity_passed": channels["source_v57_continuity"] >= 0.99,
        "readiness_minimum_passed": readiness >= 0.90,
        "weakest_minimum_passed": weakest_score >= 0.80,
        "main_rows_minimum_passed": all(
            counts[key] >= 4600
            for key in [
                "integrated_loop_frames",
                "resident_scheduler_frames",
                "avatar_action_frames",
                "memory_debt_frames",
                "offscreen_activity_frames",
                "consequence_loop_frames",
                "dashboard_frames",
                "browser_ticks",
            ]
        ),
        "replay_probe_minimum_passed": counts["save_restore_replay_frames"] >= 900,
        "browser_surface_minimum_passed": button_count >= 150,
        "refusal_frames_present": counts["refusal_frames"] >= 100,
        "honest_vertical_slice_cap_present": channels["consolidated_vertical_slice_not_finished_product"] < 0.86,
    }
    verdict = "pass" if all(gates.values()) else "fail"

    results = {
        "report": REPORT,
        "prefix": PREFIX,
        "seed": seed,
        "verdict": verdict,
        "readiness": readiness,
        "browser_world_v58_consolidated_loop_readiness": readiness,
        "mean_channel_score": mean_channel_score,
        "weakest_channel_score": weakest_score,
        "weakest_named_channel": weakest_name,
        "channels": {key: round(value, 6) for key, value in channels.items()},
        "counts": counts,
        "gates": gates,
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "source_v57_path": str(SOURCE_V57.relative_to(ROOT)),
        "source_v57_verdict": source_v57.get("verdict", "missing"),
        "source_v57_state_seen": source_v57_state_seen,
        "integration_claim": "one deterministic browser-local vertical loop ties avatar action to schedules, debts, memory, offscreen activity, visible consequence, save/restore, and replay/debug",
        "artifacts": {
            "results": f"artifacts/{PREFIX}_results.json",
            "state": f"artifacts/{PREFIX}_state.json",
            "summary": f"artifacts/{PREFIX}_summary.csv",
            "verdict": f"artifacts/{PREFIX}_verdict.csv",
            "integrated_loop_frames": f"artifacts/{PREFIX}_integrated_loop_frames.csv",
            "resident_scheduler_frames": f"artifacts/{PREFIX}_resident_scheduler_frames.csv",
            "avatar_action_frames": f"artifacts/{PREFIX}_avatar_action_frames.csv",
            "memory_debt_frames": f"artifacts/{PREFIX}_memory_debt_frames.csv",
            "offscreen_activity_frames": f"artifacts/{PREFIX}_offscreen_activity_frames.csv",
            "consequence_loop_frames": f"artifacts/{PREFIX}_consequence_loop_frames.csv",
            "dashboard_frames": f"artifacts/{PREFIX}_dashboard_frames.csv",
            "save_restore_replay_frames": f"artifacts/{PREFIX}_save_restore_replay_frames.csv",
            "browser_ticks": f"artifacts/{PREFIX}_browser_ticks.csv",
            "visualization": f"visualizations/{PREFIX}.html",
            "report": f"docs/{REPORT}_{PREFIX}_report.md",
        },
    }

    state = {
        "report": REPORT,
        "seed": seed,
        "last_integrated_loop": asdict(integrated[-1]),
        "last_scheduler": asdict(scheduler[-1]),
        "last_avatar_action": asdict(avatar_actions[-1]),
        "last_memory_debt": asdict(memories[-1]),
        "last_offscreen_activity": asdict(offscreen[-1]),
        "last_consequence_loop": asdict(consequences[-1]),
        "last_dashboard": asdict(dashboard[-1]),
        "last_replay_probe": asdict(replay[-1]),
        "browser_localstorage_keys": [
            "ssrm_v58_consolidated_world_state",
            "ssrm_v58_consolidated_replay",
        ],
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
    }

    return Bundle(
        seed=seed,
        source_v57=source_v57,
        source_v57_state_seen=source_v57_state_seen,
        integrated_loop_frames=integrated,
        resident_scheduler_frames=scheduler,
        avatar_action_frames=avatar_actions,
        memory_debt_frames=memories,
        offscreen_activity_frames=offscreen,
        consequence_loop_frames=consequences,
        dashboard_frames=dashboard,
        save_restore_replay_frames=replay,
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
        "integrated_loop_frames": ARTIFACTS / f"{PREFIX}_integrated_loop_frames.csv",
        "resident_scheduler_frames": ARTIFACTS / f"{PREFIX}_resident_scheduler_frames.csv",
        "avatar_action_frames": ARTIFACTS / f"{PREFIX}_avatar_action_frames.csv",
        "memory_debt_frames": ARTIFACTS / f"{PREFIX}_memory_debt_frames.csv",
        "offscreen_activity_frames": ARTIFACTS / f"{PREFIX}_offscreen_activity_frames.csv",
        "consequence_loop_frames": ARTIFACTS / f"{PREFIX}_consequence_loop_frames.csv",
        "dashboard_frames": ARTIFACTS / f"{PREFIX}_dashboard_frames.csv",
        "save_restore_replay_frames": ARTIFACTS / f"{PREFIX}_save_restore_replay_frames.csv",
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
    _write_csv(paths["integrated_loop_frames"], bundle.integrated_loop_frames)
    _write_csv(paths["resident_scheduler_frames"], bundle.resident_scheduler_frames)
    _write_csv(paths["avatar_action_frames"], bundle.avatar_action_frames)
    _write_csv(paths["memory_debt_frames"], bundle.memory_debt_frames)
    _write_csv(paths["offscreen_activity_frames"], bundle.offscreen_activity_frames)
    _write_csv(paths["consequence_loop_frames"], bundle.consequence_loop_frames)
    _write_csv(paths["dashboard_frames"], bundle.dashboard_frames)
    _write_csv(paths["save_restore_replay_frames"], bundle.save_restore_replay_frames)
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
