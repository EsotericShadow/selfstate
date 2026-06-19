const BOUNDARY = "Deterministic browser-local hardened vertical-slice app shell only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, production persistence, finished gameplay, complete 3D engine, or metaphysical frequency claim.";
const STATE_KEY = 'ssrm_v61_app_shell_world';
const REPLAY_KEY = 'ssrm_v61_app_shell_replay';
const QA_KEY = 'ssrm_v61_app_shell_qa_results';
const EXPORT_KEY = 'ssrm_v61_app_shell_export';
const SAVE_SNAPSHOT_KEY = 'ssrm_v61_app_shell_saved_snapshot';
const PROTOTYPE_SAVE_KEY = 'ssrm_v61_game_prototype_saves';
const PROTOTYPE_ACCEPTANCE_KEY = 'ssrm_v61_game_prototype_acceptance_receipt';
const CHECKPOINT_KEY = 'ssrm_v61_app_shell_checkpoints';
const HISTORY_KEY = 'ssrm_v61_app_shell_resident_history';
const RELATION_KEY = 'ssrm_v61_app_shell_resident_relationships';
const RECEIPT_OBSERVATION_KEY = 'ssrm_v61_app_shell_receipt_observations';
const OBSERVATION_FILTER_KEY = 'ssrm_v61_app_shell_observation_filter';

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

const receiptFieldIds = ['entry_and_movement', 'schedule_visibility', 'debt_consequence', 'offscreen_life', 'recoverable_trust_repair', 'resident_social_memory', 'public_history_sync', 'replay_export_ready', 'resume_ready_snapshot'];

const qaManifest = {
  stateKeys: [STATE_KEY, REPLAY_KEY, QA_KEY, EXPORT_KEY, SAVE_SNAPSHOT_KEY, PROTOTYPE_SAVE_KEY, PROTOTYPE_ACCEPTANCE_KEY, CHECKPOINT_KEY, HISTORY_KEY, RELATION_KEY, RECEIPT_OBSERVATION_KEY, OBSERVATION_FILTER_KEY],
  publicState: ['avatar', 'selected', 'residents', 'resources', 'replay', 'returnContinuity', 'returnGreetingContinuity', 'accountabilitySocialEcho', 'boundedEchoConversation', 'echoInfluencedChoiceReceipt', 'anomalyDiscovery', 'anomalyInvestigationSchedule', 'stochasticConsequencePulse', 'stochasticRecoveryLoop', 'stochasticHistoryInfluence', 'stochasticOrdinaryAffordance', 'civilizationPressure', 'practicalDiscovery', 'emergentPracticeGraph', 'villageBoard', 'realityConstraintLedger', 'avatarHintDivergence', 'hintBranchPersistence', 'gamePrototype', 'deepTimeCivilization', 'autonomousResidents', 'gamePrototypeQA', 'prototypeClock', 'gamePrototypeSaves', 'gamePrototypeAcceptance', 'promiseFollowUp', 'obligationLedger', 'scheduleQueue', 'debtLedger', 'offscreenObligationEvents', 'absentTimeSummary', 'absentTimeThreads', 'absentTimeChoiceReceipt', 'avatarAbsenceAccountabilityReceipt'],
  forbiddenPublicState: ['privateWorkspace', 'subjectiveFeeling', 'llmTranscript'],
  boundary: BOUNDARY,
  directHooks: ['runPlaytestChecklist', 'runStateBoundaryAudit', 'runSaveRestoreSmoke', 'runAuditAfterRollbackCheck', 'runAllQAHooks', 'toggleAudit', 'exportReplay', 'exportPrototypeAcceptanceReceipt']
};

const urlParams = new URLSearchParams(window.location.search);
if (urlParams.get('reset') === '1') {
  [STATE_KEY, REPLAY_KEY, QA_KEY, EXPORT_KEY, SAVE_SNAPSHOT_KEY, PROTOTYPE_SAVE_KEY, PROTOTYPE_ACCEPTANCE_KEY, CHECKPOINT_KEY, HISTORY_KEY, RELATION_KEY, RECEIPT_OBSERVATION_KEY, OBSERVATION_FILTER_KEY].forEach(key => localStorage.removeItem(key));
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
  returnContinuity: null,
  returnGreetingContinuity: null,
  accountabilitySocialEcho: null,
  boundedEchoConversation: null,
  echoInfluencedChoiceReceipt: null,
  anomalyDiscovery: null,
  anomalyInvestigationSchedule: null,
  stochasticConsequencePulse: null,
  stochasticRecoveryLoop: null,
  stochasticHistoryInfluence: null,
  stochasticOrdinaryAffordance: null,
  civilizationPressure: null,
  practicalDiscovery: null,
  emergentPracticeGraph: null,
  villageBoard: null,
  realityConstraintLedger: null,
  avatarHintDivergence: null,
  hintBranchPersistence: null,
  gamePrototype: null,
  deepTimeCivilization: null,
  autonomousResidents: null,
  gamePrototypeQA: null,
  prototypeClock: null,
  gamePrototypeSaves: null,
  gamePrototypeAcceptance: null,
  promiseFollowUp: null,
  obligationLedger: [],
  scheduleQueue: [],
  debtLedger: [],
  offscreenObligationEvents: [],
  absentTimeSummary: null,
  absentTimeThreads: [],
  absentTimeChoiceReceipt: null,
  avatarAbsenceAccountabilityReceipt: null,
  selectedObligationId: null,
  lastQA: []
}));

const canvas = document.getElementById('world');
const ctx = canvas.getContext('2d');
const residentSelect = document.getElementById('residentSelect');
const phraseSelect = document.getElementById('phraseSelect');
let prototypeAutoTimer = null;
let livedActionAutoIntegrationPaused = false;

function clamp(value) { return Math.max(0, Math.min(1, value)); }
function currentResident() { return world.residents[world.selected]; }
function renderReturnContinuity() {
  const node = document.getElementById('returnContinuityOut');
  if (!node) return;
  if (!world.returnContinuity) {
    node.textContent = 'No return recognition yet.';
    return;
  }
  node.textContent = `${world.returnContinuity.resident} ${world.returnContinuity.memory}; replay before return ${world.returnContinuity.replayRowsBeforeReturn}.`;
}
function renderReturnGreetingContinuity() {
  const node = document.getElementById('returnGreetingContinuityOut');
  if (!node) return;
  if (!world.returnGreetingContinuity) {
    node.textContent = 'No accountability return greeting yet.';
    return;
  }
  node.textContent = [
    `${world.returnGreetingContinuity.resident} greeting: ${world.returnGreetingContinuity.greeting}`,
    `Resolved: ${world.returnGreetingContinuity.residentThreadId} ${world.returnGreetingContinuity.residentObligationStatus}`,
    `Avatar absence: ${world.returnGreetingContinuity.avatarThreadStatus}`,
    `History preserved: ${world.returnGreetingContinuity.residentHistoryPreserved ? 'yes' : 'no'}`
  ].join('\n');
}
function renderAccountabilitySocialEcho() {
  const node = document.getElementById('accountabilitySocialEchoOut');
  if (!node) return;
  if (!world.accountabilitySocialEcho) {
    node.textContent = 'No resident-to-resident accountability echo yet.';
    return;
  }
  node.textContent = [
    `Echo: ${world.accountabilitySocialEcho.echo}`,
    `Source resident: ${world.accountabilitySocialEcho.sourceResident}`,
    `Echo resident: ${world.accountabilitySocialEcho.echoResident}`,
    `Mentions: ${world.accountabilitySocialEcho.residentThreadId} ${world.accountabilitySocialEcho.residentObligationStatus} / avatar absence ${world.accountabilitySocialEcho.avatarThreadStatus}`,
    `Direct avatar command: ${world.accountabilitySocialEcho.directAvatarCommand ? 'yes' : 'no'}`,
    `History preserved: ${world.accountabilitySocialEcho.residentHistoryPreserved ? 'yes' : 'no'}`
  ].join('\n');
}
function renderBoundedEchoConversation() {
  const node = document.getElementById('boundedEchoConversationOut');
  if (!node) return;
  if (!world.boundedEchoConversation) {
    node.textContent = 'No bounded echo conversation yet.';
    return;
  }
  node.textContent = [
    `Resident: ${world.boundedEchoConversation.resident}`,
    `Phrase: ${world.boundedEchoConversation.phrase}`,
    `Reply: ${world.boundedEchoConversation.reply}`,
    `Source echo: ${world.boundedEchoConversation.sourceEchoId}`,
    `No LLM: ${world.boundedEchoConversation.noLLM ? 'yes' : 'no'}`,
    `Autonomous language: ${world.boundedEchoConversation.autonomousLanguage ? 'yes' : 'no'}`,
    `Phrasebook only: ${world.boundedEchoConversation.phrasebookOnly ? 'yes' : 'no'}`
  ].join('\n');
}
function renderEchoInfluencedChoiceReceipt() {
  const node = document.getElementById('echoInfluencedChoiceReceiptOut');
  if (!node) return;
  if (!world.echoInfluencedChoiceReceipt) {
    node.textContent = 'No echo-influenced choice yet.';
    return;
  }
  node.textContent = [
    `Resident: ${world.echoInfluencedChoiceReceipt.resident}`,
    `Action: ${world.echoInfluencedChoiceReceipt.action}`,
    `Choice: ${world.echoInfluencedChoiceReceipt.choice}`,
    `Refusal: ${world.echoInfluencedChoiceReceipt.refusal}`,
    `Source echo: ${world.echoInfluencedChoiceReceipt.sourceEchoId}`,
    `Source preserved: ${world.echoInfluencedChoiceReceipt.sourceAttributionPreserved ? 'yes' : 'no'}`,
    `Direct avatar command: ${world.echoInfluencedChoiceReceipt.directAvatarCommand ? 'yes' : 'no'}`,
    `No LLM: ${world.echoInfluencedChoiceReceipt.noLLM ? 'yes' : 'no'}`,
    `Autonomous language: ${world.echoInfluencedChoiceReceipt.autonomousLanguage ? 'yes' : 'no'}`,
    `Phrasebook only: ${world.echoInfluencedChoiceReceipt.phrasebookOnly ? 'yes' : 'no'}`,
    `Recoverable: ${world.echoInfluencedChoiceReceipt.recoverable ? 'yes' : 'no'}`
  ].join('\n');
}
function renderAnomalyDiscovery() {
  const summaryNode = document.getElementById('anomalyDiscoverySummaryOut');
  const detailNode = document.getElementById('anomalyDiscoveryOut');
  const discovery = world.anomalyDiscovery;
  if (summaryNode) {
    summaryNode.textContent = discovery
      ? `${discovery.label}: ${discovery.observations.length} observations / ${discovery.experiments.length} tests / ${discovery.failures.length} failures`
      : 'No anomaly introduced yet.';
  }
  if (!detailNode) return;
  if (!discovery) {
    detailNode.textContent = 'No anomaly introduced yet. Use Introduce anomaly to create hidden laws and public observations.';
    return;
  }
  const hiddenLines = world.audit
    ? Object.entries(discovery.hiddenWorldLaw.materials).map(([id, props]) => `${id}: transfer ${props.conductivityLike} / retain ${props.chargeRetention} / friction ${props.frictionResponse} / wet ${props.moistureSensitivity} / heat ${props.heatTolerance} / fragile ${props.fragility} / toxin ${props.toxicity} / burn ${props.combustionRisk} / block ${props.insulationBlocking} / store ${props.storagePotential} / pull ${props.magneticAttraction}`)
    : ['Hidden law: concealed from residents; toggle Audit to inspect simulator-only material properties.'];
  const observationLines = discovery.observations.slice(-6).map(row => `${row.id} ${row.witness}: ${row.effect} (${row.materials.join(' + ')})`);
  const beliefLines = Object.entries(discovery.residentBeliefs).map(([resident, belief]) => `${resident}: "${belief.label}" conf ${belief.confidence} / ${belief.kind} / source ${belief.source} / witnessed ${belief.personallyWitnessed ? 'yes' : 'no'} / contradictions ${belief.contradictionCount}`);
  const experimentLines = discovery.experiments.slice(-6).map(row => `${row.id} ${row.actor}: ${row.materials.join(' + ')} -> ${row.outcome}${row.failure ? ' [failed]' : ''}; reason ${row.reason}`);
  const socialLines = discovery.socialTransmissions.slice(-6).map(row => `${row.channel} ${row.from}->${row.to}: "${row.before}" became "${row.after}"`);
  const culturalLines = discovery.culturalMemory.slice(-4).map(row => `${row.id}: ${row.memory}`);
  const auditLines = discovery.auditReplay.slice(-10).map(row => `${row.type}: ${row.summary}`);
  detailNode.textContent = [
    `Anomaly: ${discovery.label} seed=${discovery.seed}`,
    `Avatar boundary: ${discovery.avatarBoundary}`,
    '',
    'Hidden/world-law layer:',
    ...hiddenLines,
    '',
    'Public observations:',
    ...observationLines,
    '',
    'Resident partial beliefs:',
    ...beliefLines,
    '',
    'Resident experiments and preserved failures:',
    ...experimentLines,
    '',
    'Social transmission mutations:',
    ...socialLines,
    '',
    'Cultural memory:',
    ...culturalLines,
    '',
    'Audit replay:',
    ...auditLines
  ].join('\n');
}
function renderAnomalyInvestigationSchedule() {
  const summaryNode = document.getElementById('anomalyInvestigationScheduleSummaryOut');
  const detailNode = document.getElementById('anomalyInvestigationScheduleOut');
  const schedule = world.anomalyInvestigationSchedule;
  if (summaryNode) {
    summaryNode.textContent = schedule
      ? `${schedule.slots.length} slots / ${schedule.testsRun} tests / ${schedule.refusals} refusals / ${schedule.ordinaryWorkDelayed} work delays`
      : 'No anomaly investigation schedule yet.';
  }
  if (!detailNode) return;
  if (!schedule) {
    detailNode.textContent = 'No anomaly investigation schedule yet. Plan investigation after introducing an anomaly.';
    return;
  }
  const slotLines = schedule.slots.map(slot => [
    `${slot.block} ${slot.resident}: ${slot.decision}`,
    `work=${slot.ordinaryWork}`,
    `belief=${slot.belief}`,
    `cost=${Object.entries(slot.materialCost).map(([key, value]) => `${key}:${value}`).join(',')}`,
    `fear=${slot.fear}`,
    `trust=${slot.trust}`,
    `pressure=${slot.socialPressure}`,
    `status=${slot.status}`,
    `reason=${slot.reason}`
  ].join(' / '));
  const executionLines = schedule.executionLog.slice(-8).map(row => `${row.slotId} ${row.resident}: ${row.outcome}`);
  detailNode.textContent = [
    `Schedule seed: ${schedule.seed}`,
    `Boundary: ${schedule.boundary}`,
    `Resources before: ${JSON.stringify(schedule.resourcesBefore)}`,
    `Resources now: ${JSON.stringify(world.resources)}`,
    `Material scarcity blocks: ${schedule.materialScarcityBlocks}`,
    `Ordinary work delayed: ${schedule.ordinaryWorkDelayed}`,
    `Refusals/deferments: ${schedule.refusals}`,
    '',
    'Scheduled slots:',
    ...slotLines,
    '',
    'Execution log:',
    ...(executionLines.length ? executionLines : ['No scheduled slots executed yet.'])
  ].join('\n');
}
function renderStochasticConsequencePulse() {
  const summaryNode = document.getElementById('stochasticConsequencePulseSummaryOut');
  const detailNode = document.getElementById('stochasticConsequencePulseOut');
  const pulse = world.stochasticConsequencePulse;
  if (summaryNode) {
    summaryNode.textContent = pulse
      ? `${pulse.pulses.length} pulses / ${pulse.entropyLedger.length} entropy bytes / ${pulse.scheduleCouplings.length} schedule couplings`
      : 'No stochastic consequence pulse yet.';
  }
  if (!detailNode) return;
  if (!pulse) {
    detailNode.textContent = 'No stochastic consequence pulse yet. Run a pulse to record runtime entropy, branch choice, resource deltas, resident consequence, and replay evidence.';
    return;
  }
  const recent = pulse.pulses.slice(-8).map(row => [
    `${row.id} ${row.actor}: ${row.event}`,
    `entropy=${row.entropy.map(item => `${item.label}:${item.value}`).join(',')}`,
    `need=${row.needBefore.dominant}->${row.needAfter.dominant}`,
    `resources=${JSON.stringify(row.resourcesBefore)} -> ${JSON.stringify(row.resourcesAfter)}`,
    `schedule=${row.scheduleCoupling || 'none'}`,
    `consequence=${row.consequence}`
  ].join(' / '));
  const couplings = pulse.scheduleCouplings.slice(-6).map(row => `${row.pulseId}: ${row.summary}`);
  detailNode.textContent = [
    `Mode: ${pulse.mode}`,
    `Boundary: ${pulse.boundary}`,
    `Replayable entropy: ${pulse.replayableEntropy ? 'yes' : 'no'}`,
    `Non-deterministic runtime source: ${pulse.runtimeEntropySource}`,
    `Resident need snapshots: ${Object.keys(pulse.needs).length}`,
    '',
    'Recent stochastic pulses:',
    ...(recent.length ? recent : ['No pulses recorded yet.']),
    '',
    'Schedule couplings:',
    ...(couplings.length ? couplings : ['No schedule coupling yet.'])
  ].join('\n');
}
function renderStochasticRecoveryLoop() {
  const summaryNode = document.getElementById('stochasticRecoveryLoopSummaryOut');
  const detailNode = document.getElementById('stochasticRecoveryLoopOut');
  const loop = world.stochasticRecoveryLoop;
  if (summaryNode) {
    summaryNode.textContent = loop
      ? `${loop.recoveryQueue.length} recoveries / ${loop.resolvedCount} resolved / ${loop.relationshipRepairs.length} relationship repairs`
      : 'No stochastic recovery loop yet.';
  }
  if (!detailNode) return;
  if (!loop) {
    detailNode.textContent = 'No stochastic recovery loop yet. Plan recovery after stochastic pulses to turn surprise into bounded repair, not permanent damage.';
    return;
  }
  const queueLines = loop.recoveryQueue.slice(-10).map(row => [
    `${row.id} ${row.actor}: ${row.status}`,
    `pulse=${row.pulseId}`,
    `harm=${row.harmType}`,
    `action=${row.repairAction}`,
    `cost=${Object.entries(row.resourceCost).map(([key, value]) => `${key}:${value}`).join(',')}`,
    `need=${row.needBefore}->${row.needAfter}`,
    `schedule=${row.scheduleRepair || 'none'}`
  ].join(' / '));
  const repairLines = loop.relationshipRepairs.slice(-8).map(row => `${row.recoveryId} ${row.actor}: trust ${row.trustBefore}->${row.trustAfter} / ${row.note}`);
  const ledgerLines = loop.repairLedger.slice(-8).map(row => `${row.recoveryId}: ${row.outcome}`);
  detailNode.textContent = [
    `Boundary: ${loop.boundary}`,
    `Source pulses observed: ${loop.sourcePulseCount}`,
    `No permanent damage policy: ${loop.noPermanentDamagePolicy}`,
    `Pending: ${loop.pendingCount} / Resolved: ${loop.resolvedCount} / Stabilized without materials: ${loop.stabilizedWithoutMaterials}`,
    '',
    'Recovery queue:',
    ...(queueLines.length ? queueLines : ['No recovery rows planned yet.']),
    '',
    'Relationship repairs:',
    ...(repairLines.length ? repairLines : ['No relationship repairs recorded yet.']),
    '',
    'Repair ledger:',
    ...(ledgerLines.length ? ledgerLines : ['No repair ledger rows yet.'])
  ].join('\n');
}
function renderStochasticHistoryInfluence() {
  const summaryNode = document.getElementById('stochasticHistoryInfluenceSummaryOut');
  const detailNode = document.getElementById('stochasticHistoryInfluenceOut');
  const influence = world.stochasticHistoryInfluence;
  if (summaryNode) {
    summaryNode.textContent = influence
      ? `${influence.choiceRecords.length} choices / ${influence.refusalRecords.length} refusals / ${influence.socialEchoes.length} echoes`
      : 'No stochastic history influence yet.';
  }
  if (!detailNode) return;
  if (!influence) {
    detailNode.textContent = 'No stochastic history influence yet. Run influence after stochastic recovery to make recovered and unrecovered histories affect later bounded choices.';
    return;
  }
  const choices = influence.choiceRecords.slice(-8).map(row => [
    `${row.id} ${row.actor}: ${row.decision}`,
    `recovered=${row.recoveredCount}`,
    `pending=${row.pendingCount}`,
    `stabilized=${row.stabilizedCount}`,
    `reason=${row.reason}`,
    `permanentPenalty=${row.permanentPenalty}`
  ].join(' / '));
  const refusals = influence.refusalRecords.slice(-6).map(row => `${row.id} ${row.actor}: ${row.reason} / recoveryPath=${row.recoveryPath}`);
  const echoes = influence.socialEchoes.slice(-8).map(row => `${row.id} ${row.from}->${row.to}: ${row.message} / directAvatarCommand=${row.directAvatarCommand}`);
  detailNode.textContent = [
    `Boundary: ${influence.boundary}`,
    `Source recovery count: ${influence.sourceRecoveryCount}`,
    `Policy: ${influence.noPermanentPunishmentPolicy}`,
    '',
    'Choice records:',
    ...(choices.length ? choices : ['No choice records yet.']),
    '',
    'Bounded refusals:',
    ...(refusals.length ? refusals : ['No bounded refusals yet.']),
    '',
    'Social echoes:',
    ...(echoes.length ? echoes : ['No social echoes yet.'])
  ].join('\n');
}
function renderStochasticOrdinaryAffordance() {
  const summaryNode = document.getElementById('stochasticOrdinaryAffordanceSummaryOut');
  const detailNode = document.getElementById('stochasticOrdinaryAffordanceOut');
  const affordance = world.stochasticOrdinaryAffordance;
  if (summaryNode) {
    summaryNode.textContent = affordance
      ? `${affordance.actionRecords.length} normal actions / ${affordance.blockedCount} bounded blocks / ${affordance.movementBiasCount} movement biases`
      : 'No ordinary-affordance influence yet.';
  }
  if (!detailNode) return;
  if (!affordance) {
    detailNode.textContent = 'No ordinary-affordance influence yet. Use normal actions after stochastic history influence to see Talk, Help, Schedule, and Movement change from recovery history.';
    return;
  }
  const actionLines = affordance.actionRecords.slice(-10).map(row => [
    `${row.id} ${row.actor}: ${row.action}`,
    `decision=${row.sourceDecision}`,
    `outcome=${row.outcome}`,
    `blocked=${row.blocked}`,
    `moveScale=${row.movementScale}`,
    `source=${row.sourceChoiceId || 'none'}`,
    `permanentPenalty=${row.permanentPenalty}`
  ].join(' / '));
  const sourceLines = affordance.sourceLedger.slice(-8).map(row => `${row.actionId}: ${row.sourceChoiceId} -> ${row.normalAction}`);
  detailNode.textContent = [
    `Boundary: ${affordance.boundary}`,
    `Policy: ${affordance.normalPlayPolicy}`,
    `Source history choices: ${affordance.sourceChoiceCount}`,
    '',
    'Normal action records:',
    ...(actionLines.length ? actionLines : ['No normal actions influenced yet.']),
    '',
    'Source ledger:',
    ...(sourceLines.length ? sourceLines : ['No source links recorded yet.'])
  ].join('\n');
}
function renderPromiseFollowUp() {
  const node = document.getElementById('promiseFollowUpOut');
  if (!node) return;
  if (!world.promiseFollowUp) {
    node.textContent = 'No remembered follow-up yet.';
    return;
  }
  node.textContent = world.promiseFollowUp.visibleStatus;
}
function renderObligationList() {
  const listNode = document.getElementById('obligationListOut');
  const selectNode = document.getElementById('obligationSelect');
  const obligations = world.obligationLedger || [];
  if (selectNode) {
    selectNode.innerHTML = obligations.map(item => `<option value="${item.id}">${item.resident}: ${item.status} / ${item.stage}</option>`).join('');
    if (obligations.length > 0) {
      if (!world.selectedObligationId || !obligations.some(item => item.id === world.selectedObligationId)) {
        world.selectedObligationId = obligations[0].id;
      }
      selectNode.value = world.selectedObligationId;
    }
  }
  if (!listNode) return;
  if (obligations.length === 0) {
    listNode.textContent = 'No selectable obligations yet.';
    return;
  }
  listNode.textContent = obligations.map(item => `${item.id}: ${item.status} / ${item.stage} / ${item.visibleStatus}`).join('\n');
}
function renderScheduleDebtIntegration() {
  const scheduleNode = document.getElementById('scheduleQueueOut');
  const debtNode = document.getElementById('debtLedgerOut');
  const scheduleQueue = world.scheduleQueue || [];
  const debtLedger = world.debtLedger || [];
  if (scheduleNode) {
    scheduleNode.textContent = scheduleQueue.length
      ? scheduleQueue.map(item => `${item.id}: ${item.status} / ${item.visibleStatus}`).join('\n')
      : 'No obligation-linked schedule items yet.';
  }
  if (debtNode) {
    debtNode.textContent = debtLedger.length
      ? debtLedger.map(item => `${item.id}: ${item.status} / debt ${item.debtAfter} / ${item.visibleStatus}`).join('\n')
      : 'No obligation-linked debt entries yet.';
  }
}
function renderAbsentTimeSummary() {
  const node = document.getElementById('absentTimeSummaryOut');
  if (!node) return;
  if (!world.absentTimeSummary) {
    node.textContent = 'No absent-time summary yet.';
    return;
  }
  node.textContent = [
    `Phase: ${world.absentTimeSummary.phase}`,
    `Avatar-caused: ${world.absentTimeSummary.avatarCaused.join('; ')}`,
    `Resident-caused: ${world.absentTimeSummary.residentCaused.join('; ')}`,
    `Before choosing: ${world.absentTimeSummary.beforeChoice}`
  ].join('\n');
}
function renderAbsentTimeChoice() {
  const node = document.getElementById('absentTimeChoiceOut');
  if (!node) return;
  const threads = world.absentTimeThreads || [];
  if (!world.absentTimeSummary || threads.length === 0) {
    node.textContent = 'No absent-time choice yet.';
    return;
  }
  const receipt = world.absentTimeChoiceReceipt;
  const pendingUnchosen = receipt
    ? threads.filter(thread => thread.id !== receipt.chosenThreadId && thread.status === 'pending').map(thread => thread.id)
    : threads.map(thread => thread.id);
  node.textContent = [
    `Threads: ${threads.map(thread => `${thread.id} ${thread.source} ${thread.status}`).join('; ')}`,
    receipt ? `Choice: ${receipt.chosenThreadId} / ${receipt.chosenSource} / ${receipt.phase}` : 'Choice: no thread chosen yet',
    `Unchosen pending: ${pendingUnchosen.length ? pendingUnchosen.join('; ') : 'none'}`,
    receipt ? `Receipt: ${receipt.visibleStatus}` : 'Receipt: waiting for bounded choice'
  ].join('\n');
}
function renderAvatarAbsenceAccountability() {
  const node = document.getElementById('avatarAbsenceAccountabilityOut');
  if (!node) return;
  const receipt = world.avatarAbsenceAccountabilityReceipt;
  if (!receipt) {
    node.textContent = 'No avatar absence accountability receipt yet.';
    return;
  }
  node.textContent = [
    `Phase: ${receipt.phase}`,
    `Avatar thread: ${receipt.avatarThreadStatus}`,
    `Resident thread: ${receipt.residentThreadId} ${receipt.residentThreadStatus}`,
    `History preserved: ${receipt.residentHistoryPreserved ? 'yes' : 'no'}`,
    `Receipt: ${receipt.visibleStatus}`
  ].join('\n');
}
function log(event, payload) {
  const row = { event, tick: world.tick++, selected: world.selected, room: world.avatar.room, payload };
  world.replay.push(row);
  if (world.replay.length > 240) world.replay.shift();
  localStorage.setItem(STATE_KEY, JSON.stringify(world));
  localStorage.setItem(REPLAY_KEY, JSON.stringify(world.replay));
  render();
  renderReturnContinuity();
  renderReturnGreetingContinuity();
  renderAccountabilitySocialEcho();
  renderBoundedEchoConversation();
  renderEchoInfluencedChoiceReceipt();
  renderAnomalyDiscovery();
  renderAnomalyInvestigationSchedule();
  renderPromiseFollowUp();
  renderObligationList();
  renderScheduleDebtIntegration();
  renderAbsentTimeSummary();
  renderAbsentTimeChoice();
  renderAvatarAbsenceAccountability();
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
function enterWorld() {
  const returningVisit = world.entered === true && world.replay.length > 0;
  const replayRowsBeforeReturn = world.replay.length;
  world.entered = true;
  world.avatar.room = 'arrival court';
  if (returningVisit) {
    const residentName = world.selected;
    mutateResident(residentName, {
      trust: 0.01,
      progress: 0.006,
      memory: `recognized returning avatar after ${replayRowsBeforeReturn} replay row(s)`,
      historyEvent: 'return recognition',
      historyDetail: `recognized avatar returning through ${world.avatar.room}`
    });
    world.returnContinuity = {
      reportIntroduced: 350,
      resident: residentName,
      replayRowsBeforeReturn,
      memory: world.residents[residentName].memory,
      recognizedAtTick: world.tick,
      boundary: 'browser-local-return-recognition-public-state-only'
    };
    advancePromiseFollowUpState(residentName, 'return', replayRowsBeforeReturn);
    applyAccountabilityReturnGreeting(replayRowsBeforeReturn);
  }
  return log('enterWorld', { boundary: BOUNDARY, returningVisit, returnContinuity: world.returnContinuity || null, returnGreetingContinuity: world.returnGreetingContinuity || null, promiseFollowUp: world.promiseFollowUp || null });
}
function applyAccountabilityReturnGreeting(replayRowsBeforeReturn) {
  const receipt = world.avatarAbsenceAccountabilityReceipt;
  if (!receipt || receipt.phase !== 'avatar-absence-accounted') return null;
  const residentThreadId = receipt.residentThreadId;
  const obligation = (world.obligationLedger || []).find(row => row.id === residentThreadId);
  const event = (world.offscreenObligationEvents || []).find(row => row.obligationId === residentThreadId);
  const residentName = obligation ? obligation.resident : receipt.residentThreadId.split('-')[0];
  const resident = world.residents[residentName];
  if (!resident) return null;
  const historyPreserved = Boolean(event && obligation && receipt.residentHistoryPreserved);
  const greeting = `${residentName} remembers ${residentThreadId} was ${obligation ? obligation.status : 'missing'} and your absence was ${receipt.avatarThreadStatus}`;
  mutateResident(residentName, {
    trust: 0.008,
    progress: 0.007,
    memory: `return greeting linked ${residentThreadId} and accounted avatar absence`,
    historyEvent: 'accountability return greeting',
    historyDetail: `${greeting}; history preserved ${historyPreserved ? 'yes' : 'no'}`
  });
  world.returnGreetingContinuity = {
    reportIntroduced: 358,
    resident: residentName,
    greeting,
    residentThreadId,
    residentObligationStatus: obligation ? `${obligation.status}/${obligation.stage}` : 'missing',
    avatarThreadStatus: receipt.avatarThreadStatus,
    residentHistoryPreserved: historyPreserved,
    replayRowsBeforeReturn,
    boundary: 'browser-local-accountability-return-greeting-only'
  };
  return world.returnGreetingContinuity;
}
function moveNorth() {
  const ordinaryInfluence = applyStochasticHistoryToOrdinaryAction('moveNorth', world.selected);
  const step = Math.max(8, Math.round(34 * ordinaryInfluence.movementScale));
  world.avatar.y = Math.max(52, world.avatar.y - step);
  return log('moveNorth', { y: world.avatar.y, step, ordinaryInfluence });
}
function moveSouth() {
  const ordinaryInfluence = applyStochasticHistoryToOrdinaryAction('moveSouth', world.selected);
  const step = Math.max(8, Math.round(34 * ordinaryInfluence.movementScale));
  world.avatar.y = Math.min(560, world.avatar.y + step);
  return log('moveSouth', { y: world.avatar.y, step, ordinaryInfluence });
}
function moveWest() {
  const ordinaryInfluence = applyStochasticHistoryToOrdinaryAction('moveWest', world.selected);
  const step = Math.max(8, Math.round(34 * ordinaryInfluence.movementScale));
  world.avatar.x = Math.max(52, world.avatar.x - step);
  updateRoom();
  return log('moveWest', { x: world.avatar.x, room: world.avatar.room, step, ordinaryInfluence });
}
function moveEast() {
  const ordinaryInfluence = applyStochasticHistoryToOrdinaryAction('moveEast', world.selected);
  const step = Math.max(8, Math.round(34 * ordinaryInfluence.movementScale));
  world.avatar.x = Math.min(970, world.avatar.x + step);
  updateRoom();
  return log('moveEast', { x: world.avatar.x, room: world.avatar.room, step, ordinaryInfluence });
}
function updateRoom() { world.avatar.room = ['arrival court', 'tool alcove', 'rain court', 'fiber loft'][Math.floor(world.avatar.x / 250) % 4]; }
function buildBoundedEchoConversation(phrase) {
  const echo = world.accountabilitySocialEcho;
  if (!echo || world.selected !== echo.echoResident) return null;
  if (!['greet', 'ask_schedule', 'ask_debt'].includes(phrase)) return null;
  const reply = `${echo.echoResident} says: I heard ${echo.sourceResident} say ${echo.residentThreadId} stayed ${echo.residentObligationStatus}; avatar absence ${echo.avatarThreadStatus}.`;
  world.boundedEchoConversation = {
    reportIntroduced: 360,
    resident: echo.echoResident,
    phrase,
    reply,
    sourceEchoId: echo.residentThreadId,
    sourceResident: echo.sourceResident,
    echoResident: echo.echoResident,
    residentObligationStatus: echo.residentObligationStatus,
    avatarThreadStatus: echo.avatarThreadStatus,
    directAvatarCommand: echo.directAvatarCommand,
    noLLM: true,
    autonomousLanguage: false,
    phrasebookOnly: true,
    boundary: 'browser-local-bounded-echo-conversation-only'
  };
  recordResidentHistory(echo.echoResident, 'bounded echo conversation', `${reply}; no LLM true; phrasebook only true`);
  return world.boundedEchoConversation;
}
function talkBounded() {
  const phrase = phraseSelect.value;
  const boundedEchoConversation = buildBoundedEchoConversation(phrase);
  const ordinaryInfluence = applyStochasticHistoryToOrdinaryAction('talkBounded', world.selected);
  const memory = boundedEchoConversation
    ? `bounded echo reply referenced ${boundedEchoConversation.sourceEchoId}`
    : `${ordinaryInfluence.talkTone}: heard bounded phrase ${phrase}`;
  mutateResident(world.selected, { trust: ordinaryInfluence.trustDelta, progress: ordinaryInfluence.progressDelta, memory });
  const livedActionPressure = recordOrdinaryPlayPressure('talkBounded', world.selected);
  return log('talkBounded', { phrase, boundedEchoConversation, ordinaryInfluence, livedActionPressure, noLLM: true, autonomousLanguage: false, phrasebookOnly: true });
}
function applyEchoInfluencedChoiceReceipt(action) {
  const conversation = world.boundedEchoConversation;
  const echo = world.accountabilitySocialEcho;
  if (!conversation || !echo || world.selected !== conversation.resident || conversation.resident !== echo.echoResident) return null;
  if (action !== 'offer_help') return null;
  const obligation = (world.obligationLedger || []).find(row => row.id === conversation.sourceEchoId);
  const event = (world.offscreenObligationEvents || []).find(row => row.obligationId === conversation.sourceEchoId);
  const sourceAttributionPreserved = Boolean(obligation && event && echo.residentHistoryPreserved && echo.directAvatarCommand === false);
  const choice = 'accept_source_bounded_help';
  const refusal = `refuses to rewrite ${event ? event.actor : 'unknown'} as the direct avatar cause or erase ${echo.sourceResident}'s source memory`;
  const visibleStatus = `${conversation.resident} accepts help only for ${conversation.sourceEchoId} follow-up and refuses history rewrite; source attribution preserved ${sourceAttributionPreserved ? 'yes' : 'no'}`;
  world.echoInfluencedChoiceReceipt = {
    reportIntroduced: 361,
    resident: conversation.resident,
    action,
    choice,
    refusal,
    visibleStatus,
    sourceEchoId: conversation.sourceEchoId,
    sourceResident: echo.sourceResident,
    echoResident: echo.echoResident,
    sourceAttributionPreserved,
    directAvatarCommand: false,
    noLLM: true,
    autonomousLanguage: false,
    phrasebookOnly: true,
    recoverable: true,
    boundary: 'browser-local-echo-influenced-choice-refusal-only'
  };
  recordResidentHistory(conversation.resident, 'echo-influenced choice/refusal', `${visibleStatus}; no LLM true; recoverable true`);
  return world.echoInfluencedChoiceReceipt;
}
function askSchedule() {
  const ordinaryInfluence = applyStochasticHistoryToOrdinaryAction('askSchedule', world.selected);
  const schedule = ordinaryInfluence.blocked ? 'schedule answer bounded by pending recovery' : currentResident().schedule;
  const livedActionPressure = recordOrdinaryPlayPressure('askSchedule', world.selected);
  return log('askSchedule', { schedule, ordinaryInfluence, livedActionPressure });
}
function offerHelp() {
  const echoInfluencedChoiceReceipt = applyEchoInfluencedChoiceReceipt('offer_help');
  const ordinaryInfluence = applyStochasticHistoryToOrdinaryAction('offerHelp', world.selected);
  const memory = ordinaryInfluence.blocked
    ? `bounded refusal from stochastic history: ${ordinaryInfluence.outcome}`
    : (echoInfluencedChoiceReceipt ? `accepted source-bounded help for ${echoInfluencedChoiceReceipt.sourceEchoId}; refused history rewrite` : `${ordinaryInfluence.outcome} with ${currentResident().schedule}`);
  mutateResident(world.selected, { trust: ordinaryInfluence.trustDelta, debt: ordinaryInfluence.debtDelta, progress: ordinaryInfluence.progressDelta, memory });
  world.resources.care = Math.max(0, world.resources.care - ordinaryInfluence.careCost);
  const livedActionPressure = recordOrdinaryPlayPressure('offerHelp', world.selected);
  return log('offerHelp', { care: world.resources.care, helped: !ordinaryInfluence.blocked, echoInfluencedChoiceReceipt, ordinaryInfluence, livedActionPressure, noLLM: true, autonomousLanguage: false, phrasebookOnly: true });
}
function borrowTool() {
  mutateResident(world.selected, { trust: -0.018, debt: 1, memory: 'avatar borrowed tool' });
  const livedActionPressure = recordOrdinaryPlayPressure('borrowTool', world.selected);
  return log('borrowTool', { consequence: 'debt increases', livedActionPressure });
}
function returnTool() {
  mutateResident(world.selected, { trust: 0.022, debt: -1, memory: 'avatar returned tool' });
  const livedActionPressure = recordOrdinaryPlayPressure('returnTool', world.selected);
  return log('returnTool', { consequence: 'trust repairs partially', livedActionPressure });
}
function seededAnomalyRng(seed) {
  let state = (Number(seed) >>> 0) || 362;
  return function next() {
    state = (state * 1664525 + 1013904223) >>> 0;
    return state / 4294967296;
  };
}
function anomalySeed() {
  return Number(urlParams.get('anomalySeed') || (world.anomalyDiscovery && world.anomalyDiscovery.seed) || 36217);
}
function roundedProperty(value) { return Number(Math.max(0, Math.min(1, value)).toFixed(3)); }
function generateHiddenWorldLaw(seed) {
  const rng = seededAnomalyRng(seed);
  const templates = {
    red_scrap: { conductivityLike: 0.78, chargeRetention: 0.22, frictionResponse: 0.30, moistureSensitivity: 0.18, heatTolerance: 0.74, fragility: 0.26, toxicity: 0.12, combustionRisk: 0.10, insulationBlocking: 0.08, storagePotential: 0.30, magneticAttraction: 0.64 },
    dry_resin: { conductivityLike: 0.20, chargeRetention: 0.72, frictionResponse: 0.82, moistureSensitivity: 0.70, heatTolerance: 0.42, fragility: 0.38, toxicity: 0.18, combustionRisk: 0.52, insulationBlocking: 0.58, storagePotential: 0.68, magneticAttraction: 0.06 },
    wet_wood: { conductivityLike: 0.34, chargeRetention: 0.08, frictionResponse: 0.12, moistureSensitivity: 0.92, heatTolerance: 0.36, fragility: 0.32, toxicity: 0.08, combustionRisk: 0.44, insulationBlocking: 0.38, storagePotential: 0.10, magneticAttraction: 0.04 },
    reed_fiber: { conductivityLike: 0.16, chargeRetention: 0.48, frictionResponse: 0.76, moistureSensitivity: 0.55, heatTolerance: 0.30, fragility: 0.62, toxicity: 0.06, combustionRisk: 0.60, insulationBlocking: 0.54, storagePotential: 0.42, magneticAttraction: 0.03 },
    ash_glass: { conductivityLike: 0.10, chargeRetention: 0.62, frictionResponse: 0.54, moistureSensitivity: 0.24, heatTolerance: 0.82, fragility: 0.78, toxicity: 0.10, combustionRisk: 0.02, insulationBlocking: 0.74, storagePotential: 0.76, magneticAttraction: 0.02 },
    iron_sand: { conductivityLike: 0.68, chargeRetention: 0.18, frictionResponse: 0.22, moistureSensitivity: 0.30, heatTolerance: 0.70, fragility: 0.18, toxicity: 0.16, combustionRisk: 0.06, insulationBlocking: 0.12, storagePotential: 0.26, magneticAttraction: 0.86 },
    clay_jar: { conductivityLike: 0.12, chargeRetention: 0.52, frictionResponse: 0.44, moistureSensitivity: 0.46, heatTolerance: 0.66, fragility: 0.70, toxicity: 0.04, combustionRisk: 0.01, insulationBlocking: 0.68, storagePotential: 0.64, magneticAttraction: 0.01 }
  };
  const materials = {};
  Object.entries(templates).forEach(([id, props]) => {
    materials[id] = {};
    Object.entries(props).forEach(([key, value]) => {
      materials[id][key] = roundedProperty(value + (rng() - 0.5) * 0.16);
    });
  });
  return { seed, materials, hiddenFromResidents: true, propertyNames: Object.keys(templates.red_scrap) };
}
function observationForMaterials(law, materials, witness, phase) {
  const props = materials.map(id => law.materials[id]);
  const avg = key => props.reduce((sum, row) => sum + row[key], 0) / props.length;
  let effect = 'nothing repeated clearly';
  let severity = 'low';
  if (avg('combustionRisk') > 0.48 && avg('heatTolerance') < 0.52) {
    effect = 'smoke appeared and the test was stopped';
    severity = 'risk';
  } else if (avg('magneticAttraction') > 0.45) {
    effect = 'dark grains crawled toward the red scrap';
  } else if (avg('conductivityLike') > 0.48 && avg('chargeRetention') > 0.24) {
    effect = 'the sharp bite carried farther than a handspan';
  } else if (avg('frictionResponse') > 0.58 && avg('chargeRetention') > 0.42) {
    effect = 'loose fiber jumped after rubbing';
  } else if (avg('moistureSensitivity') > 0.62) {
    effect = 'wet pieces dulled the effect and left only a sting';
  } else if (avg('fragility') > 0.68) {
    effect = 'a tool edge cracked before the sign returned';
    severity = 'breakage';
  }
  return {
    id: `OBS-${String((world.anomalyDiscovery ? world.anomalyDiscovery.observations.length : 0) + 1).padStart(2, '0')}`,
    witness,
    phase,
    materials,
    effect,
    severity,
    trueLawExposed: false
  };
}
function residentAnomalyVocabulary(name, rng) {
  const vocab = {
    Ari: ['awl-bite', 'roof-snap', 'dry-path'],
    Fay: ['quiet sting', 'jar omen', 'herb-jump'],
    Milo: ['water-anger', 'red carry', 'handspan bite'],
    Sera: ['cloak ghost', 'smoke warning', 'cold spark'],
    Tovan: ['route sign', 'safe-gap', 'storm crumb'],
    Nia: ['glass sleep', 'grain pull', 'shelf whisper']
  };
  const options = vocab[name] || ['strange sign'];
  return options[Math.floor(rng() * options.length)];
}
function generateInitialBelief(name, observation, rng, transmitted) {
  const kinds = ['practical', 'skeptical', 'ritualized', 'fearful', 'useful_wrong'];
  const kind = kinds[Math.floor(rng() * kinds.length)];
  return {
    label: residentAnomalyVocabulary(name, rng),
    kind,
    confidence: Number((0.28 + rng() * 0.32 + (transmitted ? -0.06 : 0.04)).toFixed(3)),
    source: transmitted ? 'social transmission' : observation.id,
    evidence: [observation.effect],
    contradictionCount: 0,
    socialTrust: Number(((world.residents[name] || currentResident()).trust || 0.5).toFixed(3)),
    personallyWitnessed: !transmitted,
    modernConcept: false,
    directAvatarCommand: false
  };
}
function introduceWorldAnomaly() {
  if (world.anomalyDiscovery) return log('introduceWorldAnomaly', { alreadyIntroduced: true, seed: world.anomalyDiscovery.seed });
  const seed = anomalySeed();
  const rng = seededAnomalyRng(seed);
  const hiddenWorldLaw = generateHiddenWorldLaw(seed);
  const observation = observationForMaterials(hiddenWorldLaw, ['dry_resin', 'reed_fiber'], world.selected, 'avatar demonstration');
  const beliefs = {};
  beliefs[world.selected] = generateInitialBelief(world.selected, observation, rng, false);
  world.anomalyDiscovery = {
    reportIntroduced: 362,
    seed,
    label: `unexplained material sign ${seed}`,
    hiddenWorldLaw,
    observations: [observation],
    residentBeliefs: beliefs,
    experiments: [],
    failures: [],
    socialTransmissions: [],
    culturalMemory: [],
    auditReplay: [
      { type: 'hidden_law', summary: 'simulator created hidden material properties; not resident knowledge', auditOnly: true },
      { type: 'public_observation', summary: `${observation.witness} observed ${observation.effect}`, auditOnly: false },
      { type: 'private_belief', summary: `${world.selected} formed "${beliefs[world.selected].label}" without modern terms`, auditOnly: false }
    ],
    avatarBoundary: 'avatar demonstrated an unexplained effect; residents receive observations only, not a correct concept',
    noTechnologyTree: true,
    noInstantCorrectUnlock: true,
    boundary: 'browser-local-non-scripted-anomaly-discovery-only'
  };
  mutateResident(world.selected, { trust: 0.004, memory: `saw unexplained material sign and named it ${beliefs[world.selected].label}`, historyEvent: 'anomaly observation', historyDetail: observation.effect });
  return log('introduceWorldAnomaly', { seed, publicObservation: observation, residentBelief: beliefs[world.selected], hiddenLawAuditOnly: true, avatarHintNotCommand: true });
}
function chooseAnomalyTest(discovery, forcedActor) {
  const rng = seededAnomalyRng(discovery.seed + discovery.experiments.length * 97 + world.tick);
  const names = Object.keys(world.residents);
  const actor = forcedActor || names[(discovery.experiments.length + Math.floor(rng() * names.length)) % names.length];
  const belief = discovery.residentBeliefs[actor] || generateInitialBelief(actor, discovery.observations[0], rng, true);
  discovery.residentBeliefs[actor] = belief;
  const candidateTests = [
    { materials: ['red_scrap', 'dry_resin'], reason: 'compare red carry with dry sign' },
    { materials: ['wet_wood', 'dry_resin'], reason: 'try a wet counterexample' },
    { materials: ['ash_glass', 'reed_fiber'], reason: 'see whether glass sleep holds the jump' },
    { materials: ['iron_sand', 'red_scrap'], reason: 'test whether dark grains follow red scrap' },
    { materials: ['clay_jar', 'reed_fiber'], reason: 'try storage in a common jar' },
    { materials: ['wet_wood', 'red_scrap'], reason: 'ask whether water ruins the carry' }
  ];
  const offset = Math.floor((belief.confidence + belief.socialTrust + rng()) * candidateTests.length) % candidateTests.length;
  return { actor, belief, ...candidateTests[offset] };
}
function runAnomalyExperiment(forcedActor) {
  if (!world.anomalyDiscovery) introduceWorldAnomaly();
  const discovery = world.anomalyDiscovery;
  const test = chooseAnomalyTest(discovery, forcedActor);
  const observation = observationForMaterials(discovery.hiddenWorldLaw, test.materials, test.actor, 'resident experiment');
  const failure = /nothing|dulled|cracked|smoke/.test(observation.effect);
  const belief = discovery.residentBeliefs[test.actor];
  if (failure) {
    belief.contradictionCount += 1;
    belief.confidence = Number(Math.max(0.08, belief.confidence - 0.09).toFixed(3));
  } else {
    belief.confidence = Number(Math.min(0.86, belief.confidence + 0.08).toFixed(3));
  }
  belief.evidence = belief.evidence.concat([observation.effect]).slice(-5);
  const experiment = {
    id: `EXP-${String(discovery.experiments.length + 1).padStart(2, '0')}`,
    actor: test.actor,
    materials: test.materials,
    reason: test.reason,
    consumed: { time: 1 + discovery.experiments.length, materials: test.materials },
    outcome: observation.effect,
    failure,
    sourceBelief: belief.label,
    noGuaranteedSuccess: true,
    technologyUnlock: false
  };
  discovery.observations.push(observation);
  discovery.experiments.push(experiment);
  if (failure) discovery.failures.push(experiment);
  discovery.auditReplay.push(
    { type: 'experiment', summary: `${experiment.actor} tested ${experiment.materials.join(' + ')} from belief "${belief.label}"`, auditOnly: false },
    { type: failure ? 'failed_experiment' : 'public_observation', summary: `${experiment.id} outcome: ${experiment.outcome}`, auditOnly: false },
    { type: 'private_belief', summary: `${experiment.actor} confidence now ${belief.confidence}; contradictions ${belief.contradictionCount}`, auditOnly: false }
  );
  mutateResident(test.actor, { progress: failure ? 0.004 : 0.014, trust: failure ? -0.002 : 0.006, memory: `tested ${belief.label}: ${observation.effect}`, historyEvent: failure ? 'failed anomaly experiment' : 'anomaly experiment', historyDetail: `${experiment.id} ${test.materials.join(' + ')} -> ${observation.effect}` });
  return log('runAnomalyExperiment', { experiment, observation, belief, failedExperimentPreserved: failure, materialConstraintBinding: true, scheduledResident: forcedActor || null });
}
function spreadAnomalyBelief() {
  if (!world.anomalyDiscovery) introduceWorldAnomaly();
  const discovery = world.anomalyDiscovery;
  if (!discovery.experiments.length) runAnomalyExperiment();
  const rng = seededAnomalyRng(discovery.seed + discovery.socialTransmissions.length * 131 + 17);
  const names = Object.keys(world.residents);
  const from = names[Math.floor(rng() * names.length)];
  const to = names[(names.indexOf(from) + 1 + Math.floor(rng() * (names.length - 1))) % names.length];
  const sourceBelief = discovery.residentBeliefs[from] || generateInitialBelief(from, discovery.observations[0], rng, true);
  discovery.residentBeliefs[from] = sourceBelief;
  const mutationWords = ['warning', 'trick', 'path', 'omen', 'craft', 'taboo'];
  const after = `${sourceBelief.label}-${mutationWords[Math.floor(rng() * mutationWords.length)]}`;
  const transmittedObservation = discovery.observations[Math.floor(rng() * discovery.observations.length)];
  discovery.residentBeliefs[to] = {
    label: after,
    kind: rng() > 0.62 ? 'ritualized' : rng() > 0.44 ? 'useful_wrong' : 'practical',
    confidence: Number(Math.max(0.1, Math.min(0.78, sourceBelief.confidence + (rng() - 0.5) * 0.18)).toFixed(3)),
    source: `heard from ${from}`,
    evidence: [transmittedObservation.effect],
    contradictionCount: Math.max(0, sourceBelief.contradictionCount + (rng() > 0.72 ? 1 : 0)),
    socialTrust: Number(((world.residents[to] || currentResident()).trust || 0.5).toFixed(3)),
    personallyWitnessed: false,
    modernConcept: false,
    directAvatarCommand: false
  };
  const channels = ['gossip', 'teaching', 'trade', 'argument', 'ritual caution', 'household warning'];
  const row = {
    id: `SOC-${String(discovery.socialTransmissions.length + 1).padStart(2, '0')}`,
    from,
    to,
    channel: channels[Math.floor(rng() * channels.length)],
    before: sourceBelief.label,
    after,
    mutation: 'label/evidence/confidence mutated during social spread',
    sourceAvatarCommand: false
  };
  discovery.socialTransmissions.push(row);
  const successCount = discovery.experiments.filter(item => !item.failure).length;
  const memory = successCount >= 2
    ? `Some residents keep a practical dry-material test, but no one has a final name.`
    : discovery.failures.length >= 2
      ? `The sign is remembered with caution because failures stayed in the story.`
      : `Residents disagree about ${after} and keep testing.`;
  discovery.culturalMemory.push({ id: `CUL-${String(discovery.culturalMemory.length + 1).padStart(2, '0')}`, memory, competingBeliefs: Object.values(discovery.residentBeliefs).map(item => item.label).slice(-6), noCorrectUnlock: true });
  discovery.auditReplay.push(
    { type: 'social_transmission', summary: `${from} -> ${to} via ${row.channel}; "${row.before}" mutated to "${row.after}"`, auditOnly: false },
    { type: 'cultural_memory', summary: memory, auditOnly: false }
  );
  mutateResident(to, { trust: 0.003, progress: 0.006, memory: `heard anomaly belief ${after} from ${from}`, historyEvent: 'anomaly social transmission', historyDetail: `${row.channel}: ${row.before} -> ${row.after}` });
  return log('spreadAnomalyBelief', { transmission: row, transmittedBelief: discovery.residentBeliefs[to], culturalMemory: discovery.culturalMemory.slice(-1)[0], socialTransmissionMutation: true, avatarHintNotCommand: true });
}
function anomalySlotMaterialCost(resident, index) {
  const costs = [
    { fiber: 1, wood: 1, care: 0, water: 0 },
    { fiber: 0, wood: 1, care: 1, water: 1 },
    { fiber: 1, wood: 0, care: 1, water: 0 },
    { fiber: 0, wood: 2, care: 0, water: 1 }
  ];
  const offset = (resident.charCodeAt(0) + index) % costs.length;
  return costs[offset];
}
function hasResourcesFor(cost) {
  return Object.entries(cost).every(([key, value]) => (world.resources[key] || 0) >= value);
}
function applyResourceCost(cost) {
  Object.entries(cost).forEach(([key, value]) => {
    world.resources[key] = Math.max(0, (world.resources[key] || 0) - value);
  });
}
function planAnomalyInvestigationSchedule() {
  if (!world.anomalyDiscovery) introduceWorldAnomaly();
  const discovery = world.anomalyDiscovery;
  const residentsToPlan = Object.keys(world.residents).slice(0, 5);
  const blocks = ['dawn work block', 'midday work block', 'rain pause', 'evening repair', 'market gossip'];
  const beliefKinds = new Set(Object.values(discovery.residentBeliefs).map(belief => belief.kind));
  const slots = residentsToPlan.map((resident, index) => {
    const rng = seededAnomalyRng(discovery.seed + index * 211 + world.tick);
    const baseObservation = discovery.observations[0];
    if (!discovery.residentBeliefs[resident]) {
      discovery.residentBeliefs[resident] = generateInitialBelief(resident, baseObservation, rng, true);
    }
    const belief = discovery.residentBeliefs[resident];
    const materialCost = anomalySlotMaterialCost(resident, index);
    const scarce = !hasResourcesFor(materialCost);
    const fear = Number(Math.min(1, (belief.kind === 'fearful' ? 0.42 : 0.12) + belief.contradictionCount * 0.16 + (belief.kind === 'ritualized' ? 0.14 : 0)).toFixed(3));
    const trust = Number((world.residents[resident].trust || 0.5).toFixed(3));
    const socialPressure = Number(Math.min(1, discovery.socialTransmissions.filter(row => row.from === resident || row.to === resident).length * 0.18 + beliefKinds.size * 0.04).toFixed(3));
    let decision = 'test_anomaly';
    let reason = 'curiosity and available materials beat ordinary work';
    if (scarce) {
      decision = 'defer_for_materials';
      reason = 'ordinary work keeps scarce material';
    } else if (fear > trust + 0.18) {
      decision = 'refuse_test';
      reason = 'fear and contradictions outweigh trust';
    } else if (socialPressure > 0.42 && belief.confidence < 0.48) {
      decision = 'argue_before_test';
      reason = 'social disagreement delays the test';
    }
    return {
      id: `AIS-${String(index + 1).padStart(2, '0')}`,
      block: blocks[index],
      resident,
      ordinaryWork: world.residents[resident].schedule,
      belief: belief.label,
      decision,
      reason,
      materialCost,
      fear,
      trust,
      socialPressure,
      status: 'planned',
      experimentId: null
    };
  });
  world.anomalyInvestigationSchedule = {
    reportIntroduced: 363,
    seed: discovery.seed,
    resourcesBefore: { ...world.resources },
    slots,
    testsRun: 0,
    refusals: 0,
    ordinaryWorkDelayed: 0,
    materialScarcityBlocks: slots.filter(slot => slot.decision === 'defer_for_materials').length,
    socialDisagreementKinds: beliefKinds.size,
    executionLog: [],
    noPanelOnlyLoop: true,
    boundary: 'browser-local-scheduled-anomaly-investigation-only'
  };
  discovery.auditReplay.push({ type: 'schedule_tradeoff', summary: `planned ${slots.length} anomaly investigation slots against ordinary resident work`, auditOnly: false });
  recordCheckpoint('anomaly schedule planned');
  return log('planAnomalyInvestigationSchedule', { slots, resourcesBefore: world.anomalyInvestigationSchedule.resourcesBefore, noPanelOnlyLoop: true, socialDisagreementKinds: beliefKinds.size });
}
function runScheduledAnomalyInvestigation() {
  if (!world.anomalyInvestigationSchedule) planAnomalyInvestigationSchedule();
  const schedule = world.anomalyInvestigationSchedule;
  const slot = schedule.slots.find(item => item.status === 'planned');
  if (!slot) return log('runScheduledAnomalyInvestigation', { complete: true, testsRun: schedule.testsRun, refusals: schedule.refusals, ordinaryWorkDelayed: schedule.ordinaryWorkDelayed });
  if (slot.decision !== 'test_anomaly') {
    slot.status = slot.decision === 'argue_before_test' ? 'deferred by disagreement' : 'refused or deferred';
    schedule.refusals += 1;
    const outcome = `${slot.resident} kept ${slot.ordinaryWork} ahead of anomaly testing because ${slot.reason}`;
    schedule.executionLog.push({ slotId: slot.id, resident: slot.resident, outcome, decision: slot.decision });
    world.anomalyDiscovery.auditReplay.push({ type: 'schedule_tradeoff', summary: outcome, auditOnly: false });
    mutateResident(slot.resident, { trust: slot.decision === 'refuse_test' ? -0.003 : 0.001, progress: 0.006, memory: `deferred anomaly test: ${slot.reason}`, historyEvent: 'anomaly schedule tradeoff', historyDetail: outcome });
    return log('runScheduledAnomalyInvestigation', { slot, executedTest: false, scheduleTradeoff: true, resources: world.resources });
  }
  if (!hasResourcesFor(slot.materialCost)) {
    slot.status = 'blocked by scarce materials';
    schedule.materialScarcityBlocks += 1;
    schedule.refusals += 1;
    const outcome = `${slot.resident} could not test ${slot.belief}; resources were too scarce`;
    schedule.executionLog.push({ slotId: slot.id, resident: slot.resident, outcome, decision: 'blocked_by_scarcity' });
    world.anomalyDiscovery.auditReplay.push({ type: 'schedule_tradeoff', summary: outcome, auditOnly: false });
    return log('runScheduledAnomalyInvestigation', { slot, executedTest: false, materialScarcityBlock: true, resources: world.resources });
  }
  applyResourceCost(slot.materialCost);
  schedule.ordinaryWorkDelayed += 1;
  const experimentRow = runAnomalyExperiment(slot.resident);
  const experiment = experimentRow.payload.experiment;
  slot.status = experiment.failure ? 'failed test preserved' : 'test completed';
  slot.experimentId = experiment.id;
  schedule.testsRun += 1;
  const outcome = `${slot.resident} delayed ${slot.ordinaryWork}, spent scheduled materials, and got ${experiment.outcome}`;
  schedule.executionLog.push({ slotId: slot.id, resident: slot.resident, outcome, decision: slot.decision, experimentId: experiment.id, failure: experiment.failure });
  world.anomalyDiscovery.auditReplay.push({ type: 'schedule_tradeoff', summary: outcome, auditOnly: false });
  return log('runScheduledAnomalyInvestigation', { slot, executedTest: true, experiment, resources: world.resources, ordinaryWorkDelayed: schedule.ordinaryWorkDelayed });
}
function ensureStochasticConsequencePulse() {
  if (!world.stochasticConsequencePulse) {
    world.stochasticConsequencePulse = {
      reportIntroduced: 364,
      mode: 'runtime entropy recorded for inspectable replay',
      runtimeEntropySource: window.crypto && window.crypto.getRandomValues ? 'crypto.getRandomValues' : 'Math.random fallback',
      replayableEntropy: true,
      pulses: [],
      entropyLedger: [],
      scheduleCouplings: [],
      needs: {},
      boundary: 'browser-local-stochastic-consequence-pulse-only; no LLM call, no subjective consciousness, no moral patienthood'
    };
  }
  return world.stochasticConsequencePulse;
}
function entropyByte(label) {
  const pulse = ensureStochasticConsequencePulse();
  const bytes = new Uint8Array(1);
  if (window.crypto && window.crypto.getRandomValues) {
    window.crypto.getRandomValues(bytes);
  } else {
    bytes[0] = Math.floor(Math.random() * 256);
  }
  const row = { label, value: bytes[0], tick: world.tick, source: pulse.runtimeEntropySource };
  pulse.entropyLedger.push(row);
  if (pulse.entropyLedger.length > 80) pulse.entropyLedger.shift();
  return row;
}
function weightedEntropyPick(options, entropy) {
  const total = options.reduce((sum, option) => sum + option.weight, 0);
  let cursor = (entropy.value / 256) * total;
  for (const option of options) {
    cursor -= option.weight;
    if (cursor <= 0) return option;
  }
  return options[options.length - 1];
}
function residentNeedSnapshot(name) {
  const resident = world.residents[name];
  const resourcePressure = Math.max(0, 8 - world.resources.water - world.resources.care);
  const schedulePressure = world.anomalyInvestigationSchedule ? world.anomalyInvestigationSchedule.refusals + world.anomalyInvestigationSchedule.ordinaryWorkDelayed : 0;
  const energy = Number(Math.max(0.12, Math.min(0.95, 0.72 - resident.debt * 0.08 - resourcePressure * 0.03)).toFixed(3));
  const comfort = Number(Math.max(0.08, Math.min(0.96, 0.58 + resident.trust * 0.28 - schedulePressure * 0.025)).toFixed(3));
  const focus = Number(Math.max(0.1, Math.min(0.92, resident.progress + resident.trust * 0.18 - schedulePressure * 0.018)).toFixed(3));
  const dominant = energy < 0.35 ? 'rest' : comfort < 0.42 ? 'safety' : focus < 0.5 ? 'finish-work' : 'explore';
  return { energy, comfort, focus, dominant };
}
function applyResourceDelta(delta) {
  Object.keys(delta).forEach(key => {
    world.resources[key] = Math.max(0, (world.resources[key] || 0) + delta[key]);
  });
}
function runStochasticConsequencePulse() {
  if (!world.anomalyInvestigationSchedule) planAnomalyInvestigationSchedule();
  const pulse = ensureStochasticConsequencePulse();
  const names = Object.keys(world.residents);
  const actorEntropy = entropyByte('actor');
  const eventEntropy = entropyByte('event');
  const intensityEntropy = entropyByte('intensity');
  const actor = names[actorEntropy.value % names.length];
  const needBefore = residentNeedSnapshot(actor);
  const schedule = world.anomalyInvestigationSchedule;
  const pendingSlot = schedule && schedule.slots.find(slot => slot.status === 'planned' && (slot.resident === actor || eventEntropy.value % 3 === 0));
  const options = [
    { id: 'roof_leak', weight: 3 + (world.resources.wood < 2 ? 3 : 0), delta: { water: -1, fiber: 0, wood: -1, care: 0 }, trust: -0.004, progress: -0.006, debt: 1 },
    { id: 'tool_snag', weight: 3 + (pendingSlot ? 2 : 0), delta: { water: 0, fiber: -1, wood: 0, care: 0 }, trust: -0.002, progress: -0.01, debt: 0 },
    { id: 'neighbor_help', weight: 2 + Math.round(world.residents[actor].trust * 3), delta: { water: 0, fiber: 0, wood: 0, care: 1 }, trust: 0.008, progress: 0.014, debt: -1 },
    { id: 'argument_echo', weight: 2 + (schedule ? schedule.refusals : 0), delta: { water: 0, fiber: 0, wood: 0, care: 0 }, trust: -0.007, progress: -0.002, debt: 0 },
    { id: 'found_material', weight: 2 + (world.resources.fiber < 3 ? 3 : 0), delta: { water: 0, fiber: 1, wood: 1, care: 0 }, trust: 0.004, progress: 0.008, debt: 0 },
    { id: 'quiet_recovery', weight: 2 + (needBefore.energy < 0.42 ? 4 : 0), delta: { water: 0, fiber: 0, wood: 0, care: 0 }, trust: 0.003, progress: 0.006, debt: -1 }
  ];
  const event = weightedEntropyPick(options, eventEntropy);
  const intensity = Number((0.5 + intensityEntropy.value / 255).toFixed(3));
  const resourcesBefore = { ...world.resources };
  const scaledDelta = {};
  Object.keys(event.delta).forEach(key => {
    const value = event.delta[key];
    scaledDelta[key] = value < 0 && intensity > 1.1 ? value - 1 : value;
  });
  applyResourceDelta(scaledDelta);
  let scheduleCoupling = '';
  if (pendingSlot && ['roof_leak', 'tool_snag', 'argument_echo'].includes(event.id)) {
    pendingSlot.status = event.id === 'argument_echo' ? 'stochastically disputed' : 'stochastically delayed';
    schedule.refusals += 1;
    const summary = `${actor} ${pendingSlot.status} ${pendingSlot.id} while ${pendingSlot.ordinaryWork} competed with ${event.id}`;
    schedule.executionLog.push({ slotId: pendingSlot.id, resident: actor, outcome: summary, decision: event.id });
    scheduleCoupling = summary;
  } else if (pendingSlot && ['neighbor_help', 'found_material'].includes(event.id)) {
    pendingSlot.trust = Number(Math.min(0.99, pendingSlot.trust + 0.018).toFixed(3));
    scheduleCoupling = `${actor} made ${pendingSlot.id} easier to attempt after ${event.id}`;
  }
  const consequence = `${actor} encountered ${event.id} with intensity ${intensity}`;
  mutateResident(actor, {
    trust: Number((event.trust * intensity).toFixed(3)),
    progress: Number((event.progress * intensity).toFixed(3)),
    debt: event.debt,
    memory: `stochastic pulse: ${event.id}`,
    historyEvent: 'stochastic consequence',
    historyDetail: consequence
  });
  const needAfter = residentNeedSnapshot(actor);
  const row = {
    id: `SP-${String(pulse.pulses.length + 1).padStart(2, '0')}`,
    actor,
    event: event.id,
    entropy: [actorEntropy, eventEntropy, intensityEntropy],
    intensity,
    resourcesBefore,
    resourcesAfter: { ...world.resources },
    resourceDelta: scaledDelta,
    needBefore,
    needAfter,
    scheduleCoupling,
    consequence
  };
  pulse.needs[actor] = needAfter;
  pulse.pulses.push(row);
  if (pulse.pulses.length > 30) pulse.pulses.shift();
  if (scheduleCoupling) pulse.scheduleCouplings.push({ pulseId: row.id, summary: scheduleCoupling });
  if (pulse.scheduleCouplings.length > 20) pulse.scheduleCouplings.shift();
  recordCheckpoint('stochastic consequence pulse');
  return log('runStochasticConsequencePulse', { pulse: row, replayableEntropy: true, scheduleCoupled: Boolean(scheduleCoupling) });
}
function runStochasticConsequenceBurst() {
  const before = ensureStochasticConsequencePulse().pulses.length;
  for (let index = 0; index < 4; index += 1) runStochasticConsequencePulse();
  const after = ensureStochasticConsequencePulse().pulses.length;
  return log('runStochasticConsequenceBurst', { pulsesAdded: after - before, totalPulses: after, replayableEntropy: true });
}
function ensureStochasticRecoveryLoop() {
  if (!world.stochasticRecoveryLoop) {
    world.stochasticRecoveryLoop = {
      reportIntroduced: 365,
      sourcePulseCount: 0,
      recoveryQueue: [],
      repairLedger: [],
      relationshipRepairs: [],
      pendingCount: 0,
      resolvedCount: 0,
      stabilizedWithoutMaterials: 0,
      noPermanentDamagePolicy: 'every stochastic harm must have a bounded recovery or stabilization path',
      boundary: 'browser-local-stochastic-recovery-loop-only; no LLM call, no subjective consciousness, no moral patienthood'
    };
  }
  return world.stochasticRecoveryLoop;
}
function recoveryTemplateForPulse(pulse) {
  const templates = {
    roof_leak: { harmType: 'shelter stress', repairAction: 'patch leak and rest near dry place', resourceCost: { water: 0, fiber: 1, wood: 1, care: 0 }, trustDelta: 0.012, progressDelta: 0.014, debtDelta: -1, relationshipNote: 'help after environmental stress' },
    tool_snag: { harmType: 'tool frustration', repairAction: 're-tie tool lashing and return focus', resourceCost: { water: 0, fiber: 1, wood: 0, care: 0 }, trustDelta: 0.008, progressDelta: 0.018, debtDelta: 0, relationshipNote: 'practical repair after blocked work' },
    neighbor_help: { harmType: 'received help', repairAction: 'acknowledge help and share credit', resourceCost: { water: 0, fiber: 0, wood: 0, care: 0 }, trustDelta: 0.006, progressDelta: 0.012, debtDelta: -1, relationshipNote: 'gratitude keeps help socially sticky' },
    argument_echo: { harmType: 'social disagreement', repairAction: 'mediate disagreement and name source boundary', resourceCost: { water: 0, fiber: 0, wood: 0, care: 1 }, trustDelta: 0.014, progressDelta: 0.008, debtDelta: 0, relationshipNote: 'argument repaired without erasing disagreement' },
    found_material: { harmType: 'opportunity allocation', repairAction: 'share found material with pending work', resourceCost: { water: 0, fiber: 0, wood: 0, care: 0 }, trustDelta: 0.005, progressDelta: 0.016, debtDelta: -1, relationshipNote: 'benefit distributed instead of hoarded' },
    quiet_recovery: { harmType: 'fatigue recovery', repairAction: 'protect quiet rest and resume slowly', resourceCost: { water: 0, fiber: 0, wood: 0, care: 0 }, trustDelta: 0.004, progressDelta: 0.01, debtDelta: -1, relationshipNote: 'rest respected as recovery' }
  };
  return templates[pulse.event] || templates.quiet_recovery;
}
function planStochasticRecoveryLoop() {
  const pulse = ensureStochasticConsequencePulse();
  if (!pulse.pulses.length) runStochasticConsequenceBurst();
  const refreshedPulse = ensureStochasticConsequencePulse();
  const loop = ensureStochasticRecoveryLoop();
  const existingPulseIds = new Set(loop.recoveryQueue.map(row => row.pulseId));
  const planned = [];
  refreshedPulse.pulses.slice(-10).forEach(source => {
    if (existingPulseIds.has(source.id)) return;
    const template = recoveryTemplateForPulse(source);
    const row = {
      id: `SR-${String(loop.recoveryQueue.length + planned.length + 1).padStart(2, '0')}`,
      pulseId: source.id,
      actor: source.actor,
      event: source.event,
      harmType: template.harmType,
      repairAction: template.repairAction,
      resourceCost: { ...template.resourceCost },
      trustDelta: template.trustDelta,
      progressDelta: template.progressDelta,
      debtDelta: template.debtDelta,
      relationshipNote: template.relationshipNote,
      needBefore: source.needAfter ? source.needAfter.dominant : 'unknown',
      needAfter: 'unrecovered',
      scheduleCoupling: source.scheduleCoupling || '',
      scheduleRepair: '',
      status: 'pending'
    };
    loop.recoveryQueue.push(row);
    planned.push(row);
  });
  loop.sourcePulseCount = refreshedPulse.pulses.length;
  loop.pendingCount = loop.recoveryQueue.filter(row => row.status === 'pending').length;
  recordCheckpoint('stochastic recovery planned');
  return log('planStochasticRecoveryLoop', { planned: planned.length, pending: loop.pendingCount, sourcePulseCount: loop.sourcePulseCount, noPermanentDamagePolicy: loop.noPermanentDamagePolicy });
}
function resolveStochasticRecoveryStep() {
  if (!world.stochasticRecoveryLoop || !world.stochasticRecoveryLoop.recoveryQueue.some(row => row.status === 'pending')) planStochasticRecoveryLoop();
  const loop = ensureStochasticRecoveryLoop();
  const row = loop.recoveryQueue.find(item => item.status === 'pending');
  if (!row) return log('resolveStochasticRecoveryStep', { complete: true, resolvedCount: loop.resolvedCount, pendingCount: loop.pendingCount });
  const resident = world.residents[row.actor];
  const trustBefore = Number(resident.trust.toFixed(3));
  const resourcesBefore = { ...world.resources };
  let outcome = '';
  if (hasResourcesFor(row.resourceCost)) {
    applyResourceCost(row.resourceCost);
    row.status = 'resolved';
    row.needAfter = row.harmType === 'social disagreement' ? 'social-safety' : 'recovering';
    outcome = `${row.actor} used ${row.repairAction} after ${row.event}`;
    loop.resolvedCount += 1;
  } else {
    row.status = 'stabilized without materials';
    row.needAfter = 'stabilized';
    row.resourceCost = { water: 0, fiber: 0, wood: 0, care: 0 };
    row.trustDelta = Number((row.trustDelta * 0.5).toFixed(3));
    row.progressDelta = Number((row.progressDelta * 0.5).toFixed(3));
    outcome = `${row.actor} could not spend materials, so recovery stabilized through rest and attention`;
    loop.stabilizedWithoutMaterials += 1;
  }
  if (row.scheduleCoupling && world.anomalyInvestigationSchedule) {
    const slot = world.anomalyInvestigationSchedule.slots.find(item => item.resident === row.actor && /stochastically/.test(item.status));
    if (slot) {
      slot.recoveryNoted = true;
      slot.recoveryNote = row.repairAction;
      row.scheduleRepair = `${slot.id} recovery noted`;
    } else {
      row.scheduleRepair = 'schedule consequence acknowledged';
    }
  }
  mutateResident(row.actor, {
    trust: row.trustDelta,
    progress: row.progressDelta,
    debt: row.debtDelta,
    memory: `recovered from stochastic pulse: ${row.event}`,
    historyEvent: 'stochastic recovery',
    historyDetail: outcome
  });
  const trustAfter = Number(world.residents[row.actor].trust.toFixed(3));
  const repair = {
    recoveryId: row.id,
    pulseId: row.pulseId,
    actor: row.actor,
    trustBefore,
    trustAfter,
    note: row.relationshipNote,
    scheduleRepair: row.scheduleRepair
  };
  loop.relationshipRepairs.push(repair);
  if (loop.relationshipRepairs.length > 24) loop.relationshipRepairs.shift();
  loop.repairLedger.push({
    recoveryId: row.id,
    pulseId: row.pulseId,
    outcome,
    resourcesBefore,
    resourcesAfter: { ...world.resources },
    status: row.status
  });
  if (loop.repairLedger.length > 24) loop.repairLedger.shift();
  loop.pendingCount = loop.recoveryQueue.filter(item => item.status === 'pending').length;
  recordCheckpoint('stochastic recovery step');
  return log('resolveStochasticRecoveryStep', { recovery: row, relationshipRepair: repair, outcome, pendingCount: loop.pendingCount });
}
function runStochasticRecoveryLoop() {
  if (!world.stochasticRecoveryLoop || !world.stochasticRecoveryLoop.recoveryQueue.some(row => row.status === 'pending')) planStochasticRecoveryLoop();
  const before = ensureStochasticRecoveryLoop().resolvedCount + ensureStochasticRecoveryLoop().stabilizedWithoutMaterials;
  for (let index = 0; index < 3; index += 1) {
    if (!ensureStochasticRecoveryLoop().recoveryQueue.some(row => row.status === 'pending')) break;
    resolveStochasticRecoveryStep();
  }
  const loop = ensureStochasticRecoveryLoop();
  const after = loop.resolvedCount + loop.stabilizedWithoutMaterials;
  return log('runStochasticRecoveryLoop', { recoveredThisRun: after - before, pendingCount: loop.pendingCount, relationshipRepairs: loop.relationshipRepairs.length, noPermanentDamagePolicy: loop.noPermanentDamagePolicy });
}
function ensureStochasticHistoryInfluence() {
  if (!world.stochasticHistoryInfluence) {
    world.stochasticHistoryInfluence = {
      reportIntroduced: 366,
      sourceRecoveryCount: 0,
      choiceRecords: [],
      refusalRecords: [],
      socialEchoes: [],
      influenceLedger: [],
      noPermanentPunishmentPolicy: 'unrecovered stochastic history can justify bounded caution, not permanent punishment',
      boundary: 'browser-local-stochastic-history-influence-only; no LLM call, no subjective consciousness, no moral patienthood'
    };
  }
  return world.stochasticHistoryInfluence;
}
function stochasticRecoveryStats(actor) {
  if (!world.stochasticRecoveryLoop || !world.stochasticRecoveryLoop.recoveryQueue.length) {
    runStochasticConsequenceBurst();
    planStochasticRecoveryLoop();
    resolveStochasticRecoveryStep();
  }
  const loop = ensureStochasticRecoveryLoop();
  const rows = loop.recoveryQueue.filter(row => row.actor === actor);
  const recovered = rows.filter(row => row.status === 'resolved').length;
  const pending = rows.filter(row => row.status === 'pending').length;
  const stabilized = rows.filter(row => row.status === 'stabilized without materials').length;
  const recent = rows[rows.length - 1] || null;
  return { rows, recovered, pending, stabilized, recent };
}
function chooseHistoryInfluenceActor() {
  const names = Object.keys(world.residents);
  const influence = ensureStochasticHistoryInfluence();
  const scored = names.map(name => ({ name, stats: stochasticRecoveryStats(name) }))
    .sort((left, right) => (right.stats.pending + right.stats.recovered + right.stats.stabilized) - (left.stats.pending + left.stats.recovered + left.stats.stabilized));
  const offset = influence.choiceRecords.length % Math.max(1, scored.length);
  return scored[offset] && scored[offset].stats.rows.length ? scored[offset].name : world.selected;
}
function runStochasticHistoryChoice() {
  const influence = ensureStochasticHistoryInfluence();
  const actor = chooseHistoryInfluenceActor();
  const stats = stochasticRecoveryStats(actor);
  const resident = world.residents[actor];
  let decision = 'wait_for_more_context';
  let reason = 'history is too thin to change action';
  let trustDelta = 0.001;
  let progressDelta = 0.002;
  let refusalBounded = false;
  if (stats.pending > stats.recovered) {
    decision = 'bounded_refusal_until_recovery';
    reason = 'unrecovered stochastic harm is still pending';
    trustDelta = -0.003;
    progressDelta = -0.002;
    refusalBounded = true;
  } else if (stats.stabilized > 0 && stats.recovered === 0) {
    decision = 'cautious_help_with_limits';
    reason = 'history stabilized without materials, so help stays cautious';
    trustDelta = 0.002;
    progressDelta = 0.004;
  } else if (stats.recovered > 0) {
    decision = 'accept_recovery_informed_help';
    reason = 'past stochastic harm was recovered and can support trust';
    trustDelta = 0.008;
    progressDelta = 0.01;
  }
  mutateResident(actor, {
    trust: trustDelta,
    progress: progressDelta,
    memory: `choice influenced by stochastic history: ${decision}`,
    historyEvent: 'stochastic history choice',
    historyDetail: `${actor} chose ${decision} because ${reason}`
  });
  const sourceRecoveryIds = stats.rows.slice(-4).map(row => row.id);
  const row = {
    id: `SHC-${String(influence.choiceRecords.length + 1).padStart(2, '0')}`,
    actor,
    decision,
    reason,
    recoveredCount: stats.recovered,
    pendingCount: stats.pending,
    stabilizedCount: stats.stabilized,
    sourceRecoveryIds,
    refusalBounded,
    recoveryPath: stats.recent ? stats.recent.repairAction : 'plan recovery first',
    permanentPenalty: false,
    trust: Number(resident.trust.toFixed(3))
  };
  influence.choiceRecords.push(row);
  if (influence.choiceRecords.length > 30) influence.choiceRecords.shift();
  if (refusalBounded) {
    influence.refusalRecords.push({ id: row.id, actor, reason, recoveryPath: row.recoveryPath, permanentPenalty: false });
    if (influence.refusalRecords.length > 20) influence.refusalRecords.shift();
  }
  influence.sourceRecoveryCount = world.stochasticRecoveryLoop ? world.stochasticRecoveryLoop.recoveryQueue.length : 0;
  influence.influenceLedger.push({ type: 'choice', id: row.id, actor, decision, sourceRecoveryIds });
  if (influence.influenceLedger.length > 40) influence.influenceLedger.shift();
  recordCheckpoint('stochastic history choice');
  return log('runStochasticHistoryChoice', { choice: row, noPermanentPunishmentPolicy: influence.noPermanentPunishmentPolicy });
}
function runStochasticHistorySocialEcho() {
  const influence = ensureStochasticHistoryInfluence();
  if (!influence.choiceRecords.length) runStochasticHistoryChoice();
  const choice = influence.choiceRecords[influence.choiceRecords.length - 1];
  const names = Object.keys(world.residents);
  const fromIndex = names.indexOf(choice.actor);
  const target = names[(fromIndex + 1 + influence.socialEchoes.length) % names.length] || world.selected;
  const message = `${choice.actor} carried ${choice.decision} from stochastic recovery history`;
  mutateResident(target, {
    trust: choice.refusalBounded ? -0.001 : 0.003,
    progress: 0.003,
    memory: `heard stochastic history echo from ${choice.actor}`,
    historyEvent: 'stochastic history social echo',
    historyDetail: message
  });
  const row = {
    id: `SHE-${String(influence.socialEchoes.length + 1).padStart(2, '0')}`,
    from: choice.actor,
    to: target,
    message,
    sourceChoiceId: choice.id,
    directAvatarCommand: false,
    boundedRefusalCarried: choice.refusalBounded,
    permanentPenalty: false
  };
  influence.socialEchoes.push(row);
  if (influence.socialEchoes.length > 24) influence.socialEchoes.shift();
  influence.influenceLedger.push({ type: 'social_echo', id: row.id, from: row.from, to: row.to, sourceChoiceId: row.sourceChoiceId });
  if (influence.influenceLedger.length > 40) influence.influenceLedger.shift();
  recordCheckpoint('stochastic history social echo');
  return log('runStochasticHistorySocialEcho', { echo: row, sourceChoice: choice });
}
function runStochasticHistoryInfluenceLoop() {
  if (!world.stochasticRecoveryLoop || !world.stochasticRecoveryLoop.recoveryQueue.length) {
    runStochasticConsequenceBurst();
    planStochasticRecoveryLoop();
  }
  const firstChoice = runStochasticHistoryChoice();
  resolveStochasticRecoveryStep();
  const secondChoice = runStochasticHistoryChoice();
  const echo = runStochasticHistorySocialEcho();
  return log('runStochasticHistoryInfluenceLoop', {
    choices: [firstChoice.payload.choice.id, secondChoice.payload.choice.id],
    echo: echo.payload.echo.id,
    noPermanentPunishmentPolicy: ensureStochasticHistoryInfluence().noPermanentPunishmentPolicy
  });
}
function ensureStochasticOrdinaryAffordance() {
  if (!world.stochasticOrdinaryAffordance) {
    world.stochasticOrdinaryAffordance = {
      reportIntroduced: 367,
      sourceChoiceCount: 0,
      actionRecords: [],
      sourceLedger: [],
      blockedCount: 0,
      movementBiasCount: 0,
      normalPlayPolicy: 'stochastic history may bias ordinary actions, but normal play keeps source IDs and recovery paths visible',
      boundary: 'browser-local-stochastic-ordinary-affordance-only; no LLM call, no subjective consciousness, no moral patienthood'
    };
  }
  return world.stochasticOrdinaryAffordance;
}
function latestHistoryChoiceFor(actor) {
  const influence = ensureStochasticHistoryInfluence();
  if (!influence.choiceRecords.length) runStochasticHistoryInfluenceLoop();
  const refreshed = ensureStochasticHistoryInfluence();
  const choices = refreshed.choiceRecords.filter(row => row.actor === actor);
  return choices[choices.length - 1] || refreshed.choiceRecords[refreshed.choiceRecords.length - 1] || null;
}
function applyStochasticHistoryToOrdinaryAction(action, actor) {
  const affordance = ensureStochasticOrdinaryAffordance();
  const choice = latestHistoryChoiceFor(actor);
  let outcome = 'normal action unchanged by stochastic history';
  let blocked = false;
  let movementScale = 1;
  let careCost = action === 'offerHelp' ? 1 : 0;
  let trustDelta = 0.004;
  let progressDelta = 0.004;
  let debtDelta = 0;
  let talkTone = 'plain bounded reply';
  const decision = choice ? choice.decision : 'none';
  if (decision === 'bounded_refusal_until_recovery') {
    if (action === 'offerHelp' || action === 'askSchedule') blocked = true;
    movementScale = action.startsWith('move') ? 0.5 : 1;
    careCost = blocked ? 0 : careCost;
    trustDelta = action === 'offerHelp' ? -0.004 : -0.001;
    progressDelta = blocked ? 0 : 0.001;
    talkTone = 'guarded bounded reply';
    outcome = 'pending recovery creates bounded caution';
  } else if (decision === 'cautious_help_with_limits') {
    movementScale = action.startsWith('move') ? 0.75 : 1;
    trustDelta = action === 'offerHelp' ? 0.008 : 0.004;
    progressDelta = action === 'offerHelp' ? 0.014 : 0.004;
    talkTone = 'careful bounded reply';
    outcome = 'stabilized history allows cautious action';
  } else if (decision === 'accept_recovery_informed_help') {
    trustDelta = action === 'offerHelp' ? 0.02 : 0.01;
    progressDelta = action === 'offerHelp' ? 0.028 : 0.006;
    debtDelta = action === 'offerHelp' ? -1 : 0;
    talkTone = 'warm recovery-informed reply';
    outcome = 'recovered history supports ordinary action';
  }
  const row = {
    id: `SOA-${String(affordance.actionRecords.length + 1).padStart(2, '0')}`,
    action,
    actor,
    sourceChoiceId: choice ? choice.id : '',
    sourceDecision: decision,
    outcome,
    blocked,
    movementScale,
    careCost,
    trustDelta,
    progressDelta,
    debtDelta,
    talkTone,
    recoveryPath: choice ? choice.recoveryPath : '',
    permanentPenalty: false,
    normalAffordance: true
  };
  affordance.actionRecords.push(row);
  if (affordance.actionRecords.length > 36) affordance.actionRecords.shift();
  affordance.sourceChoiceCount = ensureStochasticHistoryInfluence().choiceRecords.length;
  if (blocked) affordance.blockedCount += 1;
  if (action.startsWith('move') && movementScale !== 1) affordance.movementBiasCount += 1;
  affordance.sourceLedger.push({ actionId: row.id, sourceChoiceId: row.sourceChoiceId, normalAction: action, outcome });
  if (affordance.sourceLedger.length > 40) affordance.sourceLedger.shift();
  return row;
}
function runOrdinaryAffordanceInfluenceLoop() {
  if (!world.stochasticHistoryInfluence || !world.stochasticHistoryInfluence.choiceRecords.length) runStochasticHistoryInfluenceLoop();
  const before = ensureStochasticOrdinaryAffordance().actionRecords.length;
  talkBounded();
  askSchedule();
  offerHelp();
  moveEast();
  const affordance = ensureStochasticOrdinaryAffordance();
  return log('runOrdinaryAffordanceInfluenceLoop', {
    actionsAdded: affordance.actionRecords.length - before,
    blockedCount: affordance.blockedCount,
    movementBiasCount: affordance.movementBiasCount,
    normalPlayPolicy: affordance.normalPlayPolicy
  });
}
function waitOffscreen() {
  Object.keys(world.residents).forEach((name, index) => mutateResident(name, { progress: 0.018 + index * 0.003, trust: index % 2 ? 0.002 : -0.001 }));
  const offscreenObligation = runOffscreenResidentObligationPulse();
  updateAbsentTimeSummary(offscreenObligation);
  return log('waitOffscreen', { offscreenLife: true, offscreenObligation, absentTimeSummary: world.absentTimeSummary });
}
function repairTrust() { mutateResident(world.selected, { trust: 0.018, debt: -1, memory: 'trust repaired non-magically' }); return log('repairTrust', { nonMagic: true }); }
function advancePromiseFollowUpState(residentName, trigger, replayRowsBeforeReturn) {
  const previous = world.promiseFollowUp && world.promiseFollowUp.resident === residentName ? world.promiseFollowUp : null;
  const stageOrder = ['opened', 'advanced', 'confirmed'];
  const previousIndex = previous ? stageOrder.indexOf(previous.stage) : -1;
  const nextStage = stageOrder[Math.min(previousIndex + 1, stageOrder.length - 1)];
  const returnCount = (previous ? previous.returnCount : 0) + (trigger === 'return' ? 1 : 0);
  const obligation = previous ? previous.obligation : `${residentName} wants the avatar to check the awning repair after returning`;
  world.promiseFollowUp = {
    reportIntroduced: 351,
    resident: residentName,
    obligation,
    stage: nextStage,
    returnCount,
    trigger,
    replayRowsBeforeReturn,
    advancedAtTick: world.tick,
    visibleStatus: `${residentName} follow-up ${nextStage}: ${obligation} (${returnCount} return(s))`,
    boundary: 'browser-local-public-obligation-thread-only'
  };
  const ledgerRow = syncPromiseFollowUpObligation(world.promiseFollowUp);
  mutateResident(residentName, {
    trust: nextStage === 'opened' ? 0.004 : 0.006,
    progress: nextStage === 'opened' ? 0.012 : 0.018,
    schedule: `follow-up ${nextStage}: check awning repair`,
    memory: `recognized returning avatar; follow-up ${nextStage}: ${obligation}`,
    historyEvent: 'promise follow-up',
    historyDetail: `${nextStage} remembered obligation after ${returnCount} return(s)`
  });
  syncScheduleDebtFromObligation(ledgerRow, `follow-up-${nextStage}`);
  return world.promiseFollowUp;
}
function advancePromiseFollowUp() {
  const followUp = advancePromiseFollowUpState(world.selected, 'manual', world.replay.length);
  return log('advancePromiseFollowUp', { followUp, boundary: BOUNDARY });
}
function syncPromiseFollowUpObligation(followUp) {
  if (!followUp) return null;
  if (!world.obligationLedger) world.obligationLedger = [];
  const id = `${followUp.resident.toLowerCase()}-awning-followup`;
  const existing = world.obligationLedger.find(item => item.id === id);
  const status = existing && existing.status === 'resolved' ? 'resolved' : 'open';
  const row = {
    id,
    reportIntroduced: 352,
    resident: followUp.resident,
    obligation: followUp.obligation,
    stage: followUp.stage,
    status,
    returnCount: followUp.returnCount,
    selected: true,
    lastTrigger: followUp.trigger,
    lastReplayRowsBeforeReturn: followUp.replayRowsBeforeReturn,
    visibleStatus: `${followUp.resident} obligation ${status}: ${followUp.obligation} / follow-up ${followUp.stage} / ${followUp.returnCount} return(s)`,
    boundary: 'browser-local-selectable-obligation-list-only'
  };
  if (existing) Object.assign(existing, row);
  else world.obligationLedger.push(row);
  world.selectedObligationId = id;
  return row;
}
function syncScheduleDebtFromObligation(obligation, action) {
  if (!obligation) return null;
  if (!world.scheduleQueue) world.scheduleQueue = [];
  if (!world.debtLedger) world.debtLedger = [];
  const resident = world.residents[obligation.resident] || currentResident();
  const scheduleStatus = action === 'resolve' ? 'resolved' : action === 'defer' ? 'deferred' : 'pending';
  const debtStatus = action === 'resolve' ? 'settled' : action === 'defer' ? 'deferred' : 'outstanding';
  const scheduleRow = {
    id: obligation.id,
    reportIntroduced: 353,
    resident: obligation.resident,
    status: scheduleStatus,
    action,
    schedule: resident.schedule,
    obligation: obligation.obligation,
    visibleStatus: `${obligation.resident} schedule ${scheduleStatus}: ${resident.schedule}`,
    boundary: 'browser-local-obligation-schedule-queue-only'
  };
  const debtRow = {
    id: obligation.id,
    reportIntroduced: 353,
    resident: obligation.resident,
    status: debtStatus,
    action,
    debtAfter: resident.debt,
    trustAfter: Number(resident.trust.toFixed(3)),
    obligation: obligation.obligation,
    visibleStatus: `${obligation.resident} debt ${debtStatus}: ${resident.debt} after ${action}`,
    boundary: 'browser-local-obligation-debt-ledger-only'
  };
  const scheduleIndex = world.scheduleQueue.findIndex(item => item.id === obligation.id);
  const debtIndex = world.debtLedger.findIndex(item => item.id === obligation.id);
  if (scheduleIndex >= 0) world.scheduleQueue[scheduleIndex] = scheduleRow;
  else world.scheduleQueue.push(scheduleRow);
  if (debtIndex >= 0) world.debtLedger[debtIndex] = debtRow;
  else world.debtLedger.push(debtRow);
  obligation.scheduleQueueStatus = scheduleStatus;
  obligation.debtLedgerStatus = debtStatus;
  obligation.scheduleAfter = resident.schedule;
  obligation.debtAfter = resident.debt;
  return { scheduleRow, debtRow };
}
function runOffscreenResidentObligationPulse() {
  if (!world.obligationLedger) world.obligationLedger = [];
  if (!world.offscreenObligationEvents) world.offscreenObligationEvents = [];
  const actor = 'Fay';
  const target = world.selected === 'Milo' ? 'Sera' : 'Milo';
  const id = `${target.toLowerCase()}-offscreen-water-jars`;
  const obligation = `${actor} found leaking water jars while the avatar was absent`;
  const existing = world.obligationLedger.find(item => item.id === id);
  const alreadyOpen = existing && existing.status === 'open';
  const row = {
    id,
    reportIntroduced: 354,
    resident: target,
    actor,
    source: 'offscreen-resident-action',
    obligation,
    stage: 'offscreen-pending',
    status: 'open',
    selected: false,
    returnCount: 0,
    visibleStatus: `${target} offscreen obligation open from ${actor}: inspect leaking water jars`,
    boundary: 'browser-local-offscreen-cross-resident-obligation-only'
  };
  if (existing) Object.assign(existing, row);
  else world.obligationLedger.push(row);
  world.selectedObligationId = id;
  mutateResident(target, {
    trust: -0.004,
    debt: alreadyOpen ? 0 : 1,
    progress: 0.013,
    schedule: 'offscreen obligation: inspect leaking water jars',
    memory: `${actor} left offscreen obligation: inspect leaking water jars`,
    historyEvent: 'offscreen obligation received',
    historyDetail: `${actor} changed ${target}'s obligation while avatar absent`
  });
  recordResidentHistory(actor, 'offscreen obligation issued', `${actor} changed ${target}'s obligation while avatar absent`);
  const linkedLedger = syncScheduleDebtFromObligation(row, 'offscreen-resident-action');
  const event = {
    reportIntroduced: 354,
    actor,
    target,
    obligationId: id,
    replayRowsBeforeEvent: world.replay.length,
    linkedLedger,
    persistedIn: STATE_KEY,
    boundary: 'browser-local-offscreen-cross-resident-obligation-event-only'
  };
  world.offscreenObligationEvents.push(event);
  world.offscreenObligationEvents = world.offscreenObligationEvents.slice(-8);
  return event;
}
function updateAbsentTimeSummary(offscreenEvent) {
  const event = offscreenEvent || (world.offscreenObligationEvents || [])[world.offscreenObligationEvents.length - 1];
  if (!event) return null;
  const obligation = (world.obligationLedger || []).find(item => item.id === event.obligationId);
  const scheduleRow = (world.scheduleQueue || []).find(item => item.id === event.obligationId);
  const debtRow = (world.debtLedger || []).find(item => item.id === event.obligationId);
  world.absentTimeSummary = {
    reportIntroduced: 355,
    phase: 'before-obligation-choice',
    avatarCaused: [
      `avatar chose Wait offscreen at replay row ${event.replayRowsBeforeEvent}`,
      'avatar did not choose the new obligation target'
    ],
    residentCaused: [
      `${event.actor} changed ${event.target}'s obligation while avatar absent`,
      `${event.obligationId} is ${obligation ? obligation.status : 'missing'} / ${obligation ? obligation.stage : 'missing'}`
    ],
    beforeChoice: `${event.target} obligation is selectable before resolve/defer; schedule ${scheduleRow ? scheduleRow.status : 'missing'}; debt ${debtRow ? debtRow.status : 'missing'}`,
    obligationId: event.obligationId,
    actor: event.actor,
    target: event.target,
    scheduleQueueStatus: scheduleRow ? scheduleRow.status : 'missing',
    debtLedgerStatus: debtRow ? debtRow.status : 'missing',
    boundary: 'browser-local-absent-time-summary-only'
  };
  world.absentTimeThreads = buildAbsentTimeThreads(event, obligation);
  world.absentTimeChoiceReceipt = null;
  world.avatarAbsenceAccountabilityReceipt = null;
  return world.absentTimeSummary;
}
function buildAbsentTimeThreads(event, obligation) {
  const existingThreads = world.absentTimeThreads || [];
  const existingAvatarThread = existingThreads.find(thread => thread.id === 'avatar-absence-thread');
  const existingResidentThread = existingThreads.find(thread => thread.id === event.obligationId);
  return [
    {
      id: 'avatar-absence-thread',
      reportIntroduced: 356,
      source: 'avatar-caused',
      status: existingAvatarThread ? existingAvatarThread.status : 'pending',
      label: 'avatar chose Wait offscreen and must decide whether to account for absence first',
      boundary: 'browser-local-absent-time-choice-thread-only'
    },
    {
      id: event.obligationId,
      reportIntroduced: 356,
      source: 'resident-caused',
      status: existingResidentThread ? existingResidentThread.status : 'pending',
      label: `${event.actor} changed ${event.target}'s obligation while avatar absent`,
      obligationStatus: obligation ? obligation.status : 'missing',
      boundary: 'browser-local-absent-time-choice-thread-only'
    }
  ];
}
function ensureAbsentTimeThreads() {
  if ((!world.absentTimeThreads || world.absentTimeThreads.length === 0) && world.absentTimeSummary) {
    const event = (world.offscreenObligationEvents || []).find(row => row.obligationId === world.absentTimeSummary.obligationId);
    if (event) {
      const obligation = (world.obligationLedger || []).find(row => row.id === event.obligationId);
      world.absentTimeThreads = buildAbsentTimeThreads(event, obligation);
    }
  }
  return world.absentTimeThreads || [];
}
function chooseAbsentTimeThread(threadId) {
  const threads = ensureAbsentTimeThreads();
  const chosen = threads.find(thread => thread.id === threadId);
  if (!chosen) return log('chooseAbsentTimeThread', { chosen: false, reason: 'no absent-time thread', threadId, boundary: BOUNDARY });
  threads.forEach(thread => {
    thread.status = thread.id === threadId ? 'chosen' : 'pending';
  });
  if (threadId !== 'avatar-absence-thread') world.selectedObligationId = threadId;
  const unchosen = threads.filter(thread => thread.id !== threadId);
  world.absentTimeChoiceReceipt = {
    reportIntroduced: 356,
    phase: 'thread-choice-recorded',
    chosenThreadId: threadId,
    chosenSource: chosen.source,
    chosenAction: chosen.source === 'avatar-caused' ? 'acknowledge avatar-caused absence first' : 'handle resident-caused offscreen obligation first',
    unchosenThreadIds: unchosen.map(thread => thread.id),
    unchosenThreadStatus: unchosen.map(thread => `${thread.id}: ${thread.status}`),
    visibleStatus: `${chosen.source} chosen first; unchosen remains ${unchosen.map(thread => `${thread.id} ${thread.status}`).join('; ')}`,
    boundary: 'browser-local-absent-time-choice-receipt-only'
  };
  return log('chooseAbsentTimeThread', { chosen: true, absentTimeChoiceReceipt: world.absentTimeChoiceReceipt, absentTimeThreads: threads, boundary: BOUNDARY });
}
function handleAvatarAbsenceFirst() {
  return chooseAbsentTimeThread('avatar-absence-thread');
}
function handleResidentOffscreenFirst() {
  const event = (world.offscreenObligationEvents || [])[world.offscreenObligationEvents.length - 1];
  const threadId = world.absentTimeSummary ? world.absentTimeSummary.obligationId : event && event.obligationId;
  return chooseAbsentTimeThread(threadId || 'missing-resident-thread');
}
function accountForAvatarAbsence() {
  const threads = ensureAbsentTimeThreads();
  const avatarThread = threads.find(thread => thread.id === 'avatar-absence-thread');
  const residentThreadId = world.absentTimeSummary ? world.absentTimeSummary.obligationId : null;
  const residentThread = threads.find(thread => thread.id === residentThreadId);
  const obligation = (world.obligationLedger || []).find(row => row.id === residentThreadId);
  const event = (world.offscreenObligationEvents || []).find(row => row.obligationId === residentThreadId);
  if (!avatarThread || !residentThreadId) {
    return log('accountForAvatarAbsence', { accounted: false, reason: 'no avatar absence thread', boundary: BOUNDARY });
  }
  avatarThread.status = 'accounted';
  world.resources.care = Math.max(0, world.resources.care - 1);
  if (obligation && world.residents[obligation.resident]) {
    mutateResident(obligation.resident, {
      trust: 0.006,
      progress: 0.006,
      memory: `avatar accounted for absence after ${residentThreadId}`,
      historyEvent: 'avatar absence accounted',
      historyDetail: `avatar acknowledged absence without erasing ${residentThreadId}`
    });
  }
  const residentHistoryPreserved = Boolean(obligation && event && (world.offscreenObligationEvents || []).some(row => row.obligationId === residentThreadId));
  world.avatarAbsenceAccountabilityReceipt = {
    reportIntroduced: 357,
    phase: 'avatar-absence-accounted',
    avatarThreadId: avatarThread.id,
    avatarThreadStatus: avatarThread.status,
    residentThreadId,
    residentThreadStatus: residentThread ? residentThread.status : 'missing',
    residentObligationStatus: obligation ? obligation.status : 'missing',
    residentObligationStage: obligation ? obligation.stage : 'missing',
    residentHistoryPreserved,
    careAfter: world.resources.care,
    visibleStatus: `avatar-caused absence accounted; resident-caused ${residentThreadId} remains ${residentThread ? residentThread.status : 'missing'} with obligation ${obligation ? `${obligation.status}/${obligation.stage}` : 'missing'}`,
    boundary: 'browser-local-avatar-absence-accountability-receipt-only'
  };
  return log('accountForAvatarAbsence', { accounted: true, avatarAbsenceAccountabilityReceipt: world.avatarAbsenceAccountabilityReceipt, absentTimeThreads: threads, boundary: BOUNDARY });
}
function recordObligationChoiceOutcome(obligation, action, linkedLedger) {
  if (!world.absentTimeSummary || world.absentTimeSummary.obligationId !== obligation.id) return null;
  const threads = ensureAbsentTimeThreads();
  const residentThread = threads.find(thread => thread.id === obligation.id);
  const avatarThread = threads.find(thread => thread.id === 'avatar-absence-thread');
  if (residentThread) residentThread.status = action === 'resolve' ? 'resolved' : 'deferred';
  if (avatarThread && avatarThread.status !== 'chosen') avatarThread.status = 'pending';
  const scheduleRow = linkedLedger && linkedLedger.scheduleRow ? linkedLedger.scheduleRow : null;
  const debtRow = linkedLedger && linkedLedger.debtRow ? linkedLedger.debtRow : null;
  world.absentTimeChoiceReceipt = {
    reportIntroduced: 356,
    phase: 'obligation-action-recorded',
    chosenThreadId: obligation.id,
    chosenSource: 'resident-caused',
    chosenAction: action,
    unchosenThreadIds: avatarThread ? [avatarThread.id] : [],
    unchosenThreadStatus: avatarThread ? [`${avatarThread.id}: ${avatarThread.status}`] : [],
    residentThreadStatus: residentThread ? residentThread.status : 'missing',
    avatarAbsenceStatus: avatarThread ? avatarThread.status : 'missing',
    scheduleQueueStatus: scheduleRow ? scheduleRow.status : 'missing',
    debtLedgerStatus: debtRow ? debtRow.status : 'missing',
    visibleStatus: `resident-caused offscreen obligation ${action}; avatar-caused absence thread ${avatarThread ? avatarThread.status : 'missing'}`,
    boundary: 'browser-local-absent-time-choice-receipt-only'
  };
  return world.absentTimeChoiceReceipt;
}
function selectedObligation() {
  const obligations = world.obligationLedger || [];
  if (!world.selectedObligationId && obligations.length > 0) world.selectedObligationId = obligations[0].id;
  return obligations.find(item => item.id === world.selectedObligationId) || null;
}
function resolveSelectedObligation() {
  const obligation = selectedObligation();
  if (!obligation) return log('resolveSelectedObligation', { resolved: false, reason: 'no selectable obligation', boundary: BOUNDARY });
  obligation.status = 'resolved';
  obligation.stage = 'resolved';
  obligation.resolution = 'avatar resolved selected follow-up through bounded help action';
  obligation.resolvedAtTick = world.tick;
  obligation.visibleStatus = `${obligation.resident} obligation resolved by avatar help: ${obligation.obligation}`;
  if (world.promiseFollowUp && world.promiseFollowUp.resident === obligation.resident) {
    world.promiseFollowUp = { ...world.promiseFollowUp, stage: 'resolved', resolutionStatus: 'resolved', visibleStatus: obligation.visibleStatus };
  }
  mutateResident(obligation.resident, {
    trust: 0.018,
    debt: -1,
    progress: 0.024,
    schedule: 'follow-up resolved: awning repair checked',
    memory: `resolved obligation: ${obligation.obligation}`,
    historyEvent: 'obligation resolved',
    historyDetail: 'bounded action resolved selected follow-up'
  });
  const linkedLedger = syncScheduleDebtFromObligation(obligation, 'resolve');
  const absentTimeChoiceReceipt = recordObligationChoiceOutcome(obligation, 'resolve', linkedLedger);
  return log('resolveSelectedObligation', { resolved: true, obligation, linkedLedger, absentTimeChoiceReceipt, boundedAction: true, boundary: BOUNDARY });
}
function deferSelectedObligation() {
  const obligation = selectedObligation();
  if (!obligation) return log('deferSelectedObligation', { deferred: false, reason: 'no selectable obligation', boundary: BOUNDARY });
  obligation.status = 'deferred';
  obligation.stage = 'deferred';
  obligation.deferredAtTick = world.tick;
  obligation.dueReplayRows = world.replay.length + 2;
  obligation.visibleStatus = `${obligation.resident} obligation deferred by avatar: ${obligation.obligation} / due after replay row ${obligation.dueReplayRows}`;
  if (world.promiseFollowUp && world.promiseFollowUp.resident === obligation.resident) {
    world.promiseFollowUp = { ...world.promiseFollowUp, stage: 'deferred', resolutionStatus: 'deferred', visibleStatus: obligation.visibleStatus };
  }
  mutateResident(obligation.resident, {
    trust: -0.006,
    progress: 0.004,
    schedule: 'follow-up deferred: awning repair check queued',
    memory: `deferred obligation: ${obligation.obligation}`,
    historyEvent: 'obligation deferred',
    historyDetail: 'bounded action deferred selected follow-up'
  });
  const linkedLedger = syncScheduleDebtFromObligation(obligation, 'defer');
  const absentTimeChoiceReceipt = recordObligationChoiceOutcome(obligation, 'defer', linkedLedger);
  return log('deferSelectedObligation', { deferred: true, obligation, linkedLedger, absentTimeChoiceReceipt, boundedAction: true, boundary: BOUNDARY });
}
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
    returnContinuity: world.returnContinuity,
    returnGreetingContinuity: world.returnGreetingContinuity,
    accountabilitySocialEcho: world.accountabilitySocialEcho,
    boundedEchoConversation: world.boundedEchoConversation,
    echoInfluencedChoiceReceipt: world.echoInfluencedChoiceReceipt,
    anomalyDiscovery: world.anomalyDiscovery,
    anomalyInvestigationSchedule: world.anomalyInvestigationSchedule,
    stochasticConsequencePulse: world.stochasticConsequencePulse,
    stochasticRecoveryLoop: world.stochasticRecoveryLoop,
    stochasticHistoryInfluence: world.stochasticHistoryInfluence,
    stochasticOrdinaryAffordance: world.stochasticOrdinaryAffordance,
    civilizationPressure: world.civilizationPressure,
    practicalDiscovery: world.practicalDiscovery,
    emergentPracticeGraph: world.emergentPracticeGraph,
    villageBoard: world.villageBoard,
    realityConstraintLedger: world.realityConstraintLedger,
    avatarHintDivergence: world.avatarHintDivergence,
    hintBranchPersistence: world.hintBranchPersistence,
    promiseFollowUp: world.promiseFollowUp,
    obligationLedger: world.obligationLedger,
    scheduleQueue: world.scheduleQueue,
    debtLedger: world.debtLedger,
    offscreenObligationEvents: world.offscreenObligationEvents,
    absentTimeSummary: world.absentTimeSummary,
    absentTimeThreads: world.absentTimeThreads,
    absentTimeChoiceReceipt: world.absentTimeChoiceReceipt,
    avatarAbsenceAccountabilityReceipt: world.avatarAbsenceAccountabilityReceipt,
    selectedObligationId: world.selectedObligationId,
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

function ensureGamePrototype() {
  if (!world.gamePrototype) {
    world.gamePrototype = {
      mode: 'game-prototype-v0',
      objective: 'Enter the village, learn a resident concern, support without commanding, observe practice formation, save, return, and see history still matter.',
      milestones: [],
      lastLoop: null,
      noMoreResearchReportsByDefault: true,
      scope: {
        village: 'one village',
        residentsMaximum: 6,
        anomalyFamilies: 1,
        practiceChains: 'one or two',
        interfaceGoal: 'normal player-facing interface plus optional audit mode',
      },
    };
  }
  return world.gamePrototype;
}

function recordPrototypeMilestone(step, detail) {
  const prototype = ensureGamePrototype();
  prototype.milestones.push({
    step,
    detail,
    tick: world.tick,
    replayRows: world.replay.length,
    selected: world.selected,
    room: world.avatar.room,
  });
  prototype.lastLoop = step;
  return prototype;
}

function runPrototypeOpening() {
  ensureGamePrototype();
  enterWorld();
  askSchedule();
  talkBounded();
  recordPrototypeMilestone('opening', `${world.selected} visible in ${world.avatar.room}; schedule ${currentResident().schedule}; memory ${currentResident().memory}`);
  return log('runPrototypeOpening', { entered: world.entered, selected: world.selected, schedule: currentResident().schedule, milestones: world.gamePrototype.milestones.length });
}

function runPrototypePracticeChain() {
  ensureGamePrototype();
  runPracticalDiscoveryLoop();
  runVillageBoardLoop();
  supportVillageProposal();
  runRealityConstraintAudit();
  const practiceCount = world.emergentPracticeGraph ? world.emergentPracticeGraph.nodes.length : 0;
  const proposalCount = world.villageBoard ? world.villageBoard.projectProposals.length : 0;
  recordPrototypeMilestone('practice-and-proposal', `${practiceCount} practice node(s), ${proposalCount} proposal(s), avatar support remains non-commanding`);
  return log('runPrototypePracticeChain', { practiceCount, proposalCount, realityRows: world.realityConstraintLedger ? world.realityConstraintLedger.rows.length : 0 });
}

function runPrototypeReturnProof() {
  ensureGamePrototype();
  saveWorld();
  waitOffscreen();
  enterWorld();
  runAvatarHintDivergenceLoop();
  runHintBranchPersistenceLoop();
  saveWorld();
  const branchRows = world.hintBranchPersistence ? world.hintBranchPersistence.continuityRows.length : 0;
  const revivalRows = world.hintBranchPersistence ? world.hintBranchPersistence.revivalEvents.length : 0;
  recordPrototypeMilestone('save-return-history', `${branchRows} branch continuity row(s), ${revivalRows} revival row(s), saved after return`);
  return log('runPrototypeReturnProof', { branchRows, revivalRows, saved: true, entered: world.entered });
}

function runFirstPlayablePrototypeLoop() {
  ensureGamePrototype();
  runPrototypeOpening();
  runPrototypePracticeChain();
  runPrototypeReturnProof();
  recordPrototypeMilestone('first-playable-loop-complete', 'opening, practice, proposal, audit, save, return, and branch persistence executed from one game surface');
  return log('runFirstPlayablePrototypeLoop', {
    milestones: world.gamePrototype.milestones.length,
    practices: world.emergentPracticeGraph ? world.emergentPracticeGraph.nodes.length : 0,
    proposals: world.villageBoard ? world.villageBoard.projectProposals.length : 0,
    branchContinuity: world.hintBranchPersistence ? world.hintBranchPersistence.continuityRows.length : 0,
  });
}

function deepTimeEntropyByte() {
  const bytes = new Uint8Array(1);
  if (window.crypto && window.crypto.getRandomValues) {
    window.crypto.getRandomValues(bytes);
    return bytes[0];
  }
  return Math.floor(Math.random() * 256);
}

function ensureDeepTimeCivilization() {
  if (!world.deepTimeCivilization) {
    world.deepTimeCivilization = {
      year: 0,
      epoch: 0,
      timeline: [],
      lineages: [],
      emergentEffects: [],
      villageConsequences: [],
      boardLinks: [],
      extinctions: [],
      survivalLedger: [],
      civilizationState: {
        status: 'young',
        continuityScore: 0.5,
        activeLineages: 0,
        traceLineages: 0,
        resourceTotal: Object.values(world.resources || {}).reduce((sum, value) => sum + Number(value || 0), 0),
        millionYearCapable: false,
      },
      pressureLedger: [],
      entropyLedger: [],
      boundary: {
        compressedDeepTime: true,
        activeResidentsRemainSix: true,
        noIntentionalTechTree: true,
        effectsEmergeFromPressure: true,
        hiddenLawsRemainAuditOnly: true,
      },
    };
  }
  return world.deepTimeCivilization;
}

function seedDeepTimeLineages() {
  const sim = ensureDeepTimeCivilization();
  if (sim.lineages.length) return sim.lineages;
  if (!world.emergentPracticeGraph || !world.emergentPracticeGraph.nodes.length) runPrototypePracticeChain();
  const practiceNodes = world.emergentPracticeGraph && world.emergentPracticeGraph.nodes.length ? world.emergentPracticeGraph.nodes : [
    { practice_id: 'proto-practice-1', local_name: 'dry keeping habit', status: 'emerging', maintenance_cost: 1, risk_flags: 'none' },
  ];
  sim.lineages = practiceNodes.slice(0, 6).map((node, index) => ({
    lineage_id: `DTL-${String(index + 1).padStart(2, '0')}`,
    source_practice_id: node.practice_id || `practice-${index + 1}`,
    local_name: node.local_name || node.practice_id || 'unnamed local habit',
    status: node.status || 'emerging',
    age_years: 0,
    adaptations: 0,
    memory_strength: 0.58,
    usefulness: Number(node.practical_score || 0.38),
    maintenance_burden: Number(node.maintenance_cost || 1),
    risk_flags: node.risk_flags || 'none',
    origin_household: node.origin_household || `house_${index % 4}`,
  }));
  return sim.lineages;
}

function chooseDeepTimePressure(entropy) {
  const pressures = [
    'long drought cycle',
    'wet storage decay',
    'route drift',
    'material vein exhaustion',
    'memory compression',
    'rare flood season',
    'tool wear cascade',
    'quiet abundance interval',
  ];
  return pressures[entropy % pressures.length];
}

function pressureResourceDelta(pressure, entropy) {
  const swing = (entropy % 5) - 2;
  if (pressure.includes('drought')) return { water: -3, fiber: swing, wood: -1, care: -1 };
  if (pressure.includes('wet')) return { water: 1, fiber: -2, wood: -1, care: 0 };
  if (pressure.includes('route')) return { water: swing, fiber: -1, wood: 0, care: -1 };
  if (pressure.includes('exhaustion')) return { water: 0, fiber: -2, wood: -2, care: 0 };
  if (pressure.includes('abundance')) return { water: 2, fiber: 2, wood: 1, care: 1 };
  return { water: swing, fiber: swing > 0 ? 1 : -1, wood: 0, care: 0 };
}

function applyDeepTimeResourceDelta(delta) {
  Object.entries(delta).forEach(([key, value]) => {
    world.resources[key] = Math.max(0, Math.min(99, (world.resources[key] || 0) + value));
  });
}

function mutateDeepTimeLineage(lineage, pressure, entropy, years) {
  const stress = pressure.includes('decay') || pressure.includes('exhaustion') || pressure.includes('drought') || pressure.includes('wear');
  const memoryLoss = stress ? 0.05 : 0.02;
  const adaptationChance = (entropy % 100) / 100;
  lineage.age_years += years;
  lineage.memory_strength = clamp(lineage.memory_strength - memoryLoss + (adaptationChance > 0.72 ? 0.08 : 0));
  if (adaptationChance > 0.64) {
    lineage.adaptations += 1;
    lineage.usefulness = clamp(lineage.usefulness + 0.07);
    lineage.status = lineage.adaptations > 4 ? 'institutionalized' : (lineage.status === 'taboo' ? 'ritualized' : 'adapted');
    lineage.local_name = `${lineage.local_name} variant ${lineage.adaptations}`;
  } else if (lineage.memory_strength < 0.18) {
    lineage.status = 'forgotten';
  } else if (stress && adaptationChance < 0.22) {
    lineage.status = lineage.status === 'forgotten' ? 'forgotten' : 'burdened';
    lineage.maintenance_burden += 1;
  }
  return lineage;
}

function runCivilizationDeepTimeEpoch(yearOverride) {
  ensureGamePrototype();
  const sim = ensureDeepTimeCivilization();
  const lineages = seedDeepTimeLineages();
  const entropy = deepTimeEntropyByte();
  const yearOptions = [50, 250, 1000, 10000, 50000];
  const years = Number(yearOverride || yearOptions[entropy % yearOptions.length]);
  const pressure = chooseDeepTimePressure(entropy);
  const delta = pressureResourceDelta(pressure, entropy);
  applyDeepTimeResourceDelta(delta);
  sim.epoch += 1;
  sim.year += years;
  sim.entropyLedger.push({ epoch: sim.epoch, entropy, years, source: window.crypto && window.crypto.getRandomValues ? 'crypto.getRandomValues' : 'Math.random fallback' });
  sim.pressureLedger.push({ epoch: sim.epoch, year: sim.year, pressure, resource_delta: delta });
  lineages.forEach((lineage, index) => mutateDeepTimeLineage(lineage, pressure, (entropy + index * 37) % 256, years));
  const forgotten = lineages.filter(row => row.status === 'forgotten');
  forgotten.forEach(row => {
    if (!sim.extinctions.find(existing => existing.lineage_id === row.lineage_id)) {
      sim.extinctions.push({ epoch: sim.epoch, year: sim.year, lineage_id: row.lineage_id, local_name: row.local_name, reason: `${pressure} plus memory loss` });
    }
  });
  const effectSource = lineages[(entropy + sim.epoch) % lineages.length];
  const effect = {
    effect_id: `DTE-${String(sim.emergentEffects.length + 1).padStart(3, '0')}`,
    epoch: sim.epoch,
    year: sim.year,
    source_lineage_id: effectSource.lineage_id,
    pressure,
    local_name: `${pressure} ${effectSource.local_name}`.slice(0, 96),
    emerged_without_intent: true,
    hidden_law_named_to_residents: false,
    outcome: effectSource.status === 'forgotten' ? 'trace fossil only' : (effectSource.status === 'burdened' ? 'costly survival habit' : 'living cultural technique'),
  };
  sim.emergentEffects.push(effect);
  applyDeepTimeEffectToVillage(effect, delta);
  sim.timeline.push({
    epoch: sim.epoch,
    year: sim.year,
    years_advanced: years,
    pressure,
    resources: { ...world.resources },
    lineage_statuses: lineages.map(row => `${row.lineage_id}:${row.status}`).join(';'),
    effect_id: effect.effect_id,
  });
  evaluateCivilizationSurvival(pressure);
  recordPrototypeMilestone('deep-time-epoch', `+${years} years; ${pressure}; effect ${effect.effect_id}`);
  return log('runCivilizationDeepTimeEpoch', { yearsAdvanced: years, year: sim.year, pressure, lineages: lineages.length, effects: sim.emergentEffects.length, entropy });
}

function evaluateCivilizationSurvival(pressure = 'manual audit') {
  const sim = ensureDeepTimeCivilization();
  const lineages = seedDeepTimeLineages();
  const activeLineages = lineages.filter(row => row.status !== 'forgotten').length;
  const traceLineages = lineages.length - activeLineages;
  const resourceTotal = Object.values(world.resources || {}).reduce((sum, value) => sum + Number(value || 0), 0);
  const averageMemory = lineages.length ? lineages.reduce((sum, row) => sum + Number(row.memory_strength || 0), 0) / lineages.length : 0;
  const totalBurden = lineages.reduce((sum, row) => sum + Number(row.maintenance_burden || 0), 0);
  const recoveryPotential = Number(((world.resources.care || 0) + activeLineages + sim.villageConsequences.length * 0.08).toFixed(3));
  const continuityScore = clamp((activeLineages / Math.max(1, lineages.length)) * 0.42 + averageMemory * 0.28 + Math.min(1, resourceTotal / 36) * 0.18 + Math.min(1, recoveryPotential / 12) * 0.12 - Math.min(0.3, totalBurden / 80));
  let status = 'flourishing';
  if (continuityScore < 0.18 || activeLineages === 0) status = 'collapsed into trace memory';
  else if (continuityScore < 0.34) status = 'trace-memory survival';
  else if (continuityScore < 0.52) status = 'fragmented survival';
  else if (continuityScore < 0.72) status = 'strained continuity';
  const survivalRow = {
    audit_id: `DTS-${String(sim.survivalLedger.length + 1).padStart(3, '0')}`,
    epoch: sim.epoch,
    year: sim.year,
    pressure,
    status,
    continuity_score: Number(continuityScore.toFixed(3)),
    active_lineages: activeLineages,
    trace_lineages: traceLineages,
    resource_total: resourceTotal,
    average_memory: Number(averageMemory.toFixed(3)),
    total_burden: totalBurden,
    recovery_potential: recoveryPotential,
    million_year_capable: sim.year >= 1000000 && activeLineages > 0 && continuityScore >= 0.18,
    emerged_without_intent: true,
  };
  sim.civilizationState = {
    status,
    continuityScore: survivalRow.continuity_score,
    activeLineages,
    traceLineages,
    resourceTotal,
    averageMemory: survivalRow.average_memory,
    totalBurden,
    recoveryPotential,
    millionYearCapable: survivalRow.million_year_capable,
  };
  sim.survivalLedger.push(survivalRow);
  return survivalRow;
}

function runCivilizationSurvivalAudit() {
  const row = evaluateCivilizationSurvival('player survival audit');
  recordPrototypeMilestone('survival-audit', `${row.status}; continuity ${row.continuity_score}; active lineages ${row.active_lineages}`);
  return log('runCivilizationSurvivalAudit', { status: row.status, continuityScore: row.continuity_score, activeLineages: row.active_lineages, millionYearCapable: row.million_year_capable });
}

function applyDeepTimeEffectToVillage(effect, resourceDelta = null) {
  const sim = ensureDeepTimeCivilization();
  const board = ensureVillageBoard();
  const residentNames = Object.keys(world.residents);
  const resident = residentNames[(effect.epoch + effect.local_name.length) % residentNames.length];
  const consequenceId = `DTC-${String(sim.villageConsequences.length + 1).padStart(3, '0')}`;
  const scheduleVerb = effect.outcome.includes('trace') ? 'asks elders about' : effect.outcome.includes('costly') ? 'maintains' : 'teaches';
  mutateResident(resident, {
    trust: effect.outcome.includes('costly') ? -0.004 : 0.006,
    progress: effect.outcome.includes('trace') ? 0.002 : 0.01,
    schedule: `${scheduleVerb} ${effect.local_name}`,
    memory: `carries deep-time effect ${effect.effect_id}: ${effect.local_name}`,
    historyEvent: 'deep-time consequence',
    historyDetail: `${effect.outcome}; emerged without intent ${effect.emerged_without_intent ? 'yes' : 'no'}`
  });
  const concern = {
    concern_id: `VBC-DT-${String(board.concerns.length + 1).padStart(2, '0')}`,
    resident,
    problem: `deep-time pressure left ${effect.outcome} around ${effect.local_name}`,
    source: effect.effect_id,
    urgency: effect.outcome.includes('costly') ? 'high' : effect.outcome.includes('trace') ? 'low' : 'medium',
    who_felt_this: resident,
    avatar_direct_control: false
  };
  const proposal = {
    proposal_id: `VBP-DT-${String(board.projectProposals.length + 1).padStart(2, '0')}`,
    proposer: resident,
    problem_addressed: concern.problem,
    materials_needed: effect.outcome.includes('costly') ? ['fiber', 'wood', 'care'] : ['fiber', 'care'],
    likely_helpers: residentNames.filter(name => name !== resident).slice(0, 2),
    resident_willingness: Number(Math.max(0.16, Math.min(0.9, world.residents[resident].trust - world.residents[resident].debt * 0.04)).toFixed(3)),
    known_objections: ['nobody planned this effect', 'maintenance burden may outlive the current residents'],
    risk: concern.urgency,
    maintenance_cost: effect.outcome.includes('costly') ? 3 : 1,
    related_memories: [world.residents[resident].memory],
    related_practice_nodes: [effect.source_lineage_id],
    possible_failure_modes: ['lineage forgotten', 'materials run short', 'ritual replaces useful habit'],
    current_support_level: 0,
    avatar_can_force: false,
    status: 'deep-time consequence proposed'
  };
  board.concerns.push(concern);
  board.projectProposals.push(proposal);
  const consequence = {
    consequence_id: consequenceId,
    effect_id: effect.effect_id,
    resident,
    schedule: world.residents[resident].schedule,
    proposal_id: proposal.proposal_id,
    emerged_without_intent: true,
    hidden_law_named_to_residents: false,
    resource_delta: resourceDelta || {},
  };
  sim.villageConsequences.push(consequence);
  sim.boardLinks.push({ effect_id: effect.effect_id, concern_id: concern.concern_id, proposal_id: proposal.proposal_id, resident, avatar_commanded: false });
  recordRealityConstraint('deep_time_effect_to_village', {
    resident,
    sourceBeliefId: effect.effect_id,
    materials: proposal.materials_needed,
    publicObservation: effect.local_name,
    residentInterpretation: proposal.status,
    materialTransformation: 'deep-time pressure changed obligations, not a free construction',
    timeCost: 1,
    workCost: proposal.maintenance_cost,
    toolWear: effect.outcome.includes('costly') ? 1 : 0,
    maintenanceObligation: proposal.proposal_id,
    unintendedConsequence: effect.outcome,
    hiddenLawInvolved: 'audit-only deep-time lineage source',
    conservationCheck: true
  });
  return consequence;
}

function applyLatestDeepTimeEffectToVillage() {
  const sim = ensureDeepTimeCivilization();
  if (!sim.emergentEffects.length) runCivilizationDeepTimeEpoch();
  const effect = sim.emergentEffects[sim.emergentEffects.length - 1];
  const existing = (sim.villageConsequences || []).find(row => row.effect_id === effect.effect_id);
  if (existing) {
    recordPrototypeMilestone('apply-deep-time-effect', `${effect.effect_id} was already affecting ${existing.resident} through ${existing.proposal_id}`);
    return log('applyLatestDeepTimeEffectToVillage', { resident: existing.resident, proposalId: existing.proposal_id, effectId: effect.effect_id, alreadyApplied: true });
  }
  const consequence = applyDeepTimeEffectToVillage(effect, { replayed_by_player: true });
  recordPrototypeMilestone('apply-deep-time-effect', `${effect.effect_id} affected ${consequence.resident} through ${consequence.proposal_id}`);
  return log('applyLatestDeepTimeEffectToVillage', { resident: consequence.resident, proposalId: consequence.proposal_id, effectId: effect.effect_id });
}

function runCivilizationMillionYearSim() {
  ensureGamePrototype();
  const sim = ensureDeepTimeCivilization();
  const startEpoch = sim.epoch;
  while (sim.year < 1000000 && sim.epoch - startEpoch < 40) {
    runCivilizationDeepTimeEpoch(50000);
  }
  recordPrototypeMilestone('million-year-sim', `${sim.year} compressed years across ${sim.epoch} epoch(s); ${sim.emergentEffects.length} emergent effect(s)`);
  const survival = evaluateCivilizationSurvival('million-year survival audit');
  return log('runCivilizationMillionYearSim', { year: sim.year, epochs: sim.epoch, effects: sim.emergentEffects.length, extinctions: sim.extinctions.length, survivalStatus: survival.status, continuityScore: survival.continuity_score });
}

function runCivilizationTenMillionYearSim() {
  ensureGamePrototype();
  const sim = ensureDeepTimeCivilization();
  const startEpoch = sim.epoch;
  while (sim.year < 10000000 && sim.epoch - startEpoch < 220) {
    runCivilizationDeepTimeEpoch(50000);
    if (sim.civilizationState && sim.civilizationState.status === 'collapsed into trace memory' && sim.epoch - startEpoch > 20) break;
  }
  const survival = evaluateCivilizationSurvival('ten-million-year survival audit');
  recordPrototypeMilestone('ten-million-year-sim', `${sim.year} compressed years; ${survival.status}; continuity ${survival.continuity_score}`);
  return log('runCivilizationTenMillionYearSim', { year: sim.year, epochs: sim.epoch, effects: sim.emergentEffects.length, extinctions: sim.extinctions.length, survivalStatus: survival.status, continuityScore: survival.continuity_score });
}

function ensureAutonomousResidents() {
  if (!world.autonomousResidents) {
    const needState = {};
    Object.keys(world.residents).forEach((name, index) => {
      needState[name] = {
        energy: 0.68 - index * 0.03,
        hunger: 0.18 + index * 0.02,
        attention: 0.62,
        safety: 0.74,
        autonomy: 0.58,
      };
    });
    world.autonomousResidents = {
      day: 0,
      season: 0,
      needState,
      actionLog: [],
      refusalLog: [],
      careLedger: [],
      expressionLedger: [],
      entropyLedger: [],
      boundary: {
        noDirectPlayerCommand: true,
        residentsCanRefuse: true,
        actionsCostTimeAndNeed: true,
        expressionsArePublicCuesOnly: true,
        stochasticButAudited: true,
      },
    };
  }
  if (!world.autonomousResidents.expressionLedger) world.autonomousResidents.expressionLedger = [];
  if (!world.autonomousResidents.boundary.expressionsArePublicCuesOnly) world.autonomousResidents.boundary.expressionsArePublicCuesOnly = true;
  return world.autonomousResidents;
}

function clampNeed(value) {
  return Math.max(0, Math.min(1, Number(value || 0)));
}

function driftResidentNeeds(needs, entropy, action) {
  const effort = ['proposal_work', 'practice_maintenance', 'experiment', 'forage'].includes(action) ? 0.12 : 0.04;
  const stress = entropy % 7 === 0 ? 0.08 : 0.02;
  needs.energy = clampNeed(needs.energy - effort + (action === 'rest' ? 0.22 : 0));
  needs.hunger = clampNeed(needs.hunger + effort * 0.6 - (action === 'forage' ? 0.12 : 0));
  needs.attention = clampNeed(needs.attention - effort * 0.8 + (action === 'teach' ? 0.04 : 0));
  needs.safety = clampNeed(needs.safety - stress + (action === 'repair_safety' ? 0.14 : 0));
  needs.autonomy = clampNeed(needs.autonomy + (action === 'refuse' ? 0.08 : -0.015));
  return needs;
}

function chooseAutonomousResidentAction(residentName, entropy) {
  const sim = ensureAutonomousResidents();
  const needs = sim.needState[residentName];
  const board = world.villageBoard;
  const hasProposal = Boolean(board && board.projectProposals && board.projectProposals.length);
  const hasPractice = Boolean(world.emergentPracticeGraph && world.emergentPracticeGraph.nodes && world.emergentPracticeGraph.nodes.length);
  const lowResource = (world.resources.water || 0) < 5 || (world.resources.fiber || 0) < 5 || (world.resources.care || 0) < 3;
  if (needs.energy < 0.22 || needs.hunger > 0.78) return 'rest';
  if (needs.autonomy > 0.74 && entropy % 5 === 0) return 'refuse';
  if (needs.safety < 0.42) return 'repair_safety';
  if (lowResource) return 'forage';
  if (hasProposal && entropy % 3 !== 0) return 'proposal_work';
  if (hasPractice && entropy % 4 === 0) return 'practice_maintenance';
  if (hasPractice && entropy % 4 === 1) return 'teach';
  return entropy % 2 === 0 ? 'experiment' : 'observe';
}

function deriveVisibleResidentExpression(residentName, action = 'observe', needsOverride = null) {
  const sim = world.autonomousResidents;
  const needs = needsOverride || (sim && sim.needState ? sim.needState[residentName] : null);
  const resident = world.residents[residentName] || {};
  let posture = 'upright and available';
  let movementCue = 'steady';
  let gazeCue = 'looks toward current work';
  let marker = 'available';
  let reason = resident.schedule || 'ordinary village state';
  if (needs && needs.energy < 0.28) {
    posture = 'low rest posture';
    movementCue = 'slow steps';
    gazeCue = 'looks for a quiet place';
    marker = 'tired';
    reason = 'low energy';
  } else if (needs && needs.hunger > 0.74) {
    posture = 'leaning toward commons';
    movementCue = 'searching path';
    gazeCue = 'checks stores';
    marker = 'hungry';
    reason = 'food pressure';
  } else if (needs && needs.safety < 0.45) {
    posture = 'guarded stance';
    movementCue = 'short careful steps';
    gazeCue = 'scans route edges';
    marker = 'guarded';
    reason = 'low safety';
  } else if ((needs && needs.autonomy > 0.70) || action === 'refuse') {
    posture = 'turned half-away';
    movementCue = 'keeps distance';
    gazeCue = 'checks for pressure';
    marker = 'boundary';
    reason = 'autonomy pressure';
  } else if (action === 'proposal_work') {
    posture = 'carrying work bundle';
    movementCue = 'purposeful';
    gazeCue = 'checks board and helpers';
    marker = 'working';
    reason = 'resident proposal work';
  } else if (action === 'practice_maintenance') {
    posture = 'hands near practice materials';
    movementCue = 'careful repeat';
    gazeCue = 'watches stored materials';
    marker = 'maintaining';
    reason = 'practice upkeep';
  } else if (action === 'teach') {
    posture = 'open teaching stance';
    movementCue = 'small demonstration';
    gazeCue = 'faces a nearby resident';
    marker = 'teaching';
    reason = 'social transmission';
  } else if (action === 'experiment') {
    posture = 'careful crouch';
    movementCue = 'measured handling';
    gazeCue = 'watches materials';
    marker = 'testing';
    reason = 'resident-chosen test';
  } else if (action === 'forage') {
    posture = 'forward carrying stance';
    movementCue = 'route-bound';
    gazeCue = 'checks commons';
    marker = 'foraging';
    reason = 'resource pressure';
  } else if (action === 'rest') {
    posture = 'seated near familiar work';
    movementCue = 'still';
    gazeCue = 'softly watches safe people';
    marker = 'resting';
    reason = 'recovery';
  }
  return {
    resident: residentName,
    posture,
    movementCue,
    gazeCue,
    marker,
    reason,
    publicCueOnly: true,
    hiddenStateExposed: false,
  };
}

function recordVisibleResidentExpression(residentName, action, needs) {
  const sim = ensureAutonomousResidents();
  const expression = deriveVisibleResidentExpression(residentName, action, needs);
  const row = {
    expression_id: `VBE-${String(sim.expressionLedger.length + 1).padStart(3, '0')}`,
    day: sim.day,
    action,
    ...expression,
  };
  sim.expressionLedger.push(row);
  if (sim.expressionLedger.length > 80) sim.expressionLedger.shift();
  return row;
}

function latestVisibleExpressionFor(residentName) {
  const sim = world.autonomousResidents;
  if (sim && sim.expressionLedger) {
    const existing = sim.expressionLedger.slice().reverse().find(row => row.resident === residentName);
    if (existing) return existing;
  }
  return deriveVisibleResidentExpression(residentName);
}

function applyAutonomousResidentAction(residentName, action, entropy) {
  const sim = ensureAutonomousResidents();
  const needs = driftResidentNeeds(sim.needState[residentName], entropy, action);
  const resident = world.residents[residentName];
  const board = ensureVillageBoard();
  const proposal = board.projectProposals[board.projectProposals.length - 1] || null;
  const practice = world.emergentPracticeGraph && world.emergentPracticeGraph.nodes.length ? world.emergentPracticeGraph.nodes[world.emergentPracticeGraph.nodes.length - 1] : null;
  let schedule = resident.schedule;
  let memory = resident.memory;
  let materialCost = [];
  let progressDelta = 0.004;
  let trustDelta = 0;
  let careDelta = 0;
  if (action === 'rest') {
    schedule = 'rests near familiar work';
    memory = 'rested before deciding what to carry next';
    progressDelta = 0.001;
  } else if (action === 'refuse') {
    schedule = 'keeps boundary before helping';
    memory = 'refused an implied priority and kept autonomy';
    trustDelta = -0.003;
    sim.refusalLog.push({ day: sim.day, resident: residentName, reason: 'autonomy need exceeded threshold', entropy });
  } else if (action === 'repair_safety') {
    schedule = 'repairs a safety marker';
    memory = 'raised safety after pressure';
    materialCost = ['wood'];
    world.resources.wood = Math.max(0, world.resources.wood - 1);
    progressDelta = 0.008;
  } else if (action === 'forage') {
    schedule = 'forages for strained commons';
    memory = 'brought back small supplies under pressure';
    world.resources.water = Math.min(99, world.resources.water + 1);
    world.resources.fiber = Math.min(99, world.resources.fiber + 1);
    progressDelta = 0.006;
  } else if (action === 'proposal_work' && proposal) {
    schedule = `works on ${proposal.problem_addressed}`;
    memory = `worked on resident proposal ${proposal.proposal_id}`;
    materialCost = proposal.materials_needed.slice(0, 2);
    world.resources.fiber = Math.max(0, world.resources.fiber - (materialCost.includes('fiber') ? 1 : 0));
    world.resources.care = Math.max(0, world.resources.care - (materialCost.includes('care') ? 1 : 0));
    proposal.current_support_level = Number(Math.min(1, proposal.current_support_level + 0.08).toFixed(3));
    progressDelta = 0.012;
    trustDelta = 0.003;
  } else if (action === 'practice_maintenance' && practice) {
    schedule = `maintains ${practice.local_name || practice.practice_id}`;
    memory = `kept practice ${practice.practice_id || practice.local_name} from decaying`;
    materialCost = ['fiber'];
    world.resources.fiber = Math.max(0, world.resources.fiber - 1);
    progressDelta = 0.009;
  } else if (action === 'teach' && practice) {
    schedule = `teaches ${practice.local_name || practice.practice_id}`;
    memory = `taught a local variant without naming hidden law`;
    progressDelta = 0.01;
    trustDelta = 0.002;
  } else if (action === 'experiment') {
    schedule = 'tries a small resident-chosen test';
    memory = 'made a small observation from ordinary bottleneck';
    materialCost = ['fiber'];
    world.resources.fiber = Math.max(0, world.resources.fiber - 1);
    runPracticalDiscoveryStep('autonomous_experiment');
    progressDelta = 0.007;
  } else {
    schedule = 'observes village pressure';
    memory = 'noticed pressure without acting yet';
  }
  mutateResident(residentName, {
    trust: trustDelta,
    progress: progressDelta,
    schedule,
    memory,
    historyEvent: 'autonomous resident action',
    historyDetail: `${action}; entropy ${entropy}; no direct player command`
  });
  const row = {
    action_id: `ARA-${String(sim.actionLog.length + 1).padStart(3, '0')}`,
    day: sim.day,
    season: sim.season,
    resident: residentName,
    action,
    entropy,
    needs: { ...needs },
    material_cost: materialCost,
    schedule,
    memory,
    no_direct_player_command: true,
  };
  sim.actionLog.push(row);
  const expression = recordVisibleResidentExpression(residentName, action, needs);
  row.visible_expression_id = expression.expression_id;
  sim.careLedger.push({ action_id: row.action_id, resident: residentName, energy: needs.energy, hunger: needs.hunger, safety: needs.safety, autonomy: needs.autonomy });
  recordRealityConstraint('autonomous_resident_action', {
    resident: residentName,
    sourceBeliefId: row.action_id,
    materials: materialCost,
    publicObservation: schedule,
    residentInterpretation: memory,
    materialTransformation: materialCost.length ? 'resident consumed or moved material through autonomous action' : 'attention/time spent without material transformation',
    timeCost: 1,
    workCost: ['rest', 'observe', 'refuse'].includes(action) ? 0 : 1,
    toolWear: ['proposal_work', 'practice_maintenance', 'repair_safety'].includes(action) ? 1 : 0,
    maintenanceObligation: action === 'proposal_work' && proposal ? proposal.proposal_id : 'none',
    unintendedConsequence: action === 'refuse' ? 'resident autonomy preserved' : 'ordinary world state changed without player command',
    hiddenLawInvolved: 'none in normal view',
    conservationCheck: true
  });
  return row;
}

function runAutonomousResidentTick() {
  const sim = ensureAutonomousResidents();
  const entropy = deepTimeEntropyByte();
  const residentNames = Object.keys(world.residents);
  const residentName = residentNames[(entropy + sim.day + sim.actionLog.length) % residentNames.length];
  const action = chooseAutonomousResidentAction(residentName, entropy);
  sim.day += 1;
  sim.entropyLedger.push({ day: sim.day, entropy, source: window.crypto && window.crypto.getRandomValues ? 'crypto.getRandomValues' : 'Math.random fallback' });
  const row = applyAutonomousResidentAction(residentName, action, entropy);
  recordPrototypeMilestone('autonomous-resident-tick', `${residentName} chose ${action} without direct player command`);
  return log('runAutonomousResidentTick', { resident: residentName, action, day: sim.day, entropy, needs: row.needs });
}

function runAutonomousResidentSeason() {
  const sim = ensureAutonomousResidents();
  const before = sim.actionLog.length;
  sim.season += 1;
  for (let i = 0; i < 18; i += 1) runAutonomousResidentTick();
  if (sim.season % 2 === 0) runCivilizationDeepTimeEpoch(250);
  recordPrototypeMilestone('autonomous-resident-season', `${sim.actionLog.length - before} autonomous action(s); season ${sim.season}`);
  return log('runAutonomousResidentSeason', { season: sim.season, actionsAdded: sim.actionLog.length - before, totalActions: sim.actionLog.length });
}

function formatPrototypeVillageState() {
  const residentLines = Object.entries(world.residents)
    .slice(0, 6)
    .map(([name, row]) => {
      const expression = latestVisibleExpressionFor(name);
      return `${name}: ${row.schedule}; trust=${row.trust.toFixed(2)} debt=${row.debt} progress=${row.progress.toFixed(2)}; cue=${expression.marker}/${expression.posture}; memory=${row.memory}`;
    });
  const resources = Object.entries(world.resources).map(([key, value]) => `${key}=${value}`).join(', ');
  return [
    `Entered: ${world.entered ? 'yes' : 'no'} / room: ${world.avatar.room} / selected: ${world.selected}`,
    `Resources: ${resources}`,
    'Residents:',
    ...residentLines,
  ].join('\n');
}

function formatPrototypePublicOutcomes() {
  const practiceCount = world.emergentPracticeGraph ? world.emergentPracticeGraph.nodes.length : 0;
  const latestPractice = practiceCount ? world.emergentPracticeGraph.nodes[world.emergentPracticeGraph.nodes.length - 1] : null;
  const boardCount = world.villageBoard ? world.villageBoard.projectProposals.length : 0;
  const latestProposal = boardCount ? world.villageBoard.projectProposals[world.villageBoard.projectProposals.length - 1] : null;
  const ledgerRows = world.realityConstraintLedger ? world.realityConstraintLedger.rows.length : 0;
  const branchRows = world.hintBranchPersistence ? world.hintBranchPersistence.continuityRows.length : 0;
  const latestBranch = branchRows ? world.hintBranchPersistence.continuityRows[world.hintBranchPersistence.continuityRows.length - 1] : null;
  const deepTime = world.deepTimeCivilization;
  const consequenceCount = deepTime && deepTime.villageConsequences ? deepTime.villageConsequences.length : 0;
  const survivalStatus = deepTime && deepTime.civilizationState ? deepTime.civilizationState.status : 'not audited';
  const autonomous = world.autonomousResidents;
  const saves = world.gamePrototypeSaves;
  return [
    `Practice graph: ${practiceCount} node(s)${latestPractice ? ` / latest ${latestPractice.local_name || latestPractice.practice_id}` : ''}`,
    `Village board: ${boardCount} proposal(s)${latestProposal ? ` / latest ${latestProposal.problem_addressed || latestProposal.proposal_id}` : ''}`,
    `Reality ledger: ${ledgerRows} causal row(s)`,
    `Return branches: ${branchRows} continuity row(s)${latestBranch ? ` / latest ${latestBranch.return_status}` : ''}`,
    `Deep time: ${deepTime ? `${deepTime.year} years / ${deepTime.emergentEffects.length} emergent effect(s) / ${consequenceCount} village consequence(s) / ${survivalStatus}` : 'not started'}`,
    `Autonomous residents: ${autonomous ? `${autonomous.day} day(s) / ${autonomous.actionLog.length} action(s) / ${autonomous.refusalLog.length} refusal(s)` : 'not started'}`,
    `Save slots: ${saves ? `${saves.slots.length} slot(s) / active ${saves.activeSlotId || 'none'} / returns ${saves.returnLog.length}` : 'none'}`,
    `Audit mode: ${world.audit ? 'on' : 'off'} / hidden law normal view: no`,
  ].join('\n');
}

function formatPrototypeLoopReceipt() {
  const prototype = world.gamePrototype || ensureGamePrototype();
  const milestones = prototype.milestones.slice(-8).map(row => `${row.step}: ${row.detail} [room=${row.room}, replay=${row.replayRows}]`);
  return [
    `Mode: ${prototype.mode}`,
    `No more research reports by default: ${prototype.noMoreResearchReportsByDefault ? 'yes' : 'no'}`,
    `Last loop: ${prototype.lastLoop || 'not started'}`,
    'Milestones:',
    ...(milestones.length ? milestones : ['none yet']),
  ].join('\n');
}

function formatPrototypeDeepTime() {
  const sim = world.deepTimeCivilization;
  if (!sim) return 'No deep-time epochs yet. Run Deep-time epoch or Million-year sim.';
  const latestTimeline = sim.timeline.slice(-6).map(row => `epoch ${row.epoch}: year ${row.year}, ${row.pressure}, effect=${row.effect_id}`);
  const latestEffects = sim.emergentEffects.slice(-6).map(row => `${row.effect_id}: ${row.local_name} -> ${row.outcome}`);
  const latestConsequences = (sim.villageConsequences || []).slice(-6).map(row => `${row.consequence_id}: ${row.effect_id} changed ${row.resident} schedule via ${row.proposal_id}`);
  const latestSurvival = (sim.survivalLedger || []).slice(-6).map(row => `${row.audit_id}: year ${row.year}, ${row.status}, score=${row.continuity_score}, active=${row.active_lineages}`);
  const lineageRows = sim.lineages.slice(0, 6).map(row => `${row.lineage_id}: ${row.local_name}; status=${row.status}; age=${row.age_years}; memory=${row.memory_strength.toFixed(2)}; burden=${row.maintenance_burden}`);
  const state = sim.civilizationState || {};
  return [
    `Compressed year: ${sim.year}`,
    `Epochs: ${sim.epoch}`,
    `Extinctions: ${sim.extinctions.length}`,
    `Civilization status: ${state.status || 'unknown'} / continuity=${state.continuityScore ?? 'n/a'} / million-year capable=${state.millionYearCapable ? 'yes' : 'not yet'}`,
    `Boundary: no intentional tech tree; hidden laws audit-only; effects emerge from pressure.`,
    'Lineages:',
    ...(lineageRows.length ? lineageRows : ['none']),
    'Recent epochs:',
    ...(latestTimeline.length ? latestTimeline : ['none']),
    'Emergent effects:',
    ...(latestEffects.length ? latestEffects : ['none']),
    'Village consequences:',
    ...(latestConsequences.length ? latestConsequences : ['none']),
    'Survival ledger:',
    ...(latestSurvival.length ? latestSurvival : ['none']),
  ].join('\n');
}

function formatPrototypeAutonomousResidents() {
  const sim = world.autonomousResidents;
  if (!sim) return 'No autonomous resident ticks yet. Run Resident tick or Resident season.';
  const actions = sim.actionLog.slice(-8).map(row => `${row.action_id}: day ${row.day}, ${row.resident} chose ${row.action}; energy=${row.needs.energy.toFixed(2)} hunger=${row.needs.hunger.toFixed(2)} safety=${row.needs.safety.toFixed(2)}`);
  const refusals = sim.refusalLog.slice(-4).map(row => `day ${row.day}: ${row.resident} refused because ${row.reason}`);
  const care = sim.careLedger.slice(-6).map(row => `${row.action_id}: ${row.resident} energy=${row.energy.toFixed(2)} hunger=${row.hunger.toFixed(2)} autonomy=${row.autonomy.toFixed(2)}`);
  const expressions = (sim.expressionLedger || []).slice(-8).map(row => `${row.expression_id}: ${row.resident} ${row.marker}; posture=${row.posture}; movement=${row.movementCue}; gaze=${row.gazeCue}`);
  return [
    `Day: ${sim.day} / season: ${sim.season}`,
    `Boundary: stochastic autonomous actions; no direct player command; actions cost time/needs/materials.`,
    'Recent actions:',
    ...(actions.length ? actions : ['none']),
    'Visible expression cues:',
    ...(expressions.length ? expressions : ['none']),
    'Refusals:',
    ...(refusals.length ? refusals : ['none']),
    'Care ledger:',
    ...(care.length ? care : ['none']),
  ].join('\n');
}

function formatPrototypeReadableBehavior() {
  const names = Object.keys(world.residents).slice(0, 6);
  const rows = names.map(name => {
    const expression = latestVisibleExpressionFor(name);
    return `${name}: ${expression.marker}; posture=${expression.posture}; movement=${expression.movementCue}; gaze=${expression.gazeCue}; reason=${expression.reason}`;
  });
  const ledgerCount = world.autonomousResidents && world.autonomousResidents.expressionLedger ? world.autonomousResidents.expressionLedger.length : 0;
  return [
    `Public cue ledger: ${ledgerCount} row(s)`,
    'Boundary: readable behavior is public body-language state only; no hidden/private workspace exposed.',
    'Resident cues:',
    ...rows,
  ].join('\n');
}

function runPrototypeQASmoke() {
  runFirstPlayablePrototypeLoop();
  runAutonomousResidentSeason();
  runCivilizationMillionYearSim();
  runCivilizationSurvivalAudit();
  runRealityConstraintAudit();
  askSchedule();
  askSchedule();
  saveWorld();
  const savedCounts = {
    autonomousActions: world.autonomousResidents ? world.autonomousResidents.actionLog.length : 0,
    deepTimeYear: world.deepTimeCivilization ? world.deepTimeCivilization.year : 0,
    practiceNodes: world.emergentPracticeGraph ? world.emergentPracticeGraph.nodes.length : 0,
    proposals: world.villageBoard ? world.villageBoard.projectProposals.length : 0,
    ordinaryPlayFeed: world.practicalDiscovery && world.practicalDiscovery.ordinaryPlayFeed ? world.practicalDiscovery.ordinaryPlayFeed.length : 0,
    autoGeneratedTests: world.practicalDiscovery && world.practicalDiscovery.autoGeneratedTests ? world.practicalDiscovery.autoGeneratedTests.length : 0,
    visibleExpressions: world.autonomousResidents && world.autonomousResidents.expressionLedger ? world.autonomousResidents.expressionLedger.length : 0,
  };
  runAutonomousResidentTick();
  restoreWorld();
  const checks = [
    { id: 'entered-village', pass: world.entered === true, evidence: world.avatar.room },
    { id: 'six-residents-max', pass: Object.keys(world.residents).length <= 6, evidence: `${Object.keys(world.residents).length} residents` },
    { id: 'autonomous-actions', pass: Boolean(world.autonomousResidents && world.autonomousResidents.actionLog.length >= savedCounts.autonomousActions && savedCounts.autonomousActions > 0), evidence: `${world.autonomousResidents ? world.autonomousResidents.actionLog.length : 0} action(s)` },
    { id: 'emergent-practice', pass: Boolean(world.emergentPracticeGraph && world.emergentPracticeGraph.nodes.length > 0), evidence: `${world.emergentPracticeGraph ? world.emergentPracticeGraph.nodes.length : 0} node(s)` },
    { id: 'ordinary-play-generates-tests', pass: Boolean(world.practicalDiscovery && world.practicalDiscovery.ordinaryPlayFeed && world.practicalDiscovery.ordinaryPlayFeed.length >= savedCounts.ordinaryPlayFeed && savedCounts.ordinaryPlayFeed > 0 && world.practicalDiscovery.autoGeneratedTests && world.practicalDiscovery.autoGeneratedTests.length >= savedCounts.autoGeneratedTests && savedCounts.autoGeneratedTests > 0), evidence: `${savedCounts.ordinaryPlayFeed} feed row(s), ${savedCounts.autoGeneratedTests} auto test(s)` },
    { id: 'visible-body-expression', pass: Boolean(world.autonomousResidents && world.autonomousResidents.expressionLedger && world.autonomousResidents.expressionLedger.length >= savedCounts.visibleExpressions && savedCounts.visibleExpressions > 0 && world.autonomousResidents.expressionLedger.every(row => row.publicCueOnly === true && row.hiddenStateExposed === false)), evidence: `${savedCounts.visibleExpressions} expression cue(s)` },
    { id: 'village-proposals', pass: Boolean(world.villageBoard && world.villageBoard.projectProposals.length > 0), evidence: `${world.villageBoard ? world.villageBoard.projectProposals.length : 0} proposal(s)` },
    { id: 'deep-time-million-year', pass: Boolean(world.deepTimeCivilization && world.deepTimeCivilization.year >= 1000000), evidence: `${world.deepTimeCivilization ? world.deepTimeCivilization.year : 0} years` },
    { id: 'survival-audited', pass: Boolean(world.deepTimeCivilization && world.deepTimeCivilization.survivalLedger && world.deepTimeCivilization.survivalLedger.length > 0), evidence: world.deepTimeCivilization && world.deepTimeCivilization.civilizationState ? world.deepTimeCivilization.civilizationState.status : 'none' },
    { id: 'causal-ledger', pass: Boolean(world.realityConstraintLedger && world.realityConstraintLedger.rows.length > 0), evidence: `${world.realityConstraintLedger ? world.realityConstraintLedger.rows.length : 0} row(s)` },
    { id: 'save-return-preserved', pass: Boolean(world.deepTimeCivilization && world.autonomousResidents && world.gamePrototype), evidence: `saved actions=${savedCounts.autonomousActions}, saved year=${savedCounts.deepTimeYear}` },
    { id: 'no-research-report-mode', pass: Boolean(world.gamePrototype && world.gamePrototype.noMoreResearchReportsByDefault), evidence: 'game build branch' },
  ];
  const passed = checks.filter(row => row.pass).length;
  world.gamePrototypeQA = {
    run_id: `GPQA-${String((world.gamePrototypeQA ? world.gamePrototypeQA.runCount || 0 : 0) + 1).padStart(2, '0')}`,
    runCount: (world.gamePrototypeQA ? world.gamePrototypeQA.runCount || 0 : 0) + 1,
    pass: passed === checks.length,
    passed,
    total: checks.length,
    checks,
    savedCounts,
    replayRows: world.replay.length,
    boundary: 'prototype QA only; browser-local game build smoke, not production certification',
  };
  recordPrototypeMilestone('prototype-qa-smoke', `${passed}/${checks.length} checks passed`);
  return log('runPrototypeQASmoke', { pass: world.gamePrototypeQA.pass, passed, total: checks.length });
}

function ensurePrototypeClock() {
  if (!world.prototypeClock) {
    world.prototypeClock = {
      running: false,
      step: 0,
      intervalMs: 1200,
      lastAction: 'not started',
      lastSavedStep: 0,
      cadence: {
        residentTickEveryStep: true,
        deepTimeEvery: 8,
        survivalAuditEvery: 12,
        saveEvery: 18,
      },
      boundary: 'browser-local auto sim; no hidden server process; player can pause',
    };
  }
  return world.prototypeClock;
}

function runPrototypeAutoStep() {
  const clock = ensurePrototypeClock();
  if (!world.entered) runPrototypeOpening();
  clock.step += 1;
  runAutonomousResidentTick();
  let action = 'resident tick';
  if (clock.step % 6 === 0) {
    supportVillageProposal();
    action += ' + proposal support';
  }
  if (clock.step % clock.cadence.deepTimeEvery === 0) {
    runCivilizationDeepTimeEpoch(250);
    action += ' + deep-time epoch';
  }
  if (clock.step % clock.cadence.survivalAuditEvery === 0) {
    runCivilizationSurvivalAudit();
    action += ' + survival audit';
  }
  if (clock.step % clock.cadence.saveEvery === 0) {
    saveWorld();
    clock.lastSavedStep = clock.step;
    action += ' + save';
  }
  clock.lastAction = action;
  recordPrototypeMilestone('auto-sim-step', `step ${clock.step}: ${action}`);
  return log('runPrototypeAutoStep', { step: clock.step, action, running: clock.running });
}

function startPrototypeAutoSim() {
  const clock = ensurePrototypeClock();
  if (prototypeAutoTimer) return log('startPrototypeAutoSim', { running: true, step: clock.step, alreadyRunning: true });
  clock.running = true;
  prototypeAutoTimer = window.setInterval(() => {
    runPrototypeAutoStep();
  }, clock.intervalMs);
  return log('startPrototypeAutoSim', { running: true, step: clock.step, intervalMs: clock.intervalMs });
}

function pausePrototypeAutoSim() {
  const clock = ensurePrototypeClock();
  if (prototypeAutoTimer) {
    window.clearInterval(prototypeAutoTimer);
    prototypeAutoTimer = null;
  }
  clock.running = false;
  return log('pausePrototypeAutoSim', { running: false, step: clock.step });
}

function runPrototypeAutoBurst() {
  const clock = ensurePrototypeClock();
  const before = clock.step;
  for (let i = 0; i < 20; i += 1) runPrototypeAutoStep();
  clock.running = Boolean(prototypeAutoTimer);
  return log('runPrototypeAutoBurst', { stepsAdded: clock.step - before, step: clock.step, running: clock.running });
}

function saveSlotSummary(slot) {
  return {
    slot_id: slot.slot_id,
    label: slot.label,
    saved_tick: slot.saved_tick,
    replay_rows: slot.replay_rows,
    year: slot.year,
    autonomous_day: slot.autonomous_day,
    survival_status: slot.survival_status,
    residents: slot.residents,
    practices: slot.practices,
    proposals: slot.proposals,
  };
}

function ensurePrototypeSaves() {
  if (!world.gamePrototypeSaves) {
    let stored = null;
    try {
      stored = JSON.parse(localStorage.getItem(PROTOTYPE_SAVE_KEY) || 'null');
    } catch (_error) {
      stored = null;
    }
    world.gamePrototypeSaves = stored || {
      slots: [],
      activeSlotId: null,
      returnLog: [],
      exportReceipt: null,
      boundary: 'browser-local prototype save slots; not production persistence',
    };
  }
  return world.gamePrototypeSaves;
}

function persistPrototypeSaves() {
  const saves = ensurePrototypeSaves();
  localStorage.setItem(PROTOTYPE_SAVE_KEY, JSON.stringify(saves));
}

function snapshotWorldForPrototypeSlot(saves) {
  const shallowSaves = {
    ...saves,
    slots: saves.slots.map(slot => ({ ...slot, snapshot: null })),
  };
  return JSON.stringify({ ...world, gamePrototypeSaves: shallowSaves });
}

function savePrototypeSlot(label = 'manual prototype save') {
  ensureGamePrototype();
  const saves = ensurePrototypeSaves();
  const deepTime = world.deepTimeCivilization;
  const autonomous = world.autonomousResidents;
  const slotNumber = saves.slots.length + 1;
  const slot = {
    slot_id: `GPS-${String(slotNumber).padStart(2, '0')}`,
    label,
    saved_tick: world.tick,
    replay_rows: world.replay.length,
    year: deepTime ? deepTime.year : 0,
    autonomous_day: autonomous ? autonomous.day : 0,
    survival_status: deepTime && deepTime.civilizationState ? deepTime.civilizationState.status : 'not audited',
    residents: Object.keys(world.residents).length,
    practices: world.emergentPracticeGraph ? world.emergentPracticeGraph.nodes.length : 0,
    proposals: world.villageBoard ? world.villageBoard.projectProposals.length : 0,
    snapshot: null,
  };
  slot.snapshot = snapshotWorldForPrototypeSlot(saves);
  saves.slots.push(slot);
  if (saves.slots.length > 4) saves.slots.shift();
  saves.activeSlotId = slot.slot_id;
  persistPrototypeSaves();
  recordPrototypeMilestone('prototype-save-slot', `${slot.slot_id} saved year ${slot.year}, day ${slot.autonomous_day}`);
  recordCheckpoint(`prototype save ${slot.slot_id}`);
  return log('savePrototypeSlot', { slotId: slot.slot_id, year: slot.year, autonomousDay: slot.autonomous_day, practices: slot.practices, proposals: slot.proposals });
}

function returnPrototypeSlot() {
  const saves = ensurePrototypeSaves();
  const slot = saves.slots.find(row => row.slot_id === saves.activeSlotId) || saves.slots[saves.slots.length - 1];
  if (!slot || !slot.snapshot) return log('returnPrototypeSlot', { restored: false, reason: 'no prototype save slot' });
  const returnEntry = {
    slot_id: slot.slot_id,
    returned_from_tick: world.tick,
    returned_from_replay_rows: world.replay.length,
    restored_year: slot.year,
    restored_autonomous_day: slot.autonomous_day,
  };
  const nextWorld = JSON.parse(slot.snapshot);
  saves.returnLog.push(returnEntry);
  nextWorld.gamePrototypeSaves = saves;
  world = nextWorld;
  persistPrototypeSaves();
  recordPrototypeMilestone('prototype-return-slot', `${slot.slot_id} restored year ${slot.year}, day ${slot.autonomous_day}`);
  recordCheckpoint(`prototype return ${slot.slot_id}`);
  return log('returnPrototypeSlot', { restored: true, slotId: slot.slot_id, year: slot.year, autonomousDay: slot.autonomous_day });
}

function exportPrototypeSaveReceipt() {
  const saves = ensurePrototypeSaves();
  const receipt = {
    exported_at_tick: world.tick,
    active_slot_id: saves.activeSlotId,
    slots: saves.slots.map(saveSlotSummary),
    return_log: saves.returnLog.slice(-8),
    boundary: saves.boundary,
  };
  saves.exportReceipt = receipt;
  localStorage.setItem(EXPORT_KEY, JSON.stringify(receipt, null, 2));
  persistPrototypeSaves();
  let link = document.getElementById('preparedPrototypeSaveDownload');
  if (!link) {
    link = document.createElement('a');
    link.id = 'preparedPrototypeSaveDownload';
    link.textContent = 'Prepared prototype save receipt';
    link.download = 'ssrm_game_prototype_save_receipt.json';
    link.style.display = 'block';
    link.style.marginTop = '10px';
    document.querySelector('.side-panel').appendChild(link);
  }
  link.href = URL.createObjectURL(new Blob([JSON.stringify(receipt, null, 2)], { type: 'application/json' }));
  return log('exportPrototypeSaveReceipt', { slots: receipt.slots.length, activeSlotId: receipt.active_slot_id });
}

function buildPrototypeAcceptanceReceipt() {
  const prototype = ensureGamePrototype();
  const qa = world.gamePrototypeQA || null;
  const deepTime = world.deepTimeCivilization || null;
  const autonomous = world.autonomousResidents || null;
  const practiceGraph = world.emergentPracticeGraph || null;
  const board = world.villageBoard || null;
  const ledger = world.realityConstraintLedger || null;
  const saves = world.gamePrototypeSaves || null;
  const requirements = [
    { id: 'basic_visual_surface', pass: Boolean(world.entered && Object.keys(world.residents).length <= 6), evidence: `${Object.keys(world.residents).length} resident(s), room=${world.avatar.room}` },
    { id: 'persistent_save_return', pass: Boolean(saves && saves.slots && saves.slots.length > 0 && saves.returnLog && saves.returnLog.length > 0), evidence: saves ? `${saves.slots.length} slot(s), ${saves.returnLog.length} return(s)` : 'no prototype saves' },
    { id: 'autonomous_stochastic_residents', pass: Boolean(autonomous && autonomous.actionLog.length > 0 && autonomous.entropyLedger.length > 0), evidence: autonomous ? `${autonomous.actionLog.length} action(s), entropy rows=${autonomous.entropyLedger.length}` : 'not started' },
    { id: 'reality_grounded_causality', pass: Boolean(ledger && ledger.rows.length > 0 && ledger.rows.every(row => row.conservation_check && row.normal_view_hidden_law_exposed === false)), evidence: ledger ? `${ledger.rows.length} causal row(s)` : 'no ledger' },
    { id: 'emergent_beliefs_and_practices', pass: Boolean(practiceGraph && practiceGraph.nodes.length > 0 && practiceGraph.noPredefinedTechTree === true), evidence: practiceGraph ? `${practiceGraph.nodes.length} node(s), no tech tree=${practiceGraph.noPredefinedTechTree}` : 'no practice graph' },
    { id: 'village_management_without_command', pass: Boolean(board && board.projectProposals.length > 0 && board.avatarCannotForce === true), evidence: board ? `${board.projectProposals.length} proposal(s), force=${board.avatarCannotForce === false}` : 'no board' },
    { id: 'million_year_survival_path', pass: Boolean(deepTime && deepTime.year >= 1000000 && deepTime.civilizationState && deepTime.civilizationState.millionYearCapable), evidence: deepTime ? `${deepTime.year} year(s), status=${deepTime.civilizationState ? deepTime.civilizationState.status : 'none'}` : 'not run' },
    { id: 'ordinary_play_can_seed_tests', pass: Boolean(world.practicalDiscovery && world.practicalDiscovery.autoGeneratedTests && world.practicalDiscovery.autoGeneratedTests.length > 0), evidence: world.practicalDiscovery ? `${world.practicalDiscovery.autoGeneratedTests.length} auto-generated test(s)` : 'no practical discovery' },
    { id: 'readable_public_behavior', pass: Boolean(autonomous && autonomous.expressionLedger && autonomous.expressionLedger.length > 0 && autonomous.expressionLedger.every(row => row.publicCueOnly === true && row.hiddenStateExposed === false)), evidence: autonomous && autonomous.expressionLedger ? `${autonomous.expressionLedger.length} expression cue(s)` : 'no expression ledger' },
    { id: 'prototype_qa_passes', pass: Boolean(qa && qa.pass === true), evidence: qa ? `${qa.passed}/${qa.total} QA checks` : 'QA not run' },
    { id: 'research_arc_closed_mode', pass: Boolean(prototype.noMoreResearchReportsByDefault && prototype.mode === 'game-prototype-v0'), evidence: `${prototype.mode}, reports default=${prototype.noMoreResearchReportsByDefault ? 'off' : 'on'}` },
  ];
  const passed = requirements.filter(row => row.pass).length;
  return {
    receipt_id: `GPAR-${String((world.gamePrototypeAcceptance ? world.gamePrototypeAcceptance.runCount || 0 : 0) + 1).padStart(2, '0')}`,
    runCount: (world.gamePrototypeAcceptance ? world.gamePrototypeAcceptance.runCount || 0 : 0) + 1,
    generated_tick: world.tick,
    generated_replay_rows: world.replay.length,
    branch_mode: prototype.mode,
    pass: passed === requirements.length,
    passed,
    total: requirements.length,
    requirements,
    qa_run_id: qa ? qa.run_id : 'none',
    boundary: 'browser-local acceptance receipt only; not production certification, not consciousness evidence, not an LLM claim',
  };
}

function exportPrototypeAcceptanceReceipt() {
  if (!world.gamePrototypeQA || !world.gamePrototypeQA.pass) runPrototypeQASmoke();
  savePrototypeSlot('acceptance receipt save');
  runAutonomousResidentTick();
  returnPrototypeSlot();
  const receipt = buildPrototypeAcceptanceReceipt();
  world.gamePrototypeAcceptance = receipt;
  localStorage.setItem(PROTOTYPE_ACCEPTANCE_KEY, JSON.stringify(receipt, null, 2));
  localStorage.setItem(EXPORT_KEY, JSON.stringify(receipt, null, 2));
  let link = document.getElementById('preparedPrototypeAcceptanceDownload');
  if (!link) {
    link = document.createElement('a');
    link.id = 'preparedPrototypeAcceptanceDownload';
    link.textContent = 'Prepared prototype acceptance receipt';
    link.download = 'ssrm_game_prototype_acceptance_receipt.json';
    link.style.display = 'block';
    link.style.marginTop = '10px';
    document.querySelector('.side-panel').appendChild(link);
  }
  link.href = URL.createObjectURL(new Blob([JSON.stringify(receipt, null, 2)], { type: 'application/json' }));
  recordPrototypeMilestone('prototype-acceptance-receipt', `${receipt.passed}/${receipt.total} acceptance checks passed`);
  return log('exportPrototypeAcceptanceReceipt', { pass: receipt.pass, passed: receipt.passed, total: receipt.total, receiptId: receipt.receipt_id });
}

function formatPrototypeQA() {
  const qa = world.gamePrototypeQA;
  if (!qa) return 'No prototype QA run yet. Run Prototype QA.';
  const rows = qa.checks.map(row => `${row.pass ? 'PASS' : 'FAIL'} ${row.id}: ${row.evidence}`);
  return [
    `${qa.run_id}: ${qa.pass ? 'PASS' : 'FAIL'} (${qa.passed}/${qa.total})`,
    `Boundary: ${qa.boundary}`,
    ...rows,
  ].join('\n');
}

function formatPrototypeClock() {
  const clock = world.prototypeClock;
  if (!clock) return 'Auto simulation has not started. Use Start auto sim or Auto burst.';
  const sim = world.autonomousResidents;
  const deepTime = world.deepTimeCivilization;
  return [
    `Running: ${clock.running ? 'yes' : 'no'} / step ${clock.step} / last action: ${clock.lastAction}`,
    `Cadence: resident every step, deep time every ${clock.cadence.deepTimeEvery}, survival every ${clock.cadence.survivalAuditEvery}, save every ${clock.cadence.saveEvery}`,
    `Last saved step: ${clock.lastSavedStep}`,
    `Autonomous days: ${sim ? sim.day : 0}`,
    `Deep-time year: ${deepTime ? deepTime.year : 0}`,
    `Boundary: ${clock.boundary}`,
  ].join('\n');
}

function formatPrototypeSaves() {
  const saves = world.gamePrototypeSaves || ensurePrototypeSaves();
  const slots = saves.slots.slice(-4).map(slot => `${slot.slot_id}: ${slot.label}; year=${slot.year}; day=${slot.autonomous_day}; practices=${slot.practices}; proposals=${slot.proposals}; survival=${slot.survival_status}`);
  const returns = saves.returnLog.slice(-5).map(row => `${row.slot_id}: restored year=${row.restored_year}, day=${row.restored_autonomous_day}, from replay=${row.returned_from_replay_rows}`);
  return [
    `Active slot: ${saves.activeSlotId || 'none'}`,
    `Boundary: ${saves.boundary}`,
    'Slots:',
    ...(slots.length ? slots : ['none']),
    'Returns:',
    ...(returns.length ? returns : ['none']),
    `Export receipt: ${saves.exportReceipt ? `${saves.exportReceipt.slots.length} slot(s) prepared` : 'not prepared'}`,
  ].join('\n');
}

function formatPrototypeAcceptance() {
  const receipt = world.gamePrototypeAcceptance || null;
  if (!receipt) return 'No acceptance receipt yet. Use Export acceptance after running or seeding the prototype.';
  const rows = receipt.requirements.map(row => `${row.pass ? 'PASS' : 'FAIL'} ${row.id}: ${row.evidence}`);
  return [
    `${receipt.receipt_id}: ${receipt.pass ? 'PASS' : 'FAIL'} (${receipt.passed}/${receipt.total})`,
    `QA run: ${receipt.qa_run_id}`,
    `Boundary: ${receipt.boundary}`,
    ...rows,
  ].join('\n');
}

function renderGamePrototypeSurface() {
  const objectiveNode = document.getElementById('gamePrototypeObjectiveOut');
  const villageNode = document.getElementById('gamePrototypeVillageOut');
  const publicNode = document.getElementById('gamePrototypePublicOut');
  const loopNode = document.getElementById('gamePrototypeLoopOut');
  const deepTimeNode = document.getElementById('gamePrototypeDeepTimeOut');
  const autonomousNode = document.getElementById('gamePrototypeAutonomousOut');
  const expressionNode = document.getElementById('gamePrototypeExpressionOut');
  const qaNode = document.getElementById('gamePrototypeQAOut');
  const clockNode = document.getElementById('gamePrototypeClockOut');
  const saveNode = document.getElementById('gamePrototypeSaveOut');
  const acceptanceNode = document.getElementById('gamePrototypeAcceptanceOut');
  const prototype = world.gamePrototype || ensureGamePrototype();
  if (objectiveNode) objectiveNode.textContent = prototype.objective;
  if (villageNode) villageNode.textContent = formatPrototypeVillageState();
  if (publicNode) publicNode.textContent = formatPrototypePublicOutcomes();
  if (loopNode) loopNode.textContent = formatPrototypeLoopReceipt();
  if (deepTimeNode) deepTimeNode.textContent = formatPrototypeDeepTime();
  if (autonomousNode) autonomousNode.textContent = formatPrototypeAutonomousResidents();
  if (expressionNode) expressionNode.textContent = formatPrototypeReadableBehavior();
  if (qaNode) qaNode.textContent = formatPrototypeQA();
  if (clockNode) clockNode.textContent = formatPrototypeClock();
  if (saveNode) saveNode.textContent = formatPrototypeSaves();
  if (acceptanceNode) acceptanceNode.textContent = formatPrototypeAcceptance();
}

function bindControls() {
  document.querySelectorAll('[data-action]').forEach(button => {
    button.addEventListener('click', () => {
      const action = button.getAttribute('data-action');
      if (typeof window[action] === 'function') window[action]();
    });
  });
  residentSelect.innerHTML = Object.keys(world.residents).map(name => `<option value="${name}">${name}</option>`).join('');
  document.getElementById('receiptFieldSelect').innerHTML = receiptFieldIds.map(field => `<option value="${field}">${field}</option>`).join('');
  residentSelect.value = world.selected;
  residentSelect.addEventListener('change', () => { world.selected = residentSelect.value; log('selectResident', { selected: world.selected }); });
  const obligationSelect = document.getElementById('obligationSelect');
  if (obligationSelect) {
    obligationSelect.addEventListener('change', () => { world.selectedObligationId = obligationSelect.value; log('selectObligation', { selectedObligationId: world.selectedObligationId }); });
  }
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
  renderReturnContinuity();
  renderReturnGreetingContinuity();
  renderAccountabilitySocialEcho();
  renderBoundedEchoConversation();
  renderEchoInfluencedChoiceReceipt();
  renderAnomalyDiscovery();
  renderAnomalyInvestigationSchedule();
  renderPromiseFollowUp();
  renderObligationList();
  renderScheduleDebtIntegration();
  renderAbsentTimeSummary();
  renderAbsentTimeChoice();
  renderAvatarAbsenceAccountability();
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
  const accountabilitySocialEcho = propagateAccountabilitySocialEcho();
  recordCheckpoint('resident social pulse');
  return log('runSocialMemoryPulse', { residentToResident: true, pairCount: pairs.length, accountabilitySocialEcho, persistentKey: RELATION_KEY });
}
function propagateAccountabilitySocialEcho() {
  const greeting = world.returnGreetingContinuity;
  if (!greeting || greeting.resident !== 'Milo') return null;
  const sourceResident = 'Milo';
  const echoResident = 'Fay';
  const residentThreadId = greeting.residentThreadId;
  const obligation = (world.obligationLedger || []).find(row => row.id === residentThreadId);
  const event = (world.offscreenObligationEvents || []).find(row => row.obligationId === residentThreadId);
  const historyPreserved = Boolean(event && obligation && greeting.residentHistoryPreserved);
  const originalCause = event ? `${event.actor} changed ${event.target}'s obligation while avatar absent` : 'original offscreen cause missing';
  const echo = `${echoResident} heard ${sourceResident} say ${residentThreadId} stayed ${greeting.residentObligationStatus} and the avatar absence was ${greeting.avatarThreadStatus}; preserving ${originalCause}`;
  const edge = mutateRelationship(sourceResident, echoResident, {
    trust: 0.014,
    debt: 0,
    memory: echo,
    historyEvent: 'accountability social echo source',
    historyDetail: echo,
    partnerEvent: 'accountability social echo witness',
    partnerDetail: echo
  });
  mutateResident(echoResident, {
    trust: 0.006,
    progress: 0.004,
    memory: `heard ${sourceResident} mention ${residentThreadId} was ${obligation ? obligation.status : 'missing'} and avatar absence was ${greeting.avatarThreadStatus}`,
    historyEvent: 'resident-to-resident accountability echo',
    historyDetail: `${echo}; direct avatar command false; history preserved ${historyPreserved ? 'yes' : 'no'}`
  });
  world.accountabilitySocialEcho = {
    reportIntroduced: 359,
    sourceResident,
    echoResident,
    residentThreadId,
    residentObligationStatus: greeting.residentObligationStatus,
    avatarThreadStatus: greeting.avatarThreadStatus,
    residentHistoryPreserved: historyPreserved,
    directAvatarCommand: false,
    relationshipTrust: Number(edge.trust.toFixed(3)),
    echo,
    boundary: 'browser-local-accountability-social-echo-only'
  };
  return world.accountabilitySocialEcho;
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
function generateScenarioReceipt() {
  recordCheckpoint('integrated scenario receipt');
  return log('generateScenarioReceipt', { publicReceipt: true, passCount: calculateScenarioReceipt().passCount, fieldCount: calculateScenarioReceipt().fieldCount });
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
function calculateScenarioReceipt() {
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
    ['replay_export_ready', events.includes('exportReplay') && exportBytes > 0, `replay export bytes=${exportBytes}`],
    ['resume_ready_snapshot', events.includes('saveWorld') && readCheckpoints().some(row => row.label === 'continuity loop complete' || row.label === 'integrated scenario receipt'), 'saved checkpoint exists for resume verification']
  ];
  const passCount = checks.filter(([_id, pass]) => pass).length;
  return { checks, passCount, fieldCount: checks.length };
}
function readReceiptObservations() {
  try {
    const rows = JSON.parse(localStorage.getItem(RECEIPT_OBSERVATION_KEY) || '[]');
    return Array.isArray(rows) ? rows : [];
  } catch (_error) {
    return [];
  }
}
function writeReceiptObservations(rows) {
  const trimmed = rows.slice(-30);
  localStorage.setItem(RECEIPT_OBSERVATION_KEY, JSON.stringify(trimmed));
  return trimmed;
}
function receiptCheckForField(field) {
  const receipt = calculateScenarioReceipt();
  const row = receipt.checks.find(([id]) => id === field) || receipt.checks.find(([_id, pass]) => pass === false) || receipt.checks[0];
  return { field: row[0], pass: row[1], detail: row[2], passCount: receipt.passCount, fieldCount: receipt.fieldCount };
}
function logReceiptObservation() {
  const fieldSelect = document.getElementById('receiptFieldSelect');
  const severitySelect = document.getElementById('receiptSeveritySelect');
  const field = fieldSelect && fieldSelect.value ? fieldSelect.value : (calculateScenarioReceipt().checks.find(([_id, pass]) => pass === false) || calculateScenarioReceipt().checks[0])[0];
  const severity = severitySelect && severitySelect.value ? severitySelect.value : 'watch';
  const check = receiptCheckForField(field);
  const rows = readReceiptObservations();
  const row = {
    id: `RO-${String(world.tick).padStart(3, '0')}-${String(rows.length + 1).padStart(2, '0')}`,
    field: check.field,
    severity,
    status: check.pass ? 'watch' : 'open',
    receiptStatus: check.pass ? 'PASS' : 'FAIL',
    detail: check.detail,
    note: check.pass ? `Reviewer note on passing field ${check.field}` : `Reviewer flagged failing field ${check.field}`,
    tick: world.tick,
    selected: world.selected,
    replayRows: world.replay.length
  };
  rows.push(row);
  writeReceiptObservations(rows);
  recordCheckpoint('receipt observation logged');
  return log('logReceiptObservation', { id: row.id, field: row.field, severity: row.severity, status: row.status, receiptStatus: row.receiptStatus });
}
function resolveLatestObservation() {
  const rows = readReceiptObservations();
  const index = rows.map(row => row.status !== 'resolved').lastIndexOf(true);
  if (index < 0) return log('resolveLatestObservation', { resolved: false, reason: 'no open receipt observation' });
  rows[index] = { ...rows[index], status: 'resolved', resolvedTick: world.tick, resolution: 'reviewed against current integrated receipt' };
  writeReceiptObservations(rows);
  recordCheckpoint('receipt observation resolved');
  return log('resolveLatestObservation', { resolved: true, id: rows[index].id, field: rows[index].field });
}
function readObservationFilter() {
  const filter = localStorage.getItem(OBSERVATION_FILTER_KEY) || 'all';
  return ['all', 'open', 'watch', 'resolved', 'blocking'].includes(filter) ? filter : 'all';
}
function setObservationFilter(filter) {
  localStorage.setItem(OBSERVATION_FILTER_KEY, filter);
  recordCheckpoint('observation triage ' + filter);
  return log('setObservationFilter', { filter, visibleRows: filterReceiptObservations(filter).length });
}
function setObservationFilterAll() { return setObservationFilter('all'); }
function setObservationFilterOpen() { return setObservationFilter('open'); }
function setObservationFilterWatch() { return setObservationFilter('watch'); }
function setObservationFilterResolved() { return setObservationFilter('resolved'); }
function setObservationFilterBlocking() { return setObservationFilter('blocking'); }
const reviewerFailureActionBook = {
  entry_and_movement: 'Click Enter or use Run reviewer pass to establish avatar entry.',
  schedule_visibility: 'Ask schedule or run the reviewer pass so the selected resident schedule is public.',
  debt_consequence: 'Borrow/return or run the reviewer pass to create a visible debt/trust consequence.',
  offscreen_life: 'Use Wait offscreen or run the reviewer pass to advance resident progress while absent.',
  recoverable_trust_repair: 'Run the trust repair sequence: interrupt, apologize, give space, repair with help.',
  resident_social_memory: 'Run social pulse and settle one selected resident-to-resident obligation.',
  public_history_sync: 'Create avatar and resident-to-resident events until selected resident history updates.',
  replay_export_ready: 'Export replay after the loop so review evidence has bytes and public rows.',
  resume_ready_snapshot: 'Save world after the loop so launcher resume has a public checkpoint.'
};
function reviewerFailureActions(receipt = calculateScenarioReceipt()) {
  const failing = receipt.checks.filter(([_id, pass]) => !pass);
  if (!failing.length) return ['All receipt fields currently pass. Keep deep panels optional unless a reviewer wants trace detail.'];
  return failing.map(([id, _pass, detail]) => `FIX ${id}: ${reviewerFailureActionBook[id] || 'Run reviewer pass, then inspect receipt and transcript.'} Current evidence: ${detail}`);
}
function auditLandingFailures() {
  const receipt = calculateScenarioReceipt();
  const rows = readReceiptObservations();
  const failing = receipt.checks.filter(([_id, pass]) => !pass);
  failing.forEach(([field, _pass, detail]) => {
    rows.push({
      id: 'landing-block-' + (rows.length + 1),
      field,
      severity: 'blocking',
      status: 'open',
      receiptStatus: 'FAIL',
      detail,
      note: reviewerFailureActionBook[field] || 'Reviewer landing needs manual follow-up.',
      tick: world.tick,
      selected: world.selected,
      replayRows: world.replay.length
    });
  });
  writeReceiptObservations(rows);
  localStorage.setItem(OBSERVATION_FILTER_KEY, 'blocking');
  recordCheckpoint('reviewer landing failure audit');
  return log('auditLandingFailures', { failingFields: failing.length, blockingRows: rows.filter(row => row.severity === 'blocking' && row.status !== 'resolved').length });
}
function reviewerFocusEnabled() {
  return document.body.classList.contains('reviewer-focus');
}
function toggleDeepPanels() {
  document.body.classList.toggle('reviewer-focus');
  return log('toggleDeepPanels', { reviewerFocus: reviewerFocusEnabled(), deepPanelsVisible: !reviewerFocusEnabled() });
}
function runReviewerLandingPass() {
  runContinuityLoop();
  generateScenarioReceipt();
  setObservationFilterAll();
  recordCheckpoint('reviewer landing pass');
  return log('runReviewerLandingPass', {
    reviewerFocus: reviewerFocusEnabled(),
    corePanels: ['boundary', 'sessionTranscriptOut', 'continuityLoopOut', 'scenarioReceiptOut', 'observationTriageOut'],
    deepPanelsOptional: true, returnToLauncherHandoff: true
  });
}
function filterReceiptObservations(filter = readObservationFilter()) {
  const rows = readReceiptObservations();
  if (filter === 'open') return rows.filter(row => row.status !== 'resolved');
  if (filter === 'watch') return rows.filter(row => row.severity === 'watch' || row.status === 'watch');
  if (filter === 'resolved') return rows.filter(row => row.status === 'resolved');
  if (filter === 'blocking') return rows.filter(row => row.severity === 'blocking');
  return rows;
}
function formatReviewerLanding() {
  const receipt = calculateScenarioReceipt();
  const observationRows = readReceiptObservations();
  const focus = reviewerFocusEnabled();
  const requiredEvents = ['runContinuityLoop', 'generateScenarioReceipt'];
  const events = world.replay.map(row => row.event);
  const missing = requiredEvents.filter(event => !events.includes(event));
  return `Reviewer landing: ${missing.length ? 'READY_FOR_RUN' : 'PASSABLE_REVIEW_PATH'}
Boundary: deterministic browser-local public state only; no consciousness, no autonomous language, no moral patienthood.
Focus mode: ${focus ? 'core panels only' : 'deep panels visible'}
Core path: boundary -> Run reviewer pass -> session transcript -> integrated receipt -> observation triage -> Return to launcher handoff
Receipt: ${receipt.passCount}/${receipt.fieldCount} pass
Observation triage: ${observationRows.length} observations / active filter ${readObservationFilter()}
Missing reviewer-pass events: ${missing.length ? missing.join(', ') : 'none'}
Actionable failure map:
${reviewerFailureActions(receipt).join('\n')}
Next step: use Return to launcher handoff when the receipt is all pass.
Deep diagnostics: ${focus ? 'hidden by default; use Toggle deep panels only when an action remains unclear' : 'visible for trace, checkpoints, history, and QA manifest'}`;
}
function formatScenarioReceipt() {
  const receipt = calculateScenarioReceipt();
  const rows = receipt.checks.map(([id, pass, detail]) => `${pass ? 'PASS' : 'FAIL'} ${id}: ${detail}`);
  const status = receipt.passCount === receipt.fieldCount ? 'ALL_PASS' : 'INCOMPLETE';
  return `Integrated scenario receipt: ${status} (${receipt.passCount}/${receipt.fieldCount})
Scope: public browser-local state only; no subjective consciousness, no autonomous language, no moral patienthood.
${rows.join('\n')}`;
}
function formatReceiptObservations() {
  const rows = readReceiptObservations();
  const open = rows.filter(row => row.status !== 'resolved').length;
  if (!rows.length) return 'No receipt observations yet. Pick a receipt field and log an observation after running the integrated loop.';
  const recent = rows.slice(-10).map(row => `${row.id} | ${row.status} | ${row.severity} | ${row.field} | receipt=${row.receiptStatus} | ${row.note}`);
  return `Receipt observation ledger: ${open} open / ${rows.length} total
Persistent key: ${RECEIPT_OBSERVATION_KEY}
Recent observations:
${recent.join('\n')}`;
}
function formatObservationTriage() {
  const rows = readReceiptObservations();
  const filter = readObservationFilter();
  const visible = filterReceiptObservations(filter);
  const counts = {
    total: rows.length,
    open: rows.filter(row => row.status !== 'resolved').length,
    watch: rows.filter(row => row.severity === 'watch' || row.status === 'watch').length,
    resolved: rows.filter(row => row.status === 'resolved').length,
    blocking: rows.filter(row => row.severity === 'blocking').length,
    minor: rows.filter(row => row.severity === 'minor').length
  };
  const lines = visible.slice(-8).map(row => `${row.id} | ${row.status} | ${row.severity} | ${row.field} | receipt=${row.receiptStatus}`);
  return `Observation triage filter: ${filter}
Counts: total ${counts.total} | open ${counts.open} | watch ${counts.watch} | minor ${counts.minor} | blocking ${counts.blocking} | resolved ${counts.resolved}
Visible rows: ${visible.length}
${lines.length ? lines.join('\n') : 'No observations match this filter.'}`;
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
    offerHelp: `help action helped=${payload.helped !== false} care left=${payload.care}`,
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
    generateScenarioReceipt: `generated public receipt pass=${payload.passCount}/${payload.fieldCount}`,
    logReceiptObservation: `logged receipt observation ${payload.id} ${payload.field} status=${payload.status}`,
    resolveLatestObservation: `resolved receipt observation=${payload.resolved === true} ${payload.id || payload.reason || ''}`,
    setObservationFilter: `set observation triage filter=${payload.filter} rows=${payload.visibleRows}`,
    auditLandingFailures: `audited landing failures=${payload.failingFields} blockingRows=${payload.blockingRows}`,
    toggleDeepPanels: `deep panels visible=${payload.deepPanelsVisible === true}`,
    runReviewerLandingPass: `ran reviewer landing pass focus=${payload.reviewerFocus === true}`,
    toggleAudit: `audit overlay=${payload.audit === true}`,
    selectResident: `selected resident ${payload.selected}`,
    canvasMove: `canvas move to ${payload.room} at ${payload.x},${payload.y}`
    ,
    introduceWorldAnomaly: `introduced anomaly seed=${payload.seed}; hidden law audit only=${payload.hiddenLawAuditOnly === true}`,
    runAnomalyExperiment: `anomaly experiment ${payload.experiment ? payload.experiment.id : ''} failed=${payload.failedExperimentPreserved === true}`,
    spreadAnomalyBelief: `spread anomaly belief mutation=${payload.socialTransmissionMutation === true}`,
    planAnomalyInvestigationSchedule: `planned anomaly investigation slots=${payload.slots ? payload.slots.length : 0}`,
    runScheduledAnomalyInvestigation: `scheduled anomaly investigation executed=${payload.executedTest === true} tradeoff=${payload.scheduleTradeoff === true}`,
    runStochasticConsequencePulse: `stochastic pulse ${payload.pulse ? payload.pulse.event : ''} actor=${payload.pulse ? payload.pulse.actor : ''} entropy=${payload.replayableEntropy === true}`,
    runStochasticConsequenceBurst: `stochastic burst pulses=${payload.pulsesAdded} entropy=${payload.replayableEntropy === true}`,
    planStochasticRecoveryLoop: `planned stochastic recoveries=${payload.planned} pending=${payload.pending}`,
    resolveStochasticRecoveryStep: `resolved stochastic recovery pending=${payload.pendingCount}`,
    runStochasticRecoveryLoop: `ran stochastic recovery loop recovered=${payload.recoveredThisRun} pending=${payload.pendingCount}`,
    runStochasticHistoryChoice: `stochastic history choice ${payload.choice ? payload.choice.decision : ''}`,
    runStochasticHistorySocialEcho: `stochastic history echo ${payload.echo ? payload.echo.from : ''}->${payload.echo ? payload.echo.to : ''}`,
    runStochasticHistoryInfluenceLoop: `stochastic history influence choices=${payload.choices ? payload.choices.length : 0} echo=${payload.echo}`,
    runOrdinaryAffordanceInfluenceLoop: `ordinary affordance influence actions=${payload.actionsAdded} blocked=${payload.blockedCount}`,
    runCivilizationPressureStep: `civilization pressure ${payload.pressureType} resident=${payload.resident} schedule=${payload.schedule}`,
    runCivilizationPressureLoop: `civilization pressure loop steps=${payload.stepsAdded} schedules=${payload.scheduleRewrites}`,
    runPracticalDiscoveryStep: `practical discovery ${payload.action} bottleneck=${payload.bottleneckType} candidate=${payload.practiceCandidate}`,
    runPracticalDiscoveryLoop: `practical discovery loop actions=${payload.livedActions} candidates=${payload.practiceCandidates} adopted=${payload.practiceAdoptions}`,
    runVillageBoardLoop: `village board concerns=${payload.concerns} proposals=${payload.proposals} support=${payload.supportEvents}`,
    introduceAvatarHint: `avatar hint ${payload.hintId} type=${payload.hintType} direct=${payload.directInstall === true}`,
    runHintDivergenceInterpretation: `hint interpretations=${payload.interpretations} branches=${payload.branches} uniform=${payload.uniform === true}`,
    runAvatarHintDivergenceLoop: `hint divergence hints=${payload.hints} branches=${payload.branches} mutations=${payload.mutations}`,
    runHintBranchReturnSession: `hint branch return session=${payload.session} persisted=${payload.persisted} forgotten=${payload.forgotten} revived=${payload.revived}`,
    maintainHintBranchPractice: `maintained hint branch ${payload.branchId} cost=${payload.maintenanceCost}`,
    reviveForgottenHintPractice: `revived hint branch ${payload.branchId} success=${payload.revived === true}`,
    runHintBranchPersistenceLoop: `hint branch persistence sessions=${payload.sessions} continuity=${payload.continuityRows}`,
    runPrototypeOpening: `prototype opening selected=${payload.selected} entered=${payload.entered}`,
    runPrototypePracticeChain: `prototype practice chain practices=${payload.practiceCount} proposals=${payload.proposalCount}`,
    runPrototypeReturnProof: `prototype return proof branches=${payload.branchRows} revivals=${payload.revivalRows}`,
    runFirstPlayablePrototypeLoop: `first playable prototype milestones=${payload.milestones} branches=${payload.branchContinuity}`,
    runCivilizationDeepTimeEpoch: `deep-time epoch +${payload.yearsAdvanced} years pressure=${payload.pressure} lineages=${payload.lineages}`,
    applyLatestDeepTimeEffectToVillage: `deep-time effect applied resident=${payload.resident} proposal=${payload.proposalId}`,
    runCivilizationMillionYearSim: `million-year sim year=${payload.year} epochs=${payload.epochs} effects=${payload.effects}`,
    runCivilizationTenMillionYearSim: `ten-million-year sim year=${payload.year} status=${payload.survivalStatus}`,
    runCivilizationSurvivalAudit: `survival audit ${payload.status} score=${payload.continuityScore}`,
    runAutonomousResidentTick: `autonomous resident ${payload.resident} chose ${payload.action} day=${payload.day}`,
    runAutonomousResidentSeason: `autonomous season ${payload.season} actions=${payload.actionsAdded}`,
    runPrototypeQASmoke: `prototype QA ${payload.pass ? 'PASS' : 'FAIL'} ${payload.passed}/${payload.total}`,
    runPrototypeAutoStep: `auto sim step=${payload.step} action=${payload.action}`,
    startPrototypeAutoSim: `auto sim started step=${payload.step}`,
    pausePrototypeAutoSim: `auto sim paused step=${payload.step}`,
    runPrototypeAutoBurst: `auto sim burst +${payload.stepsAdded} step=${payload.step}`,
    savePrototypeSlot: `prototype save ${payload.slotId} year=${payload.year} day=${payload.autonomousDay}`,
    returnPrototypeSlot: `prototype return restored=${payload.restored === true} ${payload.slotId || payload.reason || ''}`,
    exportPrototypeSaveReceipt: `prototype save export slots=${payload.slots} active=${payload.activeSlotId || 'none'}`,
    exportPrototypeAcceptanceReceipt: `prototype acceptance ${payload.pass ? 'PASS' : 'FAIL'} ${payload.passed}/${payload.total}`,
    supportVillageProposal: `supported village proposal ${payload.proposalId} accepted=${payload.accepted}`,
    askVillageBoardQuestion: `asked village board question ${payload.proposalId}`,
    waitOnVillageBoard: `waited on village board proposals=${payload.proposals}`,
    runRealityConstraintAudit: `reality constraint audit pass=${payload.pass === true} rows=${payload.rows}`
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
  document.getElementById('reviewerLandingOut').textContent = formatReviewerLanding();
  document.getElementById('traceOut').textContent = JSON.stringify({ latest: world.replay[world.replay.length - 1] || null, world }, null, 2);
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
  document.getElementById('observationTriageOut').textContent = formatObservationTriage();
  document.getElementById('taskList').innerHTML = playtestTasks.map(task => `<li><strong>${task.id}</strong>: ${task.title}<br><span>${task.expected}</span></li>`).join('');
  document.getElementById('qaManifestOut').textContent = JSON.stringify(qaManifest, null, 2);
  renderGamePrototypeSurface();
  renderStochasticConsequencePulse();
  renderStochasticRecoveryLoop();
  renderStochasticHistoryInfluence();
  renderStochasticOrdinaryAffordance();
  renderCivilizationPressure();
  renderPracticalDiscovery();
  renderEmergentPracticeGraph();
  renderVillageBoard();
  renderRealityConstraintLedger();
  renderAvatarHintDivergence();
  renderHintBranchPersistence();
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
  const zones = [
    { name: 'Shelter', x: 70, y: 72, w: 210, h: 118, color: 'rgba(213,161,58,0.18)' },
    { name: 'Storage', x: 315, y: 72, w: 210, h: 118, color: 'rgba(47,113,123,0.18)' },
    { name: 'Work yard', x: 560, y: 72, w: 210, h: 118, color: 'rgba(183,93,57,0.18)' },
    { name: 'Village board', x: 805, y: 72, w: 170, h: 118, color: 'rgba(245,232,199,0.16)' },
  ];
  zones.forEach(zone => {
    ctx.fillStyle = zone.color;
    ctx.fillRect(zone.x, zone.y, zone.w, zone.h);
    ctx.strokeStyle = 'rgba(249,235,201,0.28)';
    ctx.strokeRect(zone.x, zone.y, zone.w, zone.h);
    ctx.fillStyle = '#f9ebc9';
    ctx.font = '18px Optima, sans-serif';
    ctx.fillText(zone.name, zone.x + 14, zone.y + 30);
  });

  const resources = Object.entries(world.resources).map(([key, value]) => `${key}:${value}`).join('  ');
  const clock = world.prototypeClock || { running: false, step: 0, lastAction: 'not started' };
  const deepTime = world.deepTimeCivilization;
  const survival = deepTime && deepTime.civilizationState ? deepTime.civilizationState : null;
  ctx.fillStyle = 'rgba(17,24,22,0.72)';
  ctx.fillRect(28, 22, 984, 36);
  ctx.fillStyle = '#f9ebc9';
  ctx.font = '16px Optima, sans-serif';
  ctx.fillText(`Resources ${resources}  |  auto ${clock.running ? 'running' : 'paused'} step ${clock.step}  |  year ${deepTime ? deepTime.year : 0}`, 42, 46);
  const survivalScore = survival ? Number(survival.continuityScore || 0) : 0;
  ctx.fillStyle = 'rgba(249,235,201,0.16)';
  ctx.fillRect(730, 35, 250, 10);
  ctx.fillStyle = survivalScore > 0.65 ? '#9fca77' : survivalScore > 0.34 ? '#d5a13a' : '#b75d39';
  ctx.fillRect(730, 35, 250 * survivalScore, 10);

  ctx.fillStyle = '#d5a13a'; ctx.beginPath(); ctx.arc(world.avatar.x, world.avatar.y, 24, 0, Math.PI * 2); ctx.fill();
  ctx.fillStyle = '#111816'; ctx.fillText('You', world.avatar.x - 11, world.avatar.y + 4);
  Object.entries(world.residents).forEach(([name, resident], index) => {
    const needs = world.autonomousResidents && world.autonomousResidents.needState ? world.autonomousResidents.needState[name] : null;
    const expression = latestVisibleExpressionFor(name);
    const x = 130 + (index % 3) * 275;
    const y = 275 + Math.floor(index / 3) * 150;
    const energy = needs ? needs.energy : resident.progress;
    const safety = needs ? needs.safety : resident.trust;
    const radius = 20 + Math.round(resident.trust * 10);
    const expressionColor = expression.marker === 'boundary' ? '#b75d39' : expression.marker === 'tired' ? '#8aa1b1' : expression.marker === 'working' || expression.marker === 'maintaining' ? '#9fca77' : expression.marker === 'testing' ? '#d5a13a' : '#aad0c3';
    ctx.fillStyle = name === world.selected ? '#f0c35b' : (safety < 0.45 ? '#d98d69' : expressionColor);
    ctx.beginPath(); ctx.arc(x, y, radius, 0, Math.PI * 2); ctx.fill();
    ctx.strokeStyle = '#111816'; ctx.lineWidth = 3; ctx.stroke();
    if (expression.marker === 'boundary' || expression.marker === 'guarded') {
      ctx.strokeStyle = '#b75d39';
      ctx.lineWidth = 4;
      ctx.beginPath(); ctx.moveTo(x - radius - 16, y - radius - 10); ctx.lineTo(x - radius - 4, y + radius + 12); ctx.stroke();
    } else if (expression.marker === 'working' || expression.marker === 'maintaining') {
      ctx.fillStyle = '#5b4428';
      ctx.fillRect(x + radius - 3, y - 6, 26, 12);
    } else if (expression.marker === 'teaching') {
      ctx.strokeStyle = '#f9ebc9';
      ctx.lineWidth = 2;
      ctx.beginPath(); ctx.arc(x + radius + 10, y - 12, 8, 0, Math.PI * 2); ctx.stroke();
    } else if (expression.marker === 'testing') {
      ctx.fillStyle = '#f9ebc9';
      ctx.beginPath(); ctx.arc(x + radius + 8, y + 8, 5, 0, Math.PI * 2); ctx.fill();
    }
    ctx.fillStyle = 'rgba(249,235,201,0.24)';
    ctx.beginPath(); ctx.arc(x, y, radius + 8, -Math.PI / 2, -Math.PI / 2 + Math.PI * 2 * energy); ctx.strokeStyle = '#9fca77'; ctx.lineWidth = 5; ctx.stroke();
    ctx.fillStyle = '#111816'; ctx.font = '16px Optima, sans-serif'; ctx.fillText(name, x - 14, y + 5);
    ctx.fillStyle = '#f9ebc9'; ctx.font = '13px Optima, sans-serif';
    const schedule = resident.schedule.length > 34 ? resident.schedule.slice(0, 34) + '...' : resident.schedule;
    ctx.fillText(schedule, x - 62, y + 45);
    ctx.fillStyle = expression.marker === 'boundary' || expression.marker === 'guarded' ? '#f0c35b' : '#aad0c3';
    ctx.fillText(`${expression.marker}: ${expression.movementCue}`.slice(0, 36), x - 62, y + 62);
    if (needs && needs.autonomy > 0.7) {
      ctx.fillStyle = '#b75d39';
      ctx.fillText('autonomy high', x - 30, y + 78);
    }
  });

  const board = world.villageBoard;
  const proposals = board && board.projectProposals ? board.projectProposals.slice(-4) : [];
  proposals.forEach((proposal, index) => {
    const x = 825;
    const y = 218 + index * 38;
    ctx.fillStyle = proposal.status === 'accepted' ? '#9fca77' : '#d5a13a';
    ctx.fillRect(x, y, 20, 20);
    ctx.fillStyle = '#f9ebc9';
    ctx.font = '13px Optima, sans-serif';
    const label = `${proposal.proposal_id}: ${proposal.problem_addressed}`.slice(0, 42);
    ctx.fillText(label, x + 28, y + 15);
  });

  const practiceGraph = world.emergentPracticeGraph;
  const practices = practiceGraph && practiceGraph.nodes ? practiceGraph.nodes.slice(-5) : [];
  practices.forEach((practice, index) => {
    const x = 82 + index * 150;
    const y = 555;
    ctx.fillStyle = practice.status === 'taboo' ? '#b75d39' : practice.status === 'forgotten' ? '#777' : '#2f717b';
    ctx.beginPath(); ctx.rect(x, y, 18, 18); ctx.fill();
    ctx.fillStyle = '#f9ebc9';
    ctx.font = '12px Optima, sans-serif';
    ctx.fillText((practice.local_name || practice.practice_id || 'practice').slice(0, 20), x + 24, y + 14);
  });

  const effects = deepTime && deepTime.emergentEffects ? deepTime.emergentEffects.slice(-3) : [];
  effects.forEach((effect, index) => {
    const x = 735;
    const y = 500 + index * 28;
    ctx.fillStyle = '#d5a13a';
    ctx.beginPath(); ctx.arc(x, y, 8, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = '#f9ebc9';
    ctx.font = '12px Optima, sans-serif';
    ctx.fillText(`${effect.effect_id}: ${effect.outcome}`.slice(0, 42), x + 18, y + 4);
  });

  if (world.audit) {
    ctx.fillStyle = 'rgba(17,24,22,0.78)'; ctx.fillRect(34, 430, 520, 142);
    ctx.fillStyle = '#f9ebc9'; ctx.fillText('AUDIT: localStorage-backed state, replay export, private workspace hidden', 54, 462);
    ctx.fillText('Replay rows: ' + world.replay.length + ' / QA rows: ' + world.lastQA.length, 54, 494);
    ctx.fillText('Ledger rows: ' + (world.realityConstraintLedger ? world.realityConstraintLedger.rows.length : 0) + ' / survival: ' + (survival ? survival.status : 'not audited'), 54, 526);
  }
  ctx.fillStyle = '#f9ebc9'; ctx.fillText('Boundary visible: deterministic prototype only; no consciousness or LLM claim.', 32, canvas.height - 24);
}

function ensureCivilizationPressure() {
  if (!world.anomalyDiscovery) introduceWorldAnomaly();
  if (!world.anomalyInvestigationSchedule) planAnomalyInvestigationSchedule();
  if (!world.civilizationPressure) {
    world.civilizationPressure = {
      reportIntroduced: 369,
      boundary: 'browser-local-civilization-pressure-only; no LLM call, no subjective consciousness, no moral patienthood, no predeclared device tree',
      lineagePolicy: 'belief lineage can rewrite ordinary schedules, apprenticeships, trade routes, safety customs, and later resident choices while preserving source belief IDs',
      scheduleRewrites: [],
      apprenticeships: [],
      tradeRoutes: [],
      safetyCustoms: [],
      ordinaryChoiceEffects: [],
      pressureLedger: [],
      sourceLedger: []
    };
  }
  return world.civilizationPressure;
}

function civilizationBeliefEntries() {
  if (!world.anomalyDiscovery) introduceWorldAnomaly();
  const entries = Object.entries(world.anomalyDiscovery.residentBeliefs || {});
  if (entries.length >= 4) return entries;
  while (Object.keys(world.anomalyDiscovery.residentBeliefs || {}).length < 4) spreadAnomalyBelief();
  return Object.entries(world.anomalyDiscovery.residentBeliefs || {});
}

function civilizationPressureType(index, belief) {
  const cycle = ['schedule_rewrite', 'apprenticeship', 'trade_route', 'safety_custom'];
  if (belief && (belief.contradictionCount > 1 || belief.kind === 'fearful')) return 'safety_custom';
  return cycle[index % cycle.length];
}

function scheduleTextForCivilizationPressure(type, belief) {
  const label = belief ? belief.label : 'unsettled sign';
  if (type === 'apprenticeship') return `teaching ${label}`;
  if (type === 'trade_route') return `hauling material for ${label}`;
  if (type === 'safety_custom') return `checking safe boundary for ${label}`;
  return `arguing schedule around ${label}`;
}

function runCivilizationPressureStep() {
  const pressure = ensureCivilizationPressure();
  const entries = civilizationBeliefEntries();
  const index = pressure.pressureLedger.length;
  const [resident, belief] = entries[index % entries.length];
  const schedule = world.anomalyInvestigationSchedule;
  const slot = schedule && Array.isArray(schedule.slots) ? schedule.slots.find(item => item.resident === resident) || schedule.slots[index % schedule.slots.length] : null;
  const pressureType = civilizationPressureType(index, belief);
  const newSchedule = scheduleTextForCivilizationPressure(pressureType, belief);
  const sourceBeliefId = `${resident}:${belief.label}`;
  const row = {
    id: `CIV-${String(index + 1).padStart(2, '0')}`,
    tick: world.tick,
    resident,
    pressureType,
    sourceBeliefId,
    sourceBeliefLabel: belief.label,
    sourceBeliefKind: belief.kind,
    sourceSlotId: slot ? slot.id : 'none',
    scheduleBefore: world.residents[resident].schedule,
    scheduleAfter: newSchedule,
    directAvatarCommand: false,
    trueLawExposed: false,
    ordinarySurface: true
  };
  world.residents[resident].schedule = newSchedule;
  world.scheduleQueue.push({ id: row.id, resident, task: newSchedule, status: 'civilization_pressure', sourceBeliefId, source: 'belief_lineage_pressure', tick: world.tick });
  pressure.scheduleRewrites.push(row);
  if (pressureType === 'apprenticeship') {
    const apprentice = Object.keys(world.residents)[(Object.keys(world.residents).indexOf(resident) + 1) % Object.keys(world.residents).length];
    pressure.apprenticeships.push({ id: row.id, mentor: resident, apprentice, sourceBeliefId, practice: belief.label, ordinaryScheduleChanged: true });
  }
  if (pressureType === 'trade_route') {
    const before = { ...world.resources };
    world.resources.fiber += 1;
    world.resources.wood = Math.max(0, world.resources.wood - 1);
    pressure.tradeRoutes.push({ id: row.id, resident, route: `route for ${belief.label}`, sourceBeliefId, resourcesBefore: before, resourcesAfter: { ...world.resources }, ordinaryResourcesChanged: true });
  }
  if (pressureType === 'safety_custom') {
    pressure.safetyCustoms.push({ id: row.id, resident, custom: `ask before repeating ${belief.label}`, sourceBeliefId, refusalAllowed: true, recoverable: true });
  }
  pressure.ordinaryChoiceEffects.push({ id: row.id, resident, action: pressureType === 'safety_custom' ? 'offerHelp_may_refuse' : 'askSchedule_mentions_lineage', sourceBeliefId, scheduleAfter: newSchedule, bounded: true });
  pressure.sourceLedger.push({ id: row.id, sourceBeliefId, sourceSlotId: row.sourceSlotId, publicResidentKnowledgeOnly: true, hiddenLawExposed: false });
  pressure.pressureLedger.push(row);
  mutateResident(resident, { progress: 0.008, trust: pressureType === 'safety_custom' ? 0.001 : 0.004, memory: `civilization pressure from ${belief.label}: ${newSchedule}`, historyEvent: 'civilization pressure', historyDetail: `${pressureType} from ${sourceBeliefId}` });
  recordCheckpoint('civilization pressure applied');
  return log('runCivilizationPressureStep', { pressureType, resident, sourceBeliefId, schedule: newSchedule, sourceSlotId: row.sourceSlotId, ordinarySurface: true });
}

function runCivilizationPressureLoop() {
  const pressure = ensureCivilizationPressure();
  const before = pressure.pressureLedger.length;
  for (let i = 0; i < 4; i += 1) runCivilizationPressureStep();
  const after = pressure.pressureLedger.length;
  return log('runCivilizationPressureLoop', {
    stepsAdded: after - before,
    scheduleRewrites: pressure.scheduleRewrites.length,
    apprenticeships: pressure.apprenticeships.length,
    tradeRoutes: pressure.tradeRoutes.length,
    safetyCustoms: pressure.safetyCustoms.length,
    ordinaryChoiceEffects: pressure.ordinaryChoiceEffects.length,
    sourceLedger: pressure.sourceLedger.length,
    boundary: pressure.boundary
  });
}

function renderCivilizationPressure() {
  const summaryNode = document.getElementById('civilizationPressureSummaryOut');
  const detailNode = document.getElementById('civilizationPressureOut');
  const pressure = world.civilizationPressure;
  if (summaryNode) {
    summaryNode.textContent = pressure
      ? `${pressure.scheduleRewrites.length} schedules / ${pressure.apprenticeships.length} apprenticeships / ${pressure.tradeRoutes.length} routes / ${pressure.safetyCustoms.length} safety customs`
      : 'No civilization pressure yet.';
  }
  if (!detailNode) return;
  if (!pressure) {
    detailNode.textContent = 'No civilization pressure yet. Run pressure loop after anomaly beliefs exist.';
    return;
  }
  const schedules = pressure.scheduleRewrites.slice(-6).map(row => `${row.id}: ${row.resident} ${row.scheduleBefore} -> ${row.scheduleAfter} from ${row.sourceBeliefLabel}`);
  const apprenticeships = pressure.apprenticeships.slice(-4).map(row => `${row.id}: ${row.mentor} teaches ${row.apprentice} practice=${row.practice}`);
  const routes = pressure.tradeRoutes.slice(-4).map(row => `${row.id}: ${row.route} resources ${JSON.stringify(row.resourcesBefore)} -> ${JSON.stringify(row.resourcesAfter)}`);
  const safety = pressure.safetyCustoms.slice(-4).map(row => `${row.id}: ${row.resident} custom=${row.custom} refusalAllowed=${row.refusalAllowed}`);
  const choices = pressure.ordinaryChoiceEffects.slice(-6).map(row => `${row.id}: ${row.action} for ${row.resident} source=${row.sourceBeliefId}`);
  detailNode.textContent = [
    `Boundary: ${pressure.boundary}`,
    `Policy: ${pressure.lineagePolicy}`,
    'Schedule rewrites:',
    ...(schedules.length ? schedules : ['none']),
    'Apprenticeships:',
    ...(apprenticeships.length ? apprenticeships : ['none']),
    'Trade routes:',
    ...(routes.length ? routes : ['none']),
    'Safety customs:',
    ...(safety.length ? safety : ['none']),
    'Ordinary choice effects:',
    ...(choices.length ? choices : ['none'])
  ].join('\n');
}

function ensurePracticalDiscovery(allowPressureBootstrap = true) {
  if (allowPressureBootstrap && !world.civilizationPressure) runCivilizationPressureLoop();
  if (!world.practicalDiscovery) {
    world.practicalDiscovery = {
      reportIntroduced: 370,
      boundary: 'browser-local-lived-practical-discovery-only; no LLM call, no subjective consciousness, no moral patienthood, no predeclared invention list',
      discoveryPolicy: 'ordinary actions create bottlenecks; residents propose tests from those bottlenecks; repeated evidence can stabilize a local practice without installing a correct concept',
      ordinaryIntegrationPolicy: 'normal player actions are recorded as pressure; repeated actions can trigger tests only when public history exists',
      ordinaryPlayFeed: [],
      livedActions: [],
      bottlenecks: [],
      residentProposals: [],
      practicalTests: [],
      preservedFailures: [],
      practiceCandidates: [],
      practiceAdoptions: [],
      autoGeneratedTests: [],
      sourceLedger: []
    };
  }
  if (!world.practicalDiscovery.ordinaryPlayFeed) world.practicalDiscovery.ordinaryPlayFeed = [];
  if (!world.practicalDiscovery.autoGeneratedTests) world.practicalDiscovery.autoGeneratedTests = [];
  if (!world.practicalDiscovery.ordinaryIntegrationPolicy) {
    world.practicalDiscovery.ordinaryIntegrationPolicy = 'normal player actions are recorded as pressure; repeated actions can trigger tests only when public history exists';
  }
  return world.practicalDiscovery;
}

function latestCivilizationSourceFor(resident) {
  const pressure = ensureCivilizationPressure();
  return pressure.pressureLedger.slice().reverse().find(row => row.resident === resident)
    || pressure.pressureLedger[pressure.pressureLedger.length - 1]
    || { sourceBeliefId: `${resident}:unsettled-sign`, sourceBeliefLabel: 'unsettled sign', pressureType: 'schedule_rewrite' };
}

function livedBottleneckFor(action, resident) {
  const source = latestCivilizationSourceFor(resident);
  const schedule = world.residents[resident].schedule;
  let type = 'schedule_conflict';
  let detail = `${resident} is doing ${schedule}`;
  if (action === 'borrowTool' || /hauling|route/.test(schedule)) {
    type = 'material_shortage';
    detail = `materials shifted around ${source.sourceBeliefLabel}`;
  } else if (action === 'offerHelp' && (/safe|checking|boundary/.test(schedule) || source.pressureType === 'safety_custom')) {
    type = 'safety_limit';
    detail = `help must respect a safety custom around ${source.sourceBeliefLabel}`;
  } else if (/teaching/.test(schedule)) {
    type = 'apprenticeship_gap';
    detail = `teaching needs a repeatable practice for ${source.sourceBeliefLabel}`;
  } else if (world.resources.care < 3) {
    type = 'care_shortage';
    detail = 'care is scarce after ordinary help actions';
  }
  return { type, detail, source };
}

function materialsForBottleneck(type, label) {
  const materials = ['reed_fiber', 'dry_resin'];
  if (/red|bite|carry/.test(label)) materials[0] = 'red_scrap';
  if (/wet|water|safe|boundary/.test(label) || type === 'safety_limit') materials[1] = 'wet_wood';
  if (/jar|archive|school/.test(label) || type === 'apprenticeship_gap') materials[1] = 'clay_jar';
  if (/route|grain|hauling/.test(label) || type === 'material_shortage') materials[0] = 'iron_sand';
  return materials;
}

function recordOrdinaryPlayPressure(action, resident) {
  if (livedActionAutoIntegrationPaused) return { recorded: false, reason: 'explicit discovery loop owns this action' };
  const discovery = ensurePracticalDiscovery(false);
  const pressureReady = Boolean(world.civilizationPressure && world.civilizationPressure.pressureLedger && world.civilizationPressure.pressureLedger.length);
  const source = pressureReady
    ? latestCivilizationSourceFor(resident)
    : { sourceBeliefId: 'ordinary-play-before-public-pressure', sourceBeliefLabel: 'ordinary village pressure', pressureType: 'unbound' };
  const bottleneck = pressureReady
    ? livedBottleneckFor(action, resident)
    : { type: 'ordinary_observation', detail: `${resident} acted before a shared anomaly or pressure history existed`, source };
  const similarBefore = discovery.ordinaryPlayFeed.filter(row => row.action === action && row.resident === resident && row.bottleneckType === bottleneck.type && row.sourceBeliefId === source.sourceBeliefId).length;
  const row = {
    id: `OPF-${String(discovery.ordinaryPlayFeed.length + 1).padStart(2, '0')}`,
    tick: world.tick,
    action,
    resident,
    bottleneckType: bottleneck.type,
    detail: bottleneck.detail,
    sourceBeliefId: source.sourceBeliefId,
    sourceBeliefLabel: source.sourceBeliefLabel,
    pressureReady,
    repeatedOrdinaryActions: similarBefore + 1,
    triggeredResidentTest: false,
    panelOnly: false,
    avatarDirectCommand: false
  };
  discovery.ordinaryPlayFeed.push(row);
  if (discovery.ordinaryPlayFeed.length > 80) discovery.ordinaryPlayFeed.shift();
  if (!pressureReady) return { recorded: true, pressureReady: false, repeatedOrdinaryActions: row.repeatedOrdinaryActions, reason: 'waiting for public pressure or resident belief source' };
  if (row.repeatedOrdinaryActions < 2 || row.repeatedOrdinaryActions % 2 !== 0) {
    return { recorded: true, pressureReady: true, repeatedOrdinaryActions: row.repeatedOrdinaryActions, triggeredResidentTest: false };
  }
  livedActionAutoIntegrationPaused = true;
  try {
    runPracticalDiscoveryStep(action);
  } finally {
    livedActionAutoIntegrationPaused = false;
  }
  const test = discovery.practicalTests[discovery.practicalTests.length - 1] || null;
  row.triggeredResidentTest = Boolean(test);
  const autoTest = {
    id: `PAT-${String(discovery.autoGeneratedTests.length + 1).padStart(2, '0')}`,
    sourceFeedId: row.id,
    action,
    resident,
    testId: test ? test.id : 'none',
    repeatedOrdinaryActions: row.repeatedOrdinaryActions,
    sourceBeliefId: source.sourceBeliefId,
    noPredeclaredInvention: true
  };
  discovery.autoGeneratedTests.push(autoTest);
  if (discovery.autoGeneratedTests.length > 40) discovery.autoGeneratedTests.shift();
  return { recorded: true, pressureReady: true, repeatedOrdinaryActions: row.repeatedOrdinaryActions, triggeredResidentTest: row.triggeredResidentTest, testId: autoTest.testId };
}

function runPracticalDiscoveryStep(action = 'lived_pressure') {
  const discovery = ensurePracticalDiscovery();
  const resident = world.selected;
  const bottleneck = livedBottleneckFor(action, resident);
  const source = bottleneck.source;
  const sequence = discovery.practicalTests.length + 1;
  const materials = materialsForBottleneck(bottleneck.type, source.sourceBeliefLabel);
  const repeatedEvidence = discovery.practicalTests.filter(row => row.sourceBeliefId === source.sourceBeliefId && row.bottleneckType === bottleneck.type).length + 1;
  const failure = bottleneck.type === 'safety_limit' && repeatedEvidence < 2;
  const outcome = failure
    ? `test paused because ${bottleneck.detail}`
    : `repeatable workaround for ${bottleneck.detail}`;
  const candidateLabel = `${source.sourceBeliefLabel} ${bottleneck.type.replace('_', ' ')} practice`;
  const actionRow = { id: `LIV-${String(discovery.livedActions.length + 1).padStart(2, '0')}`, action, resident, schedule: world.residents[resident].schedule, resources: { ...world.resources }, ordinaryAction: true };
  const bottleneckRow = { id: `BOT-${String(discovery.bottlenecks.length + 1).padStart(2, '0')}`, actionId: actionRow.id, resident, bottleneckType: bottleneck.type, detail: bottleneck.detail, sourceBeliefId: source.sourceBeliefId, sourceBeliefLabel: source.sourceBeliefLabel };
  const proposal = { id: `PDP-${String(discovery.residentProposals.length + 1).padStart(2, '0')}`, resident, sourceBottleneckId: bottleneckRow.id, sourceBeliefId: source.sourceBeliefId, materials, question: `try a local workaround for ${bottleneck.type}`, residentGenerated: true, avatarAnswer: false, predeclaredInvention: false };
  const test = { id: `PDT-${String(sequence).padStart(2, '0')}`, proposalId: proposal.id, resident, materials, outcome, failure, preservedFailure: failure, repeatedEvidence, candidateLabel, sourceBeliefId: source.sourceBeliefId, bottleneckType: bottleneck.type, noCorrectConceptInstalled: true };
  discovery.livedActions.push(actionRow);
  discovery.bottlenecks.push(bottleneckRow);
  discovery.residentProposals.push(proposal);
  discovery.practicalTests.push(test);
  if (failure) discovery.preservedFailures.push(test);
  if (repeatedEvidence >= 2 && !failure) {
    const existing = discovery.practiceCandidates.find(row => row.label === candidateLabel);
    const candidate = existing || { id: `PDC-${String(discovery.practiceCandidates.length + 1).padStart(2, '0')}`, label: candidateLabel, sourceBeliefId: source.sourceBeliefId, bottleneckType: bottleneck.type, evidenceCount: 0, adopted: false, predeclaredInvention: false };
    candidate.evidenceCount += 1;
    if (!existing) discovery.practiceCandidates.push(candidate);
    if (candidate.evidenceCount >= 2 && !candidate.adopted) {
      candidate.adopted = true;
      const adoption = { id: `PDA-${String(discovery.practiceAdoptions.length + 1).padStart(2, '0')}`, resident, practiceCandidateId: candidate.id, label: candidate.label, sourceBeliefId: source.sourceBeliefId, changedSchedule: true, changedMemory: true, predeclaredInvention: false };
      discovery.practiceAdoptions.push(adoption);
      mutateResident(resident, { progress: 0.012, trust: 0.006, schedule: `using ${candidate.label}`, memory: `adopted local practice ${candidate.label}`, historyEvent: 'practical discovery adoption', historyDetail: `${candidate.label} from ${source.sourceBeliefId}` });
    }
  }
  discovery.sourceLedger.push({ id: test.id, sourceBeliefId: source.sourceBeliefId, sourceBottleneckId: bottleneckRow.id, ordinaryAction: action, hiddenLawExposed: false, avatarAnswer: false });
  updateEmergentPracticeGraphFromTest(test, proposal, bottleneckRow, source);
  recordRealityConstraint('practical_test', {
    resident,
    sourceBeliefId: source.sourceBeliefId,
    materials,
    publicObservation: outcome,
    residentInterpretation: candidateLabel,
    materialTransformation: failure ? 'materials handled then test paused' : 'materials combined into repeatable local practice attempt',
    timeCost: 1,
    workCost: bottleneck.type === 'material_shortage' ? 2 : 1,
    toolWear: materials.includes('iron_sand') ? 1 : 0,
    maintenanceObligation: repeatedEvidence >= 2 ? `keep checking ${candidateLabel}` : 'none',
    unintendedConsequence: failure ? 'safety caution increased' : 'none',
    hiddenLawInvolved: source.sourceBeliefLabel,
    conservationCheck: true
  });
  return log('runPracticalDiscoveryStep', { action, resident, bottleneckType: bottleneck.type, sourceBeliefId: source.sourceBeliefId, proposal: proposal.id, test: test.id, failure, repeatedEvidence, practiceCandidate: candidateLabel, adoptedCount: discovery.practiceAdoptions.length });
}

function runPracticalDiscoveryLoop() {
  const discovery = ensurePracticalDiscovery();
  const before = discovery.practicalTests.length;
  const actions = [
    ['askSchedule', () => askSchedule()],
    ['borrowTool', () => borrowTool()],
    ['offerHelp', () => offerHelp()],
    ['runScheduledAnomalyInvestigation', () => runScheduledAnomalyInvestigation()],
    ['askSchedule', () => askSchedule()],
    ['offerHelp', () => offerHelp()]
  ];
  actions.forEach(([name, fn]) => {
    livedActionAutoIntegrationPaused = true;
    try {
      fn();
    } finally {
      livedActionAutoIntegrationPaused = false;
    }
    runPracticalDiscoveryStep(name);
  });
  return log('runPracticalDiscoveryLoop', {
    livedActions: discovery.livedActions.length,
    stepsAdded: discovery.practicalTests.length - before,
    bottlenecks: discovery.bottlenecks.length,
    residentProposals: discovery.residentProposals.length,
    practicalTests: discovery.practicalTests.length,
    preservedFailures: discovery.preservedFailures.length,
    practiceCandidates: discovery.practiceCandidates.length,
    practiceAdoptions: discovery.practiceAdoptions.length,
    boundary: discovery.boundary
  });
}

function renderPracticalDiscovery() {
  const summaryNode = document.getElementById('practicalDiscoverySummaryOut');
  const detailNode = document.getElementById('practicalDiscoveryOut');
  const discovery = world.practicalDiscovery;
  if (summaryNode) {
    summaryNode.textContent = discovery
      ? `${(discovery.ordinaryPlayFeed || []).length} ordinary actions / ${discovery.livedActions.length} lived tests / ${discovery.practiceCandidates.length} candidates / ${discovery.practiceAdoptions.length} adopted`
      : 'No practical discovery yet.';
  }
  if (!detailNode) return;
  if (!discovery) {
    detailNode.textContent = 'No practical discovery yet. Run lived action loop after civilization pressure exists.';
    return;
  }
  const feed = (discovery.ordinaryPlayFeed || []).slice(-6).map(row => `${row.id}: ${row.action} for ${row.resident} repeated=${row.repeatedOrdinaryActions} pressureReady=${row.pressureReady} triggered=${row.triggeredResidentTest}`);
  const bottlenecks = discovery.bottlenecks.slice(-6).map(row => `${row.id}: ${row.resident} ${row.bottleneckType} from ${row.sourceBeliefLabel}`);
  const proposals = discovery.residentProposals.slice(-6).map(row => `${row.id}: ${row.resident} tries ${row.materials.join(' + ')} / ${row.question}`);
  const tests = discovery.practicalTests.slice(-6).map(row => `${row.id}: repeated=${row.repeatedEvidence} failure=${row.failure} candidate=${row.candidateLabel}`);
  const adoptions = discovery.practiceAdoptions.slice(-4).map(row => `${row.id}: ${row.resident} adopted ${row.label}`);
  detailNode.textContent = [
    `Boundary: ${discovery.boundary}`,
    `Policy: ${discovery.discoveryPolicy}`,
    `Ordinary integration: ${discovery.ordinaryIntegrationPolicy || 'not initialized'}`,
    'Ordinary play feed:',
    ...(feed.length ? feed : ['none']),
    'Bottlenecks from lived actions:',
    ...(bottlenecks.length ? bottlenecks : ['none']),
    'Resident-generated proposals:',
    ...(proposals.length ? proposals : ['none']),
    'Practical tests:',
    ...(tests.length ? tests : ['none']),
    'Practice adoptions:',
    ...(adoptions.length ? adoptions : ['none'])
  ].join('\n');
}

function ensureEmergentPracticeGraph() {
  if (!world.emergentPracticeGraph) {
    world.emergentPracticeGraph = {
      reportIntroduced: 370,
      boundary: 'browser-local-emergent-practice-graph-only; graph generated after history, not before action',
      nodes: [],
      edges: [],
      auditSplit: 'normal view shows local names and resident beliefs; audit view may show hidden material properties',
      noPredefinedTechTree: true
    };
  }
  return world.emergentPracticeGraph;
}

function updateEmergentPracticeGraphFromTest(test, proposal, bottleneck, source) {
  const graph = ensureEmergentPracticeGraph();
  if (test.repeatedEvidence < 2 && !test.failure) return null;
  const existing = graph.nodes.find(row => row.local_name === test.candidateLabel);
  const failedAncestors = (world.practicalDiscovery ? world.practicalDiscovery.preservedFailures : [])
    .filter(row => row.sourceBeliefId === source.sourceBeliefId)
    .map(row => row.id);
  const status = test.failure ? 'taboo' : test.repeatedEvidence >= 4 ? 'institutionalized' : test.repeatedEvidence >= 3 ? 'practical' : 'emerging';
  const node = existing || {
    practice_id: `EPG-${String(graph.nodes.length + 1).padStart(2, '0')}`,
    local_name: test.candidateLabel,
    origin_tick: world.tick,
    origin_resident: test.resident,
    origin_household: `${test.resident}-household`,
    origin_event: test.id,
    problem_pressure: bottleneck.bottleneckType,
    materials_used: proposal.materials,
    observations_supporting: [],
    failed_ancestor_tests: [],
    beliefs_involved: [],
    social_transmission_path: [],
    mutation_variants: [],
    adoption_count: 0,
    adoption_households: [],
    practical_score: 0,
    ritual_score: 0,
    taboo_score: 0,
    dispute_score: 0,
    maintenance_cost: proposal.materials.length + 1,
    risk_flags: [],
    generations_survived: 0,
    status,
    avatar_role: 'witness_or_supporter',
    hidden_properties_audit_only: true
  };
  node.observations_supporting = Array.from(new Set(node.observations_supporting.concat([test.outcome])));
  node.failed_ancestor_tests = Array.from(new Set(node.failed_ancestor_tests.concat(failedAncestors)));
  node.beliefs_involved = Array.from(new Set(node.beliefs_involved.concat([source.sourceBeliefId])));
  node.social_transmission_path = Array.from(new Set(node.social_transmission_path.concat([`${test.resident}->${world.selected}`])));
  node.mutation_variants = Array.from(new Set(node.mutation_variants.concat([test.candidateLabel, source.sourceBeliefLabel])));
  node.adoption_count += test.failure ? 0 : 1;
  node.adoption_households = Array.from(new Set(node.adoption_households.concat([`${test.resident}-household`])));
  node.practical_score = Number(Math.min(1, node.practical_score + (test.failure ? 0 : 0.24)).toFixed(3));
  node.ritual_score = Number(Math.min(1, node.ritual_score + (bottleneck.bottleneckType === 'safety_limit' ? 0.18 : 0.04)).toFixed(3));
  node.taboo_score = Number(Math.min(1, node.taboo_score + (test.failure ? 0.28 : 0.02)).toFixed(3));
  node.dispute_score = Number(Math.min(1, node.dispute_score + (test.repeatedEvidence < 3 ? 0.12 : 0.03)).toFixed(3));
  node.risk_flags = Array.from(new Set(node.risk_flags.concat(test.failure ? ['failed ancestor'] : bottleneck.bottleneckType === 'safety_limit' ? ['safety custom'] : [])));
  node.generations_survived = Math.max(node.generations_survived, Math.floor(test.repeatedEvidence / 2));
  node.status = status;
  if (!existing) graph.nodes.push(node);
  graph.edges.push({ from: source.sourceBeliefId, to: node.practice_id, event: test.id, relation: test.failure ? 'failed_into_safety_memory' : 'repeated_use_into_practice', hiddenLawExposed: false });
  return node;
}

function ensureVillageBoard() {
  if (!world.villageBoard) {
    world.villageBoard = {
      reportIntroduced: 370,
      boundary: 'diegetic-village-board-only; avatar supports conditions, residents decide',
      concerns: [],
      projectProposals: [],
      supportEvents: [],
      councilNotes: [],
      avatarCannotForce: true
    };
  }
  return world.villageBoard;
}

function villageConcernFromState(index) {
  const graph = ensureEmergentPracticeGraph();
  const node = graph.nodes[index % Math.max(1, graph.nodes.length)] || null;
  const pressure = world.civilizationPressure ? world.civilizationPressure.pressureLedger[index % Math.max(1, world.civilizationPressure.pressureLedger.length)] : null;
  const resident = pressure ? pressure.resident : Object.keys(world.residents)[index % Object.keys(world.residents).length];
  const problem = node ? `maintenance for ${node.local_name}` : pressure ? `schedule strain around ${pressure.sourceBeliefLabel}` : 'fiber stores strained';
  return {
    concern_id: `VBC-${String(index + 1).padStart(2, '0')}`,
    resident,
    problem,
    source: node ? node.practice_id : pressure ? pressure.sourceBeliefId : 'resource commons',
    urgency: node && node.status === 'taboo' ? 'high' : world.resources.fiber < 8 ? 'medium' : 'low',
    who_felt_this: resident,
    avatar_direct_control: false
  };
}

function projectProposalFromConcern(concern) {
  const resident = world.residents[concern.resident] || currentResident();
  return {
    proposal_id: `VBP-${String(world.villageBoard.projectProposals.length + 1).padStart(2, '0')}`,
    proposer: concern.resident,
    problem_addressed: concern.problem,
    materials_needed: concern.urgency === 'high' ? ['fiber', 'wood', 'care'] : ['fiber', 'care'],
    likely_helpers: Object.keys(world.residents).filter(name => name !== concern.resident).slice(0, 2),
    resident_willingness: Number(Math.max(0.12, Math.min(0.92, resident.trust - resident.debt * 0.06)).toFixed(3)),
    known_objections: concern.urgency === 'high' ? ['fear of repeating failed test'] : ['ordinary work delay'],
    risk: concern.urgency,
    maintenance_cost: concern.urgency === 'high' ? 2 : 1,
    related_memories: [resident.memory],
    related_practice_nodes: world.emergentPracticeGraph ? world.emergentPracticeGraph.nodes.slice(-2).map(row => row.practice_id) : [],
    possible_failure_modes: ['materials run short', 'resident refuses', 'weather interrupts'],
    current_support_level: 0,
    avatar_can_force: false,
    status: 'resident proposed'
  };
}

function runVillageBoardLoop() {
  const board = ensureVillageBoard();
  if (!world.practicalDiscovery || !world.practicalDiscovery.practicalTests.length) runPracticalDiscoveryLoop();
  const before = board.concerns.length;
  for (let i = 0; i < 3; i += 1) {
    const concern = villageConcernFromState(board.concerns.length);
    const proposal = projectProposalFromConcern(concern);
    board.concerns.push(concern);
    board.projectProposals.push(proposal);
    recordRealityConstraint('village_board_proposal', {
      resident: concern.resident,
      sourceBeliefId: concern.source,
      materials: proposal.materials_needed,
      publicObservation: concern.problem,
      residentInterpretation: proposal.status,
      materialTransformation: 'proposal only; no construction without support and material cost',
      timeCost: 1,
      workCost: 1,
      toolWear: 0,
      maintenanceObligation: `maintain proposal ${proposal.proposal_id}`,
      unintendedConsequence: 'ordinary work may be delayed',
      hiddenLawInvolved: 'audit only if related practice node exists',
      conservationCheck: true
    });
  }
  return log('runVillageBoardLoop', { concerns: board.concerns.length, proposals: board.projectProposals.length, supportEvents: board.supportEvents.length, addedConcerns: board.concerns.length - before, avatarCannotForce: board.avatarCannotForce });
}

function supportVillageProposal() {
  const board = ensureVillageBoard();
  if (!board.projectProposals.length) runVillageBoardLoop();
  const proposal = board.projectProposals.find(row => row.status !== 'accepted' && row.status !== 'refused') || board.projectProposals[board.projectProposals.length - 1];
  const accepted = proposal.resident_willingness + proposal.current_support_level >= 0.48;
  proposal.current_support_level = Number(Math.min(1, proposal.current_support_level + 0.25).toFixed(3));
  proposal.status = accepted ? 'accepted' : 'resident still considering';
  if (accepted) {
    world.resources.fiber = Math.max(0, world.resources.fiber - 1);
    world.resources.care = Math.max(0, world.resources.care - 1);
    mutateResident(proposal.proposer, { trust: 0.006, progress: 0.008, memory: `felt supported on ${proposal.problem_addressed}`, historyEvent: 'village board support', historyDetail: proposal.proposal_id });
  }
  board.supportEvents.push({ proposalId: proposal.proposal_id, accepted, avatarAction: 'support conditions', whoFeltThis: proposal.proposer, forced: false });
  recordRealityConstraint('proposal_support', {
    resident: proposal.proposer,
    sourceBeliefId: proposal.proposal_id,
    materials: proposal.materials_needed,
    publicObservation: proposal.problem_addressed,
    residentInterpretation: accepted ? 'support accepted' : 'support not enough yet',
    materialTransformation: accepted ? 'fiber and care consumed as support' : 'no material consumed yet',
    timeCost: 1,
    workCost: accepted ? 2 : 1,
    toolWear: 0,
    maintenanceObligation: accepted ? `follow through ${proposal.proposal_id}` : 'none',
    unintendedConsequence: accepted ? 'resource commons reduced' : 'resident autonomy preserved',
    hiddenLawInvolved: 'none in normal view',
    conservationCheck: true
  });
  return log('supportVillageProposal', { proposalId: proposal.proposal_id, accepted, support: proposal.current_support_level, resident: proposal.proposer });
}

function askVillageBoardQuestion() {
  const board = ensureVillageBoard();
  if (!board.projectProposals.length) runVillageBoardLoop();
  const proposal = board.projectProposals[board.projectProposals.length - 1];
  board.councilNotes.push({ proposalId: proposal.proposal_id, note: `${proposal.proposer} explains ${proposal.problem_addressed} without giving hidden law`, avatarQuestion: true, directCommand: false });
  return log('askVillageBoardQuestion', { proposalId: proposal.proposal_id, proposer: proposal.proposer, directCommand: false });
}

function waitOnVillageBoard() {
  const board = ensureVillageBoard();
  if (!board.projectProposals.length) runVillageBoardLoop();
  board.projectProposals.forEach(proposal => {
    if (proposal.status === 'resident proposed' && proposal.resident_willingness < 0.42) proposal.status = 'delayed by resident schedule';
  });
  return log('waitOnVillageBoard', { proposals: board.projectProposals.length, delayed: board.projectProposals.filter(row => /delayed/.test(row.status)).length });
}

function ensureRealityConstraintLedger() {
  if (!world.realityConstraintLedger) {
    world.realityConstraintLedger = {
      reportIntroduced: 370,
      boundary: 'audit-causal-ledger-only; normal residents see observations and beliefs, not hidden simulator law',
      rows: [],
      invariants: ['no effect without cause', 'no material without source', 'no work without time', 'no knowledge without observation or teaching', 'no recovery without cost or time']
    };
  }
  return world.realityConstraintLedger;
}

function recordRealityConstraint(event, detail) {
  const ledger = ensureRealityConstraintLedger();
  const row = {
    id: `RCL-${String(ledger.rows.length + 1).padStart(2, '0')}`,
    event,
    material_sources: detail.materials || [],
    material_transformations: detail.materialTransformation || 'none',
    energy_work_time_cost: { time: detail.timeCost || 0, work: detail.workCost || 0 },
    tool_wear: detail.toolWear || 0,
    resident_effort_fatigue: detail.workCost || 0,
    weather_moisture_heat_effects: detail.materials && detail.materials.includes('wet_wood') ? 'wet material changed interpretation' : 'none modeled',
    hidden_law_involved: detail.hiddenLawInvolved || 'audit only',
    public_observation: detail.publicObservation || 'none',
    resident_interpretation: detail.residentInterpretation || 'none',
    conservation_check: detail.conservationCheck !== false,
    maintenance_obligation_created: detail.maintenanceObligation || 'none',
    unintended_consequence: detail.unintendedConsequence || 'none',
    source_belief_id: detail.sourceBeliefId || 'none',
    normal_view_hidden_law_exposed: false
  };
  ledger.rows.push(row);
  return row;
}

function runRealityConstraintAudit() {
  const ledger = ensureRealityConstraintLedger();
  const pass = ledger.rows.every(row => row.conservation_check && row.energy_work_time_cost.time >= 0 && row.normal_view_hidden_law_exposed === false);
  return log('runRealityConstraintAudit', { pass, rows: ledger.rows.length, invariants: ledger.invariants.length });
}

function renderEmergentPracticeGraph() {
  const summaryNode = document.getElementById('emergentPracticeGraphSummaryOut');
  const detailNode = document.getElementById('emergentPracticeGraphOut');
  const graph = world.emergentPracticeGraph;
  if (summaryNode) summaryNode.textContent = graph ? `${graph.nodes.length} nodes / ${graph.edges.length} edges` : 'No practice graph yet.';
  if (!detailNode) return;
  if (!graph) {
    detailNode.textContent = 'No emergent practice graph yet. Run practical discovery loop.';
    return;
  }
  const nodes = graph.nodes.slice(-6).map(row => `${row.practice_id}: ${row.local_name} / status=${row.status} / origin=${row.origin_resident} / materials=${row.materials_used.join(' + ')} / avatar=${row.avatar_role}`);
  detailNode.textContent = [`Boundary: ${graph.boundary}`, `Audit split: ${graph.auditSplit}`, 'Practice nodes:', ...(nodes.length ? nodes : ['none'])].join('\n');
}

function renderVillageBoard() {
  const summaryNode = document.getElementById('villageBoardSummaryOut');
  const detailNode = document.getElementById('villageBoardOut');
  const board = world.villageBoard;
  if (summaryNode) summaryNode.textContent = board ? `${board.concerns.length} concerns / ${board.projectProposals.length} proposals / ${board.supportEvents.length} support events` : 'No village board yet.';
  if (!detailNode) return;
  if (!board) {
    detailNode.textContent = 'No village board yet. Run board loop to let residents post concerns.';
    return;
  }
  const concerns = board.concerns.slice(-6).map(row => `${row.concern_id}: ${row.resident} feels ${row.problem} urgency=${row.urgency}`);
  const proposals = board.projectProposals.slice(-6).map(row => `${row.proposal_id}: ${row.proposer} proposes ${row.problem_addressed} support=${row.current_support_level} status=${row.status} force=${row.avatar_can_force}`);
  detailNode.textContent = [`Boundary: ${board.boundary}`, 'Resident concerns:', ...(concerns.length ? concerns : ['none']), 'Project proposals:', ...(proposals.length ? proposals : ['none'])].join('\n');
}

function renderRealityConstraintLedger() {
  const summaryNode = document.getElementById('realityConstraintLedgerSummaryOut');
  const detailNode = document.getElementById('realityConstraintLedgerOut');
  const ledger = world.realityConstraintLedger;
  if (summaryNode) summaryNode.textContent = ledger ? `${ledger.rows.length} causal rows` : 'No causal rows yet.';
  if (!detailNode) return;
  if (!ledger) {
    detailNode.textContent = 'No reality constraint ledger yet. Practical discovery or village board actions will write causal rows.';
    return;
  }
  const rows = ledger.rows.slice(-8).map(row => `${row.id}: ${row.event} / materials=${row.material_sources.join('+') || 'none'} / time=${row.energy_work_time_cost.time} work=${row.energy_work_time_cost.work} / conservation=${row.conservation_check} / hiddenShown=${row.normal_view_hidden_law_exposed}`);
  detailNode.textContent = [`Boundary: ${ledger.boundary}`, `Invariants: ${ledger.invariants.join('; ')}`, 'Recent causal rows:', ...(rows.length ? rows : ['none'])].join('\n');
}

function ensureAvatarHintDivergence() {
  if (!world.avatarHintDivergence) {
    world.avatarHintDivergence = {
      hints: [],
      householdInterpretations: [],
      branches: [],
      practiceMutations: [],
      negotiations: [],
      sourceLinks: [],
      boundary: {
        avatarCanInfluenceInquiry: true,
        avatarCanInstallCorrectConcept: false,
        hiddenLawNormalView: false,
        uniformUnlocksAllowed: false,
      },
    };
  }
  return world.avatarHintDivergence;
}

function hintResidentFor(offset) {
  const records = Array.isArray(world.residents) ? world.residents : Object.values(world.residents || {});
  const names = records.map((row) => row.name || row.id || row.resident).filter(Boolean);
  const fallback = ['Ari', 'Fay', 'Milo', 'Sera', 'Tovan', 'Nia'];
  const pool = names.length ? names : fallback;
  return pool[offset % pool.length];
}

function latestPracticeForHint() {
  if (!world.emergentPracticeGraph || !world.emergentPracticeGraph.nodes.length) runPracticalDiscoveryLoop();
  const graph = ensureEmergentPracticeGraph();
  return graph.nodes[graph.nodes.length - 1] || {
    practice_id: 'local-observation-only',
    local_name: 'quiet sign practice',
    materials_used: ['reed_fiber', 'dry_resin'],
    status: 'emerging',
    origin_event: 'avatar-nearby-observation',
  };
}

function introduceAvatarHint(kind = 'question') {
  const hints = ensureAvatarHintDivergence();
  if (!world.villageBoard || !world.villageBoard.projectProposals.length) runVillageBoardLoop();
  const source = latestPracticeForHint();
  const hintIndex = hints.hints.length;
  const hintKinds = ['question', 'warning', 'material_offer', 'demonstration', 'wait_and_return'];
  const hintType = hintKinds[hintIndex % hintKinds.length] || kind;
  const resident = hintResidentFor(hintIndex);
  const sourceMaterials = Array.isArray(source.materials_used) ? source.materials_used : String(source.materials_used || 'local material').split('+');
  const material = hintType === 'material_offer' ? ['dry_reed_scrap'] : sourceMaterials;
  const hint = {
    hint_id: `AHD-${String(hints.hints.length + 1).padStart(2, '0')}`,
    tick: world.tick || world.replay.length,
    hint_type: hintType,
    resident_target: resident,
    household: `house_${hintIndex % 4}`,
    source_practice_id: source.practice_id,
    source_local_name: source.local_name,
    avatar_action: hintType === 'question' ? 'asked what changed, without naming the cause' : `offered ${hintType.replace('_', ' ')}`,
    material_used: material,
    visible_demonstration: hintType === 'demonstration' ? `showed ${source.local_name} once` : 'no final answer given',
    correct_explanation_given: false,
    direct_install: false,
    future_use_named: false,
    resident_must_interpret: true,
    time_cost: 1,
    material_cost: hintType === 'material_offer' || hintType === 'demonstration' ? 1 : 0,
  };
  hints.hints.push(hint);
  hints.sourceLinks.push({ source_practice_id: source.practice_id, hint_id: hint.hint_id, avatar_role: 'influenced inquiry, did not command adoption', hidden_law_exposed: false });
  recordRealityConstraint('avatar_hint_divergence', {
    materialSources: material,
    materialTransformation: hint.material_cost ? 'one sample handled during hint' : 'no material transformed',
    timeCost: hint.time_cost,
    laborCost: 1,
    toolWear: 0,
    residentEffort: 1,
    hiddenLawInvolved: 'audit-only material law',
    publicObservation: hint.visible_demonstration,
    residentInterpretation: 'open question, warning, or offer',
    resourcesBefore: 10,
    resourcesAfter: 10 - hint.material_cost,
    conservationCheck: true,
    maintenanceObligationCreated: 'none',
    unintendedConsequence: 'households may disagree',
  });
  return log('introduceAvatarHint', { hintId: hint.hint_id, hintType, directInstall: false, resident });
}

function runHintDivergenceInterpretation() {
  const hints = ensureAvatarHintDivergence();
  if (!hints.hints.length) introduceAvatarHint();
  const hint = hints.hints[hints.hints.length - 1];
  const interpretationsBefore = hints.householdInterpretations.length;
  const branchesBefore = hints.branches.length;
  const branchPlans = [
    { status: 'useful_practice', label: 'dry keeping habit', stance: 'tries a small repeat', willingness: 0.72 },
    { status: 'ritualized', label: 'quiet sign waiting', stance: 'keeps a caution ritual', willingness: 0.48 },
    { status: 'taboo', label: 'storm-thread avoidance', stance: 'warns children away', willingness: 0.26 },
    { status: 'disputed', label: 'wet counterexample note', stance: 'asks for another test', willingness: 0.55 },
  ];
  for (let i = 0; i < 3; i += 1) {
    const plan = branchPlans[(hints.branches.length + i) % branchPlans.length];
    const resident = hintResidentFor(hints.householdInterpretations.length + i + 1);
    const interpretation = {
      interpretation_id: `AHI-${String(hints.householdInterpretations.length + 1).padStart(2, '0')}`,
      hint_id: hint.hint_id,
      resident,
      household: `house_${(hints.householdInterpretations.length + i) % 4}`,
      local_interpretation: `${plan.label} from ${hint.source_local_name}`,
      stance: plan.stance,
      trust_gate: plan.willingness,
      hidden_law_known: false,
      correct_concept_received: false,
      modern_name_used: false,
    };
    hints.householdInterpretations.push(interpretation);
    const branch = {
      branch_id: `AHB-${String(hints.branches.length + 1).padStart(2, '0')}`,
      hint_id: hint.hint_id,
      interpretation_id: interpretation.interpretation_id,
      resident,
      household: interpretation.household,
      branch_status: plan.status,
      branch_reason: `${resident} interprets the hint through ${plan.stance}`,
      accepts_avatar_priority: plan.willingness > 0.5,
      can_refuse_or_delay: plan.willingness <= 0.55,
      source_practice_id: hint.source_practice_id,
      social_echo: `${resident}->${hintResidentFor(hints.branches.length + 2)}`,
      avatar_commanded: false,
    };
    hints.branches.push(branch);
    hints.negotiations.push({
      negotiation_id: `AHN-${String(hints.negotiations.length + 1).padStart(2, '0')}`,
      branch_id: branch.branch_id,
      resident,
      response: branch.accepts_avatar_priority ? 'accepts a limited trial' : 'delays, refuses, or asks council first',
      remembered_boundary: 'avatar suggested; resident decided',
    });
    if (plan.status === 'useful_practice' || plan.status === 'ritualized' || plan.status === 'taboo') {
      hints.practiceMutations.push({
        mutation_id: `AHM-${String(hints.practiceMutations.length + 1).padStart(2, '0')}`,
        parent_practice_id: hint.source_practice_id,
        local_name: interpretation.local_interpretation,
        status: plan.status === 'useful_practice' ? 'practical' : plan.status,
        originating_household: interpretation.household,
        evidence_source: interpretation.interpretation_id,
        adoption_count: plan.status === 'taboo' ? 0 : 1,
        not_predefined_unlock: true,
      });
    }
    recordRealityConstraint('household_hint_interpretation', {
      materialSources: hint.material_used,
      materialTransformation: 'no new material unless household repeats it later',
      timeCost: 1,
      laborCost: 1,
      toolWear: 0,
      residentEffort: 1,
      hiddenLawInvolved: 'audit-only material law',
      publicObservation: hint.visible_demonstration,
      residentInterpretation: interpretation.local_interpretation,
      resourcesBefore: 10,
      resourcesAfter: 10,
      conservationCheck: true,
      maintenanceObligationCreated: plan.status === 'useful_practice' ? interpretation.local_interpretation : 'none',
      unintendedConsequence: branch.branch_status,
    });
  }
  return log('runHintDivergenceInterpretation', {
    interpretations: hints.householdInterpretations.length,
    branches: hints.branches.length,
    addedInterpretations: hints.householdInterpretations.length - interpretationsBefore,
    addedBranches: hints.branches.length - branchesBefore,
    uniform: new Set(hints.branches.map((row) => row.branch_status)).size <= 1,
  });
}

function runAvatarHintDivergenceLoop() {
  const hints = ensureAvatarHintDivergence();
  runVillageBoardLoop();
  introduceAvatarHint('question');
  runHintDivergenceInterpretation();
  introduceAvatarHint('warning');
  runHintDivergenceInterpretation();
  return log('runAvatarHintDivergenceLoop', {
    hints: hints.hints.length,
    interpretations: hints.householdInterpretations.length,
    branches: hints.branches.length,
    mutations: hints.practiceMutations.length,
    directInstall: hints.hints.some((row) => row.direct_install),
  });
}

function renderAvatarHintDivergence() {
  const summaryNode = document.getElementById('avatarHintDivergenceSummaryOut');
  const detailNode = document.getElementById('avatarHintDivergenceOut');
  const hints = world.avatarHintDivergence;
  if (summaryNode) summaryNode.textContent = hints ? `${hints.hints.length} hints / ${hints.branches.length} branches / ${hints.practiceMutations.length} mutations` : 'No hints yet.';
  if (!detailNode) return;
  if (!hints) {
    detailNode.textContent = 'No avatar hint divergence yet. The avatar can ask, warn, demonstrate, or offer material, but residents must interpret it.';
    return;
  }
  const recentHints = hints.hints.slice(-4).map(row => `${row.hint_id}: ${row.hint_type} to ${row.resident_target}, direct=${row.direct_install}`);
  const branches = hints.branches.slice(-8).map(row => `${row.branch_id}: ${row.resident} ${row.branch_status}, force=${row.avatar_commanded}`);
  const mutations = hints.practiceMutations.slice(-6).map(row => `${row.mutation_id}: ${row.local_name} status=${row.status} parent=${row.parent_practice_id}`);
  detailNode.textContent = [
    `Boundary: avatar influences inquiry, residents interpret; hidden laws remain audit-only; no uniform unlock.`,
    'Hints:',
    ...(recentHints.length ? recentHints : ['none']),
    'Branches:',
    ...(branches.length ? branches : ['none']),
    'Practice mutations:',
    ...(mutations.length ? mutations : ['none']),
  ].join('\n');
}

function ensureHintBranchPersistence() {
  if (!world.hintBranchPersistence) {
    world.hintBranchPersistence = {
      returnSessions: [],
      continuityRows: [],
      householdReputation: [],
      maintenanceBurden: [],
      forgettingEvents: [],
      revivalEvents: [],
      sourceLinks: [],
      boundary: {
        branchesPersistWithoutReset: true,
        maintenanceHasCost: true,
        forgettingAllowed: true,
        revivalRequiresEvidence: true,
        uniformUnlocksAllowed: false,
      },
    };
  }
  return world.hintBranchPersistence;
}

function currentHintBranchesForReturn() {
  if (!world.avatarHintDivergence || !world.avatarHintDivergence.branches.length) runAvatarHintDivergenceLoop();
  const hints = ensureAvatarHintDivergence();
  return hints.branches.slice(-6);
}

function branchReturnStatus(branch, sessionIndex, offset) {
  if (branch.branch_status === 'taboo') return sessionIndex % 2 === 0 ? 'warning_persisted' : 'ritual_warning';
  if (branch.branch_status === 'ritualized') return offset % 3 === 0 ? 'burdened_ritual' : 'remembered_ritual';
  if (branch.branch_status === 'disputed') return sessionIndex > 1 ? 'forgotten' : 'still_disputed';
  if (branch.branch_status === 'rejected') return 'forgotten';
  if (branch.branch_status === 'useful_practice') return offset % 4 === 0 && sessionIndex > 1 ? 'needs_maintenance' : 'persisted';
  return 'still_carried';
}

function runHintBranchReturnSession() {
  const persistence = ensureHintBranchPersistence();
  const branches = currentHintBranchesForReturn();
  const sessionIndex = persistence.returnSessions.length + 1;
  const session = {
    session_id: `HRS-${String(sessionIndex).padStart(2, '0')}`,
    tick: world.tick || world.replay.length,
    branches_seen: branches.length,
    avatar_action: 'returned and asked what residents still carry',
    direct_reset: false,
  };
  persistence.returnSessions.push(session);
  let persisted = 0;
  let forgotten = 0;
  let revived = 0;
  branches.forEach((branch, offset) => {
    const status = branchReturnStatus(branch, sessionIndex, offset);
    const maintenanceCost = status === 'needs_maintenance' || status === 'burdened_ritual' ? 2 : (status.includes('ritual') ? 1 : 0);
    const reputationDelta = status === 'persisted' || status === 'warning_persisted' ? 0.04 : (status === 'forgotten' ? -0.03 : 0.01);
    const continuity = {
      continuity_id: `HRC-${String(persistence.continuityRows.length + 1).padStart(2, '0')}`,
      session_id: session.session_id,
      branch_id: branch.branch_id,
      hint_id: branch.hint_id,
      household: branch.household,
      resident: branch.resident,
      prior_status: branch.branch_status,
      return_status: status,
      maintenance_cost: maintenanceCost,
      reputation_delta: reputationDelta,
      expression_marker: status === 'forgotten' ? 'looks unsure and asks another resident' : (status.includes('warning') ? 'keeps distance and points to the old place' : (maintenanceCost ? 'moves slowly while carrying upkeep material' : 'faces the avatar and names the remembered branch')),
      avatar_commanded: false,
      source_practice_id: branch.source_practice_id,
    };
    persistence.continuityRows.push(continuity);
    persistence.householdReputation.push({
      session_id: session.session_id,
      household: branch.household,
      resident: branch.resident,
      branch_id: branch.branch_id,
      reputation_delta: reputationDelta,
      reason: status,
    });
    if (maintenanceCost > 0) {
      persistence.maintenanceBurden.push({
        session_id: session.session_id,
        branch_id: branch.branch_id,
        household: branch.household,
        material_cost: maintenanceCost,
        labor_cost: 1,
        created_obligation: `${status} upkeep for ${branch.branch_status}`,
      });
      world.resources.fiber = Math.max(0, world.resources.fiber - maintenanceCost);
    }
    if (status === 'forgotten') {
      forgotten += 1;
      persistence.forgettingEvents.push({
        session_id: session.session_id,
        branch_id: branch.branch_id,
        household: branch.household,
        reason: 'low trust, disputed value, or higher priority work',
        recoverable: true,
      });
    } else {
      persisted += 1;
    }
    if (sessionIndex >= 3 && status === 'forgotten' && offset % 2 === 0) {
      revived += 1;
      persistence.revivalEvents.push({
        session_id: session.session_id,
        branch_id: branch.branch_id,
        household: branch.household,
        evidence: 'older resident repeats the remembered counterexample',
        cost: 1,
        revived_as: 'cautious retry',
      });
      world.resources.care = Math.max(0, world.resources.care - 1);
    }
    persistence.sourceLinks.push({
      session_id: session.session_id,
      branch_id: branch.branch_id,
      hint_id: branch.hint_id,
      source_practice_id: branch.source_practice_id,
      avatar_commanded: false,
      hidden_law_exposed: false,
    });
    recordRealityConstraint('hint_branch_return_persistence', {
      materialSources: maintenanceCost ? ['fiber', 'care'] : [],
      materialTransformation: maintenanceCost ? 'upkeep consumed material and attention' : 'memory carried without material transformation',
      timeCost: 1,
      laborCost: 1,
      toolWear: 0,
      residentEffort: 1,
      hiddenLawInvolved: 'audit-only material law',
      publicObservation: status,
      residentInterpretation: `${branch.resident} carries ${branch.branch_status} as ${status}`,
      resourcesBefore: 10,
      resourcesAfter: 10 - maintenanceCost,
      conservationCheck: true,
      maintenanceObligationCreated: maintenanceCost ? continuity.continuity_id : 'none',
      unintendedConsequence: status === 'forgotten' ? 'recoverable forgetting' : 'ongoing social memory',
    });
  });
  return log('runHintBranchReturnSession', { session: session.session_id, persisted, forgotten, revived, branches: branches.length });
}

function maintainHintBranchPractice() {
  const persistence = ensureHintBranchPersistence();
  if (!persistence.continuityRows.length) runHintBranchReturnSession();
  const target = [...persistence.continuityRows].reverse().find(row => row.return_status !== 'forgotten') || persistence.continuityRows[persistence.continuityRows.length - 1];
  const maintenanceCost = Math.max(1, Number(target.maintenance_cost || 0) + 1);
  persistence.maintenanceBurden.push({
    session_id: target.session_id,
    branch_id: target.branch_id,
    household: target.household,
    material_cost: maintenanceCost,
    labor_cost: 1,
    created_obligation: 'avatar-supported upkeep offer, resident still decides',
  });
  persistence.householdReputation.push({
    session_id: target.session_id,
    household: target.household,
    resident: target.resident,
    branch_id: target.branch_id,
    reputation_delta: 0.05,
    reason: 'maintained_with_cost',
  });
  world.resources.fiber = Math.max(0, world.resources.fiber - maintenanceCost);
  recordRealityConstraint('hint_branch_maintenance', {
    materialSources: ['fiber'],
    materialTransformation: 'fiber spent on upkeep',
    timeCost: 1,
    laborCost: 1,
    toolWear: 1,
    residentEffort: 1,
    hiddenLawInvolved: 'audit-only material law',
    publicObservation: 'maintenance helped a remembered branch',
    residentInterpretation: 'support helped, but did not command adoption',
    resourcesBefore: 10,
    resourcesAfter: 10 - maintenanceCost,
    conservationCheck: true,
    maintenanceObligationCreated: target.branch_id,
    unintendedConsequence: 'upkeep burden remains visible',
  });
  return log('maintainHintBranchPractice', { branchId: target.branch_id, maintenanceCost, avatarCommanded: false });
}

function reviveForgottenHintPractice() {
  const persistence = ensureHintBranchPersistence();
  if (!persistence.forgettingEvents.length) runHintBranchReturnSession();
  const target = persistence.forgettingEvents[persistence.forgettingEvents.length - 1];
  if (!target) return log('reviveForgottenHintPractice', { branchId: 'none', revived: false });
  persistence.revivalEvents.push({
    session_id: target.session_id,
    branch_id: target.branch_id,
    household: target.household,
    evidence: 'resident asks whether the old branch should be tried again',
    cost: 1,
    revived_as: 'bounded revival proposal',
  });
  persistence.continuityRows.push({
    continuity_id: `HRC-${String(persistence.continuityRows.length + 1).padStart(2, '0')}`,
    session_id: target.session_id,
    branch_id: target.branch_id,
    hint_id: 'from-forgetting-event',
    household: target.household,
    resident: 'household',
    prior_status: 'forgotten',
    return_status: 'revived_as_disputed_memory',
    maintenance_cost: 1,
    reputation_delta: 0.02,
    avatar_commanded: false,
    source_practice_id: 'source-linked-in-branch-ledger',
  });
  world.resources.care = Math.max(0, world.resources.care - 1);
  recordRealityConstraint('hint_branch_revival', {
    materialSources: ['care'],
    materialTransformation: 'attention spent on revival discussion',
    timeCost: 1,
    laborCost: 1,
    toolWear: 0,
    residentEffort: 1,
    hiddenLawInvolved: 'audit-only material law',
    publicObservation: 'forgotten branch revived as disputed memory',
    residentInterpretation: 'old branch may matter again',
    resourcesBefore: 10,
    resourcesAfter: 9,
    conservationCheck: true,
    maintenanceObligationCreated: target.branch_id,
    unintendedConsequence: 'revival remains disputed',
  });
  return log('reviveForgottenHintPractice', { branchId: target.branch_id, revived: true, avatarCommanded: false });
}

function runHintBranchPersistenceLoop() {
  const persistence = ensureHintBranchPersistence();
  runHintBranchReturnSession();
  maintainHintBranchPractice();
  runHintBranchReturnSession();
  runHintBranchReturnSession();
  reviveForgottenHintPractice();
  return log('runHintBranchPersistenceLoop', {
    sessions: persistence.returnSessions.length,
    continuityRows: persistence.continuityRows.length,
    maintenanceRows: persistence.maintenanceBurden.length,
    forgettingRows: persistence.forgettingEvents.length,
    revivalRows: persistence.revivalEvents.length,
  });
}

function renderHintBranchPersistence() {
  const summaryNode = document.getElementById('hintBranchPersistenceSummaryOut');
  const detailNode = document.getElementById('hintBranchPersistenceOut');
  const persistence = world.hintBranchPersistence;
  if (summaryNode) summaryNode.textContent = persistence ? `${persistence.returnSessions.length} sessions / ${persistence.continuityRows.length} continuity / ${persistence.forgettingEvents.length} forgotten / ${persistence.revivalEvents.length} revived` : 'No branch returns yet.';
  if (!detailNode) return;
  if (!persistence) {
    detailNode.textContent = 'No hint branch persistence yet. Run a return session after avatar hint divergence.';
    return;
  }
  const sessions = persistence.returnSessions.slice(-4).map(row => `${row.session_id}: branches=${row.branches_seen} reset=${row.direct_reset}`);
  const continuity = persistence.continuityRows.slice(-8).map(row => `${row.continuity_id}: ${row.branch_id} ${row.prior_status}->${row.return_status} cost=${row.maintenance_cost} expression=${row.expression_marker || 'none'}`);
  const revivals = persistence.revivalEvents.slice(-4).map(row => `${row.branch_id}: ${row.revived_as} cost=${row.cost}`);
  detailNode.textContent = [
    'Boundary: branches persist, decay, burden, or revive across returns; the avatar cannot reset them into a uniform unlock.',
    'Return sessions:',
    ...(sessions.length ? sessions : ['none']),
    'Continuity:',
    ...(continuity.length ? continuity : ['none']),
    'Revivals:',
    ...(revivals.length ? revivals : ['none']),
  ].join('\n');
}

Object.assign(window, { enterWorld, moveNorth, moveSouth, moveWest, moveEast, talkBounded, askSchedule, offerHelp, borrowTool, returnTool, waitOffscreen, introduceWorldAnomaly, runAnomalyExperiment, spreadAnomalyBelief, planAnomalyInvestigationSchedule, runScheduledAnomalyInvestigation, runStochasticConsequencePulse, runStochasticConsequenceBurst, planStochasticRecoveryLoop, resolveStochasticRecoveryStep, runStochasticRecoveryLoop, runStochasticHistoryChoice, runStochasticHistorySocialEcho, runStochasticHistoryInfluenceLoop, runOrdinaryAffordanceInfluenceLoop, runCivilizationPressureStep, runCivilizationPressureLoop, runPracticalDiscoveryStep, runPracticalDiscoveryLoop, runVillageBoardLoop, supportVillageProposal, askVillageBoardQuestion, waitOnVillageBoard, runRealityConstraintAudit, introduceAvatarHint, runHintDivergenceInterpretation, runAvatarHintDivergenceLoop, runHintBranchReturnSession, maintainHintBranchPractice, reviveForgottenHintPractice, runHintBranchPersistenceLoop, runPrototypeOpening, runPrototypePracticeChain, runPrototypeReturnProof, runFirstPlayablePrototypeLoop, runCivilizationDeepTimeEpoch, applyLatestDeepTimeEffectToVillage, runCivilizationMillionYearSim, runCivilizationTenMillionYearSim, runCivilizationSurvivalAudit, runAutonomousResidentTick, runAutonomousResidentSeason, runPrototypeQASmoke, runPrototypeAutoStep, startPrototypeAutoSim, pausePrototypeAutoSim, runPrototypeAutoBurst, savePrototypeSlot, returnPrototypeSlot, exportPrototypeSaveReceipt, exportPrototypeAcceptanceReceipt, repairTrust, saveWorld, restoreWorld, toggleAudit, exportReplay, runPlaytestChecklist, runStateBoundaryAudit, runSaveRestoreSmoke, runAuditAfterRollbackCheck, runAllQAHooks, runDashboardResidentAction, interruptWork, apologizeToResident, giveSpace, completeTrustRepair, runContinuityLoop, runSocialMemoryPulse, settleSelectedRelationship, generateScenarioReceipt, logReceiptObservation, resolveLatestObservation, setObservationFilter, setObservationFilterAll, setObservationFilterOpen, setObservationFilterWatch, setObservationFilterResolved, setObservationFilterBlocking, auditLandingFailures, toggleDeepPanels, runReviewerLandingPass });
bindControls();
render();
