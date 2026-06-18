const HANDOFF_KEY = 'ssrm_primary_demo_handoff';
const MANUAL_RECORD_KEY = 'ssrm_primary_demo_manual_pass_records';
const DEFECT_LEDGER_KEY = 'ssrm_primary_demo_defect_ledger';
const RECORDER_EXPORT_KEY = 'ssrm_primary_demo_recorder_export';
const LIFECYCLE_PREFLIGHT_EXPORT_KEY = 'ssrm_primary_demo_lifecycle_preflight_packet';
const OUTSIDE_REVIEW_KEY = 'ssrm_primary_demo_outside_review_checklist';
const OUTSIDE_REVIEW_EXPORT_KEY = 'ssrm_primary_demo_outside_review_handoff';
const SHELL_STATE_KEY = 'ssrm_v61_app_shell_world';
const SHELL_REPLAY_KEY = 'ssrm_v61_app_shell_replay';
const SHELL_EXPORT_KEY = 'ssrm_v61_app_shell_export';
const SHELL_RECEIPT_OBSERVATION_KEY = 'ssrm_v61_app_shell_receipt_observations';
const SHELL_CHECKPOINT_KEY = 'ssrm_v61_app_shell_checkpoints';
const OUTSIDE_REVIEW_ITEMS = [
  { itemId: 'OR-01', label: 'Read boundary before launching' },
  { itemId: 'OR-02', label: 'Launch clean reviewer path' },
  { itemId: 'OR-03', label: 'Run reviewer pass inside the shell' },
  { itemId: 'OR-04', label: 'Inspect transcript, receipt, and observation triage' },
  { itemId: 'OR-05', label: 'Audit failures if the receipt is incomplete' },
  { itemId: 'OR-06', label: 'Reveal deep panels only for unresolved questions' },
  { itemId: 'OR-07', label: 'Record manual outcome and export handoff' }
];

function currentLauncherUrl() {
  return window.location.href.split('#')[0].split('?')[0];
}

function renderCurrentLauncherUrl() {
  const node = document.getElementById('currentLaunchUrl');
  if (node) node.textContent = currentLauncherUrl();
}

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
    launcherUrl: currentLauncherUrl(),
    recordedAt: new Date().toISOString(),
    boundary: 'primary-demo-launcher-only'
  };
  localStorage.setItem(HANDOFF_KEY, JSON.stringify(payload));
  renderHandoff(payload);
}

function renderHandoff(payload) {
  const node = document.getElementById('handoffStatus');
  if (!node) return;
  node.textContent = `Last handoff: ${payload.kind} launch from ${payload.launcherUrl || currentLauncherUrl()} toward ${payload.target} at ${payload.recordedAt}.`;
}

for (const [id, kind] of [['cleanLaunch', 'clean'], ['resumeLaunch', 'resume']]) {
  const node = document.getElementById(id);
  if (node) node.addEventListener('click', () => recordLaunch(kind));
}

renderCurrentLauncherUrl();

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

function readRecorderExportPayload() {
  const text = localStorage.getItem(RECORDER_EXPORT_KEY) || '';
  if (!text) return null;
  try {
    return JSON.parse(text);
  } catch (error) {
    return { parseError: true, rawLength: text.length, boundary: 'primary-demo-recorder-export-public-local-only' };
  }
}

function reviewedHandoffCompletionState() {
  const evidence = buildOutsideReviewEvidence();
  const manualRecords = readList(MANUAL_RECORD_KEY);
  const defects = readList(DEFECT_LEDGER_KEY);
  const recorderExport = readRecorderExportPayload();
  const openDefectCount = defects.filter(row => row.status !== 'resolved').length;
  const missing = [];
  if (!evidence.reviewerPassSeen) missing.push('reviewer pass');
  if (!evidence.receiptAllPass) missing.push('all-pass receipt');
  if (!evidence.replayExportReady) missing.push('replay export');
  if (!recorderExport) missing.push('recorder export');
  if (!manualRecords.length) missing.push('manual recorder outcome');
  if (openDefectCount > 0) missing.push('open defect resolution');
  return {
    reportIntroduced: 327,
    ready: missing.length === 0,
    missing,
    manualRecordCount: manualRecords.length,
    defectCount: defects.length,
    openDefectCount,
    recorderExportPrepared: Boolean(recorderExport),
    recorderExportRecordCount: recorderExport && Array.isArray(recorderExport.records) ? recorderExport.records.length : 0,
    shellEvidence: evidence,
    boundary: 'reviewed-handoff-completion-public-local-only'
  };
}

function completeReviewedHandoff() {
  const completion = reviewedHandoffCompletionState();
  if (!completion.ready) {
    renderOutsideReviewEvidence('Reviewed handoff is not complete yet.');
    renderOutsideReviewChecklist(`Reviewed handoff blocked: missing ${completion.missing.join(', ')}.`);
    return completion;
  }
  const state = outsideReviewState();
  OUTSIDE_REVIEW_ITEMS.forEach(item => { state.items[item.itemId] = true; });
  state.updatedAt = new Date().toISOString();
  state.completedAt = state.updatedAt;
  state.completedBy = 'completeReviewedHandoff';
  state.completion = completion;
  writeOutsideReviewState(state);
  renderOutsideReviewEvidence('Reviewed handoff complete from refreshed shell evidence.');
  renderOutsideReviewChecklist(`${OUTSIDE_REVIEW_ITEMS.length}/${OUTSIDE_REVIEW_ITEMS.length} outside-review checklist items complete after shell evidence and recorder export.`);
  return completion;
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
  const doneCount = OUTSIDE_REVIEW_ITEMS.filter(item => state.items[item.itemId] === true).length;
  renderOutsideReviewChecklist(doneCount === OUTSIDE_REVIEW_ITEMS.length ? `${doneCount}/${OUTSIDE_REVIEW_ITEMS.length} outside-review checklist items complete.` : `${itemId} marked done.`);
}

function exportOutsideReviewHandoff() {
  const lifecyclePreflightPacket = prepareLifecyclePreflightPacket('outside-review-handoff');
  const payload = {
    reportIntroduced: 323,
    combinedReceiptReportIntroduced: 346,
    checklistState: outsideReviewState(),
    handoff: readObject(HANDOFF_KEY, null),
    shellEvidence: buildOutsideReviewEvidence(),
    reviewedHandoffCompletion: reviewedHandoffCompletionState(),
    manualRecords: readList(MANUAL_RECORD_KEY),
    defects: readList(DEFECT_LEDGER_KEY),
    recorderExport: readRecorderExportPayload(),
    recorderExportPrepared: Boolean(localStorage.getItem(RECORDER_EXPORT_KEY)),
    lifecyclePreflightPacket,
    lifecyclePreflightPacketPrepared: Boolean(localStorage.getItem(LIFECYCLE_PREFLIGHT_EXPORT_KEY)),
    lifecyclePreflightPacketSource: LIFECYCLE_PREFLIGHT_EXPORT_KEY,
    combinedReceiptIncludes: ['shellEvidence', 'reviewedHandoffCompletion', 'manualRecords', 'defects', 'recorderExport', 'lifecyclePreflightPacket'],
    targetShell: '../ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html',
    launchUrl: currentLauncherUrl(),
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
  renderOutsideReviewEvidence('Outside-review handoff prepared with shell evidence.');
  renderOutsideReviewHandoffPreview('Outside-review handoff payload visible below.');
  renderOutsideReviewChecklist('Outside-review handoff prepared.');
}

function clearOutsideReviewChecklist() {
  localStorage.removeItem(OUTSIDE_REVIEW_KEY);
  localStorage.removeItem(OUTSIDE_REVIEW_EXPORT_KEY);
  const link = document.getElementById('preparedOutsideReviewExport');
  if (link) link.remove();
  renderOutsideReviewHandoffPreview('Outside-review handoff cleared.');
  renderOutsideReviewChecklist('Outside-review checklist cleared.');
}

function shellReplayRows() {
  const world = readObject(SHELL_STATE_KEY, {});
  if (Array.isArray(world.replay)) return world.replay;
  const replay = readObject(SHELL_REPLAY_KEY, []);
  return Array.isArray(replay) ? replay : [];
}

function buildOutsideReviewEvidence() {
  const replay = shellReplayRows();
  const events = replay.map(row => row.event);
  const receiptEvents = replay.filter(row => row.event === 'generateScenarioReceipt');
  const latestReceipt = receiptEvents[receiptEvents.length - 1]?.payload || {};
  const passCount = Number(latestReceipt.passCount || 0);
  const fieldCount = Number(latestReceipt.fieldCount || 0);
  const observations = readObject(SHELL_RECEIPT_OBSERVATION_KEY, []);
  const checkpoints = readObject(SHELL_CHECKPOINT_KEY, []);
  const exportText = localStorage.getItem(SHELL_EXPORT_KEY) || '';
  return {
    reportIntroduced: 324,
    handoff: readObject(HANDOFF_KEY, null),
    replayRows: replay.length,
    reviewerPassSeen: events.includes('runReviewerLandingPass'),
    receiptAllPass: fieldCount > 0 && passCount === fieldCount,
    receipt: { passCount, fieldCount },
    observationRows: Array.isArray(observations) ? observations.length : 0,
    blockingObservationRows: Array.isArray(observations) ? observations.filter(row => row.severity === 'blocking' && row.status !== 'resolved').length : 0,
    checkpointRows: Array.isArray(checkpoints) ? checkpoints.length : 0,
    replayExportReady: exportText.length > 0 || events.includes('exportReplay'),
    deepPanelsRevealed: events.includes('toggleDeepPanels'),
    targetShell: '../ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html',
    boundary: 'outside-review-shell-evidence-public-local-only'
  };
}

function renderOutsideReviewEvidence(message) {
  const evidence = buildOutsideReviewEvidence();
  const status = document.getElementById('outsideReviewEvidenceStatus');
  if (status) {
    const receipt = evidence.receipt.fieldCount ? `${evidence.receipt.passCount}/${evidence.receipt.fieldCount}` : 'missing';
    status.textContent = message || `Shell evidence: replay ${evidence.replayRows} rows / reviewer pass ${evidence.reviewerPassSeen ? 'seen' : 'missing'} / receipt ${receipt} / observations ${evidence.observationRows} / export ${evidence.replayExportReady ? 'ready' : 'missing'}.`;
  }
  const out = document.getElementById('outsideReviewEvidenceOut');
  if (out) out.textContent = JSON.stringify(evidence, null, 2);
  if (readOutsideReviewHandoffPayload()) renderOutsideReviewHandoffPreview();
  return evidence;
}

function readOutsideReviewHandoffPayload() {
  const text = localStorage.getItem(OUTSIDE_REVIEW_EXPORT_KEY) || '';
  if (!text) return null;
  try {
    return JSON.parse(text);
  } catch (error) {
    return { parseError: true, raw: text, boundary: 'outside-review-handoff-preview-public-local-only' };
  }
}

function handoffPayloadFreshnessState(payload) {
  if (!payload) {
    return { fresh: false, mismatches: ['missing payload'], boundary: 'outside-review-handoff-freshness-public-local-only' };
  }
  const currentEvidence = buildOutsideReviewEvidence();
  const currentCompletion = reviewedHandoffCompletionState();
  const payloadHandoff = payload.handoff || {};
  const currentHandoff = currentEvidence.handoff || {};
  const mismatches = [];
  if ((payloadHandoff.recordedAt || null) !== (currentHandoff.recordedAt || null)) mismatches.push('launch handoff changed');
  if ((payloadHandoff.kind || null) !== (currentHandoff.kind || null)) mismatches.push('launch kind changed');
  if ((payload.shellEvidence || {}).replayRows !== currentEvidence.replayRows) mismatches.push('shell replay rows changed');
  if (((payload.reviewedHandoffCompletion || {}).manualRecordCount || 0) !== currentCompletion.manualRecordCount) mismatches.push('manual recorder count changed');
  if (((payload.reviewedHandoffCompletion || {}).openDefectCount || 0) !== currentCompletion.openDefectCount) mismatches.push('open defect count changed');
  return {
    fresh: mismatches.length === 0,
    mismatches,
    payloadHandoffKind: payloadHandoff.kind || null,
    currentHandoffKind: currentHandoff.kind || null,
    payloadHandoffRecordedAt: payloadHandoff.recordedAt || null,
    currentHandoffRecordedAt: currentHandoff.recordedAt || null,
    payloadReplayRows: (payload.shellEvidence || {}).replayRows || 0,
    currentReplayRows: currentEvidence.replayRows,
    payloadManualRecordCount: (payload.reviewedHandoffCompletion || {}).manualRecordCount || 0,
    currentManualRecordCount: currentCompletion.manualRecordCount,
    boundary: 'outside-review-handoff-freshness-public-local-only'
  };
}

function readableHandoffSummary(payload, freshness) {
  if (!payload) return 'No outside-review handoff export prepared yet.';
  const checklistItems = ((payload.checklistState || {}).items) || {};
  const checklistDone = Object.values(checklistItems).filter(Boolean).length;
  const shellEvidence = payload.shellEvidence || {};
  const completion = payload.reviewedHandoffCompletion || {};
  const recorderExport = payload.recorderExport || {};
  const handoff = payload.handoff || {};
  const receipt = shellEvidence.receipt || {};
  const receiptText = receipt.fieldCount ? `${receipt.passCount}/${receipt.fieldCount}` : 'missing';
  const recorderReady = payload.recorderExportPrepared || Boolean(recorderExport.recordCount) ? 'ready' : 'missing';
  const manualCount = Array.isArray(payload.manualRecords) ? payload.manualRecords.length : (completion.manualRecordCount || 0);
  const freshnessText = freshness && freshness.fresh ? 'fresh' : `stale: ${(freshness && freshness.mismatches || ['unknown mismatch']).join(', ')}`;
  const preflightPacket = payload.lifecyclePreflightPacket || {};
  const preflightPhaseCount = preflightPacket.phaseCount || Object.keys(preflightPacket.phaseStatuses || {}).length;
  const preflightText = payload.lifecyclePreflightPacketPrepared ? `lifecycle preflight blocking phase ${preflightPacket.blockingPhase || 'unknown'} / ${preflightPhaseCount} phase(s)` : 'lifecycle preflight missing';
  return `Outside-review handoff ready: ${freshnessText} ${handoff.kind || 'unknown'} handoff; checklist ${checklistDone}/${OUTSIDE_REVIEW_ITEMS.length}; shell evidence reviewer pass ${shellEvidence.reviewerPassSeen ? 'seen' : 'missing'} / receipt ${receiptText} / replay export ${shellEvidence.replayExportReady ? 'ready' : 'missing'}; recorder ${manualCount} manual record(s) / export ${recorderReady}; ${preflightText}; next action: click Continue from prepared ${handoff.kind || 'unknown'} handoff, or download combined outside-review handoff JSON.`;
}

function preparedHandoffHref(payload) {
  const handoff = (payload && payload.handoff) || {};
  const target = handoff.target || '../ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html';
  const separator = target.includes('?') ? '&' : '?';
  const params = handoff.kind === 'clean' ? 'reset=1&source=primary-demo-v63' : 'source=primary-demo-v63';
  return `${target}${separator}${params}`;
}

function renderOutsideReviewHandoffActions(payload, freshness) {
  const actions = document.getElementById('outsideReviewHandoffActions');
  if (!actions) return;
  actions.textContent = '';
  if (!payload) return;
  const kind = (payload.handoff || {}).kind || 'unknown';
  if (freshness && freshness.fresh) {
    const continueLink = document.createElement('a');
    continueLink.id = 'continuePreparedHandoff';
    continueLink.className = 'button primary';
    continueLink.href = preparedHandoffHref(payload);
    continueLink.textContent = `Continue from prepared ${kind} handoff`;
    actions.appendChild(continueLink);
  } else {
    const staleNote = document.createElement('span');
    staleNote.className = 'status-line';
    staleNote.textContent = 'Re-prepare before continuing from this handoff.';
    actions.appendChild(staleNote);
  }
  const existingDownload = document.getElementById('preparedOutsideReviewExport');
  if (existingDownload) existingDownload.remove();
  const download = document.createElement('a');
  download.id = 'preparedOutsideReviewExport';
  download.className = 'button';
  download.download = 'ssrm_primary_demo_outside_review_handoff.json';
  download.textContent = 'Download prepared outside-review handoff JSON';
  const text = localStorage.getItem(OUTSIDE_REVIEW_EXPORT_KEY) || JSON.stringify(payload, null, 2);
  download.href = URL.createObjectURL(new Blob([text], { type: 'application/json' }));
  actions.appendChild(download);
}

function renderOutsideReviewHandoffPreview(message) {
  const payload = readOutsideReviewHandoffPayload();
  const freshness = payload ? handoffPayloadFreshnessState(payload) : null;
  const status = document.getElementById('outsideReviewHandoffStatus');
  if (status) {
    if (payload && freshness && !freshness.fresh) {
      status.textContent = `Prepared handoff payload is stale: ${freshness.mismatches.join(', ')}. Payload is ${freshness.payloadHandoffKind || 'unknown'} while current shell is ${freshness.currentHandoffKind || 'unknown'}. Re-run Prepare outside-review handoff.`;
    } else {
      status.textContent = payload ? readableHandoffSummary(payload, freshness) : (message || 'No outside-review handoff export prepared yet.');
    }
  }
  const out = document.getElementById('outsideReviewHandoffOut');
  if (out) {
    out.textContent = payload ? JSON.stringify({ ...payload, previewFreshness: freshness, previewReadableSummary: readableHandoffSummary(payload, freshness) }, null, 2) : 'No outside-review handoff export prepared yet.';
  }
  renderOutsideReviewHandoffActions(payload, freshness);
  return payload;
}

function lifecyclePreflightPhaseStatuses() {
  const rows = Array.from(document.querySelectorAll('[data-lifecycle-preflight-phase]'));
  return rows.reduce((accumulator, row) => {
    accumulator[row.dataset.lifecyclePreflightPhase] = row.dataset.lifecyclePreflightStatus || 'unknown';
    return accumulator;
  }, {});
}

function readLifecyclePreflightPacket() {
  const text = localStorage.getItem(LIFECYCLE_PREFLIGHT_EXPORT_KEY) || '';
  if (!text) return null;
  try {
    return JSON.parse(text);
  } catch (error) {
    return { parseError: true, raw: text, boundary: 'lifecycle-preflight-packet-preview-public-local-only' };
  }
}

function buildLifecyclePreflightPacket(action = 'prepare') {
  const sourceNode = document.getElementById('lifecycleSmokePreflight');
  const phaseStatuses = lifecyclePreflightPhaseStatuses();
  return {
    reportIntroduced: 345,
    action,
    command: document.getElementById('lifecycleSmokeRunnerCommand')?.textContent || '',
    policy: document.getElementById('lifecycleSmokeRunnerPolicy')?.textContent || '',
    freshness: (document.getElementById('lifecycleSmokeFreshness')?.textContent || '').replace('Runner freshness: ', ''),
    blockingPhase: sourceNode?.dataset.lifecyclePreflightBlockingPhase || 'unknown',
    phaseStatuses,
    phaseCount: Object.keys(phaseStatuses).length,
    sources: {
      sourceMarker: sourceNode?.dataset.lifecyclePreflightSource || 'unknown',
      report: document.getElementById('lifecycleSmokeRunnerReport')?.getAttribute('href') || '',
      results: document.getElementById('lifecycleSmokeRunnerResults')?.getAttribute('href') || '',
      manifest: document.getElementById('lifecycleSmokeRunnerManifest')?.getAttribute('href') || ''
    },
    preparedAt: new Date().toISOString(),
    boundary: 'lifecycle-preflight-packet-browser-local-artifact-status-only'
  };
}

function renderLifecyclePreflightPacket(message) {
  const packet = readLifecyclePreflightPacket();
  const status = document.getElementById('lifecyclePreflightExportStatus');
  if (status) status.textContent = message || (packet ? `Lifecycle preflight packet prepared at ${packet.preparedAt}; blocking phase ${packet.blockingPhase}.` : 'No lifecycle preflight packet prepared yet.');
  const out = document.getElementById('lifecyclePreflightPacketOut');
  if (out) out.textContent = packet ? JSON.stringify(packet, null, 2) : 'No lifecycle preflight packet prepared yet.';
  return packet;
}

function prepareLifecyclePreflightPacket(action = 'prepare') {
  const packet = buildLifecyclePreflightPacket(action);
  const text = JSON.stringify(packet, null, 2);
  localStorage.setItem(LIFECYCLE_PREFLIGHT_EXPORT_KEY, text);
  let link = document.getElementById('preparedLifecyclePreflightPacket');
  if (!link) {
    link = document.createElement('a');
    link.id = 'preparedLifecyclePreflightPacket';
    link.className = 'button';
    link.download = 'ssrm_primary_demo_lifecycle_preflight_packet.json';
    link.textContent = 'Download lifecycle preflight packet JSON';
    document.getElementById('lifecyclePreflightPacketActions')?.appendChild(link);
  }
  link.href = URL.createObjectURL(new Blob([text], { type: 'application/json' }));
  renderLifecyclePreflightPacket(`Lifecycle preflight packet prepared; blocking phase ${packet.blockingPhase}.`);
  return packet;
}

async function copyLifecyclePreflightPacket() {
  const packet = prepareLifecyclePreflightPacket('copy');
  const text = JSON.stringify(packet, null, 2);
  if (navigator.clipboard && navigator.clipboard.writeText) {
    try {
      await navigator.clipboard.writeText(text);
      renderLifecyclePreflightPacket(`Lifecycle preflight packet copied; blocking phase ${packet.blockingPhase}.`);
      return packet;
    } catch (error) {
      renderLifecyclePreflightPacket(`Clipboard copy blocked; download link prepared instead. Blocking phase ${packet.blockingPhase}.`);
      return packet;
    }
  }
  renderLifecyclePreflightPacket(`Clipboard unavailable; download link prepared instead. Blocking phase ${packet.blockingPhase}.`);
  return packet;
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
  const records = readList(MANUAL_RECORD_KEY);
  const defects = readList(DEFECT_LEDGER_KEY);
  const payload = {
    reportIntroduced: 305,
    records,
    defects,
    recordCount: records.length,
    defectCount: defects.length,
    openDefectCount: defects.filter(row => row.status !== 'resolved').length,
    preparedAt: new Date().toISOString(),
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
  if (out) out.textContent = JSON.stringify({ records, defects, recorderExport: readRecorderExportPayload() }, null, 2);
}

document.querySelectorAll('[data-record-step]').forEach(button => {
  button.addEventListener('click', () => recordStep(button.dataset.recordStep, button.dataset.recordResult));
});
document.getElementById('recordDefect')?.addEventListener('click', recordDefectNote);
document.getElementById('resolveLatestDefect')?.addEventListener('click', resolveLatestDefect);
document.getElementById('exportRecorder')?.addEventListener('click', exportRecorder);
document.getElementById('prepareLifecyclePreflightPacket')?.addEventListener('click', () => prepareLifecyclePreflightPacket());
document.getElementById('copyLifecyclePreflightPacket')?.addEventListener('click', () => { copyLifecyclePreflightPacket(); });
document.getElementById('clearRecorder')?.addEventListener('click', clearRecorder);
document.querySelectorAll('[data-outside-review-item]').forEach(button => {
  button.addEventListener('click', () => markOutsideReviewItem(button.dataset.outsideReviewItem));
});
document.getElementById('refreshOutsideReviewEvidence')?.addEventListener('click', () => renderOutsideReviewEvidence());
document.getElementById('completeReviewedHandoff')?.addEventListener('click', completeReviewedHandoff);
document.getElementById('exportOutsideReview')?.addEventListener('click', exportOutsideReviewHandoff);
document.getElementById('clearOutsideReview')?.addEventListener('click', clearOutsideReviewChecklist);
renderOutsideReviewChecklist();
renderOutsideReviewEvidence();
renderOutsideReviewHandoffPreview();
renderLifecyclePreflightPacket();
renderRecorder();
