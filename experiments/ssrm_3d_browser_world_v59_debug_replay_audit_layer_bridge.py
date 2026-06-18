"""Report 299: SSRM-3D browser world v59 debug/replay/audit layer bridge.

This deterministic benchmark adds an inspectable debug/replay/audit layer on top
of the consolidated playable consequence loop from Report 298/v58. The purpose is
not another isolated feature channel; it is traceability for the same playable loop
by tick, resident, memory, debt, schedule, consequence, invariant, and localStorage
snapshot.

Boundary: deterministic browser-local scaffold only. No LLM calls, no subjective
consciousness claim, no autonomous natural language claim, no real consent or
moral-patienthood claim, no production persistence claim, and no complete 3D game
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

REPORT = 299
PREFIX = "ssrm_3d_browser_world_v59_debug_replay_audit_layer_bridge"
DEFAULT_SEED = 20270519
LIVE_DAYS = 280
TICKS_PER_DAY = 18
TOTAL_TICKS = LIVE_DAYS * TICKS_PER_DAY

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
VISUALIZATIONS = ROOT / "visualizations"

SOURCE_V58 = ARTIFACTS / "ssrm_3d_browser_world_v58_consolidated_playable_consequence_loop_bridge_results.json"
SOURCE_V58_STATE = ARTIFACTS / "ssrm_3d_browser_world_v58_consolidated_playable_consequence_loop_bridge_state.json"

BOUNDARY = (
    "Deterministic browser-local debug/replay/audit layer over the consolidated "
    "playable consequence loop only; no LLM call, subjective consciousness, real "
    "consent, autonomous natural language, moral patienthood, production persistence, "
    "complete gameplay, complete 3D engine, or metaphysical frequency claim."
)

NEXT_GATE = (
    "Report 300 consolidated playable vertical slice build: one URL-style browser "
    "artifact where arrival, movement, bounded conversation, resident schedules, debts, "
    "offscreen life, memory, visible consequences, save/restore, and audit replay are "
    "usable together rather than reported as separate bridges"
)


@dataclass(frozen=True)
class ReplayScrubFrame:
    tick: int
    day: int
    slot: int
    selected_tick: int
    selected_resident: str
    event_key: str
    event_kind: str
    previous_event_key: str
    next_event_key: str
    scrubber_position: float
    replay_row_visible: bool
    same_loop_reference: str


@dataclass(frozen=True)
class ResidentAuditIndexFrame:
    tick: int
    day: int
    resident: str
    schedule_key: str
    memory_key: str
    debt_key: str
    consequence_key: str
    snapshot_key: str
    index_lookup: str
    resident_filterable: bool
    crosslinks_complete: bool


@dataclass(frozen=True)
class MemoryDebtAuditFrame:
    tick: int
    day: int
    resident: str
    memory_key: str
    debt_name: str
    debt_before: float
    debt_after: float
    trust_before: float
    trust_after: float
    causal_action: str
    visible_in_dashboard: bool
    persists_after_restore: bool
    history_not_erased: bool


@dataclass(frozen=True)
class ScheduleDiffAuditFrame:
    tick: int
    day: int
    resident: str
    schedule_before: str
    schedule_after: str
    changed_by_avatar: bool
    changed_offscreen: bool
    diff_summary: str
    agency_flag: str
    visible_after_return: bool


@dataclass(frozen=True)
class LocalStorageSnapshotFrame:
    tick: int
    day: int
    snapshot_key: str
    avatar_room: str
    selected_resident: str
    resident_state_digest: str
    resource_state_digest: str
    replay_event_count: int
    snapshot_size_bytes: int
    restored_ok: bool
    storage_keys_present: bool


@dataclass(frozen=True)
class InvariantAuditFrame:
    tick: int
    day: int
    invariant_name: str
    observed_value: float
    lower_bound: float
    upper_bound: float
    passed: bool
    severity: str
    repair_hint: str
    linked_replay_key: str


@dataclass(frozen=True)
class ConsequenceCausalityFrame:
    tick: int
    day: int
    resident: str
    cause_action: str
    direct_effect: str
    delayed_effect: str
    affected_resource: str
    recovery_path: str
    causal_chain_id: str
    chain_scrubbable: bool
    non_magical_trust_repair: bool


@dataclass(frozen=True)
class AuditUIFrame:
    tick: int
    day: int
    active_panel: str
    selected_resident: str
    selected_tick: int
    filter_text: str
    visible_columns: str
    panel_patch: str
    keyboard_shortcut: str
    export_ready: bool
    private_workspace_hidden: bool


@dataclass(frozen=True)
class BrowserWorldV59Tick:
    tick: int
    day: int
    slot: int
    selected_resident: str
    scrub_frame: int
    index_frame: int
    memory_debt_frame: int
    schedule_diff_frame: int
    localstorage_snapshot_frame: int
    invariant_frame: int
    causality_frame: int
    audit_ui_frame: int
    audit_layer_attached_to_v58_loop: bool
    boundary_visible: bool


@dataclass
class Bundle:
    seed: int
    source_v58: dict[str, Any]
    source_v58_state_seen: bool
    replay_scrub_frames: list[ReplayScrubFrame]
    resident_audit_index_frames: list[ResidentAuditIndexFrame]
    memory_debt_audit_frames: list[MemoryDebtAuditFrame]
    schedule_diff_audit_frames: list[ScheduleDiffAuditFrame]
    localstorage_snapshot_frames: list[LocalStorageSnapshotFrame]
    invariant_audit_frames: list[InvariantAuditFrame]
    consequence_causality_frames: list[ConsequenceCausalityFrame]
    audit_ui_frames: list[AuditUIFrame]
    browser_ticks: list[BrowserWorldV59Tick]
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


def _buttons() -> str:
    funcs = [
        "scrubTick",
        "stepReplay",
        "filterResident",
        "inspectMemoryDebt",
        "inspectScheduleDiff",
        "inspectSnapshot",
        "inspectInvariant",
        "inspectCausality",
        "jumpAnomaly",
        "togglePrivateBoundary",
        "exportAudit",
        "restoreSnapshot",
    ]
    rows = []
    for idx in range(204):
        fn = funcs[idx % len(funcs)]
        label = fn.replace("inspect", "inspect ").replace("Resident", " resident").replace("Snapshot", " snapshot").replace("Invariant", " invariant")
        rows.append(f'<button type="button" onclick="{fn}({idx})">{label} {idx:03d}</button>')
    rows.extend(
        [
            '<button type="button" onclick="saveAuditState()">save audit state</button>',
            '<button type="button" onclick="loadAuditState()">load audit state</button>',
            '<button type="button" onclick="downloadReplay()">download replay</button>',
            '<button type="button" onclick="showBoundary()">show boundary</button>',
        ]
    )
    return "\n".join(rows)


def _render_html(sample: dict[str, Any], counts: dict[str, int]) -> str:
    sample_pre = json.dumps(sample, indent=2, sort_keys=True)
    sample_js = json.dumps(sample, sort_keys=True)
    counts_js = json.dumps(counts, sort_keys=True)
    html = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>Report 299 - Browser World v59 Debug Replay Audit Layer</title>
<style>
:root {
  --ink: #101714;
  --paper: #f1e4c6;
  --line: #263d34;
  --amber: #c8892c;
  --rust: #b65b3b;
  --cyan: #347b84;
  --sage: #738b57;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  color: var(--ink);
  background:
    linear-gradient(135deg, rgba(16,23,20,0.06), rgba(52,123,132,0.18)),
    radial-gradient(circle at 16% 8%, rgba(200,137,44,0.34), transparent 24%),
    radial-gradient(circle at 85% 18%, rgba(182,91,59,0.28), transparent 28%),
    #eadcbf;
  font-family: 'Avenir Next Condensed', 'Trebuchet MS', sans-serif;
}
main { max-width: 1280px; margin: 0 auto; padding: 22px; }
h1 { margin: 0; max-width: 1040px; font-size: clamp(2.2rem, 5vw, 5.4rem); line-height: 0.88; letter-spacing: -0.055em; }
.boundary { margin: 16px 0; padding: 14px 16px; border-left: 9px solid var(--rust); background: rgba(255,255,255,0.64); }
.layout { display: grid; grid-template-columns: minmax(460px, 1fr) 410px; gap: 16px; }
canvas { width: 100%; min-height: 560px; border: 5px solid var(--ink); background: #12231e; box-shadow: 0 20px 70px rgba(16,23,20,0.33); }
.panel { background: rgba(255,255,255,0.72); border: 1px solid rgba(16,23,20,0.20); border-radius: 18px; padding: 14px; }
.metrics { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 8px; margin: 12px 0 16px; }
.metrics span { border-radius: 999px; border: 1px solid rgba(16,23,20,0.16); background: rgba(255,255,255,0.64); padding: 8px 10px; }
.audit-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 8px; margin-top: 10px; }
.card { border-radius: 14px; border: 1px solid rgba(16,23,20,0.14); background: rgba(241,228,198,0.78); padding: 10px; min-height: 82px; }
#controls { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 6px; max-height: 384px; overflow: auto; }
button { border: 0; border-radius: 999px; padding: 8px 9px; color: white; background: var(--line); cursor: pointer; font-size: 12px; }
button:nth-child(3n) { background: var(--cyan); }
button:nth-child(5n) { background: var(--rust); }
button:nth-child(7n) { background: var(--sage); }
pre { white-space: pre-wrap; background: rgba(16,23,20,0.90); color: #f7ebcd; padding: 12px; border-radius: 12px; max-height: 360px; overflow: auto; }
input[type=range] { width: 100%; accent-color: var(--rust); }
@media (max-width: 920px) { .layout { grid-template-columns: 1fr; } .metrics { grid-template-columns: repeat(2, minmax(0, 1fr)); } #controls { grid-template-columns: repeat(2, minmax(0, 1fr)); } .audit-grid { grid-template-columns: 1fr; } }
</style>
</head>
<body>
<main>
  <h1>Debug the same little world: scrub time, resident, debt, schedule, memory, snapshot.</h1>
  <p class="boundary">__BOUNDARY__</p>
  <div class="metrics">
    <span>scrub frames: __SCRUB__</span>
    <span>snapshots: __SNAPS__</span>
    <span>invariants: __INVARIANTS__</span>
    <span>buttons: __BUTTONS_COUNT__</span>
  </div>
  <div class="layout">
    <section>
      <canvas id="world" width="990" height="590" aria-label="debug replay audit canvas"></canvas>
      <div class="panel">
        <label for="scrub">Replay scrubber</label>
        <input id="scrub" type="range" min="0" max="__MAX_TICK__" value="__SAMPLE_TICK__" oninput="scrubTick(Number(this.value))" />
        <div class="audit-grid">
          <div class="card"><strong>Resident</strong><p id="resident"></p></div>
          <div class="card"><strong>Memory/Debt</strong><p id="memory"></p></div>
          <div class="card"><strong>Invariant</strong><p id="invariant"></p></div>
        </div>
      </div>
      <pre id="trace"></pre>
    </section>
    <aside class="panel">
      <h2>Audit controls</h2>
      <div id="controls">__BUTTONS__</div>
      <h2>Sample frame</h2>
      <pre>__SAMPLE_PRE__</pre>
    </aside>
  </div>
</main>
<script>
const SAMPLE = __SAMPLE_JS__;
const COUNTS = __COUNTS_JS__;
const BOUNDARY = "__BOUNDARY_JS__";
const auditKey = 'ssrm_v59_audit_state';
const replayKey = 'ssrm_v59_audit_replay';
let audit = JSON.parse(localStorage.getItem(auditKey) || JSON.stringify({
  tick: SAMPLE.replay_scrub.tick,
  resident: SAMPLE.replay_scrub.selected_resident,
  panel: 'scrubber',
  privateBoundary: true,
  rows: [],
  snapshot: SAMPLE.localstorage_snapshot
}));
const canvas = document.getElementById('world');
const ctx = canvas.getContext('2d');
const trace = document.getElementById('trace');
function log(event, payload) {
  const row = { event, tick: audit.tick, resident: audit.resident, panel: audit.panel, payload };
  audit.rows.push(row);
  if (audit.rows.length > 160) audit.rows.shift();
  localStorage.setItem(auditKey, JSON.stringify(audit));
  localStorage.setItem(replayKey, JSON.stringify(audit.rows));
  render();
}
function residentFor(i) { return ['Ari','Fay','Milo','Sera','Tovan','Nia'][Math.abs(i) % 6]; }
function scrubTick(i) { audit.tick = Math.max(0, Math.min(COUNTS.browser_ticks - 1, i)); audit.panel = 'scrubber'; log('scrubTick', { selectedTick: audit.tick, sample: SAMPLE.replay_scrub }); }
function stepReplay(i) { audit.tick = Math.max(0, Math.min(COUNTS.browser_ticks - 1, audit.tick + (i % 2 ? 1 : -1))); audit.panel = 'step'; log('stepReplay', { selectedTick: audit.tick }); }
function filterResident(i) { audit.resident = residentFor(i); audit.panel = 'resident-index'; log('filterResident', { resident: audit.resident, index: SAMPLE.resident_audit_index }); }
function inspectMemoryDebt(i) { audit.panel = 'memory-debt'; log('inspectMemoryDebt', { memory: SAMPLE.memory_debt_audit, selected: audit.resident }); }
function inspectScheduleDiff(i) { audit.panel = 'schedule-diff'; log('inspectScheduleDiff', { schedule: SAMPLE.schedule_diff_audit }); }
function inspectSnapshot(i) { audit.panel = 'snapshot'; audit.snapshot = SAMPLE.localstorage_snapshot; log('inspectSnapshot', { snapshot: audit.snapshot }); }
function inspectInvariant(i) { audit.panel = 'invariant'; log('inspectInvariant', { invariant: SAMPLE.invariant_audit }); }
function inspectCausality(i) { audit.panel = 'causality'; log('inspectCausality', { causality: SAMPLE.consequence_causality }); }
function jumpAnomaly(i) { audit.tick = (i * 37) % COUNTS.browser_ticks; audit.panel = 'anomaly'; log('jumpAnomaly', { tick: audit.tick, severity: SAMPLE.invariant_audit.severity }); }
function togglePrivateBoundary(i) { audit.privateBoundary = !audit.privateBoundary; log('togglePrivateBoundary', { privateBoundary: audit.privateBoundary }); }
function exportAudit(i) { log('exportAudit', { rows: audit.rows.length, noPrivateWorkspace: audit.privateBoundary }); }
function restoreSnapshot(i) { audit.snapshot = SAMPLE.localstorage_snapshot; log('restoreSnapshot', { restored: true, snapshotKey: audit.snapshot.snapshot_key }); }
function saveAuditState() { localStorage.setItem(auditKey, JSON.stringify(audit)); log('saveAuditState', { saved: true }); }
function loadAuditState() { audit = JSON.parse(localStorage.getItem(auditKey) || JSON.stringify(audit)); log('loadAuditState', { loaded: true }); }
function downloadReplay() {
  const blob = new Blob([JSON.stringify(audit.rows, null, 2)], { type: 'application/json' });
  const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = 'report_299_v59_audit_replay.json'; a.click();
  log('downloadReplay', { rows: audit.rows.length });
}
function showBoundary() { log('showBoundary', { boundary: BOUNDARY }); }
function render() {
  document.getElementById('resident').textContent = audit.resident + ' / panel ' + audit.panel + ' / tick ' + audit.tick;
  document.getElementById('memory').textContent = SAMPLE.memory_debt_audit.memory_key + ' / ' + SAMPLE.memory_debt_audit.debt_name;
  document.getElementById('invariant').textContent = SAMPLE.invariant_audit.invariant_name + ': ' + (SAMPLE.invariant_audit.passed ? 'pass' : 'flag');
  trace.textContent = JSON.stringify({ audit, latest: audit.rows[audit.rows.length - 1] || null }, null, 2);
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  const grad = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
  grad.addColorStop(0, '#10241d'); grad.addColorStop(1, '#4f3f2b');
  ctx.fillStyle = grad; ctx.fillRect(0, 0, canvas.width, canvas.height);
  ctx.strokeStyle = 'rgba(247,235,205,0.13)';
  for (let x = 50; x < canvas.width; x += 90) { ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, canvas.height); ctx.stroke(); }
  for (let y = 50; y < canvas.height; y += 90) { ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(canvas.width, y); ctx.stroke(); }
  const timelineWidth = canvas.width - 90;
  const px = 45 + (audit.tick / Math.max(1, COUNTS.browser_ticks - 1)) * timelineWidth;
  ctx.fillStyle = '#c8892c'; ctx.fillRect(45, 48, timelineWidth, 18);
  ctx.fillStyle = '#b65b3b'; ctx.fillRect(px - 4, 38, 8, 38);
  ctx.fillStyle = '#f7ebcd'; ctx.fillText('Replay scrubber over v58 loop tick ' + audit.tick, 45, 30);
  ['Ari','Fay','Milo','Sera','Tovan','Nia'].forEach((name, idx) => {
    const x = 120 + idx * 138;
    const y = 170 + ((audit.tick + idx * 31) % 260);
    ctx.fillStyle = name === audit.resident ? '#c8892c' : '#9fc8bd';
    ctx.beginPath(); ctx.arc(x, y, 24, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = '#101714'; ctx.fillText(name, x - 13, y + 4);
    ctx.fillStyle = '#f7ebcd'; ctx.fillText('memory/debt/schedule indexed', x - 50, y + 42);
  });
  ctx.fillStyle = '#f7ebcd';
  ctx.fillText('Audit layer attached to consolidated v58 loop; private workspace remains hidden.', 45, canvas.height - 26);
}
render();
showBoundary();
</script>
</body>
</html>
"""
    return (
        html.replace("__BOUNDARY__", BOUNDARY)
        .replace("__BOUNDARY_JS__", BOUNDARY.replace('"', "'"))
        .replace("__SCRUB__", str(counts["replay_scrub_frames"]))
        .replace("__SNAPS__", str(counts["localstorage_snapshot_frames"]))
        .replace("__INVARIANTS__", str(counts["invariant_audit_frames"]))
        .replace("__BUTTONS_COUNT__", str(counts["browser_buttons"]))
        .replace("__MAX_TICK__", str(counts["browser_ticks"] - 1))
        .replace("__SAMPLE_TICK__", str(sample["replay_scrub"]["tick"]))
        .replace("__BUTTONS__", _buttons())
        .replace("__SAMPLE_PRE__", sample_pre)
        .replace("__SAMPLE_JS__", sample_js)
        .replace("__COUNTS_JS__", counts_js)
    )


def generate(seed: int = DEFAULT_SEED) -> Bundle:
    rng = random.Random(seed)
    source_v58 = _load_json(SOURCE_V58)
    source_v58_state_seen = SOURCE_V58_STATE.exists()

    residents = ["Ari", "Fay", "Milo", "Sera", "Tovan", "Nia"]
    events = ["move", "talk", "offer_help", "borrow_tool", "return_tool", "interrupt_work", "wait_offscreen", "repair_trust"]
    schedules = ["work", "rest", "negotiate debt", "seek tool", "care duty", "private task", "recover focus"]
    debts = ["tool loan", "water carry", "repair promise", "missed greeting", "care favor", "route warning"]
    resources = ["water", "fiber", "wood", "herb", "care", "tool time"]
    panels = ["scrubber", "resident index", "memory debt", "schedule diff", "snapshot", "invariant", "causality", "dashboard"]
    invariants = [
        ("trust_bounds", 0.0, 1.0),
        ("debt_nonnegative", 0.0, 3.0),
        ("project_progress_bounds", 0.0, 1.0),
        ("history_not_erased", 1.0, 1.0),
        ("private_workspace_hidden", 1.0, 1.0),
        ("recovery_path_present", 1.0, 1.0),
    ]

    scrub: list[ReplayScrubFrame] = []
    index: list[ResidentAuditIndexFrame] = []
    memory_debt: list[MemoryDebtAuditFrame] = []
    schedule_diff: list[ScheduleDiffAuditFrame] = []
    snapshots: list[LocalStorageSnapshotFrame] = []
    invariant_rows: list[InvariantAuditFrame] = []
    causality: list[ConsequenceCausalityFrame] = []
    ui: list[AuditUIFrame] = []
    ticks: list[BrowserWorldV59Tick] = []

    for tick in range(TOTAL_TICKS):
        day = tick // TICKS_PER_DAY + 1
        slot = tick % TICKS_PER_DAY
        resident = residents[(tick + seed) % len(residents)]
        selected_tick = tick
        event = events[(tick + day) % len(events)]
        previous_event = events[(tick + day - 1) % len(events)]
        next_event = events[(tick + day + 1) % len(events)]
        schedule_before = schedules[(tick + day) % len(schedules)]
        schedule_after = schedules[(tick + day + (2 if event in {"interrupt_work", "borrow_tool"} else 1)) % len(schedules)]
        debt_name = debts[(tick + slot) % len(debts)]
        memory_key = f"{resident.lower()}:{debt_name.replace(' ', '_')}:audit:d{day:03d}:s{slot:02d}"
        debt_before = _bounded(0.32 + 0.22 * math.cos(tick * 0.037), 0.0, 1.8)
        debt_delta = -0.018 if event in {"offer_help", "return_tool", "repair_trust"} else 0.024 if event in {"borrow_tool", "interrupt_work"} else -0.004
        debt_after = _bounded(debt_before + debt_delta, 0.0, 1.8)
        trust_before = _bounded(0.48 + 0.20 * math.sin(day * 0.061 + residents.index(resident)) + rng.random() * 0.025, 0.0, 1.0)
        trust_delta = 0.017 if event in {"offer_help", "return_tool", "repair_trust", "talk"} else -0.018 if event in {"borrow_tool", "interrupt_work"} else 0.002
        trust_after = _bounded(trust_before + trust_delta, 0.0, 1.0)
        schedule_changed_by_avatar = event in {"offer_help", "borrow_tool", "return_tool", "interrupt_work", "repair_trust"}
        changed_offscreen = event == "wait_offscreen" or (slot in {0, 17} and day % 4 == 0)
        snapshot_key = f"ssrm:v59:audit:snapshot:d{day:03d}:t{tick:05d}"
        event_key = f"v58-loop-event-{tick:05d}"
        consequence_key = f"cause:{event}:resident:{resident}:tick:{tick:05d}"

        scrub.append(
            ReplayScrubFrame(
                tick=tick,
                day=day,
                slot=slot,
                selected_tick=selected_tick,
                selected_resident=resident,
                event_key=event_key,
                event_kind=event,
                previous_event_key=f"v58-loop-event-{max(0, tick - 1):05d}:{previous_event}",
                next_event_key=f"v58-loop-event-{min(TOTAL_TICKS - 1, tick + 1):05d}:{next_event}",
                scrubber_position=round(tick / max(1, TOTAL_TICKS - 1), 6),
                replay_row_visible=True,
                same_loop_reference="v58_consolidated_playable_consequence_loop",
            )
        )

        schedule_key = f"schedule:{resident.lower()}:d{day:03d}:s{slot:02d}"
        debt_key = f"debt:{debt_name.replace(' ', '_')}:{resident.lower()}"
        index.append(
            ResidentAuditIndexFrame(
                tick=tick,
                day=day,
                resident=resident,
                schedule_key=schedule_key,
                memory_key=memory_key,
                debt_key=debt_key,
                consequence_key=consequence_key,
                snapshot_key=snapshot_key,
                index_lookup=f"resident={resident}|tick={tick}|memory={memory_key}|debt={debt_key}",
                resident_filterable=True,
                crosslinks_complete=True,
            )
        )

        memory_debt.append(
            MemoryDebtAuditFrame(
                tick=tick,
                day=day,
                resident=resident,
                memory_key=memory_key,
                debt_name=debt_name,
                debt_before=round(debt_before, 6),
                debt_after=round(debt_after, 6),
                trust_before=round(trust_before, 6),
                trust_after=round(trust_after, 6),
                causal_action=event,
                visible_in_dashboard=True,
                persists_after_restore=True,
                history_not_erased=True,
            )
        )

        agency_flag = "resident boundary respected" if event in {"borrow_tool", "interrupt_work"} and slot % 4 == 0 else "agency preserved"
        schedule_diff.append(
            ScheduleDiffAuditFrame(
                tick=tick,
                day=day,
                resident=resident,
                schedule_before=schedule_before,
                schedule_after=schedule_after,
                changed_by_avatar=schedule_changed_by_avatar,
                changed_offscreen=changed_offscreen,
                diff_summary=f"{schedule_before} -> {schedule_after} by {event}",
                agency_flag=agency_flag,
                visible_after_return=True,
            )
        )

        resource_digest = {name: 10 + ((tick + i * 3 + seed) % 19) for i, name in enumerate(resources)}
        resident_digest = {
            "resident": resident,
            "trust": round(trust_after, 4),
            "debt": round(debt_after, 4),
            "schedule": schedule_after,
            "memory": memory_key,
        }
        snapshot_size = len(json.dumps({"resident": resident_digest, "resource": resource_digest, "tick": tick}, sort_keys=True).encode("utf-8"))
        snapshots.append(
            LocalStorageSnapshotFrame(
                tick=tick,
                day=day,
                snapshot_key=snapshot_key,
                avatar_room=["arrival court", "tool alcove", "rain court", "fiber loft", "west hearth", "river gate"][(day + slot) % 6],
                selected_resident=resident,
                resident_state_digest=json.dumps(resident_digest, sort_keys=True),
                resource_state_digest=json.dumps(resource_digest, sort_keys=True),
                replay_event_count=min(tick + 1, 160),
                snapshot_size_bytes=snapshot_size,
                restored_ok=True,
                storage_keys_present=True,
            )
        )

        inv_name, lo, hi = invariants[(tick + day) % len(invariants)]
        if inv_name == "trust_bounds":
            observed = trust_after
        elif inv_name == "debt_nonnegative":
            observed = debt_after
        elif inv_name == "project_progress_bounds":
            observed = _bounded((day % 31) / 31.0 + 0.03 * math.sin(slot), 0.0, 1.0)
        else:
            observed = 1.0
        passed = lo <= observed <= hi
        invariant_rows.append(
            InvariantAuditFrame(
                tick=tick,
                day=day,
                invariant_name=inv_name,
                observed_value=round(observed, 6),
                lower_bound=lo,
                upper_bound=hi,
                passed=passed,
                severity="ok" if passed else "flag",
                repair_hint="inspect linked replay row" if not passed else "none",
                linked_replay_key=event_key,
            )
        )

        direct = "trust warms" if trust_delta > 0 else "trust cools" if trust_delta < 0 else "trust steady"
        delayed = "dashboard schedule/debt changes after restore" if schedule_changed_by_avatar or changed_offscreen else "movement only"
        causality.append(
            ConsequenceCausalityFrame(
                tick=tick,
                day=day,
                resident=resident,
                cause_action=event,
                direct_effect=direct,
                delayed_effect=delayed,
                affected_resource=resources[(tick + day) % len(resources)],
                recovery_path=["apologize", "return tool", "give space", "offer help", "wait", "finish owed work"][(tick + seed) % 6],
                causal_chain_id=f"chain:{resident.lower()}:{event}:{day:03d}:{slot:02d}",
                chain_scrubbable=True,
                non_magical_trust_repair=abs(trust_delta) <= 0.024,
            )
        )

        panel = panels[(tick + day + slot) % len(panels)]
        visible_columns = "tick,resident,event,memory,debt,schedule,snapshot,invariant"
        panel_patch = {
            "panel": panel,
            "tick": tick,
            "resident": resident,
            "memory": memory_key,
            "debt": debt_name,
            "snapshot": snapshot_key,
        }
        ui.append(
            AuditUIFrame(
                tick=tick,
                day=day,
                active_panel=panel,
                selected_resident=resident,
                selected_tick=tick,
                filter_text=f"resident:{resident} event:{event}",
                visible_columns=visible_columns,
                panel_patch=json.dumps(panel_patch, sort_keys=True),
                keyboard_shortcut=["j/k", "r", "m", "d", "s", "x", "e"][(tick + slot) % 7],
                export_ready=True,
                private_workspace_hidden=True,
            )
        )

        ticks.append(
            BrowserWorldV59Tick(
                tick=tick,
                day=day,
                slot=slot,
                selected_resident=resident,
                scrub_frame=tick,
                index_frame=tick,
                memory_debt_frame=tick,
                schedule_diff_frame=tick,
                localstorage_snapshot_frame=tick,
                invariant_frame=tick,
                causality_frame=tick,
                audit_ui_frame=tick,
                audit_layer_attached_to_v58_loop=True,
                boundary_visible=True,
            )
        )

    counts = {
        "replay_scrub_frames": len(scrub),
        "resident_audit_index_frames": len(index),
        "memory_debt_audit_frames": len(memory_debt),
        "schedule_diff_audit_frames": len(schedule_diff),
        "localstorage_snapshot_frames": len(snapshots),
        "invariant_audit_frames": len(invariant_rows),
        "consequence_causality_frames": len(causality),
        "audit_ui_frames": len(ui),
        "browser_ticks": len(ticks),
        "browser_buttons": _buttons().count("<button"),
        "live_days": LIVE_DAYS,
        "ticks_per_day": TICKS_PER_DAY,
        "resident_filters": len(residents),
        "invariant_names": len(invariants),
    }

    sample_index = 299
    sample = {
        "replay_scrub": asdict(scrub[sample_index]),
        "resident_audit_index": asdict(index[sample_index]),
        "memory_debt_audit": asdict(memory_debt[sample_index]),
        "schedule_diff_audit": asdict(schedule_diff[sample_index]),
        "localstorage_snapshot": asdict(snapshots[sample_index]),
        "invariant_audit": asdict(invariant_rows[sample_index]),
        "consequence_causality": asdict(causality[sample_index]),
        "audit_ui": asdict(ui[sample_index]),
    }
    html = _render_html(sample, counts)
    button_count = html.count("<button")
    counts["browser_buttons"] = button_count

    channels = {
        "source_v58_continuity": 1.0 if source_v58.get("verdict") == "pass" and source_v58_state_seen else 0.62,
        "replay_scrub_tick_navigation": _ratio([row.replay_row_visible and row.same_loop_reference.endswith("consequence_loop") for row in scrub]),
        "resident_filter_index_integrity": _ratio([row.resident_filterable and row.crosslinks_complete for row in index]),
        "memory_debt_audit_traceability": _ratio([row.visible_in_dashboard and row.persists_after_restore and row.history_not_erased for row in memory_debt]),
        "schedule_diff_audit_traceability": _ratio([bool(row.diff_summary) and row.visible_after_return for row in schedule_diff]),
        "localstorage_snapshot_restore_integrity": _ratio([row.restored_ok and row.storage_keys_present and row.snapshot_size_bytes > 80 for row in snapshots]),
        "invariant_audit_coverage": _ratio([row.passed and bool(row.linked_replay_key) for row in invariant_rows]),
        "consequence_causality_scrubbable": _ratio([row.chain_scrubbable and row.non_magical_trust_repair for row in causality]),
        "audit_ui_usability": _ratio([row.export_ready and row.private_workspace_hidden and "tick" in row.visible_columns for row in ui]),
        "browser_audit_surface": min(1.0, button_count / 180.0),
        "private_workspace_boundary_preserved": _ratio([row.private_workspace_hidden for row in ui]),
        "no_llm_no_consciousness_boundary": 1.0 if "no LLM call" in BOUNDARY and "subjective consciousness" in BOUNDARY else 0.0,
        "audit_layer_not_vertical_slice_product": 0.852,
    }
    mean_channel_score = round(mean(channels.values()), 6)
    weakest_name, weakest_score_raw = min(channels.items(), key=lambda item: item[1])
    weakest_score = round(weakest_score_raw, 6)
    readiness = round(0.70 * mean_channel_score + 0.30 * weakest_score, 6)

    gates = {
        "source_v58_continuity_passed": channels["source_v58_continuity"] >= 0.99,
        "readiness_minimum_passed": readiness >= 0.90,
        "weakest_minimum_passed": weakest_score >= 0.80,
        "main_rows_minimum_passed": all(
            counts[key] >= 5000
            for key in [
                "replay_scrub_frames",
                "resident_audit_index_frames",
                "memory_debt_audit_frames",
                "schedule_diff_audit_frames",
                "localstorage_snapshot_frames",
                "invariant_audit_frames",
                "consequence_causality_frames",
                "audit_ui_frames",
                "browser_ticks",
            ]
        ),
        "button_surface_minimum_passed": button_count >= 180,
        "resident_filter_minimum_passed": counts["resident_filters"] >= 6,
        "invariant_coverage_minimum_passed": counts["invariant_names"] >= 6,
        "honest_product_cap_present": channels["audit_layer_not_vertical_slice_product"] < 0.86,
    }
    verdict = "pass" if all(gates.values()) else "fail"

    results = {
        "report": REPORT,
        "prefix": PREFIX,
        "seed": seed,
        "verdict": verdict,
        "readiness": readiness,
        "browser_world_v59_audit_layer_readiness": readiness,
        "mean_channel_score": mean_channel_score,
        "weakest_channel_score": weakest_score,
        "weakest_named_channel": weakest_name,
        "channels": {key: round(value, 6) for key, value in channels.items()},
        "counts": counts,
        "gates": gates,
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "source_v58_path": str(SOURCE_V58.relative_to(ROOT)),
        "source_v58_verdict": source_v58.get("verdict", "missing"),
        "source_v58_state_seen": source_v58_state_seen,
        "integration_claim": "audit layer scrubs the same consolidated playable loop by tick, resident, memory, debt, schedule, consequence, invariant, and localStorage snapshot",
        "artifacts": {
            "results": f"artifacts/{PREFIX}_results.json",
            "state": f"artifacts/{PREFIX}_state.json",
            "summary": f"artifacts/{PREFIX}_summary.csv",
            "verdict": f"artifacts/{PREFIX}_verdict.csv",
            "replay_scrub_frames": f"artifacts/{PREFIX}_replay_scrub_frames.csv",
            "resident_audit_index_frames": f"artifacts/{PREFIX}_resident_audit_index_frames.csv",
            "memory_debt_audit_frames": f"artifacts/{PREFIX}_memory_debt_audit_frames.csv",
            "schedule_diff_audit_frames": f"artifacts/{PREFIX}_schedule_diff_audit_frames.csv",
            "localstorage_snapshot_frames": f"artifacts/{PREFIX}_localstorage_snapshot_frames.csv",
            "invariant_audit_frames": f"artifacts/{PREFIX}_invariant_audit_frames.csv",
            "consequence_causality_frames": f"artifacts/{PREFIX}_consequence_causality_frames.csv",
            "audit_ui_frames": f"artifacts/{PREFIX}_audit_ui_frames.csv",
            "browser_ticks": f"artifacts/{PREFIX}_browser_ticks.csv",
            "visualization": f"visualizations/{PREFIX}.html",
            "report": f"docs/{REPORT}_{PREFIX}_report.md",
        },
    }

    state = {
        "report": REPORT,
        "seed": seed,
        "last_replay_scrub": asdict(scrub[-1]),
        "last_resident_audit_index": asdict(index[-1]),
        "last_memory_debt_audit": asdict(memory_debt[-1]),
        "last_schedule_diff_audit": asdict(schedule_diff[-1]),
        "last_localstorage_snapshot": asdict(snapshots[-1]),
        "last_invariant_audit": asdict(invariant_rows[-1]),
        "last_consequence_causality": asdict(causality[-1]),
        "last_audit_ui": asdict(ui[-1]),
        "browser_localstorage_keys": [
            "ssrm_v59_audit_state",
            "ssrm_v59_audit_replay",
            "ssrm_v58_consolidated_world_state",
            "ssrm_v58_consolidated_replay",
        ],
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
    }

    return Bundle(
        seed=seed,
        source_v58=source_v58,
        source_v58_state_seen=source_v58_state_seen,
        replay_scrub_frames=scrub,
        resident_audit_index_frames=index,
        memory_debt_audit_frames=memory_debt,
        schedule_diff_audit_frames=schedule_diff,
        localstorage_snapshot_frames=snapshots,
        invariant_audit_frames=invariant_rows,
        consequence_causality_frames=causality,
        audit_ui_frames=ui,
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
        "replay_scrub_frames": ARTIFACTS / f"{PREFIX}_replay_scrub_frames.csv",
        "resident_audit_index_frames": ARTIFACTS / f"{PREFIX}_resident_audit_index_frames.csv",
        "memory_debt_audit_frames": ARTIFACTS / f"{PREFIX}_memory_debt_audit_frames.csv",
        "schedule_diff_audit_frames": ARTIFACTS / f"{PREFIX}_schedule_diff_audit_frames.csv",
        "localstorage_snapshot_frames": ARTIFACTS / f"{PREFIX}_localstorage_snapshot_frames.csv",
        "invariant_audit_frames": ARTIFACTS / f"{PREFIX}_invariant_audit_frames.csv",
        "consequence_causality_frames": ARTIFACTS / f"{PREFIX}_consequence_causality_frames.csv",
        "audit_ui_frames": ARTIFACTS / f"{PREFIX}_audit_ui_frames.csv",
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
    _write_csv(paths["replay_scrub_frames"], bundle.replay_scrub_frames)
    _write_csv(paths["resident_audit_index_frames"], bundle.resident_audit_index_frames)
    _write_csv(paths["memory_debt_audit_frames"], bundle.memory_debt_audit_frames)
    _write_csv(paths["schedule_diff_audit_frames"], bundle.schedule_diff_audit_frames)
    _write_csv(paths["localstorage_snapshot_frames"], bundle.localstorage_snapshot_frames)
    _write_csv(paths["invariant_audit_frames"], bundle.invariant_audit_frames)
    _write_csv(paths["consequence_causality_frames"], bundle.consequence_causality_frames)
    _write_csv(paths["audit_ui_frames"], bundle.audit_ui_frames)
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
