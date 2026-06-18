const HANDOFF_KEY = 'ssrm_primary_demo_handoff';
const MANUAL_RECORD_KEY = 'ssrm_primary_demo_manual_pass_records';
const DEFECT_LEDGER_KEY = 'ssrm_primary_demo_defect_ledger';
const RECORDER_EXPORT_KEY = 'ssrm_primary_demo_recorder_export';
const OUTSIDE_REVIEW_KEY = 'ssrm_primary_demo_outside_review_checklist';
const OUTSIDE_REVIEW_EXPORT_KEY = 'ssrm_primary_demo_outside_review_handoff';
const OUTSIDE_REVIEW_ITEMS = [
  { itemId: 'OR-01', label: 'Read boundary before launching' },
  { itemId: 'OR-02', label: 'Launch clean reviewer path' },
  { itemId: 'OR-03', label: 'Run reviewer pass inside the shell' },
  { itemId: 'OR-04', label: 'Inspect transcript, receipt, and observation triage' },
  { itemId: 'OR-05', label: 'Audit failures if the receipt is incomplete' },
  { itemId: 'OR-06', label: 'Reveal deep panels only for unresolved questions' },
  { itemId: 'OR-07', label: 'Record manual outcome and export handoff' }
];

function readObject(key, fallback) {
  try {
    return JSON.parse(localStorage.getItem(key) || JSON.stringify(fallback));
  } catch (error) {
    localStorage.removeItem(key);
    return fallback;
  }
}

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

function outsideReviewState() {
  const state = readObject(OUTSIDE_REVIEW_KEY, { items: {}, updatedAt: null });
  return state && typeof state === 'object' && state.items ? state : { items: {}, updatedAt: null };
}

function writeOutsideReviewState(state) {
  localStorage.setItem(OUTSIDE_REVIEW_KEY, JSON.stringify(state));
}

function renderOutsideReviewChecklist(message) {
  const state = outsideReviewState();
  const doneCount = OUTSIDE_REVIEW_ITEMS.filter(item => state.items[item.itemId] === true).length;
  document.querySelectorAll('[data-outside-review-item]').forEach(button => {
    const itemId = button.dataset.outsideReviewItem;
    const done = state.items[itemId] === true;
    button.textContent = done ? 'Done' : 'Mark done';
    button.closest('[data-outside-review-row]')?.classList.toggle('done', done);
  });
  const status = document.getElementById('outsideReviewStatus');
  if (status) status.textContent = message || `${doneCount}/${OUTSIDE_REVIEW_ITEMS.length} outside-review checklist items complete.`;
  const out = document.getElementById('outsideReviewOut');
  if (out) {
    out.textContent = JSON.stringify({
      reportIntroduced: 323,
      checklist: OUTSIDE_REVIEW_ITEMS,
      state,
      targetShell: '../ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html',
      boundary: 'outside-review-checklist-public-local-only'
    }, null, 2);
  }
}

function markOutsideReviewItem(itemId) {
  const state = outsideReviewState();
  state.items[itemId] = true;
  state.updatedAt = new Date().toISOString();
  writeOutsideReviewState(state);
  renderOutsideReviewChecklist(`${itemId} marked done.`);
}

function exportOutsideReviewHandoff() {
  const payload = {
    reportIntroduced: 323,
    checklistState: outsideReviewState(),
    handoff: readObject(HANDOFF_KEY, null),
    manualRecords: readList(MANUAL_RECORD_KEY),
    defects: readList(DEFECT_LEDGER_KEY),
    recorderExportPrepared: Boolean(localStorage.getItem(RECORDER_EXPORT_KEY)),
    targetShell: '../ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html',
    launchUrl: 'http://127.0.0.1:8765/visualizations/ssrm_3d_browser_world_primary_demo/index.html',
    boundary: 'outside-review-handoff-public-local-only'
  };
  const text = JSON.stringify(payload, null, 2);
  localStorage.setItem(OUTSIDE_REVIEW_EXPORT_KEY, text);
  let link = document.getElementById('preparedOutsideReviewExport');
  if (!link) {
    link = document.createElement('a');
    link.id = 'preparedOutsideReviewExport';
    link.textContent = 'Prepared outside-review handoff';
    link.download = 'ssrm_primary_demo_outside_review_handoff.json';
    link.style.display = 'block';
    link.style.marginTop = '10px';
    document.getElementById('outsideReviewChecklist')?.appendChild(link);
  }
  link.href = URL.createObjectURL(new Blob([text], { type: 'application/json' }));
  renderOutsideReviewChecklist('Outside-review handoff prepared.');
}

function clearOutsideReviewChecklist() {
  localStorage.removeItem(OUTSIDE_REVIEW_KEY);
  localStorage.removeItem(OUTSIDE_REVIEW_EXPORT_KEY);
  const link = document.getElementById('preparedOutsideReviewExport');
  if (link) link.remove();
  renderOutsideReviewChecklist('Outside-review checklist cleared.');
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
  const stepId = document.getElementById('defectStep')?.value || 'unassigned';
  const severity = document.getElementById('defectSeverity')?.value || 'watch';
  if (!note) {
    renderRecorder('No defect note recorded: note was empty.');
    return;
  }
  const defects = readList(DEFECT_LEDGER_KEY);
  defects.push({
    id: `D-${String(defects.length + 1).padStart(3, '0')}`,
    stepId,
    severity,
    status: 'open',
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

function resolveLatestDefect() {
  const defects = readList(DEFECT_LEDGER_KEY);
  const index = defects.map((row, rowIndex) => ({ row, rowIndex })).reverse().find(item => item.row.status !== 'resolved')?.rowIndex;
  if (index === undefined) {
    renderRecorder('No open defect to resolve.');
    return;
  }
  const note = document.getElementById('resolutionNote')?.value.trim() || 'Resolved in primary-demo review.';
  defects[index] = {
    ...defects[index],
    status: 'resolved',
    resolutionNote: note,
    resolvedAt: new Date().toISOString(),
    resolutionReportIntroduced: 307,
    resolutionBoundary: 'manual-defect-resolution-public-local-only'
  };
  writeList(DEFECT_LEDGER_KEY, defects);
  document.getElementById('resolutionNote').value = '';
  renderRecorder('Latest open defect resolved.');
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
  const openDefects = defects.filter(row => row.status !== 'resolved').length;
  const resolvedDefects = defects.filter(row => row.status === 'resolved').length;
  const status = document.getElementById('recordStatus');
  if (status) status.textContent = message || `${records.length} step records / ${passed} pass / ${failed} fail / ${defects.length} defect notes / ${openDefects} open / ${resolvedDefects} resolved`;
  const out = document.getElementById('recordLedgerOut');
  if (out) out.textContent = JSON.stringify({ records, defects }, null, 2);
}

document.querySelectorAll('[data-record-step]').forEach(button => {
  button.addEventListener('click', () => recordStep(button.dataset.recordStep, button.dataset.recordResult));
});
document.getElementById('recordDefect')?.addEventListener('click', recordDefectNote);
document.getElementById('resolveLatestDefect')?.addEventListener('click', resolveLatestDefect);
document.getElementById('exportRecorder')?.addEventListener('click', exportRecorder);
document.getElementById('clearRecorder')?.addEventListener('click', clearRecorder);
document.querySelectorAll('[data-outside-review-item]').forEach(button => {
  button.addEventListener('click', () => markOutsideReviewItem(button.dataset.outsideReviewItem));
});
document.getElementById('exportOutsideReview')?.addEventListener('click', exportOutsideReviewHandoff);
document.getElementById('clearOutsideReview')?.addEventListener('click', clearOutsideReviewChecklist);
renderOutsideReviewChecklist();
renderRecorder();
