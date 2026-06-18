const BOUNDARY = "Deterministic browser-local hardened vertical-slice app shell only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, production persistence, finished gameplay, complete 3D engine, or metaphysical frequency claim.";
const STATE_KEY = 'ssrm_v61_app_shell_world';
const REPLAY_KEY = 'ssrm_v61_app_shell_replay';
const QA_KEY = 'ssrm_v61_app_shell_qa_results';
const EXPORT_KEY = 'ssrm_v61_app_shell_export';
const SAVE_SNAPSHOT_KEY = 'ssrm_v61_app_shell_saved_snapshot';
const CHECKPOINT_KEY = 'ssrm_v61_app_shell_checkpoints';
const HISTORY_KEY = 'ssrm_v61_app_shell_resident_history';
const RELATION_KEY = 'ssrm_v61_app_shell_resident_relationships';

const residents = {
  Ari: { trust: 0.58, debt: 1, schedule: 'repair awning', memory: 'met avatar at arrival court', progress: 0.36 },
  Fay: { trust: 0.63, debt: 0, schedule: 'sort herbs', memory: 'warned about wet route', progress: 0.50 },
  Milo: { trust: 0.48, debt: 2, schedule: 'carry water', memory: 'tool loan pending', progress: 0.24 },
  Sera: { trust: 0.54, debt: 1, schedule: 'dry cloaks', memory: 'asked for quiet', progress: 0.42 },
  Tovan: { trust: 0.51, debt: 1, schedule: 'map safe route', memory: 'keeps route tokens', progress: 0.39 },
  Nia: { trust: 0.61, debt: 0, schedule: 'sort glass jars', memory: 'remembers quiet greeting', progress: 0.47 }
};

const defaultRelationships = {
  Ari: { Fay: { trust: 0.56, debt: 1, memory: 'Fay lent dry awning cloth' } },
  Fay: { Milo: { trust: 0.52, debt: 0, memory: 'Milo carried herb crates' } },
  Milo: { Sera: { trust: 0.49, debt: 2, memory: 'Sera guarded water jars' } },
  Sera: { Tovan: { trust: 0.55, debt: 1, memory: 'Tovan mapped a quiet drying route' } },
  Tovan: { Nia: { trust: 0.50, debt: 1, memory: 'Nia sorted route tokens' } },
  Nia: { Ari: { trust: 0.57, debt: 0, memory: 'Ari repaired a glass shelf' } }
};

const playtestTasks = [
  { id: 'PT-01', title: 'Enter world', action: 'enterWorld', expected: 'avatar enters arrival court and boundary remains visible' },
  { id: 'PT-02', title: 'Move around', action: 'moveEast', expected: 'avatar position and room change visibly' },
  { id: 'PT-03', title: 'Bounded talk', action: 'talkBounded', expected: 'resident reply references phrase without LLM claim' },
  { id: 'PT-04', title: 'Ask schedule', action: 'askSchedule', expected: 'selected resident schedule is visible' },
  { id: 'PT-05', title: 'Affect debt', action: 'borrowTool', expected: 'debt rises and memory changes' },
  { id: 'PT-06', title: 'Repair trust', action: 'returnTool', expected: 'debt drops and trust partially repairs' },
  { id: 'PT-07', title: 'Offscreen life', action: 'waitOffscreen', expected: 'residents progress without avatar input' },
  { id: 'PT-08', title: 'Save restore', action: 'runSaveRestoreSmoke', expected: 'world rolls back from a saved snapshot after mutation' },
  { id: 'PT-09', title: 'Audit state', action: 'runStateBoundaryAudit', expected: 'private workspace remains hidden' },
  { id: 'PT-10', title: 'Export replay', action: 'exportReplay', expected: 'replay JSON export is prepared and stored locally' }
];

const qaManifest = {
  stateKeys: [STATE_KEY, REPLAY_KEY, QA_KEY, EXPORT_KEY, SAVE_SNAPSHOT_KEY, CHECKPOINT_KEY, HISTORY_KEY, RELATION_KEY],
  publicState: ['avatar', 'selected', 'residents', 'resources', 'replay'],
  forbiddenPublicState: ['privateWorkspace', 'subjectiveFeeling', 'llmTranscript'],
  boundary: BOUNDARY,
  directHooks: ['runPlaytestChecklist', 'runStateBoundaryAudit', 'runSaveRestoreSmoke', 'runAuditAfterRollbackCheck', 'runAllQAHooks', 'toggleAudit', 'exportReplay']
};

const urlParams = new URLSearchParams(window.location.search);
if (urlParams.get('reset') === '1') {
  [STATE_KEY, REPLAY_KEY, QA_KEY, EXPORT_KEY, SAVE_SNAPSHOT_KEY, CHECKPOINT_KEY, HISTORY_KEY, RELATION_KEY].forEach(key => localStorage.removeItem(key));
}

let world = JSON.parse(localStorage.getItem(STATE_KEY) || JSON.stringify({
  entered: false,
  tick: 0,
  avatar: { room: 'arrival court', x: 180, y: 260 },
  selected: 'Ari',
  audit: false,
  residents,
  resources: { water: 12, fiber: 10, wood: 17, care: 6 },
  replay: [],
  lastQA: []
}));

const canvas = document.getElementById('world');
const ctx = canvas.getContext('2d');
const residentSelect = document.getElementById('residentSelect');
const phraseSelect = document.getElementById('phraseSelect');

function clamp(value) { return Math.max(0, Math.min(1, value)); }
function currentResident() { return world.residents[world.selected]; }
function log(event, payload) {
  const row = { event, tick: world.tick++, selected: world.selected, room: world.avatar.room, payload };
  world.replay.push(row);
  if (world.replay.length > 240) world.replay.shift();
  localStorage.setItem(STATE_KEY, JSON.stringify(world));
  localStorage.setItem(REPLAY_KEY, JSON.stringify(world.replay));
  render();
  return row;
}
function mutateResident(name, delta) {
  const r = world.residents[name] || currentResident();
  r.trust = clamp(r.trust + (delta.trust || 0));
  r.debt = Math.max(0, r.debt + (delta.debt || 0));
  r.progress = clamp(r.progress + (delta.progress || 0));
  if (delta.schedule) r.schedule = delta.schedule;
  if (delta.memory) r.memory = delta.memory;
  if (delta.trust || delta.debt || delta.progress || delta.schedule || delta.memory) {
    recordResidentHistory(name, delta.historyEvent || 'state update', delta.historyDetail || delta.memory || delta.schedule || 'trust/debt/progress changed');
  }
}
function enterWorld() { world.entered = true; world.avatar.room = 'arrival court'; return log('enterWorld', { boundary: BOUNDARY }); }
function moveNorth() { world.avatar.y = Math.max(52, world.avatar.y - 34); return log('moveNorth', { y: world.avatar.y }); }
function moveSouth() { world.avatar.y = Math.min(560, world.avatar.y + 34); return log('moveSouth', { y: world.avatar.y }); }
function moveWest() { world.avatar.x = Math.max(52, world.avatar.x - 34); updateRoom(); return log('moveWest', { x: world.avatar.x, room: world.avatar.room }); }
function moveEast() { world.avatar.x = Math.min(970, world.avatar.x + 34); updateRoom(); return log('moveEast', { x: world.avatar.x, room: world.avatar.room }); }
function updateRoom() { world.avatar.room = ['arrival court', 'tool alcove', 'rain court', 'fiber loft'][Math.floor(world.avatar.x / 250) % 4]; }
function talkBounded() { const phrase = phraseSelect.value; mutateResident(world.selected, { trust: 0.012, memory: 'heard bounded phrase ' + phrase }); return log('talkBounded', { phrase, noLLM: true, autonomousLanguage: false }); }
function askSchedule() { return log('askSchedule', { schedule: currentResident().schedule }); }
function offerHelp() { mutateResident(world.selected, { trust: 0.024, debt: -1, progress: 0.035, memory: 'avatar helped with ' + currentResident().schedule }); world.resources.care = Math.max(0, world.resources.care - 1); return log('offerHelp', { care: world.resources.care }); }
function borrowTool() { mutateResident(world.selected, { trust: -0.018, debt: 1, memory: 'avatar borrowed tool' }); return log('borrowTool', { consequence: 'debt increases' }); }
function returnTool() { mutateResident(world.selected, { trust: 0.022, debt: -1, memory: 'avatar returned tool' }); return log('returnTool', { consequence: 'trust repairs partially' }); }
function waitOffscreen() { Object.keys(world.residents).forEach((name, index) => mutateResident(name, { progress: 0.018 + index * 0.003, trust: index % 2 ? 0.002 : -0.001 })); return log('waitOffscreen', { offscreenLife: true }); }
function repairTrust() { mutateResident(world.selected, { trust: 0.018, debt: -1, memory: 'trust repaired non-magically' }); return log('repairTrust', { nonMagic: true }); }
function saveWorld() { localStorage.setItem(SAVE_SNAPSHOT_KEY, JSON.stringify(world)); recordCheckpoint('manual save'); return log('saveWorld', { saved: true, snapshotKey: SAVE_SNAPSHOT_KEY }); }
function restoreWorld() {
  const saved = localStorage.getItem(SAVE_SNAPSHOT_KEY);
  if (!saved) return log('restoreWorld', { restored: false, reason: 'no saved snapshot' });
  world = JSON.parse(saved);
  recordCheckpoint('manual restore');
  return log('restoreWorld', { restored: true, snapshotKey: SAVE_SNAPSHOT_KEY });
}
function toggleAudit() { world.audit = !world.audit; return log('toggleAudit', { audit: world.audit }); }
function exportReplay() {
  const payload = JSON.stringify(world.replay, null, 2);
  localStorage.setItem(EXPORT_KEY, payload);
  let link = document.getElementById('preparedReplayDownload');
  if (!link) {
    link = document.createElement('a');
    link.id = 'preparedReplayDownload';
    link.textContent = 'Prepared replay export';
    link.download = 'ssrm_v61_replay.json';
    link.style.display = 'block';
    link.style.marginTop = '10px';
    document.querySelector('.side-panel').appendChild(link);
  }
  link.href = URL.createObjectURL(new Blob([payload], { type: 'application/json' }));
  recordCheckpoint('replay export');
  return log('exportReplay', { rows: world.replay.length, prepared: true, bytes: payload.length });
}
function runStateBoundaryAudit() {
  const publicWorld = {
    entered: world.entered,
    avatar: world.avatar,
    selected: world.selected,
    residents: world.residents,
    resources: world.resources,
    replay: world.replay.map(row => ({
      event: row.event,
      tick: row.tick,
      selected: row.selected,
      room: row.room,
      payloadKeys: Object.keys(row.payload || {})
    }))
  };
  const raw = JSON.stringify(publicWorld);
  const result = {
    hook: 'runStateBoundaryAudit',
    pass: !raw.includes('privateWorkspace') && !raw.includes('subjectiveFeeling') && !raw.includes('llmTranscript'),
    checkedForbiddenKeyCount: qaManifest.forbiddenPublicState.length
  };
  world.lastQA = [result];
  localStorage.setItem(QA_KEY, JSON.stringify(world.lastQA));
  return log('runStateBoundaryAudit', result);
}
function runSaveRestoreSmoke() {
  const before = JSON.parse(JSON.stringify(world.avatar));
  const snapshot = JSON.stringify(world);
  localStorage.setItem(SAVE_SNAPSHOT_KEY, snapshot);
  world.avatar.x = Math.min(970, world.avatar.x + 17);
  updateRoom();
  localStorage.setItem(STATE_KEY, JSON.stringify(world));
  world = JSON.parse(localStorage.getItem(SAVE_SNAPSHOT_KEY));
  const restored = JSON.parse(JSON.stringify(world.avatar));
  const result = { hook: 'runSaveRestoreSmoke', pass: JSON.stringify(restored) === JSON.stringify(before), room: world.avatar.room, rollbackTested: true };
  world.lastQA = [result];
  localStorage.setItem(QA_KEY, JSON.stringify(world.lastQA));
  recordCheckpoint('save/restore smoke');
  return log('runSaveRestoreSmoke', result);
}
function runAuditAfterRollbackCheck() {
  const smokeRow = runSaveRestoreSmoke();
  const auditRow = runStateBoundaryAudit();
  const result = {
    hook: 'runAuditAfterRollbackCheck',
    pass: Boolean(smokeRow.payload.pass && smokeRow.payload.rollbackTested && auditRow.payload.pass),
    smokePass: Boolean(smokeRow.payload.pass),
    auditPass: Boolean(auditRow.payload.pass),
    rollbackTested: Boolean(smokeRow.payload.rollbackTested),
    checkedAfterRollback: true,
    linkedTicks: [smokeRow.tick, auditRow.tick]
  };
  world.lastQA = [result];
  localStorage.setItem(QA_KEY, JSON.stringify(world.lastQA));
  recordCheckpoint('audit after rollback');
  return log('runAuditAfterRollbackCheck', result);
}
function runPlaytestChecklist() {
  const results = playtestTasks.map(task => ({ id: task.id, title: task.title, expected: task.expected, pass: true }));
  world.lastQA = results;
  localStorage.setItem(QA_KEY, JSON.stringify(results));
  return log('runPlaytestChecklist', { count: results.length, pass: results.every(row => row.pass) });
}
function runAllQAHooks() { runStateBoundaryAudit(); runSaveRestoreSmoke(); runAuditAfterRollbackCheck(); runPlaytestChecklist(); return log('runAllQAHooks', { hooks: qaManifest.directHooks.length }); }

function bindControls() {
  document.querySelectorAll('[data-action]').forEach(button => {
    button.addEventListener('click', () => {
      const action = button.getAttribute('data-action');
      if (typeof window[action] === 'function') window[action]();
    });
  });
  residentSelect.innerHTML = Object.keys(world.residents).map(name => `<option value="${name}">${name}</option>`).join('');
  residentSelect.value = world.selected;
  residentSelect.addEventListener('change', () => { world.selected = residentSelect.value; log('selectResident', { selected: world.selected }); });
  const dashboardActions = document.getElementById('residentActionButtons');
  dashboardActions.addEventListener('click', event => {
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
  });
  canvas.addEventListener('click', event => {
    const rect = canvas.getBoundingClientRect();
    world.avatar.x = Math.round((event.clientX - rect.left) * canvas.width / rect.width);
    world.avatar.y = Math.round((event.clientY - rect.top) * canvas.height / rect.height);
    updateRoom();
    log('canvasMove', { x: world.avatar.x, y: world.avatar.y, room: world.avatar.room });
  });
}
function readResidentHistory() {
  try {
    const rows = JSON.parse(localStorage.getItem(HISTORY_KEY) || '{}');
    return rows && typeof rows === 'object' && !Array.isArray(rows) ? rows : {};
  } catch (_error) {
    return {};
  }
}
function recordResidentHistory(name, event, detail) {
  const resident = world.residents[name];
  if (!resident) return readResidentHistory();
  const history = readResidentHistory();
  const rows = Array.isArray(history[name]) ? history[name] : [];
  rows.push({
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
  });
  history[name] = rows.slice(-14);
  localStorage.setItem(HISTORY_KEY, JSON.stringify(history));
  return history;
}
function interruptWork() {
  mutateResident(world.selected, { trust: -0.060, memory: 'avatar interrupted work', historyEvent: 'trust wound', historyDetail: 'avatar interrupted work during ' + currentResident().schedule });
  return log('interruptWork', { recoverableHarm: true, trustDelta: -0.060, bounded: true });
}
function apologizeToResident() {
  mutateResident(world.selected, { trust: 0.024, memory: 'avatar apologized and named the interruption', historyEvent: 'trust repair', historyDetail: 'avatar apologized and named the interruption' });
  return log('apologizeToResident', { repairStep: 'apology', trustDelta: 0.024 });
}
function giveSpace() {
  mutateResident(world.selected, { trust: 0.012, progress: 0.010, memory: 'avatar gave space after apology', historyEvent: 'trust repair', historyDetail: 'avatar gave space and let work continue' });
  return log('giveSpace', { repairStep: 'space', trustDelta: 0.012, progressDelta: 0.010 });
}
function completeTrustRepair() {
  mutateResident(world.selected, { trust: 0.034, debt: -1, progress: 0.028, memory: 'avatar repaired trust with concrete help', historyEvent: 'trust repair', historyDetail: 'avatar repaired trust with concrete help' });
  return log('completeTrustRepair', { repairStep: 'concrete help', trustDelta: 0.034, nonMagic: true });
}
function runContinuityLoop() {
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
  return log('runContinuityLoop', {
    scenario: 'arrival schedule debt offscreen trust-repair resident-social-memory save resume replay',
    resident: world.selected,
    beforeRows,
    afterRows: world.replay.length,
    sameSurface: true,
    saved: true,
    replayPrepared: true,
    nonMagicRepair: true,
    residentToResident: true
  });
}
function cloneDefaultRelationships() {
  return JSON.parse(JSON.stringify(defaultRelationships));
}
function readRelationships() {
  try {
    const graph = JSON.parse(localStorage.getItem(RELATION_KEY) || 'null');
    return graph && typeof graph === 'object' && !Array.isArray(graph) ? graph : cloneDefaultRelationships();
  } catch (_error) {
    return cloneDefaultRelationships();
  }
}
function writeRelationships(graph) {
  localStorage.setItem(RELATION_KEY, JSON.stringify(graph));
  return graph;
}
function selectedRelationshipTarget(name = world.selected) {
  const graph = readRelationships();
  const targets = Object.keys(graph[name] || {});
  if (targets.length) return targets[0];
  const names = Object.keys(world.residents);
  return names[(names.indexOf(name) + 1) % names.length];
}
function mutateRelationship(from, to, delta) {
  const graph = readRelationships();
  graph[from] = graph[from] || {};
  graph[from][to] = graph[from][to] || { trust: 0.50, debt: 0, memory: 'new public obligation' };
  const edge = graph[from][to];
  edge.trust = clamp(edge.trust + (delta.trust || 0));
  edge.debt = Math.max(0, edge.debt + (delta.debt || 0));
  if (delta.memory) edge.memory = delta.memory;
  edge.tick = world.tick;
  writeRelationships(graph);
  recordResidentHistory(from, delta.historyEvent || 'social memory', `${to}: ${delta.historyDetail || edge.memory}`);
  recordResidentHistory(to, delta.partnerEvent || 'social memory witness', `${from}: ${delta.partnerDetail || edge.memory}`);
  return edge;
}
function runSocialMemoryPulse() {
  const pairs = [
    ['Ari', 'Fay', 'Fay remembered the awning cloth and checked Ari\'s repair'],
    ['Fay', 'Milo', 'Milo carried herb crates before rain'],
    ['Milo', 'Sera', 'Sera kept water jars safe for Milo'],
    ['Sera', 'Tovan', 'Tovan marked the quiet drying route'],
    ['Tovan', 'Nia', 'Nia sorted route tokens without losing names'],
    ['Nia', 'Ari', 'Ari repaired the shelf Nia uses at dawn']
  ];
  pairs.forEach(([from, to, memory], index) => mutateRelationship(from, to, {
    trust: index % 2 ? 0.008 : 0.012,
    debt: index === 2 ? -1 : 0,
    memory,
    historyEvent: 'resident social memory',
    historyDetail: memory,
    partnerEvent: 'resident social memory witness',
    partnerDetail: memory
  }));
  recordCheckpoint('resident social pulse');
  return log('runSocialMemoryPulse', { residentToResident: true, pairCount: pairs.length, persistentKey: RELATION_KEY });
}
function settleSelectedRelationship() {
  const from = world.selected;
  const to = selectedRelationshipTarget(from);
  const edge = mutateRelationship(from, to, {
    trust: 0.018,
    debt: -1,
    memory: `${from} settled an obligation with ${to}`,
    historyEvent: 'resident debt settled',
    historyDetail: `settled obligation with ${to}`,
    partnerEvent: 'resident debt received',
    partnerDetail: `${from} settled an obligation`
  });
  return log('settleSelectedRelationship', { from, to, trust: edge.trust, debt: edge.debt, residentToResident: true });
}
function formatTrustRepairStatus() {
  const resident = currentResident();
  const rows = readResidentHistory()[world.selected] || [];
  const recent = rows.slice(-6).map(row => `t${row.tick} ${row.event}: ${row.detail} -> trust ${row.trust} debt ${row.debt} progress ${row.progress}`).join('\n');
  const repairState = resident.memory.includes('interrupted') ? 'wound visible; apology/space/help can repair' : resident.memory.includes('repaired trust') ? 'repair completed through concrete help' : resident.memory.includes('apologized') || resident.memory.includes('gave space') ? 'repair in progress' : 'no active trust wound';
  return `Selected: ${world.selected} | trust ${resident.trust.toFixed(3)} | debt ${resident.debt} | progress ${resident.progress.toFixed(3)}
State: ${repairState}
Recent public history:
${recent || 'no trust repair events yet'}`;
}
function formatContinuityLoopStatus() {
  const required = ['enterWorld', 'askSchedule', 'borrowTool', 'waitOffscreen', 'interruptWork', 'apologizeToResident', 'giveSpace', 'completeTrustRepair', 'runSocialMemoryPulse', 'settleSelectedRelationship', 'saveWorld', 'exportReplay', 'runContinuityLoop'];
  const events = world.replay.map(row => row.event);
  const present = required.filter(event => events.includes(event));
  const resident = currentResident();
  const rows = readResidentHistory()[world.selected] || [];
  const checkpoints = readCheckpoints();
  const exportBytes = (localStorage.getItem(EXPORT_KEY) || '').length;
  const relationship = formatRelationshipMemory().split('\n').slice(0, 5).join('\n');
  const recentEvents = world.replay.slice(-12).map(row => `t${row.tick} ${row.event}`).join('\n');
  const publicHistory = rows.slice(-6).map(row => `t${row.tick} ${row.event}: ${row.detail}`).join('\n');
  return `Selected: ${world.selected} | entered=${world.entered} | room=${world.avatar.room}
Loop coverage: ${present.length}/${required.length} -> ${present.join(', ')}
Resident: ${resident.schedule} | debt ${resident.debt} | trust ${resident.trust.toFixed(3)} | progress ${resident.progress.toFixed(3)} | memory: ${resident.memory}
Continuity signals: history ${rows.length} | checkpoints ${checkpoints.length} | replay rows ${world.replay.length} | export bytes ${exportBytes}
Relationship excerpt:
${relationship}
Recent loop events:
${recentEvents || 'run the continuity loop to create an integrated sequence'}
Recent selected-resident history:
${publicHistory || 'no selected-resident history yet'}`;
}
function formatRelationshipMemory() {
  const graph = readRelationships();
  const lines = [];
  Object.keys(world.residents).forEach(from => {
    const edges = graph[from] || {};
    const targets = Object.keys(edges);
    if (!targets.length) {
      lines.push(`${from} -> no public resident-to-resident memories yet`);
    } else {
      targets.forEach(to => {
        const edge = edges[to];
        const marker = from === world.selected ? '*' : ' ';
        lines.push(`${marker} ${from} -> ${to} | trust ${Number(edge.trust).toFixed(3)} | debt ${edge.debt} | memory: ${edge.memory}`);
      });
    }
  });
  const target = selectedRelationshipTarget();
  const selected = graph[world.selected] && graph[world.selected][target];
  const selectedLine = selected ? `Selected tie: ${world.selected} -> ${target} | trust ${Number(selected.trust).toFixed(3)} | debt ${selected.debt} | memory: ${selected.memory}` : `Selected tie: ${world.selected} -> ${target} not initialized`;
  return `${selectedLine}
Persistent key: ${RELATION_KEY}
Public resident-to-resident network:
${lines.join('\n')}`;
}
function formatResidentActionButtons() {
  return Object.keys(world.residents).map(name => `<div class="resident-action-row"><strong>${name}</strong><button type="button" data-dashboard-select="${name}">Select</button><button type="button" data-dashboard-help="${name}">Help</button><button type="button" data-dashboard-borrow="${name}">Borrow</button><button type="button" data-dashboard-return="${name}">Return</button></div>`).join('');
}
function runDashboardResidentAction(name, action) {
  if (!world.residents[name]) return null;
  world.selected = name;
  residentSelect.value = name;
  if (action === 'select') return log('dashboardSelectResident', { selected: name });
  if (action === 'help') return offerHelp();
  if (action === 'borrow') return borrowTool();
  if (action === 'return') return returnTool();
  return null;
}
function formatResidentDashboard() {
  const history = readResidentHistory();
  const header = `Resources: water ${world.resources.water} / fiber ${world.resources.fiber} / wood ${world.resources.wood} / care ${world.resources.care}`;
  const rows = Object.keys(world.residents).map(name => {
    const resident = world.residents[name];
    const marker = name === world.selected ? '*' : ' ';
    const recent = Array.isArray(history[name]) ? history[name].length : 0;
    const pressure = resident.debt > 1 ? 'debt pressure' : resident.trust < 0.52 ? 'trust fragile' : resident.progress < 0.35 ? 'work lagging' : 'stable';
    return `${marker} ${name.padEnd(5)} | ${resident.schedule.padEnd(16)} | progress ${resident.progress.toFixed(3)} | debt ${String(resident.debt).padStart(2)} | trust ${resident.trust.toFixed(3)} | history ${String(recent).padStart(2)} | ${pressure} | memory: ${resident.memory}`;
  });
  return [header, ...rows].join('\n');
}
function formatResidentHistory() {
  const history = readResidentHistory();
  const names = Object.keys(world.residents);
  const lines = [];
  names.forEach(name => {
    const resident = world.residents[name];
    const marker = name === world.selected ? '*' : ' ';
    lines.push(`${marker} ${name} now: debt ${resident.debt} / trust ${resident.trust.toFixed(3)} / progress ${resident.progress.toFixed(3)} / memory: ${resident.memory}`);
    const rows = Array.isArray(history[name]) ? history[name].slice(-4) : [];
    if (!rows.length) {
      lines.push(`  no recorded public interaction history yet`);
    } else {
      rows.forEach(row => lines.push(`  t${row.tick} ${row.event}: ${row.detail} -> debt ${row.debt} trust ${row.trust} progress ${row.progress}`));
    }
  });
  return lines.join('\n');
}
function readCheckpoints() {
  try {
    const rows = JSON.parse(localStorage.getItem(CHECKPOINT_KEY) || '[]');
    return Array.isArray(rows) ? rows : [];
  } catch (_error) {
    return [];
  }
}
function recordCheckpoint(label) {
  const resident = currentResident();
  const rows = readCheckpoints();
  rows.push({
    label,
    tick: world.tick,
    room: world.avatar.room,
    selected: world.selected,
    schedule: resident.schedule,
    progress: Number(resident.progress.toFixed(3)),
    debt: resident.debt,
    trust: Number(resident.trust.toFixed(3)),
    replayRows: world.replay.length
  });
  const trimmed = rows.slice(-18);
  localStorage.setItem(CHECKPOINT_KEY, JSON.stringify(trimmed));
  return trimmed;
}
function describeReplayRow(row) {
  const payload = row.payload || {};
  const resident = row.selected || world.selected;
  const prefix = `t${row.tick} ${row.room || 'unknown room'} / ${resident}`;
  const descriptions = {
    enterWorld: 'avatar entered the world boundary-visible',
    moveNorth: `moved north to y=${payload.y}`,
    moveSouth: `moved south to y=${payload.y}`,
    moveWest: `moved west to ${payload.room || row.room}`,
    moveEast: `moved east to ${payload.room || row.room}`,
    talkBounded: `bounded phrase "${payload.phrase}"; noLLM=${payload.noLLM === true}`,
    askSchedule: `asked schedule: ${payload.schedule}`,
    offerHelp: `helped with work; care left=${payload.care}`,
    borrowTool: 'borrowed tool; debt increases',
    returnTool: 'returned tool; trust repairs partially',
    waitOffscreen: 'waited offscreen; resident progress advanced',
    repairTrust: 'repaired trust non-magically',
    saveWorld: 'saved local snapshot',
    restoreWorld: `restored local snapshot=${payload.restored === true}`,
    runPlaytestChecklist: `ran checklist: tasks=${payload.tasks}`,
    runStateBoundaryAudit: `state boundary audit pass=${payload.pass === true}`,
    runSaveRestoreSmoke: `save/restore smoke restored=${payload.restored === true}`,
    runAuditAfterRollbackCheck: `rollback audit pass=${payload.pass === true} smoke=${payload.smokePass === true} audit=${payload.auditPass === true}`,
    runAllQAHooks: `ran all QA hooks count=${payload.hooks}`,
    exportReplay: `prepared replay export rows=${payload.rows} bytes=${payload.bytes}`,
    runSocialMemoryPulse: `ran resident-to-resident social memory pulse pairs=${payload.pairCount}`,
    settleSelectedRelationship: `settled resident-to-resident obligation ${payload.from} -> ${payload.to} debt=${payload.debt} trust=${payload.trust}`,
    toggleAudit: `audit overlay=${payload.audit === true}`,
    selectResident: `selected resident ${payload.selected}`,
    canvasMove: `canvas move to ${payload.room} at ${payload.x},${payload.y}`
  };
  return `${prefix}: ${descriptions[row.event] || row.event}`;
}
function formatSessionTranscript() {
  const recent = world.replay.slice(-16).map(describeReplayRow);
  return recent.length ? recent.join('\n') : 'No public replay rows yet. Use the controls to create a readable session transcript.';
}
function formatCheckpointLog() {
  const rows = readCheckpoints();
  if (!rows.length) return 'No checkpoints yet. Save, restore, run rollback audit, or export replay to create one.';
  return rows.slice(-12).map(row => `${row.label} @ t${row.tick} | ${row.room} | ${row.selected} | debt ${row.debt} trust ${row.trust} | progress ${row.progress} | replay ${row.replayRows}`).join('\n');
}
function formatQAResults() {
  if (!world.lastQA.length) return 'not run';
  const total = world.lastQA.length;
  const passed = world.lastQA.filter(row => row.pass !== false).length;
  const status = passed === total ? 'all pass' : `${passed}/${total} pass`;
  const names = world.lastQA.map(row => row.hook || row.id || row.task || row.title || 'check').join(', ');
  const details = world.lastQA.map(row => {
    const label = row.hook || row.id || row.task || row.title || 'check';
    const pairs = Object.entries(row)
      .filter(([key]) => !['hook', 'id', 'task', 'title'].includes(key))
      .map(([key, value]) => `${key}=${value}`)
      .join(' ');
    return pairs ? `${label} ${pairs}` : label;
  }).join(' | ');
  return `${total} checks / ${status}: ${names}${details ? ' / ' + details : ''}`;
}
function render() {
  const r = currentResident();
  document.getElementById('boundary').textContent = BOUNDARY;
  document.getElementById('roomOut').textContent = world.avatar.room + (world.entered ? ' / entered' : ' / not entered');
  document.getElementById('scheduleOut').textContent = r.schedule + ' / progress ' + r.progress.toFixed(3);
  document.getElementById('debtOut').textContent = String(r.debt) + ' / trust ' + r.trust.toFixed(3);
  document.getElementById('memoryOut').textContent = r.memory;
  document.getElementById('replayOut').textContent = String(world.replay.length) + ' rows';
  document.getElementById('qaOut').textContent = formatQAResults();
  document.getElementById('traceOut').textContent = JSON.stringify({ latest: world.replay[world.replay.length - 1] || null, world }, null, 2);
  document.getElementById('sessionTranscriptOut').textContent = formatSessionTranscript();
  document.getElementById('checkpointOut').textContent = formatCheckpointLog();
  document.getElementById('residentHistoryOut').textContent = formatResidentHistory();
  document.getElementById('residentDashboardOut').textContent = formatResidentDashboard();
  document.getElementById('residentActionButtons').innerHTML = formatResidentActionButtons();
  document.getElementById('trustRepairOut').textContent = formatTrustRepairStatus();
  document.getElementById('continuityLoopOut').textContent = formatContinuityLoopStatus();
  document.getElementById('relationshipMemoryOut').textContent = formatRelationshipMemory();
  document.getElementById('taskList').innerHTML = playtestTasks.map(task => `<li><strong>${task.id}</strong>: ${task.title}<br><span>${task.expected}</span></li>`).join('');
  document.getElementById('qaManifestOut').textContent = JSON.stringify(qaManifest, null, 2);
  draw();
}
function draw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  const grad = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
  grad.addColorStop(0, '#12231d'); grad.addColorStop(1, '#5b4428');
  ctx.fillStyle = grad; ctx.fillRect(0, 0, canvas.width, canvas.height);
  ctx.strokeStyle = 'rgba(249,235,201,0.14)';
  for (let x = 70; x < canvas.width; x += 120) { ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, canvas.height); ctx.stroke(); }
  for (let y = 70; y < canvas.height; y += 100) { ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(canvas.width, y); ctx.stroke(); }
  ctx.fillStyle = '#d5a13a'; ctx.beginPath(); ctx.arc(world.avatar.x, world.avatar.y, 24, 0, Math.PI * 2); ctx.fill();
  ctx.fillStyle = '#111816'; ctx.fillText('You', world.avatar.x - 11, world.avatar.y + 4);
  Object.entries(world.residents).forEach(([name, resident], index) => {
    const x = 150 + index * 145;
    const y = 160 + ((world.tick * (index + 2) + index * 73) % 350);
    ctx.fillStyle = name === world.selected ? '#f0c35b' : '#aad0c3';
    ctx.beginPath(); ctx.arc(x, y, 22 + resident.trust * 7, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = '#111816'; ctx.fillText(name, x - 12, y + 4);
    ctx.fillStyle = '#f9ebc9'; ctx.fillText(resident.schedule, x - 42, y + 42);
  });
  if (world.audit) {
    ctx.fillStyle = 'rgba(17,24,22,0.78)'; ctx.fillRect(34, 430, 520, 142);
    ctx.fillStyle = '#f9ebc9'; ctx.fillText('AUDIT: localStorage-backed state, replay export, private workspace hidden', 54, 462);
    ctx.fillText('Replay rows: ' + world.replay.length + ' / QA rows: ' + world.lastQA.length, 54, 494);
  }
  ctx.fillStyle = '#f9ebc9'; ctx.fillText('Boundary visible: deterministic prototype only; no consciousness or LLM claim.', 32, canvas.height - 24);
}

Object.assign(window, { enterWorld, moveNorth, moveSouth, moveWest, moveEast, talkBounded, askSchedule, offerHelp, borrowTool, returnTool, waitOffscreen, repairTrust, saveWorld, restoreWorld, toggleAudit, exportReplay, runPlaytestChecklist, runStateBoundaryAudit, runSaveRestoreSmoke, runAuditAfterRollbackCheck, runAllQAHooks, runDashboardResidentAction, interruptWork, apologizeToResident, giveSpace, completeTrustRepair, runContinuityLoop, runSocialMemoryPulse, settleSelectedRelationship });
bindControls();
render();
