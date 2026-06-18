const HANDOFF_KEY = 'ssrm_primary_demo_handoff';
const MANUAL_RECORD_KEY = 'ssrm_primary_demo_manual_pass_records';
const DEFECT_LEDGER_KEY = 'ssrm_primary_demo_defect_ledger';
const RECORDER_EXPORT_KEY = 'ssrm_primary_demo_recorder_export';

function recordLaunch(kind) {
  const payload = {
    kind,
    report: 303,
    target: '../ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html',
    recordedAt: new Date().toISOString(),
    boundary: 'primary-demo-launcher-only'
  };
  localStorage.setItem(HANDOFF_KEY, JSON.stringify(payload));
  renderHandoff(payload);
}

function renderHandoff(payload) {
  const node = document.getElementById('handoffStatus');
  if (!node) return;
  node.textContent = `Last handoff: ${payload.kind} launch toward ${payload.target} at ${payload.recordedAt}.`;
}

for (const [id, kind] of [['cleanLaunch', 'clean'], ['resumeLaunch', 'resume']]) {
  const node = document.getElementById(id);
  if (node) node.addEventListener('click', () => recordLaunch(kind));
}

try {
  const existing = JSON.parse(localStorage.getItem(HANDOFF_KEY) || 'null');
  if (existing) renderHandoff(existing);
} catch (error) {
  localStorage.removeItem(HANDOFF_KEY);
}

function readList(key) {
  try {
    return JSON.parse(localStorage.getItem(key) || '[]');
  } catch (error) {
    localStorage.removeItem(key);
    return [];
  }
}

function writeList(key, rows) {
  localStorage.setItem(key, JSON.stringify(rows));
}

function recordStep(stepId, result) {
  const rows = readList(MANUAL_RECORD_KEY);
  rows.push({
    stepId,
    result,
    reportIntroduced: 305,
    targetShell: '../ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html',
    recordedAt: new Date().toISOString(),
    boundary: 'manual-recorder-public-local-only'
  });
  writeList(MANUAL_RECORD_KEY, rows);
  renderRecorder();
}

function recordDefectNote() {
  const note = document.getElementById('defectNote')?.value.trim() || '';
  if (!note) {
    renderRecorder('No defect note recorded: note was empty.');
    return;
  }
  const defects = readList(DEFECT_LEDGER_KEY);
  defects.push({
    note,
    reportIntroduced: 305,
    targetShell: '../ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html',
    recordedAt: new Date().toISOString(),
    boundary: 'manual-defect-ledger-public-local-only'
  });
  writeList(DEFECT_LEDGER_KEY, defects);
  document.getElementById('defectNote').value = '';
  renderRecorder();
}

function exportRecorder() {
  const payload = {
    reportIntroduced: 305,
    records: readList(MANUAL_RECORD_KEY),
    defects: readList(DEFECT_LEDGER_KEY),
    boundary: 'primary-demo-recorder-export-public-local-only'
  };
  const text = JSON.stringify(payload, null, 2);
  localStorage.setItem(RECORDER_EXPORT_KEY, text);
  let link = document.getElementById('preparedRecorderExport');
  if (!link) {
    link = document.createElement('a');
    link.id = 'preparedRecorderExport';
    link.textContent = 'Prepared recorder export';
    link.download = 'ssrm_primary_demo_recorder.json';
    link.style.display = 'block';
    link.style.marginTop = '10px';
    document.getElementById('manualRecorder').appendChild(link);
  }
  link.href = URL.createObjectURL(new Blob([text], { type: 'application/json' }));
  renderRecorder('Recorder export prepared.');
}

function clearRecorder() {
  [MANUAL_RECORD_KEY, DEFECT_LEDGER_KEY, RECORDER_EXPORT_KEY].forEach(key => localStorage.removeItem(key));
  const link = document.getElementById('preparedRecorderExport');
  if (link) link.remove();
  renderRecorder('Recorder cleared.');
}

function renderRecorder(message) {
  const records = readList(MANUAL_RECORD_KEY);
  const defects = readList(DEFECT_LEDGER_KEY);
  const passed = records.filter(row => row.result === 'pass').length;
  const failed = records.filter(row => row.result === 'fail').length;
  const status = document.getElementById('recordStatus');
  if (status) status.textContent = message || `${records.length} step records / ${passed} pass / ${failed} fail / ${defects.length} defect notes`;
  const out = document.getElementById('recordLedgerOut');
  if (out) out.textContent = JSON.stringify({ records, defects }, null, 2);
}

document.querySelectorAll('[data-record-step]').forEach(button => {
  button.addEventListener('click', () => recordStep(button.dataset.recordStep, button.dataset.recordResult));
});
document.getElementById('recordDefect')?.addEventListener('click', recordDefectNote);
document.getElementById('exportRecorder')?.addEventListener('click', exportRecorder);
document.getElementById('clearRecorder')?.addEventListener('click', clearRecorder);
renderRecorder();
