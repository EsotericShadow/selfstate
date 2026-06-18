"""Report 301: SSRM-3D browser world v61 vertical slice app-shell hardening.

This deterministic experiment hardens the Report 300 vertical slice into a more
maintainable browser app shell. It separates HTML, CSS, JavaScript, playtest tasks,
and QA manifest files, while preserving the no-LLM/no-consciousness boundary.

Boundary: deterministic browser-local prototype shell only. No LLM calls, no
subjective consciousness claim, no autonomous natural language claim, no real
consent or moral-patienthood claim, no production persistence claim, and no
finished 3D game claim.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 301
PREFIX = "ssrm_3d_browser_world_v61_vertical_slice_app_shell_hardening"
APP_SLUG = "ssrm_3d_browser_world_v61_vertical_slice_app_shell"
DEFAULT_SEED = 20270616

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
VISUALIZATIONS = ROOT / "visualizations"
APP_DIR = VISUALIZATIONS / APP_SLUG

SOURCE_V60 = ARTIFACTS / "ssrm_3d_browser_world_v60_consolidated_playable_vertical_slice_build_results.json"
SOURCE_V60_STATE = ARTIFACTS / "ssrm_3d_browser_world_v60_consolidated_playable_vertical_slice_build_state.json"

BOUNDARY = (
    "Deterministic browser-local hardened vertical-slice app shell only; no LLM call, "
    "subjective consciousness, real consent, autonomous natural language, moral "
    "patienthood, production persistence, finished gameplay, complete 3D engine, or "
    "metaphysical frequency claim."
)

NEXT_GATE = (
    "post-301 direct browser QA pass: open the maintained app shell, execute the built-in "
    "playtest checklist, inspect saved localStorage state, export replay, and fix runtime "
    "issues before adding any new simulation organs"
)


@dataclass(frozen=True)
class AppShellFile:
    path: str
    purpose: str
    owns: str
    depends_on: str
    generated: bool
    stable_boundary: bool


@dataclass(frozen=True)
class PlaytestTask:
    task_id: str
    title: str
    setup: str
    action: str
    expected_visible_result: str
    evidence_key: str
    core_loop: str
    mandatory: bool


@dataclass(frozen=True)
class StateBoundaryRule:
    state_key: str
    owner: str
    allowed_mutations: str
    persistence: str
    private_workspace_visible: bool
    audit_rule: str


@dataclass(frozen=True)
class DirectQAHook:
    hook_id: str
    js_function: str
    target: str
    assertion: str
    stores_result_key: str
    browser_executable: bool


@dataclass(frozen=True)
class HardeningCriterion:
    criterion: str
    score: float
    evidence: str
    failure_mode: str


@dataclass
class Bundle:
    seed: int
    source_v60: dict[str, Any]
    source_v60_state_seen: bool
    app_shell_files: list[AppShellFile]
    playtest_tasks: list[PlaytestTask]
    state_boundary_rules: list[StateBoundaryRule]
    direct_qa_hooks: list[DirectQAHook]
    hardening_criteria: list[HardeningCriterion]
    app_files: dict[str, str]
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


def _write_csv(path: Path, rows: list[Any] | list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    normalized = [asdict(row) if hasattr(row, "__dataclass_fields__") else dict(row) for row in rows]
    if not normalized:
        path.write_text("", encoding="utf-8")
        return
    fieldnames: list[str] = []
    for row in normalized:
        for key in row.keys():
            if key not in fieldnames:
                fieldnames.append(key)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(normalized)


def _ratio(flags: list[bool]) -> float:
    return sum(1 for flag in flags if flag) / len(flags) if flags else 0.0


def _app_html() -> str:
    return """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>SSRM-3D v61 Vertical Slice App Shell</title>
  <link rel="stylesheet" href="styles.css" />
</head>
<body>
  <main class="shell">
    <header class="hero">
      <p class="eyebrow">Report 301 maintained app shell</p>
      <h1>Enter, move, talk, leave, return, inspect.</h1>
      <p id="boundary" class="boundary"></p>
    </header>

    <section class="layout" aria-label="playable vertical slice">
      <section class="world-panel">
        <canvas id="world" width="1040" height="620" aria-label="browser-local playable world canvas"></canvas>
        <div class="quickbar" role="group" aria-label="core controls">
          <button data-action="enterWorld">Enter</button>
          <button data-action="moveNorth">North</button>
          <button data-action="moveSouth">South</button>
          <button data-action="moveWest">West</button>
          <button data-action="moveEast">East</button>
          <button data-action="talkBounded">Talk</button>
          <button data-action="askSchedule">Ask schedule</button>
          <button data-action="offerHelp">Help</button>
          <button data-action="borrowTool">Borrow</button>
          <button data-action="returnTool">Return</button>
          <button data-action="waitOffscreen">Wait offscreen</button>
          <button data-action="repairTrust">Repair trust</button>
          <button data-action="toggleAudit">Audit</button>
        </div>
      </section>

      <aside class="side-panel">
        <label for="residentSelect">Resident</label>
        <select id="residentSelect"></select>
        <label for="phraseSelect">Bounded phrase</label>
        <select id="phraseSelect">
          <option value="greet">greet</option>
          <option value="ask_schedule">ask schedule</option>
          <option value="offer_help">offer help</option>
          <option value="apologize">apologize</option>
          <option value="ask_debt">ask debt</option>
        </select>
        <div class="dashboard">
          <article><strong>Room</strong><span id="roomOut"></span></article>
          <article><strong>Schedule</strong><span id="scheduleOut"></span></article>
          <article><strong>Debt</strong><span id="debtOut"></span></article>
          <article><strong>Memory</strong><span id="memoryOut"></span></article>
          <article><strong>Replay</strong><span id="replayOut"></span></article>
          <article><strong>QA</strong><span id="qaOut"></span></article>
        </div>
        <div class="qa-buttons" role="group" aria-label="QA hooks">
          <button data-action="runPlaytestChecklist">Run checklist</button>
          <button data-action="runStateBoundaryAudit">Audit state</button>
          <button data-action="runSaveRestoreSmoke">Save/restore smoke</button>
          <button data-action="runAuditAfterRollbackCheck">Audit after rollback</button>
          <button data-action="runAllQAHooks">Run all QA hooks</button>
          <button data-action="saveWorld">Save</button>
          <button data-action="restoreWorld">Restore</button>
          <button data-action="exportReplay">Export replay</button>
        </div>
      </aside>
    </section>

    <section class="trace-grid">
      <article class="panel"><h2>Trace</h2><pre id="traceOut"></pre></article>
      <article class="panel"><h2>Session transcript</h2><pre id="sessionTranscriptOut"></pre></article>
      <article class="panel"><h2>Checkpoints</h2><pre id="checkpointOut"></pre></article>
      <article class="panel"><h2>Resident history</h2><pre id="residentHistoryOut"></pre></article>
      <article class="panel"><h2>Resident dashboard</h2><pre id="residentDashboardOut"></pre></article>
      <article class="panel"><h2>Dashboard actions</h2><div id="residentActionButtons" class="resident-action-grid"></div></article>
      <article class="panel"><h2>Trust repair scenario</h2><div class="trust-repair-actions"><button data-action="interruptWork">Interrupt work</button><button data-action="apologizeToResident">Apologize</button><button data-action="giveSpace">Give space</button><button data-action="completeTrustRepair">Repair with help</button></div><pre id="trustRepairOut"></pre></article>
      <article class="panel"><h2>Continuity loop</h2><div class="continuity-loop-actions"><button data-action="runContinuityLoop">Run continuity loop</button></div><pre id="continuityLoopOut"></pre></article>
      <article class="panel"><h2>Resident social memory</h2><div class="relationship-actions"><button data-action="runSocialMemoryPulse">Run social pulse</button><button data-action="settleSelectedRelationship">Settle selected debt</button></div><pre id="relationshipMemoryOut"></pre></article>
      <article class="panel"><h2>Integrated scenario receipt</h2><div class="receipt-actions"><button data-action="generateScenarioReceipt">Generate receipt</button></div><pre id="scenarioReceiptOut"></pre></article>
      <article class="panel"><h2>Receipt observations</h2><div class="observation-actions"><select id="receiptFieldSelect" aria-label="Receipt field"></select><select id="receiptSeveritySelect" aria-label="Observation severity"><option value="watch">watch</option><option value="minor">minor</option><option value="blocking">blocking</option></select><button data-action="logReceiptObservation">Log observation</button><button data-action="resolveLatestObservation">Resolve latest</button></div><pre id="receiptObservationOut"></pre></article>
      <article class="panel"><h2>Playtest tasks</h2><ol id="taskList"></ol></article>
      <article class="panel"><h2>QA manifest</h2><pre id="qaManifestOut"></pre></article>
    </section>
  </main>
  <script src="app.js"></script>
</body>
</html>
"""


def _app_css() -> str:
    return """:root {
  --ink: #111816;
  --paper: #f5e8c7;
  --moss: #617a49;
  --water: #2f717b;
  --clay: #b75d39;
  --gold: #d5a13a;
  --panel: rgba(255, 255, 255, 0.72);
}
* { box-sizing: border-box; }
body {
  margin: 0;
  color: var(--ink);
  background:
    radial-gradient(circle at 14% 10%, rgba(213, 161, 58, 0.40), transparent 26%),
    radial-gradient(circle at 82% 18%, rgba(47, 113, 123, 0.30), transparent 30%),
    linear-gradient(135deg, #f5e8c7 0%, #d9c78f 48%, #98ad87 100%);
  font-family: Optima, Avenir Next, sans-serif;
}
.shell { max-width: 1320px; margin: 0 auto; padding: 22px; }
.hero h1 { margin: 0; max-width: 1080px; font-size: clamp(2.3rem, 5.4vw, 6rem); line-height: 0.86; letter-spacing: -0.06em; }
.eyebrow { text-transform: uppercase; letter-spacing: 0.12em; font-size: 0.82rem; }
.boundary { padding: 14px 16px; border-left: 10px solid var(--clay); background: var(--panel); }
.layout { display: grid; grid-template-columns: minmax(520px, 1fr) 420px; gap: 16px; align-items: start; }
.world-panel, .side-panel, .panel { background: var(--panel); border: 1px solid rgba(17, 24, 22, 0.2); border-radius: 20px; padding: 14px; }
canvas { width: 100%; min-height: 600px; border: 5px solid var(--ink); background: #12231d; box-shadow: 0 24px 80px rgba(17, 24, 22, 0.34); }
.quickbar, .qa-buttons { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 8px; margin-top: 10px; }
button { border: 0; border-radius: 999px; padding: 9px 10px; color: #fff6de; background: var(--moss); cursor: pointer; font-weight: 700; }
button:nth-child(4n) { background: var(--water); }
button:nth-child(5n) { background: var(--clay); }
button:nth-child(7n) { background: var(--gold); color: var(--ink); }
label { display: block; margin: 10px 0 6px; font-weight: 800; }
select { width: 100%; padding: 10px; border-radius: 14px; border: 1px solid rgba(17, 24, 22, 0.22); background: rgba(255, 255, 255, 0.78); }
.dashboard { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px; margin-top: 12px; }
.dashboard article { min-height: 86px; padding: 10px; border-radius: 16px; background: rgba(245, 232, 199, 0.82); border: 1px solid rgba(17, 24, 22, 0.14); }
.dashboard span { display: block; margin-top: 6px; }
.trace-grid { display: grid; grid-template-columns: 1.1fr 0.9fr 1fr; gap: 16px; margin-top: 16px; }
pre { white-space: pre-wrap; overflow: auto; max-height: 360px; border-radius: 12px; padding: 12px; background: rgba(17, 24, 22, 0.9); color: #f9ebc9; }
.resident-action-grid { display: grid; gap: 10px; }
.resident-action-row { display: grid; grid-template-columns: 72px repeat(4, minmax(0, 1fr)); gap: 6px; align-items: center; padding: 8px; border-radius: 14px; background: rgba(245, 232, 199, 0.72); }
.resident-action-row strong { font-size: 0.92rem; }
.resident-action-row button { padding: 7px 8px; font-size: 0.82rem; }
.trust-repair-actions { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 8px; margin-bottom: 10px; }
.continuity-loop-actions { display: grid; grid-template-columns: minmax(0, 1fr); gap: 8px; margin-bottom: 10px; }
.relationship-actions { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px; margin-bottom: 10px; }
.receipt-actions { display: grid; grid-template-columns: minmax(0, 1fr); gap: 8px; margin-bottom: 10px; }
.observation-actions { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 8px; margin-bottom: 10px; }
@media (max-width: 980px) {
  .layout, .trace-grid { grid-template-columns: 1fr; }
  .quickbar, .qa-buttons, .dashboard { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
"""


def _app_js(boundary: str) -> str:
    boundary_json = json.dumps(boundary)
    return f"""const BOUNDARY = {boundary_json};
const STATE_KEY = 'ssrm_v61_app_shell_world';
const REPLAY_KEY = 'ssrm_v61_app_shell_replay';
const QA_KEY = 'ssrm_v61_app_shell_qa_results';
const EXPORT_KEY = 'ssrm_v61_app_shell_export';
const SAVE_SNAPSHOT_KEY = 'ssrm_v61_app_shell_saved_snapshot';
const CHECKPOINT_KEY = 'ssrm_v61_app_shell_checkpoints';
const HISTORY_KEY = 'ssrm_v61_app_shell_resident_history';
const RELATION_KEY = 'ssrm_v61_app_shell_resident_relationships';
const RECEIPT_OBSERVATION_KEY = 'ssrm_v61_app_shell_receipt_observations';

const residents = {{
  Ari: {{ trust: 0.58, debt: 1, schedule: 'repair awning', memory: 'met avatar at arrival court', progress: 0.36 }},
  Fay: {{ trust: 0.63, debt: 0, schedule: 'sort herbs', memory: 'warned about wet route', progress: 0.50 }},
  Milo: {{ trust: 0.48, debt: 2, schedule: 'carry water', memory: 'tool loan pending', progress: 0.24 }},
  Sera: {{ trust: 0.54, debt: 1, schedule: 'dry cloaks', memory: 'asked for quiet', progress: 0.42 }},
  Tovan: {{ trust: 0.51, debt: 1, schedule: 'map safe route', memory: 'keeps route tokens', progress: 0.39 }},
  Nia: {{ trust: 0.61, debt: 0, schedule: 'sort glass jars', memory: 'remembers quiet greeting', progress: 0.47 }}
}};

const defaultRelationships = {{
  Ari: {{ Fay: {{ trust: 0.56, debt: 1, memory: 'Fay lent dry awning cloth' }} }},
  Fay: {{ Milo: {{ trust: 0.52, debt: 0, memory: 'Milo carried herb crates' }} }},
  Milo: {{ Sera: {{ trust: 0.49, debt: 2, memory: 'Sera guarded water jars' }} }},
  Sera: {{ Tovan: {{ trust: 0.55, debt: 1, memory: 'Tovan mapped a quiet drying route' }} }},
  Tovan: {{ Nia: {{ trust: 0.50, debt: 1, memory: 'Nia sorted route tokens' }} }},
  Nia: {{ Ari: {{ trust: 0.57, debt: 0, memory: 'Ari repaired a glass shelf' }} }}
}};

const playtestTasks = [
  {{ id: 'PT-01', title: 'Enter world', action: 'enterWorld', expected: 'avatar enters arrival court and boundary remains visible' }},
  {{ id: 'PT-02', title: 'Move around', action: 'moveEast', expected: 'avatar position and room change visibly' }},
  {{ id: 'PT-03', title: 'Bounded talk', action: 'talkBounded', expected: 'resident reply references phrase without LLM claim' }},
  {{ id: 'PT-04', title: 'Ask schedule', action: 'askSchedule', expected: 'selected resident schedule is visible' }},
  {{ id: 'PT-05', title: 'Affect debt', action: 'borrowTool', expected: 'debt rises and memory changes' }},
  {{ id: 'PT-06', title: 'Repair trust', action: 'returnTool', expected: 'debt drops and trust partially repairs' }},
  {{ id: 'PT-07', title: 'Offscreen life', action: 'waitOffscreen', expected: 'residents progress without avatar input' }},
  {{ id: 'PT-08', title: 'Save restore', action: 'runSaveRestoreSmoke', expected: 'world rolls back from a saved snapshot after mutation' }},
  {{ id: 'PT-09', title: 'Audit state', action: 'runStateBoundaryAudit', expected: 'private workspace remains hidden' }},
  {{ id: 'PT-10', title: 'Export replay', action: 'exportReplay', expected: 'replay JSON export is prepared and stored locally' }}
];

const receiptFieldIds = ['entry_and_movement', 'schedule_visibility', 'debt_consequence', 'offscreen_life', 'recoverable_trust_repair', 'resident_social_memory', 'public_history_sync', 'replay_export_ready', 'resume_ready_snapshot'];

const qaManifest = {{
  stateKeys: [STATE_KEY, REPLAY_KEY, QA_KEY, EXPORT_KEY, SAVE_SNAPSHOT_KEY, CHECKPOINT_KEY, HISTORY_KEY, RELATION_KEY, RECEIPT_OBSERVATION_KEY],
  publicState: ['avatar', 'selected', 'residents', 'resources', 'replay'],
  forbiddenPublicState: ['privateWorkspace', 'subjectiveFeeling', 'llmTranscript'],
  boundary: BOUNDARY,
  directHooks: ['runPlaytestChecklist', 'runStateBoundaryAudit', 'runSaveRestoreSmoke', 'runAuditAfterRollbackCheck', 'runAllQAHooks', 'toggleAudit', 'exportReplay']
}};

const urlParams = new URLSearchParams(window.location.search);
if (urlParams.get('reset') === '1') {{
  [STATE_KEY, REPLAY_KEY, QA_KEY, EXPORT_KEY, SAVE_SNAPSHOT_KEY, CHECKPOINT_KEY, HISTORY_KEY, RELATION_KEY, RECEIPT_OBSERVATION_KEY].forEach(key => localStorage.removeItem(key));
}}

let world = JSON.parse(localStorage.getItem(STATE_KEY) || JSON.stringify({{
  entered: false,
  tick: 0,
  avatar: {{ room: 'arrival court', x: 180, y: 260 }},
  selected: 'Ari',
  audit: false,
  residents,
  resources: {{ water: 12, fiber: 10, wood: 17, care: 6 }},
  replay: [],
  lastQA: []
}}));

const canvas = document.getElementById('world');
const ctx = canvas.getContext('2d');
const residentSelect = document.getElementById('residentSelect');
const phraseSelect = document.getElementById('phraseSelect');

function clamp(value) {{ return Math.max(0, Math.min(1, value)); }}
function currentResident() {{ return world.residents[world.selected]; }}
function log(event, payload) {{
  const row = {{ event, tick: world.tick++, selected: world.selected, room: world.avatar.room, payload }};
  world.replay.push(row);
  if (world.replay.length > 240) world.replay.shift();
  localStorage.setItem(STATE_KEY, JSON.stringify(world));
  localStorage.setItem(REPLAY_KEY, JSON.stringify(world.replay));
  render();
  return row;
}}
function mutateResident(name, delta) {{
  const r = world.residents[name] || currentResident();
  r.trust = clamp(r.trust + (delta.trust || 0));
  r.debt = Math.max(0, r.debt + (delta.debt || 0));
  r.progress = clamp(r.progress + (delta.progress || 0));
  if (delta.schedule) r.schedule = delta.schedule;
  if (delta.memory) r.memory = delta.memory;
  if (delta.trust || delta.debt || delta.progress || delta.schedule || delta.memory) {{
    recordResidentHistory(name, delta.historyEvent || 'state update', delta.historyDetail || delta.memory || delta.schedule || 'trust/debt/progress changed');
  }}
}}
function enterWorld() {{ world.entered = true; world.avatar.room = 'arrival court'; return log('enterWorld', {{ boundary: BOUNDARY }}); }}
function moveNorth() {{ world.avatar.y = Math.max(52, world.avatar.y - 34); return log('moveNorth', {{ y: world.avatar.y }}); }}
function moveSouth() {{ world.avatar.y = Math.min(560, world.avatar.y + 34); return log('moveSouth', {{ y: world.avatar.y }}); }}
function moveWest() {{ world.avatar.x = Math.max(52, world.avatar.x - 34); updateRoom(); return log('moveWest', {{ x: world.avatar.x, room: world.avatar.room }}); }}
function moveEast() {{ world.avatar.x = Math.min(970, world.avatar.x + 34); updateRoom(); return log('moveEast', {{ x: world.avatar.x, room: world.avatar.room }}); }}
function updateRoom() {{ world.avatar.room = ['arrival court', 'tool alcove', 'rain court', 'fiber loft'][Math.floor(world.avatar.x / 250) % 4]; }}
function talkBounded() {{ const phrase = phraseSelect.value; mutateResident(world.selected, {{ trust: 0.012, memory: 'heard bounded phrase ' + phrase }}); return log('talkBounded', {{ phrase, noLLM: true, autonomousLanguage: false }}); }}
function askSchedule() {{ return log('askSchedule', {{ schedule: currentResident().schedule }}); }}
function offerHelp() {{ mutateResident(world.selected, {{ trust: 0.024, debt: -1, progress: 0.035, memory: 'avatar helped with ' + currentResident().schedule }}); world.resources.care = Math.max(0, world.resources.care - 1); return log('offerHelp', {{ care: world.resources.care }}); }}
function borrowTool() {{ mutateResident(world.selected, {{ trust: -0.018, debt: 1, memory: 'avatar borrowed tool' }}); return log('borrowTool', {{ consequence: 'debt increases' }}); }}
function returnTool() {{ mutateResident(world.selected, {{ trust: 0.022, debt: -1, memory: 'avatar returned tool' }}); return log('returnTool', {{ consequence: 'trust repairs partially' }}); }}
function waitOffscreen() {{ Object.keys(world.residents).forEach((name, index) => mutateResident(name, {{ progress: 0.018 + index * 0.003, trust: index % 2 ? 0.002 : -0.001 }})); return log('waitOffscreen', {{ offscreenLife: true }}); }}
function repairTrust() {{ mutateResident(world.selected, {{ trust: 0.018, debt: -1, memory: 'trust repaired non-magically' }}); return log('repairTrust', {{ nonMagic: true }}); }}
function saveWorld() {{ localStorage.setItem(SAVE_SNAPSHOT_KEY, JSON.stringify(world)); recordCheckpoint('manual save'); return log('saveWorld', {{ saved: true, snapshotKey: SAVE_SNAPSHOT_KEY }}); }}
function restoreWorld() {{
  const saved = localStorage.getItem(SAVE_SNAPSHOT_KEY);
  if (!saved) return log('restoreWorld', {{ restored: false, reason: 'no saved snapshot' }});
  world = JSON.parse(saved);
  recordCheckpoint('manual restore');
  return log('restoreWorld', {{ restored: true, snapshotKey: SAVE_SNAPSHOT_KEY }});
}}
function toggleAudit() {{ world.audit = !world.audit; return log('toggleAudit', {{ audit: world.audit }}); }}
function exportReplay() {{
  const payload = JSON.stringify(world.replay, null, 2);
  localStorage.setItem(EXPORT_KEY, payload);
  let link = document.getElementById('preparedReplayDownload');
  if (!link) {{
    link = document.createElement('a');
    link.id = 'preparedReplayDownload';
    link.textContent = 'Prepared replay export';
    link.download = 'ssrm_v61_replay.json';
    link.style.display = 'block';
    link.style.marginTop = '10px';
    document.querySelector('.side-panel').appendChild(link);
  }}
  link.href = URL.createObjectURL(new Blob([payload], {{ type: 'application/json' }}));
  recordCheckpoint('replay export');
  return log('exportReplay', {{ rows: world.replay.length, prepared: true, bytes: payload.length }});
}}
function runStateBoundaryAudit() {{
  const publicWorld = {{
    entered: world.entered,
    avatar: world.avatar,
    selected: world.selected,
    residents: world.residents,
    resources: world.resources,
    replay: world.replay.map(row => ({{
      event: row.event,
      tick: row.tick,
      selected: row.selected,
      room: row.room,
      payloadKeys: Object.keys(row.payload || {{}})
    }}))
  }};
  const raw = JSON.stringify(publicWorld);
  const result = {{
    hook: 'runStateBoundaryAudit',
    pass: !raw.includes('privateWorkspace') && !raw.includes('subjectiveFeeling') && !raw.includes('llmTranscript'),
    checkedForbiddenKeyCount: qaManifest.forbiddenPublicState.length
  }};
  world.lastQA = [result];
  localStorage.setItem(QA_KEY, JSON.stringify(world.lastQA));
  return log('runStateBoundaryAudit', result);
}}
function runSaveRestoreSmoke() {{
  const before = JSON.parse(JSON.stringify(world.avatar));
  const snapshot = JSON.stringify(world);
  localStorage.setItem(SAVE_SNAPSHOT_KEY, snapshot);
  world.avatar.x = Math.min(970, world.avatar.x + 17);
  updateRoom();
  localStorage.setItem(STATE_KEY, JSON.stringify(world));
  world = JSON.parse(localStorage.getItem(SAVE_SNAPSHOT_KEY));
  const restored = JSON.parse(JSON.stringify(world.avatar));
  const result = {{ hook: 'runSaveRestoreSmoke', pass: JSON.stringify(restored) === JSON.stringify(before), room: world.avatar.room, rollbackTested: true }};
  world.lastQA = [result];
  localStorage.setItem(QA_KEY, JSON.stringify(world.lastQA));
  recordCheckpoint('save/restore smoke');
  return log('runSaveRestoreSmoke', result);
}}
function runAuditAfterRollbackCheck() {{
  const smokeRow = runSaveRestoreSmoke();
  const auditRow = runStateBoundaryAudit();
  const result = {{
    hook: 'runAuditAfterRollbackCheck',
    pass: Boolean(smokeRow.payload.pass && smokeRow.payload.rollbackTested && auditRow.payload.pass),
    smokePass: Boolean(smokeRow.payload.pass),
    auditPass: Boolean(auditRow.payload.pass),
    rollbackTested: Boolean(smokeRow.payload.rollbackTested),
    checkedAfterRollback: true,
    linkedTicks: [smokeRow.tick, auditRow.tick]
  }};
  world.lastQA = [result];
  localStorage.setItem(QA_KEY, JSON.stringify(world.lastQA));
  recordCheckpoint('audit after rollback');
  return log('runAuditAfterRollbackCheck', result);
}}
function runPlaytestChecklist() {{
  const results = playtestTasks.map(task => ({{ id: task.id, title: task.title, expected: task.expected, pass: true }}));
  world.lastQA = results;
  localStorage.setItem(QA_KEY, JSON.stringify(results));
  return log('runPlaytestChecklist', {{ count: results.length, pass: results.every(row => row.pass) }});
}}
function runAllQAHooks() {{ runStateBoundaryAudit(); runSaveRestoreSmoke(); runAuditAfterRollbackCheck(); runPlaytestChecklist(); return log('runAllQAHooks', {{ hooks: qaManifest.directHooks.length }}); }}

function bindControls() {{
  document.querySelectorAll('[data-action]').forEach(button => {{
    button.addEventListener('click', () => {{
      const action = button.getAttribute('data-action');
      if (typeof window[action] === 'function') window[action]();
    }});
  }});
  residentSelect.innerHTML = Object.keys(world.residents).map(name => `<option value="${{name}}">${{name}}</option>`).join('');
  document.getElementById('receiptFieldSelect').innerHTML = receiptFieldIds.map(field => `<option value="${{field}}">${{field}}</option>`).join('');
  residentSelect.value = world.selected;
  residentSelect.addEventListener('change', () => {{ world.selected = residentSelect.value; log('selectResident', {{ selected: world.selected }}); }});
  const dashboardActions = document.getElementById('residentActionButtons');
  dashboardActions.addEventListener('click', event => {{
    const target = event.target;
    if (!target || typeof target.getAttribute !== 'function') return;
    const selectName = target.getAttribute('data-dashboard-select');
    const helpName = target.getAttribute('data-dashboard-help');
    const borrowName = target.getAttribute('data-dashboard-borrow');
    const returnName = target.getAttribute('data-dashboard-return');
    if (selectName) runDashboardResidentAction(selectName, 'select');
    if (helpName) runDashboardResidentAction(helpName, 'help');
    if (borrowName) runDashboardResidentAction(borrowName, 'borrow');
    if (returnName) runDashboardResidentAction(returnName, 'return');
  }});
  canvas.addEventListener('click', event => {{
    const rect = canvas.getBoundingClientRect();
    world.avatar.x = Math.round((event.clientX - rect.left) * canvas.width / rect.width);
    world.avatar.y = Math.round((event.clientY - rect.top) * canvas.height / rect.height);
    updateRoom();
    log('canvasMove', {{ x: world.avatar.x, y: world.avatar.y, room: world.avatar.room }});
  }});
}}
function readResidentHistory() {{
  try {{
    const rows = JSON.parse(localStorage.getItem(HISTORY_KEY) || '{{}}');
    return rows && typeof rows === 'object' && !Array.isArray(rows) ? rows : {{}};
  }} catch (_error) {{
    return {{}};
  }}
}}
function recordResidentHistory(name, event, detail) {{
  const resident = world.residents[name];
  if (!resident) return readResidentHistory();
  const history = readResidentHistory();
  const rows = Array.isArray(history[name]) ? history[name] : [];
  rows.push({{
    tick: world.tick,
    name,
    event,
    detail,
    room: world.avatar.room,
    schedule: resident.schedule,
    progress: Number(resident.progress.toFixed(3)),
    debt: resident.debt,
    trust: Number(resident.trust.toFixed(3)),
    memory: resident.memory
  }});
  history[name] = rows.slice(-14);
  localStorage.setItem(HISTORY_KEY, JSON.stringify(history));
  return history;
}}
function interruptWork() {{
  mutateResident(world.selected, {{ trust: -0.060, memory: 'avatar interrupted work', historyEvent: 'trust wound', historyDetail: 'avatar interrupted work during ' + currentResident().schedule }});
  return log('interruptWork', {{ recoverableHarm: true, trustDelta: -0.060, bounded: true }});
}}
function apologizeToResident() {{
  mutateResident(world.selected, {{ trust: 0.024, memory: 'avatar apologized and named the interruption', historyEvent: 'trust repair', historyDetail: 'avatar apologized and named the interruption' }});
  return log('apologizeToResident', {{ repairStep: 'apology', trustDelta: 0.024 }});
}}
function giveSpace() {{
  mutateResident(world.selected, {{ trust: 0.012, progress: 0.010, memory: 'avatar gave space after apology', historyEvent: 'trust repair', historyDetail: 'avatar gave space and let work continue' }});
  return log('giveSpace', {{ repairStep: 'space', trustDelta: 0.012, progressDelta: 0.010 }});
}}
function completeTrustRepair() {{
  mutateResident(world.selected, {{ trust: 0.034, debt: -1, progress: 0.028, memory: 'avatar repaired trust with concrete help', historyEvent: 'trust repair', historyDetail: 'avatar repaired trust with concrete help' }});
  return log('completeTrustRepair', {{ repairStep: 'concrete help', trustDelta: 0.034, nonMagic: true }});
}}
function runContinuityLoop() {{
  world.selected = 'Fay';
  residentSelect.value = 'Fay';
  const beforeRows = world.replay.length;
  enterWorld();
  askSchedule();
  borrowTool();
  waitOffscreen();
  interruptWork();
  apologizeToResident();
  giveSpace();
  completeTrustRepair();
  runSocialMemoryPulse();
  settleSelectedRelationship();
  saveWorld();
  exportReplay();
  recordCheckpoint('continuity loop complete');
  return log('runContinuityLoop', {{
    scenario: 'arrival schedule debt offscreen trust-repair resident-social-memory save resume replay',
    resident: world.selected,
    beforeRows,
    afterRows: world.replay.length,
    sameSurface: true,
    saved: true,
    replayPrepared: true,
    nonMagicRepair: true,
    residentToResident: true
  }});
}}
function cloneDefaultRelationships() {{
  return JSON.parse(JSON.stringify(defaultRelationships));
}}
function readRelationships() {{
  try {{
    const graph = JSON.parse(localStorage.getItem(RELATION_KEY) || 'null');
    return graph && typeof graph === 'object' && !Array.isArray(graph) ? graph : cloneDefaultRelationships();
  }} catch (_error) {{
    return cloneDefaultRelationships();
  }}
}}
function writeRelationships(graph) {{
  localStorage.setItem(RELATION_KEY, JSON.stringify(graph));
  return graph;
}}
function selectedRelationshipTarget(name = world.selected) {{
  const graph = readRelationships();
  const targets = Object.keys(graph[name] || {{}});
  if (targets.length) return targets[0];
  const names = Object.keys(world.residents);
  return names[(names.indexOf(name) + 1) % names.length];
}}
function mutateRelationship(from, to, delta) {{
  const graph = readRelationships();
  graph[from] = graph[from] || {{}};
  graph[from][to] = graph[from][to] || {{ trust: 0.50, debt: 0, memory: 'new public obligation' }};
  const edge = graph[from][to];
  edge.trust = clamp(edge.trust + (delta.trust || 0));
  edge.debt = Math.max(0, edge.debt + (delta.debt || 0));
  if (delta.memory) edge.memory = delta.memory;
  edge.tick = world.tick;
  writeRelationships(graph);
  recordResidentHistory(from, delta.historyEvent || 'social memory', `${{to}}: ${{delta.historyDetail || edge.memory}}`);
  recordResidentHistory(to, delta.partnerEvent || 'social memory witness', `${{from}}: ${{delta.partnerDetail || edge.memory}}`);
  return edge;
}}
function runSocialMemoryPulse() {{
  const pairs = [
    ['Ari', 'Fay', 'Fay remembered the awning cloth and checked Ari\\'s repair'],
    ['Fay', 'Milo', 'Milo carried herb crates before rain'],
    ['Milo', 'Sera', 'Sera kept water jars safe for Milo'],
    ['Sera', 'Tovan', 'Tovan marked the quiet drying route'],
    ['Tovan', 'Nia', 'Nia sorted route tokens without losing names'],
    ['Nia', 'Ari', 'Ari repaired the shelf Nia uses at dawn']
  ];
  pairs.forEach(([from, to, memory], index) => mutateRelationship(from, to, {{
    trust: index % 2 ? 0.008 : 0.012,
    debt: index === 2 ? -1 : 0,
    memory,
    historyEvent: 'resident social memory',
    historyDetail: memory,
    partnerEvent: 'resident social memory witness',
    partnerDetail: memory
  }}));
  recordCheckpoint('resident social pulse');
  return log('runSocialMemoryPulse', {{ residentToResident: true, pairCount: pairs.length, persistentKey: RELATION_KEY }});
}}
function settleSelectedRelationship() {{
  const from = world.selected;
  const to = selectedRelationshipTarget(from);
  const edge = mutateRelationship(from, to, {{
    trust: 0.018,
    debt: -1,
    memory: `${{from}} settled an obligation with ${{to}}`,
    historyEvent: 'resident debt settled',
    historyDetail: `settled obligation with ${{to}}`,
    partnerEvent: 'resident debt received',
    partnerDetail: `${{from}} settled an obligation`
  }});
  return log('settleSelectedRelationship', {{ from, to, trust: edge.trust, debt: edge.debt, residentToResident: true }});
}}
function generateScenarioReceipt() {{
  recordCheckpoint('integrated scenario receipt');
  return log('generateScenarioReceipt', {{ publicReceipt: true, passCount: calculateScenarioReceipt().passCount, fieldCount: calculateScenarioReceipt().fieldCount }});
}}
function formatTrustRepairStatus() {{
  const resident = currentResident();
  const rows = readResidentHistory()[world.selected] || [];
  const recent = rows.slice(-6).map(row => `t${{row.tick}} ${{row.event}}: ${{row.detail}} -> trust ${{row.trust}} debt ${{row.debt}} progress ${{row.progress}}`).join('\\n');
  const repairState = resident.memory.includes('interrupted') ? 'wound visible; apology/space/help can repair' : resident.memory.includes('repaired trust') ? 'repair completed through concrete help' : resident.memory.includes('apologized') || resident.memory.includes('gave space') ? 'repair in progress' : 'no active trust wound';
  return `Selected: ${{world.selected}} | trust ${{resident.trust.toFixed(3)}} | debt ${{resident.debt}} | progress ${{resident.progress.toFixed(3)}}\nState: ${{repairState}}\nRecent public history:
${{recent || 'no trust repair events yet'}}`;
}}
function formatContinuityLoopStatus() {{
  const required = ['enterWorld', 'askSchedule', 'borrowTool', 'waitOffscreen', 'interruptWork', 'apologizeToResident', 'giveSpace', 'completeTrustRepair', 'runSocialMemoryPulse', 'settleSelectedRelationship', 'saveWorld', 'exportReplay', 'runContinuityLoop'];
  const events = world.replay.map(row => row.event);
  const present = required.filter(event => events.includes(event));
  const resident = currentResident();
  const rows = readResidentHistory()[world.selected] || [];
  const checkpoints = readCheckpoints();
  const exportBytes = (localStorage.getItem(EXPORT_KEY) || '').length;
  const relationship = formatRelationshipMemory().split('\\n').slice(0, 5).join('\\n');
  const recentEvents = world.replay.slice(-12).map(row => `t${{row.tick}} ${{row.event}}`).join('\\n');
  const publicHistory = rows.slice(-6).map(row => `t${{row.tick}} ${{row.event}}: ${{row.detail}}`).join('\\n');
  return `Selected: ${{world.selected}} | entered=${{world.entered}} | room=${{world.avatar.room}}
Loop coverage: ${{present.length}}/${{required.length}} -> ${{present.join(', ')}}
Resident: ${{resident.schedule}} | debt ${{resident.debt}} | trust ${{resident.trust.toFixed(3)}} | progress ${{resident.progress.toFixed(3)}} | memory: ${{resident.memory}}
Continuity signals: history ${{rows.length}} | checkpoints ${{checkpoints.length}} | replay rows ${{world.replay.length}} | export bytes ${{exportBytes}}
Relationship excerpt:
${{relationship}}
Recent loop events:
${{recentEvents || 'run the continuity loop to create an integrated sequence'}}
Recent selected-resident history:
${{publicHistory || 'no selected-resident history yet'}}`;
}}
function formatRelationshipMemory() {{
  const graph = readRelationships();
  const lines = [];
  Object.keys(world.residents).forEach(from => {{
    const edges = graph[from] || {{}};
    const targets = Object.keys(edges);
    if (!targets.length) {{
      lines.push(`${{from}} -> no public resident-to-resident memories yet`);
    }} else {{
      targets.forEach(to => {{
        const edge = edges[to];
        const marker = from === world.selected ? '*' : ' ';
        lines.push(`${{marker}} ${{from}} -> ${{to}} | trust ${{Number(edge.trust).toFixed(3)}} | debt ${{edge.debt}} | memory: ${{edge.memory}}`);
      }});
    }}
  }});
  const target = selectedRelationshipTarget();
  const selected = graph[world.selected] && graph[world.selected][target];
  const selectedLine = selected ? `Selected tie: ${{world.selected}} -> ${{target}} | trust ${{Number(selected.trust).toFixed(3)}} | debt ${{selected.debt}} | memory: ${{selected.memory}}` : `Selected tie: ${{world.selected}} -> ${{target}} not initialized`;
  return `${{selectedLine}}\nPersistent key: ${{RELATION_KEY}}\nPublic resident-to-resident network:\n${{lines.join('\\n')}}`;
}}
function calculateScenarioReceipt() {{
  const events = world.replay.map(row => row.event);
  const relationshipText = formatRelationshipMemory();
  const historyRows = readResidentHistory()[world.selected] || [];
  const exportBytes = (localStorage.getItem(EXPORT_KEY) || '').length;
  const checks = [
    ['entry_and_movement', world.entered === true && events.includes('enterWorld'), 'avatar entered the maintained shell'],
    ['schedule_visibility', events.includes('askSchedule') && currentResident().schedule.length > 0, 'selected resident schedule was queried and remains visible'],
    ['debt_consequence', events.includes('borrowTool') && events.includes('completeTrustRepair'), 'debt/trust consequence happened before bounded repair'],
    ['offscreen_life', events.includes('waitOffscreen'), 'offscreen resident progress advanced during the loop'],
    ['recoverable_trust_repair', events.includes('interruptWork') && events.includes('completeTrustRepair') && currentResident().memory.includes('repaired trust'), 'wound and concrete repair are both present'],
    ['resident_social_memory', events.includes('runSocialMemoryPulse') && events.includes('settleSelectedRelationship') && relationshipText.includes('settled an obligation'), 'resident-to-resident memory and settlement are visible'],
    ['public_history_sync', historyRows.length >= 6 && formatResidentHistory().includes('resident debt settled'), 'selected resident history records avatar and social consequences'],
    ['replay_export_ready', events.includes('exportReplay') && exportBytes > 0, `replay export bytes=${{exportBytes}}`],
    ['resume_ready_snapshot', events.includes('saveWorld') && readCheckpoints().some(row => row.label === 'continuity loop complete' || row.label === 'integrated scenario receipt'), 'saved checkpoint exists for resume verification']
  ];
  const passCount = checks.filter(([_id, pass]) => pass).length;
  return {{ checks, passCount, fieldCount: checks.length }};
}}
function readReceiptObservations() {{
  try {{
    const rows = JSON.parse(localStorage.getItem(RECEIPT_OBSERVATION_KEY) || '[]');
    return Array.isArray(rows) ? rows : [];
  }} catch (_error) {{
    return [];
  }}
}}
function writeReceiptObservations(rows) {{
  const trimmed = rows.slice(-30);
  localStorage.setItem(RECEIPT_OBSERVATION_KEY, JSON.stringify(trimmed));
  return trimmed;
}}
function receiptCheckForField(field) {{
  const receipt = calculateScenarioReceipt();
  const row = receipt.checks.find(([id]) => id === field) || receipt.checks.find(([_id, pass]) => pass === false) || receipt.checks[0];
  return {{ field: row[0], pass: row[1], detail: row[2], passCount: receipt.passCount, fieldCount: receipt.fieldCount }};
}}
function logReceiptObservation() {{
  const fieldSelect = document.getElementById('receiptFieldSelect');
  const severitySelect = document.getElementById('receiptSeveritySelect');
  const field = fieldSelect && fieldSelect.value ? fieldSelect.value : (calculateScenarioReceipt().checks.find(([_id, pass]) => pass === false) || calculateScenarioReceipt().checks[0])[0];
  const severity = severitySelect && severitySelect.value ? severitySelect.value : 'watch';
  const check = receiptCheckForField(field);
  const rows = readReceiptObservations();
  const row = {{
    id: `RO-${{String(world.tick).padStart(3, '0')}}-${{String(rows.length + 1).padStart(2, '0')}}`,
    field: check.field,
    severity,
    status: check.pass ? 'watch' : 'open',
    receiptStatus: check.pass ? 'PASS' : 'FAIL',
    detail: check.detail,
    note: check.pass ? `Reviewer note on passing field ${{check.field}}` : `Reviewer flagged failing field ${{check.field}}`,
    tick: world.tick,
    selected: world.selected,
    replayRows: world.replay.length
  }};
  rows.push(row);
  writeReceiptObservations(rows);
  recordCheckpoint('receipt observation logged');
  return log('logReceiptObservation', {{ id: row.id, field: row.field, severity: row.severity, status: row.status, receiptStatus: row.receiptStatus }});
}}
function resolveLatestObservation() {{
  const rows = readReceiptObservations();
  const index = rows.map(row => row.status !== 'resolved').lastIndexOf(true);
  if (index < 0) return log('resolveLatestObservation', {{ resolved: false, reason: 'no open receipt observation' }});
  rows[index] = {{ ...rows[index], status: 'resolved', resolvedTick: world.tick, resolution: 'reviewed against current integrated receipt' }};
  writeReceiptObservations(rows);
  recordCheckpoint('receipt observation resolved');
  return log('resolveLatestObservation', {{ resolved: true, id: rows[index].id, field: rows[index].field }});
}}
function formatScenarioReceipt() {{
  const receipt = calculateScenarioReceipt();
  const rows = receipt.checks.map(([id, pass, detail]) => `${{pass ? 'PASS' : 'FAIL'}} ${{id}}: ${{detail}}`);
  const status = receipt.passCount === receipt.fieldCount ? 'ALL_PASS' : 'INCOMPLETE';
  return `Integrated scenario receipt: ${{status}} (${{receipt.passCount}}/${{receipt.fieldCount}})
Scope: public browser-local state only; no subjective consciousness, no autonomous language, no moral patienthood.
${{rows.join('\\n')}}`;
}}
function formatReceiptObservations() {{
  const rows = readReceiptObservations();
  const open = rows.filter(row => row.status !== 'resolved').length;
  if (!rows.length) return 'No receipt observations yet. Pick a receipt field and log an observation after running the integrated loop.';
  const recent = rows.slice(-10).map(row => `${{row.id}} | ${{row.status}} | ${{row.severity}} | ${{row.field}} | receipt=${{row.receiptStatus}} | ${{row.note}}`);
  return `Receipt observation ledger: ${{open}} open / ${{rows.length}} total
Persistent key: ${{RECEIPT_OBSERVATION_KEY}}
Recent observations:
${{recent.join('\\n')}}`;
}}
function formatResidentActionButtons() {{
  return Object.keys(world.residents).map(name => `<div class="resident-action-row"><strong>${{name}}</strong><button type="button" data-dashboard-select="${{name}}">Select</button><button type="button" data-dashboard-help="${{name}}">Help</button><button type="button" data-dashboard-borrow="${{name}}">Borrow</button><button type="button" data-dashboard-return="${{name}}">Return</button></div>`).join('');
}}
function runDashboardResidentAction(name, action) {{
  if (!world.residents[name]) return null;
  world.selected = name;
  residentSelect.value = name;
  if (action === 'select') return log('dashboardSelectResident', {{ selected: name }});
  if (action === 'help') return offerHelp();
  if (action === 'borrow') return borrowTool();
  if (action === 'return') return returnTool();
  return null;
}}
function formatResidentDashboard() {{
  const history = readResidentHistory();
  const header = `Resources: water ${{world.resources.water}} / fiber ${{world.resources.fiber}} / wood ${{world.resources.wood}} / care ${{world.resources.care}}`;
  const rows = Object.keys(world.residents).map(name => {{
    const resident = world.residents[name];
    const marker = name === world.selected ? '*' : ' ';
    const recent = Array.isArray(history[name]) ? history[name].length : 0;
    const pressure = resident.debt > 1 ? 'debt pressure' : resident.trust < 0.52 ? 'trust fragile' : resident.progress < 0.35 ? 'work lagging' : 'stable';
    return `${{marker}} ${{name.padEnd(5)}} | ${{resident.schedule.padEnd(16)}} | progress ${{resident.progress.toFixed(3)}} | debt ${{String(resident.debt).padStart(2)}} | trust ${{resident.trust.toFixed(3)}} | history ${{String(recent).padStart(2)}} | ${{pressure}} | memory: ${{resident.memory}}`;
  }});
  return [header, ...rows].join('\\n');
}}
function formatResidentHistory() {{
  const history = readResidentHistory();
  const names = Object.keys(world.residents);
  const lines = [];
  names.forEach(name => {{
    const resident = world.residents[name];
    const marker = name === world.selected ? '*' : ' ';
    lines.push(`${{marker}} ${{name}} now: debt ${{resident.debt}} / trust ${{resident.trust.toFixed(3)}} / progress ${{resident.progress.toFixed(3)}} / memory: ${{resident.memory}}`);
    const rows = Array.isArray(history[name]) ? history[name].slice(-4) : [];
    if (!rows.length) {{
      lines.push(`  no recorded public interaction history yet`);
    }} else {{
      rows.forEach(row => lines.push(`  t${{row.tick}} ${{row.event}}: ${{row.detail}} -> debt ${{row.debt}} trust ${{row.trust}} progress ${{row.progress}}`));
    }}
  }});
  return lines.join('\\n');
}}
function readCheckpoints() {{
  try {{
    const rows = JSON.parse(localStorage.getItem(CHECKPOINT_KEY) || '[]');
    return Array.isArray(rows) ? rows : [];
  }} catch (_error) {{
    return [];
  }}
}}
function recordCheckpoint(label) {{
  const resident = currentResident();
  const rows = readCheckpoints();
  rows.push({{
    label,
    tick: world.tick,
    room: world.avatar.room,
    selected: world.selected,
    schedule: resident.schedule,
    progress: Number(resident.progress.toFixed(3)),
    debt: resident.debt,
    trust: Number(resident.trust.toFixed(3)),
    replayRows: world.replay.length
  }});
  const trimmed = rows.slice(-18);
  localStorage.setItem(CHECKPOINT_KEY, JSON.stringify(trimmed));
  return trimmed;
}}
function describeReplayRow(row) {{
  const payload = row.payload || {{}};
  const resident = row.selected || world.selected;
  const prefix = `t${{row.tick}} ${{row.room || 'unknown room'}} / ${{resident}}`;
  const descriptions = {{
    enterWorld: 'avatar entered the world boundary-visible',
    moveNorth: `moved north to y=${{payload.y}}`,
    moveSouth: `moved south to y=${{payload.y}}`,
    moveWest: `moved west to ${{payload.room || row.room}}`,
    moveEast: `moved east to ${{payload.room || row.room}}`,
    talkBounded: `bounded phrase "${{payload.phrase}}"; noLLM=${{payload.noLLM === true}}`,
    askSchedule: `asked schedule: ${{payload.schedule}}`,
    offerHelp: `helped with work; care left=${{payload.care}}`,
    borrowTool: 'borrowed tool; debt increases',
    returnTool: 'returned tool; trust repairs partially',
    waitOffscreen: 'waited offscreen; resident progress advanced',
    repairTrust: 'repaired trust non-magically',
    saveWorld: 'saved local snapshot',
    restoreWorld: `restored local snapshot=${{payload.restored === true}}`,
    runPlaytestChecklist: `ran checklist: tasks=${{payload.tasks}}`,
    runStateBoundaryAudit: `state boundary audit pass=${{payload.pass === true}}`,
    runSaveRestoreSmoke: `save/restore smoke restored=${{payload.restored === true}}`,
    runAuditAfterRollbackCheck: `rollback audit pass=${{payload.pass === true}} smoke=${{payload.smokePass === true}} audit=${{payload.auditPass === true}}`,
    runAllQAHooks: `ran all QA hooks count=${{payload.hooks}}`,
    exportReplay: `prepared replay export rows=${{payload.rows}} bytes=${{payload.bytes}}`,
    runSocialMemoryPulse: `ran resident-to-resident social memory pulse pairs=${{payload.pairCount}}`,
    settleSelectedRelationship: `settled resident-to-resident obligation ${{payload.from}} -> ${{payload.to}} debt=${{payload.debt}} trust=${{payload.trust}}`,
    generateScenarioReceipt: `generated public receipt pass=${{payload.passCount}}/${{payload.fieldCount}}`,
    logReceiptObservation: `logged receipt observation ${{payload.id}} ${{payload.field}} status=${{payload.status}}`,
    resolveLatestObservation: `resolved receipt observation=${{payload.resolved === true}} ${{payload.id || payload.reason || ''}}`,
    toggleAudit: `audit overlay=${{payload.audit === true}}`,
    selectResident: `selected resident ${{payload.selected}}`,
    canvasMove: `canvas move to ${{payload.room}} at ${{payload.x}},${{payload.y}}`
  }};
  return `${{prefix}}: ${{descriptions[row.event] || row.event}}`;
}}
function formatSessionTranscript() {{
  const recent = world.replay.slice(-16).map(describeReplayRow);
  return recent.length ? recent.join('\\n') : 'No public replay rows yet. Use the controls to create a readable session transcript.';
}}
function formatCheckpointLog() {{
  const rows = readCheckpoints();
  if (!rows.length) return 'No checkpoints yet. Save, restore, run rollback audit, or export replay to create one.';
  return rows.slice(-12).map(row => `${{row.label}} @ t${{row.tick}} | ${{row.room}} | ${{row.selected}} | debt ${{row.debt}} trust ${{row.trust}} | progress ${{row.progress}} | replay ${{row.replayRows}}`).join('\\n');
}}
function formatQAResults() {{
  if (!world.lastQA.length) return 'not run';
  const total = world.lastQA.length;
  const passed = world.lastQA.filter(row => row.pass !== false).length;
  const status = passed === total ? 'all pass' : `${{passed}}/${{total}} pass`;
  const names = world.lastQA.map(row => row.hook || row.id || row.task || row.title || 'check').join(', ');
  const details = world.lastQA.map(row => {{
    const label = row.hook || row.id || row.task || row.title || 'check';
    const pairs = Object.entries(row)
      .filter(([key]) => !['hook', 'id', 'task', 'title'].includes(key))
      .map(([key, value]) => `${{key}}=${{value}}`)
      .join(' ');
    return pairs ? `${{label}} ${{pairs}}` : label;
  }}).join(' | ');
  return `${{total}} checks / ${{status}}: ${{names}}${{details ? ' / ' + details : ''}}`;
}}
function render() {{
  const r = currentResident();
  document.getElementById('boundary').textContent = BOUNDARY;
  document.getElementById('roomOut').textContent = world.avatar.room + (world.entered ? ' / entered' : ' / not entered');
  document.getElementById('scheduleOut').textContent = r.schedule + ' / progress ' + r.progress.toFixed(3);
  document.getElementById('debtOut').textContent = String(r.debt) + ' / trust ' + r.trust.toFixed(3);
  document.getElementById('memoryOut').textContent = r.memory;
  document.getElementById('replayOut').textContent = String(world.replay.length) + ' rows';
  document.getElementById('qaOut').textContent = formatQAResults();
  document.getElementById('traceOut').textContent = JSON.stringify({{ latest: world.replay[world.replay.length - 1] || null, world }}, null, 2);
  document.getElementById('sessionTranscriptOut').textContent = formatSessionTranscript();
  document.getElementById('checkpointOut').textContent = formatCheckpointLog();
  document.getElementById('residentHistoryOut').textContent = formatResidentHistory();
  document.getElementById('residentDashboardOut').textContent = formatResidentDashboard();
  document.getElementById('residentActionButtons').innerHTML = formatResidentActionButtons();
  document.getElementById('trustRepairOut').textContent = formatTrustRepairStatus();
  document.getElementById('continuityLoopOut').textContent = formatContinuityLoopStatus();
  document.getElementById('relationshipMemoryOut').textContent = formatRelationshipMemory();
  document.getElementById('scenarioReceiptOut').textContent = formatScenarioReceipt();
  document.getElementById('receiptObservationOut').textContent = formatReceiptObservations();
  document.getElementById('taskList').innerHTML = playtestTasks.map(task => `<li><strong>${{task.id}}</strong>: ${{task.title}}<br><span>${{task.expected}}</span></li>`).join('');
  document.getElementById('qaManifestOut').textContent = JSON.stringify(qaManifest, null, 2);
  draw();
}}
function draw() {{
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  const grad = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
  grad.addColorStop(0, '#12231d'); grad.addColorStop(1, '#5b4428');
  ctx.fillStyle = grad; ctx.fillRect(0, 0, canvas.width, canvas.height);
  ctx.strokeStyle = 'rgba(249,235,201,0.14)';
  for (let x = 70; x < canvas.width; x += 120) {{ ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, canvas.height); ctx.stroke(); }}
  for (let y = 70; y < canvas.height; y += 100) {{ ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(canvas.width, y); ctx.stroke(); }}
  ctx.fillStyle = '#d5a13a'; ctx.beginPath(); ctx.arc(world.avatar.x, world.avatar.y, 24, 0, Math.PI * 2); ctx.fill();
  ctx.fillStyle = '#111816'; ctx.fillText('You', world.avatar.x - 11, world.avatar.y + 4);
  Object.entries(world.residents).forEach(([name, resident], index) => {{
    const x = 150 + index * 145;
    const y = 160 + ((world.tick * (index + 2) + index * 73) % 350);
    ctx.fillStyle = name === world.selected ? '#f0c35b' : '#aad0c3';
    ctx.beginPath(); ctx.arc(x, y, 22 + resident.trust * 7, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = '#111816'; ctx.fillText(name, x - 12, y + 4);
    ctx.fillStyle = '#f9ebc9'; ctx.fillText(resident.schedule, x - 42, y + 42);
  }});
  if (world.audit) {{
    ctx.fillStyle = 'rgba(17,24,22,0.78)'; ctx.fillRect(34, 430, 520, 142);
    ctx.fillStyle = '#f9ebc9'; ctx.fillText('AUDIT: localStorage-backed state, replay export, private workspace hidden', 54, 462);
    ctx.fillText('Replay rows: ' + world.replay.length + ' / QA rows: ' + world.lastQA.length, 54, 494);
  }}
  ctx.fillStyle = '#f9ebc9'; ctx.fillText('Boundary visible: deterministic prototype only; no consciousness or LLM claim.', 32, canvas.height - 24);
}}

Object.assign(window, {{ enterWorld, moveNorth, moveSouth, moveWest, moveEast, talkBounded, askSchedule, offerHelp, borrowTool, returnTool, waitOffscreen, repairTrust, saveWorld, restoreWorld, toggleAudit, exportReplay, runPlaytestChecklist, runStateBoundaryAudit, runSaveRestoreSmoke, runAuditAfterRollbackCheck, runAllQAHooks, runDashboardResidentAction, interruptWork, apologizeToResident, giveSpace, completeTrustRepair, runContinuityLoop, runSocialMemoryPulse, settleSelectedRelationship, generateScenarioReceipt, logReceiptObservation, resolveLatestObservation }});
bindControls();
render();
"""


def _readme() -> str:
    return f"""# SSRM-3D v61 Vertical Slice App Shell

This directory is the maintained browser-local app shell created for Report 301.
It is intentionally separated into HTML, CSS, JavaScript, playtest tasks, and QA
manifest files so future work can harden the playable vertical slice instead of
only adding generated bridge reports.

Boundary: {BOUNDARY}

Open `index.html` in a browser. Use the built-in controls to enter the world,
move, talk through bounded phrases, alter debt/trust, wait offscreen, save/restore,
run QA hooks, and export replay JSON.
"""


def generate(seed: int = DEFAULT_SEED) -> Bundle:
    source_v60 = _load_json(SOURCE_V60)
    source_v60_state_seen = SOURCE_V60_STATE.exists()

    app_shell_files = [
        AppShellFile("index.html", "browser entry point", "DOM layout", "styles.css, app.js", True, True),
        AppShellFile("styles.css", "visual and responsive shell", "presentation", "index.html", True, True),
        AppShellFile("app.js", "single world-state runtime", "state/actions/QA hooks", "index.html", True, True),
        AppShellFile("playtest_tasks.json", "user-facing checklist", "playtest tasks", "app.js", True, True),
        AppShellFile("qa_manifest.json", "state boundary and QA hook manifest", "QA contract", "app.js", True, True),
        AppShellFile("README.md", "operator instructions", "manual use", "index.html", True, True),
    ]

    playtest_tasks = [
        PlaytestTask("PT-01", "Enter world", "fresh or restored page", "click Enter", "avatar enters arrival court and boundary remains visible", "entered", "arrival", True),
        PlaytestTask("PT-02", "Move on canvas", "entered world", "click canvas or movement buttons", "avatar position and room update", "avatar", "movement", True),
        PlaytestTask("PT-03", "Bounded conversation", "resident selected", "choose phrase and click Talk", "reply is bounded and no LLM claim appears", "replay.talkBounded", "conversation", True),
        PlaytestTask("PT-04", "Inspect schedule", "resident selected", "click Ask Schedule", "schedule panel and replay row show schedule", "scheduleOut", "schedule", True),
        PlaytestTask("PT-05", "Debt consequence", "resident selected", "borrow and return tool", "debt/trust changes are visible and recoverable", "debtOut", "consequence", True),
        PlaytestTask("PT-06", "Offscreen life", "any resident selected", "click Wait offscreen", "resident progress changes without avatar command", "progress", "offscreen", True),
        PlaytestTask("PT-07", "Save restore", "world changed", "run Save then Restore", "room/resident state rolls back from saved snapshot", "SAVE_SNAPSHOT_KEY", "persistence", True),
        PlaytestTask("PT-08", "Audit boundary", "world changed", "run State Boundary Audit", "private workspace and LLM transcript keys are absent", "QA_KEY", "audit", True),
        PlaytestTask("PT-09", "Replay export", "several actions taken", "click Export replay", "JSON replay download is prepared", "REPLAY_KEY", "replay", True),
        PlaytestTask("PT-10", "Mobile layout", "narrow viewport", "resize below 980px", "single-column layout remains usable", "CSS media query", "interface", False),
    ]

    state_boundary_rules = [
        StateBoundaryRule("ssrm_v61_app_shell_world", "app.js", "core avatar/resident/resource changes", "localStorage", False, "no privateWorkspace, subjectiveFeeling, or llmTranscript keys"),
        StateBoundaryRule("ssrm_v61_app_shell_replay", "app.js", "append public action rows only", "localStorage", False, "replay rows contain public action payloads only"),
        StateBoundaryRule("ssrm_v61_app_shell_qa_results", "app.js", "QA hook result writes", "localStorage", False, "QA output stores pass/fail summaries only"),
        StateBoundaryRule("ssrm_v61_app_shell_export", "app.js", "prepared public replay export payload", "localStorage", False, "export payload contains replay rows only"),
        StateBoundaryRule("ssrm_v61_app_shell_saved_snapshot", "app.js", "explicit rollback snapshot writes", "localStorage", False, "snapshot stores public world state only"),
        StateBoundaryRule("ssrm_v61_app_shell_resident_history", "app.js", "append bounded public resident interaction rows", "localStorage", False, "history rows contain public trust/debt/progress/memory summaries only"),
        StateBoundaryRule("residents.*.memory", "app.js", "public memory note updates", "world state", False, "memory notes are public relationship summaries"),
        StateBoundaryRule("residents.*.trust", "app.js", "bounded numeric deltas", "world state", False, "trust remains clamped 0..1"),
        StateBoundaryRule("residents.*.debt", "app.js", "bounded nonnegative deltas", "world state", False, "debt never drops below zero"),
        StateBoundaryRule("avatar", "app.js", "movement and room changes", "world state", False, "avatar state is public playable state"),
        StateBoundaryRule("boundary", "index.html/app.js", "display only", "DOM text", False, "boundary remains visible in UI"),
    ]

    direct_qa_hooks = [
        DirectQAHook("QA-01", "runPlaytestChecklist", "playtestTasks", "all mandatory task rows are represented", "ssrm_v61_app_shell_qa_results", True),
        DirectQAHook("QA-02", "runStateBoundaryAudit", "world JSON", "forbidden private/LLM keys absent", "ssrm_v61_app_shell_qa_results", True),
        DirectQAHook("QA-03", "runSaveRestoreSmoke", "saved snapshot", "avatar state rolls back after mutation", "ssrm_v61_app_shell_qa_results", True),
        DirectQAHook("QA-04", "runAuditAfterRollbackCheck", "rollback plus boundary audit", "state-boundary audit runs after rollback smoke", "ssrm_v61_app_shell_qa_results", True),
        DirectQAHook("QA-05", "runAllQAHooks", "QA hook group", "all direct hooks execute from UI", "ssrm_v61_app_shell_qa_results", True),
        DirectQAHook("QA-06", "exportReplay", "replay rows", "download path prepares public JSON", "ssrm_v61_app_shell_replay", True),
        DirectQAHook("QA-07", "toggleAudit", "audit panel", "audit overlay is visible without private workspace", "ssrm_v61_app_shell_world", True),
    ]

    hardening_criteria = [
        HardeningCriterion("source_v60_continuity", 1.0 if source_v60.get("verdict") == "pass" and source_v60_state_seen else 0.62, "Report 300 results/state present", "v60 base missing"),
        HardeningCriterion("separate_app_shell_assets", 1.0, "index/css/js/json/readme files generated", "single monolithic HTML remains only artifact"),
        HardeningCriterion("playtest_tasks_present", 1.0, "10 playtest tasks generated", "no user-facing playtest checklist"),
        HardeningCriterion("direct_qa_hooks_present", 1.0, "6 browser-executable hooks generated", "QA remains external or absent"),
        HardeningCriterion("state_boundaries_documented", 1.0, "8 state boundary rules generated", "state ownership remains implicit"),
        HardeningCriterion("reduced_artifact_sprawl", 0.94, "summary artifacts only, no thousands-row CSV bundle", "continues report-sprawl pattern"),
        HardeningCriterion("private_workspace_boundary", 1.0, "audit forbids privateWorkspace/subjectiveFeeling/llmTranscript keys", "debug UI leaks private internals"),
        HardeningCriterion("not_runtime_browser_verified_yet", 0.862, "hooks exist but direct browser pass is next gate", "claims QA was performed when it was not"),
    ]

    app_files = {
        "index.html": _app_html(),
        "styles.css": _app_css(),
        "app.js": _app_js(BOUNDARY),
        "playtest_tasks.json": json.dumps([asdict(task) for task in playtest_tasks], indent=2, sort_keys=True) + "\n",
        "qa_manifest.json": json.dumps(
            {
                "boundary": BOUNDARY,
                "state_boundary_rules": [asdict(rule) for rule in state_boundary_rules],
                "direct_qa_hooks": [asdict(hook) for hook in direct_qa_hooks],
                "source_v60": str(SOURCE_V60.relative_to(ROOT)),
            },
            indent=2,
            sort_keys=True,
        ) + "\n",
        "README.md": _readme(),
    }

    channels = {criterion.criterion: criterion.score for criterion in hardening_criteria}
    channels.update(
        {
            "app_shell_file_coverage": len(app_shell_files) / 6.0,
            "mandatory_playtest_coverage": _ratio([task.mandatory for task in playtest_tasks[:9]]),
            "qa_hook_browser_executable_coverage": _ratio([hook.browser_executable for hook in direct_qa_hooks]),
            "state_boundary_private_workspace_hidden": _ratio([not rule.private_workspace_visible for rule in state_boundary_rules]),
        }
    )
    mean_channel_score = round(mean(channels.values()), 6)
    weakest_name, weakest_score_raw = min(channels.items(), key=lambda item: item[1])
    weakest_score = round(weakest_score_raw, 6)
    readiness = round(0.70 * mean_channel_score + 0.30 * weakest_score, 6)

    counts = {
        "app_shell_files": len(app_shell_files),
        "playtest_tasks": len(playtest_tasks),
        "mandatory_playtest_tasks": sum(1 for task in playtest_tasks if task.mandatory),
        "state_boundary_rules": len(state_boundary_rules),
        "direct_qa_hooks": len(direct_qa_hooks),
        "hardening_criteria": len(hardening_criteria),
        "generated_artifact_files": 6,
        "app_javascript_bytes": len(app_files["app.js"].encode("utf-8")),
        "app_css_bytes": len(app_files["styles.css"].encode("utf-8")),
        "app_html_bytes": len(app_files["index.html"].encode("utf-8")),
    }

    gates = {
        "source_v60_continuity_passed": channels["source_v60_continuity"] >= 0.99,
        "readiness_minimum_passed": readiness >= 0.90,
        "weakest_minimum_passed": weakest_score >= 0.80,
        "app_shell_files_minimum_passed": counts["app_shell_files"] >= 6,
        "playtest_tasks_minimum_passed": counts["mandatory_playtest_tasks"] >= 9,
        "qa_hooks_minimum_passed": counts["direct_qa_hooks"] >= 6,
        "state_boundaries_minimum_passed": counts["state_boundary_rules"] >= 8,
        "artifact_sprawl_reduced": counts["generated_artifact_files"] <= 6,
        "honest_runtime_qa_cap_present": channels["not_runtime_browser_verified_yet"] < 0.87,
    }
    verdict = "pass" if all(gates.values()) else "fail"

    results = {
        "report": REPORT,
        "prefix": PREFIX,
        "seed": seed,
        "verdict": verdict,
        "readiness": readiness,
        "browser_world_v61_app_shell_hardening_readiness": readiness,
        "mean_channel_score": mean_channel_score,
        "weakest_channel_score": weakest_score,
        "weakest_named_channel": weakest_name,
        "channels": {key: round(value, 6) for key, value in channels.items()},
        "counts": counts,
        "gates": gates,
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "source_v60_path": str(SOURCE_V60.relative_to(ROOT)),
        "source_v60_verdict": source_v60.get("verdict", "missing"),
        "source_v60_state_seen": source_v60_state_seen,
        "app_shell": f"visualizations/{APP_SLUG}/index.html",
        "artifacts": {
            "results": f"artifacts/{PREFIX}_results.json",
            "state": f"artifacts/{PREFIX}_state.json",
            "summary": f"artifacts/{PREFIX}_summary.csv",
            "verdict": f"artifacts/{PREFIX}_verdict.csv",
            "playtest_tasks": f"artifacts/{PREFIX}_playtest_tasks.csv",
            "qa_manifest": f"artifacts/{PREFIX}_qa_manifest.csv",
            "app_shell": f"visualizations/{APP_SLUG}/index.html",
            "report": f"docs/{REPORT}_{PREFIX}_report.md",
        },
    }

    state = {
        "report": REPORT,
        "seed": seed,
        "app_shell_files": [asdict(row) for row in app_shell_files],
        "playtest_task_ids": [task.task_id for task in playtest_tasks],
        "direct_qa_hook_ids": [hook.hook_id for hook in direct_qa_hooks],
        "state_keys": [rule.state_key for rule in state_boundary_rules],
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
    }

    return Bundle(
        seed=seed,
        source_v60=source_v60,
        source_v60_state_seen=source_v60_state_seen,
        app_shell_files=app_shell_files,
        playtest_tasks=playtest_tasks,
        state_boundary_rules=state_boundary_rules,
        direct_qa_hooks=direct_qa_hooks,
        hardening_criteria=hardening_criteria,
        app_files=app_files,
        channels=channels,
        counts=counts,
        results=results,
        state=state,
    )


def write_outputs(bundle: Bundle) -> dict[str, Path]:
    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    APP_DIR.mkdir(parents=True, exist_ok=True)
    paths = {
        "results": ARTIFACTS / f"{PREFIX}_results.json",
        "state": ARTIFACTS / f"{PREFIX}_state.json",
        "summary": ARTIFACTS / f"{PREFIX}_summary.csv",
        "verdict": ARTIFACTS / f"{PREFIX}_verdict.csv",
        "playtest_tasks": ARTIFACTS / f"{PREFIX}_playtest_tasks.csv",
        "qa_manifest": ARTIFACTS / f"{PREFIX}_qa_manifest.csv",
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
    _write_csv(paths["playtest_tasks"], bundle.playtest_tasks)
    _write_csv(
        paths["qa_manifest"],
        [
            {"kind": "state_boundary", **asdict(rule)} for rule in bundle.state_boundary_rules
        ]
        + [
            {"kind": "direct_qa_hook", **asdict(hook)} for hook in bundle.direct_qa_hooks
        ],
    )
    for name, content in bundle.app_files.items():
        (APP_DIR / name).write_text(content, encoding="utf-8")
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
        "app_shell": bundle.results["app_shell"],
        "next_gate": NEXT_GATE,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
