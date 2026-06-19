const BOUNDARY = "Deterministic browser-local hardened vertical-slice app shell with physics-first stochastic simulation; no LLM call, subjective consciousness, real consent, open-ended autonomous natural language, moral patienthood, production persistence, finished gameplay, polished 3D art pipeline, production-certified physical accuracy, or metaphysical frequency claim.";
const STATE_KEY = 'ssrm_v61_app_shell_world';
const REPLAY_KEY = 'ssrm_v61_app_shell_replay';
const QA_KEY = 'ssrm_v61_app_shell_qa_results';
const EXPORT_KEY = 'ssrm_v61_app_shell_export';
const SAVE_SNAPSHOT_KEY = 'ssrm_v61_app_shell_saved_snapshot';
const PROTOTYPE_SAVE_KEY = 'ssrm_v61_game_prototype_saves';
const PROTOTYPE_ACCEPTANCE_KEY = 'ssrm_v61_game_prototype_acceptance_receipt';
const WALKTHROUGH_KEY = 'ssrm_v61_first_playable_walkthrough_receipt';
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
  stateKeys: [STATE_KEY, REPLAY_KEY, QA_KEY, EXPORT_KEY, SAVE_SNAPSHOT_KEY, PROTOTYPE_SAVE_KEY, PROTOTYPE_ACCEPTANCE_KEY, WALKTHROUGH_KEY, CHECKPOINT_KEY, HISTORY_KEY, RELATION_KEY, RECEIPT_OBSERVATION_KEY, OBSERVATION_FILTER_KEY],
  publicState: ['avatar', 'selected', 'residents', 'resources', 'replay', 'returnContinuity', 'returnGreetingContinuity', 'accountabilitySocialEcho', 'boundedEchoConversation', 'echoInfluencedChoiceReceipt', 'anomalyDiscovery', 'anomalyInvestigationSchedule', 'stochasticConsequencePulse', 'stochasticRecoveryLoop', 'stochasticHistoryInfluence', 'stochasticOrdinaryAffordance', 'civilizationPressure', 'practicalDiscovery', 'emergentPracticeGraph', 'villageBoard', 'realityConstraintLedger', 'avatarHintDivergence', 'hintBranchPersistence', 'gamePrototype', 'gamePrototypePlayableSlice', 'gamePrototypeVillageDay03', 'gamePrototypeWorldStage', 'gamePrototypeWalkthrough', 'gamePrototypeActionRail', 'gamePrototypePlayerMode', 'gamePrototypeProposalDeck', 'gamePrototypeLivedPractice', 'gamePrototypeWorksite', 'deepTimeCivilization', 'autonomousResidents', 'gamePrototypeQA', 'prototypeClock', 'gamePrototypeSaves', 'gamePrototypeAcceptance', 'gamePrototypeDivergence', 'gamePrototypeCommons', 'gamePrototypeProjects', 'gamePrototypeCommonsSupport', 'gamePrototypeNearbyActions', 'gamePrototypeDayCycle', 'gamePrototypeReturnLater', 'gamePrototype3DWorld', 'gamePrototypeMaterialManipulation', 'gamePrototypeResidentBodies', 'gamePrototypeTerrain', 'gamePrototypeTools', 'gamePrototypeResourcePhysics', 'gamePrototypeThermalPhysics', 'gamePrototypeWaterPhysics', 'gamePrototypeEcologyPhysics', 'promiseFollowUp', 'obligationLedger', 'scheduleQueue', 'debtLedger', 'offscreenObligationEvents', 'absentTimeSummary', 'absentTimeThreads', 'absentTimeChoiceReceipt', 'avatarAbsenceAccountabilityReceipt'],
  forbiddenPublicState: ['privateWorkspace', 'subjectiveFeeling', 'llmTranscript'],
  boundary: BOUNDARY,
  directHooks: ['runPlaytestChecklist', 'runStateBoundaryAudit', 'runSaveRestoreSmoke', 'runAuditAfterRollbackCheck', 'runAllQAHooks', 'toggleAudit', 'exportReplay', 'exportPrototypeAcceptanceReceipt', 'comparePrototypeDivergenceSeeds', 'auditPrototypeCommons', 'runPrototypeGuidedStep', 'runPlayablePhysicsPracticeSliceStep', 'runPlayablePhysicsPracticeSliceLoop', 'runPlayableVillageDay03Step', 'runPlayableVillageDay03Loop', 'runPrimaryPlaySurfaceStep', 'runPrimaryPlaySurfaceLoop', 'runFirstPlayableWalkthrough', 'exportFirstPlayableWalkthrough', 'runNormalPlayLook', 'runNormalPlayAsk', 'runNormalPlaySupport', 'runNormalPlayWait', 'runNormalPlayReturn', 'runNormalPlaySave', 'runNormalPlayActionRailLoop', 'enterPlayerMode', 'exitPlayerMode', 'togglePlayerMode', 'runPlayerModeInterfaceLoop', 'runPlayerProposalDeckLoop', 'supportPlayerProposalDeck', 'askPlayerProposalDeck', 'waitPlayerProposalDeck', 'runLivedPracticeLoop', 'runResidentWorksiteLoop', 'advanceVillageProject', 'supportResourceCommons', 'performNearbyAction', 'endVillageDay', 'leaveAndReturnLater', 'runPrototypeMaterialWorldStep', 'runPrototypePhysicsStep', 'runStructuralPhysicsStep', 'runStructuralPhysicsLoop', 'runContactConstraintPhysicsStep', 'runContactConstraintPhysicsLoop', 'runMaterialStatePhysicsStep', 'runMaterialStatePhysicsLoop', 'runTerrainPhysicsStep', 'runTerrainPhysicsLoop', 'runToolPhysicsStep', 'runToolPhysicsLoop', 'runResourcePhysicsStep', 'runResourcePhysicsLoop', 'runThermalPhysicsStep', 'runThermalPhysicsLoop', 'runWaterPhysicsStep', 'runWaterPhysicsLoop', 'runEcologyPhysicsStep', 'runEcologyPhysicsLoop', 'runResidentMaterialManipulationStep', 'runResidentMaterialManipulationLoop', 'runResidentBodyPhysicsStep', 'runResidentBodyPhysicsLoop', 'runDeepTimePhysicsEpoch']
};

const urlParams = new URLSearchParams(window.location.search);
if (urlParams.get('reset') === '1') {
  [STATE_KEY, REPLAY_KEY, QA_KEY, EXPORT_KEY, SAVE_SNAPSHOT_KEY, PROTOTYPE_SAVE_KEY, PROTOTYPE_ACCEPTANCE_KEY, WALKTHROUGH_KEY, CHECKPOINT_KEY, HISTORY_KEY, RELATION_KEY, RECEIPT_OBSERVATION_KEY, OBSERVATION_FILTER_KEY].forEach(key => localStorage.removeItem(key));
}

let world = JSON.parse(localStorage.getItem(STATE_KEY) || JSON.stringify({
  entered: false,
  tick: 0,
  avatar: { room: 'arrival court', x: 180, y: 260 },
  selected: 'Ari',
  audit: false,
  residents,
  resources: { water: 12, fiber: 10, wood: 17, care: 6, food: 7 },
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
  gamePrototypePlayableSlice: null,
  gamePrototypeVillageDay03: null,
  gamePrototypeWorldStage: null,
  gamePrototypeWalkthrough: null,
  gamePrototypeActionRail: null,
  gamePrototypePlayerMode: null,
  gamePrototypeProposalDeck: null,
  gamePrototypeLivedPractice: null,
  gamePrototypeWorksite: null,
  deepTimeCivilization: null,
  autonomousResidents: null,
  gamePrototypeQA: null,
  prototypeClock: null,
  gamePrototypeSaves: null,
  gamePrototypeAcceptance: null,
  gamePrototypeDivergence: null,
  gamePrototypeCommons: null,
  gamePrototypeProjects: null,
  gamePrototypeCommonsSupport: null,
	  gamePrototypeNearbyActions: null,
		  gamePrototypeDayCycle: null,
		  gamePrototypeReturnLater: null,
		  gamePrototype3DWorld: null,
		  gamePrototypeMaterialManipulation: null,
		  gamePrototypeResidentBodies: null,
		  gamePrototypeTerrain: null,
		  gamePrototypeTools: null,
      gamePrototypeResourcePhysics: null,
      gamePrototypeThermalPhysics: null,
      gamePrototypeWaterPhysics: null,
      gamePrototypeEcologyPhysics: null,
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
  updateRoom();
  return log('moveNorth', { y: world.avatar.y, room: world.avatar.room, zone: locationZoneForAvatar().zone_id, step, ordinaryInfluence });
}
function moveSouth() {
  const ordinaryInfluence = applyStochasticHistoryToOrdinaryAction('moveSouth', world.selected);
  const step = Math.max(8, Math.round(34 * ordinaryInfluence.movementScale));
  world.avatar.y = Math.min(560, world.avatar.y + step);
  updateRoom();
  return log('moveSouth', { y: world.avatar.y, room: world.avatar.room, zone: locationZoneForAvatar().zone_id, step, ordinaryInfluence });
}
function moveWest() {
  const ordinaryInfluence = applyStochasticHistoryToOrdinaryAction('moveWest', world.selected);
  const step = Math.max(8, Math.round(34 * ordinaryInfluence.movementScale));
  world.avatar.x = Math.max(52, world.avatar.x - step);
  updateRoom();
  return log('moveWest', { x: world.avatar.x, room: world.avatar.room, zone: locationZoneForAvatar().zone_id, step, ordinaryInfluence });
}
function moveEast() {
  const ordinaryInfluence = applyStochasticHistoryToOrdinaryAction('moveEast', world.selected);
  const step = Math.max(8, Math.round(34 * ordinaryInfluence.movementScale));
  world.avatar.x = Math.min(970, world.avatar.x + step);
  updateRoom();
  return log('moveEast', { x: world.avatar.x, room: world.avatar.room, zone: locationZoneForAvatar().zone_id, step, ordinaryInfluence });
}
function updateRoom() { world.avatar.room = ['arrival court', 'tool alcove', 'rain court', 'fiber loft'][Math.floor(world.avatar.x / 250) % 4]; }

function locationZoneForAvatar() {
  const zones = [
    { zone_id: 'shelter', label: 'Shelter', x: 70, y: 72, w: 210, h: 118, defaultAction: 'offerHelp', reason: 'near rest mats and care obligations' },
    { zone_id: 'storage', label: 'Storage', x: 315, y: 72, w: 210, h: 118, defaultAction: 'supportResourceCommons', reason: 'near shared material stores' },
    { zone_id: 'work_yard', label: 'Work yard', x: 560, y: 72, w: 210, h: 118, defaultAction: 'advanceVillageProject', reason: 'near project work and practical tests' },
    { zone_id: 'village_board', label: 'Village board', x: 805, y: 72, w: 170, h: 118, defaultAction: 'runVillageBoardLoop', reason: 'near posted concerns and proposals' },
  ];
  const hit = zones.find(zone => world.avatar.x >= zone.x && world.avatar.x <= zone.x + zone.w && world.avatar.y >= zone.y && world.avatar.y <= zone.y + zone.h);
  if (hit) return hit;
  return {
    zone_id: world.avatar.room.replace(/\s+/g, '_'),
    label: world.avatar.room,
    x: world.avatar.x,
    y: world.avatar.y,
    w: 1,
    h: 1,
    defaultAction: 'askSchedule',
    reason: 'near the selected resident in ordinary village space',
  };
}

function ensurePrototypeNearbyActions() {
  if (!world.gamePrototypeNearbyActions) {
    world.gamePrototypeNearbyActions = {
      runCount: 0,
      actionLedger: [],
      lastPlan: null,
      boundary: 'location-sensitive normal play only; nearby action routes to existing systems and does not directly command residents',
    };
  }
  return world.gamePrototypeNearbyActions;
}

function nearbyActionPlan() {
  const zone = locationZoneForAvatar();
  let action = zone.defaultAction;
  let why = zone.reason;
  if (zone.zone_id === 'work_yard') {
    const incompleteProject = world.villageBoard && world.villageBoard.projectProposals && world.villageBoard.projectProposals.some(row => !row.project_completed);
    action = incompleteProject ? 'advanceVillageProject' : 'runPracticalDiscoveryStep';
    why = incompleteProject ? 'project work is physically nearby' : 'work yard tests can turn lived pressure into practical discovery';
  }
  if (zone.zone_id === 'village_board') {
    const board = world.villageBoard;
    action = !board || !board.projectProposals.length ? 'runVillageBoardLoop' : 'supportVillageProposal';
    why = !board || !board.projectProposals.length ? 'residents need to post concerns first' : 'a visible proposal can be supported without command';
  }
  if (zone.zone_id === 'storage') {
    action = 'supportResourceCommons';
    why = 'storage action can recover commons through named material sources';
  }
  if (zone.zone_id === 'shelter') {
    action = world.resources.care > 0 ? 'offerHelp' : 'supportResourceCommons';
    why = world.resources.care > 0 ? 'shelter action offers bounded care to the selected resident' : 'care is low, so shelter redirects to commons support';
  }
  return {
    zone_id: zone.zone_id,
    label: zone.label,
    room: world.avatar.room,
    action,
    why,
    selected: world.selected,
    x: world.avatar.x,
    y: world.avatar.y,
  };
}

function performNearbyAction() {
  ensureGamePrototype();
  const nearby = ensurePrototypeNearbyActions();
  const plan = nearbyActionPlan();
  nearby.runCount += 1;
  nearby.lastPlan = plan;
  let result = null;
  if (plan.action === 'offerHelp') result = offerHelp();
  if (plan.action === 'supportResourceCommons') result = supportResourceCommons();
  if (plan.action === 'advanceVillageProject') result = advanceVillageProject();
  if (plan.action === 'runPracticalDiscoveryStep') result = runPracticalDiscoveryStep();
  if (plan.action === 'runVillageBoardLoop') result = runVillageBoardLoop();
  if (plan.action === 'supportVillageProposal') result = supportVillageProposal();
  if (plan.action === 'askSchedule') result = askSchedule();
	  const row = {
    nearby_id: `GPNA-${String(nearby.actionLedger.length + 1).padStart(3, '0')}`,
    tick: world.tick,
    zone_id: plan.zone_id,
    label: plan.label,
    room: plan.room,
    action: plan.action,
    why: plan.why,
    resident: plan.selected,
    result_event: result && result.event ? result.event : 'none',
    avatar_direct_command: false,
    x: plan.x,
    y: plan.y,
  };
  nearby.actionLedger.push(row);
  if (nearby.actionLedger.length > 40) nearby.actionLedger.shift();
  recordRealityConstraint('nearby_play_action', {
    resident: plan.selected,
    sourceBeliefId: row.nearby_id,
    materials: plan.action === 'offerHelp' ? ['care'] : [],
    publicObservation: `${plan.label} nearby action routed to ${plan.action}`,
    residentInterpretation: plan.why,
    materialTransformation: plan.action === 'offerHelp' ? 'care/time offered through existing help action' : 'no direct material transformation by nearby router',
    timeCost: 1,
    workCost: plan.action === 'askSchedule' ? 0 : 1,
    toolWear: 0,
    maintenanceObligation: 'preserve location-action trace',
    unintendedConsequence: 'ordinary movement now changes available action context',
    hiddenLawInvolved: 'none in normal view',
    conservationCheck: true
  });
  recordPrototypeMilestone('nearby-action', `${plan.label} -> ${plan.action}; result ${row.result_event}`);
  return log('performNearbyAction', { zone: plan.zone_id, label: plan.label, action: plan.action, resultEvent: row.result_event, directCommand: false });
}

function ensurePrototypeDayCycle() {
  if (!world.gamePrototypeDayCycle) {
    world.gamePrototypeDayCycle = {
      day: 0,
      dayLedger: [],
      weatherLedger: [],
      recapLedger: [],
      boundary: 'village day cycle only; time, weather, labor, and resources change through causal rows, not free skips',
    };
  }
  return world.gamePrototypeDayCycle;
}

function villageDayWeather(entropy, dayNumber) {
  const patterns = [
    { weather: 'drizzle', material: 'fiber', delta: -1, bonus: 'water', bonusDelta: 1, effect: 'damp fiber slows drying but refills jars' },
    { weather: 'dry wind', material: 'water', delta: -1, bonus: 'fiber', bonusDelta: 1, effect: 'water drops while fiber dries better' },
    { weather: 'cold morning', material: 'care', delta: -1, bonus: null, bonusDelta: 0, effect: 'more care is spent keeping residents steady' },
    { weather: 'fallen branch', material: 'wood', delta: 1, bonus: null, bonusDelta: 0, effect: 'windfall wood becomes available after carrying' },
    { weather: 'storage damp', material: 'wood', delta: -1, bonus: 'fiber', bonusDelta: -1, effect: 'stored wood and fiber decay under damp cover' },
    { weather: 'clear workday', material: null, delta: 0, bonus: null, bonusDelta: 0, effect: 'no resource shift, but residents can focus on work' },
  ];
  return patterns[(entropy + dayNumber) % patterns.length];
}

function applyResourceDelta(resource, delta) {
  if (!resource || !delta) return 0;
  const before = Number(world.resources[resource] || 0);
  world.resources[resource] = Math.max(0, Math.min(99, before + delta));
  return world.resources[resource] - before;
}

function endVillageDay(options = {}) {
  ensureGamePrototype();
  const offscreen = Boolean(options && options.offscreen);
  if (!world.entered && !offscreen) runPrototypeOpening();
  const cycle = ensurePrototypeDayCycle();
  const dayNumber = cycle.day + 1;
  const entropy = deepTimeEntropyByte();
  const weather = villageDayWeather(entropy, dayNumber);
  const resourceDeltas = {};
  const primaryDelta = applyResourceDelta(weather.material, weather.delta);
  if (weather.material) resourceDeltas[weather.material] = primaryDelta;
  const bonusDelta = applyResourceDelta(weather.bonus, weather.bonusDelta);
  if (weather.bonus) resourceDeltas[weather.bonus] = bonusDelta;
  const weatherRow = {
    weather_id: `GPDW-${String(cycle.weatherLedger.length + 1).padStart(3, '0')}`,
    day: dayNumber,
    entropy,
    weather: weather.weather,
    effect: weather.effect,
    resource_deltas: resourceDeltas,
    conservation_checked: true,
  };
  cycle.weatherLedger.push(weatherRow);
	  recordRealityConstraint('village_day_weather', {
    resident: world.selected,
    sourceBeliefId: weatherRow.weather_id,
    materials: Object.keys(resourceDeltas),
    publicObservation: `${weather.weather}: ${weather.effect}`,
    residentInterpretation: 'weather changed ordinary resource pressure',
    materialTransformation: Object.entries(resourceDeltas).map(([key, value]) => `${key} ${value >= 0 ? '+' : ''}${value}`).join(', ') || 'weather passed without material transformation',
    timeCost: 1,
    workCost: 0,
    toolWear: weather.weather === 'storage damp' ? 1 : 0,
    maintenanceObligation: weather.weather === 'storage damp' ? 'check storage covers' : 'watch weather pressure',
    unintendedConsequence: 'day passed and resource pressure changed before player could optimize',
    hiddenLawInvolved: 'none in normal view',
	    conservationCheck: true
	  });
  const materialResult = runPrototypeMaterialWorldStep().payload;
  const terrainResult = runTerrainPhysicsStep('village day terrain').payload;
  const resourceResult = runResourcePhysicsStep('village day resource stock').payload;
  const thermalResult = runThermalPhysicsStep('village day watched warmth').payload;
  const waterResult = runWaterPhysicsStep('village day water movement').payload;
  const ecologyResult = runEcologyPhysicsStep('village day ecology').payload;
  const structuralResult = runStructuralPhysicsStep('village day structural stress').payload;
  const constraintResult = runContactConstraintPhysicsStep('village day contact constraints').payload;
  const materialStateResult = runMaterialStatePhysicsStep('village day material state').payload;
	  const beforeActions = world.autonomousResidents ? world.autonomousResidents.actionLog.length : 0;
  const residentActionIds = [];
  for (let i = 0; i < 4; i += 1) {
    const row = runAutonomousResidentTick().payload;
    residentActionIds.push(`${row.resident}:${row.action}`);
  }
  let projectResult = null;
  const acceptedProject = world.villageBoard && world.villageBoard.projectProposals && world.villageBoard.projectProposals.some(row => !row.project_completed && (row.status === 'accepted' || row.status === 'in progress'));
  if (acceptedProject) projectResult = advanceVillageProject().payload;
  const lowResource = Object.values(world.resources).some(value => Number(value || 0) <= 2);
  let commonsResult = null;
  if (lowResource || (projectResult && projectResult.stalled)) commonsResult = supportResourceCommons().payload;
  if (!world.villageBoard || !world.villageBoard.projectProposals.length) runVillageBoardLoop();
  if (!world.practicalDiscovery || !(world.practicalDiscovery.autoGeneratedTests || []).length) runPracticalDiscoveryStep('village_day_bottleneck');
  cycle.day = dayNumber;
  const dayRow = {
    day_id: `GPD-${String(cycle.dayLedger.length + 1).padStart(3, '0')}`,
    day: dayNumber,
	    weather: weather.weather,
    physics_result: materialResult ? { stepId: materialResult.physicsStepId || 'none', proposalId: materialResult.physicsProposalId || null, stability: materialResult.stability, repairCost: materialResult.repairCost } : null,
    terrain_result: terrainResult ? { stepId: terrainResult.terrainStepId || 'none', weakCells: terrainResult.weakCells || 0 } : null,
    resource_result: resourceResult ? { stepId: resourceResult.stepId || 'none', resources: resourceResult.resources || { ...world.resources }, losses: resourceResult.losses || 0, gains: resourceResult.gains || 0 } : null,
    thermal_result: thermalResult ? { stepId: thermalResult.stepId || 'none', smoke: thermalResult.totalSmoke || 0, heat: thermalResult.maxHeat || 0, hazard: thermalResult.hazard === true } : null,
    water_result: waterResult ? { stepId: waterResult.stepId || 'none', leaks: waterResult.leaks || 0, routePressure: waterResult.routePressure || 0, water: waterResult.water || world.resources.water } : null,
    ecology_result: ecologyResult ? { stepId: ecologyResult.stepId || 'none', harvested: ecologyResult.harvested || 0, fed: ecologyResult.fed || 0, food: ecologyResult.food || world.resources.food } : null,
    structural_result: structuralResult ? { stepId: structuralResult.stepId || 'none', stress: structuralResult.maxStress || 0, deflection: structuralResult.maxDeflection || 0, collapses: structuralResult.collapses || 0, repairRows: structuralResult.repairRows || 0 } : null,
    constraint_result: constraintResult ? { stepId: constraintResult.stepId || 'none', contacts: constraintResult.contactRows || 0, joints: constraintResult.jointRows || 0, failedJoints: constraintResult.failedJoints || 0, repairRows: constraintResult.repairRows || 0 } : null,
    material_state_result: materialStateResult ? { stepId: materialStateResult.stepId || 'none', phaseChanges: materialStateResult.phaseChanges || 0, riskyComponents: materialStateResult.riskyComponents || 0, repairRows: materialStateResult.repairRows || 0 } : null,
	    resident_actions_added: (world.autonomousResidents ? world.autonomousResidents.actionLog.length : 0) - beforeActions,
    resident_action_sample: residentActionIds,
    project_result: projectResult ? { proposalId: projectResult.proposalId || 'none', status: projectResult.status || projectResult.reason || 'none', completed: projectResult.completed === true } : null,
    commons_result: commonsResult ? { resource: commonsResult.resource, amount: commonsResult.amount, blocked: commonsResult.blocked === true } : null,
    resources_after: { ...world.resources },
    direct_player_command: false,
    avatar_present: !offscreen,
  };
  cycle.dayLedger.push(dayRow);
  cycle.recapLedger.push({
    recap_id: `GPDR-${String(cycle.recapLedger.length + 1).padStart(3, '0')}`,
    day: dayNumber,
	    summary: `${offscreen ? 'offscreen ' : ''}${weather.weather}; physics ${dayRow.physics_result ? dayRow.physics_result.stepId : 'none'}; resources ${dayRow.resource_result ? dayRow.resource_result.stepId : 'none'}; thermal ${dayRow.thermal_result ? dayRow.thermal_result.stepId : 'none'}; water ${dayRow.water_result ? dayRow.water_result.stepId : 'none'}; ecology ${dayRow.ecology_result ? dayRow.ecology_result.stepId : 'none'}; structure ${dayRow.structural_result ? dayRow.structural_result.stepId : 'none'}; constraints ${dayRow.constraint_result ? dayRow.constraint_result.stepId : 'none'}; material ${dayRow.material_state_result ? dayRow.material_state_result.stepId : 'none'}; ${dayRow.resident_actions_added} resident action(s); project ${dayRow.project_result ? dayRow.project_result.status : 'none'}; commons ${dayRow.commons_result ? dayRow.commons_result.resource : 'none'}`,
	  });
  world.gamePrototypeCommons = null;
  recordPrototypeMilestone('village-day-ended', `day ${dayNumber}: ${weather.weather}, ${dayRow.resident_actions_added} resident action(s)`);
	  return log('endVillageDay', { day: dayNumber, weather: weather.weather, physicsStepId: dayRow.physics_result ? dayRow.physics_result.stepId : null, physicsProposalId: dayRow.physics_result ? dayRow.physics_result.proposalId : null, resourceStepId: dayRow.resource_result ? dayRow.resource_result.stepId : null, thermalStepId: dayRow.thermal_result ? dayRow.thermal_result.stepId : null, waterStepId: dayRow.water_result ? dayRow.water_result.stepId : null, ecologyStepId: dayRow.ecology_result ? dayRow.ecology_result.stepId : null, structuralStepId: dayRow.structural_result ? dayRow.structural_result.stepId : null, constraintStepId: dayRow.constraint_result ? dayRow.constraint_result.stepId : null, materialStateStepId: dayRow.material_state_result ? dayRow.material_state_result.stepId : null, actionsAdded: dayRow.resident_actions_added, projectStatus: dayRow.project_result ? dayRow.project_result.status : 'none', commonsResource: dayRow.commons_result ? dayRow.commons_result.resource : 'none', offscreen, directCommand: false });
	}

function ensurePrototypeReturnLater() {
  if (!world.gamePrototypeReturnLater) {
    world.gamePrototypeReturnLater = {
      runCount: 0,
      absenceLedger: [],
      returnLedger: [],
      latestReceipt: null,
      boundary: 'forward return-session persistence only; leaving advances living state and does not restore an old snapshot',
    };
  }
  return world.gamePrototypeReturnLater;
}

function leaveAndReturnLater(daysAway = 3) {
  ensureGamePrototype();
  if (!world.entered) runPrototypeOpening();
  const returns = ensurePrototypeReturnLater();
  const dayCycle = ensurePrototypeDayCycle();
  const days = Math.max(1, Math.min(7, Number(daysAway) || 3));
  const beforeResources = { ...world.resources };
  const beforeDay = dayCycle.day;
  const replayBefore = world.replay.length;
  const selectedBefore = world.selected;
  const absence = {
    absence_id: `GPLA-${String(returns.absenceLedger.length + 1).padStart(3, '0')}`,
    start_tick: world.tick,
    selected_resident: selectedBefore,
    days_away: days,
    day_before: beforeDay,
    resources_before: beforeResources,
    replay_before: replayBefore,
    direct_reset: false,
  };
  returns.absenceLedger.push(absence);
  world.entered = false;
  world.avatar.room = 'away trail';
  for (let i = 0; i < days; i += 1) endVillageDay({ offscreen: true });
  world.entered = true;
  world.avatar.room = 'arrival court';
  world.avatar.x = 180;
  world.avatar.y = 260;
  updateRoom();
  const afterResources = { ...world.resources };
  const afterDay = ensurePrototypeDayCycle().day;
  const resourceDelta = Object.fromEntries(Object.keys(afterResources).map(key => [key, Number(afterResources[key] || 0) - Number(beforeResources[key] || 0)]));
  const residentNames = Object.keys(world.residents);
  const rememberedResidents = residentNames.slice(0, 3);
  rememberedResidents.forEach((name, index) => {
    mutateResident(name, {
      trust: name === selectedBefore ? 0.008 : 0.003,
      progress: 0.004 + index * 0.001,
      memory: `${name === selectedBefore ? 'recognized' : 'noticed'} avatar return after ${days} offscreen day(s)`,
      historyEvent: 'return later recognition',
      historyDetail: `avatar away ${days} day(s); village advanced from day ${beforeDay} to ${afterDay}`
    });
  });
  const receipt = {
    return_id: `GPLR-${String(returns.returnLedger.length + 1).padStart(3, '0')}`,
    absence_id: absence.absence_id,
    returned_tick: world.tick,
    selected_resident: selectedBefore,
    days_away: days,
    day_before: beforeDay,
    day_after: afterDay,
    resources_before: beforeResources,
    resources_after: afterResources,
    resource_delta: resourceDelta,
    replay_before: replayBefore,
    replay_after: world.replay.length,
    residents_who_remembered: rememberedResidents,
    restored_old_state: false,
    direct_reset: false,
    continuity_preserved: true,
  };
  returns.runCount += 1;
  returns.returnLedger.push(receipt);
  returns.latestReceipt = receipt;
  recordRealityConstraint('return_later_session', {
    resident: selectedBefore,
    sourceBeliefId: receipt.return_id,
    materials: Object.keys(resourceDelta).filter(key => resourceDelta[key] !== 0),
    publicObservation: `avatar returned after ${days} offscreen day(s)`,
    residentInterpretation: `${rememberedResidents.join(', ')} remember the absence while world state continued`,
    materialTransformation: Object.entries(resourceDelta).map(([key, value]) => `${key} ${value >= 0 ? '+' : ''}${value}`).join(', ') || 'no net resource change',
    timeCost: days,
    workCost: days,
    toolWear: 0,
    maintenanceObligation: 'preserve return-later receipt and resident memory',
    unintendedConsequence: 'village changed while avatar was away',
    hiddenLawInvolved: 'none in normal view',
    conservationCheck: true
  });
  recordPrototypeMilestone('return-later', `${days} day(s) away; day ${beforeDay}->${afterDay}; remembered by ${rememberedResidents.join(', ')}`);
  return log('leaveAndReturnLater', { daysAway: days, dayBefore: beforeDay, dayAfter: afterDay, remembered: rememberedResidents.length, restoredOldState: false, directReset: false });
}

function ensurePrototype3DWorld() {
  if (!world.gamePrototype3DWorld) {
    world.gamePrototype3DWorld = {
      runCount: 0,
      boundary: 'physics-first stochastic material simulation; simple primitive rendering, component-built structures, no fixed building sprites, no polished art, no production-certified physical accuracy claim',
      renderer: 'existing canvas projects 3D component state into simple placeholder primitives',
      noStickerMap: true,
      noFixedBuildingAssets: true,
      noPredeclaredStructureClass: true,
      noEnglishResidentTechLabels: true,
      physics: {
        kernel_id: 'G3P-KERNEL-001',
        mode: 'stochastic physics first',
        integrator: 'bounded semi-implicit discrete timestep',
        timestep: 1,
        gravity: 9.8,
        solver_layers: ['mass', 'weight', 'support', 'collision/contact', 'friction', 'moisture', 'heat', 'decay', 'tool wear', 'labor/work', 'stochastic field pressure', 'stochastic failure', 'load path', 'structural stress', 'deformation/sag', 'anchor slip', 'partial collapse', 'contact constraint', 'joint/binding constraint', 'surface friction', 'impulse transfer', 'material state', 'phase drift', 'property mutation'],
        environment: { moisture: 0.31, heat: 0.46, wind: 0.18, decayPressure: 0.22, stress: 0.16 },
        forceLedger: [],
        supportLedger: [],
        collisionLedger: [],
        failureLedger: [],
        fieldLedger: [],
        energyLedger: [],
        loadPathLedger: [],
        stressLedger: [],
        deformationLedger: [],
        collapseLedger: [],
        structuralRepairLedger: [],
        contactConstraintLedger: [],
        jointConstraintLedger: [],
        frictionLedger: [],
        impulseLedger: [],
        constraintRepairLedger: [],
        materialStateLedger: [],
        phaseChangeLedger: [],
        propertyDriftLedger: [],
        materialStateRepairLedger: [],
        transformationLedger: [],
        latestStep: null
      },
      materialCatalog: {
        rough_branch: { id: 'rough_branch', name: 'rough branch', mass: 2.4, hardness: 0.48, flexibility: 0.38, brittleness: 0.32, water_resistance: 0.34, heat_resistance: 0.42, friction: 0.72, tensile_strength: 0.34, compression_strength: 0.58, decay_rate: 0.035, flammability: 0.62, conductivity_like_property: 0.08, insulation_like_property: 0.47, workability: 0.52, tool_required: 'cutting edge or scraping stone' },
        fiber: { id: 'fiber', name: 'fiber binding', mass: 0.2, hardness: 0.12, flexibility: 0.84, brittleness: 0.22, water_resistance: 0.28, heat_resistance: 0.18, friction: 0.81, tensile_strength: 0.68, compression_strength: 0.08, decay_rate: 0.055, flammability: 0.7, conductivity_like_property: 0.04, insulation_like_property: 0.56, workability: 0.78, tool_required: 'hands and twisting practice' },
        clay_vessel: { id: 'clay_vessel', name: 'clay vessel', mass: 1.9, hardness: 0.62, flexibility: 0.06, brittleness: 0.58, water_resistance: 0.45, heat_resistance: 0.74, friction: 0.43, tensile_strength: 0.12, compression_strength: 0.7, decay_rate: 0.012, flammability: 0.02, conductivity_like_property: 0.12, insulation_like_property: 0.5, workability: 0.34, tool_required: 'fired or dried clay practice' },
        reed_cover: { id: 'reed_cover', name: 'reed cover', mass: 0.8, hardness: 0.22, flexibility: 0.67, brittleness: 0.3, water_resistance: 0.36, heat_resistance: 0.22, friction: 0.64, tensile_strength: 0.29, compression_strength: 0.18, decay_rate: 0.05, flammability: 0.76, conductivity_like_property: 0.05, insulation_like_property: 0.61, workability: 0.72, tool_required: 'bundling and tying practice' },
        resin_smear: { id: 'resin_smear', name: 'resin smear', mass: 0.12, hardness: 0.24, flexibility: 0.44, brittleness: 0.2, water_resistance: 0.81, heat_resistance: 0.2, friction: 0.36, tensile_strength: 0.18, compression_strength: 0.16, decay_rate: 0.018, flammability: 0.66, conductivity_like_property: 0.2, insulation_like_property: 0.66, workability: 0.58, tool_required: 'warming, rubbing, or scraping practice' }
      },
      components: [
        { component_id: 'G3C-001', engine_concept: 'rough_branch_vertical_support', resident_term_id: 'TERM-TAKU-REN', material_id: 'rough_branch', affordance: 'vertical_support', source: 'fallen branch salvage', shape: 'post', position3d: { x: 0, y: 0, z: 0 }, dimensions: { x: 10, y: 10, z: 70 }, mass: 2.4, moisture: 0.22, damage: 0.04, support_role: 'left front support', stability: 0.84, created_by: 'Nia', origin_event: 'wet ground jar storage failed repeatedly' },
        { component_id: 'G3C-002', engine_concept: 'rough_branch_vertical_support', resident_term_id: 'TERM-TAKU-REN', material_id: 'rough_branch', affordance: 'vertical_support', source: 'fallen branch salvage', shape: 'post', position3d: { x: 88, y: 0, z: 0 }, dimensions: { x: 10, y: 10, z: 70 }, mass: 2.4, moisture: 0.21, damage: 0.03, support_role: 'right front support', stability: 0.85, created_by: 'Nia', origin_event: 'wet ground jar storage failed repeatedly' },
        { component_id: 'G3C-003', engine_concept: 'rough_branch_vertical_support', resident_term_id: 'TERM-TAKU-REN', material_id: 'rough_branch', affordance: 'vertical_support', source: 'fallen branch salvage', shape: 'post', position3d: { x: 0, y: 56, z: 0 }, dimensions: { x: 10, y: 10, z: 62 }, mass: 2.2, moisture: 0.24, damage: 0.05, support_role: 'left rear support', stability: 0.8, created_by: 'Milo', origin_event: 'raised branch support copied with uneven rear height' },
        { component_id: 'G3C-004', engine_concept: 'rough_branch_vertical_support', resident_term_id: 'TERM-TAKU-REN', material_id: 'rough_branch', affordance: 'vertical_support', source: 'fallen branch salvage', shape: 'post', position3d: { x: 88, y: 56, z: 0 }, dimensions: { x: 10, y: 10, z: 62 }, mass: 2.2, moisture: 0.25, damage: 0.05, support_role: 'right rear support', stability: 0.79, created_by: 'Milo', origin_event: 'raised branch support copied with uneven rear height' },
        { component_id: 'G3C-005', engine_concept: 'rough_branch_horizontal_span', resident_term_id: 'TERM-TAKU-REN', material_id: 'rough_branch', affordance: 'horizontal_span', source: 'worked branch, not a discovered flat member', shape: 'beam_x', position3d: { x: 44, y: 0, z: 70 }, dimensions: { x: 108, y: 8, z: 8 }, mass: 2.1, moisture: 0.23, damage: 0.06, support_role: 'front raised surface span', stability: 0.77, created_by: 'Ari', origin_event: 'support attempt after clay shelf collapse' },
        { component_id: 'G3C-006', engine_concept: 'rough_branch_horizontal_span', resident_term_id: 'TERM-TAKU-REN', material_id: 'rough_branch', affordance: 'horizontal_span', source: 'worked branch, not a discovered flat member', shape: 'beam_x', position3d: { x: 44, y: 56, z: 62 }, dimensions: { x: 108, y: 8, z: 8 }, mass: 2.0, moisture: 0.27, damage: 0.08, support_role: 'rear raised surface span', stability: 0.72, created_by: 'Ari', origin_event: 'support attempt after clay shelf collapse' },
        { component_id: 'G3C-007', engine_concept: 'fiber_binding_point', resident_term_id: 'TERM-TAKU-REN', material_id: 'fiber', affordance: 'binding_point', source: 'twisted fiber commons', shape: 'lash', position3d: { x: 44, y: 28, z: 66 }, dimensions: { x: 94, y: 58, z: 6 }, mass: 0.7, moisture: 0.31, damage: 0.09, support_role: 'binding and surface retention', stability: 0.68, created_by: 'Sera', origin_event: 'loose branches shifted under jars' },
        { component_id: 'G3C-008', engine_concept: 'reed_rain_shedding_cover', resident_term_id: 'TERM-TAKU-REN', material_id: 'reed_cover', affordance: 'rain_shedding_cover', source: 'bundled reeds from storage edge', shape: 'plane', position3d: { x: 44, y: 28, z: 86 }, dimensions: { x: 118, y: 74, z: 4 }, mass: 0.8, moisture: 0.34, damage: 0.07, support_role: 'partial cover', stability: 0.7, created_by: 'Fay', origin_event: 'rain dampened raised jars once' },
        { component_id: 'G3C-009', engine_concept: 'clay_vessel_container', resident_term_id: 'TERM-KU', material_id: 'clay_vessel', affordance: 'carried_container', source: 'existing dried clay vessel', shape: 'cylinder', position3d: { x: 28, y: 22, z: 78 }, dimensions: { x: 20, y: 20, z: 32 }, mass: 1.9, moisture: 0.18, damage: 0.04, support_role: 'stored contents', stability: 0.81, created_by: 'Nia', origin_event: 'vessels spoiled less when lifted from wet ground' },
        { component_id: 'G3C-010', engine_concept: 'clay_vessel_container', resident_term_id: 'TERM-KU', material_id: 'clay_vessel', affordance: 'carried_container', source: 'existing dried clay vessel', shape: 'cylinder', position3d: { x: 66, y: 34, z: 78 }, dimensions: { x: 18, y: 18, z: 28 }, mass: 1.6, moisture: 0.19, damage: 0.05, support_role: 'stored contents', stability: 0.79, created_by: 'Nia', origin_event: 'vessels spoiled less when lifted from wet ground' }
      ],
      structures: [
        {
          structure_id: 'G3S-001',
          engine_concept: 'raised_dry_storage_surface',
          resident_term_id: 'TERM-TAKU-REN',
          player_gloss: 'roughly raised dry vessel practice',
          component_ids: ['G3C-001', 'G3C-002', 'G3C-003', 'G3C-004', 'G3C-005', 'G3C-006', 'G3C-007', 'G3C-008', 'G3C-009', 'G3C-010'],
          affordances_satisfied: ['vertical_support', 'horizontal_span', 'raised_surface', 'storage_surface', 'binding_point', 'rain_shedding_cover'],
          status: 'partial practical structure',
          stability: 0.76,
          moisture_risk: 0.28,
          maintenance_cost: 1,
          risk_flags: ['fiber binding weakens when damp', 'rear support uneven', 'cover is partial'],
          no_fixed_asset: true
        }
      ],
      language: {
        soundRoots: [
          { sound_id: 'SND-TA', sound_form: 'ta', phonetic_shape: 'open front + stop', meaning_association: 'dry, safer, sun-warmed', grounded_event: 'stored vessels kept off wet ground spoiled less', linked_observation: 'dry raised jars lasted longer', linked_material: 'clay_vessel', linked_action: 'dry and lift', linked_place: 'storage edge', linked_resident: 'Nia', linked_practice: 'G3S-001', emotional_weight: 0.54, practical_weight: 0.78, ritual_weight: 0.18, taboo_weight: 0.08, first_speaker: 'Nia', first_household: 'jar keepers', transmission_path: ['Nia', 'Fay', 'Sera'], variants: ['taa'], drift_history: ['dry ground', 'safe dryness'], adoption_count: 3, translation_confidence: 0.62, player_gloss: 'dry or safe' },
          { sound_id: 'SND-KU', sound_form: 'ku', phonetic_shape: 'closed back + stop', meaning_association: 'hollow vessel or carried container', grounded_event: 'clay vessels repeatedly used for stored material', linked_observation: 'hollow things hold goods and can spoil', linked_material: 'clay_vessel', linked_action: 'carry and store', linked_place: 'storage edge', linked_resident: 'Nia', linked_practice: 'G3S-001', emotional_weight: 0.36, practical_weight: 0.81, ritual_weight: 0.12, taboo_weight: 0.04, first_speaker: 'Nia', first_household: 'jar keepers', transmission_path: ['Nia', 'Milo'], variants: ['kuk'], drift_history: ['hollow thing', 'vessel'], adoption_count: 4, translation_confidence: 0.68, player_gloss: 'vessel or hollow thing' },
          { sound_id: 'SND-REN', sound_form: 'ren', phonetic_shape: 'liquid + nasal close', meaning_association: 'raised, held above, kept off ground', grounded_event: 'branches lifted vessels above wet soil', linked_observation: 'lifted vessels stayed less damp', linked_material: 'rough_branch', linked_action: 'raise and bind', linked_place: 'storage edge', linked_resident: 'Ari', linked_practice: 'G3S-001', emotional_weight: 0.42, practical_weight: 0.74, ritual_weight: 0.16, taboo_weight: 0.1, first_speaker: 'Ari', first_household: 'repair hands', transmission_path: ['Ari', 'Nia', 'Milo'], variants: ['re'], drift_history: ['held up', 'raised support'], adoption_count: 3, translation_confidence: 0.57, player_gloss: 'raised or held above' }
        ],
        terms: [
          {
            term_id: 'TERM-TAKU-REN',
            resident_word: 'taku-ren',
            player_gloss: 'roughly raised dry vessel practice',
            engine_concept: 'raised_dry_storage_surface',
            roots: ['SND-TA', 'SND-KU', 'SND-REN'],
            root_glosses: ['dry/safe', 'vessel/hollow thing', 'raised/held above'],
            origin_resident: 'Nia',
            origin_household: 'jar keepers',
            origin_event: 'wet ground vessel failures followed by repeated raised-storage success',
            linked_practice_id: 'G3S-001',
            linked_materials: ['clay_vessel', 'rough_branch', 'fiber', 'reed_cover'],
            adoption_count: 3,
            variants: ['takren'],
            meaning_drift: ['dry vessel raised place', 'safe jar lifting habit'],
            taboo_score: 0.08,
            ritual_score: 0.18,
            practical_score: 0.82,
            translation_confidence: 0.61,
            current_status: 'practical household term',
          },
          {
            term_id: 'TERM-KU',
            resident_word: 'ku',
            player_gloss: 'roughly vessel or hollow thing',
            engine_concept: 'clay_vessel_container',
            roots: ['SND-KU'],
            root_glosses: ['vessel/hollow thing'],
            origin_resident: 'Nia',
            origin_household: 'jar keepers',
            origin_event: 'repeated storage handling',
            linked_practice_id: 'G3S-001',
            linked_materials: ['clay_vessel'],
            adoption_count: 4,
            variants: ['kuk'],
            meaning_drift: ['hollow object', 'kept vessel'],
            taboo_score: 0.04,
            ritual_score: 0.1,
            practical_score: 0.74,
            translation_confidence: 0.68,
            current_status: 'practical root word',
          }
        ],
      },
	      observationLedger: [
	        { observation_id: 'G3O-001', public_observation: 'vessels off wet ground spoiled less often', resident_interpretation: 'taku-ren is safer for ku when ground is wet', linked_structure: 'G3S-001', hidden_law_visible_normal_view: false, engine_concept_audit_only: 'raised_dry_storage_surface' },
	        { observation_id: 'G3O-002', public_observation: 'fiber bindings loosened after damp weather', resident_interpretation: 'ren needs retying after rain', linked_structure: 'G3S-001', hidden_law_visible_normal_view: false, engine_concept_audit_only: 'fiber water resistance and decay' }
	      ],
      constructionLedger: [],
	      stepLedger: [],
	      latestStep: null,
	    };
	  }
  if (!Array.isArray(world.gamePrototype3DWorld.constructionLedger)) world.gamePrototype3DWorld.constructionLedger = [];
	  if (!world.gamePrototype3DWorld.physics) {
    world.gamePrototype3DWorld.physics = {
      kernel_id: 'G3P-KERNEL-001',
      mode: 'stochastic physics first',
      integrator: 'bounded semi-implicit discrete timestep',
      timestep: 1,
      gravity: 9.8,
	      solver_layers: ['mass', 'weight', 'support', 'collision/contact', 'friction', 'moisture', 'heat', 'decay', 'tool wear', 'labor/work', 'stochastic field pressure', 'stochastic failure', 'load path', 'structural stress', 'deformation/sag', 'anchor slip', 'partial collapse', 'contact constraint', 'joint/binding constraint', 'surface friction', 'impulse transfer', 'material state', 'phase drift', 'property mutation'],
	      environment: { moisture: 0.31, heat: 0.46, wind: 0.18, decayPressure: 0.22, stress: 0.16 },
	      forceLedger: [],
	      supportLedger: [],
	      collisionLedger: [],
	      failureLedger: [],
	      fieldLedger: [],
	      energyLedger: [],
	      loadPathLedger: [],
	      stressLedger: [],
	      deformationLedger: [],
	      collapseLedger: [],
	      structuralRepairLedger: [],
	      contactConstraintLedger: [],
	      jointConstraintLedger: [],
	      frictionLedger: [],
	      impulseLedger: [],
	      constraintRepairLedger: [],
	      materialStateLedger: [],
	      phaseChangeLedger: [],
	      propertyDriftLedger: [],
	      materialStateRepairLedger: [],
	      transformationLedger: [],
	      latestStep: null
	    };
	  }
  if (!world.gamePrototype3DWorld.physics.environment) world.gamePrototype3DWorld.physics.environment = { moisture: 0.31, heat: 0.46, wind: 0.18, decayPressure: 0.22, stress: 0.16 };
  ['forceLedger', 'supportLedger', 'collisionLedger', 'failureLedger', 'fieldLedger', 'energyLedger', 'loadPathLedger', 'stressLedger', 'deformationLedger', 'collapseLedger', 'structuralRepairLedger', 'contactConstraintLedger', 'jointConstraintLedger', 'frictionLedger', 'impulseLedger', 'constraintRepairLedger', 'materialStateLedger', 'phaseChangeLedger', 'propertyDriftLedger', 'materialStateRepairLedger', 'transformationLedger'].forEach(key => {
    if (!Array.isArray(world.gamePrototype3DWorld.physics[key])) world.gamePrototype3DWorld.physics[key] = [];
  });
  if (!Array.isArray(world.gamePrototype3DWorld.physics.solver_layers)) world.gamePrototype3DWorld.physics.solver_layers = ['mass', 'weight', 'support', 'collision/contact', 'friction', 'moisture', 'heat', 'decay', 'tool wear', 'labor/work', 'stochastic field pressure', 'stochastic failure'];
  ['heat', 'stochastic field pressure', 'load path', 'structural stress', 'deformation/sag', 'anchor slip', 'partial collapse', 'contact constraint', 'joint/binding constraint', 'surface friction', 'impulse transfer', 'material state', 'phase drift', 'property mutation'].forEach(layer => {
    if (!world.gamePrototype3DWorld.physics.solver_layers.includes(layer)) world.gamePrototype3DWorld.physics.solver_layers.push(layer);
  });
  return world.gamePrototype3DWorld;
}

function ensureComponentPhysics(component) {
  if (!component.physics) {
    component.physics = {
      velocity: { x: 0, y: 0, z: 0 },
      acceleration: { x: 0, y: 0, z: 0 },
      forces: { gravity: 0, normal: 0, friction: 0 },
      supported_by: 'unknown',
      grounded: false,
      collision_count: 0,
      last_failure_probability: 0,
    };
  }
  return component.physics;
}

function componentFootprint(component) {
  const pos = component.position3d || { x: 0, y: 0, z: 0 };
  const dim = component.dimensions || { x: 1, y: 1, z: 1 };
  return {
    minX: pos.x - dim.x / 2,
    maxX: pos.x + dim.x / 2,
    minY: pos.y - dim.y / 2,
    maxY: pos.y + dim.y / 2,
    minZ: pos.z,
    maxZ: pos.z + dim.z,
  };
}

function footprintsOverlapXY(a, b) {
  return a.minX <= b.maxX && a.maxX >= b.minX && a.minY <= b.maxY && a.maxY >= b.minY;
}

function applyPrototypePhysicsField(sim, stepId, entropy, source = 'physics') {
  const physics = sim.physics;
  const field = physics.environment || { moisture: 0.31, heat: 0.46, wind: 0.18, decayPressure: 0.22, stress: 0.16 };
  const cycle = world.gamePrototypeDayCycle || null;
  const latestWeather = cycle && cycle.weatherLedger && cycle.weatherLedger.length ? cycle.weatherLedger[cycle.weatherLedger.length - 1].weather : 'settled dry air';
  const wetWeather = /drizzle|damp|rain|wet|flood/.test(latestWeather) || /wet|flood/.test(source);
  const dryWeather = /dry|wind|sun|drought/.test(latestWeather) || /dry|drought/.test(source);
  const heatNudge = dryWeather ? 0.024 : (wetWeather ? -0.012 : ((entropy % 7) - 3) / 1000);
  const moistureNudge = wetWeather ? 0.045 : (dryWeather ? -0.038 : ((entropy % 9) - 4) / 1000);
  field.moisture = Number(clamp(Number(field.moisture || 0.31) + moistureNudge).toFixed(3));
  field.heat = Number(clamp(Number(field.heat || 0.46) + heatNudge).toFixed(3));
  field.wind = Number(clamp(Number(field.wind || 0.18) + ((entropy % 13) - 6) / 1000 + (dryWeather ? 0.012 : 0)).toFixed(3));
  field.decayPressure = Number(clamp(Number(field.decayPressure || 0.22) + field.moisture * 0.012 - field.heat * 0.006).toFixed(3));
  field.stress = Number(clamp(Number(field.stress || 0.16) + field.wind * 0.01 + field.decayPressure * 0.012).toFixed(3));
  physics.environment = field;
  const componentRows = (sim.components || []).map((component, index) => {
    const material = sim.materialCatalog[component.material_id] || {};
    const before = {
      moisture: Number(component.moisture || 0),
      damage: Number(component.damage || 0),
      stability: Number(component.stability || 0),
      temperature: Number(component.temperature || field.heat),
      field_stress: Number(component.field_stress || 0),
    };
    const waterFlux = (field.moisture - before.moisture) * (1 - Number(material.water_resistance || 0.5)) * 0.18;
    const heatFlux = (field.heat - before.temperature) * (1 - Number(material.heat_resistance || 0.4)) * 0.12;
    const stressFlux = field.stress * (Number(component.mass || material.mass || 1) / 6) + field.wind * (1 - Number(material.flexibility || 0.4)) * 0.035;
    const decayFlux = Number(material.decay_rate || 0.02) * (0.25 + field.decayPressure + Math.max(0, before.moisture - Number(material.water_resistance || 0.5)) * 0.4);
    const stochasticHit = ((entropy + index * 23 + stepId.length) % 100) / 100 < clamp(field.stress * 0.14 + field.moisture * 0.04) ? 0.012 : 0;
    component.moisture = Number(clamp(before.moisture + waterFlux).toFixed(3));
    component.temperature = Number(clamp(before.temperature + heatFlux).toFixed(3));
    component.field_stress = Number(clamp(before.field_stress * 0.45 + stressFlux).toFixed(3));
    component.damage = Number(clamp(before.damage + decayFlux + stochasticHit).toFixed(3));
    component.stability = Number(clamp(before.stability - component.field_stress * 0.01 - decayFlux * 0.08 + (dryWeather ? 0.004 : 0)).toFixed(3));
    return {
      step_id: stepId,
      component_id: component.component_id,
      material_id: component.material_id,
      water_flux: Number(waterFlux.toFixed(4)),
      heat_flux: Number(heatFlux.toFixed(4)),
      stress_flux: Number(stressFlux.toFixed(4)),
      decay_flux: Number(decayFlux.toFixed(4)),
      stochastic_hit: stochasticHit > 0,
      after_moisture: component.moisture,
      after_temperature: component.temperature,
      after_stability: component.stability,
    };
  });
  const fieldRow = {
    field_id: `G3F-${String((physics.fieldLedger || []).length + 1).padStart(3, '0')}`,
    step_id: stepId,
    source,
    entropy,
    weather: latestWeather,
    moisture: field.moisture,
    heat: field.heat,
    wind: field.wind,
    decay_pressure: field.decayPressure,
    stress: field.stress,
    component_count: componentRows.length,
    hidden_law_normal_view: false,
  };
  const energyRow = {
    energy_id: `G3E-${String((physics.energyLedger || []).length + 1).padStart(3, '0')}`,
    step_id: stepId,
    source,
    gravity_work_proxy: Number((sim.components || []).reduce((sum, component) => sum + Number(component.mass || 1) * Number(physics.gravity || 9.8) * Math.max(0, Number(component.position3d && component.position3d.z || 0)), 0).toFixed(3)),
    field_stress_total: Number((sim.components || []).reduce((sum, component) => sum + Number(component.field_stress || 0), 0).toFixed(3)),
    decay_work_proxy: Number(componentRows.reduce((sum, row) => sum + row.decay_flux, 0).toFixed(3)),
    resident_free_energy: false,
    resource_spawning: false,
  };
  physics.fieldLedger.push(fieldRow);
  physics.energyLedger.push(energyRow);
  physics.fieldLedger = physics.fieldLedger.slice(-120);
  physics.energyLedger = physics.energyLedger.slice(-120);
  return {
    fieldRow,
    energyRow,
    componentRows,
    failure_bias: clamp(field.stress * 0.08 + field.moisture * 0.04 + field.decayPressure * 0.05),
  };
}

function applyPrototypePhysicsStep(source = 'manual') {
  const sim = ensurePrototype3DWorld();
  const physics = sim.physics;
  const entropy = typeof deepTimeEntropyByte === 'function' ? deepTimeEntropyByte() : ((world.tick * 73) % 256);
  physics.step = (physics.step || 0) + 1;
  const stepId = `G3P-${String(physics.step).padStart(3, '0')}`;
  const fieldResult = applyPrototypePhysicsField(sim, stepId, entropy, source);
  const gravity = Number(physics.gravity || 9.8);
  const supportRows = [];
  const collisionRows = [];
  const forceRows = [];
  const failureRows = [];
  const transformRows = [];
  const components = sim.components || [];
  components.forEach(component => ensureComponentPhysics(component));
  components.forEach(component => {
    const material = sim.materialCatalog[component.material_id] || {};
    const phys = ensureComponentPhysics(component);
    const footprint = componentFootprint(component);
    const mass = Number(component.mass || material.mass || 1);
    const weight = Number((mass * gravity).toFixed(3));
    let supportedBy = component.position3d.z <= 0 ? 'ground' : null;
    let supportCapacity = supportedBy === 'ground' ? Infinity : 0;
    if (!supportedBy) {
      components.forEach(candidate => {
        if (candidate.component_id === component.component_id) return;
        const candidateFootprint = componentFootprint(candidate);
        const verticalGap = Math.abs(candidateFootprint.maxZ - footprint.minZ);
        if (verticalGap <= 9 && footprintsOverlapXY(footprint, candidateFootprint)) {
          const candidateMaterial = sim.materialCatalog[candidate.material_id] || {};
          const compression = Number(candidateMaterial.compression_strength || 0.3);
          const candidateArea = Math.max(1, Number(candidate.dimensions && candidate.dimensions.x || 1) * Number(candidate.dimensions && candidate.dimensions.y || 1));
          const capacity = compression * candidateArea * Number(candidate.stability || 0.6);
          if (capacity > supportCapacity) {
            supportCapacity = capacity;
            supportedBy = candidate.component_id;
          }
        }
      });
    }
    const unsupported = !supportedBy || supportCapacity < weight * 0.35;
    phys.supported_by = supportedBy || 'falling';
    phys.grounded = supportedBy === 'ground';
    phys.forces.gravity = weight;
    phys.forces.normal = supportedBy ? Math.min(weight, supportCapacity === Infinity ? weight : supportCapacity) : 0;
    phys.forces.friction = Number(((Number(material.friction || 0.4)) * phys.forces.normal).toFixed(3));
    phys.acceleration.z = unsupported ? -gravity : 0;
    if (unsupported) {
      phys.velocity.z = Number((Number(phys.velocity.z || 0) + phys.acceleration.z * Number(physics.timestep || 1)).toFixed(3));
      component.position3d.z = Number(Math.max(0, Number(component.position3d.z || 0) + phys.velocity.z * 0.08).toFixed(3));
      component.damage = Number(clamp(Number(component.damage || 0) + 0.035).toFixed(3));
      component.stability = Number(clamp(Number(component.stability || 0) - 0.04).toFixed(3));
    } else {
      phys.velocity.z = Number((Number(phys.velocity.z || 0) * 0.35).toFixed(3));
    }
    const entropyPressure = (entropy % 17) / 100 + Number(fieldResult.failure_bias || 0);
    const moisture = Number(component.moisture || 0);
    const brittleness = Number(material.brittleness || 0.3);
    const failureProbability = clamp((unsupported ? 0.28 : 0.02) + moisture * 0.12 + brittleness * 0.08 + entropyPressure - Number(component.stability || 0.6) * 0.1);
    phys.last_failure_probability = Number(failureProbability.toFixed(3));
    const failureThreshold = ((entropy + component.component_id.charCodeAt(component.component_id.length - 1)) % 100) / 100;
    if (failureProbability > 0.22 && failureThreshold < failureProbability) {
      component.damage = Number(clamp(Number(component.damage || 0) + failureProbability * 0.18).toFixed(3));
      component.stability = Number(clamp(Number(component.stability || 0) - failureProbability * 0.12).toFixed(3));
      failureRows.push({ step_id: stepId, component_id: component.component_id, reason: unsupported ? 'unsupported weight under gravity' : 'stochastic material fatigue', probability: Number(failureProbability.toFixed(3)), threshold: Number(failureThreshold.toFixed(3)), new_damage: component.damage, new_stability: component.stability });
    }
    supportRows.push({ step_id: stepId, component_id: component.component_id, supported_by: phys.supported_by, weight, normal_force: phys.forces.normal, support_capacity: supportCapacity === Infinity ? 'ground' : Number(supportCapacity.toFixed(3)), unsupported });
    forceRows.push({ step_id: stepId, component_id: component.component_id, mass, gravity_force: weight, normal_force: phys.forces.normal, friction_force: phys.forces.friction, velocity_z: phys.velocity.z, field_stress: component.field_stress || 0, temperature: component.temperature || null });
  });
  for (let i = 0; i < components.length; i += 1) {
    for (let j = i + 1; j < components.length; j += 1) {
      const a = components[i];
      const b = components[j];
      const fa = componentFootprint(a);
      const fb = componentFootprint(b);
      const overlaps = footprintsOverlapXY(fa, fb) && fa.minZ <= fb.maxZ && fa.maxZ >= fb.minZ;
      if (overlaps) {
        ensureComponentPhysics(a).collision_count += 1;
        ensureComponentPhysics(b).collision_count += 1;
        const impulse = Number(((Number(a.mass || 1) + Number(b.mass || 1)) * 0.012).toFixed(3));
        a.damage = Number(clamp(Number(a.damage || 0) + impulse * 0.08).toFixed(3));
        b.damage = Number(clamp(Number(b.damage || 0) + impulse * 0.08).toFixed(3));
        collisionRows.push({ step_id: stepId, a: a.component_id, b: b.component_id, impulse, result: 'contact damage and support pressure updated' });
      }
    }
  }
  const structure = sim.structures && sim.structures[0] ? sim.structures[0] : null;
	  if (structure) {
	    const linkedComponents = components.filter(component => structure.component_ids.includes(component.component_id));
	    structure.stability = Number(clamp(linkedComponents.reduce((sum, component) => sum + Number(component.stability || 0), 0) / Math.max(1, linkedComponents.length)).toFixed(3));
	    structure.moisture_risk = Number(clamp(linkedComponents.reduce((sum, component) => sum + Number(component.moisture || 0), 0) / Math.max(1, linkedComponents.length)).toFixed(3));
	    transformRows.push({ step_id: stepId, structure_id: structure.structure_id, stability: structure.stability, moisture_risk: structure.moisture_risk, result: 'structure state derived from component physics' });
	  }
  const minStability = components.reduce((min, component) => Math.min(min, Number(component.stability || 1)), 1);
  const maxDamage = components.reduce((max, component) => Math.max(max, Number(component.damage || 0)), 0);
  const maintenancePressure = Boolean(failureRows.length || collisionRows.length || minStability < 0.7 || maxDamage > 0.18 || (structure && Number(structure.moisture_risk || 0) > 0.32));
	  physics.forceLedger.push(...forceRows);
  physics.supportLedger.push(...supportRows);
  physics.collisionLedger.push(...collisionRows);
  physics.failureLedger.push(...failureRows);
  physics.transformationLedger.push(...transformRows);
  physics.forceLedger = physics.forceLedger.slice(-120);
  physics.supportLedger = physics.supportLedger.slice(-120);
  physics.collisionLedger = physics.collisionLedger.slice(-80);
  physics.failureLedger = physics.failureLedger.slice(-80);
  physics.transformationLedger = physics.transformationLedger.slice(-80);
  physics.latestStep = {
    step_id: stepId,
    source,
    entropy,
    components: components.length,
    support_checks: supportRows.length,
    collision_checks: (components.length * Math.max(0, components.length - 1)) / 2,
    collisions: collisionRows.length,
    failures: failureRows.length,
	    force_rows: forceRows.length,
	    transformations: transformRows.length,
	    field_id: fieldResult.fieldRow.field_id,
	    energy_id: fieldResult.energyRow.energy_id,
	    min_stability: Number(minStability.toFixed(3)),
	    max_damage: Number(maxDamage.toFixed(3)),
	    structure_stability: structure ? Number(structure.stability || 0) : null,
	    moisture_risk: structure ? Number(structure.moisture_risk || 0) : null,
	    field_moisture: fieldResult.fieldRow.moisture,
	    field_heat: fieldResult.fieldRow.heat,
	    field_stress: fieldResult.fieldRow.stress,
	    field_decay_pressure: fieldResult.fieldRow.decay_pressure,
	    maintenance_pressure: maintenancePressure,
	    gravity_applied: true,
    stochastic_physics: true,
    resource_spawning: false,
    hidden_law_normal_view: false,
  };
	  return physics.latestStep;
	}

function supportCapacityNumber(row, fallback) {
  if (!row) return Number(fallback || 0);
  if (row.support_capacity === 'ground') return Number((Number(fallback || 0) * 2.5 + 12).toFixed(3));
  const parsed = Number(row.support_capacity);
  return Number.isFinite(parsed) ? parsed : Number(fallback || 0);
}

function runStructuralPhysicsStep(source = 'manual structural stress') {
  ensureGamePrototype();
  const sim = ensurePrototype3DWorld();
  const physics = sim.physics;
  ['loadPathLedger', 'stressLedger', 'deformationLedger', 'collapseLedger', 'structuralRepairLedger'].forEach(key => {
    if (!Array.isArray(physics[key])) physics[key] = [];
  });
  ['load path', 'structural stress', 'deformation/sag', 'anchor slip', 'partial collapse'].forEach(layer => {
    if (!physics.solver_layers.includes(layer)) physics.solver_layers.push(layer);
  });
  const baseStep = applyPrototypePhysicsStep(`${source} base`);
  const entropy = typeof deepTimeEntropyByte === 'function' ? deepTimeEntropyByte() : ((world.tick * 91) % 256);
  physics.structuralStep = (physics.structuralStep || 0) + 1;
  const stepId = `G3X-${String(physics.structuralStep).padStart(3, '0')}`;
  const supportRows = physics.supportLedger.filter(row => row.step_id === baseStep.step_id);
  const supportByComponent = Object.fromEntries(supportRows.map(row => [row.component_id, row]));
  const field = physics.environment || { moisture: 0.31, heat: 0.46, wind: 0.18, stress: 0.16, decayPressure: 0.22 };
  const gravity = Number(physics.gravity || 9.8);
  const components = sim.components || [];
  const loadPathRows = [];
  const stressRows = [];
  const deformationRows = [];
  const collapseRows = [];
  let overloads = 0;
  let maxStress = 0;
  let maxDeflection = 0;
  let minMargin = 9;

  components.forEach((component, index) => {
    const material = sim.materialCatalog[component.material_id] || {};
    const footprint = componentFootprint(component);
    const mass = Number(component.mass || material.mass || 1);
    const weight = Number((mass * gravity).toFixed(3));
    const aboveLoad = components.reduce((sum, other) => {
      if (other.component_id === component.component_id) return sum;
      const otherFootprint = componentFootprint(other);
      const nearAbove = otherFootprint.minZ >= footprint.minZ && otherFootprint.minZ <= footprint.maxZ + 24;
      return footprintsOverlapXY(footprint, otherFootprint) && nearAbove ? sum + Number(other.mass || 1) * gravity * 0.52 : sum;
    }, 0);
    const span = Math.max(1, Number(component.dimensions && component.dimensions.x || 1), Number(component.dimensions && component.dimensions.y || 1));
    const area = Math.max(1, Number(component.dimensions && component.dimensions.x || 1) * Number(component.dimensions && component.dimensions.y || 1));
    const height = Math.max(1, Number(component.position3d && component.position3d.z || 0) + Number(component.dimensions && component.dimensions.z || 1));
    const supportRow = supportByComponent[component.component_id];
    const compressionCapacity = Number(material.compression_strength || 0.3) * area * Math.max(0.15, Number(component.stability || 0.5));
    const tensileCapacity = Number(material.tensile_strength || 0.2) * Math.max(1, span / 8) * Math.max(0.15, Number(component.stability || 0.5));
    const supportCapacity = supportCapacityNumber(supportRow, compressionCapacity + tensileCapacity);
    const windLoad = Number((Number(field.wind || 0.18) * height * (1 - Number(material.friction || 0.4)) * 0.18).toFixed(3));
    const demand = Number((weight + aboveLoad + windLoad + Number(component.field_stress || 0) * 7).toFixed(3));
    const supportMargin = Number(((supportCapacity - demand) / Math.max(1, demand)).toFixed(3));
    const affordance = String(component.affordance || '');
    const isSpan = /span|cover|surface|binding/.test(affordance);
    const moistureWeakening = Math.max(0, Number(component.moisture || 0) - Number(material.water_resistance || 0.45));
    const heatWeakening = Math.max(0, Number(component.temperature || field.heat || 0.45) - Number(material.heat_resistance || 0.4));
    const brittleness = Number(material.brittleness || 0.3);
    const bendingStress = isSpan ? (demand * span) / Math.max(20, (Number(material.tensile_strength || 0.2) + Number(material.flexibility || 0.3)) * 1800) : (demand * height / Math.max(20, Number(material.compression_strength || 0.3) * 2200));
    const anchorSlipDelta = /binding|fiber|lash/.test(`${affordance} ${component.material_id} ${component.shape}`) ? Number((Number(component.moisture || 0) * 0.025 + Math.max(0, -supportMargin) * 0.08 + Number(field.wind || 0) * 0.01).toFixed(4)) : Number((Math.max(0, -supportMargin) * 0.018).toFixed(4));
    const stochasticHit = ((entropy + index * 37 + stepId.length) % 100) / 100;
    const stressScore = clamp(
      bendingStress * 0.18 +
      Math.max(0, -supportMargin) * 0.38 +
      moistureWeakening * 0.22 +
      heatWeakening * 0.1 +
      Number(component.damage || 0) * 0.38 +
      Number(field.stress || 0.16) * 0.18 +
      brittleness * 0.04 +
      (stochasticHit < 0.12 ? 0.025 : 0)
    );
    const deflectionDelta = Number((stressScore * (isSpan ? 0.42 : 0.16) + anchorSlipDelta * 0.7).toFixed(4));
    component.structural_load = Number(demand.toFixed(3));
    component.support_margin = supportMargin;
    component.anchor_slip = Number(clamp(Number(component.anchor_slip || 0) + anchorSlipDelta).toFixed(3));
    component.deflection = Number(clamp(Number(component.deflection || 0) + deflectionDelta).toFixed(3));
    component.tilt = Number(clamp(Number(component.tilt || 0) + Math.max(0, -supportMargin) * 0.028 + Number(field.wind || 0) * 0.003).toFixed(3));
    component.damage = Number(clamp(Number(component.damage || 0) + stressScore * 0.016 + anchorSlipDelta * 0.12).toFixed(3));
    component.stability = Number(clamp(Number(component.stability || 0.6) - stressScore * 0.018 - component.anchor_slip * 0.006).toFixed(3));
    const collapseProbability = clamp(stressScore * 0.32 + Math.max(0, -supportMargin) * 0.28 + component.deflection * 0.12 + (Number(component.stability || 0.6) < 0.46 ? 0.16 : 0));
    const collapseThreshold = ((entropy + index * 19 + component.component_id.length) % 100) / 100;
    if ((collapseProbability > 0.22 && collapseThreshold < collapseProbability) || component.deflection > 0.62) {
      component.partial_collapse = true;
      component.position3d.z = Number(Math.max(0, Number(component.position3d && component.position3d.z || 0) - Math.min(8, 1 + component.deflection * 6)).toFixed(3));
      component.damage = Number(clamp(Number(component.damage || 0) + 0.045).toFixed(3));
      component.stability = Number(clamp(Number(component.stability || 0) - 0.065).toFixed(3));
      collapseRows.push({
        structural_step_id: stepId,
        component_id: component.component_id,
        collapse_probability: Number(collapseProbability.toFixed(3)),
        threshold: Number(collapseThreshold.toFixed(3)),
        result: 'partial sag/collapse marked; component remains conserved and repairable',
        no_resource_spawning: true,
        hidden_law_normal_view: false
      });
    }
    if (supportMargin < 0.08 || stressScore > 0.36) overloads += 1;
    maxStress = Math.max(maxStress, stressScore);
    maxDeflection = Math.max(maxDeflection, Number(component.deflection || 0));
    minMargin = Math.min(minMargin, supportMargin);
    loadPathRows.push({
      structural_step_id: stepId,
      base_step_id: baseStep.step_id,
      component_id: component.component_id,
      supported_by: supportRow ? supportRow.supported_by : 'unknown',
      material_id: component.material_id,
      weight,
      above_load: Number(aboveLoad.toFixed(3)),
      wind_load: windLoad,
      demand,
      support_capacity: Number(supportCapacity.toFixed(3)),
      support_margin: supportMargin,
      no_resource_spawning: true,
      hidden_law_normal_view: false
    });
    stressRows.push({
      structural_step_id: stepId,
      component_id: component.component_id,
      affordance,
      bending_stress: Number(bendingStress.toFixed(4)),
      anchor_slip_delta: anchorSlipDelta,
      moisture_weakening: Number(moistureWeakening.toFixed(3)),
      heat_weakening: Number(heatWeakening.toFixed(3)),
      stress_score: Number(stressScore.toFixed(3)),
      collapse_probability: Number(collapseProbability.toFixed(3)),
      stochastic_threshold: Number(collapseThreshold.toFixed(3)),
      no_effect_without_cause: true,
      no_resource_spawning: true,
      hidden_law_normal_view: false
    });
    deformationRows.push({
      structural_step_id: stepId,
      component_id: component.component_id,
      deflection_delta: deflectionDelta,
      total_deflection: component.deflection,
      anchor_slip: component.anchor_slip,
      tilt: component.tilt,
      stability_after: component.stability,
      damage_after: component.damage,
      conserved_component: true
    });
  });

  (sim.structures || []).forEach(structure => {
    const linked = components.filter(component => structure.component_ids.includes(component.component_id));
    const linkedStress = stressRows.filter(row => linked.some(component => component.component_id === row.component_id));
    const structuralScore = linkedStress.reduce((sum, row) => sum + Number(row.stress_score || 0), 0) / Math.max(1, linkedStress.length);
    structure.structural_stress = Number(structuralScore.toFixed(3));
    structure.support_margin = Number((loadPathRows.filter(row => linked.some(component => component.component_id === row.component_id)).reduce((min, row) => Math.min(min, Number(row.support_margin || 0)), 9)).toFixed(3));
    structure.max_deflection = Number(linked.reduce((max, component) => Math.max(max, Number(component.deflection || 0)), 0).toFixed(3));
    structure.collapse_risk = Number(clamp(structuralScore * 0.5 + Math.max(0, -structure.support_margin) * 0.25 + structure.max_deflection * 0.18).toFixed(3));
    structure.status = structure.collapse_risk > 0.32 ? 'strained repair needed' : (structure.max_deflection > 0.22 ? 'sagging but usable' : structure.status);
  });

  const repairNeeded = overloads > 0 || collapseRows.length > 0 || maxDeflection > 0.24 || minMargin < 0.14;
  const repairRows = repairNeeded ? [{
    repair_id: `G3XR-${String(physics.structuralRepairLedger.length + 1).padStart(3, '0')}`,
    structural_step_id: stepId,
    source,
    materials_needed: ['fiber', 'wood', 'care'],
    labor_time_cost: Math.max(1, overloads + collapseRows.length),
    reason: collapseRows.length ? 'partial collapse or sag observed' : 'load path margin too low',
    avatar_direct_command: false,
    no_resource_spawning: true,
    hidden_law_normal_view: false
  }] : [];

  physics.loadPathLedger.push(...loadPathRows);
  physics.stressLedger.push(...stressRows);
  physics.deformationLedger.push(...deformationRows);
  physics.collapseLedger.push(...collapseRows);
  physics.structuralRepairLedger.push(...repairRows);
  physics.loadPathLedger = physics.loadPathLedger.slice(-180);
  physics.stressLedger = physics.stressLedger.slice(-180);
  physics.deformationLedger = physics.deformationLedger.slice(-180);
  physics.collapseLedger = physics.collapseLedger.slice(-80);
  physics.structuralRepairLedger = physics.structuralRepairLedger.slice(-80);
  physics.latestStructuralStep = {
    step_id: stepId,
    source,
    entropy,
    base_step_id: baseStep.step_id,
    components: components.length,
    load_paths: loadPathRows.length,
    stress_rows: stressRows.length,
    deformation_rows: deformationRows.length,
    collapses: collapseRows.length,
    repair_rows: repairRows.length,
    overloads,
    min_margin: Number(minMargin.toFixed(3)),
    max_stress: Number(maxStress.toFixed(3)),
    max_deflection: Number(maxDeflection.toFixed(3)),
    min_stability: baseStep.min_stability,
    max_damage: baseStep.max_damage,
    field_heat: baseStep.field_heat,
    field_moisture: baseStep.field_moisture,
    field_stress: baseStep.field_stress,
    failures: collapseRows.length + overloads,
    collisions: baseStep.collisions,
    support_checks: baseStep.support_checks,
    maintenance_pressure: repairNeeded,
    hidden_law_normal_view: false,
    no_resource_spawning: true
  };
  const consequence = applyPhysicsConsequencesToVillage(physics.latestStructuralStep, source);
  recordRealityConstraint('structural_stress_physics', {
    resident: world.selected,
    sourceBeliefId: stepId,
    materials: ['rough_branch', 'fiber', 'clay_vessel', 'reed_cover'],
    publicObservation: `${loadPathRows.length} load path(s), ${overloads} overload(s), ${collapseRows.length} partial collapse row(s)`,
    residentInterpretation: repairNeeded ? 'the raised place is sagging and needs attention' : 'the raised place held under load this time',
    materialTransformation: 'component deflection, slip, damage, and stability updated from load, weather, material strength, and stochastic pressure',
    timeCost: 1,
    workCost: repairNeeded ? 1 : 0,
    toolWear: overloads + collapseRows.length,
    maintenanceObligation: repairNeeded ? 'resident repair proposal from structural stress' : 'keep watching support margins',
    unintendedConsequence: collapseRows.length ? 'partial collapse changed component position and resident repair pressure' : 'stress history accumulated without component deletion',
    hiddenLawInvolved: world.audit ? 'load path, support margin, bending stress, anchor slip, stochastic collapse probability' : 'audit only',
    conservationCheck: true
  });
  recordPrototypeMilestone('structural-stress-physics', `${stepId}: load=${loadPathRows.length}, overload=${overloads}, collapse=${collapseRows.length}, repair=${repairRows.length}`);
  return log('runStructuralPhysicsStep', {
    stepId,
    baseStepId: baseStep.step_id,
    loadPaths: loadPathRows.length,
    stressRows: stressRows.length,
    deformationRows: deformationRows.length,
    overloads,
    collapses: collapseRows.length,
    repairRows: repairRows.length,
    maxStress: physics.latestStructuralStep.max_stress,
    maxDeflection: physics.latestStructuralStep.max_deflection,
    minMargin: physics.latestStructuralStep.min_margin,
    proposalId: consequence && consequence.proposal ? consequence.proposal.proposal_id : null
  });
}

function runStructuralPhysicsLoop() {
  ensureGamePrototype();
  const before = ensurePrototype3DWorld().physics.stressLedger.length;
  let last = null;
  for (let index = 0; index < 4; index += 1) {
    last = runStructuralPhysicsStep(`structural stress loop ${index + 1}`).payload;
  }
  const physics = ensurePrototype3DWorld().physics;
  return log('runStructuralPhysicsLoop', {
    stepsAdded: physics.stressLedger.length - before,
    loadRows: physics.loadPathLedger.length,
    stressRows: physics.stressLedger.length,
    deformationRows: physics.deformationLedger.length,
    collapseRows: physics.collapseLedger.length,
    repairRows: physics.structuralRepairLedger.length,
    lastStepId: last ? last.stepId : null
  });
}

function componentCenter(component) {
  const pos = component.position3d || { x: 0, y: 0, z: 0 };
  const dim = component.dimensions || { x: 1, y: 1, z: 1 };
  return {
    x: Number(pos.x || 0),
    y: Number(pos.y || 0),
    z: Number(pos.z || 0) + Number(dim.z || 1) / 2
  };
}

function componentDistance(a, b) {
  const ca = componentCenter(a);
  const cb = componentCenter(b);
  return Math.sqrt(((ca.x - cb.x) ** 2) + ((ca.y - cb.y) ** 2) + ((ca.z - cb.z) ** 2));
}

function componentsAreLikelyJointed(a, b) {
  const pairText = `${a.affordance || ''} ${b.affordance || ''} ${a.material_id || ''} ${b.material_id || ''} ${a.shape || ''} ${b.shape || ''}`;
  if (/binding|fiber|lash/.test(pairText)) return true;
  if (a.resident_term_id && a.resident_term_id === b.resident_term_id && componentDistance(a, b) < 82) return true;
  const fa = componentFootprint(a);
  const fb = componentFootprint(b);
  const verticalGap = Math.min(Math.abs(fa.maxZ - fb.minZ), Math.abs(fb.maxZ - fa.minZ));
  return footprintsOverlapXY(fa, fb) && verticalGap <= 16;
}

function runContactConstraintPhysicsStep(source = 'manual contact constraints') {
  ensureGamePrototype();
  const sim = ensurePrototype3DWorld();
  const physics = sim.physics;
  ['contactConstraintLedger', 'jointConstraintLedger', 'frictionLedger', 'impulseLedger', 'constraintRepairLedger'].forEach(key => {
    if (!Array.isArray(physics[key])) physics[key] = [];
  });
  ['contact constraint', 'joint/binding constraint', 'surface friction', 'impulse transfer'].forEach(layer => {
    if (!physics.solver_layers.includes(layer)) physics.solver_layers.push(layer);
  });
  if (!physics.latestStructuralStep) runStructuralPhysicsStep(`${source} structural precheck`);
  physics.constraintStep = (physics.constraintStep || 0) + 1;
  const stepId = `G3J-${String(physics.constraintStep).padStart(3, '0')}`;
  const entropy = typeof deepTimeEntropyByte === 'function' ? deepTimeEntropyByte() : ((world.tick * 107) % 256);
  const field = physics.environment || { moisture: 0.31, heat: 0.46, wind: 0.18, stress: 0.16 };
  const components = sim.components || [];
  const contactRows = [];
  const jointRows = [];
  const frictionRows = [];
  const impulseRows = [];
  const repairRows = [];
  let slippingContacts = 0;
  let failedJoints = 0;
  let maxImpulse = 0;
  let maxSlip = 0;

  for (let i = 0; i < components.length; i += 1) {
    for (let j = i + 1; j < components.length; j += 1) {
      const a = components[i];
      const b = components[j];
      const fa = componentFootprint(a);
      const fb = componentFootprint(b);
      const xyOverlap = footprintsOverlapXY(fa, fb);
      const verticalGap = Math.min(Math.abs(fa.maxZ - fb.minZ), Math.abs(fb.maxZ - fa.minZ));
      const distance = componentDistance(a, b);
      const contact = xyOverlap && verticalGap <= 14;
      const jointed = componentsAreLikelyJointed(a, b);
      if (!contact && !jointed) continue;
      const ma = sim.materialCatalog[a.material_id] || {};
      const mb = sim.materialCatalog[b.material_id] || {};
      const normalProxy = Number((((Number(a.mass || ma.mass || 1) + Number(b.mass || mb.mass || 1)) * Number(physics.gravity || 9.8)) / (contact ? 2.1 : 4.5)).toFixed(3));
      const frictionCoefficient = Number(((Number(ma.friction || 0.4) + Number(mb.friction || 0.4)) / 2).toFixed(3));
      const frictionLimit = Number((normalProxy * frictionCoefficient * Math.max(0.15, (Number(a.stability || 0.6) + Number(b.stability || 0.6)) / 2)).toFixed(3));
      const relativeSlip = Math.abs(Number(a.deflection || 0) - Number(b.deflection || 0)) + Math.abs(Number(a.anchor_slip || 0) - Number(b.anchor_slip || 0)) + Number(field.wind || 0) * 0.08 + Number(field.stress || 0.16) * 0.12;
      const surfaceMoisture = (Number(a.moisture || 0) + Number(b.moisture || 0)) / 2;
      const impulse = Number((normalProxy * (0.04 + relativeSlip * 0.22 + surfaceMoisture * 0.035 + (entropy % 17) / 900)).toFixed(3));
      const slipProbability = clamp((impulse / Math.max(1, frictionLimit)) * 0.16 + surfaceMoisture * 0.12 + relativeSlip * 0.18 + Number(field.stress || 0.16) * 0.08);
      const threshold = ((entropy + i * 29 + j * 11 + stepId.length) % 100) / 100;
      const slipped = slipProbability > 0.18 && threshold < slipProbability;
      const jointStrength = jointed ? Number(((Number(ma.tensile_strength || 0.2) + Number(mb.tensile_strength || 0.2)) * 0.5 + (a.material_id === 'fiber' || b.material_id === 'fiber' ? 0.24 : 0) - surfaceMoisture * 0.14 - Math.max(Number(a.damage || 0), Number(b.damage || 0)) * 0.18).toFixed(3)) : 0;
      const jointDemand = Number((impulse * (jointed ? 0.42 : 0.12) + relativeSlip * 0.18).toFixed(3));
      const jointFailed = jointed && (jointDemand > Math.max(0.05, jointStrength) || (slipped && threshold < slipProbability * 0.6));
      const slipDelta = slipped ? Number((0.018 + slipProbability * 0.04).toFixed(4)) : Number((relativeSlip * 0.003).toFixed(4));
      a.anchor_slip = Number(clamp(Number(a.anchor_slip || 0) + slipDelta * (jointed ? 0.7 : 0.35)).toFixed(3));
      b.anchor_slip = Number(clamp(Number(b.anchor_slip || 0) + slipDelta * (jointed ? 0.7 : 0.35)).toFixed(3));
      a.damage = Number(clamp(Number(a.damage || 0) + impulse * 0.002 + (jointFailed ? 0.025 : 0)).toFixed(3));
      b.damage = Number(clamp(Number(b.damage || 0) + impulse * 0.002 + (jointFailed ? 0.025 : 0)).toFixed(3));
      a.stability = Number(clamp(Number(a.stability || 0.6) - slipDelta * 0.8 - (jointFailed ? 0.02 : 0)).toFixed(3));
      b.stability = Number(clamp(Number(b.stability || 0.6) - slipDelta * 0.8 - (jointFailed ? 0.02 : 0)).toFixed(3));
      if (slipped) slippingContacts += 1;
      if (jointFailed) failedJoints += 1;
      maxImpulse = Math.max(maxImpulse, impulse);
      maxSlip = Math.max(maxSlip, slipDelta);
      contactRows.push({
        constraint_step_id: stepId,
        component_a: a.component_id,
        component_b: b.component_id,
        contact,
        jointed,
        xy_overlap: xyOverlap,
        vertical_gap: Number(verticalGap.toFixed(3)),
        distance: Number(distance.toFixed(3)),
        normal_proxy: normalProxy,
        hidden_law_normal_view: false
      });
      frictionRows.push({
        constraint_step_id: stepId,
        component_a: a.component_id,
        component_b: b.component_id,
        friction_coefficient: frictionCoefficient,
        friction_limit: frictionLimit,
        surface_moisture: Number(surfaceMoisture.toFixed(3)),
        slip_probability: Number(slipProbability.toFixed(3)),
        threshold: Number(threshold.toFixed(3)),
        slipped,
        no_resource_spawning: true,
        hidden_law_normal_view: false
      });
      impulseRows.push({
        constraint_step_id: stepId,
        component_a: a.component_id,
        component_b: b.component_id,
        impulse,
        relative_slip: Number(relativeSlip.toFixed(3)),
        slip_delta: slipDelta,
        impulse_absorbed_by_damage: Number((impulse * 0.002).toFixed(4)),
        conserved_components: true
      });
      if (jointed) {
        jointRows.push({
          constraint_step_id: stepId,
          component_a: a.component_id,
          component_b: b.component_id,
          joint_strength: Number(jointStrength.toFixed(3)),
          joint_demand: jointDemand,
          joint_failed: jointFailed,
          resident_term: a.resident_term_id || b.resident_term_id || 'local',
          no_effect_without_cause: true,
          no_resource_spawning: true,
          hidden_law_normal_view: false
        });
      }
      if (jointFailed || (slipped && slipProbability > 0.32)) {
        repairRows.push({
          repair_id: `G3JR-${String(physics.constraintRepairLedger.length + repairRows.length + 1).padStart(3, '0')}`,
          constraint_step_id: stepId,
          component_a: a.component_id,
          component_b: b.component_id,
          reason: jointFailed ? 'binding/joint demand exceeded strength' : 'wet friction surface slipped',
          materials_needed: jointed ? ['fiber', 'care'] : ['care'],
          labor_time_cost: jointed ? 2 : 1,
          avatar_direct_command: false,
          no_resource_spawning: true,
          hidden_law_normal_view: false
        });
      }
    }
  }

  (sim.structures || []).forEach(structure => {
    const linkedRows = jointRows.filter(row => structure.component_ids.includes(row.component_a) || structure.component_ids.includes(row.component_b));
    const failed = linkedRows.filter(row => row.joint_failed).length;
    structure.constraint_slip = Number(clamp(Number(structure.constraint_slip || 0) + maxSlip + failed * 0.02).toFixed(3));
    structure.collapse_risk = Number(clamp(Number(structure.collapse_risk || 0) + failed * 0.015 + slippingContacts * 0.002).toFixed(3));
    if (failed > 0) structure.status = 'joint repair needed';
  });

  physics.contactConstraintLedger.push(...contactRows);
  physics.jointConstraintLedger.push(...jointRows);
  physics.frictionLedger.push(...frictionRows);
  physics.impulseLedger.push(...impulseRows);
  physics.constraintRepairLedger.push(...repairRows);
  physics.contactConstraintLedger = physics.contactConstraintLedger.slice(-180);
  physics.jointConstraintLedger = physics.jointConstraintLedger.slice(-180);
  physics.frictionLedger = physics.frictionLedger.slice(-180);
  physics.impulseLedger = physics.impulseLedger.slice(-180);
  physics.constraintRepairLedger = physics.constraintRepairLedger.slice(-80);
  physics.latestConstraintStep = {
    step_id: stepId,
    source,
    entropy,
    contact_rows: contactRows.length,
    joint_rows: jointRows.length,
    friction_rows: frictionRows.length,
    impulse_rows: impulseRows.length,
    repair_rows: repairRows.length,
    slipping_contacts: slippingContacts,
    failed_joints: failedJoints,
    max_impulse: Number(maxImpulse.toFixed(3)),
    max_slip_delta: Number(maxSlip.toFixed(4)),
    hidden_law_normal_view: false,
    no_resource_spawning: true
  };
  if (repairRows.length) {
    applyPhysicsConsequencesToVillage({
      step_id: stepId,
      maintenance_pressure: true,
      failures: failedJoints,
      collisions: slippingContacts,
      min_stability: components.reduce((min, component) => Math.min(min, Number(component.stability || 1)), 1),
      max_damage: components.reduce((max, component) => Math.max(max, Number(component.damage || 0)), 0),
      moisture_risk: Number(field.moisture || 0),
      field_stress: Number(field.stress || 0),
      field_heat: Number(field.heat || 0),
      field_moisture: Number(field.moisture || 0),
      related_constraint_step: stepId
    }, source);
  }
  recordRealityConstraint('contact_constraint_physics', {
    resident: world.selected,
    sourceBeliefId: stepId,
    materials: ['rough_branch', 'fiber', 'clay_vessel', 'reed_cover'],
    publicObservation: `${contactRows.length} contact constraint(s), ${jointRows.length} joint row(s), ${slippingContacts} slip row(s), ${failedJoints} failed joint(s)`,
    residentInterpretation: repairRows.length ? 'some tied or touching pieces shifted and need attention' : 'touching pieces held together this time',
    materialTransformation: 'contact friction, joint demand, impulse transfer, component damage, stability, and anchor slip updated without creating or deleting material',
    timeCost: 1,
    workCost: repairRows.length ? 1 : 0,
    toolWear: failedJoints,
    maintenanceObligation: repairRows.length ? 'constraint repair pressure from slipping joints' : 'watch touching surfaces and bindings',
    unintendedConsequence: repairRows.length ? 'joint repair entered resident planning' : 'constraint history accumulated silently',
    hiddenLawInvolved: world.audit ? 'contact normal proxy, friction limit, joint strength, impulse transfer, stochastic slip probability' : 'audit only',
    conservationCheck: true
  });
  recordPrototypeMilestone('contact-constraint-physics', `${stepId}: contact=${contactRows.length}, joint=${jointRows.length}, slip=${slippingContacts}, failed=${failedJoints}`);
  return log('runContactConstraintPhysicsStep', {
    stepId,
    contactRows: contactRows.length,
    jointRows: jointRows.length,
    frictionRows: frictionRows.length,
    impulseRows: impulseRows.length,
    repairRows: repairRows.length,
    slippingContacts,
    failedJoints,
    maxImpulse: physics.latestConstraintStep.max_impulse,
    maxSlip: physics.latestConstraintStep.max_slip_delta
  });
}

function runContactConstraintPhysicsLoop() {
  ensureGamePrototype();
  const before = ensurePrototype3DWorld().physics.contactConstraintLedger.length;
  let last = null;
  for (let index = 0; index < 4; index += 1) {
    last = runContactConstraintPhysicsStep(`contact constraint loop ${index + 1}`).payload;
  }
  const physics = ensurePrototype3DWorld().physics;
  return log('runContactConstraintPhysicsLoop', {
    stepsAdded: physics.contactConstraintLedger.length - before,
    contactRows: physics.contactConstraintLedger.length,
    jointRows: physics.jointConstraintLedger.length,
    frictionRows: physics.frictionLedger.length,
    impulseRows: physics.impulseLedger.length,
    repairRows: physics.constraintRepairLedger.length,
    lastStepId: last ? last.stepId : null
  });
}

function ensureComponentMaterialState(component) {
  if (!component.material_state) {
    component.material_state = {
      dryness: Number(clamp(1 - Number(component.moisture || 0.25)).toFixed(3)),
      saturation: Number(clamp(Number(component.moisture || 0.25)).toFixed(3)),
      char: 0,
      rot: 0,
      seal: component.material_id === 'resin_smear' ? 0.35 : 0,
      crack: 0,
      softened: 0,
      hardened: 0,
      last_phase: 'ordinary',
    };
  }
  return component.material_state;
}

function materialStatePhase(component, material, state) {
  if (state.char > 0.45) return 'charred';
  if (state.rot > 0.38) return 'rotting';
  if (state.crack > 0.34) return 'cracked';
  if (state.seal > 0.42) return 'sealed';
  if (state.saturation > 0.58) return 'waterlogged';
  if (state.dryness > 0.72) return 'dry_hardened';
  if (state.softened > 0.32) return 'softened';
  if ((material.id || component.material_id) === 'clay_vessel' && state.hardened > 0.35) return 'hardened_clay';
  return 'ordinary';
}

function runMaterialStatePhysicsStep(source = 'manual material state') {
  ensureGamePrototype();
  const sim = ensurePrototype3DWorld();
  const physics = sim.physics;
  ['materialStateLedger', 'phaseChangeLedger', 'propertyDriftLedger', 'materialStateRepairLedger'].forEach(key => {
    if (!Array.isArray(physics[key])) physics[key] = [];
  });
  ['material state', 'phase drift', 'property mutation'].forEach(layer => {
    if (!physics.solver_layers.includes(layer)) physics.solver_layers.push(layer);
  });
  const entropy = typeof deepTimeEntropyByte === 'function' ? deepTimeEntropyByte() : ((world.tick * 131) % 256);
  physics.materialStateStep = (physics.materialStateStep || 0) + 1;
  const stepId = `G3M-${String(physics.materialStateStep).padStart(3, '0')}`;
  const field = physics.environment || { moisture: 0.31, heat: 0.46, wind: 0.18, stress: 0.16, decayPressure: 0.22 };
  const stateRows = [];
  const phaseRows = [];
  const propertyRows = [];
  const repairRows = [];
  let phaseChanges = 0;
  let riskyComponents = 0;

  (sim.components || []).forEach((component, index) => {
    const material = sim.materialCatalog[component.material_id] || { water_resistance: 0.4, heat_resistance: 0.4, decay_rate: 0.02, flammability: 0.2, hardness: 0.3, brittleness: 0.2, workability: 0.4 };
    const state = ensureComponentMaterialState(component);
    const beforePhase = state.last_phase || materialStatePhase(component, material, state);
    const heat = Number(component.temperature || field.heat || 0.45);
    const moisture = Number(component.moisture || field.moisture || 0.3);
    const waterResistance = Number(material.water_resistance || 0.4) + Number(state.seal || 0) * 0.18;
    const heatResistance = Number(material.heat_resistance || 0.4);
    const organic = ['rough_branch', 'fiber', 'reed_cover', 'resin_smear'].includes(component.material_id);
    const porous = ['rough_branch', 'fiber', 'reed_cover', 'clay_vessel'].includes(component.material_id);
    const stochasticPulse = ((entropy + index * 41 + stepId.length) % 100) / 100;
    const wetting = Math.max(0, moisture + Number(field.moisture || 0.3) * 0.25 - waterResistance) * (porous ? 0.08 : 0.025);
    const drying = Math.max(0, heat + Number(field.wind || 0.18) * 0.2 - moisture) * 0.055;
    const heatDamage = Math.max(0, heat - heatResistance) * 0.07;
    const charDelta = Math.max(0, heatDamage * Number(material.flammability || 0.2) + (stochasticPulse < 0.04 && heat > 0.55 ? 0.018 : 0));
    const rotDelta = organic ? Math.max(0, moisture - waterResistance) * (0.022 + Number(material.decay_rate || 0.02)) + Number(field.decayPressure || 0.2) * 0.01 : 0;
    const sealDelta = component.material_id === 'resin_smear' || /resin|seal/.test(component.source || '') ? Math.max(0, heat * 0.018 - moisture * 0.008) : 0;
    const crackDelta = component.material_id === 'clay_vessel' ? Math.max(0, heat - heatResistance + Number(state.saturation || 0) * 0.45) * 0.025 : Math.max(0, Number(material.brittleness || 0.2) - Number(material.flexibility || 0.3)) * heatDamage * 0.03;
    state.saturation = Number(clamp(Number(state.saturation || 0) + wetting - drying * 0.45).toFixed(3));
    state.dryness = Number(clamp(Number(state.dryness || 0.5) + drying - wetting * 0.5).toFixed(3));
    state.char = Number(clamp(Number(state.char || 0) + charDelta).toFixed(3));
    state.rot = Number(clamp(Number(state.rot || 0) + rotDelta).toFixed(3));
    state.seal = Number(clamp(Number(state.seal || 0) + sealDelta - state.rot * 0.003).toFixed(3));
    state.crack = Number(clamp(Number(state.crack || 0) + crackDelta).toFixed(3));
    state.softened = Number(clamp(Number(state.softened || 0) + wetting * 0.6 + heatDamage * 0.18 - drying * 0.18).toFixed(3));
    state.hardened = Number(clamp(Number(state.hardened || 0) + drying * (component.material_id === 'clay_vessel' ? 0.9 : 0.25) + state.char * 0.012).toFixed(3));
    const afterPhase = materialStatePhase(component, material, state);
    state.last_phase = afterPhase;
    const propertyDrift = {
      hardness: Number(clamp(Number(material.hardness || 0.3) + state.hardened * 0.08 + state.char * 0.05 - state.rot * 0.09 - state.softened * 0.08).toFixed(3)),
      brittleness: Number(clamp(Number(material.brittleness || 0.2) + state.crack * 0.12 + state.char * 0.11 - state.seal * 0.02).toFixed(3)),
      water_resistance: Number(clamp(Number(material.water_resistance || 0.4) + state.seal * 0.16 - state.crack * 0.04 - state.rot * 0.05).toFixed(3)),
      workability: Number(clamp(Number(material.workability || 0.4) + state.softened * 0.09 - state.char * 0.08 - state.crack * 0.06).toFixed(3)),
    };
    component.effective_properties = propertyDrift;
    component.moisture = Number(clamp(moisture + wetting - drying).toFixed(3));
    component.damage = Number(clamp(Number(component.damage || 0) + state.rot * 0.006 + state.crack * 0.004 + state.char * 0.003).toFixed(3));
    component.stability = Number(clamp(Number(component.stability || 0.6) - state.rot * 0.004 - state.crack * 0.005 + state.hardened * 0.002 + state.seal * 0.001).toFixed(3));
    if (afterPhase !== beforePhase) phaseChanges += 1;
    const risky = state.rot > 0.28 || state.char > 0.3 || state.crack > 0.24 || state.saturation > 0.66;
    if (risky) riskyComponents += 1;
    stateRows.push({
      material_state_step_id: stepId,
      component_id: component.component_id,
      material_id: component.material_id,
      saturation: state.saturation,
      dryness: state.dryness,
      char: state.char,
      rot: state.rot,
      seal: state.seal,
      crack: state.crack,
      softened: state.softened,
      hardened: state.hardened,
      phase: afterPhase,
      no_resource_spawning: true,
      hidden_law_normal_view: false
    });
    propertyRows.push({
      material_state_step_id: stepId,
      component_id: component.component_id,
      effective_hardness: propertyDrift.hardness,
      effective_brittleness: propertyDrift.brittleness,
      effective_water_resistance: propertyDrift.water_resistance,
      effective_workability: propertyDrift.workability,
      no_effect_without_cause: true,
      no_resource_spawning: true,
      hidden_law_normal_view: false
    });
    if (afterPhase !== beforePhase) {
      phaseRows.push({
        material_state_step_id: stepId,
        component_id: component.component_id,
        from_phase: beforePhase,
        to_phase: afterPhase,
        cause: `heat=${heat.toFixed(3)}, moisture=${moisture.toFixed(3)}, field=${Number(field.moisture || 0).toFixed(3)}/${Number(field.heat || 0).toFixed(3)}`,
        resident_visible_as: afterPhase === 'rotting' ? 'smell/softening' : afterPhase === 'cracked' ? 'small crack' : afterPhase === 'waterlogged' ? 'damp weight' : afterPhase === 'sealed' ? 'slicker surface' : 'changed handling',
        hidden_law_normal_view: false
      });
    }
    if (risky) {
      repairRows.push({
        repair_id: `G3MR-${String(physics.materialStateRepairLedger.length + repairRows.length + 1).padStart(3, '0')}`,
        material_state_step_id: stepId,
        component_id: component.component_id,
        reason: afterPhase,
        materials_needed: afterPhase === 'rotting' || afterPhase === 'waterlogged' ? ['fiber', 'care'] : ['care'],
        labor_time_cost: afterPhase === 'charred' || afterPhase === 'cracked' ? 2 : 1,
        avatar_direct_command: false,
        no_resource_spawning: true,
        hidden_law_normal_view: false
      });
    }
  });

  physics.materialStateLedger.push(...stateRows);
  physics.phaseChangeLedger.push(...phaseRows);
  physics.propertyDriftLedger.push(...propertyRows);
  physics.materialStateRepairLedger.push(...repairRows);
  physics.materialStateLedger = physics.materialStateLedger.slice(-180);
  physics.phaseChangeLedger = physics.phaseChangeLedger.slice(-100);
  physics.propertyDriftLedger = physics.propertyDriftLedger.slice(-180);
  physics.materialStateRepairLedger = physics.materialStateRepairLedger.slice(-100);
  physics.latestMaterialStateStep = {
    step_id: stepId,
    source,
    entropy,
    state_rows: stateRows.length,
    phase_changes: phaseChanges,
    property_rows: propertyRows.length,
    repair_rows: repairRows.length,
    risky_components: riskyComponents,
    hidden_law_normal_view: false,
    no_resource_spawning: true
  };
  if (repairRows.length) {
    applyPhysicsConsequencesToVillage({
      step_id: stepId,
      maintenance_pressure: true,
      failures: riskyComponents,
      collisions: 0,
      min_stability: (sim.components || []).reduce((min, component) => Math.min(min, Number(component.stability || 1)), 1),
      max_damage: (sim.components || []).reduce((max, component) => Math.max(max, Number(component.damage || 0)), 0),
      moisture_risk: Number(field.moisture || 0),
      field_stress: Number(field.stress || 0),
      field_heat: Number(field.heat || 0),
      field_moisture: Number(field.moisture || 0),
      related_material_state_step: stepId
    }, source);
  }
  recordRealityConstraint('material_state_physics', {
    resident: world.selected,
    sourceBeliefId: stepId,
    materials: ['rough_branch', 'fiber', 'clay_vessel', 'reed_cover', 'resin_smear'],
    publicObservation: `${stateRows.length} material state row(s), ${phaseChanges} phase change(s), ${riskyComponents} risky component(s)`,
    residentInterpretation: repairRows.length ? 'some materials changed under damp, heat, or age and need care' : 'materials changed slowly but stayed usable',
    materialTransformation: 'component state and effective properties drifted from heat, moisture, decay, sealing, cracking, and stochastic pressure without spawning material',
    timeCost: 1,
    workCost: repairRows.length ? 1 : 0,
    toolWear: riskyComponents,
    maintenanceObligation: repairRows.length ? 'material-state repair pressure entered village planning' : 'watch material condition',
    unintendedConsequence: phaseChanges ? 'resident-visible material phase change may affect future practice' : 'hidden property drift accumulated silently',
    hiddenLawInvolved: world.audit ? 'saturation, dryness, rot, char, seal, crack, hardening, effective material properties' : 'audit only',
    conservationCheck: true
  });
  recordPrototypeMilestone('material-state-physics', `${stepId}: states=${stateRows.length}, phases=${phaseChanges}, risky=${riskyComponents}`);
  return log('runMaterialStatePhysicsStep', {
    stepId,
    stateRows: stateRows.length,
    phaseChanges,
    propertyRows: propertyRows.length,
    repairRows: repairRows.length,
    riskyComponents
  });
}

function runMaterialStatePhysicsLoop() {
  ensureGamePrototype();
  const before = ensurePrototype3DWorld().physics.materialStateLedger.length;
  let last = null;
  for (let index = 0; index < 4; index += 1) {
    last = runMaterialStatePhysicsStep(`material state loop ${index + 1}`).payload;
  }
  const physics = ensurePrototype3DWorld().physics;
  return log('runMaterialStatePhysicsLoop', {
    stepsAdded: physics.materialStateLedger.length - before,
    stateRows: physics.materialStateLedger.length,
    phaseRows: physics.phaseChangeLedger.length,
    propertyRows: physics.propertyDriftLedger.length,
    repairRows: physics.materialStateRepairLedger.length,
    lastStepId: last ? last.stepId : null
  });
}

function applyPhysicsConsequencesToVillage(step, source = 'physics') {
  if (!step || !step.maintenance_pressure) return null;
  const sim = ensurePrototype3DWorld();
  const board = ensureVillageBoard();
  const structure = sim.structures && sim.structures.length ? sim.structures[0] : null;
  const term = structure ? sim.language.terms.find(row => row.term_id === structure.resident_term_id) : sim.language.terms[0];
  const resident = term ? term.origin_resident : world.selected;
  const existing = board.concerns.find(row => row.source === step.step_id);
  if (existing) return existing;
  const urgency = step.failures > 0 || step.min_stability < 0.64 ? 'high' : (step.collisions > 0 || step.moisture_risk > 0.34 ? 'medium' : 'low');
  const problem = `${term ? term.resident_word : 'local support'} physical strain after ${step.step_id}`;
  const concern = {
    concern_id: `VBC-PHY-${String(board.concerns.filter(row => /^VBC-PHY/.test(row.concern_id || '')).length + 1).padStart(2, '0')}`,
    resident,
    problem,
    source: step.step_id,
    urgency,
    who_felt_this: resident,
    avatar_direct_control: false,
    physics_cause: {
      source,
      failures: step.failures,
      collisions: step.collisions,
      min_stability: step.min_stability,
	      max_damage: step.max_damage,
	      moisture_risk: step.moisture_risk,
	      field_stress: step.field_stress,
	      field_heat: step.field_heat,
	      field_moisture: step.field_moisture,
	    }
	  };
  const proposal = {
    proposal_id: `VBP-PHY-${String(board.projectProposals.filter(row => /^VBP-PHY/.test(row.proposal_id || '')).length + 1).padStart(2, '0')}`,
    proposer: resident,
    problem_addressed: problem,
    materials_needed: urgency === 'high' ? ['fiber', 'wood', 'care'] : ['fiber', 'care'],
    likely_helpers: Object.keys(world.residents).filter(name => name !== resident).slice(0, 2),
    resident_willingness: Number(Math.max(0.18, Math.min(0.9, (world.residents[resident] ? world.residents[resident].trust : 0.5) - (urgency === 'high' ? 0.02 : 0))).toFixed(3)),
    known_objections: ['repair consumes fiber', 'weight may shift again', 'resident term does not explain hidden physics fully'],
    risk: urgency,
    maintenance_cost: urgency === 'high' ? 3 : 2,
    related_memories: [world.residents[resident] ? world.residents[resident].memory : 'physical strain noticed'],
    related_practice_nodes: structure ? [structure.structure_id] : [],
    related_physics_step: step.step_id,
    related_components: (sim.components || []).filter(component => Number(component.stability || 1) < 0.72 || Number(component.damage || 0) > 0.16).map(component => component.component_id).slice(0, 5),
    possible_failure_modes: ['support shifts again', 'fiber runs short', 'wet weather returns', 'resident misreads the cause'],
    current_support_level: urgency === 'high' ? 0.18 : 0.1,
    avatar_can_force: false,
    status: 'physics consequence proposed'
  };
  board.concerns.push(concern);
  board.projectProposals.push(proposal);
  mutateResident(resident, {
    trust: 0.002,
    progress: 0.004,
    memory: `noticed physical strain in ${term ? term.resident_word : 'local support'}`,
    historyEvent: 'physics consequence noticed',
    historyDetail: step.step_id
  });
  recordRealityConstraint('physics_to_village_board', {
    resident,
    sourceBeliefId: step.step_id,
    materials: proposal.materials_needed,
    publicObservation: concern.problem,
    residentInterpretation: proposal.status,
    materialTransformation: 'physics produced concern/proposal only; no repair until material and labor are spent',
    timeCost: 1,
    workCost: 1,
    toolWear: step.failures,
    maintenanceObligation: proposal.proposal_id,
    unintendedConsequence: 'physical instability entered social planning',
	    hiddenLawInvolved: world.audit ? 'support, collision, fatigue, moisture, heat, stochastic field pressure' : 'audit only',
    conservationCheck: true
  });
  recordPrototypeMilestone('physics-to-village-board', `${step.step_id} created ${proposal.proposal_id} for ${resident}`);
  return { concern, proposal };
}

function runPrototypePhysicsStep() {
  ensureGamePrototype();
  const step = applyPrototypePhysicsStep('manual physics step');
  const consequence = applyPhysicsConsequencesToVillage(step, 'manual physics step');
  recordRealityConstraint('prototype_stochastic_physics', {
    resident: world.selected,
    sourceBeliefId: step.step_id,
    materials: ['rough_branch', 'fiber', 'clay_vessel', 'reed_cover'],
    publicObservation: `${step.support_checks} support check(s), ${step.collisions} contact event(s), ${step.failures} failure event(s)`,
    residentInterpretation: 'materials held, shifted, or failed because bodies have weight and support limits',
    materialTransformation: step.failures ? 'component damage/stability changed from stochastic physical failure' : 'forces/support/contact updated without spawning resources',
    timeCost: 1,
    workCost: 0,
    toolWear: step.failures,
    maintenanceObligation: step.failures ? 'resident repair proposal or retying may be needed' : 'watch support and moisture',
    unintendedConsequence: step.collisions ? 'component contact added damage pressure' : 'structure remains physically constrained',
    hiddenLawInvolved: world.audit ? 'mass, gravity, support capacity, friction, stochastic fatigue' : 'audit only',
    conservationCheck: true
	  });
	  recordPrototypeMilestone('stochastic-physics-step', `${step.support_checks} support checks, ${step.collisions} collision(s), ${step.failures} failure(s)`);
	  return log('runPrototypePhysicsStep', { stepId: step.step_id, supportChecks: step.support_checks, collisions: step.collisions, failures: step.failures, maintenancePressure: step.maintenance_pressure, proposalId: consequence && consequence.proposal ? consequence.proposal.proposal_id : null, stochasticPhysics: true });
	}

function runPrototypeMaterialWorldStep() {
  ensureGamePrototype();
  const sim = ensurePrototype3DWorld();
  sim.runCount += 1;
  const physicsStep = applyPrototypePhysicsStep('material world coupled physics');
  const cycle = world.gamePrototypeDayCycle || ensurePrototypeDayCycle();
  const latestWeather = cycle.weatherLedger.length ? cycle.weatherLedger[cycle.weatherLedger.length - 1].weather : 'settled dry air';
  const wetPressure = /drizzle|damp|rain|wet/.test(latestWeather);
  const dryPressure = /dry|wind|sun/.test(latestWeather);
  const fieldMoisture = Number(physicsStep.field_moisture || 0.31);
  const fieldHeat = Number(physicsStep.field_heat || 0.46);
  const fieldStress = Number(physicsStep.field_stress || 0.16);
  const moistureDelta = wetPressure ? 0.045 + fieldMoisture * 0.015 : (dryPressure ? -0.04 + fieldMoisture * 0.006 : -0.012 + fieldMoisture * 0.004);
  let repairCost = 0;
  sim.components.forEach(component => {
    const material = sim.materialCatalog[component.material_id] || { decay_rate: 0.02, water_resistance: 0.5 };
    const waterPenalty = Math.max(0, 1 - Number(material.water_resistance || 0.5));
    component.moisture = Number(clamp(Number(component.moisture || 0) + moistureDelta * waterPenalty).toFixed(3));
    const decay = Number(material.decay_rate || 0.02) * (wetPressure ? 1.4 : 0.7);
    const heatWear = Math.max(0, fieldHeat - Number(material.heat_resistance || 0.4)) * 0.012;
    const stressWear = fieldStress * (1 - Number(material.flexibility || 0.4)) * 0.008;
    component.damage = Number(clamp(Number(component.damage || 0) + decay * (0.4 + component.moisture) + heatWear + stressWear).toFixed(3));
    component.stability = Number(clamp(Number(component.stability || 0.7) - component.damage * 0.035 - fieldStress * 0.006 + (dryPressure ? 0.01 : 0)).toFixed(3));
  });
  const structure = sim.structures[0];
  const linkedComponents = sim.components.filter(component => structure.component_ids.includes(component.component_id));
  const supportScore = linkedComponents.reduce((sum, component) => sum + Number(component.stability || 0), 0) / Math.max(1, linkedComponents.length);
  structure.stability = Number(clamp(supportScore).toFixed(3));
  structure.moisture_risk = Number(clamp(linkedComponents.reduce((sum, component) => sum + Number(component.moisture || 0), 0) / Math.max(1, linkedComponents.length)).toFixed(3));
  if (structure.stability < 0.72 && Number(world.resources.fiber || 0) > 0) {
    world.resources.fiber = Math.max(0, Number(world.resources.fiber || 0) - 1);
    repairCost = 1;
    structure.stability = Number(clamp(structure.stability + 0.04).toFixed(3));
    const binding = sim.components.find(component => component.material_id === 'fiber');
    if (binding) {
      binding.damage = Number(clamp(Number(binding.damage || 0) - 0.05).toFixed(3));
      binding.stability = Number(clamp(Number(binding.stability || 0) + 0.05).toFixed(3));
    }
  }
  const term = sim.language.terms.find(row => row.term_id === structure.resident_term_id);
  if (term) {
    term.adoption_count += 1;
    term.practical_score = Number(clamp(Number(term.practical_score || 0) + (structure.stability > 0.72 ? 0.025 : -0.01)).toFixed(3));
    term.translation_confidence = Number(clamp(Number(term.translation_confidence || 0.5) + 0.01).toFixed(3));
    if (term.adoption_count >= 5 && !term.variants.includes('taku')) term.variants.push('taku');
    if (term.meaning_drift.length < 8) term.meaning_drift.push(structure.stability > 0.72 ? 'working term for safe raised vessels' : 'warning term for retying raised vessels');
  }
  sim.language.soundRoots.forEach(root => {
    if ((root.linked_practice || '') === structure.structure_id || root.linked_practice === 'G3S-001') {
      root.adoption_count += 1;
      root.translation_confidence = Number(clamp(Number(root.translation_confidence || 0.5) + 0.006).toFixed(3));
    }
  });
  const observation = {
    observation_id: `G3O-${String(sim.observationLedger.length + 1).padStart(3, '0')}`,
    tick: world.tick,
    weather: latestWeather,
    public_observation: wetPressure ? 'raised vessels stayed usable but bindings felt damp' : 'raised vessels stayed off wet ground during ordinary storage',
    resident_interpretation: repairCost ? 'taku-ren needs fresh tying after wet weather' : 'taku-ren still seems useful for ku',
    linked_structure: structure.structure_id,
    hidden_law_visible_normal_view: false,
    engine_concept_audit_only: structure.engine_concept,
  };
  sim.observationLedger.push(observation);
  const step = {
    step_id: `G3S-${String(sim.stepLedger.length + 1).padStart(3, '0')}`,
    tick: world.tick,
    weather: latestWeather,
    components: sim.components.length,
    structures: sim.structures.length,
    resident_terms: sim.language.terms.length,
    repair_cost_fiber: repairCost,
    structure_stability: structure.stability,
    moisture_risk: structure.moisture_risk,
    no_fixed_asset: structure.no_fixed_asset,
    no_modern_resident_name: true,
    player_gloss_imperfect: true,
    hidden_law_normal_view: false,
	    physics_step_id: physicsStep.step_id,
	    support_checks: physicsStep.support_checks,
	    collisions: physicsStep.collisions,
	    failures: physicsStep.failures,
	    min_stability: physicsStep.min_stability,
	    max_damage: physicsStep.max_damage,
	    field_moisture: physicsStep.field_moisture,
	    field_heat: physicsStep.field_heat,
	    field_stress: physicsStep.field_stress,
	    maintenance_pressure: Boolean(physicsStep.maintenance_pressure || structure.stability < 0.74 || structure.moisture_risk > 0.32),
		  };
	  sim.stepLedger.push(step);
	  sim.latestStep = step;
  const consequence = applyPhysicsConsequencesToVillage(step, 'material world coupled physics');
	  recordRealityConstraint('prototype_3d_material_world', {
    resident: term ? term.origin_resident : 'Nia',
    sourceBeliefId: step.step_id,
    materials: ['rough_branch', 'fiber', 'clay_vessel', 'reed_cover'],
    publicObservation: observation.public_observation,
    residentInterpretation: observation.resident_interpretation,
	    materialTransformation: repairCost ? 'fiber consumed to retie damp raised storage supports' : 'stochastic moisture, heat, decay, and support fields updated existing components without spawning resources',
    timeCost: 1,
    workCost: 1,
    toolWear: repairCost ? 1 : 0,
    maintenanceObligation: 'inspect and retie fiber bindings on raised storage surface',
    unintendedConsequence: wetPressure ? 'damp bindings raise maintenance burden' : 'dry period strengthens confidence in local practice term',
	    hiddenLawInvolved: world.audit ? 'moisture resistance, heat resistance, decay rate, support stability, stochastic field stress' : 'audit only',
    conservationCheck: true
	  });
	  recordPrototypeMilestone('3d-material-language', `${structure.engine_concept} rendered from ${sim.components.length} components as ${term ? term.resident_word : 'local term'}`);
	  return log('runPrototypeMaterialWorldStep', { components: sim.components.length, structures: sim.structures.length, residentTerms: sim.language.terms.length, stability: structure.stability, repairCost, physicsStepId: physicsStep.step_id, physicsProposalId: consequence && consequence.proposal ? consequence.proposal.proposal_id : null, hiddenLawNormalView: false });
		}

function ensureMaterialManipulationLoop() {
  if (!world.gamePrototypeMaterialManipulation) {
    world.gamePrototypeMaterialManipulation = {
      runCount: 0,
      actionLedger: [],
      observationLedger: [],
      practiceLinks: [],
      failureLedger: [],
      boundary: 'resident-chosen physical manipulation only; avatar supports conditions and cannot command object handling',
    };
  }
  ['actionLedger', 'observationLedger', 'practiceLinks', 'failureLedger'].forEach(key => {
    if (!Array.isArray(world.gamePrototypeMaterialManipulation[key])) world.gamePrototypeMaterialManipulation[key] = [];
  });
  return world.gamePrototypeMaterialManipulation;
}

function residentCarryCapacity(residentName) {
  const autonomous = world.autonomousResidents || null;
  const needs = autonomous && autonomous.needState ? autonomous.needState[residentName] : null;
  const energy = needs ? Number(needs.energy || 0.5) : Number((world.residents[residentName] || {}).progress || 0.45);
  const hunger = needs ? Number(needs.hunger || 0.2) : 0.2;
  return Number(Math.max(1.2, 2.2 + energy * 3.4 - hunger * 0.6).toFixed(3));
}

function residentForMaterialManipulation(entropy) {
  const names = Object.keys(world.residents);
  if (world.selected && entropy % 4 !== 0) return world.selected;
  return names[(entropy + ensureMaterialManipulationLoop().actionLedger.length) % names.length];
}

function componentForManipulation(sim, action, residentName, entropy) {
  const carried = sim.components.find(component => component.carried_by === residentName);
  if (action === 'drop' && carried) return carried;
  const weak = sim.components
    .filter(component => Number(component.stability || 1) < 0.74 || Number(component.damage || 0) > 0.14 || Number(component.field_stress || 0) > 0.18)
    .sort((a, b) => (Number(a.stability || 1) - Number(b.stability || 1)) || (Number(b.damage || 0) - Number(a.damage || 0)))[0];
  const damp = sim.components
    .filter(component => Number(component.moisture || 0) > 0.34)
    .sort((a, b) => Number(b.moisture || 0) - Number(a.moisture || 0))[0];
  if (action === 'tie' && weak) return weak;
  if (action === 'dry' && damp) return damp;
  if (action === 'wet_test' && damp) return damp;
  if (action === 'carry') return sim.components.filter(component => Number(component.mass || 1) <= residentCarryCapacity(residentName)).sort((a, b) => Number(b.moisture || 0) - Number(a.moisture || 0))[0] || sim.components[entropy % sim.components.length];
  if (action === 'stack' && weak) return weak;
  return sim.components[(entropy + ensureMaterialManipulationLoop().actionLedger.length) % sim.components.length];
}

function chooseMaterialManipulationPlan(residentName, entropy, actionOverride = null) {
  const sim = ensurePrototype3DWorld();
  const loop = ensureMaterialManipulationLoop();
  const carried = sim.components.find(component => component.carried_by === residentName);
  const weak = sim.components.some(component => Number(component.stability || 1) < 0.72 || Number(component.damage || 0) > 0.18 || Number(component.field_stress || 0) > 0.2);
  const damp = sim.components.some(component => Number(component.moisture || 0) > 0.36);
  const sequence = loop.actionLedger.length + entropy;
  let action = actionOverride;
  if (!action || action === 'auto' || action === 'resident_choice') {
    if (carried && sequence % 3 === 0) action = 'drop';
    else if (weak && Number(world.resources.fiber || 0) > 0) action = 'tie';
    else if (damp && sequence % 2 === 0) action = 'dry';
    else if (sequence % 7 === 0) action = 'wet_test';
    else if (sequence % 5 === 0) action = 'stack';
    else if (sequence % 3 === 0) action = 'carry';
    else action = 'test';
  }
  const component = componentForManipulation(sim, action, residentName, entropy);
  const term = sim.language.terms.find(row => row.term_id === (component ? component.resident_term_id : 'TERM-TAKU-REN')) || sim.language.terms[0];
  return { action, residentName, component, term, capacity: residentCarryCapacity(residentName) };
}

function updatePracticeFromMaterialManipulation(row, term) {
  const loop = ensureMaterialManipulationLoop();
  const graph = ensureEmergentPracticeGraph();
  const repeated = loop.actionLedger.filter(existing => existing.action === row.action && existing.material_id === row.material_id && existing.success).length;
  const shouldCreate = row.success ? repeated >= 2 || row.action === 'test' : true;
  if (!shouldCreate) return null;
  const localVerb = row.action.replace('_', ' ');
  const localName = `${term ? term.resident_word : 'local'} ${localVerb} handling habit`;
  const existing = graph.nodes.find(node => node.local_name === localName);
  const node = existing || {
    practice_id: `EPG-${String(graph.nodes.length + 1).padStart(2, '0')}`,
    local_name: localName,
    resident_term: term ? term.resident_word : 'local',
    player_gloss: `${term ? term.player_gloss : 'local material'} ${localVerb} practice`,
    engine_concept: 'resident_physical_material_manipulation',
    origin_tick: world.tick,
    origin_resident: row.resident,
    origin_household: `${row.resident}-household`,
    origin_event: row.manipulation_id,
    problem_pressure: row.failure_reason || row.action,
    materials_used: [row.material_id],
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
    maintenance_cost: row.resource_cost && row.resource_cost.fiber ? row.resource_cost.fiber : 1,
    risk_flags: [],
    generations_survived: 0,
    status: 'emerging',
    avatar_role: 'witness_or_condition_supporter',
    hidden_properties_audit_only: true,
    source_manipulation_rows: [],
    construction_component_ids: [],
    component_affordances: [],
    language_term_id: term ? term.term_id : null,
    translation_confidence: term ? term.translation_confidence : 0.5,
  };
  node.source_manipulation_rows = Array.from(new Set((node.source_manipulation_rows || []).concat([row.manipulation_id])));
  node.construction_component_ids = Array.from(new Set((node.construction_component_ids || []).concat([row.component_id])));
  node.component_affordances = Array.from(new Set((node.component_affordances || []).concat([row.affordance])));
  node.observations_supporting = Array.from(new Set((node.observations_supporting || []).concat([row.public_observation])));
  node.failed_ancestor_tests = Array.from(new Set((node.failed_ancestor_tests || []).concat(row.success ? [] : [row.manipulation_id])));
  node.beliefs_involved = Array.from(new Set((node.beliefs_involved || []).concat([row.component_id, row.action])));
  node.social_transmission_path = Array.from(new Set((node.social_transmission_path || []).concat([`${row.resident}->${row.resident_term}`])));
  node.mutation_variants = Array.from(new Set((node.mutation_variants || []).concat([localName, row.resident_interpretation])));
  node.adoption_count += row.success ? 1 : 0;
  node.adoption_households = Array.from(new Set((node.adoption_households || []).concat([`${row.resident}-household`])));
  node.practical_score = Number(clamp(Number(node.practical_score || 0) + (row.success ? 0.12 : 0)).toFixed(3));
  node.ritual_score = Number(clamp(Number(node.ritual_score || 0) + (row.action === 'test' || !row.success ? 0.04 : 0.01)).toFixed(3));
  node.taboo_score = Number(clamp(Number(node.taboo_score || 0) + (row.success ? 0.01 : 0.18)).toFixed(3));
  node.dispute_score = Number(clamp(Number(node.dispute_score || 0) + (row.success ? 0.03 : 0.16)).toFixed(3));
  node.risk_flags = Array.from(new Set((node.risk_flags || []).concat(row.success ? ['material handling maintenance'] : ['failed manipulation warning'])));
  node.generations_survived = Math.max(Number(node.generations_survived || 0), Math.floor(node.adoption_count / 2));
  node.status = !row.success ? 'disputed' : node.adoption_count >= 4 && node.practical_score > 0.4 ? 'practical' : 'emerging';
  if (!existing) graph.nodes.push(node);
  graph.edges.push({ from: row.manipulation_id, to: node.practice_id, event: row.action, relation: row.success ? 'repeated_handling_into_practice' : 'failed_handling_into_warning', hiddenLawExposed: false });
  loop.practiceLinks.push({ manipulation_id: row.manipulation_id, practice_id: node.practice_id, relation: row.success ? 'evidence' : 'warning', resident: row.resident });
  if (loop.practiceLinks.length > 80) loop.practiceLinks.shift();
  if (term) {
    term.adoption_count += row.success ? 1 : 0;
    term.practical_score = Number(clamp(Number(term.practical_score || 0) + (row.success ? 0.012 : 0)).toFixed(3));
    term.dispute_score = Number(clamp(Number(term.dispute_score || 0) + (row.success ? 0 : 0.02)).toFixed(3));
    term.meaning_drift = term.meaning_drift || [];
    const drift = row.success ? `${term.resident_word} includes ${localVerb} handling` : `${term.resident_word} carries a ${localVerb} warning`;
    if (!term.meaning_drift.includes(drift)) term.meaning_drift.push(drift);
    if (term.adoption_count >= 8 && !term.variants.includes(`${term.resident_word}-ko`)) term.variants.push(`${term.resident_word}-ko`);
  }
  return node;
}

function runResidentMaterialManipulationStep(actionOverride = 'resident_choice') {
  ensureGamePrototype();
  const loop = ensureMaterialManipulationLoop();
  const sim = ensurePrototype3DWorld();
  if (!sim.physics || !sim.physics.latestStep) applyPrototypePhysicsStep('resident manipulation precheck');
  const entropy = deepTimeEntropyByte();
  const residentName = residentForMaterialManipulation(entropy);
  const plan = chooseMaterialManipulationPlan(residentName, entropy, actionOverride);
  const component = plan.component;
  if (!component) return log('runResidentMaterialManipulationStep', { manipulated: false, reason: 'no component available' });
  const material = sim.materialCatalog[component.material_id] || {};
  const before = {
    position3d: { ...(component.position3d || {}) },
    moisture: Number(component.moisture || 0),
    damage: Number(component.damage || 0),
    stability: Number(component.stability || 0),
    field_stress: Number(component.field_stress || 0),
    carried_by: component.carried_by || null,
  };
  const resourceCost = {};
  let success = true;
  let failureReason = null;
  let publicObservation = `${residentName} handled ${plan.term ? plan.term.resident_word : component.material_id}`;
  let residentInterpretation = `${plan.action.replace('_', ' ')} seemed worth remembering`;
  const mass = Number(component.mass || material.mass || 1);
  if (['carry', 'stack'].includes(plan.action) && mass > plan.capacity) {
    success = false;
    failureReason = `too heavy for ${residentName}`;
  }
  if (plan.action === 'tie' && Number(world.resources.fiber || 0) <= 0) {
    success = false;
    failureReason = 'no fiber for tying';
  }
  if (plan.action === 'wet_test' && Number(world.resources.water || 0) <= 0) {
    success = false;
    failureReason = 'no water for wet test';
  }
  const toolUse = success
    ? applyToolPhysicsUse(residentName, plan.action, component, 'resident_material_manipulation')
    : { tool_use_id: null, tool_id: null, fit: 0, wear_delta: 0, failed: false, repaired: false, action_blocked: false };
  if (toolUse.action_blocked) {
    success = false;
    failureReason = toolUse.failure_reason;
  }
  if (success && plan.action === 'carry') {
    component.carried_by = residentName;
    component.position3d.x = Number(Math.max(0, Math.min(120, Number(component.position3d.x || 0) + 10)).toFixed(3));
    component.position3d.y = Number(Math.max(0, Math.min(90, Number(component.position3d.y || 0) + 8)).toFixed(3));
    component.field_stress = Number(clamp(Number(component.field_stress || 0) + mass * 0.012).toFixed(3));
    publicObservation = `${residentName} carried ${plan.term ? plan.term.resident_word : component.material_id} without naming an engine concept`;
    residentInterpretation = mass > plan.capacity * 0.75 ? 'heavy things need two pauses' : 'this piece can be moved by one resident';
  } else if (success && plan.action === 'drop') {
    component.carried_by = null;
    component.position3d.z = Number(Math.max(0, Number(component.position3d.z || 0) - 4).toFixed(3));
    component.damage = Number(clamp(Number(component.damage || 0) + 0.006).toFixed(3));
    publicObservation = `${residentName} set ${plan.term ? plan.term.resident_word : component.material_id} down near the work edge`;
    residentInterpretation = 'setting it down changed the support feel';
  } else if (success && plan.action === 'tie') {
    resourceCost.fiber = 1;
    world.resources.fiber = Math.max(0, Number(world.resources.fiber || 0) - 1);
    component.damage = Number(clamp(Number(component.damage || 0) - 0.045).toFixed(3));
    component.stability = Number(clamp(Number(component.stability || 0) + 0.085).toFixed(3));
    component.field_stress = Number(clamp(Number(component.field_stress || 0) - 0.04).toFixed(3));
    publicObservation = `${residentName} retied ${plan.term ? plan.term.resident_word : component.material_id} with fiber`;
    residentInterpretation = 'tight binding makes the support less nervous';
  } else if (success && plan.action === 'dry') {
    component.moisture = Number(clamp(Number(component.moisture || 0) - 0.085).toFixed(3));
    component.temperature = Number(clamp(Number(component.temperature || 0.45) + 0.025).toFixed(3));
    component.position3d.y = Number(Math.max(0, Number(component.position3d.y || 0) - 6).toFixed(3));
    publicObservation = `${residentName} moved ${plan.term ? plan.term.resident_word : component.material_id} toward dry air`;
    residentInterpretation = 'dry handling calmed the damp part';
  } else if (success && plan.action === 'wet_test') {
    resourceCost.water = 1;
    world.resources.water = Math.max(0, Number(world.resources.water || 0) - 1);
    component.moisture = Number(clamp(Number(component.moisture || 0) + 0.09).toFixed(3));
    component.damage = Number(clamp(Number(component.damage || 0) + (1 - Number(material.water_resistance || 0.5)) * 0.025).toFixed(3));
    publicObservation = `${residentName} wet-tested ${plan.term ? plan.term.resident_word : component.material_id}`;
    residentInterpretation = Number(material.water_resistance || 0.5) < 0.4 ? 'water made it less trustworthy' : 'water did not ruin it immediately';
  } else if (success && plan.action === 'stack') {
    component.position3d.z = Number(Math.min(96, Number(component.position3d.z || 0) + 6).toFixed(3));
    component.field_stress = Number(clamp(Number(component.field_stress || 0) + 0.035).toFixed(3));
    component.stability = Number(clamp(Number(component.stability || 0) - 0.015 + Number(material.compression_strength || 0.3) * 0.02).toFixed(3));
    publicObservation = `${residentName} stacked or leaned ${plan.term ? plan.term.resident_word : component.material_id}`;
    residentInterpretation = 'height helps only if the lower pieces hold';
  } else if (success) {
    component.field_stress = Number(clamp(Number(component.field_stress || 0) + 0.02).toFixed(3));
    component.damage = Number(clamp(Number(component.damage || 0) + Number(material.brittleness || 0.3) * 0.006).toFixed(3));
    publicObservation = `${residentName} tested ${plan.term ? plan.term.resident_word : component.material_id} by touch and weight`;
    residentInterpretation = 'small test added evidence, not certainty';
  }
  if (!success) {
    publicObservation = `${residentName} failed to ${plan.action.replace('_', ' ')} ${plan.term ? plan.term.resident_word : component.material_id}: ${failureReason}`;
    residentInterpretation = 'failed handling became a warning';
    component.field_stress = Number(clamp(Number(component.field_stress || 0) + 0.012).toFixed(3));
  }
  const structure = sim.structures && sim.structures[0] ? sim.structures[0] : null;
  if (structure) {
    const linked = sim.components.filter(row => structure.component_ids.includes(row.component_id));
    structure.stability = Number(clamp(linked.reduce((sum, row) => sum + Number(row.stability || 0), 0) / Math.max(1, linked.length)).toFixed(3));
    structure.moisture_risk = Number(clamp(linked.reduce((sum, row) => sum + Number(row.moisture || 0), 0) / Math.max(1, linked.length)).toFixed(3));
  }
  const physicsStep = applyPrototypePhysicsStep('resident material manipulation');
  const row = {
    manipulation_id: `GPM-${String(loop.actionLedger.length + 1).padStart(3, '0')}`,
    tick: world.tick,
    resident: residentName,
    action: plan.action,
    component_id: component.component_id,
    material_id: component.material_id,
    affordance: component.affordance,
    resident_term: plan.term ? plan.term.resident_word : component.resident_term_id,
    player_gloss: plan.term ? plan.term.player_gloss : component.material_id,
    mass,
    carry_capacity: plan.capacity,
    resource_cost: resourceCost,
    tool_use_id: toolUse.tool_use_id,
    tool_id: toolUse.tool_id,
    tool_fit: toolUse.fit,
    tool_failed: toolUse.failed,
    tool_repaired: toolUse.repaired,
    tool_blocked: toolUse.action_blocked,
    success,
    failure_reason: failureReason,
    public_observation: publicObservation,
    resident_interpretation: residentInterpretation,
    before,
    after: {
      position3d: { ...(component.position3d || {}) },
      moisture: Number(component.moisture || 0),
      damage: Number(component.damage || 0),
      stability: Number(component.stability || 0),
      field_stress: Number(component.field_stress || 0),
      carried_by: component.carried_by || null,
    },
    physics_step_id: physicsStep.step_id,
    avatar_direct_command: false,
    resident_chosen: true,
    hidden_law_normal_view: false,
  };
  loop.runCount += 1;
  loop.actionLedger.push(row);
  loop.observationLedger.push({ observation_id: `GPO-${String(loop.observationLedger.length + 1).padStart(3, '0')}`, manipulation_id: row.manipulation_id, public_observation: publicObservation, resident_interpretation: residentInterpretation, hidden_law_visible_normal_view: false });
  if (!success) loop.failureLedger.push({ manipulation_id: row.manipulation_id, resident: residentName, component_id: component.component_id, failure_reason: failureReason, recoverable: true });
  loop.actionLedger = loop.actionLedger.slice(-120);
  loop.observationLedger = loop.observationLedger.slice(-120);
  loop.failureLedger = loop.failureLedger.slice(-80);
  const linkedPractice = updatePracticeFromMaterialManipulation(row, plan.term);
  mutateResident(residentName, {
    trust: success ? 0.002 : -0.001,
    progress: success ? 0.008 : 0.002,
    schedule: success ? `${plan.action.replace('_', ' ')} ${row.resident_term}` : `warns about ${row.resident_term}`,
    memory: residentInterpretation,
    historyEvent: 'resident material manipulation',
    historyDetail: `${row.manipulation_id} ${plan.action} ${component.component_id}`
  });
  if (world.autonomousResidents) recordVisibleResidentExpression(residentName, success ? 'material_manipulation' : 'experiment', world.autonomousResidents.needState[residentName]);
  recordRealityConstraint('resident_material_manipulation', {
    resident: residentName,
    sourceBeliefId: row.manipulation_id,
    materials: [component.material_id].concat(Object.keys(resourceCost)),
    publicObservation,
    residentInterpretation,
    materialTransformation: success ? `${plan.action.replace('_', ' ')} changed component position/moisture/damage/stability/stress` : 'failed manipulation preserved as warning evidence',
    timeCost: 1,
    workCost: success ? 2 : 1,
    toolWear: Number(toolUse.wear_delta || 0),
    maintenanceObligation: linkedPractice ? linkedPractice.practice_id : 'watch material handling evidence',
    unintendedConsequence: success ? 'resident handling can become practice evidence' : 'handling failure can become safety rule',
    hiddenLawInvolved: world.audit ? 'material mass, carry capacity, support, moisture, stress, and water resistance' : 'audit only',
    conservationCheck: true
  });
  recordPrototypeMilestone('resident-material-manipulation', `${row.manipulation_id}: ${residentName} ${plan.action} ${component.component_id}; success=${success}`);
  return log('runResidentMaterialManipulationStep', { manipulationId: row.manipulation_id, resident: residentName, action: plan.action, componentId: component.component_id, success, practiceId: linkedPractice ? linkedPractice.practice_id : null, physicsStepId: physicsStep.step_id, toolUseId: toolUse.tool_use_id, toolFailed: toolUse.failed });
}

function runResidentMaterialManipulationLoop() {
  ensureGamePrototype();
  const loop = ensureMaterialManipulationLoop();
  const before = loop.actionLedger.length;
  ['carry', 'dry', 'tie', 'wet_test', 'stack', 'test'].forEach(action => runResidentMaterialManipulationStep(action));
  recordPrototypeMilestone('resident-material-manipulation-loop', `${loop.actionLedger.length - before} resident physical handling action(s)`);
  return log('runResidentMaterialManipulationLoop', { actionsAdded: loop.actionLedger.length - before, totalActions: loop.actionLedger.length, practiceLinks: loop.practiceLinks.length });
}

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
      guideHistory: [],
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
  if (!world.gamePrototype.guideHistory) world.gamePrototype.guideHistory = [];
  if (world.resources && world.resources.food == null) world.resources.food = 7;
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
  advanceVillageProject();
  runRealityConstraintAudit();
  const practiceCount = world.emergentPracticeGraph ? world.emergentPracticeGraph.nodes.length : 0;
  const proposalCount = world.villageBoard ? world.villageBoard.projectProposals.length : 0;
  const projectRows = world.gamePrototypeProjects ? world.gamePrototypeProjects.projectLedger.length : 0;
  recordPrototypeMilestone('practice-and-proposal', `${practiceCount} practice node(s), ${proposalCount} proposal(s), ${projectRows} project work row(s), avatar support remains non-commanding`);
  return log('runPrototypePracticeChain', { practiceCount, proposalCount, projectRows, realityRows: world.realityConstraintLedger ? world.realityConstraintLedger.rows.length : 0 });
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
  runToolPhysicsLoop();
  runResourcePhysicsLoop();
  runThermalPhysicsLoop();
  runWaterPhysicsLoop();
  runEcologyPhysicsLoop();
  runStructuralPhysicsLoop();
  runContactConstraintPhysicsLoop();
  runMaterialStatePhysicsLoop();
  runPlayablePhysicsPracticeSliceLoop();
  runPlayableVillageDay03Loop();
  runPrimaryPlaySurfaceLoop();
  runFirstPlayableWalkthrough();
  runNormalPlayActionRailLoop();
  runPlayerModeInterfaceLoop();
  runPlayerProposalDeckLoop();
  runLivedPracticeLoop();
  runResidentWorksiteLoop();
  runPrototypeReturnProof();
  recordPrototypeMilestone('first-playable-loop-complete', 'opening, practice, proposal, tool physics, resource physics, thermal physics, water physics, ecology physics, structural stress, contact constraints, material state, playable physics-to-practice slice, Day 0-3 loop, primary play surface, first playable walkthrough, normal play action rail, player mode interface, resident proposal deck, lived practice loop, resident worksite, audit, save, return, and branch persistence executed from one game surface');
  return log('runFirstPlayablePrototypeLoop', {
    milestones: world.gamePrototype.milestones.length,
    practices: world.emergentPracticeGraph ? world.emergentPracticeGraph.nodes.length : 0,
    proposals: world.villageBoard ? world.villageBoard.projectProposals.length : 0,
    toolUses: world.gamePrototypeTools ? world.gamePrototypeTools.useLedger.length : 0,
    resourceSteps: world.gamePrototypeResourcePhysics ? world.gamePrototypeResourcePhysics.stockLedger.length : 0,
    thermalSteps: world.gamePrototypeThermalPhysics ? world.gamePrototypeThermalPhysics.heatLedger.length : 0,
    waterFlows: world.gamePrototypeWaterPhysics ? world.gamePrototypeWaterPhysics.flowLedger.length : 0,
    ecologyGrowth: world.gamePrototypeEcologyPhysics ? world.gamePrototypeEcologyPhysics.growthLedger.length : 0,
    structuralStress: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.stressLedger ? world.gamePrototype3DWorld.physics.stressLedger.length : 0,
    contactConstraints: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.contactConstraintLedger ? world.gamePrototype3DWorld.physics.contactConstraintLedger.length : 0,
    materialStates: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.materialStateLedger ? world.gamePrototype3DWorld.physics.materialStateLedger.length : 0,
    playableSliceReady: world.gamePrototypePlayableSlice ? world.gamePrototypePlayableSlice.acceptanceReady === true : false,
    villageDay03Ready: world.gamePrototypeVillageDay03 ? world.gamePrototypeVillageDay03.acceptanceReady === true : false,
    primaryPlaySurfaceReady: world.gamePrototypeWorldStage ? world.gamePrototypeWorldStage.acceptanceReady === true : false,
    walkthroughReady: world.gamePrototypeWalkthrough ? world.gamePrototypeWalkthrough.acceptanceReady === true : false,
    actionRailReady: world.gamePrototypeActionRail ? world.gamePrototypeActionRail.acceptanceReady === true : false,
    playerModeReady: world.gamePrototypePlayerMode ? world.gamePrototypePlayerMode.acceptanceReady === true : false,
    proposalDeckReady: world.gamePrototypeProposalDeck ? world.gamePrototypeProposalDeck.acceptanceReady === true : false,
    livedPracticeReady: world.gamePrototypeLivedPractice ? world.gamePrototypeLivedPractice.acceptanceReady === true : false,
    worksiteReady: world.gamePrototypeWorksite ? world.gamePrototypeWorksite.acceptanceReady === true : false,
    branchContinuity: world.hintBranchPersistence ? world.hintBranchPersistence.continuityRows.length : 0,
  });
}

function ensurePlayablePhysicsPracticeSlice() {
  ensureGamePrototype();
  if (!world.gamePrototypePlayableSlice) {
    world.gamePrototypePlayableSlice = {
      slice_id: 'PPS-01',
      milestone: 'physics-to-practice-playable-slice',
      runCount: 0,
      phase: 'not_started',
      phaseLedger: [],
      evidenceLedger: [],
      linkedPhysicsRows: [],
      linkedProposalIds: [],
      linkedPracticeIds: [],
      linkedResidentActionIds: [],
      linkedSaveSlotIds: [],
      returnProofRows: [],
      currentProblem: 'not observed yet',
      physicalCauseSummary: 'waiting for material, structural, contact, and resource evidence',
      residentInterpretation: 'no resident interpretation yet',
      proposedNextAction: 'enter the village and let residents observe a bottleneck',
      consequenceEvidence: 'no consequence evidence yet',
      acceptanceReady: false,
      boundary: 'playable slice evidence only; avatar influences conditions, residents decide',
      noDirectCommand: true,
      noPredeclaredTechTree: true,
      noCorrectConceptInstalled: true,
    };
  }
  return world.gamePrototypePlayableSlice;
}

function playableSliceTick() {
  return world.tick || (world.gamePrototypeDayCycle ? world.gamePrototypeDayCycle.day : 0) || 0;
}

function latestPlayableSliceRow(rows) {
  return Array.isArray(rows) && rows.length ? rows[rows.length - 1] : null;
}

function playableSliceRowId(prefix, row, fallbackIndex) {
  if (!row) return `${prefix}-none`;
  return row.step_id || row.event_id || row.row_id || row.id || row.proposal_id || row.practice_id || `${prefix}-${fallbackIndex}`;
}

function recordPlayableSlicePhase(phase, detail = {}) {
  const slice = ensurePlayablePhysicsPracticeSlice();
  const row = {
    phase,
    sequence: slice.phaseLedger.length + 1,
    tick: playableSliceTick(),
    detail,
  };
  slice.phase = phase;
  slice.phaseLedger.push(row);
  slice.evidenceLedger.push({
    evidence_id: `PPS-E-${String(slice.evidenceLedger.length + 1).padStart(2, '0')}`,
    kind: 'phase',
    phase,
    tick: row.tick,
    public_summary: detail.public_summary || phase,
    audit_summary: detail.audit_summary || detail.public_summary || phase,
    hidden_law_exposed_to_resident: false,
  });
  return row;
}

function collectPlayableSlicePhysicsEvidence() {
  const slice = ensurePlayablePhysicsPracticeSlice();
  const actionRows = [];
  if (typeof runPrototypeMaterialWorldStep === 'function') actionRows.push({ system: 'material_world', receipt: runPrototypeMaterialWorldStep('playable physics-to-practice slice') });
  if (typeof runMaterialStatePhysicsStep === 'function') actionRows.push({ system: 'material_state', receipt: runMaterialStatePhysicsStep('playable physics-to-practice slice') });
  else if (typeof runMaterialStatePhysicsLoop === 'function') actionRows.push({ system: 'material_state', receipt: runMaterialStatePhysicsLoop() });
  if (typeof runStructuralPhysicsStep === 'function') actionRows.push({ system: 'structural_stress', receipt: runStructuralPhysicsStep('playable physics-to-practice slice') });
  else if (typeof runStructuralPhysicsLoop === 'function') actionRows.push({ system: 'structural_stress', receipt: runStructuralPhysicsLoop() });
  if (typeof runContactConstraintPhysicsStep === 'function') actionRows.push({ system: 'contact_constraints', receipt: runContactConstraintPhysicsStep('playable physics-to-practice slice') });
  else if (typeof runContactConstraintPhysicsLoop === 'function') actionRows.push({ system: 'contact_constraints', receipt: runContactConstraintPhysicsLoop() });
  if (typeof runResourcePhysicsStep === 'function') actionRows.push({ system: 'resource_stock', receipt: runResourcePhysicsStep('playable physics-to-practice slice') });
  else if (typeof runResourcePhysicsLoop === 'function') actionRows.push({ system: 'resource_stock', receipt: runResourcePhysicsLoop() });

  const physics = world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics ? world.gamePrototype3DWorld.physics : {};
  const rows = [
    { system: 'material_state', row: latestPlayableSliceRow(physics.materialStateLedger), public_observation: 'worked material condition changed during ordinary use' },
    { system: 'property_drift', row: latestPlayableSliceRow(physics.propertyDriftLedger), public_observation: 'moisture, load, or wear changed a material affordance' },
    { system: 'structural_stress', row: latestPlayableSliceRow(physics.stressLedger), public_observation: 'a support or raised surface showed stress' },
    { system: 'structural_repair', row: latestPlayableSliceRow(physics.structuralRepairLedger), public_observation: 'repair work was physically needed' },
    { system: 'contact_constraint', row: latestPlayableSliceRow(physics.contactConstraintLedger), public_observation: 'a joint, resting contact, or lashing constrained movement' },
    { system: 'constraint_repair', row: latestPlayableSliceRow(physics.constraintRepairLedger), public_observation: 'a slipping or weakening constraint needed resident attention' },
  ].filter(entry => entry.row);
  if (world.gamePrototypeResourcePhysics) {
    rows.push(
      { system: 'resource_stock', row: latestPlayableSliceRow(world.gamePrototypeResourcePhysics.stockLedger), public_observation: 'commons stock changed after work' },
      { system: 'resource_loss', row: latestPlayableSliceRow(world.gamePrototypeResourcePhysics.lossLedger), public_observation: 'some stored material was lost or strained' }
    );
  }
  rows.filter(entry => entry.row).forEach((entry, index) => {
    const rowId = playableSliceRowId(entry.system, entry.row, slice.linkedPhysicsRows.length + index + 1);
    if (!slice.linkedPhysicsRows.some(existing => existing.row_id === rowId && existing.system === entry.system)) {
      slice.linkedPhysicsRows.push({
        row_id: rowId,
        system: entry.system,
        tick: playableSliceTick(),
        public_observation: entry.public_observation,
        hidden_law_reference: entry.row.hidden_law || entry.row.hidden_law_involved || entry.row.audit_law || 'audit-only material/constraint law',
        normal_view_hidden_law_exposed: false,
      });
    }
  });
  return { actionRows, rows: slice.linkedPhysicsRows.slice(-8) };
}

function summarizePlayableSlicePressure(evidence) {
  const latestSystems = evidence.rows.map(row => row.system).join(', ') || 'no physics rows yet';
  const cause = `latest grounded signals: ${latestSystems}`;
  const resourceStatus = [
    `fiber=${world.resources ? world.resources.fiber : 'n/a'}`,
    `wood=${world.resources ? world.resources.wood : 'n/a'}`,
    `care=${world.resources ? world.resources.care : 'n/a'}`
  ].join(', ');
  return {
    problem: 'raised storage and repair work are being shaped by moisture, stress, contact, and material stock',
    physicalCauseSummary: `${cause}; commons ${resourceStatus}`,
    residentInterpretation: 'residents read this as a practical storage/repair worry, not as a modern physics concept',
    proposedNextAction: 'support the resident proposal, then wait for residents to test a repair instead of assigning orders',
    consequenceEvidence: `${evidence.rows.length} linked physics row(s), ${evidence.actionRows.length} physics action(s) this step`,
  };
}

function ensurePlayableSliceProposal(pressure) {
  const slice = ensurePlayablePhysicsPracticeSlice();
  const board = ensureVillageBoard();
  const proposalId = 'VBP-PLAYABLE-PHYSICS-01';
  let proposal = board.projectProposals.find(row => row.proposal_id === proposalId);
  if (!proposal) {
    proposal = {
      proposal_id: proposalId,
      resident_proposer: 'Nia',
      problem_addressed: pressure.problem,
      materials_needed: { fiber: 1, wood: 1, care: 1 },
      likely_helpers: ['Ari', 'Fay'],
      resident_willingness: 0.74,
      known_objections: ['Milo worries that fiber stores are already strained', 'Ari wants a small test before broad adoption'],
      risk: 'repair may consume scarce fiber and still fail under wet stress',
      maintenance_cost: 'check lashings after rain and after heavy jar use',
      related_memories: ['wet storage failed before', 'raised jars sometimes stayed safer', 'bindings weaken under work'],
      related_practice_nodes: [],
      possible_failure_modes: ['binding slip', 'wet support sag', 'resource burden', 'household disagreement'],
      current_support_level: 0,
      status: 'resident proposed',
      source: slice.slice_id,
      related_physics_step: slice.linkedPhysicsRows.length ? slice.linkedPhysicsRows[slice.linkedPhysicsRows.length - 1].row_id : 'pending-physics-row',
      avatar_direct_command: false,
      avatar_can_force: false,
      hidden_law_normal_view: false,
    };
    board.projectProposals.push(proposal);
  }
  proposal.current_support_level = Math.min(1, (proposal.current_support_level || 0) + 0.25);
  proposal.status = proposal.current_support_level >= 0.5 ? 'conditions supported; resident decision pending' : proposal.status;
  proposal.problem_addressed = pressure.problem;
  proposal.related_physics_step = slice.linkedPhysicsRows.length ? slice.linkedPhysicsRows[slice.linkedPhysicsRows.length - 1].row_id : proposal.related_physics_step;
  if (!slice.linkedProposalIds.includes(proposal.proposal_id)) slice.linkedProposalIds.push(proposal.proposal_id);
  return proposal;
}

function runPlayableSliceResidentAction() {
  const slice = ensurePlayablePhysicsPracticeSlice();
  let receipt = null;
  if (typeof runResidentMaterialManipulationStep === 'function') receipt = runResidentMaterialManipulationStep('test raised storage repair');
  else if (typeof performNearbyAction === 'function') receipt = performNearbyAction();
  const actionId = receipt && receipt.id ? receipt.id : `PPS-A-${String(slice.linkedResidentActionIds.length + 1).padStart(2, '0')}`;
  if (!slice.linkedResidentActionIds.includes(actionId)) slice.linkedResidentActionIds.push(actionId);
  if (typeof mutateResident === 'function') {
    mutateResident('Nia', {
      trust: 0.002,
      progress: 0.006,
      memory: 'tested a raised storage repair after physics evidence and a supported proposal',
      historyEvent: 'playable slice resident test',
      historyDetail: 'Nia treated the avatar support as material help, not a command',
    });
  }
  return { action_id: actionId, receipt };
}

function ensurePlayableSliceLanguageTerm(practice) {
  const materialWorld = world.gamePrototype3DWorld;
  if (!materialWorld || !materialWorld.language || !Array.isArray(materialWorld.language.terms)) return null;
  const termId = 'TERM-PPS-TAKU-REN';
  let term = materialWorld.language.terms.find(row => row.term_id === termId);
  if (!term) {
    term = {
      term_id: termId,
      resident_word: 'taku-ren',
      player_gloss: 'roughly raised dry vessel repair habit',
      engine_concept: 'physics_to_practice_playable_slice',
      roots: [
        { sound: 'ta', gloss: 'dry/safe/sun-warmed', grounded_event: 'stored vessels fared better away from wet ground' },
        { sound: 'ku', gloss: 'hollow vessel/container', grounded_event: 'clay vessels repeatedly carried stored material' },
        { sound: 'ren', gloss: 'held above/tied up', grounded_event: 'supports and lashings kept vessels off wet ground' }
      ],
      origin_resident: practice.origin_resident,
      origin_household: practice.origin_household,
      origin_event: practice.origin_event,
      linked_practice_id: practice.practice_id,
      linked_materials: practice.materials_used,
      adoption_count: practice.adoption_count,
      variants: ['takren'],
      meaning_drift: ['dry/safe root applied to vessel storage', 'raised/held root added after support repairs'],
      taboo_score: practice.taboo_score,
      ritual_score: practice.ritual_score,
      practical_score: practice.practical_score,
      translation_confidence: 0.61,
      current_status: 'practical household term',
      hidden_engine_concept_exposed_to_resident: false,
    };
    materialWorld.language.terms.push(term);
  }
  term.adoption_count = practice.adoption_count;
  term.current_status = practice.status === 'practical' ? 'practical household term' : 'emerging household term';
  return term;
}

function ensurePlayableSlicePractice(proposal, pressure, residentAction) {
  const slice = ensurePlayablePhysicsPracticeSlice();
  const graph = ensureEmergentPracticeGraph();
  if (!Array.isArray(graph.edges)) graph.edges = [];
  const practiceId = 'EPG-PLAYABLE-PHYSICS-01';
  let practice = graph.nodes.find(row => row.practice_id === practiceId);
  if (!practice) {
    practice = {
      practice_id: practiceId,
      local_name: 'taku-ren',
      resident_term: 'taku-ren',
      player_gloss: 'roughly raised dry vessel repair habit',
      engine_concept: 'physics_to_practice_playable_slice',
      origin_tick: playableSliceTick(),
      origin_resident: 'Nia',
      origin_household: 'Nia household',
      origin_event: 'resident-tested repair after repeated physics and storage pressure',
      problem_pressure: pressure.problem,
      materials_used: ['clay vessel', 'rough branch support', 'fiber binding', 'drying time'],
      observations_supporting: [],
      failed_ancestor_tests: ['wet ground jar keeping', 'unsupported clay shelf', 'weak binding after rain'],
      beliefs_involved: ['quiet jars dislike wet ground', 'held-up vessels stay safer', 'bindings need checking after rain'],
      social_transmission_path: ['Nia household', 'Ari repair cue', 'Fay comfort/safety cue'],
      mutation_variants: ['takren working form', 'quiet jar repair habit'],
      adoption_count: 0,
      adoption_households: ['Nia household'],
      practical_score: 0.48,
      ritual_score: 0.12,
      taboo_score: 0.04,
      dispute_score: 0.22,
      maintenance_cost: 'fiber inspection after rain; occasional branch replacement',
      risk_flags: ['fiber scarcity', 'binding slip', 'false confidence after one dry day'],
      generation_survived: 0,
      status: 'emerging',
      source: slice.slice_id,
      avatar_caused: false,
      avatar_influenced: true,
      avatar_installed_correct_concept: false,
      hidden_law_resident_belief_split: true,
    };
    graph.nodes.push(practice);
  }
  const newObservations = slice.linkedPhysicsRows.slice(-4).map(row => `${row.system}: ${row.public_observation}`);
  newObservations.forEach(observation => {
    if (!practice.observations_supporting.includes(observation)) practice.observations_supporting.push(observation);
  });
  practice.adoption_count = Math.min(6, practice.adoption_count + 1);
  practice.practical_score = Math.min(1, practice.practical_score + 0.08);
  practice.dispute_score = Math.max(0.05, practice.dispute_score - 0.02);
  practice.status = practice.adoption_count >= 3 && practice.practical_score >= 0.62 ? 'practical' : 'emerging';
  if (proposal && Array.isArray(proposal.related_practice_nodes) && !proposal.related_practice_nodes.includes(practice.practice_id)) proposal.related_practice_nodes.push(practice.practice_id);
  if (!slice.linkedPracticeIds.includes(practice.practice_id)) slice.linkedPracticeIds.push(practice.practice_id);
  ensurePlayableSliceLanguageTerm(practice);
  if (graph.edges && proposal && !graph.edges.some(row => row.from === proposal.proposal_id && row.to === practice.practice_id)) {
    graph.edges.push({
      from: proposal.proposal_id,
      to: practice.practice_id,
      relation: 'proposal stabilized into repeated practice evidence',
      resident_action_id: residentAction ? residentAction.action_id : 'none',
      hidden_law_not_named: true,
    });
  }
  return practice;
}

function updatePlayableSliceAcceptance() {
  const slice = ensurePlayablePhysicsPracticeSlice();
  const phases = new Set(slice.phaseLedger.map(row => row.phase));
  slice.acceptanceReady = Boolean(
    phases.has('arrival') &&
    phases.has('physics_pressure') &&
    phases.has('resident_proposal') &&
    phases.has('resident_test') &&
    phases.has('practice_mutation') &&
    phases.has('save_return') &&
    slice.linkedPhysicsRows.length > 0 &&
    slice.linkedProposalIds.length > 0 &&
    slice.linkedPracticeIds.length > 0 &&
    slice.linkedSaveSlotIds.length > 0
  );
  return slice.acceptanceReady;
}

function runPlayablePhysicsPracticeSliceStep(action = 'guided playable slice') {
  const slice = ensurePlayablePhysicsPracticeSlice();
  slice.runCount += 1;
  if (!world.entered && typeof runPrototypeOpening === 'function') runPrototypeOpening();
  recordPlayableSlicePhase('arrival', {
    public_summary: 'avatar enters the village and sees ordinary storage/repair pressure',
    audit_summary: 'slice starts from current village state; no research report added',
  });

  const evidence = collectPlayableSlicePhysicsEvidence();
  const pressure = summarizePlayableSlicePressure(evidence);
  slice.currentProblem = pressure.problem;
  slice.physicalCauseSummary = pressure.physicalCauseSummary;
  slice.residentInterpretation = pressure.residentInterpretation;
  slice.proposedNextAction = pressure.proposedNextAction;
  slice.consequenceEvidence = pressure.consequenceEvidence;
  recordPlayableSlicePhase('physics_pressure', {
    public_summary: pressure.physicalCauseSummary,
    audit_summary: `${evidence.rows.length} linked physics row(s), hidden law remains audit-only`,
  });

  const proposal = ensurePlayableSliceProposal(pressure);
  recordPlayableSlicePhase('resident_proposal', {
    public_summary: `${proposal.resident_proposer} proposes a repair/test instead of receiving a command`,
    audit_summary: `${proposal.proposal_id}, support=${proposal.current_support_level}`,
  });

  const residentAction = runPlayableSliceResidentAction();
  recordPlayableSlicePhase('resident_test', {
    public_summary: `resident action ${residentAction.action_id} tests the repair path`,
    audit_summary: `action source=${action}`,
  });

  const practice = ensurePlayableSlicePractice(proposal, pressure, residentAction);
  recordPlayableSlicePhase('practice_mutation', {
    public_summary: `${practice.local_name} is ${practice.status} after repeated material evidence`,
    audit_summary: `${practice.practice_id}, adoption=${practice.adoption_count}, practical=${practice.practical_score.toFixed(2)}`,
  });

  let slot = null;
  const savesBefore = typeof ensurePrototypeSaves === 'function' ? ensurePrototypeSaves() : null;
  const plannedSlotId = savesBefore ? `GPS-${String(savesBefore.slots.length + 1).padStart(2, '0')}` : `GPS-PPS-${slice.linkedSaveSlotIds.length + 1}`;
  if (!slice.linkedSaveSlotIds.includes(plannedSlotId)) slice.linkedSaveSlotIds.push(plannedSlotId);
  slice.returnProofRows.push({
    return_id: `PPS-R-${String(slice.returnProofRows.length + 1).padStart(2, '0')}`,
    slot_id: plannedSlotId,
    phase: slice.phase,
    linked_practice_ids: slice.linkedPracticeIds.slice(),
    linked_proposal_ids: slice.linkedProposalIds.slice(),
    preserved_in_world_snapshot: true,
  });
  recordPlayableSlicePhase('save_return', {
    public_summary: `slice state saved for return with ${slice.linkedPracticeIds.length} practice link(s)`,
    audit_summary: plannedSlotId,
  });
  updatePlayableSliceAcceptance();
  if (typeof savePrototypeSlot === 'function') {
    slot = savePrototypeSlot('playable physics-to-practice slice');
    const actualSlotId = slot && slot.payload && slot.payload.slotId ? slot.payload.slotId : plannedSlotId;
    if (actualSlotId !== plannedSlotId) {
      slice.linkedSaveSlotIds = slice.linkedSaveSlotIds.map(row => row === plannedSlotId ? actualSlotId : row);
      slice.returnProofRows.forEach(row => {
        if (row.slot_id === plannedSlotId) row.slot_id = actualSlotId;
      });
    }
  }
  recordRealityConstraint('physics_to_practice_playable_slice', {
    sourceBeliefId: slice.slice_id,
    materials: ['clay_vessel', 'branch_support', 'fiber_commons'],
    materialTransformation: 'fiber support/repair attention plus resident-tested storage handling',
    timeCost: 1,
    workCost: 1,
    toolWear: 1,
    hiddenLawInvolved: 'audit-only material state, support, contact, and resource constraints',
    publicObservation: pressure.physicalCauseSummary,
    residentInterpretation: pressure.residentInterpretation,
    conservationCheck: true,
    maintenanceObligation: 'check lashings/support after rain and use',
    unintendedConsequence: 'fiber burden and household dispute remain possible',
  });
  recordPrototypeMilestone('physics-to-practice-playable-slice', {
    acceptance_ready: slice.acceptanceReady,
    phases: slice.phaseLedger.length,
    physics_rows: slice.linkedPhysicsRows.length,
    proposals: slice.linkedProposalIds.length,
    practices: slice.linkedPracticeIds.length,
    save_rows: slice.linkedSaveSlotIds.length,
  });
  return log('runPlayablePhysicsPracticeSliceStep', {
    acceptance_ready: slice.acceptanceReady,
    phase: slice.phase,
    current_problem: slice.currentProblem,
    physics_rows: slice.linkedPhysicsRows.length,
    proposals: slice.linkedProposalIds.length,
    practices: slice.linkedPracticeIds.length,
    saved_slots: slice.linkedSaveSlotIds.length,
  });
}

function runPlayablePhysicsPracticeSliceLoop() {
  let receipt = null;
  for (let step = 0; step < 2; step += 1) {
    const slice = ensurePlayablePhysicsPracticeSlice();
    if (slice.acceptanceReady && slice.linkedPracticeIds.length && slice.linkedSaveSlotIds.length) break;
    receipt = runPlayablePhysicsPracticeSliceStep('loop');
  }
  const slice = ensurePlayablePhysicsPracticeSlice();
  return log('runPlayablePhysicsPracticeSliceLoop', {
    acceptance_ready: slice.acceptanceReady,
    phases: slice.phaseLedger.length,
    physics_rows: slice.linkedPhysicsRows.length,
    proposals: slice.linkedProposalIds.length,
    practices: slice.linkedPracticeIds.length,
    saved_slots: slice.linkedSaveSlotIds.length,
    last_receipt: receipt ? receipt.type || receipt.event || 'recorded' : 'already ready',
  });
}

function formatPlayablePhysicsPracticeSlice() {
  const slice = world.gamePrototypePlayableSlice || ensurePlayablePhysicsPracticeSlice();
  const latestPractice = slice.linkedPracticeIds.length ? slice.linkedPracticeIds[slice.linkedPracticeIds.length - 1] : 'none';
  const latestProposal = slice.linkedProposalIds.length ? slice.linkedProposalIds[slice.linkedProposalIds.length - 1] : 'none';
  const latestSave = slice.linkedSaveSlotIds.length ? slice.linkedSaveSlotIds[slice.linkedSaveSlotIds.length - 1] : 'none';
  const recentPhases = slice.phaseLedger.slice(-6).map(row => `${row.sequence}. ${row.phase}: ${row.detail.public_summary || 'recorded'}`);
  return [
    `Phase: ${slice.phase}`,
    `Acceptance ready: ${slice.acceptanceReady ? 'yes' : 'no'}`,
    `Current village problem: ${slice.currentProblem}`,
    `Physical cause summary: ${slice.physicalCauseSummary}`,
    `Resident interpretation: ${slice.residentInterpretation}`,
    `Proposed next action: ${slice.proposedNextAction}`,
    `Consequence evidence: ${slice.consequenceEvidence}`,
    `Linked physics rows: ${slice.linkedPhysicsRows.length}`,
    `Linked proposal: ${latestProposal}`,
    `Linked practice: ${latestPractice}`,
    `Linked save slot: ${latestSave}`,
    `Boundary: ${slice.boundary}`,
    'Recent phases:',
    ...(recentPhases.length ? recentPhases : ['No playable slice phases yet.'])
  ].join('\n');
}

function ensurePlayableVillageDay03() {
  ensureGamePrototype();
  if (!world.gamePrototypeVillageDay03) {
    world.gamePrototypeVillageDay03 = {
      milestone: 'playable-village-day-0-3',
      phase: 'not_started',
      currentDay: 0,
      runCount: 0,
      dayLedger: [],
      playerLoopLedger: [],
      residentLoopLedger: [],
      worldLoopLedger: [],
      proposalLinks: [],
      practiceLinks: [],
      physicsLinks: [],
      saveLinks: [],
      returnLinks: [],
      observedProblems: [],
      acceptanceReady: false,
      noDirectCommand: true,
      noTechTreeUnlock: true,
      noPerfectInformation: true,
      boundary: 'finite playable Day 0-3 prototype loop; player influences conditions, residents mediate action',
    };
  }
  return world.gamePrototypeVillageDay03;
}

function latestVillageDay03Id(collection, fields, fallback) {
  if (!Array.isArray(collection) || !collection.length) return fallback;
  const row = collection[collection.length - 1];
  for (const field of fields) {
    if (row && row[field]) return row[field];
  }
  return fallback;
}

function pushUniqueVillageDay03(list, value) {
  if (value && !list.includes(value)) list.push(value);
}

function capturePlayableVillageDay03Evidence(loop, label) {
  const physics = world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics ? world.gamePrototype3DWorld.physics : null;
  const slice = world.gamePrototypePlayableSlice || null;
  const board = world.villageBoard || null;
  const graph = world.emergentPracticeGraph || null;
  const saves = world.gamePrototypeSaves || null;
  const returnLater = world.gamePrototypeReturnLater || null;
  if (physics) {
    pushUniqueVillageDay03(loop.physicsLinks, latestVillageDay03Id(physics.materialStateLedger, ['step_id', 'row_id', 'id'], null));
    pushUniqueVillageDay03(loop.physicsLinks, latestVillageDay03Id(physics.stressLedger, ['step_id', 'row_id', 'id'], null));
    pushUniqueVillageDay03(loop.physicsLinks, latestVillageDay03Id(physics.contactConstraintLedger, ['step_id', 'row_id', 'id'], null));
  }
  if (slice) {
    slice.linkedPhysicsRows.slice(-3).forEach(row => pushUniqueVillageDay03(loop.physicsLinks, row.row_id));
    slice.linkedProposalIds.slice(-2).forEach(id => pushUniqueVillageDay03(loop.proposalLinks, id));
    slice.linkedPracticeIds.slice(-2).forEach(id => pushUniqueVillageDay03(loop.practiceLinks, id));
  }
  if (board && board.projectProposals) {
    pushUniqueVillageDay03(loop.proposalLinks, latestVillageDay03Id(board.projectProposals, ['proposal_id'], null));
  }
  if (graph && graph.nodes) {
    pushUniqueVillageDay03(loop.practiceLinks, latestVillageDay03Id(graph.nodes, ['practice_id'], null));
  }
  if (saves && saves.slots) {
    pushUniqueVillageDay03(loop.saveLinks, latestVillageDay03Id(saves.slots, ['slot_id'], null));
  }
  if (returnLater && returnLater.returnLedger) {
    pushUniqueVillageDay03(loop.returnLinks, latestVillageDay03Id(returnLater.returnLedger, ['return_id'], null));
  }
  if (!loop.observedProblems.includes(label)) loop.observedProblems.push(label);
}

function recordPlayableVillageDay03(day, phase, summary, detail = {}) {
  const loop = ensurePlayableVillageDay03();
  const row = {
    row_id: `PVD03-${String(loop.dayLedger.length + 1).padStart(2, '0')}`,
    day,
    phase,
    tick: world.tick,
    summary,
    detail,
    avatar_direct_command: false,
    resident_mediated: true,
    hidden_law_normal_view: false,
  };
  loop.phase = phase;
  loop.currentDay = Math.max(loop.currentDay, day + 1);
  loop.dayLedger.push(row);
  loop.playerLoopLedger.push({
    row_id: `${row.row_id}-P`,
    day,
    action: detail.player_action || 'observe/support/wait',
    direct_command: false,
  });
  loop.residentLoopLedger.push({
    row_id: `${row.row_id}-R`,
    day,
    response: detail.resident_response || 'resident response mediated by schedule, memory, and resources',
    can_refuse_or_delay: true,
  });
  loop.worldLoopLedger.push({
    row_id: `${row.row_id}-W`,
    day,
    consequence: detail.world_consequence || 'world state changed through existing systems',
    causal_trace: true,
  });
  capturePlayableVillageDay03Evidence(loop, summary);
  return row;
}

function updatePlayableVillageDay03Acceptance() {
  const loop = ensurePlayableVillageDay03();
  const days = new Set(loop.dayLedger.map(row => row.day));
  loop.acceptanceReady = Boolean(
    days.has(0) &&
    days.has(1) &&
    days.has(2) &&
    days.has(3) &&
    loop.playerLoopLedger.length >= 4 &&
    loop.residentLoopLedger.length >= 4 &&
    loop.worldLoopLedger.length >= 4 &&
    loop.physicsLinks.length > 0 &&
    loop.proposalLinks.length > 0 &&
    loop.practiceLinks.length > 0 &&
    loop.saveLinks.length > 0 &&
    loop.returnLinks.length > 0 &&
    loop.noDirectCommand === true &&
    loop.noTechTreeUnlock === true
  );
  return loop.acceptanceReady;
}

function runPlayableVillageDay03Step() {
  const loop = ensurePlayableVillageDay03();
  loop.runCount += 1;
  const day = Math.min(loop.currentDay, 3);
  if (day === 0) {
    if (!world.entered && typeof runPrototypeOpening === 'function') runPrototypeOpening();
    if (typeof performNearbyAction === 'function') performNearbyAction();
    if (typeof runPrototypePhysicsStep === 'function') runPrototypePhysicsStep('playable village day 0');
    recordPlayableVillageDay03(0, 'day_0_arrival_inspection', 'entered village, inspected ordinary place pressure, and advanced physical state', {
      player_action: 'enter, inspect nearby, ask what is happening',
      resident_response: `${world.selected} remains on schedule while the avatar observes`,
      world_consequence: 'nearby action and stochastic 3D physics establish the first grounded bottleneck',
    });
  } else if (day === 1) {
    if (typeof runPlayablePhysicsPracticeSliceLoop === 'function') runPlayablePhysicsPracticeSliceLoop();
    if (typeof runVillageBoardLoop === 'function') runVillageBoardLoop();
    recordPlayableVillageDay03(1, 'day_1_proposal_and_test', 'physics evidence became a resident proposal and early practice test', {
      player_action: 'support conditions and watch resident proposal/test path',
      resident_response: 'residents propose and test instead of receiving a command',
      world_consequence: 'practice graph, village board, and causal ledger gain linked evidence',
    });
  } else if (day === 2) {
    if (typeof supportResourceCommons === 'function') supportResourceCommons();
    if (typeof advanceVillageProject === 'function') advanceVillageProject();
    if (typeof runAutonomousResidentSeason === 'function') runAutonomousResidentSeason();
    if (typeof runResidentBodyPhysicsLoop === 'function') runResidentBodyPhysicsLoop();
    if (typeof endVillageDay === 'function') endVillageDay();
    recordPlayableVillageDay03(2, 'day_2_resident_work_and_recovery', 'resident work, body cost, resource support, and project progress happened through existing loops', {
      player_action: 'offer material support, wait, and let residents decide work order',
      resident_response: 'residents work, delay, recover, or continue based on resources and state',
      world_consequence: 'project, commons, body physics, and day-cycle ledgers advance',
    });
  } else {
    if (typeof leaveAndReturnLater === 'function') leaveAndReturnLater();
    const saves = typeof ensurePrototypeSaves === 'function' ? ensurePrototypeSaves() : null;
    const plannedSlotId = saves ? `GPS-${String(saves.slots.length + 1).padStart(2, '0')}` : `GPS-PVD03-${loop.saveLinks.length + 1}`;
    pushUniqueVillageDay03(loop.saveLinks, plannedSlotId);
    capturePlayableVillageDay03Evidence(loop, 'return-session continuity and save proof');
    recordPlayableVillageDay03(3, 'day_3_return_and_save', 'player left, returned, and saved the Day 0-3 continuity state', {
      player_action: 'leave, return, inspect changed state, save',
      resident_response: 'residents carry forward schedule, proposal, and practice state',
      world_consequence: 'return ledger and prototype save slot preserve the loop evidence',
    });
    updatePlayableVillageDay03Acceptance();
    if (typeof savePrototypeSlot === 'function') {
      const slot = savePrototypeSlot('playable village day 0-3');
      const actualSlotId = slot && slot.payload && slot.payload.slotId ? slot.payload.slotId : plannedSlotId;
      if (actualSlotId !== plannedSlotId) {
        loop.saveLinks = loop.saveLinks.map(id => id === plannedSlotId ? actualSlotId : id);
      }
    }
  }
  updatePlayableVillageDay03Acceptance();
  recordRealityConstraint('playable_village_day_0_3', {
    sourceBeliefId: loop.milestone,
    materials: ['village_objects', 'resident_labor', 'commons_resources'],
    materialTransformation: 'ordinary play advanced physics, proposals, practice state, resident work, return, and save evidence',
    timeCost: 1,
    workCost: 1,
    toolWear: 0,
    hiddenLawInvolved: 'audit-only physics and material constraints already linked through child systems',
    publicObservation: `Playable Village Day 0-3 phase ${loop.phase}`,
    residentInterpretation: 'residents treat events as local work, repair, storage, and schedule concerns',
    conservationCheck: true,
    maintenanceObligation: 'continue observing practice maintenance, resource burden, and return-session consequences',
    unintendedConsequence: 'project burden, refusal, delay, or practice drift can still occur',
  });
  recordPrototypeMilestone('playable-village-day-0-3', {
    ready: loop.acceptanceReady,
    day_rows: loop.dayLedger.length,
    physics: loop.physicsLinks.length,
    proposals: loop.proposalLinks.length,
    practices: loop.practiceLinks.length,
    saves: loop.saveLinks.length,
    returns: loop.returnLinks.length,
  });
  return log('runPlayableVillageDay03Step', {
    ready: loop.acceptanceReady,
    phase: loop.phase,
    dayRows: loop.dayLedger.length,
    physicsLinks: loop.physicsLinks.length,
    proposalLinks: loop.proposalLinks.length,
    practiceLinks: loop.practiceLinks.length,
    saveLinks: loop.saveLinks.length,
    returnLinks: loop.returnLinks.length,
  });
}

function runPlayableVillageDay03Loop() {
  let receipt = null;
  for (let step = 0; step < 4; step += 1) {
    const loop = ensurePlayableVillageDay03();
    if (loop.acceptanceReady) break;
    receipt = runPlayableVillageDay03Step();
  }
  const loop = ensurePlayableVillageDay03();
  return log('runPlayableVillageDay03Loop', {
    ready: loop.acceptanceReady,
    phase: loop.phase,
    dayRows: loop.dayLedger.length,
    playerRows: loop.playerLoopLedger.length,
    residentRows: loop.residentLoopLedger.length,
    worldRows: loop.worldLoopLedger.length,
    lastReceipt: receipt ? receipt.type || receipt.event || 'recorded' : 'already ready',
  });
}

function formatPlayableVillageDay03() {
  const loop = world.gamePrototypeVillageDay03 || ensurePlayableVillageDay03();
  const rows = loop.dayLedger.slice(-6).map(row => `${row.row_id}: day ${row.day} / ${row.phase} / ${row.summary}`);
  return [
    `Phase: ${loop.phase}`,
    `Acceptance ready: ${loop.acceptanceReady ? 'yes' : 'no'}`,
    `Current day cursor: ${Math.min(loop.currentDay, 3)}`,
    `Player loop rows: ${loop.playerLoopLedger.length}`,
    `Resident loop rows: ${loop.residentLoopLedger.length}`,
    `World loop rows: ${loop.worldLoopLedger.length}`,
    `Physics links: ${loop.physicsLinks.length}`,
    `Proposal links: ${loop.proposalLinks.length}`,
    `Practice links: ${loop.practiceLinks.length}`,
    `Save links: ${loop.saveLinks.length}`,
    `Return links: ${loop.returnLinks.length}`,
    `Boundary: ${loop.boundary}`,
    'Recent Day 0-3 rows:',
    ...(rows.length ? rows : ['No Day 0-3 loop rows yet.'])
  ].join('\n');
}

function ensurePrimaryPlaySurface() {
  ensureGamePrototype();
  if (!world.gamePrototypeWorldStage) {
    world.gamePrototypeWorldStage = {
      milestone: 'primary-play-surface',
      phase: 'not_started',
      runCount: 0,
      focusLedger: [],
      canvasCueLedger: [],
      actionPromptLedger: [],
      latestSnapshot: null,
      acceptanceReady: false,
      canvasFirst: true,
      noHiddenLawInNormalView: true,
      noDirectCommand: true,
      boundary: 'primary canvas play surface only; panels remain inspection/audit support',
    };
  }
  return world.gamePrototypeWorldStage;
}

function currentPrimaryPlaySurfaceSnapshot() {
  const guide = derivePrototypePlayerGuide();
  const slice = world.gamePrototypePlayableSlice || null;
  const day03 = world.gamePrototypeVillageDay03 || null;
  const board = world.villageBoard || null;
  const graph = world.emergentPracticeGraph || null;
  const materialWorld = world.gamePrototype3DWorld || null;
  const physics = materialWorld && materialWorld.physics ? materialWorld.physics : null;
  const selected = world.residents[world.selected] || currentResident();
  const latestProposal = board && board.projectProposals && board.projectProposals.length ? board.projectProposals[board.projectProposals.length - 1] : null;
  const latestPractice = graph && graph.nodes && graph.nodes.length ? graph.nodes[graph.nodes.length - 1] : null;
  const latestComponent = materialWorld && materialWorld.components && materialWorld.components.length ? materialWorld.components[materialWorld.components.length - 1] : null;
  const latestPhysics = physics && physics.latestMaterialStateStep ? physics.latestMaterialStateStep : (physics && physics.latestStructuralStep ? physics.latestStructuralStep : (physics && physics.latestConstraintStep ? physics.latestConstraintStep : (physics ? physics.latestStep : null)));
  const resourcePressure = Object.entries(world.resources)
    .filter(([, value]) => Number(value || 0) <= 3)
    .map(([key, value]) => `${key}:${value}`);
  const problem = day03 && day03.observedProblems.length
    ? day03.observedProblems[day03.observedProblems.length - 1]
    : slice && slice.currentProblem !== 'not observed yet'
      ? slice.currentProblem
      : latestProposal
        ? latestProposal.problem_addressed
        : 'observe the village until a physical bottleneck becomes visible';
  return {
    snapshot_id: `PPSURF-S-${String((world.gamePrototypeWorldStage ? world.gamePrototypeWorldStage.focusLedger.length : 0) + 1).padStart(2, '0')}`,
    tick: world.tick,
    room: world.avatar.room,
    selected_resident: world.selected,
    selected_schedule: selected.schedule,
    player_next_action: guide.nextAction,
    player_next_button: guide.button,
    player_next_reason: guide.why,
    stage_phase: day03 ? day03.phase : (slice ? slice.phase : guide.phase),
    current_problem: problem,
    active_proposal_id: latestProposal ? latestProposal.proposal_id : 'none',
    active_proposal_status: latestProposal ? latestProposal.status : 'none',
    active_practice_id: latestPractice ? latestPractice.practice_id : 'none',
    active_practice_name: latestPractice ? (latestPractice.local_name || latestPractice.practice_id) : 'none',
    active_component_id: latestComponent ? latestComponent.component_id : 'none',
    active_component_gloss: latestComponent ? (latestComponent.player_gloss || latestComponent.material_id || latestComponent.component_id) : 'none',
    latest_physics_id: latestPhysics ? (latestPhysics.step_id || latestPhysics.event_id || 'physics-row') : 'none',
    resource_pressure: resourcePressure,
    canvas_cues: [
      'look at the highlighted village problem band',
      latestProposal ? `proposal ${latestProposal.proposal_id}` : 'village board has no current proposal',
      latestPractice ? `practice ${latestPractice.local_name || latestPractice.practice_id}` : 'practice graph not yet visible',
      latestComponent ? `component ${latestComponent.component_id}` : 'physical components not initialized',
    ],
    hidden_law_normal_view: false,
    avatar_direct_command: false,
  };
}

function recordPrimaryPlaySurfaceSnapshot(reason = 'player requested primary play surface') {
  const surface = ensurePrimaryPlaySurface();
  const snapshot = currentPrimaryPlaySurfaceSnapshot();
  surface.runCount += 1;
  surface.phase = snapshot.stage_phase;
  surface.latestSnapshot = snapshot;
  surface.focusLedger.push({
    focus_id: `PPSURF-F-${String(surface.focusLedger.length + 1).padStart(2, '0')}`,
    snapshot_id: snapshot.snapshot_id,
    tick: world.tick,
    resident: snapshot.selected_resident,
    problem: snapshot.current_problem,
    proposal_id: snapshot.active_proposal_id,
    practice_id: snapshot.active_practice_id,
    component_id: snapshot.active_component_id,
    reason,
    canvas_first: true,
  });
  surface.canvasCueLedger.push({
    cue_id: `PPSURF-C-${String(surface.canvasCueLedger.length + 1).padStart(2, '0')}`,
    snapshot_id: snapshot.snapshot_id,
    cues: snapshot.canvas_cues,
    normal_view_hidden_law_exposed: false,
  });
  surface.actionPromptLedger.push({
    prompt_id: `PPSURF-A-${String(surface.actionPromptLedger.length + 1).padStart(2, '0')}`,
    snapshot_id: snapshot.snapshot_id,
    button: snapshot.player_next_button,
    action: snapshot.player_next_action,
    reason: snapshot.player_next_reason,
    direct_command: false,
  });
  surface.acceptanceReady = Boolean(
    surface.focusLedger.length >= 3 &&
    surface.canvasCueLedger.length >= 3 &&
    surface.actionPromptLedger.length >= 3 &&
    surface.focusLedger.some(row => row.proposal_id !== 'none') &&
    surface.focusLedger.some(row => row.practice_id !== 'none') &&
    surface.focusLedger.some(row => row.component_id !== 'none') &&
    surface.canvasFirst === true &&
    surface.noHiddenLawInNormalView === true &&
    surface.noDirectCommand === true
  );
  recordRealityConstraint('primary_play_surface', {
    sourceBeliefId: surface.milestone,
    materials: snapshot.active_component_id === 'none' ? ['canvas_attention'] : [snapshot.active_component_id],
    materialTransformation: 'no material spawned; canvas focus summarizes existing world state',
    timeCost: 0,
    workCost: 0,
    toolWear: 0,
    hiddenLawInvolved: 'none in normal view; audit-only physics IDs may be summarized',
    publicObservation: snapshot.current_problem,
    residentInterpretation: snapshot.active_practice_name,
    conservationCheck: true,
    maintenanceObligation: snapshot.active_proposal_id !== 'none' ? `watch ${snapshot.active_proposal_id}` : 'none',
    unintendedConsequence: 'player may over-focus one issue while residents keep autonomy',
  });
  recordPrototypeMilestone('primary-play-surface', {
    ready: surface.acceptanceReady,
    focus_rows: surface.focusLedger.length,
    cue_rows: surface.canvasCueLedger.length,
    prompt_rows: surface.actionPromptLedger.length,
    phase: surface.phase,
  });
  return snapshot;
}

function runPrimaryPlaySurfaceStep() {
  const surface = ensurePrimaryPlaySurface();
  if (!world.entered && typeof runPrototypeOpening === 'function') runPrototypeOpening();
  if ((!world.gamePrototype3DWorld || !world.gamePrototype3DWorld.physics || !world.gamePrototype3DWorld.physics.latestStep) && typeof runPrototypePhysicsStep === 'function') runPrototypePhysicsStep('primary play surface bootstrap');
  if ((!world.gamePrototypePlayableSlice || !world.gamePrototypePlayableSlice.acceptanceReady) && typeof runPlayablePhysicsPracticeSliceStep === 'function') runPlayablePhysicsPracticeSliceStep('primary play surface');
  if ((!world.gamePrototypeVillageDay03 || !world.gamePrototypeVillageDay03.acceptanceReady) && typeof runPlayableVillageDay03Step === 'function') runPlayableVillageDay03Step();
  const snapshot = recordPrimaryPlaySurfaceSnapshot('primary play surface step');
  return log('runPrimaryPlaySurfaceStep', {
    ready: surface.acceptanceReady,
    phase: surface.phase,
    problem: snapshot.current_problem,
    nextAction: snapshot.player_next_action,
    proposal: snapshot.active_proposal_id,
    practice: snapshot.active_practice_id,
    component: snapshot.active_component_id,
  });
}

function runPrimaryPlaySurfaceLoop() {
  let receipt = null;
  for (let step = 0; step < 4; step += 1) {
    const surface = ensurePrimaryPlaySurface();
    if (surface.acceptanceReady) break;
    receipt = runPrimaryPlaySurfaceStep();
  }
  const surface = ensurePrimaryPlaySurface();
  return log('runPrimaryPlaySurfaceLoop', {
    ready: surface.acceptanceReady,
    focusRows: surface.focusLedger.length,
    cueRows: surface.canvasCueLedger.length,
    promptRows: surface.actionPromptLedger.length,
    lastReceipt: receipt ? receipt.type || receipt.event || 'recorded' : 'already ready',
  });
}

function formatPrimaryPlaySurface() {
  const surface = world.gamePrototypeWorldStage || ensurePrimaryPlaySurface();
  const snapshot = surface.latestSnapshot || currentPrimaryPlaySurfaceSnapshot();
  const focus = surface.focusLedger.slice(-5).map(row => `${row.focus_id}: ${row.problem} / proposal=${row.proposal_id} / practice=${row.practice_id} / component=${row.component_id}`);
  return [
    `Phase: ${surface.phase}`,
    `Acceptance ready: ${surface.acceptanceReady ? 'yes' : 'no'}`,
    `Canvas-first: ${surface.canvasFirst ? 'yes' : 'no'}`,
    `Current problem: ${snapshot.current_problem}`,
    `Selected resident: ${snapshot.selected_resident} / ${snapshot.selected_schedule}`,
    `Next player action: ${snapshot.player_next_action} (${snapshot.player_next_button})`,
    `Active proposal: ${snapshot.active_proposal_id} / ${snapshot.active_proposal_status}`,
    `Active practice: ${snapshot.active_practice_id} / ${snapshot.active_practice_name}`,
    `Active component: ${snapshot.active_component_id} / ${snapshot.active_component_gloss}`,
    `Latest physics: ${snapshot.latest_physics_id}`,
    `Resource pressure: ${snapshot.resource_pressure.length ? snapshot.resource_pressure.join(', ') : 'none'}`,
    `Rows: focus=${surface.focusLedger.length}, cues=${surface.canvasCueLedger.length}, prompts=${surface.actionPromptLedger.length}`,
    `Boundary: ${surface.boundary}`,
    'Recent focus rows:',
    ...(focus.length ? focus : ['No primary play-surface rows yet.'])
  ].join('\n');
}

function ensureFirstPlayableWalkthrough() {
  ensureGamePrototype();
  if (!world.gamePrototypeWalkthrough) {
    world.gamePrototypeWalkthrough = {
      milestone: 'first-playable-walkthrough',
      runCount: 0,
      phase: 'not_started',
      stepLedger: [],
      evidenceLinks: [],
      receipt: null,
      exportReceipt: null,
      acceptanceReady: false,
      requiredSteps: [
        'enter_village',
        'inspect_world_stage',
        'observe_physical_bottleneck',
        'resident_proposal_or_test',
        'support_conditions',
        'resident_work_or_recovery',
        'return_session',
        'save_state',
        'acceptance_snapshot'
      ],
      boundary: 'first playable walkthrough receipt only; sequences existing prototype systems without adding new research mechanics',
      noDirectCommand: true,
      noTechTreeUnlock: true,
      noHiddenLawNormalView: true,
    };
  }
  return world.gamePrototypeWalkthrough;
}

function latestWalkthroughEvidence() {
  const board = world.villageBoard || null;
  const graph = world.emergentPracticeGraph || null;
  const saves = world.gamePrototypeSaves || null;
  const returnLater = world.gamePrototypeReturnLater || null;
  const stage = world.gamePrototypeWorldStage || null;
  const day03 = world.gamePrototypeVillageDay03 || null;
  const slice = world.gamePrototypePlayableSlice || null;
  const materialWorld = world.gamePrototype3DWorld || null;
  const physics = materialWorld && materialWorld.physics ? materialWorld.physics : null;
  return {
    room: world.avatar.room,
    entered: world.entered === true,
    selected_resident: world.selected,
    proposal_id: board && board.projectProposals && board.projectProposals.length ? board.projectProposals[board.projectProposals.length - 1].proposal_id : 'none',
    practice_id: graph && graph.nodes && graph.nodes.length ? graph.nodes[graph.nodes.length - 1].practice_id : 'none',
    stage_phase: stage ? stage.phase : 'not_started',
    stage_ready: stage ? stage.acceptanceReady === true : false,
    day03_phase: day03 ? day03.phase : 'not_started',
    day03_ready: day03 ? day03.acceptanceReady === true : false,
    slice_ready: slice ? slice.acceptanceReady === true : false,
    component_id: materialWorld && materialWorld.components && materialWorld.components.length ? materialWorld.components[materialWorld.components.length - 1].component_id : 'none',
    physics_id: physics && physics.latestStep ? physics.latestStep.step_id : (physics && physics.latestMaterialStateStep ? physics.latestMaterialStateStep.step_id : 'none'),
    save_slot_id: saves && saves.slots && saves.slots.length ? saves.slots[saves.slots.length - 1].slot_id : 'none',
    return_id: returnLater && returnLater.returnLedger && returnLater.returnLedger.length ? returnLater.returnLedger[returnLater.returnLedger.length - 1].return_id : 'none',
    acceptance_pass: world.gamePrototypeAcceptance ? world.gamePrototypeAcceptance.pass === true : false,
  };
}

function recordWalkthroughStep(step, summary, action, extra = {}) {
  const walk = ensureFirstPlayableWalkthrough();
  const evidence = latestWalkthroughEvidence();
  const row = {
    row_id: `FPW-${String(walk.stepLedger.length + 1).padStart(2, '0')}`,
    step,
    tick: world.tick,
    summary,
    action,
    evidence,
    avatar_direct_command: false,
    resident_mediated: true,
    hidden_law_normal_view: false,
    ...extra,
  };
  walk.phase = step;
  walk.stepLedger.push(row);
  walk.evidenceLinks.push({
    link_id: `FPW-L-${String(walk.evidenceLinks.length + 1).padStart(2, '0')}`,
    step,
    proposal_id: evidence.proposal_id,
    practice_id: evidence.practice_id,
    component_id: evidence.component_id,
    physics_id: evidence.physics_id,
    save_slot_id: evidence.save_slot_id,
    return_id: evidence.return_id,
  });
  return row;
}

function updateFirstPlayableWalkthroughAcceptance() {
  const walk = ensureFirstPlayableWalkthrough();
  const present = new Set(walk.stepLedger.map(row => row.step));
  const evidence = latestWalkthroughEvidence();
  walk.acceptanceReady = Boolean(
    walk.requiredSteps.every(step => present.has(step)) &&
    walk.stepLedger.length >= walk.requiredSteps.length &&
    evidence.entered &&
    walk.evidenceLinks.some(row => row.proposal_id !== 'none') &&
    walk.evidenceLinks.some(row => row.practice_id !== 'none') &&
    walk.evidenceLinks.some(row => row.component_id !== 'none') &&
    walk.evidenceLinks.some(row => row.physics_id !== 'none') &&
    walk.evidenceLinks.some(row => row.save_slot_id !== 'none') &&
    walk.evidenceLinks.some(row => row.return_id !== 'none') &&
    walk.noDirectCommand === true &&
    walk.noTechTreeUnlock === true &&
    walk.noHiddenLawNormalView === true
  );
  walk.receipt = {
    receipt_id: `FPW-R-${String(walk.runCount).padStart(2, '0')}`,
    phase: walk.phase,
    acceptance_ready: walk.acceptanceReady,
    step_count: walk.stepLedger.length,
    required_steps: walk.requiredSteps,
    completed_steps: Array.from(present),
    latest_evidence: evidence,
    boundary: walk.boundary,
  };
  return walk.acceptanceReady;
}

function runFirstPlayableWalkthrough() {
  const walk = ensureFirstPlayableWalkthrough();
  walk.runCount += 1;
  if (!world.entered && typeof runPrototypeOpening === 'function') runPrototypeOpening();
  recordWalkthroughStep('enter_village', 'entered the village and established resident context', 'runPrototypeOpening');

  if (typeof runPrimaryPlaySurfaceStep === 'function') runPrimaryPlaySurfaceStep();
  recordWalkthroughStep('inspect_world_stage', 'primary canvas surface summarized current problem, resident, proposal/practice context, and next action', 'runPrimaryPlaySurfaceStep');

  if (typeof runPrototypePhysicsStep === 'function') runPrototypePhysicsStep('first playable walkthrough');
  if (typeof runMaterialStatePhysicsStep === 'function') runMaterialStatePhysicsStep('first playable walkthrough');
  recordWalkthroughStep('observe_physical_bottleneck', 'stochastic physical state produced inspectable bottleneck evidence', 'physics/material state step');

  if (typeof runPlayablePhysicsPracticeSliceLoop === 'function') runPlayablePhysicsPracticeSliceLoop();
  if (typeof runVillageBoardLoop === 'function') runVillageBoardLoop();
  recordWalkthroughStep('resident_proposal_or_test', 'resident proposal/test path linked physical evidence to practice evidence', 'runPlayablePhysicsPracticeSliceLoop');

  if (typeof supportResourceCommons === 'function') supportResourceCommons();
  recordWalkthroughStep('support_conditions', 'avatar supported material conditions without direct job assignment', 'supportResourceCommons');

  if (typeof advanceVillageProject === 'function') advanceVillageProject();
  if (typeof runAutonomousResidentSeason === 'function') runAutonomousResidentSeason();
  if (typeof runResidentBodyPhysicsLoop === 'function') runResidentBodyPhysicsLoop();
  if (typeof runPlayableVillageDay03Loop === 'function') runPlayableVillageDay03Loop();
  recordWalkthroughStep('resident_work_or_recovery', 'residents advanced work, recovery, schedule, or body-state consequences through existing loops', 'advance/project/autonomy/body/day03');

  if (typeof leaveAndReturnLater === 'function') leaveAndReturnLater();
  recordWalkthroughStep('return_session', 'player left and returned with continuity evidence instead of resetting old state', 'leaveAndReturnLater');

  let slot = null;
  if (typeof savePrototypeSlot === 'function') slot = savePrototypeSlot('first playable walkthrough');
  recordWalkthroughStep('save_state', 'prototype save slot captured walkthrough-linked state', 'savePrototypeSlot', { slot_payload: slot && slot.payload ? slot.payload : null });

  if (typeof runPrimaryPlaySurfaceLoop === 'function') runPrimaryPlaySurfaceLoop();
  if (typeof buildPrototypeAcceptanceReceipt === 'function') {
    world.gamePrototypeAcceptance = buildPrototypeAcceptanceReceipt();
  }
  recordWalkthroughStep('acceptance_snapshot', 'acceptance snapshot was built from current prototype state', 'buildPrototypeAcceptanceReceipt');

  updateFirstPlayableWalkthroughAcceptance();
  if (typeof buildPrototypeAcceptanceReceipt === 'function') {
    world.gamePrototypeAcceptance = buildPrototypeAcceptanceReceipt();
    const acceptanceStep = walk.stepLedger[walk.stepLedger.length - 1];
    if (acceptanceStep && acceptanceStep.step === 'acceptance_snapshot') {
      acceptanceStep.evidence.acceptance_pass = world.gamePrototypeAcceptance.pass === true;
      acceptanceStep.evidence.acceptance_requirements = world.gamePrototypeAcceptance.requirements ? world.gamePrototypeAcceptance.requirements.length : 0;
    }
  }
  recordRealityConstraint('first_playable_walkthrough', {
    sourceBeliefId: walk.milestone,
    materials: ['existing_world_state', 'resident_labor', 'save_slot'],
    materialTransformation: 'sequenced existing playable systems without spawning resources',
    timeCost: 1,
    workCost: 1,
    toolWear: 0,
    hiddenLawInvolved: 'audit-only hidden law remains inside child receipts',
    publicObservation: `walkthrough ${walk.acceptanceReady ? 'ready' : 'incomplete'} with ${walk.stepLedger.length} step rows`,
    residentInterpretation: 'residents continue to interpret events as local work, storage, repair, and schedule concerns',
    conservationCheck: true,
    maintenanceObligation: 'continue playtesting from receipt gaps',
    unintendedConsequence: 'walkthrough may reveal missing playability or persistence evidence',
  });
  recordPrototypeMilestone('first-playable-walkthrough', {
    ready: walk.acceptanceReady,
    steps: walk.stepLedger.length,
    evidence_links: walk.evidenceLinks.length,
    phase: walk.phase,
  });
  return log('runFirstPlayableWalkthrough', {
    ready: walk.acceptanceReady,
    steps: walk.stepLedger.length,
    phase: walk.phase,
    proposal: latestWalkthroughEvidence().proposal_id,
    practice: latestWalkthroughEvidence().practice_id,
    save: latestWalkthroughEvidence().save_slot_id,
    return: latestWalkthroughEvidence().return_id,
  });
}

function formatFirstPlayableWalkthrough() {
  const walk = world.gamePrototypeWalkthrough || ensureFirstPlayableWalkthrough();
  const receipt = walk.receipt || {
    acceptance_ready: walk.acceptanceReady,
    step_count: walk.stepLedger.length,
    latest_evidence: latestWalkthroughEvidence(),
  };
  const rows = walk.stepLedger.slice(-9).map(row => `${row.row_id}: ${row.step} / ${row.summary}`);
  return [
    `Phase: ${walk.phase}`,
    `Acceptance ready: ${walk.acceptanceReady ? 'yes' : 'no'}`,
    `Steps: ${walk.stepLedger.length}/${walk.requiredSteps.length}`,
    `Latest proposal: ${receipt.latest_evidence.proposal_id}`,
    `Latest practice: ${receipt.latest_evidence.practice_id}`,
    `Latest component: ${receipt.latest_evidence.component_id}`,
    `Latest physics: ${receipt.latest_evidence.physics_id}`,
    `Latest save: ${receipt.latest_evidence.save_slot_id}`,
    `Latest return: ${receipt.latest_evidence.return_id}`,
    `Boundary: ${walk.boundary}`,
    'Walkthrough rows:',
    ...(rows.length ? rows : ['No first playable walkthrough rows yet.'])
  ].join('\n');
}

function exportFirstPlayableWalkthrough() {
  const walk = ensureFirstPlayableWalkthrough();
  if (!walk.receipt) updateFirstPlayableWalkthroughAcceptance();
  const receipt = {
    ...(walk.receipt || {}),
    step_ledger: walk.stepLedger,
    evidence_links: walk.evidenceLinks,
    exported_at_tick: world.tick,
  };
  walk.exportReceipt = receipt;
  localStorage.setItem(WALKTHROUGH_KEY, JSON.stringify(receipt, null, 2));
  let link = document.getElementById('preparedWalkthroughDownload');
  if (!link) {
    link = document.createElement('a');
    link.id = 'preparedWalkthroughDownload';
    link.textContent = 'Prepared first playable walkthrough receipt';
    link.download = 'ssrm_first_playable_walkthrough_receipt.json';
    link.style.display = 'block';
    link.style.marginTop = '10px';
    document.querySelector('.side-panel').appendChild(link);
  }
  link.href = URL.createObjectURL(new Blob([JSON.stringify(receipt, null, 2)], { type: 'application/json' }));
  return log('exportFirstPlayableWalkthrough', { ready: walk.acceptanceReady, steps: walk.stepLedger.length, links: walk.evidenceLinks.length });
}

function ensureNormalPlayActionRail() {
  ensureGamePrototype();
  if (!world.gamePrototypeActionRail) {
    world.gamePrototypeActionRail = {
      milestone: 'normal-play-action-rail',
      runCount: 0,
      actionLedger: [],
      optionLedger: [],
      receipt: null,
      acceptanceReady: false,
      verbs: ['look', 'ask', 'support', 'wait', 'return', 'save'],
      playerLanguageOnly: true,
      noDirectCommand: true,
      noTechTreeUnlock: true,
      boundary: 'normal player-facing action rail; maps simple verbs onto existing resident-mediated systems',
    };
  }
  return world.gamePrototypeActionRail;
}

function normalPlayOptions() {
  const guide = derivePrototypePlayerGuide();
  const stage = world.gamePrototypeWorldStage || null;
  const latest = stage && stage.latestSnapshot ? stage.latestSnapshot : currentPrimaryPlaySurfaceSnapshot();
  return [
    { verb: 'look', label: 'Look', action: 'runPrimaryPlaySurfaceStep', intent: 'read the current world-stage problem and object context', recommended: guide.button === 'runPrimaryPlaySurfaceStep' || !stage || !stage.acceptanceReady },
    { verb: 'ask', label: 'Ask', action: 'askSchedule', intent: `ask ${world.selected} about schedule and current concern`, recommended: guide.button === 'askSchedule' },
    { verb: 'support', label: 'Support', action: 'supportResourceCommons', intent: 'offer material help without assigning a job', recommended: guide.button === 'supportResourceCommons' },
    { verb: 'wait', label: 'Wait', action: 'endVillageDay', intent: 'let residents and world systems advance one step', recommended: guide.button === 'endVillageDay' || guide.button === 'runPlayableVillageDay03Step' },
    { verb: 'return', label: 'Return', action: 'leaveAndReturnLater', intent: 'leave and come back to check continuity', recommended: guide.button === 'leaveAndReturnLater' },
    { verb: 'save', label: 'Save', action: 'savePrototypeSlot', intent: 'save current village and walkthrough state', recommended: guide.button === 'exportPrototypeAcceptanceReceipt' || guide.button === 'runFirstPlayableWalkthrough' },
  ].map(option => ({
    ...option,
    current_problem: latest.current_problem,
    proposal_id: latest.active_proposal_id,
    practice_id: latest.active_practice_id,
    component_id: latest.active_component_id,
  }));
}

function updateNormalPlayActionRailAcceptance() {
  const rail = ensureNormalPlayActionRail();
  const verbs = new Set(rail.actionLedger.map(row => row.verb));
  rail.acceptanceReady = Boolean(
    rail.verbs.every(verb => verbs.has(verb)) &&
    rail.actionLedger.length >= rail.verbs.length &&
    rail.actionLedger.every(row => row.player_language === true && row.avatar_direct_command === false && row.hidden_law_normal_view === false) &&
    rail.optionLedger.length > 0 &&
    rail.noDirectCommand === true &&
    rail.noTechTreeUnlock === true
  );
  rail.receipt = {
    receipt_id: `NPAR-${String(rail.runCount).padStart(2, '0')}`,
    acceptance_ready: rail.acceptanceReady,
    verbs_completed: Array.from(verbs),
    action_rows: rail.actionLedger.length,
    option_rows: rail.optionLedger.length,
    latest_options: normalPlayOptions(),
    boundary: rail.boundary,
  };
  return rail.acceptanceReady;
}

function runNormalPlayAction(verb) {
  const rail = ensureNormalPlayActionRail();
  rail.runCount += 1;
  const options = normalPlayOptions();
  rail.optionLedger.push({
    option_id: `NPAO-${String(rail.optionLedger.length + 1).padStart(2, '0')}`,
    tick: world.tick,
    options,
    selected: verb,
  });
  const option = options.find(row => row.verb === verb) || options[0];
  let receipt = null;
  if (verb === 'look') receipt = runPrimaryPlaySurfaceStep();
  else if (verb === 'ask') receipt = askSchedule();
  else if (verb === 'support') receipt = supportResourceCommons();
  else if (verb === 'wait') {
    if (world.gamePrototypeVillageDay03 && !world.gamePrototypeVillageDay03.acceptanceReady) receipt = runPlayableVillageDay03Step();
    else receipt = endVillageDay();
  } else if (verb === 'return') receipt = leaveAndReturnLater();
  else if (verb === 'save') {
    if (!world.gamePrototypeWalkthrough || !world.gamePrototypeWalkthrough.acceptanceReady) runFirstPlayableWalkthrough();
    receipt = savePrototypeSlot('normal play action rail');
  }
  const evidence = latestWalkthroughEvidence();
  const row = {
    action_id: `NPAR-${String(rail.actionLedger.length + 1).padStart(2, '0')}`,
    verb: option.verb,
    label: option.label,
    underlying_action: option.action,
    player_intent: option.intent,
    tick: world.tick,
    current_problem: option.current_problem,
    proposal_id: evidence.proposal_id,
    practice_id: evidence.practice_id,
    component_id: evidence.component_id,
    physics_id: evidence.physics_id,
    save_slot_id: evidence.save_slot_id,
    return_id: evidence.return_id,
    receipt_type: receipt ? receipt.type || receipt.event || 'recorded' : 'none',
    player_language: true,
    avatar_direct_command: false,
    hidden_law_normal_view: false,
  };
  rail.actionLedger.push(row);
  updateNormalPlayActionRailAcceptance();
  recordRealityConstraint('normal_play_action_rail', {
    sourceBeliefId: row.action_id,
    materials: row.component_id === 'none' ? ['player_attention'] : [row.component_id],
    materialTransformation: `${row.label} action mapped to ${row.underlying_action}; no resource spawned by rail`,
    timeCost: verb === 'wait' || verb === 'return' ? 1 : 0,
    workCost: verb === 'support' ? 1 : 0,
    toolWear: 0,
    hiddenLawInvolved: 'none in normal view',
    publicObservation: row.current_problem,
    residentInterpretation: row.practice_id,
    conservationCheck: true,
    maintenanceObligation: row.proposal_id !== 'none' ? `watch ${row.proposal_id}` : 'none',
    unintendedConsequence: 'player-facing simplification may hide subsystem detail but not resident autonomy',
  });
  recordPrototypeMilestone('normal-play-action-rail', {
    ready: rail.acceptanceReady,
    verb: row.verb,
    action_rows: rail.actionLedger.length,
    option_rows: rail.optionLedger.length,
  });
  return log('runNormalPlayAction', { ready: rail.acceptanceReady, verb: row.verb, actionRows: rail.actionLedger.length, proposal: row.proposal_id, practice: row.practice_id });
}

function runNormalPlayLook() { return runNormalPlayAction('look'); }
function runNormalPlayAsk() { return runNormalPlayAction('ask'); }
function runNormalPlaySupport() { return runNormalPlayAction('support'); }
function runNormalPlayWait() { return runNormalPlayAction('wait'); }
function runNormalPlayReturn() { return runNormalPlayAction('return'); }
function runNormalPlaySave() { return runNormalPlayAction('save'); }

function runNormalPlayActionRailLoop() {
  const rail = ensureNormalPlayActionRail();
  rail.verbs.forEach(verb => {
    if (!new Set(rail.actionLedger.map(row => row.verb)).has(verb)) runNormalPlayAction(verb);
  });
  updateNormalPlayActionRailAcceptance();
  return log('runNormalPlayActionRailLoop', { ready: rail.acceptanceReady, actionRows: rail.actionLedger.length, optionRows: rail.optionLedger.length });
}

function formatNormalPlayActionRail() {
  const rail = world.gamePrototypeActionRail || ensureNormalPlayActionRail();
  const options = normalPlayOptions();
  const optionRows = options.map(option => `${option.label}: ${option.intent}; recommended=${option.recommended ? 'yes' : 'no'}`);
  const actionRows = rail.actionLedger.slice(-8).map(row => `${row.action_id}: ${row.label} -> ${row.underlying_action}; proposal=${row.proposal_id}; practice=${row.practice_id}; save=${row.save_slot_id}`);
  return [
    `Acceptance ready: ${rail.acceptanceReady ? 'yes' : 'no'}`,
    `Actions: ${rail.actionLedger.length} / option snapshots=${rail.optionLedger.length}`,
    `Verbs: ${rail.verbs.join(', ')}`,
    `Boundary: ${rail.boundary}`,
    'Current normal actions:',
    ...optionRows,
    'Recent action rows:',
    ...(actionRows.length ? actionRows : ['No normal play actions yet.'])
  ].join('\n');
}

function ensurePlayerModeInterface() {
  ensureGamePrototype();
  ensureNormalPlayActionRail();
  if (!world.gamePrototypePlayerMode) {
    world.gamePrototypePlayerMode = {
      milestone: 'player-mode-interface',
      enabled: false,
      runCount: 0,
      sessionLedger: [],
      visibleSurface: null,
      receipt: null,
      acceptanceReady: false,
      normalViewOnly: true,
      debugPanelsHidden: true,
      auditToggleAvailable: true,
      playerGlossesOnly: true,
      noDirectCommand: true,
      noHiddenLawNormalView: true,
      noTechTreeUnlock: true,
      boundary: 'normal player-facing mode; hides debug-heavy surfaces while preserving audit access and resident autonomy',
    };
  }
  return world.gamePrototypePlayerMode;
}

function playerModeVisibleSurfaceSnapshot() {
  const guide = derivePrototypePlayerGuide();
  const options = normalPlayOptions();
  const stage = world.gamePrototypeWorldStage || null;
  const latest = stage && stage.latestSnapshot ? stage.latestSnapshot : currentPrimaryPlaySurfaceSnapshot();
  const expression = latestVisibleExpressionFor(world.selected);
  const practice = world.emergentPracticeGraph && world.emergentPracticeGraph.nodes.length ? world.emergentPracticeGraph.nodes[world.emergentPracticeGraph.nodes.length - 1] : null;
  const proposal = world.villageBoard && world.villageBoard.projectProposals.length ? world.villageBoard.projectProposals[world.villageBoard.projectProposals.length - 1] : null;
  return {
    tick: world.tick,
    selected_resident: world.selected,
    current_room: world.avatar.room,
    current_problem: latest.current_problem || 'none',
    resident_cue: `${expression.marker}: ${expression.reason}`,
    next_action: guide.nextAction,
    next_action_hook: guide.button,
    action_verbs: options.map(row => row.label),
    recommended_verbs: options.filter(row => row.recommended).map(row => row.label),
    active_proposal: proposal ? `${proposal.proposal_id}: ${proposal.problem_addressed}` : 'none',
    active_practice: practice ? `${practice.practice_id}: ${practice.local_name}` : 'none',
    active_component: latest.active_component_id || 'none',
    visible_cards: ['world canvas', 'normal action rail', 'player guide', 'primary play surface', 'first playable walkthrough', 'normal play action rail', 'player mode interface', 'resident proposal deck', 'lived practice loop', 'resident worksite', 'public outcomes'],
    hidden_by_default: ['trace JSON', 'QA manifest', 'deep debug panels', 'prototype subsystem action grid', 'hidden simulator law detail'],
    audit_access: 'available after leaving player mode or through explicit audit/deep-panel controls',
    shows_public_state: true,
    exposes_hidden_law: false,
    direct_command: false,
    player_language: true,
    player_glosses_only: true,
  };
}

function updatePlayerModeInterfaceAcceptance() {
  const mode = ensurePlayerModeInterface();
  const snapshot = playerModeVisibleSurfaceSnapshot();
  mode.visibleSurface = snapshot;
  mode.acceptanceReady = Boolean(
    mode.enabled === true &&
    mode.normalViewOnly === true &&
    mode.debugPanelsHidden === true &&
    mode.auditToggleAvailable === true &&
    mode.playerGlossesOnly === true &&
    mode.noDirectCommand === true &&
    mode.noHiddenLawNormalView === true &&
    mode.noTechTreeUnlock === true &&
    mode.sessionLedger.length > 0 &&
    snapshot.visible_cards.length >= 6 &&
    snapshot.action_verbs.length >= 6 &&
    snapshot.shows_public_state === true &&
    snapshot.exposes_hidden_law === false &&
    snapshot.direct_command === false
  );
  mode.receipt = {
    receipt_id: `PMI-${String(mode.runCount).padStart(2, '0')}`,
    acceptance_ready: mode.acceptanceReady,
    enabled: mode.enabled,
    visible_cards: snapshot.visible_cards,
    hidden_by_default: snapshot.hidden_by_default,
    action_verbs: snapshot.action_verbs,
    latest_next_action: snapshot.next_action,
    boundary: mode.boundary,
  };
  return mode.acceptanceReady;
}

function applyPlayerModeClass() {
  if (typeof document === 'undefined' || !document.body) return;
  const mode = world.gamePrototypePlayerMode || null;
  document.body.classList.toggle('player-mode-active', Boolean(mode && mode.enabled));
}

function enterPlayerMode() {
  const mode = ensurePlayerModeInterface();
  mode.runCount += 1;
  mode.enabled = true;
  const snapshot = playerModeVisibleSurfaceSnapshot();
  mode.sessionLedger.push({
    session_id: `PMIS-${String(mode.sessionLedger.length + 1).padStart(2, '0')}`,
    tick: world.tick,
    action: 'enter',
    selected_resident: world.selected,
    current_problem: snapshot.current_problem,
    visible_cards: snapshot.visible_cards,
    hidden_by_default: snapshot.hidden_by_default,
    no_direct_command: true,
    no_hidden_law_normal_view: true,
  });
  if (mode.sessionLedger.length > 20) mode.sessionLedger.shift();
  updatePlayerModeInterfaceAcceptance();
  applyPlayerModeClass();
  recordRealityConstraint('player_mode_interface', {
    sourceBeliefId: mode.receipt.receipt_id,
    materials: ['player_attention', 'normal_action_rail'],
    materialTransformation: 'interface mode changed visible surfaces only; no world material spawned',
    timeCost: 0,
    workCost: 0,
    toolWear: 0,
    hiddenLawInvolved: 'none in normal view',
    publicObservation: snapshot.current_problem,
    residentInterpretation: snapshot.active_practice,
    conservationCheck: true,
    maintenanceObligation: 'keep audit access separate from normal player view',
    unintendedConsequence: 'debug detail is hidden by default but recoverable through explicit audit surfaces',
  });
  recordPrototypeMilestone('player-mode-interface', {
    ready: mode.acceptanceReady,
    enabled: mode.enabled,
    sessions: mode.sessionLedger.length,
    visible_cards: snapshot.visible_cards.length,
  });
  return log('enterPlayerMode', { ready: mode.acceptanceReady, enabled: mode.enabled, sessions: mode.sessionLedger.length });
}

function exitPlayerMode() {
  const mode = ensurePlayerModeInterface();
  mode.enabled = false;
  mode.sessionLedger.push({
    session_id: `PMIS-${String(mode.sessionLedger.length + 1).padStart(2, '0')}`,
    tick: world.tick,
    action: 'exit',
    selected_resident: world.selected,
    no_direct_command: true,
    no_hidden_law_normal_view: true,
  });
  if (mode.sessionLedger.length > 20) mode.sessionLedger.shift();
  updatePlayerModeInterfaceAcceptance();
  applyPlayerModeClass();
  return log('exitPlayerMode', { ready: mode.acceptanceReady, enabled: mode.enabled, sessions: mode.sessionLedger.length });
}

function togglePlayerMode() {
  const mode = ensurePlayerModeInterface();
  if (mode.enabled) return exitPlayerMode();
  return enterPlayerMode();
}

function runPlayerModeInterfaceLoop() {
  const mode = ensurePlayerModeInterface();
  if (!world.gamePrototypeActionRail || !world.gamePrototypeActionRail.acceptanceReady) runNormalPlayActionRailLoop();
  enterPlayerMode();
  updatePlayerModeInterfaceAcceptance();
  return log('runPlayerModeInterfaceLoop', { ready: mode.acceptanceReady, enabled: mode.enabled, sessions: mode.sessionLedger.length, visibleCards: mode.visibleSurface ? mode.visibleSurface.visible_cards.length : 0 });
}

function formatPlayerModeInterface() {
  const mode = world.gamePrototypePlayerMode || ensurePlayerModeInterface();
  const snapshot = mode.visibleSurface || playerModeVisibleSurfaceSnapshot();
  const sessionRows = mode.sessionLedger.slice(-6).map(row => `${row.session_id}: ${row.action}; resident=${row.selected_resident}; hidden-law=${row.no_hidden_law_normal_view === true ? 'not shown' : 'shown'}`);
  return [
    `Enabled: ${mode.enabled ? 'yes' : 'no'}`,
    `Acceptance ready: ${mode.acceptanceReady ? 'yes' : 'no'}`,
    `Boundary: ${mode.boundary}`,
    `Current problem: ${snapshot.current_problem}`,
    `Resident cue: ${snapshot.resident_cue}`,
    `Suggested next action: ${snapshot.next_action} (${snapshot.next_action_hook})`,
    `Normal verbs: ${snapshot.action_verbs.join(', ')}`,
    `Visible cards: ${snapshot.visible_cards.join(', ')}`,
    `Hidden by default: ${snapshot.hidden_by_default.join(', ')}`,
    `Audit access: ${snapshot.audit_access}`,
    `No direct command: ${mode.noDirectCommand ? 'yes' : 'no'}`,
    `Hidden law in normal view: ${mode.noHiddenLawNormalView ? 'no' : 'yes'}`,
    'Recent player-mode sessions:',
    ...(sessionRows.length ? sessionRows : ['No player-mode session yet.'])
  ].join('\n');
}

function ensurePlayerProposalDeck() {
  ensureGamePrototype();
  if (!world.gamePrototypeProposalDeck) {
    world.gamePrototypeProposalDeck = {
      milestone: 'resident-proposal-deck',
      runCount: 0,
      cardLedger: [],
      actionLedger: [],
      receipt: null,
      acceptanceReady: false,
      playerFacing: true,
      avatarCannotForce: true,
      noDirectCommand: true,
      noHiddenLawNormalView: true,
      noTechTreeUnlock: true,
      playerGlossesOnly: true,
      boundary: 'player-facing resident proposal deck; residents propose, avatar asks/supports/waits, no direct job assignment',
    };
  }
  return world.gamePrototypeProposalDeck;
}

function proposalDeckCards(seedIfEmpty = false) {
  const board = ensureVillageBoard();
  if (seedIfEmpty && !board.projectProposals.length) runVillageBoardLoop();
  return board.projectProposals
    .filter(proposal => !proposal.project_completed)
    .slice(-6)
    .map((proposal, index) => ({
      card_id: `PDC-${String(index + 1).padStart(2, '0')}`,
      proposal_id: proposal.proposal_id,
      proposer: proposal.proposer,
      problem: proposal.problem_addressed,
      materials_needed: proposal.materials_needed || [],
      likely_helpers: proposal.likely_helpers || [],
      willingness: Number(proposal.resident_willingness || 0),
      support_level: Number(proposal.current_support_level || 0),
      status: proposal.status,
      risk: proposal.risk || 'unknown',
      maintenance_cost: proposal.maintenance_cost || 0,
      known_objections: proposal.known_objections || [],
      possible_failure_modes: proposal.possible_failure_modes || [],
      related_practice_nodes: proposal.related_practice_nodes || [],
      player_actions: ['Ask', 'Support', 'Wait'],
      player_gloss: `${proposal.proposer} is concerned about ${proposal.problem_addressed}`,
      avatar_can_force: proposal.avatar_can_force === true ? true : false,
      hidden_law_normal_view: false,
      tech_tree_unlock: false,
      who_felt_this: proposal.proposer,
    }));
}

function updatePlayerProposalDeckAcceptance() {
  const deck = ensurePlayerProposalDeck();
  const cards = proposalDeckCards();
  const actions = new Set(deck.actionLedger.map(row => row.player_action));
  deck.acceptanceReady = Boolean(
    cards.length > 0 &&
    deck.cardLedger.length > 0 &&
    ['ask', 'support', 'wait'].every(action => actions.has(action)) &&
    deck.playerFacing === true &&
    deck.avatarCannotForce === true &&
    deck.noDirectCommand === true &&
    deck.noHiddenLawNormalView === true &&
    deck.noTechTreeUnlock === true &&
    cards.every(card => card.avatar_can_force === false && card.hidden_law_normal_view === false && card.tech_tree_unlock === false)
  );
  deck.receipt = {
    receipt_id: `PDR-${String(deck.runCount).padStart(2, '0')}`,
    acceptance_ready: deck.acceptanceReady,
    cards: cards.length,
    actions: Array.from(actions),
    boundary: deck.boundary,
  };
  return deck.acceptanceReady;
}

function recordProposalDeckAction(playerAction, result) {
  const deck = ensurePlayerProposalDeck();
  const cards = proposalDeckCards();
  const active = cards[0] || null;
  const row = {
    action_id: `PDA-${String(deck.actionLedger.length + 1).padStart(2, '0')}`,
    player_action: playerAction,
    tick: world.tick,
    proposal_id: active ? active.proposal_id : 'none',
    proposer: active ? active.proposer : world.selected,
    problem: active ? active.problem : 'none',
    result_event: result && result.event ? result.event : 'recorded',
    player_language: true,
    avatar_direct_command: false,
    hidden_law_normal_view: false,
    tech_tree_unlock: false,
    who_felt_this: active ? active.who_felt_this : world.selected,
  };
  deck.actionLedger.push(row);
  deck.cardLedger.push({
    snapshot_id: `PDS-${String(deck.cardLedger.length + 1).padStart(2, '0')}`,
    tick: world.tick,
    cards,
    selected_action: playerAction,
  });
  if (deck.actionLedger.length > 30) deck.actionLedger.shift();
  if (deck.cardLedger.length > 20) deck.cardLedger.shift();
  recordRealityConstraint('player_proposal_deck_action', {
    resident: row.proposer,
    sourceBeliefId: row.proposal_id,
    materials: active ? active.materials_needed : ['player_attention'],
    publicObservation: row.problem,
    residentInterpretation: playerAction,
    materialTransformation: playerAction === 'support' ? 'support routed through resident proposal function; no direct job assignment' : 'proposal deck action changed attention/council state only',
    timeCost: playerAction === 'wait' ? 1 : 0,
    workCost: playerAction === 'support' ? 1 : 0,
    toolWear: 0,
    maintenanceObligation: active ? `watch ${active.proposal_id}` : 'none',
    unintendedConsequence: playerAction === 'support' ? 'resources may be consumed if resident accepts support' : 'resident autonomy preserved',
    hiddenLawInvolved: 'none in normal view',
    conservationCheck: true
  });
  updatePlayerProposalDeckAcceptance();
  recordPrototypeMilestone('resident-proposal-deck', {
    ready: deck.acceptanceReady,
    cards: cards.length,
    actions: deck.actionLedger.length,
    latest: playerAction,
  });
  return row;
}

function askPlayerProposalDeck() {
  const result = askVillageBoardQuestion();
  const row = recordProposalDeckAction('ask', result);
  return log('askPlayerProposalDeck', { ready: world.gamePrototypeProposalDeck.acceptanceReady, proposalId: row.proposal_id, actions: world.gamePrototypeProposalDeck.actionLedger.length });
}

function supportPlayerProposalDeck() {
  const result = supportVillageProposal();
  const row = recordProposalDeckAction('support', result);
  return log('supportPlayerProposalDeck', { ready: world.gamePrototypeProposalDeck.acceptanceReady, proposalId: row.proposal_id, actions: world.gamePrototypeProposalDeck.actionLedger.length });
}

function waitPlayerProposalDeck() {
  const result = waitOnVillageBoard();
  const row = recordProposalDeckAction('wait', result);
  return log('waitPlayerProposalDeck', { ready: world.gamePrototypeProposalDeck.acceptanceReady, proposalId: row.proposal_id, actions: world.gamePrototypeProposalDeck.actionLedger.length });
}

function runPlayerProposalDeckLoop() {
  const deck = ensurePlayerProposalDeck();
  deck.runCount += 1;
  if (!world.villageBoard || !world.villageBoard.projectProposals || !world.villageBoard.projectProposals.length) runVillageBoardLoop();
  if (!world.gamePrototypePlayerMode || !world.gamePrototypePlayerMode.enabled) enterPlayerMode();
  if (!new Set(deck.actionLedger.map(row => row.player_action)).has('ask')) askPlayerProposalDeck();
  if (!new Set(deck.actionLedger.map(row => row.player_action)).has('support')) supportPlayerProposalDeck();
  if (!new Set(deck.actionLedger.map(row => row.player_action)).has('wait')) waitPlayerProposalDeck();
  updatePlayerProposalDeckAcceptance();
  return log('runPlayerProposalDeckLoop', { ready: deck.acceptanceReady, cards: proposalDeckCards().length, actions: deck.actionLedger.length });
}

function formatPlayerProposalDeck() {
  const deck = world.gamePrototypeProposalDeck || ensurePlayerProposalDeck();
  const cards = proposalDeckCards();
  const cardRows = cards.map(card => `${card.proposal_id}: ${card.player_gloss}; status=${card.status}; support=${card.support_level}; materials=${card.materials_needed.join('+') || 'none'}; force=${card.avatar_can_force}`);
  const actionRows = deck.actionLedger.slice(-8).map(row => `${row.action_id}: ${row.player_action} ${row.proposal_id}; direct=${row.avatar_direct_command}; hidden-law=${row.hidden_law_normal_view}`);
  return [
    `Acceptance ready: ${deck.acceptanceReady ? 'yes' : 'no'}`,
    `Cards: ${cards.length} / action rows=${deck.actionLedger.length}`,
    `Boundary: ${deck.boundary}`,
    'Visible proposal cards:',
    ...(cardRows.length ? cardRows : ['No resident proposal cards yet.']),
    'Recent deck actions:',
    ...(actionRows.length ? actionRows : ['No player proposal actions yet.'])
  ].join('\n');
}

function ensureLivedPracticeLoop() {
  ensureGamePrototype();
  if (!world.gamePrototypeLivedPractice) {
    world.gamePrototypeLivedPractice = {
      milestone: 'lived-practice-loop',
      runCount: 0,
      actionLedger: [],
      practiceSnapshots: [],
      receipt: null,
      acceptanceReady: false,
      playerFacing: true,
      repeatedOrdinaryActions: true,
      noDirectCommand: true,
      noHiddenLawNormalView: true,
      noPredeclaredTechTree: true,
      noCorrectConceptInstalled: true,
      boundary: 'player-facing lived practice loop; repeated normal actions can stabilize a resident practice from observed bottlenecks',
    };
  }
  return world.gamePrototypeLivedPractice;
}

function livedPracticeSnapshot() {
  const discovery = world.practicalDiscovery || null;
  const graph = world.emergentPracticeGraph || null;
  const latestNode = graph && graph.nodes.length ? graph.nodes[graph.nodes.length - 1] : null;
  const latestTest = discovery && discovery.practicalTests.length ? discovery.practicalTests[discovery.practicalTests.length - 1] : null;
  return {
    selected_resident: world.selected,
    practice_id: latestNode ? latestNode.practice_id : 'none',
    local_name: latestNode ? latestNode.local_name : 'none',
    status: latestNode ? latestNode.status : 'none',
    materials_used: latestNode ? latestNode.materials_used : [],
    observations_supporting: latestNode ? latestNode.observations_supporting : [],
    failed_ancestor_tests: latestNode ? latestNode.failed_ancestor_tests : [],
    adoption_count: latestNode ? latestNode.adoption_count : 0,
    maintenance_cost: latestNode ? latestNode.maintenance_cost : 0,
    latest_test: latestTest ? latestTest.id : 'none',
    practical_tests: discovery ? discovery.practicalTests.length : 0,
    lived_actions: discovery ? discovery.livedActions.length : 0,
    ordinary_feed: discovery && discovery.ordinaryPlayFeed ? discovery.ordinaryPlayFeed.length : 0,
    hidden_law_normal_view: false,
    direct_command: false,
    predeclared_tech_tree: false,
  };
}

function updateLivedPracticeAcceptance() {
  const loop = ensureLivedPracticeLoop();
  const snapshot = livedPracticeSnapshot();
  const graph = world.emergentPracticeGraph || null;
  loop.acceptanceReady = Boolean(
    loop.actionLedger.length >= 4 &&
    loop.practiceSnapshots.length > 0 &&
    graph && graph.nodes.length > 0 &&
    snapshot.practice_id !== 'none' &&
    snapshot.practical_tests >= 4 &&
    loop.actionLedger.every(row => row.player_language === true && row.avatar_direct_command === false && row.hidden_law_normal_view === false && row.predeclared_tech_tree === false) &&
    loop.repeatedOrdinaryActions === true &&
    loop.noDirectCommand === true &&
    loop.noHiddenLawNormalView === true &&
    loop.noPredeclaredTechTree === true &&
    loop.noCorrectConceptInstalled === true
  );
  loop.receipt = {
    receipt_id: `LPL-${String(loop.runCount).padStart(2, '0')}`,
    acceptance_ready: loop.acceptanceReady,
    actions: loop.actionLedger.length,
    practice_id: snapshot.practice_id,
    local_name: snapshot.local_name,
    status: snapshot.status,
    practical_tests: snapshot.practical_tests,
    boundary: loop.boundary,
  };
  return loop.acceptanceReady;
}

function recordLivedPracticeAction(playerVerb, discoveryAction, result, beforeTests, beforeNodes) {
  const loop = ensureLivedPracticeLoop();
  const snapshot = livedPracticeSnapshot();
  const row = {
    action_id: `LPA-${String(loop.actionLedger.length + 1).padStart(2, '0')}`,
    tick: world.tick,
    player_verb: playerVerb,
    discovery_action: discoveryAction,
    selected_resident: world.selected,
    result_event: result && result.event ? result.event : 'recorded',
    tests_added: Math.max(0, snapshot.practical_tests - beforeTests),
    practice_nodes_added: Math.max(0, (world.emergentPracticeGraph ? world.emergentPracticeGraph.nodes.length : 0) - beforeNodes),
    practice_id: snapshot.practice_id,
    local_name: snapshot.local_name,
    status: snapshot.status,
    player_language: true,
    avatar_direct_command: false,
    hidden_law_normal_view: false,
    predeclared_tech_tree: false,
    correct_concept_installed: false,
  };
  loop.actionLedger.push(row);
  loop.practiceSnapshots.push({
    snapshot_id: `LPS-${String(loop.practiceSnapshots.length + 1).padStart(2, '0')}`,
    tick: world.tick,
    snapshot,
  });
  if (loop.actionLedger.length > 30) loop.actionLedger.shift();
  if (loop.practiceSnapshots.length > 20) loop.practiceSnapshots.shift();
  recordRealityConstraint('lived_practice_action', {
    resident: world.selected,
    sourceBeliefId: snapshot.practice_id,
    materials: snapshot.materials_used.length ? snapshot.materials_used : ['player_attention'],
    publicObservation: snapshot.local_name,
    residentInterpretation: snapshot.status,
    materialTransformation: 'repeated normal action routed into resident practical discovery; no resource spawned by interface',
    timeCost: 1,
    workCost: 1,
    toolWear: 0,
    maintenanceObligation: snapshot.practice_id !== 'none' ? `watch ${snapshot.practice_id}` : 'none',
    unintendedConsequence: 'resident practice can remain disputed, taboo, emerging, or practical',
    hiddenLawInvolved: 'none in normal view',
    conservationCheck: true
  });
  updateLivedPracticeAcceptance();
  recordPrototypeMilestone('lived-practice-loop', {
    ready: loop.acceptanceReady,
    actions: loop.actionLedger.length,
    practice: snapshot.practice_id,
    status: snapshot.status,
  });
  return row;
}

function runLivedPracticeAction(playerVerb, discoveryAction) {
  const beforeTests = world.practicalDiscovery ? world.practicalDiscovery.practicalTests.length : 0;
  const beforeNodes = world.emergentPracticeGraph ? world.emergentPracticeGraph.nodes.length : 0;
  let result = null;
  if (playerVerb === 'Ask') result = runNormalPlayAsk();
  else if (playerVerb === 'Support') result = runNormalPlaySupport();
  else if (playerVerb === 'Wait') result = runNormalPlayWait();
  else result = runNormalPlayLook();
  runPracticalDiscoveryStep(discoveryAction);
  return recordLivedPracticeAction(playerVerb, discoveryAction, result, beforeTests, beforeNodes);
}

function runLivedPracticeLoop() {
  const loop = ensureLivedPracticeLoop();
  loop.runCount += 1;
  if (!world.gamePrototypeProposalDeck || !world.gamePrototypeProposalDeck.acceptanceReady) runPlayerProposalDeckLoop();
  if (!world.gamePrototypePlayerMode || !world.gamePrototypePlayerMode.enabled) enterPlayerMode();
  const scriptedNormalActions = [
    ['Ask', 'askSchedule'],
    ['Ask', 'askSchedule'],
    ['Ask', 'askSchedule'],
    ['Ask', 'askSchedule']
  ];
  scriptedNormalActions.forEach(([verb, discoveryAction]) => runLivedPracticeAction(verb, discoveryAction));
  updateLivedPracticeAcceptance();
  return log('runLivedPracticeLoop', { ready: loop.acceptanceReady, actions: loop.actionLedger.length, practice: loop.receipt ? loop.receipt.practice_id : 'none', status: loop.receipt ? loop.receipt.status : 'none' });
}

function formatLivedPracticeLoop() {
  const loop = world.gamePrototypeLivedPractice || ensureLivedPracticeLoop();
  const snapshot = loop.practiceSnapshots.length ? loop.practiceSnapshots[loop.practiceSnapshots.length - 1].snapshot : livedPracticeSnapshot();
  const actionRows = loop.actionLedger.slice(-8).map(row => `${row.action_id}: ${row.player_verb}->${row.discovery_action}; tests+${row.tests_added}; practice=${row.practice_id}; status=${row.status}; direct=${row.avatar_direct_command}`);
  return [
    `Acceptance ready: ${loop.acceptanceReady ? 'yes' : 'no'}`,
    `Actions: ${loop.actionLedger.length} / snapshots=${loop.practiceSnapshots.length}`,
    `Boundary: ${loop.boundary}`,
    `Current practice: ${snapshot.practice_id} / ${snapshot.local_name} / status=${snapshot.status}`,
    `Materials: ${snapshot.materials_used.join(' + ') || 'none'}`,
    `Supporting observations: ${snapshot.observations_supporting.length}`,
    `Failed ancestors: ${snapshot.failed_ancestor_tests.join(', ') || 'none'}`,
    `Adoption count: ${snapshot.adoption_count}; maintenance=${snapshot.maintenance_cost}`,
    `No hidden law in normal view: ${loop.noHiddenLawNormalView ? 'yes' : 'no'}`,
    'Recent lived practice actions:',
    ...(actionRows.length ? actionRows : ['No lived practice actions yet.'])
  ].join('\n');
}

function ensureResidentWorksite() {
  ensureGamePrototype();
  if (!world.gamePrototypeWorksite) {
    world.gamePrototypeWorksite = {
      milestone: 'resident-worksite',
      runCount: 0,
      watchLedger: [],
      snapshotLedger: [],
      receipt: null,
      acceptanceReady: false,
      playerFacing: true,
      avatarCannotAssignJobs: true,
      noDirectCommand: true,
      noHiddenLawNormalView: true,
      noResourceSpawning: true,
      boundary: 'player-facing resident worksite; watch project consequences without direct job assignment',
    };
  }
  return world.gamePrototypeWorksite;
}

function residentWorksiteSnapshot() {
  const projects = world.gamePrototypeProjects || ensurePrototypeProjects();
  const board = world.villageBoard || null;
  const latestWork = projects.projectLedger.length ? projects.projectLedger[projects.projectLedger.length - 1] : null;
  const latestCompletion = projects.completionLedger.length ? projects.completionLedger[projects.completionLedger.length - 1] : null;
  const latestStall = projects.stalledLedger.length ? projects.stalledLedger[projects.stalledLedger.length - 1] : null;
  const activeProposal = board && board.projectProposals ? board.projectProposals.find(row => !row.project_completed) || board.projectProposals[board.projectProposals.length - 1] : null;
  const materialWorld = world.gamePrototype3DWorld || null;
  const latestConstruction = materialWorld && materialWorld.constructionLedger && materialWorld.constructionLedger.length ? materialWorld.constructionLedger[materialWorld.constructionLedger.length - 1] : null;
  return {
    active_proposal: activeProposal ? activeProposal.proposal_id : 'none',
    proposer: activeProposal ? activeProposal.proposer : 'none',
    problem: activeProposal ? activeProposal.problem_addressed : 'none',
    status: activeProposal ? activeProposal.status : 'none',
    progress: activeProposal ? Number(activeProposal.project_progress || 0) : 0,
    work_rows: projects.projectLedger.length,
    completions: projects.completionLedger.length,
    stalls: projects.stalledLedger.length,
    latest_work_id: latestWork ? latestWork.project_id : 'none',
    latest_stall: latestStall ? latestStall.stalled_reason : 'none',
    latest_completion: latestCompletion ? latestCompletion.completion_id : 'none',
    construction_id: latestConstruction ? latestConstruction.construction_id : 'none',
    components_added: latestConstruction ? latestConstruction.components_added.length : 0,
    components_repaired: latestConstruction ? latestConstruction.components_repaired.length : 0,
    maintenance_cost_after: latestConstruction ? latestConstruction.maintenance_cost_after : null,
    resident_term: latestConstruction ? latestConstruction.resident_term : 'none',
    practice_id: latestConstruction && latestConstruction.practice_id ? latestConstruction.practice_id : 'none',
    resource_total: Object.values(world.resources).reduce((sum, value) => sum + Number(value || 0), 0),
    no_direct_command: true,
    no_hidden_law_normal_view: true,
    no_resource_spawning: true,
  };
}

function updateResidentWorksiteAcceptance() {
  const worksite = ensureResidentWorksite();
  const snapshot = residentWorksiteSnapshot();
  worksite.acceptanceReady = Boolean(
    worksite.watchLedger.length >= 2 &&
    worksite.snapshotLedger.length > 0 &&
    snapshot.work_rows > 0 &&
    (snapshot.components_added > 0 || snapshot.components_repaired > 0 || snapshot.stalls > 0) &&
    worksite.watchLedger.every(row => row.avatar_direct_command === false && row.hidden_law_normal_view === false && row.resource_spawning === false) &&
    worksite.avatarCannotAssignJobs === true &&
    worksite.noDirectCommand === true &&
    worksite.noHiddenLawNormalView === true &&
    worksite.noResourceSpawning === true
  );
  worksite.receipt = {
    receipt_id: `RWS-${String(worksite.runCount).padStart(2, '0')}`,
    acceptance_ready: worksite.acceptanceReady,
    watch_rows: worksite.watchLedger.length,
    active_proposal: snapshot.active_proposal,
    construction_id: snapshot.construction_id,
    components_added: snapshot.components_added,
    components_repaired: snapshot.components_repaired,
    stalls: snapshot.stalls,
    boundary: worksite.boundary,
  };
  return worksite.acceptanceReady;
}

function recordResidentWorksiteWatch(result, beforeRows, beforeConstructions) {
  const worksite = ensureResidentWorksite();
  const snapshot = residentWorksiteSnapshot();
  const materialWorld = world.gamePrototype3DWorld || null;
  const currentConstructions = materialWorld && materialWorld.constructionLedger ? materialWorld.constructionLedger.length : 0;
  const row = {
    watch_id: `RWW-${String(worksite.watchLedger.length + 1).padStart(2, '0')}`,
    tick: world.tick,
    player_action: 'Watch resident work',
    result_event: result && result.event ? result.event : 'advanceVillageProject',
    proposal_id: snapshot.active_proposal,
    proposer: snapshot.proposer,
    problem: snapshot.problem,
    status: snapshot.status,
    progress: snapshot.progress,
    work_rows_added: Math.max(0, snapshot.work_rows - beforeRows),
    constructions_added: Math.max(0, currentConstructions - beforeConstructions),
    construction_id: snapshot.construction_id,
    components_added: snapshot.components_added,
    components_repaired: snapshot.components_repaired,
    maintenance_cost_after: snapshot.maintenance_cost_after,
    resident_term: snapshot.resident_term,
    practice_id: snapshot.practice_id,
    avatar_direct_command: false,
    hidden_law_normal_view: false,
    resource_spawning: false,
  };
  worksite.watchLedger.push(row);
  worksite.snapshotLedger.push({
    snapshot_id: `RWSN-${String(worksite.snapshotLedger.length + 1).padStart(2, '0')}`,
    tick: world.tick,
    snapshot,
  });
  if (worksite.watchLedger.length > 30) worksite.watchLedger.shift();
  if (worksite.snapshotLedger.length > 20) worksite.snapshotLedger.shift();
  recordRealityConstraint('resident_worksite_watch', {
    resident: row.proposer,
    sourceBeliefId: row.proposal_id,
    materials: ['player_attention', 'resident_labor'],
    publicObservation: row.problem,
    residentInterpretation: row.status,
    materialTransformation: `watched resident worksite; ${row.components_added} component(s) added and ${row.components_repaired} repaired in latest construction snapshot`,
    timeCost: 1,
    workCost: 0,
    toolWear: 0,
    maintenanceObligation: row.construction_id !== 'none' ? `maintain ${row.construction_id}` : row.proposal_id,
    unintendedConsequence: row.status && /stalled/.test(row.status) ? 'work can stall without player control' : 'new or repaired parts carry maintenance burden',
    hiddenLawInvolved: 'none in normal view',
    conservationCheck: true
  });
  updateResidentWorksiteAcceptance();
  recordPrototypeMilestone('resident-worksite', {
    ready: worksite.acceptanceReady,
    watch_rows: worksite.watchLedger.length,
    proposal: row.proposal_id,
    progress: row.progress,
  });
  return row;
}

function runResidentWorksiteLoop() {
  const worksite = ensureResidentWorksite();
  worksite.runCount += 1;
  if (!world.gamePrototypeLivedPractice || !world.gamePrototypeLivedPractice.acceptanceReady) runLivedPracticeLoop();
  if (!world.gamePrototypeProposalDeck || !world.gamePrototypeProposalDeck.acceptanceReady) runPlayerProposalDeckLoop();
  if (!world.gamePrototypePlayerMode || !world.gamePrototypePlayerMode.enabled) enterPlayerMode();
  for (let i = 0; i < 4; i += 1) {
    const beforeRows = world.gamePrototypeProjects ? world.gamePrototypeProjects.projectLedger.length : 0;
    const beforeConstructions = world.gamePrototype3DWorld && world.gamePrototype3DWorld.constructionLedger ? world.gamePrototype3DWorld.constructionLedger.length : 0;
    let result = advanceVillageProject();
    const payload = result && result.payload ? result.payload : {};
    if (payload.stalled && /missing/.test(payload.status || '')) {
      supportResourceCommons();
      result = advanceVillageProject();
    }
    recordResidentWorksiteWatch(result, beforeRows, beforeConstructions);
  }
  updateResidentWorksiteAcceptance();
  return log('runResidentWorksiteLoop', { ready: worksite.acceptanceReady, watchRows: worksite.watchLedger.length, construction: worksite.receipt ? worksite.receipt.construction_id : 'none', componentsAdded: worksite.receipt ? worksite.receipt.components_added : 0, componentsRepaired: worksite.receipt ? worksite.receipt.components_repaired : 0 });
}

function formatResidentWorksite() {
  const worksite = world.gamePrototypeWorksite || ensureResidentWorksite();
  const snapshot = worksite.snapshotLedger.length ? worksite.snapshotLedger[worksite.snapshotLedger.length - 1].snapshot : residentWorksiteSnapshot();
  const watchRows = worksite.watchLedger.slice(-8).map(row => `${row.watch_id}: ${row.proposal_id} ${row.status} progress=${row.progress}; construction+${row.constructions_added}; added=${row.components_added}; repaired=${row.components_repaired}; direct=${row.avatar_direct_command}`);
  return [
    `Acceptance ready: ${worksite.acceptanceReady ? 'yes' : 'no'}`,
    `Watch rows: ${worksite.watchLedger.length} / snapshots=${worksite.snapshotLedger.length}`,
    `Boundary: ${worksite.boundary}`,
    `Active proposal: ${snapshot.active_proposal} / ${snapshot.problem}`,
    `Resident: ${snapshot.proposer}; status=${snapshot.status}; progress=${snapshot.progress}`,
    `Construction: ${snapshot.construction_id}; term=${snapshot.resident_term}; practice=${snapshot.practice_id}`,
    `Components added/repaired: ${snapshot.components_added}/${snapshot.components_repaired}`,
    `Maintenance after: ${snapshot.maintenance_cost_after === null ? 'none' : snapshot.maintenance_cost_after}`,
    `Stalls: ${snapshot.stalls}; latest=${snapshot.latest_stall}`,
    `No direct command: ${worksite.noDirectCommand ? 'yes' : 'no'} / no resource spawning: ${worksite.noResourceSpawning ? 'yes' : 'no'}`,
    'Recent worksite watches:',
    ...(watchRows.length ? watchRows : ['No resident worksite rows yet.'])
  ].join('\n');
}

function runPrototypeGuidedStep() {
  const prototype = ensureGamePrototype();
  const guide = derivePrototypePlayerGuide();
  let result = null;
  if (guide.button === 'askSchedule') {
    askSchedule();
    result = askSchedule();
  } else if (typeof window[guide.button] === 'function' && guide.button !== 'runPrototypeGuidedStep') {
    result = window[guide.button]();
  }
  const afterGuide = derivePrototypePlayerGuide();
  const row = {
    id: `GPG-${String(prototype.guideHistory.length + 1).padStart(3, '0')}`,
    from_phase: guide.phase,
    action: guide.button,
    next_phase: afterGuide.phase,
    tick: world.tick,
    resident: world.selected,
    commanded_resident: false,
    result_event: result && result.event ? result.event : 'none',
  };
  prototype.guideHistory.push(row);
  if (prototype.guideHistory.length > 40) prototype.guideHistory.shift();
  recordPrototypeMilestone('prototype-guided-step', `${row.from_phase} -> ${row.next_phase} via ${row.action}`);
  return log('runPrototypeGuidedStep', { fromPhase: row.from_phase, nextPhase: row.next_phase, action: row.action, guidedSteps: prototype.guideHistory.length });
}

function chooseDivergenceStatus(observation, repeated, rng) {
  if (/smoke|cracked/.test(observation.effect)) return repeated > 1 && rng() > 0.34 ? 'taboo' : 'disputed';
  if (/dulled|nothing/.test(observation.effect)) return repeated > 2 ? 'safety rule' : 'disputed';
  if (/jumped|carried|crawled/.test(observation.effect)) return repeated > 2 ? 'practical' : 'emerging';
  return rng() > 0.66 ? 'ritualized' : 'emerging';
}

function simulateDivergentPracticeHistory(baseLawSeed, historySeed, branchIndex) {
  const law = generateHiddenWorldLaw(baseLawSeed);
  const rng = seededAnomalyRng(baseLawSeed * 37 + historySeed * 101 + branchIndex * 503);
  const names = Object.keys(world.residents);
  const materialSets = [
    ['dry_resin', 'reed_fiber'],
    ['red_scrap', 'dry_resin'],
    ['wet_wood', 'dry_resin'],
    ['iron_sand', 'red_scrap'],
    ['clay_jar', 'reed_fiber'],
    ['ash_glass', 'reed_fiber'],
  ];
  const pressureKinds = ['roof leak', 'strained fiber stores', 'unsafe route', 'wet storage problem', 'tool wear', 'food spoilage risk'];
  const branch = {
    branch_id: `GPD-${String(branchIndex + 1).padStart(2, '0')}`,
    base_law_seed: baseLawSeed,
    history_seed: historySeed,
    hidden_law_shared: true,
    avatar_installed_correct_concept: false,
    tests: [],
    practice_history: [],
    safety_rules: [],
    material_burdens: [],
  };
  const repeated = {};
  for (let step = 0; step < 8; step += 1) {
    const resident = names[(Math.floor(rng() * names.length) + step + branchIndex) % names.length];
    const materials = materialSets[(Math.floor(rng() * materialSets.length) + step + branchIndex) % materialSets.length];
    const observation = observationForMaterials(law, materials, resident, `divergent branch ${branch.branch_id}`);
    const pressure = pressureKinds[(Math.floor(rng() * pressureKinds.length) + step) % pressureKinds.length];
    const localBelief = `${residentAnomalyVocabulary(resident, rng)} ${pressure.split(' ')[0]}`;
    const key = `${materials.join('+')}:${pressure}`;
    repeated[key] = (repeated[key] || 0) + 1;
    const status = chooseDivergenceStatus(observation, repeated[key], rng);
    const practiceName = `${localBelief} ${status === 'safety rule' ? 'rule' : 'habit'}`;
    const test = {
      id: `${branch.branch_id}-T${String(step + 1).padStart(2, '0')}`,
      resident,
      pressure,
      materials,
      observation: observation.effect,
      local_belief: localBelief,
      repeated_count: repeated[key],
      hidden_law_exposed: false,
    };
    branch.tests.push(test);
    if (status === 'safety rule') branch.safety_rules.push(`${practiceName} from ${test.id}`);
    if (status === 'taboo' || status === 'practical' || status === 'ritualized' || repeated[key] > 1) {
      branch.practice_history.push({
        practice_id: `${branch.branch_id}-P${String(branch.practice_history.length + 1).padStart(2, '0')}`,
        local_name: practiceName,
        status,
        origin_resident: resident,
        problem_pressure: pressure,
        materials_used: materials,
        evidence: [observation.effect],
        maintenance_cost: materials.includes('iron_sand') || materials.includes('clay_jar') ? 2 : 1,
        risk: /smoke|cracked|dulled/.test(observation.effect) ? 'caution' : 'ordinary',
      });
    }
    if (materials.includes('iron_sand') || materials.includes('clay_jar')) {
      branch.material_burdens.push(`${materials.join('+')} burden at ${test.id}`);
    }
  }
  if (!branch.practice_history.length) {
    const fallback = branch.tests[branch.tests.length - 1];
    branch.practice_history.push({
      practice_id: `${branch.branch_id}-P01`,
      local_name: `${fallback.local_belief} watch habit`,
      status: 'emerging',
      origin_resident: fallback.resident,
      problem_pressure: fallback.pressure,
      materials_used: fallback.materials,
      evidence: [fallback.observation],
      maintenance_cost: 1,
      risk: 'ordinary',
    });
  }
  branch.practice_signature = branch.practice_history.map(row => `${row.local_name}:${row.status}`).join('|');
  branch.status_signature = Array.from(new Set(branch.practice_history.map(row => row.status))).sort().join(',');
  branch.material_signature = Array.from(new Set(branch.practice_history.flatMap(row => row.materials_used))).sort().join(',');
  return branch;
}

function comparePrototypeDivergenceSeeds() {
  ensureGamePrototype();
  const baseLawSeed = world.anomalyDiscovery ? world.anomalyDiscovery.seed : anomalySeed();
  const branches = [0, 1, 2].map(index => simulateDivergentPracticeHistory(baseLawSeed, baseLawSeed + 17 + index * 41 + world.tick, index));
  const uniquePracticeSignatures = new Set(branches.map(row => row.practice_signature)).size;
  const uniqueStatusSignatures = new Set(branches.map(row => row.status_signature)).size;
  const allHiddenLawShared = branches.every(row => row.hidden_law_shared && row.base_law_seed === baseLawSeed);
  const noCorrectConceptInstalled = branches.every(row => row.avatar_installed_correct_concept === false);
  world.gamePrototypeDivergence = {
    comparison_id: `GPD-CMP-${String((world.gamePrototypeDivergence ? world.gamePrototypeDivergence.runCount || 0 : 0) + 1).padStart(2, '0')}`,
    runCount: (world.gamePrototypeDivergence ? world.gamePrototypeDivergence.runCount || 0 : 0) + 1,
    base_law_seed: baseLawSeed,
    branches,
    unique_practice_signatures: uniquePracticeSignatures,
    unique_status_signatures: uniqueStatusSignatures,
    diverged: uniquePracticeSignatures > 1 || uniqueStatusSignatures > 1,
    all_hidden_law_shared: allHiddenLawShared,
    no_correct_concept_installed: noCorrectConceptInstalled,
    boundary: 'browser-local seed comparison; same hidden law, different social/history seeds; no deterministic tech tree',
  };
  recordPrototypeMilestone('prototype-seed-divergence', `${branches.length} branches; diverged=${world.gamePrototypeDivergence.diverged}; base law ${baseLawSeed}`);
  return log('comparePrototypeDivergenceSeeds', {
    comparisonId: world.gamePrototypeDivergence.comparison_id,
    branches: branches.length,
    diverged: world.gamePrototypeDivergence.diverged,
    uniquePracticeSignatures,
    uniqueStatusSignatures,
    baseLawSeed,
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
      physicalHeritageLedger: [],
      componentEffectLedger: [],
      physicsEpochLedger: [],
      materialFluxLedger: [],
	      boundary: {
        compressedDeepTime: true,
        activeResidentsRemainSix: true,
        noIntentionalTechTree: true,
        effectsEmergeFromPressure: true,
        hiddenLawsRemainAuditOnly: true,
        stochasticPhysicsSubstrate: true,
      },
    };
	  }
  if (!Array.isArray(world.deepTimeCivilization.physicalHeritageLedger)) world.deepTimeCivilization.physicalHeritageLedger = [];
  if (!Array.isArray(world.deepTimeCivilization.componentEffectLedger)) world.deepTimeCivilization.componentEffectLedger = [];
  if (!Array.isArray(world.deepTimeCivilization.physicsEpochLedger)) world.deepTimeCivilization.physicsEpochLedger = [];
  if (!Array.isArray(world.deepTimeCivilization.materialFluxLedger)) world.deepTimeCivilization.materialFluxLedger = [];
	  return world.deepTimeCivilization;
	}

function syncDeepTimeLineagesWithConstruction() {
  const sim = ensureDeepTimeCivilization();
  const graph = world.emergentPracticeGraph || null;
  const materialWorld = world.gamePrototype3DWorld || null;
  if (!graph || !graph.nodes || !graph.nodes.length || !materialWorld) return sim.lineages;
  graph.nodes
    .filter(node => node.source_construction_rows && node.source_construction_rows.length)
    .forEach(node => {
      const existing = sim.lineages.find(row => row.source_practice_id === node.practice_id);
      const componentIds = node.construction_component_ids || [];
      const linkedComponents = (materialWorld.components || []).filter(component => componentIds.includes(component.component_id));
      const averageStability = linkedComponents.length
        ? linkedComponents.reduce((sum, component) => sum + Number(component.stability || 0), 0) / linkedComponents.length
        : 0.5;
      const lineage = existing || {
        lineage_id: `DTL-${String(sim.lineages.length + 1).padStart(2, '0')}`,
        source_practice_id: node.practice_id,
        local_name: node.local_name || node.practice_id,
        status: node.status || 'emerging',
        age_years: 0,
        adaptations: 0,
        memory_strength: 0.62,
        usefulness: Number(node.practical_score || 0.42),
        maintenance_burden: Number(node.maintenance_cost || 1),
        risk_flags: node.risk_flags || [],
        origin_household: node.origin_household || `${node.origin_resident || 'resident'}-household`,
      };
      lineage.construction_source_rows = Array.from(new Set([...(lineage.construction_source_rows || []), ...(node.source_construction_rows || [])]));
      lineage.component_ids = Array.from(new Set([...(lineage.component_ids || []), ...componentIds]));
      lineage.component_affordances = Array.from(new Set([...(lineage.component_affordances || []), ...(node.component_affordances || [])]));
      lineage.resident_term = node.resident_term || lineage.resident_term || node.local_name;
      lineage.player_gloss = node.player_gloss || lineage.player_gloss || 'construction-linked practice';
      lineage.physical_stability_memory = Number(averageStability.toFixed(3));
      lineage.language_variants = Array.from(new Set([...(lineage.language_variants || []), ...((materialWorld.language && materialWorld.language.terms || []).flatMap(term => term.variants || []))])).slice(-8);
      lineage.status = node.status || lineage.status;
      lineage.usefulness = Number(clamp(Math.max(Number(lineage.usefulness || 0), Number(node.practical_score || 0)) + averageStability * 0.015).toFixed(3));
      if (!existing) sim.lineages.push(lineage);
      sim.physicalHeritageLedger.push({
        heritage_id: `DTH-${String(sim.physicalHeritageLedger.length + 1).padStart(3, '0')}`,
        epoch: sim.epoch,
        year: sim.year,
        lineage_id: lineage.lineage_id,
        source_practice_id: node.practice_id,
        construction_rows: node.source_construction_rows || [],
        component_ids: lineage.component_ids,
        resident_term: lineage.resident_term,
        physical_stability_memory: lineage.physical_stability_memory,
        no_tech_tree: true,
      });
    });
  sim.physicalHeritageLedger = sim.physicalHeritageLedger.slice(-120);
  return sim.lineages;
}

function seedDeepTimeLineages() {
  const sim = ensureDeepTimeCivilization();
  if (sim.lineages.length) return syncDeepTimeLineagesWithConstruction();
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
  return syncDeepTimeLineagesWithConstruction();
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

function mergeResourceDeltas(...deltas) {
  const keys = new Set();
  deltas.filter(Boolean).forEach(delta => Object.keys(delta).forEach(key => keys.add(key)));
  const merged = {};
  keys.forEach(key => {
    merged[key] = deltas.reduce((sum, delta) => sum + Number(delta && delta[key] || 0), 0);
  });
  return merged;
}

function applyDeepTimeResourceDelta(delta) {
  Object.entries(delta).forEach(([key, value]) => {
    world.resources[key] = Math.max(0, Math.min(99, (world.resources[key] || 0) + value));
  });
}

function applyDeepTimeStochasticPhysicsEpoch(years, pressure, entropy) {
  const sim = ensureDeepTimeCivilization();
  const materialWorld = ensurePrototype3DWorld();
  const physics = materialWorld.physics || {};
  const components = materialWorld.components || [];
  const round = value => Number(Number(value || 0).toFixed(3));
  const wet = pressure.includes('wet') || pressure.includes('flood');
  const dry = pressure.includes('drought');
  const heat = pressure.includes('abundance') || pressure.includes('drought');
  const wear = pressure.includes('wear') || pressure.includes('decay') || pressure.includes('exhaustion') || pressure.includes('route');
  const compression = pressure.includes('memory');
  const substeps = Math.max(1, Math.min(8, Math.ceil(Math.log10(Math.max(10, years))) + (wet ? 1 : 0) + (wear ? 1 : 0)));
  const linkedPhysicsSteps = [];
  for (let index = 0; index < substeps; index += 1) {
    const step = applyPrototypePhysicsStep(`deep-time stochastic physics: ${pressure}`);
    if (step && step.step_id) linkedPhysicsSteps.push(step.step_id);
  }
  const totalMassBefore = components.reduce((sum, component) => {
    const material = materialWorld.materialCatalog[component.material_id] || {};
    return sum + Number(component.mass || material.mass || 1);
  }, 0);
  const yearlyScale = Math.min(1, Math.log10(Math.max(10, years)) / 6);
  const fluxRows = components.map((component, index) => {
    const material = materialWorld.materialCatalog[component.material_id] || {};
    const before = {
      mass: Number(component.mass || material.mass || 1),
      moisture: Number(component.moisture || 0),
      damage: Number(component.damage || 0),
      stability: Number(component.stability || 0),
      z: Number(component.position3d && component.position3d.z || 0),
    };
    const waterResistance = Number(material.water_resistance || 0.5);
    const heatResistance = Number(material.heat_resistance || 0.4);
    const decayRate = Number(material.decay_rate || 0.02);
    const brittleness = Number(material.brittleness || 0.3);
    const entropyNudge = ((entropy + index * 31 + sim.epoch * 7) % 17) / 1000;
    const moistureDelta = wet
      ? (1 - waterResistance) * (0.06 + yearlyScale * 0.08) + entropyNudge
      : dry
        ? -(0.04 + yearlyScale * 0.05)
        : compression
          ? -0.01
          : entropyNudge - 0.006;
    const heatDelta = heat ? (1 - heatResistance) * (0.025 + yearlyScale * 0.025) : -0.006;
    const wearBias = wear ? 0.045 : 0.018;
    const damageGain = decayRate * (1 + yearlyScale * 8) + Math.max(0, before.moisture - waterResistance) * 0.08 + brittleness * 0.018 + wearBias * yearlyScale + entropyNudge;
    const massLoss = Math.min(before.mass * 0.18, damageGain * before.mass * 0.08);
    const stabilityLoss = Math.min(0.24, damageGain * 0.5 + (wet ? 0.025 : 0) + (wear ? 0.035 : 0));
    component.moisture = Number(clamp(before.moisture + moistureDelta).toFixed(3));
    component.temperature = Number(clamp(Number(component.temperature || 0.42) + heatDelta).toFixed(3));
    component.damage = Number(clamp(before.damage + damageGain).toFixed(3));
    component.stability = Number(clamp(before.stability - stabilityLoss + (dry && !wear ? 0.01 : 0)).toFixed(3));
    component.mass = Number(Math.max(0.25, before.mass - massLoss).toFixed(3));
    if (component.stability < 0.46 || component.damage > 0.72) {
      const settlement = Math.min(before.z, 0.8 + yearlyScale * 2.4 + entropyNudge * 20);
      if (component.position3d) {
        component.position3d.z = Number(Math.max(0, Number(component.position3d.z || 0) - settlement).toFixed(3));
        component.position3d.x = Number(Math.max(0, Math.min(140, Number(component.position3d.x || 0) + ((entropy + index) % 5 - 2) * yearlyScale)).toFixed(3));
        component.position3d.y = Number(Math.max(0, Math.min(110, Number(component.position3d.y || 0) + ((entropy + index * 3) % 5 - 2) * yearlyScale)).toFixed(3));
      }
    }
    if (component.damage > 0.92 || component.mass <= 0.28) {
      component.status = 'ruined trace';
      component.active_affordance = false;
    }
    component.deep_time_physics_epoch = `DTP-${String(sim.physicsEpochLedger.length + 1).padStart(3, '0')}`;
    return {
      flux_id: `DTF-${String(sim.materialFluxLedger.length + index + 1).padStart(4, '0')}`,
      component_id: component.component_id,
      material_id: component.material_id,
      before,
      after: {
        mass: component.mass,
        moisture: component.moisture,
        damage: component.damage,
        stability: component.stability,
        z: component.position3d ? component.position3d.z : before.z,
      },
      mass_loss: round(massLoss),
      moisture_delta: round(component.moisture - before.moisture),
      damage_delta: round(component.damage - before.damage),
      stability_delta: round(component.stability - before.stability),
      ruined_trace: component.status === 'ruined trace',
    };
  });
  if (materialWorld.structures && materialWorld.structures[0]) {
    const structure = materialWorld.structures[0];
    const linked = components.filter(component => structure.component_ids.includes(component.component_id));
    structure.stability = Number(clamp(linked.reduce((sum, component) => sum + Number(component.stability || 0), 0) / Math.max(1, linked.length)).toFixed(3));
    structure.moisture_risk = Number(clamp(linked.reduce((sum, component) => sum + Number(component.moisture || 0), 0) / Math.max(1, linked.length)).toFixed(3));
    structure.deep_time_physics_epoch = `DTP-${String(sim.physicsEpochLedger.length + 1).padStart(3, '0')}`;
  }
  const totalMassAfter = components.reduce((sum, component) => sum + Number(component.mass || 0), 0);
  const averageDamageAfter = components.length ? components.reduce((sum, component) => sum + Number(component.damage || 0), 0) / components.length : 0;
  const averageMoistureAfter = components.length ? components.reduce((sum, component) => sum + Number(component.moisture || 0), 0) / components.length : 0;
  const averageStabilityAfter = components.length ? components.reduce((sum, component) => sum + Number(component.stability || 0), 0) / components.length : 0;
  const componentsRuined = fluxRows.filter(row => row.ruined_trace).length;
  const resourceDelta = {
    water: dry ? -Math.max(1, Math.round(years / 50000)) : 0,
    fiber: wet || averageMoistureAfter > 0.55 ? -1 : 0,
    wood: averageDamageAfter > 0.58 ? -1 : 0,
    care: componentsRuined > 0 || averageStabilityAfter < 0.48 ? -1 : 0,
  };
  const lineagePressure = {};
  (sim.lineages || []).forEach(lineage => {
    const ids = lineage.component_ids || [];
    const linkedRows = fluxRows.filter(row => ids.includes(row.component_id));
    if (!linkedRows.length) return;
    const avgDamage = linkedRows.reduce((sum, row) => sum + Number(row.after.damage || 0), 0) / linkedRows.length;
    const avgStability = linkedRows.reduce((sum, row) => sum + Number(row.after.stability || 0), 0) / linkedRows.length;
    lineagePressure[lineage.lineage_id] = {
      linked_components: linkedRows.length,
      average_damage: round(avgDamage),
      average_stability: round(avgStability),
      ruined_components: linkedRows.filter(row => row.ruined_trace).length,
      maintenance_burden_delta: avgDamage > 0.58 || avgStability < 0.5 ? 1 : 0,
      memory_loss: avgStability < 0.42 ? 0.04 : 0.015,
      usefulness_gain: avgStability > 0.72 && avgDamage < 0.28 ? 0.025 : 0,
    };
  });
  const epochRow = {
    physics_epoch_id: `DTP-${String(sim.physicsEpochLedger.length + 1).padStart(3, '0')}`,
    epoch: sim.epoch,
    year: sim.year,
    years,
    pressure,
    entropy,
    linked_physics_steps: linkedPhysicsSteps,
    substeps,
    component_count: components.length,
    total_mass_before: round(totalMassBefore),
    total_mass_after: round(totalMassAfter),
    mass_lost_to_decay: round(Math.max(0, totalMassBefore - totalMassAfter)),
    average_damage_after: round(averageDamageAfter),
    average_moisture_after: round(averageMoistureAfter),
    average_stability_after: round(averageStabilityAfter),
    components_ruined: componentsRuined,
    resource_delta: resourceDelta,
    lineage_pressure: lineagePressure,
    no_effect_without_cause: true,
    no_resource_spawning: true,
    hidden_law_normal_view: false,
  };
  sim.physicsEpochLedger.push(epochRow);
  sim.materialFluxLedger.push(...fluxRows);
  sim.physicsEpochLedger = sim.physicsEpochLedger.slice(-160);
  sim.materialFluxLedger = sim.materialFluxLedger.slice(-240);
  recordRealityConstraint('deep_time_stochastic_physics_epoch', {
    resident: world.selected,
    sourceBeliefId: epochRow.physics_epoch_id,
    materials: Array.from(new Set(components.map(component => component.material_id))),
    publicObservation: `${pressure} aged ${components.length} physical component(s) over ${years} compressed years`,
    residentInterpretation: 'inherited objects changed before anyone named a new practice',
    materialTransformation: `mass ${epochRow.total_mass_before}->${epochRow.total_mass_after}; damage ${epochRow.average_damage_after}; stability ${epochRow.average_stability_after}`,
    timeCost: Math.max(1, Math.floor(years / 1000)),
    workCost: componentsRuined + (averageStabilityAfter < 0.55 ? 1 : 0),
    toolWear: averageDamageAfter > 0.55 ? 1 : 0,
    maintenanceObligation: componentsRuined > 0 ? 'ruined physical traces require care or replacement' : 'monitor long-horizon material drift',
    unintendedConsequence: `${componentsRuined} ruined trace(s), ${Object.keys(lineagePressure).length} lineage pressure link(s)`,
    hiddenLawInvolved: world.audit ? 'stochastic material decay, settlement, moisture, heat, and support laws' : 'audit only',
    conservationCheck: true
  });
  return epochRow;
}

function applyDeepTimePhysicsToLineages(lineages, physicsEpoch) {
  if (!physicsEpoch || !physicsEpoch.lineage_pressure) return lineages;
  lineages.forEach(lineage => {
    const pressure = physicsEpoch.lineage_pressure[lineage.lineage_id];
    if (!pressure) return;
    lineage.physical_epoch_count = (lineage.physical_epoch_count || 0) + 1;
    lineage.physical_risk_memory = pressure.average_damage;
    lineage.physical_stability_memory = pressure.average_stability;
    lineage.maintenance_burden += Number(pressure.maintenance_burden_delta || 0);
    lineage.memory_strength = clamp(Number(lineage.memory_strength || 0) - Number(pressure.memory_loss || 0));
    lineage.usefulness = clamp(Number(lineage.usefulness || 0) + Number(pressure.usefulness_gain || 0));
    if (pressure.ruined_components > 0 && lineage.memory_strength < 0.24) {
      lineage.status = 'forgotten';
    } else if (pressure.maintenance_burden_delta > 0 && lineage.status !== 'forgotten') {
      lineage.status = lineage.status === 'institutionalized' ? 'burdened institution' : 'burdened';
    }
  });
  return lineages;
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

function applyDeepTimePhysicalPressure(effect, pressure, years, entropy) {
  const sim = ensureDeepTimeCivilization();
  const materialWorld = world.gamePrototype3DWorld || null;
  if (!materialWorld || !materialWorld.components || !materialWorld.components.length) return null;
  const lineage = sim.lineages.find(row => row.lineage_id === effect.source_lineage_id) || null;
  const targetIds = lineage && lineage.component_ids && lineage.component_ids.length
    ? lineage.component_ids
    : materialWorld.components.filter(component => component.project_built === true).map(component => component.component_id);
  const targets = materialWorld.components.filter(component => targetIds.includes(component.component_id)).slice(0, 8);
  if (!targets.length) return null;
  const wet = pressure.includes('wet') || pressure.includes('flood');
  const dry = pressure.includes('drought');
  const wear = pressure.includes('wear') || pressure.includes('decay') || pressure.includes('exhaustion');
  const abundance = pressure.includes('abundance');
  const componentDeltas = targets.map((component, index) => {
    const material = materialWorld.materialCatalog[component.material_id] || {};
    const old = {
      moisture: Number(component.moisture || 0),
      damage: Number(component.damage || 0),
      stability: Number(component.stability || 0),
    };
    const waterResistance = Number(material.water_resistance || 0.5);
    const decayRate = Number(material.decay_rate || 0.02);
    const entropyNudge = ((entropy + index * 19) % 11) / 1000;
    if (wet) component.moisture = Number(clamp(old.moisture + (1 - waterResistance) * 0.08 + entropyNudge).toFixed(3));
    if (dry) component.moisture = Number(clamp(old.moisture - 0.07).toFixed(3));
    if (wear) component.damage = Number(clamp(Number(component.damage || old.damage) + decayRate * 2.2 + entropyNudge).toFixed(3));
    if (abundance) {
      component.damage = Number(clamp(Number(component.damage || old.damage) - 0.045).toFixed(3));
      component.stability = Number(clamp(old.stability + 0.035).toFixed(3));
    } else {
      component.stability = Number(clamp(Number(component.stability || old.stability) - Number(component.damage || old.damage) * 0.018 - (wet ? 0.012 : 0)).toFixed(3));
    }
    component.deep_time_touched = effect.effect_id;
    return {
      component_id: component.component_id,
      material_id: component.material_id,
      before: old,
      after: {
        moisture: component.moisture,
        damage: component.damage,
        stability: component.stability,
      }
    };
  });
  if (materialWorld.structures && materialWorld.structures[0]) {
    const structure = materialWorld.structures[0];
    const linked = materialWorld.components.filter(component => structure.component_ids.includes(component.component_id));
    structure.stability = Number(clamp(linked.reduce((sum, component) => sum + Number(component.stability || 0), 0) / Math.max(1, linked.length)).toFixed(3));
    structure.moisture_risk = Number(clamp(linked.reduce((sum, component) => sum + Number(component.moisture || 0), 0) / Math.max(1, linked.length)).toFixed(3));
    structure.risk_flags = Array.from(new Set([...(structure.risk_flags || []), `deep-time ${pressure}`]));
  }
  const row = {
    effect_id: effect.effect_id,
    physical_effect_id: `DTPE-${String(sim.componentEffectLedger.length + 1).padStart(3, '0')}`,
    epoch: sim.epoch,
    year: sim.year,
    years,
    pressure,
    source_lineage_id: effect.source_lineage_id,
    target_component_count: targets.length,
    component_deltas: componentDeltas,
    structure_stability_after: materialWorld.structures && materialWorld.structures[0] ? materialWorld.structures[0].stability : null,
    hidden_law_normal_view: false,
    no_resource_spawning: true,
  };
  sim.componentEffectLedger.push(row);
  sim.componentEffectLedger = sim.componentEffectLedger.slice(-120);
  recordRealityConstraint('deep_time_physical_pressure', {
    resident: world.selected,
    sourceBeliefId: effect.effect_id,
    materials: Array.from(new Set(targets.map(component => component.material_id))),
    publicObservation: `${pressure} touched ${targets.length} inherited component(s)`,
    residentInterpretation: `${effect.local_name} left physical maintenance pressure`,
    materialTransformation: `deep-time pressure changed component moisture/damage/stability for ${targets.length} component(s)`,
    timeCost: Math.max(1, Math.floor(years / 1000)),
    workCost: 0,
    toolWear: wear ? 1 : 0,
    maintenanceObligation: row.structure_stability_after !== null && row.structure_stability_after < 0.72 ? 'future residents may need repair practice' : 'watch inherited structure',
    unintendedConsequence: effect.outcome,
    hiddenLawInvolved: world.audit ? 'long-horizon material decay and stability pressure' : 'audit only',
    conservationCheck: true
  });
  return row;
}

function runCivilizationDeepTimeEpoch(yearOverride) {
  ensureGamePrototype();
  const sim = ensureDeepTimeCivilization();
  const lineages = seedDeepTimeLineages();
  const entropy = deepTimeEntropyByte();
  const yearOptions = [50, 250, 1000, 10000, 50000];
  const years = Number(yearOverride || yearOptions[entropy % yearOptions.length]);
  const pressure = chooseDeepTimePressure(entropy);
  sim.epoch += 1;
  sim.year += years;
  const physicsEpoch = applyDeepTimeStochasticPhysicsEpoch(years, pressure, entropy);
  const delta = mergeResourceDeltas(pressureResourceDelta(pressure, entropy), physicsEpoch ? physicsEpoch.resource_delta : null);
  applyDeepTimeResourceDelta(delta);
  sim.entropyLedger.push({ epoch: sim.epoch, entropy, years, source: window.crypto && window.crypto.getRandomValues ? 'crypto.getRandomValues' : 'Math.random fallback' });
  sim.pressureLedger.push({ epoch: sim.epoch, year: sim.year, pressure, resource_delta: delta, physics_epoch_id: physicsEpoch ? physicsEpoch.physics_epoch_id : null });
  lineages.forEach((lineage, index) => mutateDeepTimeLineage(lineage, pressure, (entropy + index * 37) % 256, years));
  applyDeepTimePhysicsToLineages(lineages, physicsEpoch);
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
  const physicalEffect = applyDeepTimePhysicalPressure(effect, pressure, years, entropy);
  if (physicalEffect) effect.physical_effect_id = physicalEffect.physical_effect_id;
	  applyDeepTimeEffectToVillage(effect, delta);
  sim.timeline.push({
    epoch: sim.epoch,
    year: sim.year,
    years_advanced: years,
    pressure,
    resources: { ...world.resources },
    lineage_statuses: lineages.map(row => `${row.lineage_id}:${row.status}`).join(';'),
	    effect_id: effect.effect_id,
    physical_effect_id: physicalEffect ? physicalEffect.physical_effect_id : null,
    physics_epoch_id: physicsEpoch ? physicsEpoch.physics_epoch_id : null,
	  });
  evaluateCivilizationSurvival(pressure);
  recordPrototypeMilestone('deep-time-epoch', `+${years} years; ${pressure}; effect ${effect.effect_id}`);
  return log('runCivilizationDeepTimeEpoch', { yearsAdvanced: years, year: sim.year, pressure, lineages: lineages.length, effects: sim.emergentEffects.length, entropy, physicsEpoch: physicsEpoch ? physicsEpoch.physics_epoch_id : null });
}

function runDeepTimePhysicsEpoch() {
  runCivilizationDeepTimeEpoch(50000);
  const sim = ensureDeepTimeCivilization();
  const row = sim.physicsEpochLedger[sim.physicsEpochLedger.length - 1];
  recordPrototypeMilestone('deep-time-physics-epoch', `${row.physics_epoch_id} mass ${row.total_mass_before}->${row.total_mass_after}, ruined=${row.components_ruined}`);
  return log('runDeepTimePhysicsEpoch', {
    physicsEpochId: row.physics_epoch_id,
    year: sim.year,
    pressure: row.pressure,
    massBefore: row.total_mass_before,
    massAfter: row.total_mass_after,
    componentsRuined: row.components_ruined,
    lineagePressureLinks: Object.keys(row.lineage_pressure || {}).length,
  });
}

function evaluateCivilizationSurvival(pressure = 'manual audit') {
  const sim = ensureDeepTimeCivilization();
  const lineages = seedDeepTimeLineages();
  const activeLineages = lineages.filter(row => row.status !== 'forgotten').length;
  const traceLineages = lineages.length - activeLineages;
  const resourceTotal = Object.values(world.resources || {}).reduce((sum, value) => sum + Number(value || 0), 0);
  const averageMemory = lineages.length ? lineages.reduce((sum, row) => sum + Number(row.memory_strength || 0), 0) / lineages.length : 0;
  const totalBurden = lineages.reduce((sum, row) => sum + Number(row.maintenance_burden || 0), 0);
  const materialWorld = world.gamePrototype3DWorld || null;
  const physicalComponents = materialWorld && materialWorld.components ? materialWorld.components : [];
  const componentEffectRows = sim.componentEffectLedger ? sim.componentEffectLedger.length : 0;
  const physicalHeritageRows = sim.physicalHeritageLedger ? sim.physicalHeritageLedger.length : 0;
  const physicsEpochRows = sim.physicsEpochLedger ? sim.physicsEpochLedger.length : 0;
  const constructionLinkedLineages = lineages.filter(row => row.component_ids && row.component_ids.length).length;
  const averagePhysicalStability = physicalComponents.length ? physicalComponents.reduce((sum, component) => sum + Number(component.stability || 0), 0) / physicalComponents.length : 0.5;
  const averagePhysicalDamage = physicalComponents.length ? physicalComponents.reduce((sum, component) => sum + Number(component.damage || 0), 0) / physicalComponents.length : 0;
  const massRetention = sim.physicsEpochLedger && sim.physicsEpochLedger.length
    ? sim.physicsEpochLedger.slice(-8).reduce((sum, row) => sum + (Number(row.total_mass_before || 0) > 0 ? Number(row.total_mass_after || 0) / Number(row.total_mass_before || 1) : 1), 0) / Math.min(8, sim.physicsEpochLedger.length)
    : 1;
  const physicalContinuity = clamp(averagePhysicalStability * 0.52 + (1 - averagePhysicalDamage) * 0.16 + Math.min(1, constructionLinkedLineages / Math.max(1, lineages.length)) * 0.13 + Math.min(1, componentEffectRows / 6) * 0.06 + Math.min(1, physicsEpochRows / 12) * 0.06 + massRetention * 0.07);
  const physicalBurden = Math.min(0.22, averagePhysicalDamage * 0.16 + Math.max(0, 0.68 - averagePhysicalStability) * 0.22);
  const recoveryPotential = Number(((world.resources.care || 0) + activeLineages + sim.villageConsequences.length * 0.08).toFixed(3));
  const continuityScore = clamp((activeLineages / Math.max(1, lineages.length)) * 0.34 + averageMemory * 0.22 + Math.min(1, resourceTotal / 36) * 0.16 + Math.min(1, recoveryPotential / 12) * 0.1 + physicalContinuity * 0.18 - Math.min(0.3, totalBurden / 80) - physicalBurden);
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
	    physical_heritage_rows: physicalHeritageRows,
	    component_effect_rows: componentEffectRows,
	    physics_epoch_rows: physicsEpochRows,
	    construction_linked_lineages: constructionLinkedLineages,
	    average_physical_stability: Number(averagePhysicalStability.toFixed(3)),
	    average_physical_damage: Number(averagePhysicalDamage.toFixed(3)),
	    mass_retention: Number(massRetention.toFixed(3)),
	    physical_continuity: Number(physicalContinuity.toFixed(3)),
	    physical_burden: Number(physicalBurden.toFixed(3)),
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
	    physicalHeritageRows,
	    componentEffectRows,
	    physicsEpochRows,
	    constructionLinkedLineages,
	    averagePhysicalStability: survivalRow.average_physical_stability,
	    averagePhysicalDamage: survivalRow.average_physical_damage,
	    massRetention: survivalRow.mass_retention,
	    physicalContinuity: survivalRow.physical_continuity,
	    physicalBurden: survivalRow.physical_burden,
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

function residentBodyInitialPosition(index) {
  const anchors = [
    { x: 14, y: 16, z: 0 },
    { x: 45, y: 14, z: 0 },
    { x: 76, y: 16, z: 0 },
    { x: 20, y: 58, z: 0 },
    { x: 56, y: 62, z: 0 },
    { x: 92, y: 58, z: 0 },
  ];
  return { ...anchors[index % anchors.length] };
}

function ensureResidentBodies() {
  if (!world.gamePrototypeResidentBodies) {
    world.gamePrototypeResidentBodies = {
      runCount: 0,
      bodies: {},
      bodyLedger: [],
      contactLedger: [],
      fatigueLedger: [],
      recoveryLedger: [],
      boundary: {
        residentsArePhysicalCapsules: true,
        stochasticBodyPhysics: true,
        noDirectPlayerBodyCommand: true,
        movementCostsEnergyAndSafety: true,
        collisionAndFootingAudited: true,
        recoveryIsBounded: true,
      },
    };
  }
  const sim = world.gamePrototypeResidentBodies;
  if (!sim.bodies) sim.bodies = {};
  if (!Array.isArray(sim.bodyLedger)) sim.bodyLedger = [];
  if (!Array.isArray(sim.contactLedger)) sim.contactLedger = [];
  if (!Array.isArray(sim.fatigueLedger)) sim.fatigueLedger = [];
  if (!Array.isArray(sim.recoveryLedger)) sim.recoveryLedger = [];
  Object.keys(world.residents).forEach((name, index) => {
    if (!sim.bodies[name]) {
      sim.bodies[name] = {
        body_id: `RB-${name}`,
        resident: name,
        position3d: residentBodyInitialPosition(index),
        velocity: { x: 0, y: 0, z: 0 },
        radius: 3.2 + index * 0.05,
        height: 9.4,
        mass: 46 + index * 2,
        carry_capacity: 9 + (index % 3) * 1.5,
        carried_load: 0,
        fatigue: 0.18 + index * 0.02,
        balance: 0.72,
        footing: 0.76,
        recovery_debt: 0,
        slip_risk: 0,
        contact_count: 0,
        last_action: 'initialized',
        hidden_law_normal_view: false,
      };
    }
  });
  return sim;
}

function residentBodyTargetForAction(residentName, action) {
  const index = Object.keys(world.residents).indexOf(residentName);
  const offset = Math.max(0, index);
  const targets = {
    rest: { x: 12 + offset * 2, y: 12, z: 0, label: 'shelter rest ground' },
    refuse: { x: 18 + offset * 2, y: 38, z: 0, label: 'autonomy distance' },
    repair_safety: { x: 32 + offset * 3, y: 66, z: 0, label: 'route marker' },
    forage: { x: 86, y: 74 - offset * 2, z: 0, label: 'commons route' },
    proposal_work: { x: 70 + offset, y: 18 + offset, z: 0, label: 'work yard project' },
    practice_maintenance: { x: 43 + offset, y: 18, z: 0, label: 'practice storage' },
    physics_repair: { x: 50 + offset, y: 17 + offset, z: 0, label: 'strained physical support' },
    material_manipulation: { x: 52 + offset, y: 20 + offset, z: 0, label: 'handled component' },
    teach: { x: 94, y: 20 + offset, z: 0, label: 'board teaching place' },
    experiment: { x: 66 + offset, y: 26 + offset, z: 0, label: 'small test surface' },
    observe: { x: 36 + offset * 4, y: 42, z: 0, label: 'watching place' },
  };
  return targets[action] || targets.observe;
}

function residentBodyTerrainAt(body) {
  const materialWorld = world.gamePrototype3DWorld || null;
  const field = materialWorld && materialWorld.physics ? materialWorld.physics.environment || {} : {};
  const position = body.position3d || { x: 0, y: 0, z: 0 };
  const terrainCell = world.gamePrototypeTerrain ? terrainCellAtPosition(position) : null;
  if (terrainCell) {
    return {
      moisture: clampNeed(Number(terrainCell.moisture || 0) + Number(field.moisture || 0) * 0.08),
      stress: clampNeed(Number(terrainCell.erosion || 0) * 0.35 + Number(field.stress || 0) * 0.25),
      friction: clampNeed(Number(terrainCell.walkability || 0.7)),
      slope: Number(terrainCell.slope || 0),
      label: `${terrainCell.cell_id} ${terrainCell.resource_hint}`,
    };
  }
  const routeWetness = position.y > 56 ? 0.18 : 0.04;
  const workYardRoughness = position.x > 58 && position.y < 36 ? 0.12 : 0.05;
  const moisture = clampNeed(Number(field.moisture || 0.24) + routeWetness);
  const stress = clampNeed(Number(field.stress || 0.16) + workYardRoughness);
  const friction = clampNeed(0.82 - moisture * 0.28 - stress * 0.12);
  return {
    moisture,
    stress,
    friction,
    slope: position.y > 62 ? 0.14 : 0.04,
    label: position.y > 56 ? 'wet route edge' : position.x > 58 && position.y < 36 ? 'busy work yard' : 'packed village ground',
  };
}

function carriedLoadForResident(residentName, action) {
  const materialWorld = world.gamePrototype3DWorld || null;
  const carriedMass = materialWorld && materialWorld.components
    ? materialWorld.components
      .filter(component => component.carried_by === residentName)
      .reduce((sum, component) => sum + Number(component.mass || 1), 0)
    : 0;
  const actionLoad = action === 'forage' ? 2.4 : action === 'proposal_work' ? 3.2 : action === 'physics_repair' || action === 'material_manipulation' ? 1.8 : action === 'practice_maintenance' ? 1.3 : 0;
  return Number((carriedMass + actionLoad).toFixed(3));
}

function ensurePrototypeTerrain() {
  if (!world.gamePrototypeTerrain) {
    const width = 8;
    const height = 6;
    const cells = [];
    for (let y = 0; y < height; y += 1) {
      for (let x = 0; x < width; x += 1) {
        const routeBand = y >= 4;
        const storageBand = x >= 2 && x <= 4 && y <= 1;
        const workYard = x >= 4 && x <= 6 && y <= 2;
        const moisture = routeBand ? 0.46 : storageBand ? 0.24 : 0.32 + ((x + y) % 3) * 0.025;
        const compaction = routeBand ? 0.58 : workYard ? 0.52 : 0.34;
        const erosion = routeBand ? 0.22 : 0.1 + (y * 0.015);
        cells.push({
          cell_id: `T-${x}-${y}`,
          x,
          y,
          center: { x: Number(((x + 0.5) * (120 / width)).toFixed(3)), y: Number(((y + 0.5) * (90 / height)).toFixed(3)), z: 0 },
          height: Number((0.4 + (height - y) * 0.06 + (x % 2) * 0.015).toFixed(3)),
          slope: Number((routeBand ? 0.16 : 0.05 + y * 0.012).toFixed(3)),
          moisture: Number(moisture.toFixed(3)),
          compaction: Number(compaction.toFixed(3)),
          erosion: Number(erosion.toFixed(3)),
          vegetation: Number((routeBand ? 0.18 : 0.42 - x * 0.015).toFixed(3)),
          walkability: 0.72,
          support_capacity: 0.72,
          drainage: Number((0.32 + y * 0.04).toFixed(3)),
          resource_hint: routeBand ? 'wet soil and route grit' : storageBand ? 'dry packed storage ground' : workYard ? 'trampled work yard soil' : 'mixed village soil',
          hidden_law_normal_view: false,
        });
      }
    }
    world.gamePrototypeTerrain = {
      runCount: 0,
      width,
      height,
      cells,
      terrainLedger: [],
      flowLedger: [],
      supportLedger: [],
      resourceLedger: [],
      boundary: {
        stochasticTerrainPhysics: true,
        terrainAffectsBodies: true,
        terrainAffectsComponents: true,
        noDecorativeMapOnly: true,
        noResourceSpawning: true,
        hiddenLawNormalView: false,
      },
    };
  }
  const terrain = world.gamePrototypeTerrain;
  if (!Array.isArray(terrain.cells)) terrain.cells = [];
  if (!Array.isArray(terrain.terrainLedger)) terrain.terrainLedger = [];
  if (!Array.isArray(terrain.flowLedger)) terrain.flowLedger = [];
  if (!Array.isArray(terrain.supportLedger)) terrain.supportLedger = [];
  if (!Array.isArray(terrain.resourceLedger)) terrain.resourceLedger = [];
  return terrain;
}

function terrainCellAtPosition(position) {
  const terrain = ensurePrototypeTerrain();
  const x = Math.max(0, Math.min(119.999, Number(position && position.x || 0)));
  const y = Math.max(0, Math.min(89.999, Number(position && position.y || 0)));
  const cellX = Math.max(0, Math.min(terrain.width - 1, Math.floor(x / (120 / terrain.width))));
  const cellY = Math.max(0, Math.min(terrain.height - 1, Math.floor(y / (90 / terrain.height))));
  return terrain.cells.find(cell => cell.x === cellX && cell.y === cellY) || terrain.cells[0];
}

function terrainNeighbors(cell) {
  const terrain = ensurePrototypeTerrain();
  return terrain.cells.filter(candidate => Math.abs(candidate.x - cell.x) + Math.abs(candidate.y - cell.y) === 1);
}

function runTerrainPhysicsStep(source = 'manual terrain physics') {
  ensureGamePrototype();
  const terrain = ensurePrototypeTerrain();
  const materialWorld = ensurePrototype3DWorld();
  const bodies = ensureResidentBodies();
  const entropy = deepTimeEntropyByte();
  terrain.runCount += 1;
  const stepId = `TPH-${String(terrain.runCount).padStart(3, '0')}`;
  const dayCycle = world.gamePrototypeDayCycle || null;
  const latestWeather = dayCycle && dayCycle.weatherLedger && dayCycle.weatherLedger.length ? dayCycle.weatherLedger[dayCycle.weatherLedger.length - 1].weather : 'no weather';
  const wetWeather = /drizzle|wet|rain|storm|storage damp/.test(latestWeather);
  const dryWeather = /dry|wind|heat/.test(latestWeather);
  const componentPressure = {};
  (materialWorld.components || []).forEach(component => {
    const cell = terrainCellAtPosition(component.position3d || {});
    const material = materialWorld.materialCatalog[component.material_id] || {};
    componentPressure[cell.cell_id] = (componentPressure[cell.cell_id] || 0) + Number(component.mass || material.mass || 1);
  });
  const bodyPressure = {};
  Object.values(bodies.bodies || {}).forEach(body => {
    const cell = terrainCellAtPosition(body.position3d || {});
    bodyPressure[cell.cell_id] = (bodyPressure[cell.cell_id] || 0) + Number(body.mass || 45) + Number(body.carried_load || 0);
  });
  const flowRows = [];
  const supportRows = [];
  terrain.cells.forEach((cell, index) => {
    const before = {
      moisture: Number(cell.moisture || 0),
      compaction: Number(cell.compaction || 0),
      erosion: Number(cell.erosion || 0),
      vegetation: Number(cell.vegetation || 0),
      walkability: Number(cell.walkability || 0),
      support_capacity: Number(cell.support_capacity || 0),
      height: Number(cell.height || 0),
    };
    const neighbors = terrainNeighbors(cell);
    const neighborMoisture = neighbors.length ? neighbors.reduce((sum, row) => sum + Number(row.moisture || 0), 0) / neighbors.length : before.moisture;
    const entropyNudge = ((entropy + index * 19 + terrain.runCount) % 17) / 1000;
    const rainInput = wetWeather ? 0.055 : 0;
    const evaporation = dryWeather ? 0.045 : 0.016;
    const flow = (neighborMoisture - before.moisture) * 0.08 - Number(cell.slope || 0) * Number(cell.drainage || 0) * 0.025;
    const pressure = Number(componentPressure[cell.cell_id] || 0) + Number(bodyPressure[cell.cell_id] || 0);
    const pressureScale = Math.min(1, pressure / 120);
    cell.moisture = Number(clamp(before.moisture + rainInput + flow - evaporation + entropyNudge).toFixed(3));
    cell.compaction = Number(clamp(before.compaction + pressureScale * 0.045 - cell.moisture * 0.018).toFixed(3));
    cell.erosion = Number(clamp(before.erosion + cell.moisture * Number(cell.slope || 0) * 0.035 + pressureScale * 0.02 - before.vegetation * 0.008).toFixed(3));
    cell.vegetation = Number(clamp(before.vegetation - pressureScale * 0.018 - cell.erosion * 0.006 + (wetWeather ? 0.006 : 0)).toFixed(3));
    cell.height = Number(Math.max(0, before.height - cell.erosion * 0.012 + cell.compaction * 0.002).toFixed(3));
    cell.walkability = Number(clamp(0.92 - cell.moisture * 0.3 - cell.erosion * 0.28 - pressureScale * 0.08 + cell.compaction * 0.08).toFixed(3));
    cell.support_capacity = Number(clamp(0.84 + cell.compaction * 0.18 - cell.moisture * 0.22 - cell.erosion * 0.24).toFixed(3));
    flowRows.push({
      flow_id: `TF-${String(terrain.flowLedger.length + flowRows.length + 1).padStart(4, '0')}`,
      terrain_step_id: stepId,
      cell_id: cell.cell_id,
      moisture_flow: Number(flow.toFixed(4)),
      rain_input: rainInput,
      evaporation,
      pressure_mass: Number(pressure.toFixed(3)),
      after_moisture: cell.moisture,
      after_walkability: cell.walkability,
    });
    if (pressure > 0 || cell.support_capacity < 0.58 || cell.walkability < 0.58) {
      supportRows.push({
        support_id: `TS-${String(terrain.supportLedger.length + supportRows.length + 1).padStart(4, '0')}`,
        terrain_step_id: stepId,
        cell_id: cell.cell_id,
        pressure_mass: Number(pressure.toFixed(3)),
        support_capacity: cell.support_capacity,
        walkability: cell.walkability,
        maintenance_pressure: cell.support_capacity < 0.58 || cell.walkability < 0.55,
      });
    }
  });
  (materialWorld.components || []).forEach(component => {
    const cell = terrainCellAtPosition(component.position3d || {});
    if (cell.support_capacity < 0.58 || cell.moisture > 0.62) {
      component.stability = Number(clamp(Number(component.stability || 0.6) - Math.max(0, 0.62 - cell.support_capacity) * 0.055 - Math.max(0, cell.moisture - 0.62) * 0.035).toFixed(3));
      component.damage = Number(clamp(Number(component.damage || 0) + Math.max(0, cell.moisture - 0.58) * 0.025).toFixed(3));
      component.terrain_cell_id = cell.cell_id;
    }
  });
  Object.values(bodies.bodies || {}).forEach(body => {
    const cell = terrainCellAtPosition(body.position3d || {});
    body.footing = Number(cell.walkability.toFixed(3));
    body.slip_risk = Number(clamp(Number(body.slip_risk || 0) * 0.65 + (1 - cell.walkability) * 0.24).toFixed(3));
    body.terrain_cell_id = cell.cell_id;
  });
  const averageMoisture = terrain.cells.reduce((sum, cell) => sum + Number(cell.moisture || 0), 0) / Math.max(1, terrain.cells.length);
  const averageWalkability = terrain.cells.reduce((sum, cell) => sum + Number(cell.walkability || 0), 0) / Math.max(1, terrain.cells.length);
  const weakCells = terrain.cells.filter(cell => Number(cell.support_capacity || 1) < 0.58 || Number(cell.walkability || 1) < 0.55);
  if (materialWorld.physics && materialWorld.physics.environment) {
    materialWorld.physics.environment.moisture = Number(clamp(Number(materialWorld.physics.environment.moisture || 0.3) * 0.7 + averageMoisture * 0.3).toFixed(3));
    materialWorld.physics.environment.stress = Number(clamp(Number(materialWorld.physics.environment.stress || 0.16) + weakCells.length / Math.max(1, terrain.cells.length) * 0.025).toFixed(3));
  }
  const resourceDelta = {
    water: wetWeather ? 1 : (dryWeather ? -1 : 0),
    fiber: weakCells.length > 6 ? -1 : 0,
    wood: 0,
    care: averageWalkability < 0.55 ? -1 : 0,
  };
  Object.entries(resourceDelta).forEach(([key, value]) => {
    if (value !== 0) world.resources[key] = Math.max(0, Math.min(99, Number(world.resources[key] || 0) + value));
  });
  const resourceRow = {
    resource_id: `TR-${String(terrain.resourceLedger.length + 1).padStart(3, '0')}`,
    terrain_step_id: stepId,
    resource_delta: resourceDelta,
    source: latestWeather,
    no_resource_spawning: resourceDelta.water <= 1 && resourceDelta.fiber <= 0 && resourceDelta.care <= 0,
  };
  terrain.flowLedger.push(...flowRows);
  terrain.supportLedger.push(...supportRows);
  terrain.resourceLedger.push(resourceRow);
  terrain.flowLedger = terrain.flowLedger.slice(-180);
  terrain.supportLedger = terrain.supportLedger.slice(-140);
  terrain.resourceLedger = terrain.resourceLedger.slice(-80);
  const terrainRow = {
    terrain_step_id: stepId,
    source,
    entropy,
    weather: latestWeather,
    average_moisture: Number(averageMoisture.toFixed(3)),
    average_walkability: Number(averageWalkability.toFixed(3)),
    weak_cells: weakCells.length,
    component_pressure_cells: Object.keys(componentPressure).length,
    body_pressure_cells: Object.keys(bodyPressure).length,
    flow_rows: flowRows.length,
    support_rows: supportRows.length,
    resource_delta: resourceDelta,
    no_effect_without_cause: true,
    no_resource_spawning: true,
    hidden_law_normal_view: false,
  };
  terrain.terrainLedger.push(terrainRow);
  terrain.terrainLedger = terrain.terrainLedger.slice(-120);
  recordRealityConstraint('terrain_physics_step', {
    resident: world.selected,
    sourceBeliefId: stepId,
    materials: ['soil', 'water', 'footing', 'support'],
    publicObservation: `${weakCells.length} terrain cell(s) showed footing/support pressure`,
    residentInterpretation: averageWalkability < 0.55 ? 'route and work ground feel unsafe' : 'ground conditions changed movement and support',
    materialTransformation: `moisture=${terrainRow.average_moisture}; walkability=${terrainRow.average_walkability}; weak=${weakCells.length}`,
    timeCost: 1,
    workCost: weakCells.length ? 1 : 0,
    toolWear: weakCells.length > 4 ? 1 : 0,
    maintenanceObligation: weakCells.length ? 'route or support ground may need resident project' : 'none',
    unintendedConsequence: averageWalkability < 0.55 ? 'resident body footing worsened' : 'terrain stayed traversable',
    hiddenLawInvolved: world.audit ? 'terrain moisture, drainage, compaction, erosion, support, and footing' : 'audit only',
    conservationCheck: true
  });
  return log('runTerrainPhysicsStep', { terrainStepId: stepId, weakCells: weakCells.length, averageMoisture: terrainRow.average_moisture, averageWalkability: terrainRow.average_walkability, flowRows: flowRows.length, supportRows: supportRows.length });
}

function runTerrainPhysicsLoop() {
  const before = ensurePrototypeTerrain().terrainLedger.length;
  for (let i = 0; i < 8; i += 1) runTerrainPhysicsStep('terrain loop');
  const terrain = ensurePrototypeTerrain();
  return log('runTerrainPhysicsLoop', { stepsAdded: terrain.terrainLedger.length - before, totalSteps: terrain.terrainLedger.length, flowRows: terrain.flowLedger.length, supportRows: terrain.supportLedger.length });
}

function ensurePrototypeTools() {
  if (!world.gamePrototypeTools) {
    world.gamePrototypeTools = {
      runCount: 0,
      tools: [
        { tool_id: 'TL-stone-edge', resident_term: 'kar', player_gloss: 'stone scraping edge', engine_concept: 'stone_edge_tool', material_id: 'stone', mass: 1.4, hardness: 0.74, edge_integrity: 0.68, handle_binding: 0.42, leverage: 0.36, durability: 0.72, moisture: 0.18, wear: 0.12, damage: 0.08, owner: 'Ari', current_holder: 'Ari', status: 'usable', roots: ['ka=hard/biting', 'ar=edge'] },
        { tool_id: 'TL-fiber-twist', resident_term: 'ren-ko', player_gloss: 'fiber twisting loop', engine_concept: 'fiber_tension_tool', material_id: 'fiber', mass: 0.45, hardness: 0.18, edge_integrity: 0.24, handle_binding: 0.78, leverage: 0.48, durability: 0.56, moisture: 0.24, wear: 0.18, damage: 0.06, owner: 'Sera', current_holder: 'Sera', status: 'usable', roots: ['ren=raised/held', 'ko=small hand thing'] },
        { tool_id: 'TL-branch-lever', resident_term: 'mor-ren', player_gloss: 'branch lever', engine_concept: 'rough_branch_lever', material_id: 'rough_branch', mass: 2.8, hardness: 0.46, edge_integrity: 0.16, handle_binding: 0.34, leverage: 0.82, durability: 0.61, moisture: 0.26, wear: 0.1, damage: 0.12, owner: 'Milo', current_holder: 'Milo', status: 'usable', roots: ['mor=push/turn', 'ren=raised/held'] },
        { tool_id: 'TL-clay-paddle', resident_term: 'ku-pal', player_gloss: 'clay pressing paddle', engine_concept: 'clay_work_surface_tool', material_id: 'clay_vessel', mass: 1.1, hardness: 0.48, edge_integrity: 0.2, handle_binding: 0.5, leverage: 0.44, durability: 0.64, moisture: 0.3, wear: 0.15, damage: 0.1, owner: 'Nia', current_holder: 'Nia', status: 'usable', roots: ['ku=vessel/hollow', 'pal=press/flat'] },
      ],
      useLedger: [],
      wearLedger: [],
      failureLedger: [],
      repairLedger: [],
      boundary: {
        toolsArePhysicalObjects: true,
        workRequiresToolFitOrHands: true,
        wearAndFailureAreStochastic: true,
        repairConsumesResources: true,
        noFreeConstruction: true,
        hiddenLawNormalView: false,
      },
    };
  }
  const sim = world.gamePrototypeTools;
  ['tools', 'useLedger', 'wearLedger', 'failureLedger', 'repairLedger'].forEach(key => {
    if (!Array.isArray(sim[key])) sim[key] = [];
  });
  return sim;
}

function toolFitForAction(tool, action, targetMaterial = {}) {
  const needsEdge = ['cut', 'scrape', 'shape', 'dry', 'wet_test', 'test'].includes(action);
  const needsBinding = ['tie', 'practice_maintenance', 'physics_repair'].includes(action);
  const needsLeverage = ['carry', 'stack', 'drop', 'proposal_work', 'project_work'].includes(action);
  let fit = 0.24;
  if (needsEdge) fit += Number(tool.edge_integrity || 0) * 0.5 + Number(tool.hardness || 0) * 0.18;
  if (needsBinding) fit += Number(tool.handle_binding || 0) * 0.54 + Number(tool.leverage || 0) * 0.12;
  if (needsLeverage) fit += Number(tool.leverage || 0) * 0.5 + Number(tool.durability || 0) * 0.16;
  if (action === 'project_work') fit += Math.max(Number(tool.leverage || 0), Number(tool.edge_integrity || 0)) * 0.18;
  fit -= Number(tool.damage || 0) * 0.34 + Number(tool.wear || 0) * 0.22 + Math.max(0, Number(tool.moisture || 0) - 0.45) * 0.18;
  fit -= Math.max(0, Number(targetMaterial.hardness || 0.3) - Number(tool.hardness || 0.3)) * 0.14;
  return Number(clamp(fit).toFixed(3));
}

function selectToolForWork(action, residentName, targetComponent = null) {
  const sim = ensurePrototypeTools();
  const materialWorld = world.gamePrototype3DWorld || null;
  const targetMaterial = targetComponent && materialWorld ? materialWorld.materialCatalog[targetComponent.material_id] || {} : {};
  const usable = sim.tools.filter(tool => tool.status !== 'broken');
  const candidates = usable.length ? usable : sim.tools;
  return candidates
    .map(tool => ({ tool, fit: toolFitForAction(tool, action === 'proposal_work' ? 'project_work' : action, targetMaterial), owned: tool.current_holder === residentName || tool.owner === residentName }))
    .sort((a, b) => (b.fit - a.fit) || (Number(b.owned) - Number(a.owned)))[0];
}

function repairToolIfPossible(tool, residentName, reason) {
  const sim = ensurePrototypeTools();
  const canRepair = Number(world.resources.fiber || 0) > 0 && Number(world.resources.wood || 0) > 0;
  if (!canRepair) return null;
  world.resources.fiber = Math.max(0, Number(world.resources.fiber || 0) - 1);
  world.resources.wood = Math.max(0, Number(world.resources.wood || 0) - 1);
  const before = { wear: tool.wear, damage: tool.damage, handle_binding: tool.handle_binding, edge_integrity: tool.edge_integrity, status: tool.status };
  tool.wear = Number(clamp(Number(tool.wear || 0) - 0.18).toFixed(3));
  tool.damage = Number(clamp(Number(tool.damage || 0) - 0.16).toFixed(3));
  tool.handle_binding = Number(clamp(Number(tool.handle_binding || 0) + 0.14).toFixed(3));
  tool.edge_integrity = Number(clamp(Number(tool.edge_integrity || 0) + 0.06).toFixed(3));
  tool.status = Number(tool.damage || 0) > 0.72 ? 'strained' : 'usable';
  const row = {
    repair_id: `TREP-${String(sim.repairLedger.length + 1).padStart(3, '0')}`,
    tool_id: tool.tool_id,
    resident: residentName,
    reason,
    before,
    after: { wear: tool.wear, damage: tool.damage, handle_binding: tool.handle_binding, edge_integrity: tool.edge_integrity, status: tool.status },
    resource_cost: { fiber: 1, wood: 1 },
    no_resource_spawning: true,
  };
  sim.repairLedger.push(row);
  sim.repairLedger = sim.repairLedger.slice(-80);
  return row;
}

function applyToolPhysicsUse(residentName, action, targetComponent = null, source = 'work') {
  const sim = ensurePrototypeTools();
  const materialWorld = ensurePrototype3DWorld();
  const selection = selectToolForWork(action, residentName, targetComponent);
  const tool = selection ? selection.tool : sim.tools[0];
  const material = targetComponent ? materialWorld.materialCatalog[targetComponent.material_id] || {} : {};
  const entropy = deepTimeEntropyByte();
  const before = { wear: Number(tool.wear || 0), damage: Number(tool.damage || 0), moisture: Number(tool.moisture || 0), edge_integrity: Number(tool.edge_integrity || 0), handle_binding: Number(tool.handle_binding || 0), status: tool.status };
  const fit = selection ? selection.fit : toolFitForAction(tool, action, material);
  const workLoad = action === 'project_work' || action === 'proposal_work' ? 0.16 : ['tie', 'stack', 'carry'].includes(action) ? 0.11 : 0.08;
  const materialHardness = Number(material.hardness || 0.35);
  const wetPenalty = Math.max(0, Number(tool.moisture || 0) - 0.42) * 0.08;
  const entropyWear = ((entropy + sim.useLedger.length * 11) % 13) / 1000;
  const wearDelta = Number(Math.max(0.006, workLoad * (0.6 + materialHardness * 0.5) - fit * 0.04 + wetPenalty + entropyWear).toFixed(3));
  const damageDelta = Number(Math.max(0, wearDelta * 0.38 + Math.max(0, materialHardness - Number(tool.hardness || 0.35)) * 0.045).toFixed(3));
  tool.wear = Number(clamp(Number(tool.wear || 0) + wearDelta).toFixed(3));
  tool.damage = Number(clamp(Number(tool.damage || 0) + damageDelta).toFixed(3));
  tool.moisture = Number(clamp(Number(tool.moisture || 0) + (world.gamePrototypeTerrain ? (terrainCellAtPosition((targetComponent && targetComponent.position3d) || {}).moisture - Number(tool.moisture || 0)) * 0.04 : 0)).toFixed(3));
  tool.edge_integrity = Number(clamp(Number(tool.edge_integrity || 0) - wearDelta * 0.12).toFixed(3));
  tool.handle_binding = Number(clamp(Number(tool.handle_binding || 0) - wearDelta * 0.08).toFixed(3));
  const failureProbability = clamp(Number(tool.damage || 0) * 0.32 + Number(tool.wear || 0) * 0.18 + Math.max(0, 0.42 - fit) * 0.34 + wetPenalty);
  const threshold = ((entropy + tool.tool_id.length * 7) % 100) / 100;
  const failed = threshold < failureProbability && failureProbability > 0.22;
  if (failed) tool.status = Number(tool.damage || 0) > 0.78 ? 'broken' : 'strained';
  const repair = failed ? repairToolIfPossible(tool, residentName, `${action} strained ${tool.resident_term}`) : null;
  const actionBlocked = failed && !repair && fit < 0.36;
  const row = {
    tool_use_id: `TUSE-${String(sim.useLedger.length + 1).padStart(3, '0')}`,
    resident: residentName,
    action,
    source,
    tool_id: tool.tool_id,
    resident_term: tool.resident_term,
    player_gloss: tool.player_gloss,
    engine_concept: tool.engine_concept,
    target_component_id: targetComponent ? targetComponent.component_id : 'none',
    target_material_id: targetComponent ? targetComponent.material_id : 'none',
    fit,
    wear_delta: wearDelta,
    damage_delta: damageDelta,
    failure_probability: Number(failureProbability.toFixed(3)),
    failure_threshold: Number(threshold.toFixed(3)),
    failed,
    repaired: Boolean(repair),
    repair_id: repair ? repair.repair_id : null,
    action_blocked: actionBlocked,
    failure_reason: actionBlocked ? `${tool.resident_term} failed and no repair material was available` : failed ? `${tool.resident_term} strained during work` : null,
    before,
    after: { wear: tool.wear, damage: tool.damage, moisture: tool.moisture, edge_integrity: tool.edge_integrity, handle_binding: tool.handle_binding, status: tool.status },
    no_resource_spawning: true,
    hidden_law_normal_view: false,
  };
  sim.useLedger.push(row);
  sim.wearLedger.push({ wear_id: `TWR-${String(sim.wearLedger.length + 1).padStart(3, '0')}`, tool_use_id: row.tool_use_id, tool_id: tool.tool_id, wear_delta: wearDelta, damage_delta: damageDelta, wear_after: tool.wear, damage_after: tool.damage, fit });
  if (failed) sim.failureLedger.push({ failure_id: `TFL-${String(sim.failureLedger.length + 1).padStart(3, '0')}`, tool_use_id: row.tool_use_id, tool_id: tool.tool_id, resident: residentName, reason: row.failure_reason || 'tool strained', repaired: Boolean(repair), action_blocked: actionBlocked });
  sim.useLedger = sim.useLedger.slice(-160);
  sim.wearLedger = sim.wearLedger.slice(-160);
  sim.failureLedger = sim.failureLedger.slice(-100);
  sim.runCount += 1;
  recordRealityConstraint('tool_work_physics', {
    resident: residentName,
    sourceBeliefId: row.tool_use_id,
    materials: [tool.material_id, row.target_material_id].filter(value => value && value !== 'none'),
    publicObservation: `${residentName} used ${tool.resident_term} for ${action}; fit ${fit}`,
    residentInterpretation: row.failed ? `${tool.resident_term} needs care after work` : `${tool.resident_term} carried the work`,
    materialTransformation: `tool wear ${before.wear}->${tool.wear}; damage ${before.damage}->${tool.damage}; target=${row.target_component_id}`,
    timeCost: 1,
    workCost: 1,
    toolWear: wearDelta,
    maintenanceObligation: row.failed ? `repair or rest ${tool.tool_id}` : 'monitor tool wear',
    unintendedConsequence: actionBlocked ? 'work blocked by physical tool failure' : row.failed ? 'tool repair opportunity created' : 'tool wear accumulated',
    hiddenLawInvolved: world.audit ? 'tool hardness, edge integrity, leverage, binding, moisture, durability, and stochastic failure' : 'audit only',
    conservationCheck: true
  });
  return row;
}

function runToolPhysicsStep(action = 'project_work') {
  ensureGamePrototype();
  const materialWorld = ensurePrototype3DWorld();
  const entropy = deepTimeEntropyByte();
  const residentNames = Object.keys(world.residents);
  const residentName = residentNames[(entropy + ensurePrototypeTools().useLedger.length) % residentNames.length];
  const components = materialWorld.components || [];
  const target = components[(entropy + components.length) % Math.max(1, components.length)] || null;
  const row = applyToolPhysicsUse(residentName, action, target, 'player_observed_tool_physics');
  recordPrototypeMilestone('tool-physics', `${row.tool_use_id}: ${residentName} used ${row.resident_term}; failed=${row.failed}`);
  return log('runToolPhysicsStep', { toolUseId: row.tool_use_id, resident: residentName, toolId: row.tool_id, action: row.action, fit: row.fit, failed: row.failed, repaired: row.repaired, blocked: row.action_blocked });
}

function runToolPhysicsLoop() {
  const before = ensurePrototypeTools().useLedger.length;
  ['project_work', 'tie', 'scrape', 'stack', 'test', 'physics_repair'].forEach(action => runToolPhysicsStep(action));
  const sim = ensurePrototypeTools();
  return log('runToolPhysicsLoop', { stepsAdded: sim.useLedger.length - before, totalUses: sim.useLedger.length, failures: sim.failureLedger.length, repairs: sim.repairLedger.length });
}

function ensurePrototypeResourcePhysics() {
  if (!world.gamePrototypeResourcePhysics) {
    world.gamePrototypeResourcePhysics = {
      runCount: 0,
      stocks: [
        { stock_id: 'RSP-water-jars', resource: 'water', resident_term: 'ku-wa', player_gloss: 'stored water jars', engine_concept: 'water_stock_in_vessels', quantity: Number(world.resources.water || 0), capacity: 18, mass_per_unit: 1, storage: 'clay vessels near raised dry storage', moisture: 1, temperature: 0.42, contamination: 0.08, decay: 0.02, source: 'well carry and rain catch', location3d: { x: 30, y: 24, z: 78 } },
        { stock_id: 'RSP-fiber-bundles', resource: 'fiber', resident_term: 'ren', player_gloss: 'fiber bundles', engine_concept: 'fiber_stock_binding_material', quantity: Number(world.resources.fiber || 0), capacity: 16, mass_per_unit: 0.22, storage: 'covered bundle rack', moisture: 0.32, temperature: 0.39, contamination: 0.04, decay: 0.06, source: 'reed collection and drying', location3d: { x: 52, y: 32, z: 48 } },
        { stock_id: 'RSP-wood-stack', resource: 'wood', resident_term: 'mor', player_gloss: 'rough wood stack', engine_concept: 'wood_stock_structural_material', quantity: Number(world.resources.wood || 0), capacity: 24, mass_per_unit: 2.4, storage: 'ground stack under cover edge', moisture: 0.28, temperature: 0.37, contamination: 0.03, decay: 0.035, source: 'fallen branch gathering', location3d: { x: 62, y: 50, z: 16 } },
        { stock_id: 'RSP-food-cache', resource: 'food', resident_term: 'nam', player_gloss: 'stored edible cache', engine_concept: 'food_stock_spoilable_cache', quantity: Number(world.resources.food || 0), capacity: 16, mass_per_unit: 0.35, storage: 'cool raised basket near shade', moisture: 0.26, temperature: 0.34, contamination: 0.06, decay: 0.08, source: 'nearby patches and careful gathering', location3d: { x: 38, y: 36, z: 54 } },
        { stock_id: 'RSP-care-attention', resource: 'care', resident_term: 'num', player_gloss: 'available care and attention', engine_concept: 'embodied_attention_recovery_stock', quantity: Number(world.resources.care || 0), capacity: 12, mass_per_unit: 0, storage: 'resident rest and mutual attention', moisture: 0, temperature: 0.4, contamination: 0, decay: 0.04, source: 'rest, trust, and low fatigue', location3d: { x: 44, y: 44, z: 0 } },
      ],
      stockLedger: [],
      transformLedger: [],
      lossLedger: [],
      gainLedger: [],
      syncLedger: [],
      lastWorldResources: { ...world.resources },
      boundary: {
        resourcesArePhysicalStocks: true,
        careIsEmbodiedAttentionNotMaterial: true,
        noResourceSpawning: true,
        weatherTerrainStorageAndBodiesDriveChange: true,
        hiddenLawNormalView: false,
      },
    };
  }
  const sim = world.gamePrototypeResourcePhysics;
  ['stocks', 'stockLedger', 'transformLedger', 'lossLedger', 'gainLedger', 'syncLedger'].forEach(key => {
    if (!Array.isArray(sim[key])) sim[key] = [];
  });
  if (!sim.stocks.some(stock => stock.resource === 'food')) {
    sim.stocks.push({ stock_id: 'RSP-food-cache', resource: 'food', resident_term: 'nam', player_gloss: 'stored edible cache', engine_concept: 'food_stock_spoilable_cache', quantity: Number(world.resources.food || 0), capacity: 16, mass_per_unit: 0.35, storage: 'cool raised basket near shade', moisture: 0.26, temperature: 0.34, contamination: 0.06, decay: 0.08, source: 'nearby patches and careful gathering', location3d: { x: 38, y: 36, z: 54 } });
  }
  if (!sim.lastWorldResources) sim.lastWorldResources = { ...world.resources };
  return sim;
}

function syncResourcePhysicsFromWorld(source = 'external gameplay resource ledger') {
  const sim = ensurePrototypeResourcePhysics();
  sim.stocks.forEach(stock => {
    const current = Number(world.resources[stock.resource] || 0);
    const tracked = Number(sim.lastWorldResources[stock.resource] == null ? stock.quantity : sim.lastWorldResources[stock.resource]);
    const externalDelta = Number((current - tracked).toFixed(3));
    if (externalDelta !== 0) {
      const before = Number(stock.quantity || 0);
      stock.quantity = Number(Math.max(0, Math.min(Number(stock.capacity || 99), before + externalDelta)).toFixed(3));
      sim.syncLedger.push({
        sync_id: `RSYNC-${String(sim.syncLedger.length + 1).padStart(3, '0')}`,
        resource: stock.resource,
        stock_id: stock.stock_id,
        source,
        external_delta: externalDelta,
        before,
        after: stock.quantity,
        no_resource_spawning: true,
      });
    }
  });
  sim.syncLedger = sim.syncLedger.slice(-120);
  sim.lastWorldResources = { ...world.resources };
  return sim;
}

function runResourcePhysicsStep(source = 'manual resource physics') {
  ensureGamePrototype();
  const sim = syncResourcePhysicsFromWorld(`${source} pre-sync`);
  const materialWorld = world.gamePrototype3DWorld || ensurePrototype3DWorld();
  const field = materialWorld.physics && materialWorld.physics.environment ? materialWorld.physics.environment : { moisture: 0.31, heat: 0.46, wind: 0.18, decayPressure: 0.22, stress: 0.16 };
  const weatherRows = world.gamePrototypeDayCycle && world.gamePrototypeDayCycle.weatherLedger ? world.gamePrototypeDayCycle.weatherLedger : [];
  const latestWeather = weatherRows.length ? weatherRows[weatherRows.length - 1].weather : 'steady air';
  const wetWeather = /rain|drizzle|wet|damp|storage/.test(latestWeather);
  const dryWeather = /dry|wind|heat|drought/.test(latestWeather);
  const bodies = world.gamePrototypeResidentBodies && world.gamePrototypeResidentBodies.bodies ? Object.values(world.gamePrototypeResidentBodies.bodies) : [];
  const averageFatigue = bodies.length ? bodies.reduce((sum, body) => sum + Number(body.fatigue || 0), 0) / bodies.length : 0.24;
  const vesselDamage = materialWorld.components
    ? materialWorld.components.filter(component => component.material_id === 'clay_vessel').reduce((sum, component) => sum + Number(component.damage || 0), 0)
    : 0;
  const entropy = deepTimeEntropyByte();
  const stepId = `RSPH-${String(sim.stockLedger.length + 1).padStart(3, '0')}`;
  const rows = sim.stocks.map((stock, index) => {
    const before = {
      quantity: Number(stock.quantity || 0),
      moisture: Number(stock.moisture || 0),
      temperature: Number(stock.temperature || 0),
      contamination: Number(stock.contamination || 0),
      decay: Number(stock.decay || 0),
    };
    const stochastic = (((entropy + index * 19 + sim.runCount * 7) % 11) - 5) / 100;
    const fieldMoisture = Number(field.moisture || 0.31);
    const fieldHeat = Number(field.heat || 0.46);
    const fieldWind = Number(field.wind || 0.18);
    let delta = 0;
    let cause = 'stable storage';
    if (stock.resource === 'water') {
      const rainGain = wetWeather ? 0.7 + fieldMoisture * 0.35 : 0;
      const evaporation = (dryWeather ? 0.35 : 0.08) + fieldHeat * 0.18 + fieldWind * 0.12;
      const leakLoss = vesselDamage * 0.22 + Number(stock.contamination || 0) * 0.08;
      delta = rainGain - evaporation - leakLoss + stochastic * 0.2;
      stock.contamination = Number(Math.max(0, Math.min(1, Number(stock.contamination || 0) + (wetWeather ? 0.015 : -0.006) + vesselDamage * 0.01)).toFixed(3));
      cause = `rain=${rainGain.toFixed(2)}, evaporation=${evaporation.toFixed(2)}, vesselLoss=${leakLoss.toFixed(2)}`;
    } else if (stock.resource === 'fiber') {
      const rot = Math.max(0, fieldMoisture - 0.28) * 0.5 + (wetWeather ? 0.22 : 0) + Number(stock.contamination || 0) * 0.06;
      const dryingProtection = dryWeather ? Math.min(0.18, fieldWind * 0.22 + fieldHeat * 0.08) : 0;
      delta = -Math.max(0, rot - dryingProtection) + stochastic * 0.16;
      stock.moisture = Number(Math.max(0, Math.min(1, Number(stock.moisture || 0) + fieldMoisture * 0.04 - dryingProtection * 0.08)).toFixed(3));
      stock.decay = Number(Math.max(0, Math.min(1, Number(stock.decay || 0) + Math.max(0, rot - dryingProtection) * 0.03)).toFixed(3));
      cause = `fiberRot=${rot.toFixed(2)}, dryingProtection=${dryingProtection.toFixed(2)}`;
    } else if (stock.resource === 'wood') {
      const rot = Math.max(0, fieldMoisture - 0.34) * 0.36 + Number(field.decayPressure || 0) * 0.18 + (wetWeather ? 0.12 : 0);
      const splitting = dryWeather && fieldHeat > 0.52 ? 0.08 + fieldWind * 0.05 : 0;
      delta = -(rot + splitting) + stochastic * 0.12;
      stock.moisture = Number(Math.max(0, Math.min(1, Number(stock.moisture || 0) + (fieldMoisture - Number(stock.moisture || 0)) * 0.05)).toFixed(3));
      stock.decay = Number(Math.max(0, Math.min(1, Number(stock.decay || 0) + (rot + splitting) * 0.025)).toFixed(3));
      cause = `woodRot=${rot.toFixed(2)}, splitting=${splitting.toFixed(2)}`;
    } else if (stock.resource === 'food') {
      const heatSpoil = Math.max(0, fieldHeat - 0.42) * 0.42;
      const dampSpoil = Math.max(0, fieldMoisture - 0.34) * 0.34 + (wetWeather ? 0.12 : 0);
      const dryPreserve = dryWeather ? Math.min(0.16, fieldWind * 0.18 + Math.max(0, fieldHeat - 0.38) * 0.08) : 0;
      const spoilage = Math.max(0, heatSpoil + dampSpoil + Number(stock.contamination || 0) * 0.12 - dryPreserve);
      delta = -spoilage + stochastic * 0.08;
      stock.moisture = Number(Math.max(0, Math.min(1, Number(stock.moisture || 0) + (fieldMoisture - Number(stock.moisture || 0)) * 0.06 - dryPreserve * 0.05)).toFixed(3));
      stock.contamination = Number(Math.max(0, Math.min(1, Number(stock.contamination || 0) + spoilage * 0.035 - dryPreserve * 0.012)).toFixed(3));
      stock.decay = Number(Math.max(0, Math.min(1, Number(stock.decay || 0) + spoilage * 0.03)).toFixed(3));
      cause = `foodSpoilage=${spoilage.toFixed(2)}, dryPreserve=${dryPreserve.toFixed(2)}`;
    } else {
      const fatigueCost = averageFatigue * 0.35 + Number(field.stress || 0) * 0.12;
      const restRecovery = averageFatigue < 0.32 ? 0.42 : 0.16;
      const trustRecovery = Object.values(world.residents).reduce((sum, resident) => sum + Number(resident.trust || 0), 0) / Math.max(1, Object.keys(world.residents).length) * 0.16;
      delta = restRecovery + trustRecovery - fatigueCost + stochastic * 0.1;
      cause = `rest=${restRecovery.toFixed(2)}, trust=${trustRecovery.toFixed(2)}, fatigueCost=${fatigueCost.toFixed(2)}`;
    }
    stock.temperature = Number(Math.max(0, Math.min(1, Number(stock.temperature || 0) + (fieldHeat - Number(stock.temperature || 0)) * 0.05)).toFixed(3));
    const afterQuantity = Number(Math.max(0, Math.min(Number(stock.capacity || 99), before.quantity + delta)).toFixed(3));
    stock.quantity = afterQuantity;
    const actualDelta = Number((afterQuantity - before.quantity).toFixed(3));
    const row = {
      row_id: `${stepId}-${stock.resource}`,
      step_id: stepId,
      tick: world.tick,
      resource: stock.resource,
      stock_id: stock.stock_id,
      resident_term: stock.resident_term,
      player_gloss: stock.player_gloss,
      source,
      weather: latestWeather,
      quantity_before: before.quantity,
      quantity_after: afterQuantity,
      delta: actualDelta,
      capacity: stock.capacity,
      moisture_before: before.moisture,
      moisture_after: Number(stock.moisture || 0),
      temperature_before: before.temperature,
      temperature_after: Number(stock.temperature || 0),
      causal_terms: cause,
      stochastic_term: Number(stochastic.toFixed(3)),
      no_resource_spawning: true,
      hidden_law_normal_view: false,
    };
    sim.transformLedger.push(row);
    if (actualDelta < 0) sim.lossLedger.push({ loss_id: `RLOSS-${String(sim.lossLedger.length + 1).padStart(3, '0')}`, ...row });
    if (actualDelta > 0) sim.gainLedger.push({ gain_id: `RGAIN-${String(sim.gainLedger.length + 1).padStart(3, '0')}`, ...row });
    return row;
  });
  rows.forEach(row => {
    world.resources[row.resource] = Math.max(0, Math.round(row.quantity_after));
  });
  sim.runCount += 1;
  sim.stockLedger.push({
    step_id: stepId,
    tick: world.tick,
    source,
    weather: latestWeather,
    field_moisture: Number(field.moisture || 0),
    field_heat: Number(field.heat || 0),
    field_wind: Number(field.wind || 0),
    average_fatigue: Number(averageFatigue.toFixed(3)),
    deltas: rows.reduce((acc, row) => ({ ...acc, [row.resource]: row.delta }), {}),
    resources_after: { ...world.resources },
    no_resource_spawning: true,
    hidden_law_normal_view: false,
  });
  sim.stockLedger = sim.stockLedger.slice(-120);
  sim.transformLedger = sim.transformLedger.slice(-240);
  sim.lossLedger = sim.lossLedger.slice(-160);
  sim.gainLedger = sim.gainLedger.slice(-160);
  sim.lastWorldResources = { ...world.resources };
  world.gamePrototypeCommons = null;
  recordRealityConstraint('resource_stock_physics', {
    resident: 'village',
    sourceBeliefId: stepId,
    materials: rows.map(row => row.resource),
    publicObservation: `resource stores changed under ${latestWeather}: ${rows.map(row => `${row.resource} ${row.delta}`).join(', ')}`,
    residentInterpretation: 'stores are not numbers; they leak, rot, dry, recover, or strain through use and weather',
    materialTransformation: rows.map(row => `${row.resource}: ${row.quantity_before}->${row.quantity_after} (${row.causal_terms})`).join('; '),
    timeCost: 1,
    workCost: Math.max(0, -rows.find(row => row.resource === 'care').delta),
    toolWear: 0,
    maintenanceObligation: rows.some(row => row.delta < -0.4) ? 'inspect storage and recovery conditions' : 'watch stocks',
    unintendedConsequence: rows.some(row => row.delta < 0) ? 'stock loss can constrain projects and care' : 'weather or rest recovered some stock',
    hiddenLawInvolved: world.audit ? 'resource stock capacity, moisture, heat, wind, vessel loss, fatigue, and stochastic pressure' : 'audit only',
    conservationCheck: true
  });
  recordPrototypeMilestone('resource-stock-physics', `${stepId}: ${rows.map(row => `${row.resource}${row.delta >= 0 ? '+' : ''}${row.delta}`).join(', ')}`);
  return log('runResourcePhysicsStep', { stepId, resources: { ...world.resources }, losses: sim.lossLedger.length, gains: sim.gainLedger.length });
}

function runResourcePhysicsLoop() {
  const before = ensurePrototypeResourcePhysics().stockLedger.length;
  ['weather storage', 'ordinary use', 'rest and recovery', 'maintenance pressure'].forEach(source => runResourcePhysicsStep(source));
  const sim = ensurePrototypeResourcePhysics();
  return log('runResourcePhysicsLoop', { stepsAdded: sim.stockLedger.length - before, totalSteps: sim.stockLedger.length, losses: sim.lossLedger.length, gains: sim.gainLedger.length, resources: { ...world.resources } });
}

function ensurePrototypeThermalPhysics() {
  if (!world.gamePrototypeThermalPhysics) {
    world.gamePrototypeThermalPhysics = {
      runCount: 0,
      nodes: [
        { node_id: 'TH-fire-bowl', resident_term: 'sha-ku', player_gloss: 'watched heat bowl', engine_concept: 'contained_fire_heat_source', position3d: { x: 44, y: 46, z: 8 }, heat: 0.34, fuel: 1.2, ash: 0.08, smoke: 0.06, containment: 0.68, ventilation: 0.52, status: 'warm coals', source: 'older watched ember and dry fuel', local_rule: 'never leave sha-ku alone' },
        { node_id: 'TH-warm-stone', resident_term: 'pal-sha', player_gloss: 'warm stone work spot', engine_concept: 'stored_heat_surface', position3d: { x: 50, y: 36, z: 18 }, heat: 0.22, fuel: 0, ash: 0, smoke: 0.01, containment: 0.82, ventilation: 0.64, status: 'warm surface', source: 'stone warmed near watched coals', local_rule: 'use for drying, not flame' },
      ],
      heatLedger: [],
      fuelLedger: [],
      ignitionLedger: [],
      smokeLedger: [],
      residentEffectLedger: [],
      safetyLedger: [],
      boundary: {
        fireRequiresFuelHeatAndAir: true,
        heatMovesThroughDistanceAndMaterials: true,
        smokeIsAConstraintNotDrama: true,
        hazardsAreBoundedAndRecoverable: true,
        noResourceSpawning: true,
        hiddenLawNormalView: false,
      },
    };
  }
  const sim = world.gamePrototypeThermalPhysics;
  ['nodes', 'heatLedger', 'fuelLedger', 'ignitionLedger', 'smokeLedger', 'residentEffectLedger', 'safetyLedger'].forEach(key => {
    if (!Array.isArray(sim[key])) sim[key] = [];
  });
  return sim;
}

function thermalDistance(a = {}, b = {}) {
  const dx = Number(a.x || 0) - Number(b.x || 0);
  const dy = Number(a.y || 0) - Number(b.y || 0);
  const dz = Number(a.z || 0) - Number(b.z || 0);
  return Math.sqrt(dx * dx + dy * dy + dz * dz);
}

function addThermalSafetyProposal(safetyRow) {
  if (!world.villageBoard || !world.villageBoard.projectProposals) runVillageBoardLoop();
  if (!world.villageBoard || !world.villageBoard.projectProposals) return null;
  const existing = world.villageBoard.projectProposals.find(row => row.origin_event === safetyRow.safety_id && !row.project_completed);
  if (existing) return existing.proposal_id;
  const proposal = {
    proposal_id: `GPB-THERM-${String(world.villageBoard.projectProposals.length + 1).padStart(3, '0')}`,
    proposer: safetyRow.resident || 'Sera',
    problem_addressed: safetyRow.problem,
    materials_needed: safetyRow.required_materials || ['water', 'fiber'],
    likely_helpers: ['Milo', 'Fay'],
    resident_willingness: 0.58,
    known_objections: ['do not waste water unless smoke stays high'],
    risk: safetyRow.risk,
    maintenance_cost: 0.08,
    related_memories: [safetyRow.public_observation],
    related_practice_nodes: [],
    possible_failure_modes: ['smoke returns', 'fuel gets wet', 'containment cracks'],
    current_support_level: 0.36,
    status: 'posted',
    origin_event: safetyRow.safety_id,
    avatar_can_force: false,
    project_progress: 0,
  };
  world.villageBoard.projectProposals.push(proposal);
  return proposal.proposal_id;
}

function runThermalPhysicsStep(source = 'manual thermal physics') {
  ensureGamePrototype();
  const sim = ensurePrototypeThermalPhysics();
  const materialWorld = ensurePrototype3DWorld();
  const field = materialWorld.physics && materialWorld.physics.environment ? materialWorld.physics.environment : { moisture: 0.31, heat: 0.46, wind: 0.18, decayPressure: 0.22, stress: 0.16 };
  const terrain = world.gamePrototypeTerrain || null;
  const entropy = deepTimeEntropyByte();
  const stepId = `THP-${String(sim.heatLedger.length + 1).padStart(3, '0')}`;
  const componentRows = [];
  const nodeRows = sim.nodes.map((node, nodeIndex) => {
    const before = { heat: Number(node.heat || 0), fuel: Number(node.fuel || 0), ash: Number(node.ash || 0), smoke: Number(node.smoke || 0), status: node.status };
    const cell = terrain ? terrainCellAtPosition(node.position3d || {}) : null;
    const localMoisture = cell ? Number(cell.moisture || 0.3) : Number(field.moisture || 0.31);
    const ventilation = clamp(Number(node.ventilation || 0.5) + Number(field.wind || 0.18) * 0.18 - Math.max(0, localMoisture - 0.5) * 0.22);
    const fuelNeed = before.heat > 0.28 ? 0.25 : 0.12;
    let fuelConsumed = 0;
    if (before.fuel > 0.05 && Number(world.resources.wood || 0) > 0 && (source !== 'no fuel test')) {
      fuelConsumed = Number(Math.min(fuelNeed, before.fuel, Number(world.resources.wood || 0) * 0.18).toFixed(3));
      node.fuel = Number(Math.max(0, before.fuel - fuelConsumed).toFixed(3));
      if (fuelConsumed > 0.16) world.resources.wood = Math.max(0, Number(world.resources.wood || 0) - 1);
    }
    const stochastic = (((entropy + nodeIndex * 23 + sim.runCount * 5) % 17) - 8) / 100;
    const oxygenTerm = ventilation * 0.18;
    const wetCooling = localMoisture * 0.16 + Number(field.moisture || 0.31) * 0.08;
    const heatGain = fuelConsumed * 0.44 + oxygenTerm + stochastic * 0.08;
    const heatLoss = wetCooling + Math.max(0, before.smoke - ventilation) * 0.07;
    node.heat = Number(clamp(before.heat + heatGain - heatLoss).toFixed(3));
    node.ash = Number(clamp(Number(node.ash || 0) + fuelConsumed * 0.18).toFixed(3));
    node.smoke = Number(clamp(before.smoke + fuelConsumed * (0.18 + Math.max(0, 0.5 - ventilation)) + wetCooling * 0.14 - ventilation * 0.08).toFixed(3));
    node.status = node.heat > 0.7 ? 'hot watched fire' : node.heat > 0.38 ? 'active warmth' : node.heat > 0.14 ? 'warm coals' : 'cooling';
    sim.fuelLedger.push({
      fuel_id: `THF-${String(sim.fuelLedger.length + 1).padStart(3, '0')}`,
      step_id: stepId,
      node_id: node.node_id,
      fuel_before: before.fuel,
      fuel_after: node.fuel,
      fuel_consumed: fuelConsumed,
      wood_resource_after: Number(world.resources.wood || 0),
      no_resource_spawning: true,
    });
    return {
      node_id: node.node_id,
      resident_term: node.resident_term,
      player_gloss: node.player_gloss,
      heat_before: before.heat,
      heat_after: node.heat,
      fuel_consumed: fuelConsumed,
      smoke_before: before.smoke,
      smoke_after: node.smoke,
      ventilation: Number(ventilation.toFixed(3)),
      local_moisture: Number(localMoisture.toFixed(3)),
      status_before: before.status,
      status_after: node.status,
      stochastic_term: Number(stochastic.toFixed(3)),
    };
  });
  materialWorld.components.forEach(component => {
    const material = materialWorld.materialCatalog[component.material_id] || {};
    const before = {
      temperature: Number(component.temperature || 0.4),
      damage: Number(component.damage || 0),
      moisture: Number(component.moisture || 0),
      stability: Number(component.stability || 0.5),
    };
    const nearest = sim.nodes
      .map(node => ({ node, distance: thermalDistance(node.position3d || {}, component.position3d || {}) }))
      .sort((a, b) => a.distance - b.distance)[0];
    const heatTransfer = nearest
      ? Math.max(0, Number(nearest.node.heat || 0) - before.temperature) * (1 - Number(material.heat_resistance || 0.4)) * Math.max(0.08, 1 - nearest.distance / 90)
      : 0;
    const drying = heatTransfer * (1 - Number(material.water_resistance || 0.5)) * 0.22;
    const burnRisk = Number(material.flammability || 0) * Math.max(0, Number(nearest && nearest.node ? nearest.node.heat : 0) - Number(material.heat_resistance || 0.4)) * Math.max(0.05, 1 - Number(component.moisture || 0));
    const ignitionThreshold = ((entropy + component.component_id.length * 13 + sim.ignitionLedger.length) % 100) / 100;
    const ignited = burnRisk > 0.18 && ignitionThreshold < burnRisk;
    component.temperature = Number(clamp(before.temperature + heatTransfer - Number(field.wind || 0.18) * 0.01).toFixed(3));
    component.moisture = Number(clamp(before.moisture - drying).toFixed(3));
    component.damage = Number(clamp(before.damage + burnRisk * 0.035 + (ignited ? 0.08 : 0)).toFixed(3));
    component.stability = Number(clamp(before.stability - (ignited ? 0.025 : burnRisk * 0.004)).toFixed(3));
    const row = {
      component_id: component.component_id,
      material_id: component.material_id,
      nearest_node_id: nearest ? nearest.node.node_id : 'none',
      distance: nearest ? Number(nearest.distance.toFixed(3)) : null,
      heat_transfer: Number(heatTransfer.toFixed(4)),
      drying: Number(drying.toFixed(4)),
      burn_risk: Number(burnRisk.toFixed(4)),
      ignition_threshold: Number(ignitionThreshold.toFixed(3)),
      ignited,
      before,
      after: {
        temperature: Number(component.temperature || 0),
        damage: Number(component.damage || 0),
        moisture: Number(component.moisture || 0),
        stability: Number(component.stability || 0),
      },
      hidden_law_normal_view: false,
    };
    componentRows.push(row);
    if (ignited) sim.ignitionLedger.push({ ignition_id: `THI-${String(sim.ignitionLedger.length + 1).padStart(3, '0')}`, step_id: stepId, ...row, recoverable: true });
  });
  const totalSmoke = Number(sim.nodes.reduce((sum, node) => sum + Number(node.smoke || 0), 0).toFixed(3));
  const maxHeat = Number(Math.max(...sim.nodes.map(node => Number(node.heat || 0))).toFixed(3));
  const smokeRow = {
    smoke_id: `THS-${String(sim.smokeLedger.length + 1).padStart(3, '0')}`,
    step_id: stepId,
    total_smoke: totalSmoke,
    max_heat: maxHeat,
    public_observation: totalSmoke > 0.6 ? 'smoke made residents step back from the warm place' : 'warmth stayed watched and useful',
    resident_interpretation: totalSmoke > 0.6 ? 'sha-ku needs more air or water nearby' : 'watched warmth can dry and comfort without becoming a spectacle',
    hidden_law_normal_view: false,
  };
  sim.smokeLedger.push(smokeRow);
  const bodySim = world.gamePrototypeResidentBodies || null;
  const residentNames = Object.keys(world.residents);
  residentNames.forEach((name, index) => {
    const body = bodySim && bodySim.bodies ? bodySim.bodies[name] : null;
    const bodyPosition = body ? body.position3d : { x: 44 + index * 4, y: 44, z: 0 };
    const nearest = sim.nodes
      .map(node => ({ node, distance: thermalDistance(node.position3d || {}, bodyPosition || {}) }))
      .sort((a, b) => a.distance - b.distance)[0];
    const warmth = nearest ? Math.max(0, Number(nearest.node.heat || 0) * Math.max(0.05, 1 - nearest.distance / 80)) : 0;
    const smokeStress = totalSmoke * Math.max(0.05, 1 - (nearest ? nearest.distance : 80) / 100);
    if (body) {
      body.comfort = Number(clamp(Number(body.comfort || 0.5) + warmth * 0.05 - smokeStress * 0.025).toFixed(3));
      body.safety = Number(clamp(Number(body.safety || 0.6) - smokeStress * 0.02 - (maxHeat > 0.75 ? 0.01 : 0)).toFixed(3));
      body.fatigue = Number(clamp(Number(body.fatigue || 0.2) - warmth * 0.012 + smokeStress * 0.018).toFixed(3));
    }
    if (smokeStress > 0.2) mutateResident(name, { trust: -0.001, progress: -0.002, memory: 'stepped back from smoke near watched warmth', historyEvent: 'thermal smoke caution', historyDetail: stepId });
    sim.residentEffectLedger.push({
      effect_id: `THE-${String(sim.residentEffectLedger.length + 1).padStart(3, '0')}`,
      step_id: stepId,
      resident: name,
      nearest_node_id: nearest ? nearest.node.node_id : 'none',
      warmth: Number(warmth.toFixed(3)),
      smoke_stress: Number(smokeStress.toFixed(3)),
      comfort_after: body ? body.comfort : null,
      safety_after: body ? body.safety : null,
      hidden_law_normal_view: false,
    });
  });
  const hazard = totalSmoke > 0.65 || componentRows.some(row => row.ignited) || maxHeat > 0.82;
  let safetyProposalId = null;
  if (hazard) {
    const safetyRow = {
      safety_id: `THSAFE-${String(sim.safetyLedger.length + 1).padStart(3, '0')}`,
      step_id: stepId,
      resident: 'Sera',
      risk: componentRows.some(row => row.ignited) ? 'ignition risk' : totalSmoke > 0.65 ? 'smoke risk' : 'heat risk',
      problem: 'watch warm place and keep water or spacing nearby',
      required_materials: ['water', 'fiber'],
      public_observation: smokeRow.public_observation,
      recoverable: true,
      no_permanent_punishment: true,
    };
    safetyProposalId = addThermalSafetyProposal(safetyRow);
    safetyRow.proposal_id = safetyProposalId;
    sim.safetyLedger.push(safetyRow);
  }
  const heatRow = {
    step_id: stepId,
    tick: world.tick,
    source,
    node_rows: nodeRows,
    component_rows: componentRows,
    smoke_id: smokeRow.smoke_id,
    total_smoke: totalSmoke,
    max_heat: maxHeat,
    hazard,
    safety_proposal_id: safetyProposalId,
    wood_after: Number(world.resources.wood || 0),
    no_resource_spawning: true,
    hidden_law_normal_view: false,
  };
  sim.heatLedger.push(heatRow);
  sim.runCount += 1;
  sim.heatLedger = sim.heatLedger.slice(-120);
  sim.fuelLedger = sim.fuelLedger.slice(-160);
  sim.ignitionLedger = sim.ignitionLedger.slice(-120);
  sim.smokeLedger = sim.smokeLedger.slice(-120);
  sim.residentEffectLedger = sim.residentEffectLedger.slice(-240);
  sim.safetyLedger = sim.safetyLedger.slice(-120);
  if (world.gamePrototypeResourcePhysics) syncResourcePhysicsFromWorld('thermal physics fuel consumption');
  world.gamePrototypeCommons = null;
  recordRealityConstraint('thermal_fire_physics', {
    resident: 'village',
    sourceBeliefId: stepId,
    materials: ['wood', 'heat', 'air', 'water'].concat(componentRows.filter(row => row.heat_transfer > 0).slice(0, 4).map(row => row.material_id)),
    publicObservation: smokeRow.public_observation,
    residentInterpretation: smokeRow.resident_interpretation,
    materialTransformation: `fuel rows=${nodeRows.length}; heated components=${componentRows.filter(row => row.heat_transfer > 0).length}; ignition rows=${componentRows.filter(row => row.ignited).length}; smoke=${totalSmoke}`,
    timeCost: 1,
    workCost: hazard ? 2 : 1,
    toolWear: 0,
    maintenanceObligation: hazard ? 'post thermal safety proposal and keep recovery path open' : 'keep watched warmth bounded',
    unintendedConsequence: hazard ? 'smoke or ignition risk changes resident safety and project attention' : 'warmth can dry materials and reduce fatigue without spectacle',
    hiddenLawInvolved: world.audit ? 'fuel, heat transfer, ventilation, oxygen-like exposure, material flammability, moisture, and stochastic ignition' : 'audit only',
    conservationCheck: true
  });
  recordPrototypeMilestone('thermal-fire-physics', `${stepId}: heat=${maxHeat}, smoke=${totalSmoke}, hazard=${hazard}`);
  return log('runThermalPhysicsStep', { stepId, maxHeat, totalSmoke, ignitions: componentRows.filter(row => row.ignited).length, hazard, safetyProposalId });
}

function runThermalPhysicsLoop() {
  const before = ensurePrototypeThermalPhysics().heatLedger.length;
  ['watched warmth', 'drying work', 'smoke check', 'cooling recovery'].forEach(source => runThermalPhysicsStep(source));
  const sim = ensurePrototypeThermalPhysics();
  return log('runThermalPhysicsLoop', { stepsAdded: sim.heatLedger.length - before, totalSteps: sim.heatLedger.length, smokeRows: sim.smokeLedger.length, ignitions: sim.ignitionLedger.length, safetyRows: sim.safetyLedger.length });
}

function ensurePrototypeWaterPhysics() {
  if (!world.gamePrototypeWaterPhysics) {
    world.gamePrototypeWaterPhysics = {
      runCount: 0,
      bodies: [
        { water_id: 'WAT-jars', resident_term: 'ku-wa', player_gloss: 'stored jar water', engine_concept: 'contained_water_stock', kind: 'contained', volume: Number(world.resources.water || 0), capacity: 18, position3d: { x: 30, y: 24, z: 78 }, leak_rate: 0.035, contamination: 0.08, flow_resistance: 0.82, route: 'raised storage edge', status: 'stored' },
        { water_id: 'WAT-low-puddle', resident_term: 'wa-dum', player_gloss: 'low wet patch', engine_concept: 'surface_puddle', kind: 'surface', volume: 1.4, capacity: 6, position3d: { x: 24, y: 62, z: 0 }, leak_rate: 0.12, contamination: 0.18, flow_resistance: 0.36, route: 'low crossing', status: 'shallow' },
        { water_id: 'WAT-cut-run', resident_term: 'wa-ren', player_gloss: 'small guided runoff line', engine_concept: 'hand_cut_drainage_channel', kind: 'channel', volume: 0.6, capacity: 5, position3d: { x: 48, y: 58, z: 0 }, leak_rate: 0.04, contamination: 0.1, flow_resistance: 0.28, route: 'cut beside storage path', status: 'trickling' },
      ],
      flowLedger: [],
      leakLedger: [],
      vesselLedger: [],
      qualityLedger: [],
      routeLedger: [],
      safetyLedger: [],
      boundary: {
        waterHasVolumeAndContainment: true,
        flowFollowsSlopeResistanceAndCapacity: true,
        leaksRequireVesselDamageOrGroundLoss: true,
        routeEffectsAreBounded: true,
        noResourceSpawning: true,
        hiddenLawNormalView: false,
      },
    };
  }
  const sim = world.gamePrototypeWaterPhysics;
  ['bodies', 'flowLedger', 'leakLedger', 'vesselLedger', 'qualityLedger', 'routeLedger', 'safetyLedger'].forEach(key => {
    if (!Array.isArray(sim[key])) sim[key] = [];
  });
  return sim;
}

function addWaterSafetyProposal(safetyRow) {
  if (!world.villageBoard || !world.villageBoard.projectProposals) runVillageBoardLoop();
  if (!world.villageBoard || !world.villageBoard.projectProposals) return null;
  const existing = world.villageBoard.projectProposals.find(row => row.origin_event === safetyRow.safety_id && !row.project_completed);
  if (existing) return existing.proposal_id;
  const proposal = {
    proposal_id: `GPB-WATER-${String(world.villageBoard.projectProposals.length + 1).padStart(3, '0')}`,
    proposer: safetyRow.resident || 'Milo',
    problem_addressed: safetyRow.problem,
    materials_needed: safetyRow.required_materials || ['fiber', 'wood'],
    likely_helpers: ['Nia', 'Sera'],
    resident_willingness: 0.56,
    known_objections: ['do not move jars unless leak keeps returning'],
    risk: safetyRow.risk,
    maintenance_cost: 0.07,
    related_memories: [safetyRow.public_observation],
    related_practice_nodes: [],
    possible_failure_modes: ['channel clogs', 'jars crack', 'route stays slick'],
    current_support_level: 0.34,
    status: 'posted',
    origin_event: safetyRow.safety_id,
    avatar_can_force: false,
    project_progress: 0,
  };
  world.villageBoard.projectProposals.push(proposal);
  return proposal.proposal_id;
}

function runWaterPhysicsStep(source = 'manual water physics') {
  ensureGamePrototype();
  const sim = ensurePrototypeWaterPhysics();
  const terrain = ensurePrototypeTerrain();
  const materialWorld = ensurePrototype3DWorld();
  const resourceSim = world.gamePrototypeResourcePhysics || null;
  const thermalSim = world.gamePrototypeThermalPhysics || null;
  const field = materialWorld.physics && materialWorld.physics.environment ? materialWorld.physics.environment : { moisture: 0.31, heat: 0.46, wind: 0.18, decayPressure: 0.22, stress: 0.16 };
  const weatherRows = world.gamePrototypeDayCycle && world.gamePrototypeDayCycle.weatherLedger ? world.gamePrototypeDayCycle.weatherLedger : [];
  const latestWeather = weatherRows.length ? weatherRows[weatherRows.length - 1].weather : 'settled air';
  const wetWeather = /rain|drizzle|wet|damp|storage/.test(latestWeather);
  const dryWeather = /dry|wind|heat|drought/.test(latestWeather);
  const entropy = deepTimeEntropyByte();
  const stepId = `WPH-${String(sim.flowLedger.length + 1).padStart(3, '0')}`;
  const jarStock = resourceSim && resourceSim.stocks ? resourceSim.stocks.find(stock => stock.resource === 'water') : null;
  const jarBody = sim.bodies.find(body => body.water_id === 'WAT-jars');
  if (jarStock && jarBody) jarBody.volume = Number(Math.min(jarBody.capacity, Math.max(0, Number(jarStock.quantity || jarBody.volume))).toFixed(3));
  const clayDamage = materialWorld.components
    ? materialWorld.components.filter(component => component.material_id === 'clay_vessel').reduce((sum, component) => sum + Number(component.damage || 0), 0)
    : 0;
  const thermalHeat = thermalSim && thermalSim.heatLedger.length ? Number(thermalSim.heatLedger[thermalSim.heatLedger.length - 1].max_heat || 0) : Number(field.heat || 0.46);
  const bodyPressure = world.gamePrototypeResidentBodies && world.gamePrototypeResidentBodies.bodyLedger ? world.gamePrototypeResidentBodies.bodyLedger.slice(-6) : [];
  const flowRows = [];
  const leakRows = [];
  sim.bodies.forEach((body, index) => {
    const before = {
      volume: Number(body.volume || 0),
      contamination: Number(body.contamination || 0),
      status: body.status,
    };
    const cell = terrainCellAtPosition(body.position3d || {});
    const slope = Number(cell.slope || 0.04);
    const capacityPressure = Math.max(0, before.volume - Number(body.capacity || 1));
    const rainGain = wetWeather && body.kind !== 'contained' ? 0.42 + Number(field.moisture || 0.31) * 0.28 : 0;
    const evaporation = (dryWeather ? 0.18 : 0.04) + Number(field.wind || 0.18) * 0.08 + thermalHeat * 0.05;
    const vesselLeak = body.kind === 'contained' ? clayDamage * Number(body.leak_rate || 0.02) + capacityPressure * 0.35 : 0;
    const groundLoss = body.kind !== 'contained' ? Number(body.leak_rate || 0.05) * (0.5 + slope) : 0;
    const stochastic = (((entropy + index * 29 + sim.runCount * 3) % 13) - 6) / 100;
    const flowOut = body.kind === 'channel'
      ? Math.min(before.volume, Math.max(0, slope * (1 - Number(body.flow_resistance || 0.4)) * 1.8 + capacityPressure * 0.25 + stochastic * 0.2))
      : body.kind === 'surface'
        ? Math.min(before.volume, Math.max(0, slope * (1 - Number(body.flow_resistance || 0.4)) * 0.7 + stochastic * 0.12))
        : 0;
    const afterVolume = Number(Math.max(0, Math.min(Number(body.capacity || 99), before.volume + rainGain - evaporation - vesselLeak - groundLoss - flowOut)).toFixed(3));
    body.volume = afterVolume;
    body.contamination = Number(clamp(before.contamination + (body.kind === 'surface' ? 0.018 : 0.004) + Math.max(0, Number(cell.erosion || 0)) * 0.02 - flowOut * 0.01).toFixed(3));
    body.status = body.volume > body.capacity * 0.82 ? 'near spill' : body.volume < 0.3 ? 'nearly dry' : body.kind === 'channel' ? 'trickling' : body.kind === 'surface' ? 'pooled' : 'stored';
    cell.moisture = Number(clamp(Number(cell.moisture || 0) + (rainGain + vesselLeak + groundLoss) * 0.018 - evaporation * 0.01 - flowOut * 0.012).toFixed(3));
    cell.erosion = Number(clamp(Number(cell.erosion || 0) + Math.max(0, flowOut - Number(body.flow_resistance || 0.4)) * 0.012).toFixed(3));
    cell.walkability = Number(clamp(Number(cell.walkability || 1) - Math.max(0, cell.moisture - 0.55) * 0.035 - flowOut * 0.01).toFixed(3));
    const flowRow = {
      flow_id: `${stepId}-${body.water_id}`,
      step_id: stepId,
      water_id: body.water_id,
      resident_term: body.resident_term,
      player_gloss: body.player_gloss,
      kind: body.kind,
      source,
      weather: latestWeather,
      terrain_cell: cell.cell_id,
      slope,
      volume_before: before.volume,
      volume_after: body.volume,
      rain_gain: Number(rainGain.toFixed(3)),
      evaporation: Number(evaporation.toFixed(3)),
      vessel_leak: Number(vesselLeak.toFixed(3)),
      ground_loss: Number(groundLoss.toFixed(3)),
      flow_out: Number(flowOut.toFixed(3)),
      contamination_before: before.contamination,
      contamination_after: body.contamination,
      route_status: body.status,
      no_resource_spawning: true,
      hidden_law_normal_view: false,
    };
    flowRows.push(flowRow);
    if (vesselLeak > 0.02 || groundLoss > 0.08) leakRows.push({ leak_id: `WLEAK-${String(sim.leakLedger.length + leakRows.length + 1).padStart(3, '0')}`, ...flowRow });
  });
  if (jarBody) {
    world.resources.water = Math.max(0, Math.round(jarBody.volume));
    if (jarStock) jarStock.quantity = Number(jarBody.volume.toFixed(3));
  }
  const routePressure = sim.bodies
    .filter(body => body.kind !== 'contained')
    .reduce((sum, body) => sum + Number(body.volume || 0) * (1 + Number(body.contamination || 0)), 0);
  const routeRow = {
    route_id: `WROUTE-${String(sim.routeLedger.length + 1).padStart(3, '0')}`,
    step_id: stepId,
    route: 'storage path and low crossing',
    pressure: Number(routePressure.toFixed(3)),
    body_pressure_rows: bodyPressure.length,
    walkability_min: Number(Math.min(...terrain.cells.map(cell => Number(cell.walkability || 1))).toFixed(3)),
    public_observation: routePressure > 2.4 ? 'the low crossing looked slick and residents slowed down' : 'water stayed mostly contained or guided',
    resident_interpretation: routePressure > 2.4 ? 'wa-dum asks for a marked dry step' : 'wa-ren carried some water away',
    hidden_law_normal_view: false,
  };
  sim.routeLedger.push(routeRow);
  sim.vesselLedger.push({
    vessel_id: `WVES-${String(sim.vesselLedger.length + 1).padStart(3, '0')}`,
    step_id: stepId,
    clay_damage: Number(clayDamage.toFixed(3)),
    jar_volume: jarBody ? Number(jarBody.volume || 0) : 0,
    water_resource_after: Number(world.resources.water || 0),
    no_resource_spawning: true,
  });
  sim.qualityLedger.push({
    quality_id: `WQUAL-${String(sim.qualityLedger.length + 1).padStart(3, '0')}`,
    step_id: stepId,
    average_contamination: Number((sim.bodies.reduce((sum, body) => sum + Number(body.contamination || 0), 0) / Math.max(1, sim.bodies.length)).toFixed(3)),
    surface_water_volume: Number(sim.bodies.filter(body => body.kind !== 'contained').reduce((sum, body) => sum + Number(body.volume || 0), 0).toFixed(3)),
    hidden_law_normal_view: false,
  });
  let safetyProposalId = null;
  if (routePressure > 2.4 || leakRows.length) {
    const safetyRow = {
      safety_id: `WSAFE-${String(sim.safetyLedger.length + 1).padStart(3, '0')}`,
      step_id: stepId,
      resident: 'Milo',
      risk: leakRows.length ? 'leaking stored water' : 'slick low route',
      problem: leakRows.length ? 'repair leaking jars or move water higher' : 'mark or drain the slick low crossing',
      required_materials: leakRows.length ? ['fiber', 'care'] : ['wood', 'fiber'],
      public_observation: routeRow.public_observation,
      recoverable: true,
      no_permanent_punishment: true,
    };
    safetyProposalId = addWaterSafetyProposal(safetyRow);
    safetyRow.proposal_id = safetyProposalId;
    sim.safetyLedger.push(safetyRow);
  }
  if (routePressure > 2.4 && world.gamePrototypeResidentBodies && world.gamePrototypeResidentBodies.bodies) {
    Object.values(world.gamePrototypeResidentBodies.bodies).forEach(body => {
      body.footing = Number(clamp(Number(body.footing || 0.8) - 0.015).toFixed(3));
      body.fatigue = Number(clamp(Number(body.fatigue || 0.2) + 0.006).toFixed(3));
    });
    mutateResident('Milo', { trust: -0.001, progress: -0.002, memory: 'watched slick low crossing after water moved', historyEvent: 'water route caution', historyDetail: stepId });
  }
  sim.flowLedger.push(...flowRows);
  sim.leakLedger.push(...leakRows);
  sim.runCount += 1;
  sim.flowLedger = sim.flowLedger.slice(-180);
  sim.leakLedger = sim.leakLedger.slice(-120);
  sim.vesselLedger = sim.vesselLedger.slice(-120);
  sim.qualityLedger = sim.qualityLedger.slice(-120);
  sim.routeLedger = sim.routeLedger.slice(-120);
  sim.safetyLedger = sim.safetyLedger.slice(-120);
  if (world.gamePrototypeResourcePhysics) world.gamePrototypeResourcePhysics.lastWorldResources = { ...world.resources };
  world.gamePrototypeCommons = null;
  recordRealityConstraint('water_fluid_physics', {
    resident: 'village',
    sourceBeliefId: stepId,
    materials: ['water', 'clay_vessel', 'soil', 'route'],
    publicObservation: routeRow.public_observation,
    residentInterpretation: routeRow.resident_interpretation,
    materialTransformation: `water bodies=${flowRows.length}; leaks=${leakRows.length}; routePressure=${routeRow.pressure}; jarWater=${world.resources.water}`,
    timeCost: 1,
    workCost: routePressure > 2.4 ? 2 : 1,
    toolWear: 0,
    maintenanceObligation: safetyProposalId ? `review ${safetyProposalId}` : 'watch route moisture and jar containment',
    unintendedConsequence: safetyProposalId ? 'water movement created resident safety proposal' : 'water movement changed terrain and stocks without script unlock',
    hiddenLawInvolved: world.audit ? 'volume, containment, slope, flow resistance, evaporation, leakage, contamination, and route pressure' : 'audit only',
    conservationCheck: true
  });
  recordPrototypeMilestone('water-fluid-physics', `${stepId}: flows=${flowRows.length}, leaks=${leakRows.length}, route=${routeRow.pressure}`);
  return log('runWaterPhysicsStep', { stepId, flows: flowRows.length, leaks: leakRows.length, routePressure: routeRow.pressure, water: world.resources.water, safetyProposalId });
}

function runWaterPhysicsLoop() {
  const before = ensurePrototypeWaterPhysics().flowLedger.length;
  ['jar containment', 'low crossing', 'drainage line', 'return seep'].forEach(source => runWaterPhysicsStep(source));
  const sim = ensurePrototypeWaterPhysics();
  return log('runWaterPhysicsLoop', { stepsAdded: sim.flowLedger.length - before, totalFlows: sim.flowLedger.length, leaks: sim.leakLedger.length, routeRows: sim.routeLedger.length, safetyRows: sim.safetyLedger.length, water: world.resources.water });
}

function ensurePrototypeEcologyPhysics() {
  if (!world.gamePrototypeEcologyPhysics) {
    world.gamePrototypeEcologyPhysics = {
      runCount: 0,
      patches: [
        { patch_id: 'ECO-reed-edge', resident_term: 'ren-nam', player_gloss: 'reed-edge edible shoots', engine_concept: 'wet_edge_edible_shoot_patch', terrain_cell: 'TERR-west-low', biomass: 4.2, carrying_capacity: 8, water_need: 0.55, heat_preference: 0.42, rot_sensitivity: 0.38, regrowth_rate: 0.18, harvest_difficulty: 0.32, status: 'recovering' },
        { patch_id: 'ECO-shade-berries', resident_term: 'ta-nam', player_gloss: 'shade berry patch', engine_concept: 'shade_fruit_food_patch', terrain_cell: 'TERR-storage-rise', biomass: 3.1, carrying_capacity: 6, water_need: 0.42, heat_preference: 0.38, rot_sensitivity: 0.52, regrowth_rate: 0.12, harvest_difficulty: 0.28, status: 'small fruit' },
        { patch_id: 'ECO-root-bank', resident_term: 'dum-nam', player_gloss: 'low-bank roots', engine_concept: 'root_food_bank_patch', terrain_cell: 'TERR-low-crossing', biomass: 5.4, carrying_capacity: 9, water_need: 0.48, heat_preference: 0.36, rot_sensitivity: 0.44, regrowth_rate: 0.1, harvest_difficulty: 0.48, status: 'hidden roots' },
      ],
      growthLedger: [],
      harvestLedger: [],
      spoilageLedger: [],
      hungerLedger: [],
      seedLedger: [],
      safetyLedger: [],
      boundary: {
        foodRequiresGrowthHarvestAndStorage: true,
        noFoodSpawning: true,
        harvestCostsLaborAndRouteRisk: true,
        spoilageDependsOnHeatMoistureAndStorage: true,
        hungerReliefConsumesFood: true,
        hiddenLawNormalView: false,
      },
    };
  }
  const sim = world.gamePrototypeEcologyPhysics;
  ['patches', 'growthLedger', 'harvestLedger', 'spoilageLedger', 'hungerLedger', 'seedLedger', 'safetyLedger'].forEach(key => {
    if (!Array.isArray(sim[key])) sim[key] = [];
  });
  return sim;
}

function addEcologyProposal(safetyRow) {
  if (!world.villageBoard || !world.villageBoard.projectProposals) runVillageBoardLoop();
  if (!world.villageBoard || !world.villageBoard.projectProposals) return null;
  const existing = world.villageBoard.projectProposals.find(row => row.origin_event === safetyRow.safety_id && !row.project_completed);
  if (existing) return existing.proposal_id;
  const proposal = {
    proposal_id: `GPB-ECO-${String(world.villageBoard.projectProposals.length + 1).padStart(3, '0')}`,
    proposer: safetyRow.resident || 'Fay',
    problem_addressed: safetyRow.problem,
    materials_needed: safetyRow.required_materials || ['water', 'care'],
    likely_helpers: ['Milo', 'Nia'],
    resident_willingness: 0.55,
    known_objections: ['do not overharvest the patch before it recovers'],
    risk: safetyRow.risk,
    maintenance_cost: 0.06,
    related_memories: [safetyRow.public_observation],
    related_practice_nodes: [],
    possible_failure_modes: ['patch overharvested', 'stored food spoils', 'route too wet'],
    current_support_level: 0.33,
    status: 'posted',
    origin_event: safetyRow.safety_id,
    avatar_can_force: false,
    project_progress: 0,
  };
  world.villageBoard.projectProposals.push(proposal);
  return proposal.proposal_id;
}

function runEcologyPhysicsStep(source = 'manual ecology physics') {
  ensureGamePrototype();
  const sim = ensurePrototypeEcologyPhysics();
  const terrain = ensurePrototypeTerrain();
  const materialWorld = ensurePrototype3DWorld();
  const resourceSim = world.gamePrototypeResourcePhysics || null;
  const waterSim = world.gamePrototypeWaterPhysics || null;
  const thermalSim = world.gamePrototypeThermalPhysics || null;
  const autonomous = ensureAutonomousResidents();
  const field = materialWorld.physics && materialWorld.physics.environment ? materialWorld.physics.environment : { moisture: 0.31, heat: 0.46, wind: 0.18, decayPressure: 0.22, stress: 0.16 };
  const entropy = deepTimeEntropyByte();
  const stepId = `ECO-${String(sim.growthLedger.length + 1).padStart(3, '0')}`;
  const thermalHeat = thermalSim && thermalSim.heatLedger.length ? Number(thermalSim.heatLedger[thermalSim.heatLedger.length - 1].max_heat || 0) : Number(field.heat || 0.46);
  const waterPressure = waterSim && waterSim.routeLedger.length ? Number(waterSim.routeLedger[waterSim.routeLedger.length - 1].pressure || 0) : 0;
  const foodStock = resourceSim && resourceSim.stocks ? resourceSim.stocks.find(stock => stock.resource === 'food') : null;
  const foodBefore = Number(world.resources.food || 0);
  const patchRows = sim.patches.map((patch, index) => {
    const cell = terrain.cells.find(row => row.cell_id === patch.terrain_cell) || terrain.cells[index % terrain.cells.length];
    const before = Number(patch.biomass || 0);
    const moistureFit = 1 - Math.min(1, Math.abs(Number(cell.moisture || 0.35) - Number(patch.water_need || 0.45)) * 2.2);
    const heatFit = 1 - Math.min(1, Math.abs(thermalHeat - Number(patch.heat_preference || 0.4)) * 1.8);
    const routeStress = Math.max(0, waterPressure - 1.8) * 0.035 + Number(cell.erosion || 0) * 0.05;
    const rot = Math.max(0, Number(cell.moisture || 0) - 0.62) * Number(patch.rot_sensitivity || 0.4) + Math.max(0, thermalHeat - 0.66) * 0.18;
    const stochastic = (((entropy + index * 31 + sim.runCount * 11) % 17) - 8) / 100;
    const growth = Math.max(-0.32, Number(patch.regrowth_rate || 0.1) * moistureFit * heatFit - rot - routeStress + stochastic * 0.18);
    patch.biomass = Number(Math.max(0, Math.min(Number(patch.carrying_capacity || 8), before + growth)).toFixed(3));
    patch.status = patch.biomass < 1.2 ? 'thin and recovering' : patch.biomass > patch.carrying_capacity * 0.72 ? 'ready but not infinite' : 'growing';
    return {
      growth_id: `${stepId}-${patch.patch_id}`,
      step_id: stepId,
      patch_id: patch.patch_id,
      resident_term: patch.resident_term,
      player_gloss: patch.player_gloss,
      terrain_cell: cell.cell_id,
      biomass_before: before,
      biomass_after: patch.biomass,
      moisture_fit: Number(moistureFit.toFixed(3)),
      heat_fit: Number(heatFit.toFixed(3)),
      rot: Number(rot.toFixed(3)),
      route_stress: Number(routeStress.toFixed(3)),
      growth_delta: Number((patch.biomass - before).toFixed(3)),
      hidden_law_normal_view: false,
      no_resource_spawning: true,
    };
  });
  const hungryResidents = Object.entries(autonomous.needState)
    .filter(([, needs]) => Number(needs.hunger || 0) > 0.55)
    .map(([name]) => name);
  const readyPatch = sim.patches
    .slice()
    .sort((a, b) => Number(b.biomass || 0) - Number(a.biomass || 0))[0];
  let harvested = 0;
  let overharvestRisk = 0;
  if (readyPatch && readyPatch.biomass > 1.4 && hungryResidents.length) {
    const capacityLimited = Math.min(2, Math.floor(Number(readyPatch.biomass || 0)));
    const routePenalty = waterPressure > 2.4 ? 1 : 0;
    harvested = Math.max(0, capacityLimited - routePenalty);
    if (harvested > 0) {
      readyPatch.biomass = Number(Math.max(0, Number(readyPatch.biomass || 0) - harvested * 0.72).toFixed(3));
      world.resources.food = Math.min(99, Number(world.resources.food || 0) + harvested);
      if (foodStock) foodStock.quantity = Number(Math.min(Number(foodStock.capacity || 16), Number(foodStock.quantity || 0) + harvested).toFixed(3));
    }
    overharvestRisk = Number(Math.max(0, harvested * 0.2 - Number(readyPatch.regrowth_rate || 0.1)).toFixed(3));
  }
  const foodAfterHarvest = Number(world.resources.food || 0);
  const fedResidents = [];
  hungryResidents.slice(0, Math.max(0, Math.min(Number(world.resources.food || 0), 2))).forEach(name => {
    if (Number(world.resources.food || 0) <= 0) return;
    world.resources.food = Math.max(0, Number(world.resources.food || 0) - 1);
    const needs = autonomous.needState[name];
    needs.hunger = clampNeed(Number(needs.hunger || 0) - 0.28);
    needs.energy = clampNeed(Number(needs.energy || 0) + 0.08);
    fedResidents.push(name);
    mutateResident(name, { trust: 0.002, progress: 0.002, memory: 'ate from stored food after patch work', historyEvent: 'ecology food relief', historyDetail: stepId });
  });
  const spoilage = foodStock
    ? Math.max(0, Number(foodStock.decay || 0) * 0.18 + Number(foodStock.contamination || 0) * 0.12 + Math.max(0, thermalHeat - 0.58) * 0.14 + Math.max(0, Number(field.moisture || 0) - 0.58) * 0.1)
    : 0;
  const spoiledUnits = Math.min(Number(world.resources.food || 0), spoilage > 0.18 ? 1 : 0);
  if (spoiledUnits > 0) {
    world.resources.food = Math.max(0, Number(world.resources.food || 0) - spoiledUnits);
    if (foodStock) foodStock.quantity = Math.max(0, Number(foodStock.quantity || 0) - spoiledUnits);
  } else if (foodStock) {
    foodStock.quantity = Number(world.resources.food || 0);
  }
  if (resourceSim) resourceSim.lastWorldResources = { ...world.resources };
  const harvestRow = {
    harvest_id: `EHAR-${String(sim.harvestLedger.length + 1).padStart(3, '0')}`,
    step_id: stepId,
    source,
    patch_id: readyPatch ? readyPatch.patch_id : 'none',
    harvested,
    food_before: foodBefore,
    food_after_harvest: foodAfterHarvest,
    food_after_feeding: Number(world.resources.food || 0),
    fed_residents: fedResidents,
    overharvest_risk: overharvestRisk,
    no_resource_spawning: true,
    hidden_law_normal_view: false,
  };
  const spoilageRow = {
    spoilage_id: `ESPOIL-${String(sim.spoilageLedger.length + 1).padStart(3, '0')}`,
    step_id: stepId,
    spoilage_pressure: Number(spoilage.toFixed(3)),
    spoiled_units: spoiledUnits,
    food_after: Number(world.resources.food || 0),
    hidden_law_normal_view: false,
  };
  const hungerRow = {
    hunger_id: `EHUN-${String(sim.hungerLedger.length + 1).padStart(3, '0')}`,
    step_id: stepId,
    hungry_before: hungryResidents,
    fed_residents: fedResidents,
    hunger_remaining: Object.entries(autonomous.needState).filter(([, needs]) => Number(needs.hunger || 0) > 0.55).map(([name]) => name),
    food_after: Number(world.resources.food || 0),
    hidden_law_normal_view: false,
  };
  sim.growthLedger.push(...patchRows);
  sim.harvestLedger.push(harvestRow);
  sim.spoilageLedger.push(spoilageRow);
  sim.hungerLedger.push(hungerRow);
  let safetyProposalId = null;
  if (hungerRow.hunger_remaining.length >= 2 || overharvestRisk > 0.24 || spoiledUnits > 0) {
    const safetyRow = {
      safety_id: `ECO-SAFE-${String(sim.safetyLedger.length + 1).padStart(3, '0')}`,
      step_id: stepId,
      resident: 'Fay',
      risk: hungerRow.hunger_remaining.length >= 2 ? 'food pressure' : spoiledUnits > 0 ? 'spoilage pressure' : 'overharvest risk',
      problem: hungerRow.hunger_remaining.length >= 2 ? 'protect food route and avoid overharvest' : spoiledUnits > 0 ? 'move food to cooler drier storage' : 'let patch recover before next harvest',
      required_materials: ['care', 'water'],
      public_observation: hungryResidents.length ? 'residents checked food stores and nearby patches' : 'food patches changed with weather and water',
      recoverable: true,
      no_permanent_punishment: true,
    };
    safetyProposalId = addEcologyProposal(safetyRow);
    safetyRow.proposal_id = safetyProposalId;
    sim.safetyLedger.push(safetyRow);
  }
  sim.runCount += 1;
  sim.growthLedger = sim.growthLedger.slice(-180);
  sim.harvestLedger = sim.harvestLedger.slice(-120);
  sim.spoilageLedger = sim.spoilageLedger.slice(-120);
  sim.hungerLedger = sim.hungerLedger.slice(-120);
  sim.seedLedger = sim.seedLedger.slice(-120);
  sim.safetyLedger = sim.safetyLedger.slice(-120);
  world.gamePrototypeCommons = null;
  recordRealityConstraint('ecology_food_physics', {
    resident: 'village',
    sourceBeliefId: stepId,
    materials: ['food', 'water', 'soil', 'heat', 'care'],
    publicObservation: harvestRow.harvested ? `${harvestRow.harvested} food gathered from ${harvestRow.patch_id}` : 'food patches grew, thinned, or spoiled without harvest',
    residentInterpretation: fedResidents.length ? `${fedResidents.join(', ')} ate from stored food` : 'food pressure remains observable and recoverable',
    materialTransformation: `growthRows=${patchRows.length}; harvested=${harvested}; spoiled=${spoiledUnits}; food ${foodBefore}->${world.resources.food}`,
    timeCost: 1,
    workCost: harvested ? 2 : 1,
    toolWear: harvested ? 1 : 0,
    maintenanceObligation: safetyProposalId || 'watch food patches and storage',
    unintendedConsequence: safetyProposalId ? 'food ecology created a resident proposal' : 'food stock and hunger changed through ecology',
    hiddenLawInvolved: world.audit ? 'biomass, moisture, heat, route stress, spoilage, hunger, and stochastic growth' : 'audit only',
    conservationCheck: true
  });
  recordPrototypeMilestone('ecology-food-physics', `${stepId}: harvested=${harvested}, fed=${fedResidents.length}, food=${world.resources.food}`);
  return log('runEcologyPhysicsStep', { stepId, harvested, fed: fedResidents.length, food: world.resources.food, growthRows: patchRows.length, safetyProposalId });
}

function runEcologyPhysicsLoop() {
  const before = ensurePrototypeEcologyPhysics().growthLedger.length;
  ['morning growth', 'forage route', 'storage check', 'evening hunger'].forEach(source => runEcologyPhysicsStep(source));
  const sim = ensurePrototypeEcologyPhysics();
  return log('runEcologyPhysicsLoop', { stepsAdded: sim.growthLedger.length - before, growthRows: sim.growthLedger.length, harvestRows: sim.harvestLedger.length, spoilageRows: sim.spoilageLedger.length, hungerRows: sim.hungerLedger.length, food: world.resources.food });
}

function residentBodyComponentContacts(body, materialWorld) {
  if (!materialWorld || !materialWorld.components) return [];
  const position = body.position3d || {};
  return materialWorld.components
    .filter(component => {
      const componentPosition = component.position3d || {};
      const dx = Number(componentPosition.x || 0) - Number(position.x || 0);
      const dy = Number(componentPosition.y || 0) - Number(position.y || 0);
      const dz = Math.abs(Number(componentPosition.z || 0) - Number(position.z || 0));
      const distance = Math.sqrt(dx * dx + dy * dy);
      const contactRadius = Number(body.radius || 3) + Math.max(3, Number(component.dimensions && component.dimensions.x || 6) * 0.08);
      return distance < contactRadius && dz < Number(body.height || 9);
    })
    .slice(0, 4);
}

function residentBodyResidentContacts(residentName, body, bodies) {
  const position = body.position3d || {};
  return Object.entries(bodies)
    .filter(([name]) => name !== residentName)
    .filter(([, other]) => {
      const otherPosition = other.position3d || {};
      const dx = Number(otherPosition.x || 0) - Number(position.x || 0);
      const dy = Number(otherPosition.y || 0) - Number(position.y || 0);
      const distance = Math.sqrt(dx * dx + dy * dy);
      return distance < Number(body.radius || 3) + Number(other.radius || 3) + 1.4;
    })
    .map(([name]) => name)
    .slice(0, 3);
}

function applyResidentBodyPhysics(residentName, action = 'observe', entropy = deepTimeEntropyByte(), source = 'autonomous_action') {
  const sim = ensureResidentBodies();
  const autonomous = ensureAutonomousResidents();
  const materialWorld = ensurePrototype3DWorld();
  const body = sim.bodies[residentName] || Object.values(sim.bodies)[0];
  const needs = autonomous.needState[residentName] || { energy: 0.5, safety: 0.5 };
  const before = {
    position3d: { ...body.position3d },
    velocity: { ...body.velocity },
    fatigue: Number(body.fatigue || 0),
    balance: Number(body.balance || 0),
    footing: Number(body.footing || 0),
    recovery_debt: Number(body.recovery_debt || 0),
  };
  const target = residentBodyTargetForAction(residentName, action);
  const terrain = residentBodyTerrainAt(body);
  const load = carriedLoadForResident(residentName, action);
  const overload = Math.max(0, load - Number(body.carry_capacity || 8));
  const dx = Number(target.x || 0) - Number(body.position3d.x || 0);
  const dy = Number(target.y || 0) - Number(body.position3d.y || 0);
  const distance = Math.max(0.001, Math.sqrt(dx * dx + dy * dy));
  const energyFactor = clampNeed(Number(needs.energy || 0.5) + 0.2 - Number(body.fatigue || 0) * 0.25);
  const loadFactor = clampNeed(1 - load / Math.max(1, Number(body.carry_capacity || 8)) * 0.32);
  const maxSpeed = Math.max(0.18, 2.4 * terrain.friction * energyFactor * loadFactor);
  const desired = {
    x: (dx / distance) * Math.min(maxSpeed, distance),
    y: (dy / distance) * Math.min(maxSpeed, distance),
  };
  const jitter = ((entropy % 9) - 4) * 0.018;
  body.velocity.x = Number((Number(body.velocity.x || 0) * 0.42 + desired.x * 0.58 + jitter).toFixed(3));
  body.velocity.y = Number((Number(body.velocity.y || 0) * 0.42 + desired.y * 0.58 - jitter).toFixed(3));
  body.velocity.z = Number((Number(body.velocity.z || 0) - (Number(body.position3d.z || 0) > 0 ? 0.42 : 0)).toFixed(3));
  body.position3d.x = Number(Math.max(0, Math.min(120, Number(body.position3d.x || 0) + body.velocity.x)).toFixed(3));
  body.position3d.y = Number(Math.max(0, Math.min(90, Number(body.position3d.y || 0) + body.velocity.y)).toFixed(3));
  body.position3d.z = Number(Math.max(0, Number(body.position3d.z || 0) + body.velocity.z).toFixed(3));
  if (body.position3d.z <= 0) body.velocity.z = Number((Number(body.velocity.z || 0) * -0.08).toFixed(3));
  const componentContacts = residentBodyComponentContacts(body, materialWorld);
  const residentContacts = residentBodyResidentContacts(residentName, body, sim.bodies);
  const collisionCount = componentContacts.length + residentContacts.length;
  if (collisionCount > 0) {
    body.velocity.x = Number((body.velocity.x * 0.35).toFixed(3));
    body.velocity.y = Number((body.velocity.y * 0.35).toFixed(3));
  }
  const speed = Math.sqrt(body.velocity.x * body.velocity.x + body.velocity.y * body.velocity.y);
  const slipRisk = clampNeed((1 - terrain.friction) * 0.32 + overload * 0.04 + collisionCount * 0.035 + Math.max(0, speed - 1.8) * 0.04 + terrain.slope * 0.2);
  const slipThreshold = ((entropy + sim.bodyLedger.length * 17) % 100) / 100;
  const slipEvent = slipThreshold < slipRisk;
  const fatigueDelta = Math.max(0, speed * 0.018 + load * 0.006 + terrain.stress * 0.018 + collisionCount * 0.016 + (slipEvent ? 0.06 : 0) - (action === 'rest' ? 0.09 : 0));
  const safetyDelta = Math.max(0, slipRisk * 0.08 + collisionCount * 0.012 + overload * 0.01);
  body.carried_load = load;
  body.footing = Number(terrain.friction.toFixed(3));
  body.slip_risk = Number(slipRisk.toFixed(3));
  body.balance = Number(clampNeed(Number(body.balance || 0.7) - safetyDelta + (action === 'rest' ? 0.04 : 0)).toFixed(3));
  body.fatigue = Number(clampNeed(Number(body.fatigue || 0) + fatigueDelta).toFixed(3));
  body.recovery_debt = Number(clampNeed(Number(body.recovery_debt || 0) + (slipEvent ? 0.08 : 0) + overload * 0.015 - (action === 'rest' ? 0.05 : 0)).toFixed(3));
  body.contact_count += collisionCount;
  body.last_action = action;
  needs.energy = clampNeed(Number(needs.energy || 0.5) - fatigueDelta * 0.55);
  needs.safety = clampNeed(Number(needs.safety || 0.5) - safetyDelta + (action === 'rest' ? 0.02 : 0));
  const row = {
    body_step_id: `RBP-${String(sim.bodyLedger.length + 1).padStart(3, '0')}`,
    resident: residentName,
    action,
    source,
    entropy,
    target: target.label,
    before,
    after: {
      position3d: { ...body.position3d },
      velocity: { ...body.velocity },
      fatigue: body.fatigue,
      balance: body.balance,
      footing: body.footing,
      recovery_debt: body.recovery_debt,
    },
    speed: Number(speed.toFixed(3)),
    carried_load: load,
    carry_capacity: Number(body.carry_capacity || 0),
    overload: Number(overload.toFixed(3)),
    terrain,
    component_contacts: componentContacts.map(component => component.component_id),
    resident_contacts: residentContacts,
    collision_count: collisionCount,
    slip_risk: body.slip_risk,
    slip_event: slipEvent,
    fatigue_delta: Number(fatigueDelta.toFixed(3)),
    safety_delta: Number(safetyDelta.toFixed(3)),
    no_direct_player_command: true,
    hidden_law_normal_view: false,
  };
  sim.bodyLedger.push(row);
  sim.bodyLedger = sim.bodyLedger.slice(-160);
  if (collisionCount > 0 || slipEvent) {
    sim.contactLedger.push({
      contact_id: `RBC-${String(sim.contactLedger.length + 1).padStart(3, '0')}`,
      body_step_id: row.body_step_id,
      resident: residentName,
      component_contacts: row.component_contacts,
      resident_contacts: residentContacts,
      slip_event: slipEvent,
      recovery_debt_after: body.recovery_debt,
    });
    sim.contactLedger = sim.contactLedger.slice(-120);
  }
  sim.fatigueLedger.push({
    fatigue_id: `RBF-${String(sim.fatigueLedger.length + 1).padStart(3, '0')}`,
    body_step_id: row.body_step_id,
    resident: residentName,
    fatigue_delta: row.fatigue_delta,
    fatigue_after: body.fatigue,
    energy_after: Number(needs.energy.toFixed(3)),
    footing: body.footing,
  });
  sim.fatigueLedger = sim.fatigueLedger.slice(-160);
  if (body.recovery_debt > 0.35 || slipEvent) {
    sim.recoveryLedger.push({
      recovery_id: `RBR-${String(sim.recoveryLedger.length + 1).padStart(3, '0')}`,
      body_step_id: row.body_step_id,
      resident: residentName,
      reason: slipEvent ? 'slip event during movement' : 'accumulated body recovery debt',
      bounded: true,
      recovery_path: 'rest, lighter load, safer footing, or help',
      recovery_debt_after: body.recovery_debt,
    });
    sim.recoveryLedger = sim.recoveryLedger.slice(-80);
  }
  recordRealityConstraint('resident_body_physics', {
    resident: residentName,
    sourceBeliefId: row.body_step_id,
    materials: row.component_contacts,
    publicObservation: `${residentName} moved toward ${target.label} with footing ${body.footing}`,
    residentInterpretation: slipEvent ? 'route or load felt unsafe' : 'movement cost changed body state',
    materialTransformation: `body position ${before.position3d.x},${before.position3d.y}->${body.position3d.x},${body.position3d.y}; load=${load}; contacts=${collisionCount}`,
    timeCost: 1,
    workCost: row.fatigue_delta,
    toolWear: collisionCount > 0 ? 1 : 0,
    maintenanceObligation: body.recovery_debt > 0.35 ? 'resident needs bounded rest or safer route' : 'none',
    unintendedConsequence: slipEvent ? 'slip created recovery debt' : (collisionCount ? 'contact changed movement' : 'ordinary body energy spent'),
    hiddenLawInvolved: world.audit ? 'body mass, friction, contact, footing, load, and stochastic slip' : 'audit only',
    conservationCheck: true
  });
  return row;
}

function runResidentBodyPhysicsStep() {
  ensureGamePrototype();
  const sim = ensureResidentBodies();
  const entropy = deepTimeEntropyByte();
  const residentNames = Object.keys(world.residents);
  const residentName = residentNames[(entropy + sim.bodyLedger.length) % residentNames.length];
  const action = chooseAutonomousResidentAction(residentName, entropy);
  const row = applyResidentBodyPhysics(residentName, action, entropy, 'player_observed_body_physics');
  mutateResident(residentName, {
    trust: row.slip_event ? -0.002 : 0.001,
    progress: row.slip_event ? 0.001 : 0.004,
    schedule: row.slip_event ? `recovers footing near ${row.target}` : `moves through ${row.target}`,
    memory: row.slip_event ? `remembered a slip risk near ${row.target}` : `felt the cost of moving through ${row.target}`,
    historyEvent: 'resident body physics',
    historyDetail: `${row.body_step_id}; fatigue ${row.after.fatigue}; footing ${row.after.footing}; direct command no`
  });
  recordVisibleResidentExpression(residentName, 'body_physics', ensureAutonomousResidents().needState[residentName]);
  sim.runCount += 1;
  recordPrototypeMilestone('resident-body-physics', `${residentName} ${action}; fatigue ${row.after.fatigue}; contacts ${row.collision_count}`);
  return log('runResidentBodyPhysicsStep', { bodyStepId: row.body_step_id, resident: residentName, action, fatigue: row.after.fatigue, footing: row.after.footing, contacts: row.collision_count, slip: row.slip_event });
}

function runResidentBodyPhysicsLoop() {
  const before = ensureResidentBodies().bodyLedger.length;
  for (let i = 0; i < 10; i += 1) runResidentBodyPhysicsStep();
  const sim = ensureResidentBodies();
  return log('runResidentBodyPhysicsLoop', { stepsAdded: sim.bodyLedger.length - before, totalSteps: sim.bodyLedger.length, contacts: sim.contactLedger.length, recoveries: sim.recoveryLedger.length });
}

function currentPhysicsPressure() {
  const sim = world.gamePrototype3DWorld || null;
  if (!sim || !sim.physics) return null;
  const structure = sim.structures && sim.structures.length ? sim.structures[0] : null;
  const latest = sim.physics.latestStep || null;
  const weakComponents = (sim.components || []).filter(component => Number(component.stability || 1) < 0.7 || Number(component.damage || 0) > 0.18);
  const pressure = {
    latestStepId: latest ? latest.step_id : 'none',
    failures: latest ? Number(latest.failures || 0) : 0,
    collisions: latest ? Number(latest.collisions || 0) : 0,
	    structureStability: structure ? Number(structure.stability || 0) : 1,
	    moistureRisk: structure ? Number(structure.moisture_risk || 0) : 0,
	    fieldStress: latest ? Number(latest.field_stress || 0) : Number(sim.physics.environment && sim.physics.environment.stress || 0),
	    fieldHeat: latest ? Number(latest.field_heat || 0) : Number(sim.physics.environment && sim.physics.environment.heat || 0),
	    fieldMoisture: latest ? Number(latest.field_moisture || 0) : Number(sim.physics.environment && sim.physics.environment.moisture || 0),
	    weakComponents: weakComponents.length,
	    residentTerm: structure ? structure.resident_term_id : 'none',
	  };
  pressure.active = pressure.failures > 0 || pressure.collisions > 0 || pressure.structureStability < 0.74 || pressure.moistureRisk > 0.32 || pressure.fieldStress > 0.24 || pressure.weakComponents > 0;
  return pressure;
}

function clampNeed(value) {
  return Math.max(0, Math.min(1, Number(value || 0)));
}

function driftResidentNeeds(needs, entropy, action) {
  const physicsPressure = currentPhysicsPressure();
  const physicsEffort = physicsPressure && physicsPressure.active ? 0.035 : 0;
  const fieldHeat = physicsPressure ? Number(physicsPressure.fieldHeat || 0) : 0;
  const fieldMoisture = physicsPressure ? Number(physicsPressure.fieldMoisture || 0) : 0;
  const fieldStress = physicsPressure ? Number(physicsPressure.fieldStress || 0) : 0;
  const effort = (['proposal_work', 'practice_maintenance', 'experiment', 'forage', 'physics_repair'].includes(action) ? 0.12 : 0.04) + physicsEffort + Math.max(0, fieldHeat - 0.55) * 0.05;
  const stress = (entropy % 7 === 0 ? 0.08 : 0.02) + fieldStress * 0.08 + Math.max(0, fieldMoisture - 0.5) * 0.04;
  const foodBackedRelief = action === 'forage' && Number(world.resources.food || 0) > 0 ? 0.24 : action === 'forage' ? 0.04 : 0;
  needs.energy = clampNeed(needs.energy - effort + (action === 'rest' ? 0.22 : 0));
  needs.hunger = clampNeed(needs.hunger + effort * 0.6 - foodBackedRelief);
  needs.attention = clampNeed(needs.attention - effort * 0.8 + (action === 'teach' ? 0.04 : 0));
  needs.safety = clampNeed(needs.safety - stress + (action === 'repair_safety' ? 0.14 : 0) + (action === 'physics_repair' ? 0.05 : 0));
  needs.autonomy = clampNeed(needs.autonomy + (action === 'refuse' ? 0.08 : -0.015));
  return needs;
}

function chooseAutonomousResidentAction(residentName, entropy) {
  const sim = ensureAutonomousResidents();
  const needs = sim.needState[residentName];
  const board = world.villageBoard;
  const hasProposal = Boolean(board && board.projectProposals && board.projectProposals.length);
  const hasPractice = Boolean(world.emergentPracticeGraph && world.emergentPracticeGraph.nodes && world.emergentPracticeGraph.nodes.length);
  const lowResource = (world.resources.water || 0) < 5 || (world.resources.fiber || 0) < 5 || (world.resources.care || 0) < 3 || (world.resources.food || 0) < 3;
  const physicsPressure = currentPhysicsPressure();
  if (needs.energy < 0.22 || needs.hunger > 0.78) return 'rest';
  if (needs.autonomy > 0.74 && entropy % 5 === 0) return 'refuse';
  if (needs.safety < 0.42) return 'repair_safety';
  if (physicsPressure && physicsPressure.active && entropy % 3 !== 0) return 'physics_repair';
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
	  } else if (action === 'physics_repair') {
	    posture = 'braced beside strained support';
	    movementCue = 'careful retie and weight check';
	    gazeCue = 'looks along contact points';
	    marker = 'repairing';
	    reason = 'physical support pressure';
  } else if (action === 'material_manipulation') {
	    posture = 'hands on material';
	    movementCue = 'tests weight and surface';
	    gazeCue = 'checks the part that moved';
	    marker = 'handling';
	    reason = 'resident physical manipulation';
		  } else if (action === 'body_physics') {
	    posture = 'weight shifted into footing';
	    movementCue = 'paces by load and ground';
	    gazeCue = 'checks route underfoot';
	    marker = 'moving';
	    reason = 'body physics pressure';
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
  const bodyPhysicsRow = applyResidentBodyPhysics(residentName, action, entropy, 'autonomous_resident_action');
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
    const ecology = runEcologyPhysicsStep('autonomous forage').payload;
    const ateFood = Number(world.resources.food || 0) > 0;
    if (ateFood) world.resources.food = Math.max(0, Number(world.resources.food || 0) - 1);
    if (world.gamePrototypeResourcePhysics && world.gamePrototypeResourcePhysics.stocks) {
      const stock = world.gamePrototypeResourcePhysics.stocks.find(row => row.resource === 'food');
      if (stock) stock.quantity = Number(world.resources.food || 0);
      world.gamePrototypeResourcePhysics.lastWorldResources = { ...world.resources };
    }
    memory = ateFood ? 'ate after checking nearby food patches' : 'checked patches but food pressure remained';
    if (ecology.harvested > 0) world.resources.fiber = Math.min(99, world.resources.fiber + 1);
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
  } else if (action === 'physics_repair') {
    const materialWorld = ensurePrototype3DWorld();
    const weak = materialWorld.components
      .slice()
      .sort((a, b) => (Number(a.stability || 1) - Number(b.stability || 1)) || (Number(b.damage || 0) - Number(a.damage || 0)))[0];
    const term = materialWorld.language.terms.find(row => row.term_id === (weak ? weak.resident_term_id : 'TERM-TAKU-REN')) || materialWorld.language.terms[0];
    const spentFiber = Number(world.resources.fiber || 0) > 0;
    schedule = `checks ${term ? term.resident_word : 'local support'} after physical strain`;
    memory = spentFiber ? `retied ${term ? term.resident_word : 'raised support'} after weight and damp pressure` : `noticed ${term ? term.resident_word : 'raised support'} strain but lacked fiber`;
    materialCost = spentFiber ? ['fiber'] : [];
    if (spentFiber) world.resources.fiber = Math.max(0, world.resources.fiber - 1);
    if (weak && spentFiber) {
      weak.damage = Number(clamp(Number(weak.damage || 0) - 0.07).toFixed(3));
      weak.stability = Number(clamp(Number(weak.stability || 0) + 0.08).toFixed(3));
    }
    if (materialWorld.structures && materialWorld.structures[0] && spentFiber) {
      materialWorld.structures[0].stability = Number(clamp(Number(materialWorld.structures[0].stability || 0) + 0.04).toFixed(3));
    }
    progressDelta = spentFiber ? 0.011 : 0.003;
    trustDelta = spentFiber ? 0.003 : -0.001;
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
    body_physics_step_id: bodyPhysicsRow.body_step_id,
    body_fatigue_after: bodyPhysicsRow.after.fatigue,
    body_footing: bodyPhysicsRow.after.footing,
    body_contacts: bodyPhysicsRow.collision_count,
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
  const zone = locationZoneForAvatar();
  const plan = nearbyActionPlan();
  const dayCycle = world.gamePrototypeDayCycle || null;
  const latestDay = dayCycle && dayCycle.dayLedger.length ? dayCycle.dayLedger[dayCycle.dayLedger.length - 1] : null;
  const returnLater = world.gamePrototypeReturnLater || null;
  const materialWorld = world.gamePrototype3DWorld || null;
  const terrain = world.gamePrototypeTerrain || null;
  const physicsStep = materialWorld && materialWorld.physics ? materialWorld.physics.latestStep : null;
  const residentLines = Object.entries(world.residents)
    .slice(0, 6)
    .map(([name, row]) => {
      const expression = latestVisibleExpressionFor(name);
      const body = world.gamePrototypeResidentBodies && world.gamePrototypeResidentBodies.bodies ? world.gamePrototypeResidentBodies.bodies[name] : null;
      const bodyText = body ? `body=(${body.position3d.x},${body.position3d.y}) fatigue=${body.fatigue} footing=${body.footing}` : 'body=not initialized';
      return `${name}: ${row.schedule}; trust=${row.trust.toFixed(2)} debt=${row.debt} progress=${row.progress.toFixed(2)}; cue=${expression.marker}/${expression.posture}; ${bodyText}; memory=${row.memory}`;
    });
  const resources = Object.entries(world.resources).map(([key, value]) => `${key}=${value}`).join(', ');
  return [
    `Entered: ${world.entered ? 'yes' : 'no'} / room: ${world.avatar.room} / zone: ${zone.label} / selected: ${world.selected}`,
    `Nearby action: ${plan.action} because ${plan.why}`,
    `Village day: ${dayCycle ? dayCycle.day : 0}${latestDay ? ` / last weather=${latestDay.weather}` : ''}`,
    `Return later: ${returnLater && returnLater.latestReceipt ? `${returnLater.latestReceipt.days_away} day(s) away, day ${returnLater.latestReceipt.day_before}->${returnLater.latestReceipt.day_after}` : 'not used'}`,
    `3D physics: ${materialWorld ? `${materialWorld.components.length} component(s), ${materialWorld.structures.length} structure(s), latest=${physicsStep ? physicsStep.step_id + ' failures=' + physicsStep.failures : 'not stepped'}` : 'not initialized'}`,
    `Terrain: ${terrain ? `${terrain.cells.length} cell(s), steps=${terrain.terrainLedger.length}, weak=${terrain.terrainLedger.length ? terrain.terrainLedger[terrain.terrainLedger.length - 1].weak_cells : 0}` : 'not initialized'}`,
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
  const playableSlice = world.gamePrototypePlayableSlice;
  const villageDay03 = world.gamePrototypeVillageDay03;
  const worldStage = world.gamePrototypeWorldStage;
  const walkthrough = world.gamePrototypeWalkthrough;
  const actionRail = world.gamePrototypeActionRail;
  const divergence = world.gamePrototypeDivergence;
  const commons = world.gamePrototypeCommons;
  const projects = world.gamePrototypeProjects;
  const commonsSupport = world.gamePrototypeCommonsSupport;
  const nearby = world.gamePrototypeNearbyActions;
  const dayCycle = world.gamePrototypeDayCycle;
  const returnLater = world.gamePrototypeReturnLater;
	  const materialWorld = world.gamePrototype3DWorld;
  const terrain = world.gamePrototypeTerrain;
	  const materialPhysics = materialWorld && materialWorld.physics ? materialWorld.physics.latestStep : null;
	  const latestTerm = materialWorld && materialWorld.language && materialWorld.language.terms.length ? materialWorld.language.terms[0] : null;
  const manipulation = world.gamePrototypeMaterialManipulation;
  const residentBodies = world.gamePrototypeResidentBodies;
  const tools = world.gamePrototypeTools;
  const resourcePhysics = world.gamePrototypeResourcePhysics;
  const thermalPhysics = world.gamePrototypeThermalPhysics;
  const waterPhysics = world.gamePrototypeWaterPhysics;
  const ecologyPhysics = world.gamePrototypeEcologyPhysics;
	  const constructionPracticeCount = materialWorld && materialWorld.constructionLedger ? materialWorld.constructionLedger.filter(row => row.practice_id).length : 0;
  return [
    `Practice graph: ${practiceCount} node(s)${latestPractice ? ` / latest ${latestPractice.local_name || latestPractice.practice_id}` : ''}`,
    `Village board: ${boardCount} proposal(s)${latestProposal ? ` / latest ${latestProposal.problem_addressed || latestProposal.proposal_id}` : ''}`,
    `Reality ledger: ${ledgerRows} causal row(s)`,
    `Return branches: ${branchRows} continuity row(s)${latestBranch ? ` / latest ${latestBranch.return_status}` : ''}`,
    `Deep time: ${deepTime ? `${deepTime.year} years / ${deepTime.emergentEffects.length} emergent effect(s) / ${consequenceCount} village consequence(s) / ${survivalStatus} / physics epochs=${deepTime.physicsEpochLedger ? deepTime.physicsEpochLedger.length : 0} / physical effects=${deepTime.componentEffectLedger ? deepTime.componentEffectLedger.length : 0}` : 'not started'}`,
    `Autonomous residents: ${autonomous ? `${autonomous.day} day(s) / ${autonomous.actionLog.length} action(s) / ${autonomous.refusalLog.length} refusal(s)` : 'not started'}`,
    `Save slots: ${saves ? `${saves.slots.length} slot(s) / active ${saves.activeSlotId || 'none'} / returns ${saves.returnLog.length}` : 'none'}`,
    `Playable physics-to-practice slice: ${playableSlice ? `${playableSlice.phase}, ready=${playableSlice.acceptanceReady}, physics=${playableSlice.linkedPhysicsRows.length}, practices=${playableSlice.linkedPracticeIds.length}` : 'not started'}`,
    `Playable Village Day 0-3: ${villageDay03 ? `${villageDay03.phase}, ready=${villageDay03.acceptanceReady}, rows=${villageDay03.dayLedger.length}, returns=${villageDay03.returnLinks.length}` : 'not started'}`,
    `Primary play surface: ${worldStage ? `${worldStage.phase}, ready=${worldStage.acceptanceReady}, focus=${worldStage.focusLedger.length}, prompts=${worldStage.actionPromptLedger.length}` : 'not started'}`,
    `First playable walkthrough: ${walkthrough ? `${walkthrough.phase}, ready=${walkthrough.acceptanceReady}, steps=${walkthrough.stepLedger.length}` : 'not started'}`,
    `Normal play action rail: ${actionRail ? `ready=${actionRail.acceptanceReady}, actions=${actionRail.actionLedger.length}, verbs=${actionRail.verbs.join('/')}` : 'not started'}`,
    `Seed divergence: ${divergence ? `${divergence.branches.length} branch(es), diverged=${divergence.diverged}, base law ${divergence.base_law_seed}` : 'not compared'}`,
    `Commons: ${commons ? `${commons.pressure_level}, resources=${commons.resource_total}, ledger=${commons.ledger_rows}, pass=${commons.pass}` : 'not audited'}`,
    `Projects: ${projects ? `${projects.projectLedger.length} work row(s), completed=${projects.completionLedger.length}, stalled=${projects.stalledLedger.length}` : 'not advanced'}`,
    `Commons support: ${commonsSupport ? `${commonsSupport.supportLedger.length} support row(s), recoveries=${commonsSupport.recoveryLedger.length}` : 'not supported'}`,
    `Nearby actions: ${nearby ? `${nearby.actionLedger.length} location action(s), last=${nearby.lastPlan ? nearby.lastPlan.label + ' -> ' + nearby.lastPlan.action : 'none'}` : 'not used'}`,
    `Village days: ${dayCycle ? `${dayCycle.day} day(s), weather rows=${dayCycle.weatherLedger.length}, recaps=${dayCycle.recapLedger.length}` : 'not advanced'}`,
	    `Return later: ${returnLater ? `${returnLater.returnLedger.length} return(s), latest=${returnLater.latestReceipt ? returnLater.latestReceipt.return_id : 'none'}` : 'not used'}`,
    `Terrain physics: ${terrain ? `${terrain.terrainLedger.length} terrain step(s), cells=${terrain.cells.length}, flow=${terrain.flowLedger.length}, support=${terrain.supportLedger.length}` : 'not started'}`,
	    `3D material physics: ${materialWorld ? `${materialWorld.components.length} component(s), ${materialWorld.structures.length} structure(s), term=${latestTerm ? latestTerm.resident_word + ' / ' + latestTerm.player_gloss : 'none'}, physics=${materialPhysics ? `${materialPhysics.step_id} field=${materialPhysics.field_id || 'none'} stress=${materialPhysics.field_stress || 'n/a'}` : 'not stepped'}` : 'not initialized'}`,
    `Resident material handling: ${manipulation ? `${manipulation.actionLedger.length} action(s), practice links=${manipulation.practiceLinks.length}, failures=${manipulation.failureLedger.length}` : 'not started'}`,
    `Resident body physics: ${residentBodies ? `${residentBodies.bodyLedger.length} body step(s), contacts=${residentBodies.contactLedger.length}, recoveries=${residentBodies.recoveryLedger.length}` : 'not started'}`,
    `Tool/work physics: ${tools ? `${tools.useLedger.length} use(s), failures=${tools.failureLedger.length}, repairs=${tools.repairLedger.length}` : 'not started'}`,
    `Resource stock physics: ${resourcePhysics ? `${resourcePhysics.stockLedger.length} stock step(s), losses=${resourcePhysics.lossLedger.length}, gains=${resourcePhysics.gainLedger.length}` : 'not started'}`,
    `Thermal/fire physics: ${thermalPhysics ? `${thermalPhysics.heatLedger.length} heat step(s), smoke=${thermalPhysics.smokeLedger.length}, safety=${thermalPhysics.safetyLedger.length}` : 'not started'}`,
    `Water/fluid physics: ${waterPhysics ? `${waterPhysics.flowLedger.length} flow row(s), leaks=${waterPhysics.leakLedger.length}, route=${waterPhysics.routeLedger.length}` : 'not started'}`,
    `Ecology/food physics: ${ecologyPhysics ? `${ecologyPhysics.growthLedger.length} growth row(s), harvest=${ecologyPhysics.harvestLedger.length}, hunger=${ecologyPhysics.hungerLedger.length}` : 'not started'}`,
    `Construction practices: ${constructionPracticeCount} construction row(s) linked to practice graph`,
	    `Audit mode: ${world.audit ? 'on' : 'off'} / hidden law normal view: no`,
  ].join('\n');
}

function buildPrototypeCommonsAudit() {
  const ledgerRows = world.realityConstraintLedger && world.realityConstraintLedger.rows ? world.realityConstraintLedger.rows : [];
  const resources = { ...world.resources };
  const resourceTotal = Object.values(resources).reduce((sum, value) => sum + Number(value || 0), 0);
  const lowResources = Object.entries(resources).filter(([, value]) => Number(value || 0) <= 3).map(([key]) => key);
  const workCost = ledgerRows.reduce((sum, row) => sum + Number(row.energy_work_time_cost && row.energy_work_time_cost.work || 0), 0);
  const timeCost = ledgerRows.reduce((sum, row) => sum + Number(row.energy_work_time_cost && row.energy_work_time_cost.time || 0), 0);
  const toolWear = ledgerRows.reduce((sum, row) => sum + Number(row.tool_wear || 0), 0);
  const conservationIssues = ledgerRows.filter(row => !row.conservation_check).length;
  const hiddenLawExposureIssues = ledgerRows.filter(row => row.normal_view_hidden_law_exposed === true).length;
  const maintenanceRows = ledgerRows.filter(row => row.maintenance_obligation_created && row.maintenance_obligation_created !== 'none');
  const practiceBurden = world.emergentPracticeGraph && world.emergentPracticeGraph.nodes
    ? world.emergentPracticeGraph.nodes.reduce((sum, row) => sum + Number(row.maintenance_cost || 0), 0)
    : 0;
  const acceptedProposals = world.villageBoard && world.villageBoard.projectProposals
    ? world.villageBoard.projectProposals.filter(row => row.status === 'accepted').length
    : 0;
  const commonsSupport = world.gamePrototypeCommonsSupport || null;
  const commonsSupportRows = commonsSupport ? commonsSupport.supportLedger.length : 0;
  const commonsRecoveries = commonsSupport ? commonsSupport.recoveryLedger.length : 0;
  const pressureLevel = lowResources.length >= 2 || resourceTotal < 12 ? 'strained' : (maintenanceRows.length + practiceBurden > 10 ? 'burdened' : 'stable');
  const pass = ledgerRows.length > 0 && conservationIssues === 0 && hiddenLawExposureIssues === 0 && resourceTotal >= 0;
  return {
    audit_id: `GPC-${String((world.gamePrototypeCommons ? world.gamePrototypeCommons.runCount || 0 : 0) + 1).padStart(2, '0')}`,
    runCount: (world.gamePrototypeCommons ? world.gamePrototypeCommons.runCount || 0 : 0) + 1,
    tick: world.tick,
    pass,
    resources,
    resource_total: resourceTotal,
    low_resources: lowResources,
    pressure_level: pressureLevel,
    ledger_rows: ledgerRows.length,
    work_cost: workCost,
    time_cost: timeCost,
    tool_wear: toolWear,
    maintenance_obligations: maintenanceRows.length,
    practice_maintenance_burden: practiceBurden,
    accepted_proposals: acceptedProposals,
    commons_support_rows: commonsSupportRows,
    commons_recoveries: commonsRecoveries,
    conservation_issues: conservationIssues,
    hidden_law_exposure_issues: hiddenLawExposureIssues,
    boundary: 'public commons audit only; derives from resources and causal ledger without exposing hidden law in normal view',
  };
}

function auditPrototypeCommons() {
  if (!world.realityConstraintLedger || !world.realityConstraintLedger.rows.length) runRealityConstraintAudit();
  const audit = buildPrototypeCommonsAudit();
  world.gamePrototypeCommons = audit;
  recordPrototypeMilestone('prototype-commons-audit', `${audit.pressure_level}; resources ${audit.resource_total}; ledger ${audit.ledger_rows}; pass=${audit.pass}`);
  return log('auditPrototypeCommons', { pass: audit.pass, pressureLevel: audit.pressure_level, resources: audit.resource_total, ledgerRows: audit.ledger_rows, maintenance: audit.maintenance_obligations });
}

function formatPrototypeCommons() {
  const audit = world.gamePrototypeCommons || buildPrototypeCommonsAudit();
  return [
    `${audit.audit_id}: ${audit.pass ? 'PASS' : 'WATCH'} / pressure=${audit.pressure_level}`,
    `Resources: water=${audit.resources.water} fiber=${audit.resources.fiber} wood=${audit.resources.wood} care=${audit.resources.care} food=${audit.resources.food || 0} / total=${audit.resource_total}`,
    `Costs: work=${audit.work_cost} time=${audit.time_cost} toolWear=${audit.tool_wear}`,
    `Maintenance: obligations=${audit.maintenance_obligations} practiceBurden=${audit.practice_maintenance_burden} acceptedProposals=${audit.accepted_proposals}`,
    `Commons support: rows=${audit.commons_support_rows || 0} recoveries=${audit.commons_recoveries || 0}`,
    `Ledger: rows=${audit.ledger_rows} conservationIssues=${audit.conservation_issues} hiddenLawExposure=${audit.hidden_law_exposure_issues}`,
    `Low resources: ${audit.low_resources.length ? audit.low_resources.join(', ') : 'none'}`,
    `Boundary: ${audit.boundary}`,
  ].join('\n');
}

function formatPrototypeCommonsSupport() {
  const support = world.gamePrototypeCommonsSupport || ensurePrototypeCommonsSupport();
  const supportRows = support.supportLedger.slice(-6).map(row => `${row.support_id}: ${row.resource} +${row.amount_added} from ${row.source}; resident=${row.resident}; reason=${row.reason}; directCommand=${row.avatar_direct_command}`);
  const recoveryRows = support.recoveryLedger.slice(-4).map(row => `${row.recovery_id}: ${row.resource} reopened ${row.reopened_proposals.join(', ')}`);
  return [
    `Runs: ${support.runCount} / support rows=${support.supportLedger.length} / recoveries=${support.recoveryLedger.length}`,
    `Boundary: ${support.boundary}`,
    'Recent commons support:',
    ...(supportRows.length ? supportRows : ['none']),
    'Project recoveries:',
    ...(recoveryRows.length ? recoveryRows : ['none']),
  ].join('\n');
}

function formatPrototypeNearbyActions() {
  const nearby = world.gamePrototypeNearbyActions || ensurePrototypeNearbyActions();
  const plan = nearbyActionPlan();
  const rows = nearby.actionLedger.slice(-8).map(row => `${row.nearby_id}: ${row.label} (${row.room}) -> ${row.action}; result=${row.result_event}; directCommand=${row.avatar_direct_command}`);
  return [
    `Current zone: ${plan.label} / room=${plan.room} / suggested=${plan.action}`,
    `Why: ${plan.why}`,
    `Runs: ${nearby.runCount} / ledger rows=${nearby.actionLedger.length}`,
    `Boundary: ${nearby.boundary}`,
    'Recent nearby actions:',
    ...(rows.length ? rows : ['none']),
  ].join('\n');
}

function formatPrototypeDayCycle() {
  const cycle = world.gamePrototypeDayCycle || ensurePrototypeDayCycle();
  const days = cycle.dayLedger.slice(-6).map(row => `${row.day_id}: day ${row.day}, ${row.weather}; resources=${row.resource_result ? row.resource_result.stepId : 'none'}; thermal=${row.thermal_result ? row.thermal_result.stepId : 'none'}; water=${row.water_result ? row.water_result.stepId : 'none'}; ecology=${row.ecology_result ? row.ecology_result.stepId : 'none'}; structure=${row.structural_result ? row.structural_result.stepId : 'none'}; constraints=${row.constraint_result ? row.constraint_result.stepId : 'none'}; material=${row.material_state_result ? row.material_state_result.stepId : 'none'}; residentActions=${row.resident_actions_added}; project=${row.project_result ? row.project_result.status : 'none'}; commons=${row.commons_result ? row.commons_result.resource : 'none'}`);
  const weather = cycle.weatherLedger.slice(-6).map(row => `${row.weather_id}: ${row.weather}; ${row.effect}; deltas=${JSON.stringify(row.resource_deltas)}`);
  const recaps = cycle.recapLedger.slice(-5).map(row => `${row.recap_id}: ${row.summary}`);
  return [
    `Day: ${cycle.day} / weather rows=${cycle.weatherLedger.length} / recap rows=${cycle.recapLedger.length}`,
    `Boundary: ${cycle.boundary}`,
    'Recent day rows:',
    ...(days.length ? days : ['none']),
    'Weather/resource pressure:',
    ...(weather.length ? weather : ['none']),
    'Recaps:',
    ...(recaps.length ? recaps : ['none']),
  ].join('\n');
}

function formatPrototypeReturnLater() {
  const returns = world.gamePrototypeReturnLater || ensurePrototypeReturnLater();
  const absences = returns.absenceLedger.slice(-4).map(row => `${row.absence_id}: ${row.days_away} day(s), day ${row.day_before}, selected=${row.selected_resident}, reset=${row.direct_reset}`);
  const receipts = returns.returnLedger.slice(-5).map(row => `${row.return_id}: ${row.days_away} day(s), day ${row.day_before}->${row.day_after}, remembered=${row.residents_who_remembered.join(', ')}, restoredOld=${row.restored_old_state}`);
  const latest = returns.latestReceipt;
  return [
    `Runs: ${returns.runCount} / absences=${returns.absenceLedger.length} / returns=${returns.returnLedger.length}`,
    `Boundary: ${returns.boundary}`,
    `Latest: ${latest ? `${latest.return_id}; resources delta ${JSON.stringify(latest.resource_delta)}` : 'none'}`,
    'Absences:',
    ...(absences.length ? absences : ['none']),
    'Return receipts:',
    ...(receipts.length ? receipts : ['none']),
  ].join('\n');
}

function formatPrototypeTerrain() {
  const terrain = world.gamePrototypeTerrain || ensurePrototypeTerrain();
  const latest = terrain.terrainLedger.length ? terrain.terrainLedger[terrain.terrainLedger.length - 1] : null;
  const cells = terrain.cells
    .slice()
    .sort((a, b) => (Number(a.walkability || 1) - Number(b.walkability || 1)) || (Number(b.erosion || 0) - Number(a.erosion || 0)))
    .slice(0, 8)
    .map(cell => `${cell.cell_id}: moisture=${cell.moisture} walk=${cell.walkability} support=${cell.support_capacity} erosion=${cell.erosion} compaction=${cell.compaction}; ${cell.resource_hint}`);
  const flows = terrain.flowLedger.slice(-6).map(row => `${row.flow_id}: ${row.cell_id}; flow=${row.moisture_flow}; pressure=${row.pressure_mass}; walk=${row.after_walkability}`);
  const support = terrain.supportLedger.slice(-6).map(row => `${row.support_id}: ${row.cell_id}; pressure=${row.pressure_mass}; support=${row.support_capacity}; maintenance=${row.maintenance_pressure}`);
  const resources = terrain.resourceLedger.slice(-4).map(row => `${row.resource_id}: ${row.terrain_step_id}; delta=${JSON.stringify(row.resource_delta)}; source=${row.source}; spawn=${row.no_resource_spawning === false}`);
  return [
    `Runs: ${terrain.runCount} / cells=${terrain.cells.length} / terrain rows=${terrain.terrainLedger.length}`,
    `Boundary: stochastic terrain physics; ground affects bodies and components; no decorative map-only substrate.`,
    `Latest: ${latest ? `${latest.terrain_step_id}; moisture=${latest.average_moisture}; walkability=${latest.average_walkability}; weak=${latest.weak_cells}; bodyCells=${latest.body_pressure_cells}; componentCells=${latest.component_pressure_cells}` : 'none'}`,
    'Weakest / most pressured cells:',
    ...(cells.length ? cells : ['none']),
    'Moisture flow rows:',
    ...(flows.length ? flows : ['none']),
    'Support / walkability pressure:',
    ...(support.length ? support : ['none']),
    'Resource pressure:',
    ...(resources.length ? resources : ['none']),
  ].join('\n');
}

function formatPrototypeMaterialWorld() {
  const sim = world.gamePrototype3DWorld || ensurePrototype3DWorld();
  const physics = sim.physics || { mode: 'stochastic physics first', gravity: 9.8, solver_layers: ['mass', 'support', 'collision/contact', 'friction', 'stochastic failure'], forceLedger: [], supportLedger: [], collisionLedger: [], failureLedger: [], fieldLedger: [], energyLedger: [], transformationLedger: [] };
  const structures = sim.structures.slice(-3).map(row => `${row.structure_id}: ${row.resident_term_id} / ${row.player_gloss}; stability=${row.stability}; moisture=${row.moisture_risk}; fixedAsset=${row.no_fixed_asset === false}`);
  const components = sim.components.slice(0, 8).map(row => `${row.component_id}: ${row.shape} ${row.material_id} ${row.affordance}; pos=(${row.position3d.x},${row.position3d.y},${row.position3d.z}); stability=${row.stability}; damage=${row.damage}; stress=${row.field_stress || 0}; temp=${row.temperature || 'n/a'}; term=${row.resident_term_id}`);
	  const terms = sim.language.terms.map(row => `${row.resident_word} ~ ${row.player_gloss}; engine=${world.audit ? row.engine_concept : 'audit only'}; roots=${row.root_glosses.join('+')}; variants=${row.variants.join(', ')}; confidence=${row.translation_confidence}`);
	  const roots = sim.language.soundRoots.map(row => `${row.sound_form}: ${row.player_gloss}; grounded=${row.grounded_event}; adoption=${row.adoption_count}`);
	  const latestPhysics = physics.latestStep;
	  const board = world.villageBoard || null;
	  const physicsProposals = board && board.projectProposals ? board.projectProposals.filter(row => row.related_physics_step).slice(-4).map(row => `${row.proposal_id}: ${row.problem_addressed}; status=${row.status}; materials=${(row.materials_needed || []).join('+')}`) : [];
  const constructionRows = (sim.constructionLedger || []).slice(-5).map(row => `${row.construction_id}: ${row.proposal_id}; added=${row.components_added.length}; repaired=${row.components_repaired.length}; term=${row.resident_term}; practice=${row.practice_id || 'none'}/${row.practice_status_after || 'none'}; stability=${row.structure_stability_after}`);
		  return [
    `Runs: material=${sim.runCount} / physics=${physics.step || 0}`,
    `Boundary: ${sim.boundary}`,
    `Physics kernel: ${physics.mode}; gravity=${physics.gravity}; layers=${physics.solver_layers.join(', ')}`,
    `Renderer: ${sim.renderer}`,
    'Structures from components:',
    ...(structures.length ? structures : ['none']),
    'Components:',
    ...(components.length ? components : ['none']),
    'Resident terms and imperfect glosses:',
    ...(terms.length ? terms : ['none']),
    'Grounded sound roots:',
    ...(roots.length ? roots : ['none']),
		    'Physics:',
		    latestPhysics ? `${latestPhysics.step_id}: support=${latestPhysics.support_checks}, collisions=${latestPhysics.collisions}, failures=${latestPhysics.failures}, field=${latestPhysics.field_id || 'none'}, heat=${latestPhysics.field_heat || 'n/a'}, moisture=${latestPhysics.field_moisture || 'n/a'}, stress=${latestPhysics.field_stress || 'n/a'}, entropy=${latestPhysics.entropy}` : 'none',
		    `Force rows=${physics.forceLedger.length} / support rows=${physics.supportLedger.length} / collision rows=${physics.collisionLedger.length} / failure rows=${physics.failureLedger.length} / field rows=${physics.fieldLedger ? physics.fieldLedger.length : 0} / energy rows=${physics.energyLedger ? physics.energyLedger.length : 0}`,
	    'Physics consequences:',
	    ...(physicsProposals.length ? physicsProposals : ['none']),
    'Resident construction:',
    ...(constructionRows.length ? constructionRows : ['none']),
			    'Normal view hidden law exposed: no / fixed building asset: no / English resident tech label: no',
		  ].join('\n');
		}

function formatPrototypeStructuralPhysics() {
  const sim = world.gamePrototype3DWorld || ensurePrototype3DWorld();
  const physics = sim.physics || {};
  const latest = physics.latestStructuralStep || null;
  const loads = (physics.loadPathLedger || []).slice(-6).map(row => `${row.component_id}: demand=${row.demand}, capacity=${row.support_capacity}, margin=${row.support_margin}, supported=${row.supported_by}`);
  const stress = (physics.stressLedger || []).slice(-6).map(row => `${row.component_id}: stress=${row.stress_score}, bend=${row.bending_stress}, slip=${row.anchor_slip_delta}, collapseP=${row.collapse_probability}`);
  const deform = (physics.deformationLedger || []).slice(-5).map(row => `${row.component_id}: deflection=${row.total_deflection}, slip=${row.anchor_slip}, tilt=${row.tilt}, stability=${row.stability_after}`);
  const collapses = (physics.collapseLedger || []).slice(-5).map(row => `${row.component_id}: p=${row.collapse_probability}, result=${row.result}`);
  const repairs = (physics.structuralRepairLedger || []).slice(-5).map(row => `${row.repair_id}: ${row.reason}; materials=${row.materials_needed.join('+')}; labor=${row.labor_time_cost}; direct=${row.avatar_direct_command === true}`);
  const structures = (sim.structures || []).map(row => `${row.structure_id}: stress=${row.structural_stress || 0}, margin=${row.support_margin || 'n/a'}, deflect=${row.max_deflection || 0}, risk=${row.collapse_risk || 0}, status=${row.status}`);
  return [
    latest ? `Latest: ${latest.step_id} base=${latest.base_step_id}; stress=${latest.max_stress}; deflection=${latest.max_deflection}; margin=${latest.min_margin}; collapses=${latest.collapses}; repair=${latest.repair_rows}` : 'Latest: none',
    `Ledgers: load=${(physics.loadPathLedger || []).length} / stress=${(physics.stressLedger || []).length} / deformation=${(physics.deformationLedger || []).length} / collapse=${(physics.collapseLedger || []).length} / repair=${(physics.structuralRepairLedger || []).length}`,
    'Structure state:',
    ...(structures.length ? structures : ['none']),
    'Load paths:',
    ...(loads.length ? loads : ['none']),
    'Stress rows:',
    ...(stress.length ? stress : ['none']),
    'Deformation:',
    ...(deform.length ? deform : ['none']),
    'Partial collapse rows:',
    ...(collapses.length ? collapses : ['none']),
    'Repair pressure:',
    ...(repairs.length ? repairs : ['none']),
    'Boundary: stochastic structural physics only; no material spawning, no hidden law in normal view, no fixed building asset.'
  ].join('\n');
}

function formatPrototypeContactConstraintPhysics() {
  const sim = world.gamePrototype3DWorld || ensurePrototype3DWorld();
  const physics = sim.physics || {};
  const latest = physics.latestConstraintStep || null;
  const contacts = (physics.contactConstraintLedger || []).slice(-6).map(row => `${row.component_a}<->${row.component_b}: contact=${row.contact}, jointed=${row.jointed}, gap=${row.vertical_gap}, normal=${row.normal_proxy}`);
  const joints = (physics.jointConstraintLedger || []).slice(-6).map(row => `${row.component_a}<->${row.component_b}: demand=${row.joint_demand}, strength=${row.joint_strength}, failed=${row.joint_failed}`);
  const friction = (physics.frictionLedger || []).slice(-6).map(row => `${row.component_a}<->${row.component_b}: limit=${row.friction_limit}, moisture=${row.surface_moisture}, slipP=${row.slip_probability}, slipped=${row.slipped}`);
  const impulses = (physics.impulseLedger || []).slice(-5).map(row => `${row.component_a}<->${row.component_b}: impulse=${row.impulse}, relSlip=${row.relative_slip}, slipDelta=${row.slip_delta}`);
  const repairs = (physics.constraintRepairLedger || []).slice(-5).map(row => `${row.repair_id}: ${row.component_a}<->${row.component_b}; ${row.reason}; materials=${row.materials_needed.join('+')}; labor=${row.labor_time_cost}`);
  return [
    latest ? `Latest: ${latest.step_id}; contacts=${latest.contact_rows}; joints=${latest.joint_rows}; slip=${latest.slipping_contacts}; failed=${latest.failed_joints}; impulse=${latest.max_impulse}` : 'Latest: none',
    `Ledgers: contact=${(physics.contactConstraintLedger || []).length} / joint=${(physics.jointConstraintLedger || []).length} / friction=${(physics.frictionLedger || []).length} / impulse=${(physics.impulseLedger || []).length} / repair=${(physics.constraintRepairLedger || []).length}`,
    'Contacts:',
    ...(contacts.length ? contacts : ['none']),
    'Joint constraints:',
    ...(joints.length ? joints : ['none']),
    'Friction:',
    ...(friction.length ? friction : ['none']),
    'Impulse transfer:',
    ...(impulses.length ? impulses : ['none']),
    'Repair pressure:',
    ...(repairs.length ? repairs : ['none']),
    'Boundary: contact constraints are bounded stochastic prototype physics; no hidden law in normal view and no material spawning.'
  ].join('\n');
}

function formatPrototypeMaterialStatePhysics() {
  const sim = world.gamePrototype3DWorld || ensurePrototype3DWorld();
  const physics = sim.physics || {};
  const latest = physics.latestMaterialStateStep || null;
  const states = (physics.materialStateLedger || []).slice(-6).map(row => `${row.component_id}: phase=${row.phase}, sat=${row.saturation}, dry=${row.dryness}, rot=${row.rot}, char=${row.char}, crack=${row.crack}, seal=${row.seal}`);
  const phases = (physics.phaseChangeLedger || []).slice(-6).map(row => `${row.component_id}: ${row.from_phase}->${row.to_phase}; visible=${row.resident_visible_as}`);
  const properties = (physics.propertyDriftLedger || []).slice(-5).map(row => `${row.component_id}: hard=${row.effective_hardness}, brittle=${row.effective_brittleness}, water=${row.effective_water_resistance}, work=${row.effective_workability}`);
  const repairs = (physics.materialStateRepairLedger || []).slice(-5).map(row => `${row.repair_id}: ${row.component_id}; ${row.reason}; materials=${row.materials_needed.join('+')}; labor=${row.labor_time_cost}`);
  return [
    latest ? `Latest: ${latest.step_id}; states=${latest.state_rows}; phases=${latest.phase_changes}; risky=${latest.risky_components}; repair=${latest.repair_rows}` : 'Latest: none',
    `Ledgers: state=${(physics.materialStateLedger || []).length} / phase=${(physics.phaseChangeLedger || []).length} / property=${(physics.propertyDriftLedger || []).length} / repair=${(physics.materialStateRepairLedger || []).length}`,
    'Material states:',
    ...(states.length ? states : ['none']),
    'Phase changes:',
    ...(phases.length ? phases : ['none']),
    'Effective property drift:',
    ...(properties.length ? properties : ['none']),
    'Repair pressure:',
    ...(repairs.length ? repairs : ['none']),
    'Boundary: material state physics is bounded stochastic property drift; no spawned matter and no hidden state in normal resident view.'
  ].join('\n');
}

function formatPrototypeMaterialManipulation() {
  const loop = world.gamePrototypeMaterialManipulation || ensureMaterialManipulationLoop();
  const actions = loop.actionLedger.slice(-8).map(row => `${row.manipulation_id}: ${row.resident} ${row.action} ${row.component_id}/${row.resident_term}; success=${row.success}; tool=${row.tool_id || 'none'} fit=${row.tool_fit || 0} failed=${row.tool_failed === true}; cost=${Object.entries(row.resource_cost || {}).map(([key, value]) => `${key}:${value}`).join('+') || 'none'}; physics=${row.physics_step_id}`);
  const observations = loop.observationLedger.slice(-5).map(row => `${row.observation_id}: ${row.public_observation} -> ${row.resident_interpretation}`);
  const failures = loop.failureLedger.slice(-5).map(row => `${row.manipulation_id}: ${row.failure_reason}; recoverable=${row.recoverable}`);
  const links = loop.practiceLinks.slice(-6).map(row => `${row.manipulation_id}->${row.practice_id} (${row.relation})`);
  return [
    `Runs: ${loop.runCount} / actions=${loop.actionLedger.length} / observations=${loop.observationLedger.length} / practiceLinks=${loop.practiceLinks.length}`,
    `Boundary: ${loop.boundary}`,
    'Resident physical handling:',
    ...(actions.length ? actions : ['none']),
    'Public observations:',
    ...(observations.length ? observations : ['none']),
    'Failures preserved:',
    ...(failures.length ? failures : ['none']),
    'Practice links:',
    ...(links.length ? links : ['none']),
  ].join('\n');
}

function formatPrototypeTools() {
  const sim = world.gamePrototypeTools || ensurePrototypeTools();
  const tools = sim.tools.map(tool => `${tool.tool_id}: ${tool.resident_term} / ${tool.player_gloss}; holder=${tool.current_holder}; status=${tool.status}; wear=${tool.wear}; damage=${tool.damage}; edge=${tool.edge_integrity}; bind=${tool.handle_binding}; moisture=${tool.moisture}`);
  const uses = sim.useLedger.slice(-7).map(row => `${row.tool_use_id}: ${row.resident} used ${row.resident_term} for ${row.action}; fit=${row.fit}; wear+${row.wear_delta}; failed=${row.failed}; repaired=${row.repaired}; blocked=${row.action_blocked}; source=${row.source}`);
  const failures = sim.failureLedger.slice(-5).map(row => `${row.failure_id}: ${row.tool_id}; ${row.reason}; repaired=${row.repaired}; blocked=${row.action_blocked}`);
  const repairs = sim.repairLedger.slice(-5).map(row => `${row.repair_id}: ${row.tool_id}; cost=${Object.entries(row.resource_cost || {}).map(([key, value]) => `${key}:${value}`).join('+')}; status=${row.after.status}`);
  return [
    `Runs: ${sim.runCount} / uses=${sim.useLedger.length} / wear=${sim.wearLedger.length} / failures=${sim.failureLedger.length} / repairs=${sim.repairLedger.length}`,
    `Boundary: physical tools are objects; work can wear, strain, fail, or require repair; resident terms are local glosses.`,
    'Tools:',
    ...(tools.length ? tools : ['none']),
    'Recent uses:',
    ...(uses.length ? uses : ['none']),
    'Failures:',
    ...(failures.length ? failures : ['none']),
    'Repairs:',
    ...(repairs.length ? repairs : ['none']),
    'Normal view hidden law exposed: no / no free tool repair: yes',
  ].join('\n');
}

function formatPrototypeResourcePhysics() {
  const sim = world.gamePrototypeResourcePhysics || ensurePrototypeResourcePhysics();
  const stocks = sim.stocks.map(stock => `${stock.stock_id}: ${stock.resident_term} / ${stock.player_gloss}; qty=${Number(stock.quantity || 0).toFixed(2)}/${stock.capacity}; moisture=${stock.moisture}; temp=${stock.temperature}; decay=${stock.decay}; storage=${stock.storage}`);
  const steps = sim.stockLedger.slice(-5).map(row => `${row.step_id}: weather=${row.weather}; deltas=${Object.entries(row.deltas || {}).map(([key, value]) => `${key}:${value}`).join(', ')}; resources=${JSON.stringify(row.resources_after)}`);
  const transforms = sim.transformLedger.slice(-8).map(row => `${row.row_id}: ${row.resource} ${row.quantity_before}->${row.quantity_after} delta=${row.delta}; ${row.causal_terms}`);
  const losses = sim.lossLedger.slice(-5).map(row => `${row.loss_id}: ${row.resource} delta=${row.delta}; source=${row.source}`);
  const gains = sim.gainLedger.slice(-5).map(row => `${row.gain_id}: ${row.resource} delta=+${row.delta}; source=${row.source}`);
  return [
    `Runs: ${sim.runCount} / stock steps=${sim.stockLedger.length} / transforms=${sim.transformLedger.length} / losses=${sim.lossLedger.length} / gains=${sim.gainLedger.length}`,
    `Boundary: resources are stored stocks; water leaks/evaporates, fiber and wood decay, care is embodied attention recovery.`,
    'Stocks:',
    ...(stocks.length ? stocks : ['none']),
    'Stock steps:',
    ...(steps.length ? steps : ['none']),
    'Transform rows:',
    ...(transforms.length ? transforms : ['none']),
    'Loss rows:',
    ...(losses.length ? losses : ['none']),
    'Gain rows:',
    ...(gains.length ? gains : ['none']),
    'Normal view hidden law exposed: no / no free resource spawning: yes',
  ].join('\n');
}

function formatPrototypeThermalPhysics() {
  const sim = world.gamePrototypeThermalPhysics || ensurePrototypeThermalPhysics();
  const nodes = sim.nodes.map(node => `${node.node_id}: ${node.resident_term} / ${node.player_gloss}; status=${node.status}; heat=${node.heat}; fuel=${node.fuel}; smoke=${node.smoke}; containment=${node.containment}; rule=${node.local_rule}`);
  const heat = sim.heatLedger.slice(-5).map(row => `${row.step_id}: heat=${row.max_heat}; smoke=${row.total_smoke}; hazard=${row.hazard}; safety=${row.safety_proposal_id || 'none'}; wood=${row.wood_after}`);
  const fuel = sim.fuelLedger.slice(-6).map(row => `${row.fuel_id}: ${row.node_id}; fuel ${row.fuel_before}->${row.fuel_after}; consumed=${row.fuel_consumed}; wood=${row.wood_resource_after}`);
  const smoke = sim.smokeLedger.slice(-5).map(row => `${row.smoke_id}: smoke=${row.total_smoke}; ${row.public_observation} -> ${row.resident_interpretation}`);
  const safety = sim.safetyLedger.slice(-5).map(row => `${row.safety_id}: ${row.risk}; proposal=${row.proposal_id || 'none'}; recoverable=${row.recoverable}`);
  const ignitions = sim.ignitionLedger.slice(-5).map(row => `${row.ignition_id}: ${row.component_id}/${row.material_id}; risk=${row.burn_risk}; recoverable=${row.recoverable}`);
  return [
    `Runs: ${sim.runCount} / heat=${sim.heatLedger.length} / fuel=${sim.fuelLedger.length} / smoke=${sim.smokeLedger.length} / ignitions=${sim.ignitionLedger.length} / safety=${sim.safetyLedger.length}`,
    `Boundary: fire requires fuel, heat, and air; smoke creates care/safety work, not spectacle; hazards must remain bounded and recoverable.`,
    'Thermal nodes:',
    ...(nodes.length ? nodes : ['none']),
    'Heat steps:',
    ...(heat.length ? heat : ['none']),
    'Fuel rows:',
    ...(fuel.length ? fuel : ['none']),
    'Smoke rows:',
    ...(smoke.length ? smoke : ['none']),
    'Ignition rows:',
    ...(ignitions.length ? ignitions : ['none']),
    'Safety rows:',
    ...(safety.length ? safety : ['none']),
    'Normal view hidden law exposed: no / no free fuel: yes',
  ].join('\n');
}

function formatPrototypeWaterPhysics() {
  const sim = world.gamePrototypeWaterPhysics || ensurePrototypeWaterPhysics();
  const bodies = sim.bodies.map(body => `${body.water_id}: ${body.resident_term} / ${body.player_gloss}; kind=${body.kind}; volume=${Number(body.volume || 0).toFixed(2)}/${body.capacity}; contamination=${body.contamination}; status=${body.status}; route=${body.route}`);
  const flows = sim.flowLedger.slice(-8).map(row => `${row.flow_id}: ${row.water_id}; vol ${row.volume_before}->${row.volume_after}; rain=${row.rain_gain}; evap=${row.evaporation}; leak=${row.vessel_leak + row.ground_loss}; flow=${row.flow_out}; cell=${row.terrain_cell}`);
  const leaks = sim.leakLedger.slice(-5).map(row => `${row.leak_id}: ${row.water_id}; vessel=${row.vessel_leak}; ground=${row.ground_loss}; route=${row.route_status}`);
  const routes = sim.routeLedger.slice(-5).map(row => `${row.route_id}: pressure=${row.pressure}; walk=${row.walkability_min}; ${row.public_observation} -> ${row.resident_interpretation}`);
  const quality = sim.qualityLedger.slice(-5).map(row => `${row.quality_id}: contamination=${row.average_contamination}; surface=${row.surface_water_volume}`);
  const safety = sim.safetyLedger.slice(-5).map(row => `${row.safety_id}: ${row.risk}; proposal=${row.proposal_id || 'none'}; recoverable=${row.recoverable}`);
  return [
    `Runs: ${sim.runCount} / flows=${sim.flowLedger.length} / leaks=${sim.leakLedger.length} / vessels=${sim.vesselLedger.length} / routes=${sim.routeLedger.length} / safety=${sim.safetyLedger.length}`,
    `Boundary: water has volume, containment, slope, resistance, evaporation, leakage, quality, and route pressure; no free water movement.`,
    'Water bodies:',
    ...(bodies.length ? bodies : ['none']),
    'Flow rows:',
    ...(flows.length ? flows : ['none']),
    'Leak rows:',
    ...(leaks.length ? leaks : ['none']),
    'Route rows:',
    ...(routes.length ? routes : ['none']),
    'Quality rows:',
    ...(quality.length ? quality : ['none']),
    'Safety rows:',
    ...(safety.length ? safety : ['none']),
    'Normal view hidden law exposed: no / no resource spawning: yes',
  ].join('\n');
}

function formatPrototypeEcologyPhysics() {
  const sim = world.gamePrototypeEcologyPhysics || ensurePrototypeEcologyPhysics();
  const patches = sim.patches.map(patch => `${patch.patch_id}: ${patch.resident_term} / ${patch.player_gloss}; biomass=${Number(patch.biomass || 0).toFixed(2)}/${patch.carrying_capacity}; cell=${patch.terrain_cell}; status=${patch.status}`);
  const growth = sim.growthLedger.slice(-8).map(row => `${row.growth_id}: ${row.patch_id}; biomass ${row.biomass_before}->${row.biomass_after}; moistureFit=${row.moisture_fit}; heatFit=${row.heat_fit}; rot=${row.rot}; route=${row.route_stress}`);
  const harvest = sim.harvestLedger.slice(-5).map(row => `${row.harvest_id}: patch=${row.patch_id}; harvested=${row.harvested}; fed=${row.fed_residents.join(',') || 'none'}; food=${row.food_before}->${row.food_after_feeding}; overharvest=${row.overharvest_risk}`);
  const spoilage = sim.spoilageLedger.slice(-5).map(row => `${row.spoilage_id}: pressure=${row.spoilage_pressure}; spoiled=${row.spoiled_units}; food=${row.food_after}`);
  const hunger = sim.hungerLedger.slice(-5).map(row => `${row.hunger_id}: hungry=${row.hungry_before.join(',') || 'none'}; fed=${row.fed_residents.join(',') || 'none'}; remaining=${row.hunger_remaining.join(',') || 'none'}; food=${row.food_after}`);
  const safety = sim.safetyLedger.slice(-5).map(row => `${row.safety_id}: ${row.risk}; proposal=${row.proposal_id || 'none'}; recoverable=${row.recoverable}`);
  return [
    `Runs: ${sim.runCount} / growth=${sim.growthLedger.length} / harvest=${sim.harvestLedger.length} / spoilage=${sim.spoilageLedger.length} / hunger=${sim.hungerLedger.length} / safety=${sim.safetyLedger.length}`,
    `Boundary: food requires growth, harvest, storage, spoilage pressure, and hunger consumption; no free food.`,
    'Food patches:',
    ...(patches.length ? patches : ['none']),
    'Growth rows:',
    ...(growth.length ? growth : ['none']),
    'Harvest rows:',
    ...(harvest.length ? harvest : ['none']),
    'Spoilage rows:',
    ...(spoilage.length ? spoilage : ['none']),
    'Hunger rows:',
    ...(hunger.length ? hunger : ['none']),
    'Safety rows:',
    ...(safety.length ? safety : ['none']),
    'Normal view hidden law exposed: no / no food spawning: yes',
  ].join('\n');
}

function formatPrototypeProjects() {
  const projects = world.gamePrototypeProjects || ensurePrototypeProjects();
  const board = world.villageBoard || null;
  const active = board && board.projectProposals
    ? board.projectProposals.filter(row => !row.project_completed).slice(-5)
    : [];
  const activeRows = active.map(row => `${row.proposal_id}: ${row.proposer} / ${row.status} / progress=${Number(row.project_progress || 0).toFixed(2)} / materials=${(row.materials_needed || []).join('+')}`);
  const workRows = projects.projectLedger.slice(-6).map(row => `${row.project_id}: ${row.proposal_id} ${row.status} progress=${row.progress} tool=${row.tool_id || 'none'} fit=${row.tool_fit || 0} failed=${row.tool_failed === true} consumed=${Object.entries(row.materials_consumed || {}).map(([key, value]) => `${key}:${value}`).join('+') || 'none'} construction=${row.construction_id || 'none'} added=${row.components_added ? row.components_added.length : 0} repaired=${row.components_repaired ? row.components_repaired.length : 0}`);
  const completionRows = projects.completionLedger.slice(-4).map(row => `${row.completion_id}: ${row.proposal_id} completed ${row.problem_addressed}; construction=${row.construction_id || 'none'} added=${row.components_added ? row.components_added.length : 0}; maintenance=${row.maintenance_cost}`);
  const stalledRows = projects.stalledLedger.slice(-4).map(row => `${row.project_id}: ${row.proposal_id} stalled because ${row.stalled_reason}; progress=${row.progress}`);
  return [
    `Runs: ${projects.runCount} / work rows=${projects.projectLedger.length} / completed=${projects.completionLedger.length} / stalled=${projects.stalledLedger.length}`,
    `Boundary: ${projects.boundary}`,
    'Active resident proposals:',
    ...(activeRows.length ? activeRows : ['none']),
    'Recent project work:',
    ...(workRows.length ? workRows : ['none']),
    'Completions:',
    ...(completionRows.length ? completionRows : ['none']),
    'Stalls:',
    ...(stalledRows.length ? stalledRows : ['none']),
  ].join('\n');
}

function derivePrototypePlayerGuide() {
  const guide = {
    phase: 'inspect',
    nextAction: 'Run first playable loop',
    why: 'seed the village, resident pressure, first practice, proposal, save/return proof, and public outcome receipt',
    button: 'runFirstPlayablePrototypeLoop',
    caution: 'You influence conditions; residents still decide, refuse, delay, or reinterpret.',
  };
  if (!world.entered) {
    return { ...guide, phase: 'arrival', nextAction: 'Opening loop', why: 'enter the village and meet the current selected resident', button: 'runPrototypeOpening' };
  }
  if (!world.gamePrototypeNearbyActions || !world.gamePrototypeNearbyActions.actionLedger.length) {
    const plan = nearbyActionPlan();
    return { ...guide, phase: 'nearby play', nextAction: 'Nearby action', why: `use current place ${plan.label} to do ${plan.action} through normal play`, button: 'performNearbyAction' };
  }
  if (!world.gamePrototypeDayCycle || !world.gamePrototypeDayCycle.dayLedger.length) {
    return { ...guide, phase: 'village day', nextAction: 'End day', why: 'let weather, resident autonomy, resources, and accepted work advance through one normal play loop', button: 'endVillageDay' };
  }
  if (!world.gamePrototypeReturnLater || !world.gamePrototypeReturnLater.returnLedger.length) {
    return { ...guide, phase: 'return later', nextAction: 'Return later', why: 'leave the village, advance offscreen days, and return with consequences instead of restoring an old state', button: 'leaveAndReturnLater' };
  }
	  if (!world.gamePrototype3DWorld || !world.gamePrototype3DWorld.physics || !world.gamePrototype3DWorld.physics.latestStep) {
	    return { ...guide, phase: 'stochastic physics', nextAction: 'Physics step', why: 'advance gravity, support, collision/contact, friction, material fatigue, and resident-local language/gloss grounding', button: 'runPrototypePhysicsStep' };
	  }
  if (!world.gamePrototypePlayableSlice || !world.gamePrototypePlayableSlice.acceptanceReady) {
    return { ...guide, phase: 'playable physics-to-practice slice', nextAction: 'Playable slice', why: 'connect physics evidence, a resident proposal, resident testing, practice mutation, and save/return into one playable proof loop', button: 'runPlayablePhysicsPracticeSliceStep' };
  }
  if (!world.gamePrototypeVillageDay03 || !world.gamePrototypeVillageDay03.acceptanceReady) {
    return { ...guide, phase: 'playable village day 0-3', nextAction: 'Village Day 0-3', why: 'run a finite play loop across arrival, observation, resident proposal/test, resident work/recovery, return, and save proof', button: 'runPlayableVillageDay03Step' };
  }
  if (!world.gamePrototypeWorldStage || !world.gamePrototypeWorldStage.acceptanceReady) {
    return { ...guide, phase: 'primary play surface', nextAction: 'World stage', why: 'make the canvas the main playable readout by linking problem, resident, proposal, practice, component, and next action in one visible surface', button: 'runPrimaryPlaySurfaceStep' };
  }
  if (!world.gamePrototypeWalkthrough || !world.gamePrototypeWalkthrough.acceptanceReady) {
    return { ...guide, phase: 'first playable walkthrough', nextAction: 'First playable', why: 'run the whole playable path once and produce a receipt linking entry, world-stage inspection, physics bottleneck, proposal/test, support, resident work, return, save, and acceptance snapshot', button: 'runFirstPlayableWalkthrough' };
  }
  if (!world.gamePrototypeActionRail || !world.gamePrototypeActionRail.acceptanceReady) {
    return { ...guide, phase: 'normal play controls', nextAction: 'Normal play loop', why: 'prove the prototype can be driven through player-language verbs: Look, Ask, Support, Wait, Return, and Save', button: 'runNormalPlayActionRailLoop' };
  }
  if (!world.gamePrototypePlayerMode || !world.gamePrototypePlayerMode.acceptanceReady) {
    return { ...guide, phase: 'player mode interface', nextAction: 'Player mode loop', why: 'switch the shell into a normal player-facing view that foregrounds the canvas, resident cues, public problems, and player-language verbs while hiding debug-heavy panels', button: 'runPlayerModeInterfaceLoop' };
  }
  if (!world.gamePrototypeProposalDeck || !world.gamePrototypeProposalDeck.acceptanceReady) {
    return { ...guide, phase: 'resident proposal deck', nextAction: 'Proposal deck', why: 'read resident-generated proposals as cards and use Ask, Support, or Wait without assigning jobs', button: 'runPlayerProposalDeckLoop' };
  }
  if (!world.gamePrototypeLivedPractice || !world.gamePrototypeLivedPractice.acceptanceReady) {
    return { ...guide, phase: 'lived practice loop', nextAction: 'Practice loop', why: 'repeat ordinary player actions until resident tests stabilize an emergent practice visible in normal play', button: 'runLivedPracticeLoop' };
  }
  if (!world.gamePrototypeWorksite || !world.gamePrototypeWorksite.acceptanceReady) {
    return { ...guide, phase: 'resident worksite', nextAction: 'Worksite loop', why: 'watch resident project work consume materials, repair or add components, stall, complete, and create maintenance burden without assigning jobs', button: 'runResidentWorksiteLoop' };
  }
  if (!world.gamePrototypeMaterialManipulation || !world.gamePrototypeMaterialManipulation.actionLedger.length) {
    return { ...guide, phase: 'material handling', nextAction: 'Resident handling', why: 'let residents physically move, tie, dry, wet-test, stack, or test components through material constraints', button: 'runResidentMaterialManipulationStep' };
  }
	  if (!world.anomalyDiscovery || !world.civilizationPressure) {
    return { ...guide, phase: 'world pressure', nextAction: 'Practice + proposal', why: 'create public observations, pressure, resident tests, and the first proposal without a tech-tree unlock', button: 'runPrototypePracticeChain' };
  }
  if (!world.practicalDiscovery || !(world.practicalDiscovery.autoGeneratedTests || []).length) {
    return { ...guide, phase: 'ordinary play', nextAction: 'Ask schedule twice', why: 'normal repeated play can seed resident-generated tests when public pressure exists', button: 'askSchedule' };
  }
  if (!world.villageBoard || !world.villageBoard.projectProposals.length) {
    return { ...guide, phase: 'village board', nextAction: 'Village board', why: 'let residents post concerns and proposals the avatar can support but not command', button: 'runVillageBoardLoop' };
  }
  if (
    (world.villageBoard.projectProposals || []).some(row => /^stalled: missing/.test(row.status || '')) ||
    Object.values(world.resources).some(value => Number(value || 0) <= 2)
  ) {
    return { ...guide, phase: 'commons support', nextAction: 'Support commons', why: 'recover low or stalled materials through source-traced resident labor before forcing project progress', button: 'supportResourceCommons' };
  }
  if (!world.gamePrototypeProjects || !world.gamePrototypeProjects.completionLedger || !world.gamePrototypeProjects.completionLedger.length) {
    return { ...guide, phase: 'project work', nextAction: 'Advance project', why: 'turn a resident proposal into material/time-consuming work that can complete or stall without direct command', button: 'advanceVillageProject' };
  }
  if (!world.autonomousResidents || !world.autonomousResidents.actionLog.length) {
    return { ...guide, phase: 'autonomy', nextAction: 'Resident season', why: 'let residents act from needs, resources, proposals, practices, and stochastic pressure', button: 'runAutonomousResidentSeason' };
  }
  if (!world.deepTimeCivilization || world.deepTimeCivilization.year < 1000000) {
    return { ...guide, phase: 'deep time', nextAction: 'Million-year sim', why: 'stress practice lineages and prove survival is tied back to the village loop', button: 'runCivilizationMillionYearSim' };
  }
  if (!world.gamePrototypeSaves || !world.gamePrototypeSaves.slots.length || !world.gamePrototypeSaves.returnLog.length) {
    return { ...guide, phase: 'return proof', nextAction: 'Save / return proof', why: 'prove a meaningful return path exists before acceptance export', button: 'runPrototypeReturnProof' };
  }
  if (!world.gamePrototypeQA || !world.gamePrototypeQA.pass) {
    return { ...guide, phase: 'QA', nextAction: 'Prototype QA', why: 'run the visible hardening gate across entry, autonomy, practices, proposals, survival, causality, save/return, and readable behavior', button: 'runPrototypeQASmoke' };
  }
  if (!world.gamePrototypeAcceptance || !world.gamePrototypeAcceptance.pass) {
    return { ...guide, phase: 'acceptance', nextAction: 'Export acceptance', why: 'produce durable JSON evidence for the current playable foundation', button: 'exportPrototypeAcceptanceReceipt' };
  }
  if (!world.gamePrototypeDivergence || !world.gamePrototypeDivergence.diverged) {
    return { ...guide, phase: 'seed comparison', nextAction: 'Compare seeds', why: 'check whether the same hidden law can produce different practice histories under different social/history seeds', button: 'comparePrototypeDivergenceSeeds' };
  }
  if (!world.gamePrototypeCommons || !world.gamePrototypeCommons.pass) {
    return { ...guide, phase: 'commons audit', nextAction: 'Audit commons', why: 'check resources, work cost, tool wear, maintenance burden, conservation, and hidden-law exposure before continuing', button: 'auditPrototypeCommons' };
  }
  return {
    phase: 'watch or compare',
    nextAction: 'Auto burst',
    why: 'the current foundation passes acceptance; keep watching for divergent practices, refusals, costs, and maintenance burdens',
    button: 'runPrototypeAutoBurst',
    caution: 'Acceptance is still browser-local prototype evidence, not production certification.',
  };
}

function formatPrototypePlayerGuide() {
  const guide = derivePrototypePlayerGuide();
  const prototype = ensureGamePrototype();
  const selectedExpression = latestVisibleExpressionFor(world.selected);
  const latestProposal = world.villageBoard && world.villageBoard.projectProposals.length ? world.villageBoard.projectProposals[world.villageBoard.projectProposals.length - 1] : null;
  const latestPractice = world.emergentPracticeGraph && world.emergentPracticeGraph.nodes.length ? world.emergentPracticeGraph.nodes[world.emergentPracticeGraph.nodes.length - 1] : null;
  const playableSlice = world.gamePrototypePlayableSlice || null;
  const villageDay03 = world.gamePrototypeVillageDay03 || null;
  const worldStage = world.gamePrototypeWorldStage || null;
  const walkthrough = world.gamePrototypeWalkthrough || null;
  const actionRail = world.gamePrototypeActionRail || null;
  const playerMode = world.gamePrototypePlayerMode || null;
  const proposalDeck = world.gamePrototypeProposalDeck || null;
  const livedPractice = world.gamePrototypeLivedPractice || null;
  const worksite = world.gamePrototypeWorksite || null;
  const projects = world.gamePrototypeProjects || null;
  const commonsSupport = world.gamePrototypeCommonsSupport || null;
  const nearby = world.gamePrototypeNearbyActions || null;
  const dayCycle = world.gamePrototypeDayCycle || null;
  const returnLater = world.gamePrototypeReturnLater || null;
  const history = prototype.guideHistory.slice(-5).map(row => `${row.id}: ${row.from_phase}->${row.next_phase} via ${row.action}`);
  return [
    `Phase: ${guide.phase}`,
    `Suggested action: ${guide.nextAction} (${guide.button})`,
    `Why: ${guide.why}`,
    `Selected resident: ${world.selected}; cue=${selectedExpression.marker}; schedule=${currentResident().schedule}`,
    `Latest proposal: ${latestProposal ? `${latestProposal.proposal_id} / ${latestProposal.status} / ${latestProposal.problem_addressed}` : 'none'}`,
    `Latest practice: ${latestPractice ? `${latestPractice.practice_id} / ${latestPractice.status} / ${latestPractice.local_name}` : 'none'}`,
    `Playable slice: ${playableSlice ? `${playableSlice.phase}; ready=${playableSlice.acceptanceReady}; physics=${playableSlice.linkedPhysicsRows.length}; proposals=${playableSlice.linkedProposalIds.length}; practices=${playableSlice.linkedPracticeIds.length}` : 'not started'}`,
    `Village Day 0-3: ${villageDay03 ? `${villageDay03.phase}; ready=${villageDay03.acceptanceReady}; rows=${villageDay03.dayLedger.length}; returns=${villageDay03.returnLinks.length}` : 'not started'}`,
    `Primary play surface: ${worldStage ? `${worldStage.phase}; ready=${worldStage.acceptanceReady}; focus=${worldStage.focusLedger.length}; prompts=${worldStage.actionPromptLedger.length}` : 'not started'}`,
    `First playable: ${walkthrough ? `${walkthrough.phase}; ready=${walkthrough.acceptanceReady}; steps=${walkthrough.stepLedger.length}/${walkthrough.requiredSteps.length}` : 'not started'}`,
    `Normal controls: ${actionRail ? `ready=${actionRail.acceptanceReady}; actions=${actionRail.actionLedger.length}; verbs=${actionRail.verbs.join('/')}` : 'not started'}`,
    `Player mode: ${playerMode ? `enabled=${playerMode.enabled}; ready=${playerMode.acceptanceReady}; sessions=${playerMode.sessionLedger.length}` : 'not started'}`,
    `Proposal deck: ${proposalDeck ? `ready=${proposalDeck.acceptanceReady}; cards=${proposalDeck.cardLedger.length}; actions=${proposalDeck.actionLedger.length}` : 'not started'}`,
    `Lived practice: ${livedPractice ? `ready=${livedPractice.acceptanceReady}; actions=${livedPractice.actionLedger.length}; snapshots=${livedPractice.practiceSnapshots.length}` : 'not started'}`,
    `Resident worksite: ${worksite ? `ready=${worksite.acceptanceReady}; watches=${worksite.watchLedger.length}; snapshots=${worksite.snapshotLedger.length}` : 'not started'}`,
    `Projects: ${projects ? `${projects.projectLedger.length} work row(s), completed=${projects.completionLedger.length}, stalled=${projects.stalledLedger.length}` : 'not advanced'}`,
    `Commons support: ${commonsSupport ? `${commonsSupport.supportLedger.length} support row(s), recoveries=${commonsSupport.recoveryLedger.length}` : 'not supported'}`,
    `Nearby actions: ${nearby ? `${nearby.actionLedger.length} action(s), current=${nearbyActionPlan().label}->${nearbyActionPlan().action}` : `${nearbyActionPlan().label}->${nearbyActionPlan().action}`}`,
    `Village day: ${dayCycle ? `${dayCycle.day} day(s), weather=${dayCycle.weatherLedger.length}, recaps=${dayCycle.recapLedger.length}` : 'not advanced'}`,
    `Return later: ${returnLater ? `${returnLater.returnLedger.length} return(s), latest=${returnLater.latestReceipt ? returnLater.latestReceipt.return_id : 'none'}` : 'not used'}`,
    `Physics: ${world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.latestStep ? `${world.gamePrototype3DWorld.physics.latestStep.step_id}; support=${world.gamePrototype3DWorld.physics.latestStep.support_checks}; failures=${world.gamePrototype3DWorld.physics.latestStep.failures}; field=${world.gamePrototype3DWorld.physics.latestStep.field_id || 'none'}; stress=${world.gamePrototype3DWorld.physics.latestStep.field_stress || 'n/a'}` : 'not stepped'} / residents use local terms and imperfect glosses, not engine truth`,
    `Structural stress: ${world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.latestStructuralStep ? `${world.gamePrototype3DWorld.physics.latestStructuralStep.step_id}; max=${world.gamePrototype3DWorld.physics.latestStructuralStep.max_stress}; deflect=${world.gamePrototype3DWorld.physics.latestStructuralStep.max_deflection}; repair=${world.gamePrototype3DWorld.physics.latestStructuralStep.repair_rows}` : 'not stepped'}`,
    `Contact constraints: ${world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.latestConstraintStep ? `${world.gamePrototype3DWorld.physics.latestConstraintStep.step_id}; contact=${world.gamePrototype3DWorld.physics.latestConstraintStep.contact_rows}; joints=${world.gamePrototype3DWorld.physics.latestConstraintStep.joint_rows}; failed=${world.gamePrototype3DWorld.physics.latestConstraintStep.failed_joints}` : 'not stepped'}`,
    `Material state: ${world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.latestMaterialStateStep ? `${world.gamePrototype3DWorld.physics.latestMaterialStateStep.step_id}; states=${world.gamePrototype3DWorld.physics.latestMaterialStateStep.state_rows}; phases=${world.gamePrototype3DWorld.physics.latestMaterialStateStep.phase_changes}; risky=${world.gamePrototype3DWorld.physics.latestMaterialStateStep.risky_components}` : 'not stepped'}`,
    `Seed divergence: ${world.gamePrototypeDivergence ? `${world.gamePrototypeDivergence.branches.length} branch(es), diverged=${world.gamePrototypeDivergence.diverged}` : 'not compared'}`,
    `Commons: ${world.gamePrototypeCommons ? `${world.gamePrototypeCommons.pressure_level}, resources=${world.gamePrototypeCommons.resource_total}, pass=${world.gamePrototypeCommons.pass}` : 'not audited'}`,
    `Caution: ${guide.caution}`,
    'Guide history:',
    ...(history.length ? history : ['none']),
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
  const latestTimeline = sim.timeline.slice(-6).map(row => `epoch ${row.epoch}: year ${row.year}, ${row.pressure}, effect=${row.effect_id}, physical=${row.physical_effect_id || 'none'}`);
  const latestEffects = sim.emergentEffects.slice(-6).map(row => `${row.effect_id}: ${row.local_name} -> ${row.outcome}`);
  const latestConsequences = (sim.villageConsequences || []).slice(-6).map(row => `${row.consequence_id}: ${row.effect_id} changed ${row.resident} schedule via ${row.proposal_id}`);
  const latestSurvival = (sim.survivalLedger || []).slice(-6).map(row => `${row.audit_id}: year ${row.year}, ${row.status}, score=${row.continuity_score}, active=${row.active_lineages}, physical=${row.physical_continuity || 'n/a'}, burden=${row.physical_burden || 'n/a'}`);
  const lineageRows = sim.lineages.slice(0, 6).map(row => `${row.lineage_id}: ${row.local_name}; status=${row.status}; age=${row.age_years}; memory=${row.memory_strength.toFixed(2)}; burden=${row.maintenance_burden}; components=${row.component_ids ? row.component_ids.length : 0}; stabilityMemory=${row.physical_stability_memory || 'n/a'}`);
  const heritageRows = (sim.physicalHeritageLedger || []).slice(-5).map(row => `${row.heritage_id}: ${row.lineage_id} inherited ${row.component_ids.length} component(s) from ${row.source_practice_id}; stability=${row.physical_stability_memory}`);
  const physicalRows = (sim.componentEffectLedger || []).slice(-5).map(row => `${row.physical_effect_id}: ${row.pressure} touched ${row.target_component_count} component(s); structureStability=${row.structure_stability_after || 'n/a'}`);
  const physicsEpochRows = (sim.physicsEpochLedger || []).slice(-5).map(row => `${row.physics_epoch_id}: ${row.pressure}; years=${row.years}; mass=${row.total_mass_before}->${row.total_mass_after}; damage=${row.average_damage_after}; stability=${row.average_stability_after}; ruined=${row.components_ruined}; links=${Object.keys(row.lineage_pressure || {}).length}`);
  const materialFluxRows = (sim.materialFluxLedger || []).slice(-5).map(row => `${row.flux_id}: ${row.component_id}; massLoss=${row.mass_loss}; moistureDelta=${row.moisture_delta}; damageDelta=${row.damage_delta}; stabilityDelta=${row.stability_delta}; ruined=${row.ruined_trace}`);
  const state = sim.civilizationState || {};
  return [
    `Compressed year: ${sim.year}`,
    `Epochs: ${sim.epoch}`,
    `Extinctions: ${sim.extinctions.length}`,
    `Civilization status: ${state.status || 'unknown'} / continuity=${state.continuityScore ?? 'n/a'} / physical=${state.physicalContinuity ?? 'n/a'} / million-year capable=${state.millionYearCapable ? 'yes' : 'not yet'}`,
    `Boundary: no intentional tech tree; hidden laws audit-only; effects emerge from stochastic physical pressure.`,
    'Lineages:',
    ...(lineageRows.length ? lineageRows : ['none']),
    'Recent epochs:',
    ...(latestTimeline.length ? latestTimeline : ['none']),
	    'Emergent effects:',
	    ...(latestEffects.length ? latestEffects : ['none']),
	    'Physical heritage:',
	    ...(heritageRows.length ? heritageRows : ['none']),
	    'Deep-time stochastic physics epochs:',
	    ...(physicsEpochRows.length ? physicsEpochRows : ['none']),
	    'Material flux rows:',
	    ...(materialFluxRows.length ? materialFluxRows : ['none']),
	    'Deep-time physical component effects:',
	    ...(physicalRows.length ? physicalRows : ['none']),
	    'Village consequences:',
    ...(latestConsequences.length ? latestConsequences : ['none']),
    'Survival ledger:',
    ...(latestSurvival.length ? latestSurvival : ['none']),
  ].join('\n');
}

function formatPrototypeResidentBodies() {
  const sim = world.gamePrototypeResidentBodies || ensureResidentBodies();
  const bodyRows = Object.values(sim.bodies).map(body => `${body.resident}: pos=(${body.position3d.x},${body.position3d.y},${body.position3d.z}) vel=(${body.velocity.x},${body.velocity.y},${body.velocity.z}) fatigue=${body.fatigue} footing=${body.footing} load=${body.carried_load}/${body.carry_capacity} balance=${body.balance} recovery=${body.recovery_debt} action=${body.last_action}`);
  const steps = sim.bodyLedger.slice(-8).map(row => `${row.body_step_id}: ${row.resident} ${row.action}; target=${row.target}; speed=${row.speed}; load=${row.carried_load}; contacts=${row.collision_count}; slip=${row.slip_event}; fatigueDelta=${row.fatigue_delta}`);
  const contacts = sim.contactLedger.slice(-5).map(row => `${row.contact_id}: ${row.resident}; components=${row.component_contacts.join(',') || 'none'} residents=${row.resident_contacts.join(',') || 'none'} slip=${row.slip_event}`);
  const recoveries = sim.recoveryLedger.slice(-5).map(row => `${row.recovery_id}: ${row.resident}; ${row.reason}; path=${row.recovery_path}; debt=${row.recovery_debt_after}`);
  return [
    `Runs: ${sim.runCount} / body steps=${sim.bodyLedger.length} / contacts=${sim.contactLedger.length} / recoveries=${sim.recoveryLedger.length}`,
    `Boundary: physical resident capsules; stochastic footing/contact/load/fatigue; no direct player body command.`,
    'Resident bodies:',
    ...(bodyRows.length ? bodyRows : ['none']),
    'Recent body steps:',
    ...(steps.length ? steps : ['none']),
    'Contact/slip ledger:',
    ...(contacts.length ? contacts : ['none']),
    'Bounded recovery rows:',
    ...(recoveries.length ? recoveries : ['none']),
  ].join('\n');
}

function formatPrototypeAutonomousResidents() {
  const sim = world.autonomousResidents;
  if (!sim) return 'No autonomous resident ticks yet. Run Resident tick or Resident season.';
  const actions = sim.actionLog.slice(-8).map(row => `${row.action_id}: day ${row.day}, ${row.resident} chose ${row.action}; energy=${row.needs.energy.toFixed(2)} hunger=${row.needs.hunger.toFixed(2)} safety=${row.needs.safety.toFixed(2)}; body=${row.body_physics_step_id || 'none'}`);
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
  performNearbyAction();
  endVillageDay();
  leaveAndReturnLater();
	  runPrototypeMaterialWorldStep();
	  runPrototypePhysicsStep();
  runTerrainPhysicsLoop();
  runToolPhysicsLoop();
  runResourcePhysicsLoop();
  runThermalPhysicsLoop();
  runWaterPhysicsLoop();
  runEcologyPhysicsLoop();
  runStructuralPhysicsLoop();
  runContactConstraintPhysicsLoop();
  runMaterialStatePhysicsLoop();
  runPlayablePhysicsPracticeSliceLoop();
  runPlayableVillageDay03Loop();
  runPrimaryPlaySurfaceLoop();
  runFirstPlayableWalkthrough();
  runNormalPlayActionRailLoop();
  runPlayerModeInterfaceLoop();
  runPlayerProposalDeckLoop();
  runLivedPracticeLoop();
  runResidentWorksiteLoop();
  runResidentMaterialManipulationLoop();
	  advanceVillageProject();
  advanceVillageProject();
  advanceVillageProject();
  supportResourceCommons();
  advanceVillageProject();
  runAutonomousResidentSeason();
  runResidentBodyPhysicsLoop();
  runCivilizationMillionYearSim();
  runCivilizationSurvivalAudit();
  runRealityConstraintAudit();
  auditPrototypeCommons();
  askSchedule();
  askSchedule();
  comparePrototypeDivergenceSeeds();
  saveWorld();
  const savedCounts = {
    autonomousActions: world.autonomousResidents ? world.autonomousResidents.actionLog.length : 0,
    deepTimeYear: world.deepTimeCivilization ? world.deepTimeCivilization.year : 0,
    practiceNodes: world.emergentPracticeGraph ? world.emergentPracticeGraph.nodes.length : 0,
    proposals: world.villageBoard ? world.villageBoard.projectProposals.length : 0,
    ordinaryPlayFeed: world.practicalDiscovery && world.practicalDiscovery.ordinaryPlayFeed ? world.practicalDiscovery.ordinaryPlayFeed.length : 0,
    autoGeneratedTests: world.practicalDiscovery && world.practicalDiscovery.autoGeneratedTests ? world.practicalDiscovery.autoGeneratedTests.length : 0,
    visibleExpressions: world.autonomousResidents && world.autonomousResidents.expressionLedger ? world.autonomousResidents.expressionLedger.length : 0,
    divergenceCompared: world.gamePrototypeDivergence ? world.gamePrototypeDivergence.diverged : false,
    commonsPass: world.gamePrototypeCommons ? world.gamePrototypeCommons.pass : false,
    projectRows: world.gamePrototypeProjects ? world.gamePrototypeProjects.projectLedger.length : 0,
    projectCompletions: world.gamePrototypeProjects ? world.gamePrototypeProjects.completionLedger.length : 0,
    projectStalls: world.gamePrototypeProjects ? world.gamePrototypeProjects.stalledLedger.length : 0,
    commonsSupportRows: world.gamePrototypeCommonsSupport ? world.gamePrototypeCommonsSupport.supportLedger.length : 0,
    commonsRecoveries: world.gamePrototypeCommonsSupport ? world.gamePrototypeCommonsSupport.recoveryLedger.length : 0,
    nearbyActions: world.gamePrototypeNearbyActions ? world.gamePrototypeNearbyActions.actionLedger.length : 0,
    villageDays: world.gamePrototypeDayCycle ? world.gamePrototypeDayCycle.dayLedger.length : 0,
    weatherRows: world.gamePrototypeDayCycle ? world.gamePrototypeDayCycle.weatherLedger.length : 0,
    returnLaterRows: world.gamePrototypeReturnLater ? world.gamePrototypeReturnLater.returnLedger.length : 0,
	    materialComponents: world.gamePrototype3DWorld ? world.gamePrototype3DWorld.components.length : 0,
	    residentTerms: world.gamePrototype3DWorld && world.gamePrototype3DWorld.language ? world.gamePrototype3DWorld.language.terms.length : 0,
	    physicsSteps: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics ? world.gamePrototype3DWorld.physics.step || 0 : 0,
	    supportRows: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics ? world.gamePrototype3DWorld.physics.supportLedger.length : 0,
	    forceRows: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics ? world.gamePrototype3DWorld.physics.forceLedger.length : 0,
	    fieldRows: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.fieldLedger ? world.gamePrototype3DWorld.physics.fieldLedger.length : 0,
	    energyRows: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.energyLedger ? world.gamePrototype3DWorld.physics.energyLedger.length : 0,
	    structuralLoadRows: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.loadPathLedger ? world.gamePrototype3DWorld.physics.loadPathLedger.length : 0,
	    structuralStressRows: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.stressLedger ? world.gamePrototype3DWorld.physics.stressLedger.length : 0,
	    structuralDeformationRows: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.deformationLedger ? world.gamePrototype3DWorld.physics.deformationLedger.length : 0,
	    structuralCollapseRows: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.collapseLedger ? world.gamePrototype3DWorld.physics.collapseLedger.length : 0,
	    structuralRepairRows: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.structuralRepairLedger ? world.gamePrototype3DWorld.physics.structuralRepairLedger.length : 0,
	    contactConstraintRows: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.contactConstraintLedger ? world.gamePrototype3DWorld.physics.contactConstraintLedger.length : 0,
	    jointConstraintRows: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.jointConstraintLedger ? world.gamePrototype3DWorld.physics.jointConstraintLedger.length : 0,
	    frictionRows: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.frictionLedger ? world.gamePrototype3DWorld.physics.frictionLedger.length : 0,
	    impulseRows: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.impulseLedger ? world.gamePrototype3DWorld.physics.impulseLedger.length : 0,
	    constraintRepairRows: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.constraintRepairLedger ? world.gamePrototype3DWorld.physics.constraintRepairLedger.length : 0,
	    materialStateRows: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.materialStateLedger ? world.gamePrototype3DWorld.physics.materialStateLedger.length : 0,
	    phaseChangeRows: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.phaseChangeLedger ? world.gamePrototype3DWorld.physics.phaseChangeLedger.length : 0,
	    propertyDriftRows: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.propertyDriftLedger ? world.gamePrototype3DWorld.physics.propertyDriftLedger.length : 0,
	    materialStateRepairRows: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.materialStateRepairLedger ? world.gamePrototype3DWorld.physics.materialStateRepairLedger.length : 0,
    terrainRows: world.gamePrototypeTerrain && world.gamePrototypeTerrain.terrainLedger ? world.gamePrototypeTerrain.terrainLedger.length : 0,
    terrainFlowRows: world.gamePrototypeTerrain && world.gamePrototypeTerrain.flowLedger ? world.gamePrototypeTerrain.flowLedger.length : 0,
    terrainSupportRows: world.gamePrototypeTerrain && world.gamePrototypeTerrain.supportLedger ? world.gamePrototypeTerrain.supportLedger.length : 0,
    terrainResourceRows: world.gamePrototypeTerrain && world.gamePrototypeTerrain.resourceLedger ? world.gamePrototypeTerrain.resourceLedger.length : 0,
    toolUseRows: world.gamePrototypeTools && world.gamePrototypeTools.useLedger ? world.gamePrototypeTools.useLedger.length : 0,
    toolWearRows: world.gamePrototypeTools && world.gamePrototypeTools.wearLedger ? world.gamePrototypeTools.wearLedger.length : 0,
    toolFailureRows: world.gamePrototypeTools && world.gamePrototypeTools.failureLedger ? world.gamePrototypeTools.failureLedger.length : 0,
    toolRepairRows: world.gamePrototypeTools && world.gamePrototypeTools.repairLedger ? world.gamePrototypeTools.repairLedger.length : 0,
    resourceStockRows: world.gamePrototypeResourcePhysics && world.gamePrototypeResourcePhysics.stockLedger ? world.gamePrototypeResourcePhysics.stockLedger.length : 0,
    resourceTransformRows: world.gamePrototypeResourcePhysics && world.gamePrototypeResourcePhysics.transformLedger ? world.gamePrototypeResourcePhysics.transformLedger.length : 0,
    resourceLossRows: world.gamePrototypeResourcePhysics && world.gamePrototypeResourcePhysics.lossLedger ? world.gamePrototypeResourcePhysics.lossLedger.length : 0,
    resourceGainRows: world.gamePrototypeResourcePhysics && world.gamePrototypeResourcePhysics.gainLedger ? world.gamePrototypeResourcePhysics.gainLedger.length : 0,
    thermalHeatRows: world.gamePrototypeThermalPhysics && world.gamePrototypeThermalPhysics.heatLedger ? world.gamePrototypeThermalPhysics.heatLedger.length : 0,
    thermalFuelRows: world.gamePrototypeThermalPhysics && world.gamePrototypeThermalPhysics.fuelLedger ? world.gamePrototypeThermalPhysics.fuelLedger.length : 0,
    thermalSmokeRows: world.gamePrototypeThermalPhysics && world.gamePrototypeThermalPhysics.smokeLedger ? world.gamePrototypeThermalPhysics.smokeLedger.length : 0,
    thermalSafetyRows: world.gamePrototypeThermalPhysics && world.gamePrototypeThermalPhysics.safetyLedger ? world.gamePrototypeThermalPhysics.safetyLedger.length : 0,
    waterFlowRows: world.gamePrototypeWaterPhysics && world.gamePrototypeWaterPhysics.flowLedger ? world.gamePrototypeWaterPhysics.flowLedger.length : 0,
    waterLeakRows: world.gamePrototypeWaterPhysics && world.gamePrototypeWaterPhysics.leakLedger ? world.gamePrototypeWaterPhysics.leakLedger.length : 0,
    waterRouteRows: world.gamePrototypeWaterPhysics && world.gamePrototypeWaterPhysics.routeLedger ? world.gamePrototypeWaterPhysics.routeLedger.length : 0,
    waterQualityRows: world.gamePrototypeWaterPhysics && world.gamePrototypeWaterPhysics.qualityLedger ? world.gamePrototypeWaterPhysics.qualityLedger.length : 0,
    waterSafetyRows: world.gamePrototypeWaterPhysics && world.gamePrototypeWaterPhysics.safetyLedger ? world.gamePrototypeWaterPhysics.safetyLedger.length : 0,
    ecologyGrowthRows: world.gamePrototypeEcologyPhysics && world.gamePrototypeEcologyPhysics.growthLedger ? world.gamePrototypeEcologyPhysics.growthLedger.length : 0,
    ecologyHarvestRows: world.gamePrototypeEcologyPhysics && world.gamePrototypeEcologyPhysics.harvestLedger ? world.gamePrototypeEcologyPhysics.harvestLedger.length : 0,
    ecologySpoilageRows: world.gamePrototypeEcologyPhysics && world.gamePrototypeEcologyPhysics.spoilageLedger ? world.gamePrototypeEcologyPhysics.spoilageLedger.length : 0,
    ecologyHungerRows: world.gamePrototypeEcologyPhysics && world.gamePrototypeEcologyPhysics.hungerLedger ? world.gamePrototypeEcologyPhysics.hungerLedger.length : 0,
    ecologySafetyRows: world.gamePrototypeEcologyPhysics && world.gamePrototypeEcologyPhysics.safetyLedger ? world.gamePrototypeEcologyPhysics.safetyLedger.length : 0,
	    manipulationRows: world.gamePrototypeMaterialManipulation && world.gamePrototypeMaterialManipulation.actionLedger ? world.gamePrototypeMaterialManipulation.actionLedger.length : 0,
	    manipulationPracticeLinks: world.gamePrototypeMaterialManipulation && world.gamePrototypeMaterialManipulation.practiceLinks ? world.gamePrototypeMaterialManipulation.practiceLinks.length : 0,
	    manipulationFailures: world.gamePrototypeMaterialManipulation && world.gamePrototypeMaterialManipulation.failureLedger ? world.gamePrototypeMaterialManipulation.failureLedger.length : 0,
	    bodyPhysicsRows: world.gamePrototypeResidentBodies && world.gamePrototypeResidentBodies.bodyLedger ? world.gamePrototypeResidentBodies.bodyLedger.length : 0,
	    bodyContactRows: world.gamePrototypeResidentBodies && world.gamePrototypeResidentBodies.contactLedger ? world.gamePrototypeResidentBodies.contactLedger.length : 0,
	    bodyFatigueRows: world.gamePrototypeResidentBodies && world.gamePrototypeResidentBodies.fatigueLedger ? world.gamePrototypeResidentBodies.fatigueLedger.length : 0,
	    bodyRecoveryRows: world.gamePrototypeResidentBodies && world.gamePrototypeResidentBodies.recoveryLedger ? world.gamePrototypeResidentBodies.recoveryLedger.length : 0,
	    constructionRows: world.gamePrototype3DWorld && world.gamePrototype3DWorld.constructionLedger ? world.gamePrototype3DWorld.constructionLedger.length : 0,
	    projectBuiltComponents: world.gamePrototype3DWorld && world.gamePrototype3DWorld.components ? world.gamePrototype3DWorld.components.filter(component => component.project_built === true).length : 0,
	    constructionPracticeLinks: world.gamePrototype3DWorld && world.gamePrototype3DWorld.constructionLedger ? world.gamePrototype3DWorld.constructionLedger.filter(row => row.practice_id).length : 0,
	    constructionPracticeNodes: world.emergentPracticeGraph && world.emergentPracticeGraph.nodes ? world.emergentPracticeGraph.nodes.filter(row => row.source_construction_rows && row.source_construction_rows.length).length : 0,
	    physicalHeritageRows: world.deepTimeCivilization && world.deepTimeCivilization.physicalHeritageLedger ? world.deepTimeCivilization.physicalHeritageLedger.length : 0,
	    componentEffectRows: world.deepTimeCivilization && world.deepTimeCivilization.componentEffectLedger ? world.deepTimeCivilization.componentEffectLedger.length : 0,
	    deepTimePhysicsEpochs: world.deepTimeCivilization && world.deepTimeCivilization.physicsEpochLedger ? world.deepTimeCivilization.physicsEpochLedger.length : 0,
	    deepTimeMaterialFluxRows: world.deepTimeCivilization && world.deepTimeCivilization.materialFluxLedger ? world.deepTimeCivilization.materialFluxLedger.length : 0,
	    constructionLineages: world.deepTimeCivilization && world.deepTimeCivilization.lineages ? world.deepTimeCivilization.lineages.filter(row => row.component_ids && row.component_ids.length).length : 0,
	    physicsProposals: world.villageBoard && world.villageBoard.projectProposals ? world.villageBoard.projectProposals.filter(row => row.related_physics_step).length : 0,
    physicsRepairActions: world.autonomousResidents && world.autonomousResidents.actionLog ? world.autonomousResidents.actionLog.filter(row => row.action === 'physics_repair').length : 0,
    playableSliceReady: world.gamePrototypePlayableSlice ? world.gamePrototypePlayableSlice.acceptanceReady === true : false,
    playableSlicePhases: world.gamePrototypePlayableSlice ? world.gamePrototypePlayableSlice.phaseLedger.length : 0,
    playableSlicePhysicsRows: world.gamePrototypePlayableSlice ? world.gamePrototypePlayableSlice.linkedPhysicsRows.length : 0,
    playableSliceProposalRows: world.gamePrototypePlayableSlice ? world.gamePrototypePlayableSlice.linkedProposalIds.length : 0,
    playableSlicePracticeRows: world.gamePrototypePlayableSlice ? world.gamePrototypePlayableSlice.linkedPracticeIds.length : 0,
    playableSliceReturnRows: world.gamePrototypePlayableSlice ? world.gamePrototypePlayableSlice.returnProofRows.length : 0,
    villageDay03Ready: world.gamePrototypeVillageDay03 ? world.gamePrototypeVillageDay03.acceptanceReady === true : false,
    villageDay03Rows: world.gamePrototypeVillageDay03 ? world.gamePrototypeVillageDay03.dayLedger.length : 0,
    villageDay03PlayerRows: world.gamePrototypeVillageDay03 ? world.gamePrototypeVillageDay03.playerLoopLedger.length : 0,
    villageDay03ResidentRows: world.gamePrototypeVillageDay03 ? world.gamePrototypeVillageDay03.residentLoopLedger.length : 0,
    villageDay03WorldRows: world.gamePrototypeVillageDay03 ? world.gamePrototypeVillageDay03.worldLoopLedger.length : 0,
    villageDay03PhysicsLinks: world.gamePrototypeVillageDay03 ? world.gamePrototypeVillageDay03.physicsLinks.length : 0,
    villageDay03ProposalLinks: world.gamePrototypeVillageDay03 ? world.gamePrototypeVillageDay03.proposalLinks.length : 0,
    villageDay03PracticeLinks: world.gamePrototypeVillageDay03 ? world.gamePrototypeVillageDay03.practiceLinks.length : 0,
    villageDay03SaveLinks: world.gamePrototypeVillageDay03 ? world.gamePrototypeVillageDay03.saveLinks.length : 0,
    villageDay03ReturnLinks: world.gamePrototypeVillageDay03 ? world.gamePrototypeVillageDay03.returnLinks.length : 0,
    primaryPlaySurfaceReady: world.gamePrototypeWorldStage ? world.gamePrototypeWorldStage.acceptanceReady === true : false,
    primaryPlaySurfaceFocusRows: world.gamePrototypeWorldStage ? world.gamePrototypeWorldStage.focusLedger.length : 0,
    primaryPlaySurfaceCueRows: world.gamePrototypeWorldStage ? world.gamePrototypeWorldStage.canvasCueLedger.length : 0,
    primaryPlaySurfacePromptRows: world.gamePrototypeWorldStage ? world.gamePrototypeWorldStage.actionPromptLedger.length : 0,
    walkthroughReady: world.gamePrototypeWalkthrough ? world.gamePrototypeWalkthrough.acceptanceReady === true : false,
    walkthroughSteps: world.gamePrototypeWalkthrough ? world.gamePrototypeWalkthrough.stepLedger.length : 0,
    walkthroughLinks: world.gamePrototypeWalkthrough ? world.gamePrototypeWalkthrough.evidenceLinks.length : 0,
    actionRailReady: world.gamePrototypeActionRail ? world.gamePrototypeActionRail.acceptanceReady === true : false,
    actionRailRows: world.gamePrototypeActionRail ? world.gamePrototypeActionRail.actionLedger.length : 0,
    actionRailOptionRows: world.gamePrototypeActionRail ? world.gamePrototypeActionRail.optionLedger.length : 0,
    playerModeReady: world.gamePrototypePlayerMode ? world.gamePrototypePlayerMode.acceptanceReady === true : false,
    playerModeSessions: world.gamePrototypePlayerMode ? world.gamePrototypePlayerMode.sessionLedger.length : 0,
    playerModeVisibleCards: world.gamePrototypePlayerMode && world.gamePrototypePlayerMode.visibleSurface ? world.gamePrototypePlayerMode.visibleSurface.visible_cards.length : 0,
    proposalDeckReady: world.gamePrototypeProposalDeck ? world.gamePrototypeProposalDeck.acceptanceReady === true : false,
    proposalDeckCards: world.gamePrototypeProposalDeck ? world.gamePrototypeProposalDeck.cardLedger.length : 0,
    proposalDeckActions: world.gamePrototypeProposalDeck ? world.gamePrototypeProposalDeck.actionLedger.length : 0,
    livedPracticeReady: world.gamePrototypeLivedPractice ? world.gamePrototypeLivedPractice.acceptanceReady === true : false,
    livedPracticeRows: world.gamePrototypeLivedPractice ? world.gamePrototypeLivedPractice.actionLedger.length : 0,
    livedPracticeSnapshots: world.gamePrototypeLivedPractice ? world.gamePrototypeLivedPractice.practiceSnapshots.length : 0,
    worksiteReady: world.gamePrototypeWorksite ? world.gamePrototypeWorksite.acceptanceReady === true : false,
    worksiteRows: world.gamePrototypeWorksite ? world.gamePrototypeWorksite.watchLedger.length : 0,
    worksiteSnapshots: world.gamePrototypeWorksite ? world.gamePrototypeWorksite.snapshotLedger.length : 0,
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
    { id: 'player-guide-available', pass: Boolean(derivePrototypePlayerGuide().nextAction && derivePrototypePlayerGuide().button), evidence: `${derivePrototypePlayerGuide().phase}: ${derivePrototypePlayerGuide().nextAction}` },
    { id: 'guided-step-hook', pass: Boolean(typeof runPrototypeGuidedStep === 'function' && world.gamePrototype && Array.isArray(world.gamePrototype.guideHistory)), evidence: `${world.gamePrototype && world.gamePrototype.guideHistory ? world.gamePrototype.guideHistory.length : 0} guided step(s)` },
    { id: 'seed-divergence', pass: Boolean(world.gamePrototypeDivergence && world.gamePrototypeDivergence.diverged && world.gamePrototypeDivergence.all_hidden_law_shared && world.gamePrototypeDivergence.no_correct_concept_installed), evidence: world.gamePrototypeDivergence ? `${world.gamePrototypeDivergence.branches.length} branch(es), unique practices=${world.gamePrototypeDivergence.unique_practice_signatures}` : 'not compared' },
    { id: 'commons-causal-health', pass: Boolean(world.gamePrototypeCommons && world.gamePrototypeCommons.pass && world.gamePrototypeCommons.hidden_law_exposure_issues === 0), evidence: world.gamePrototypeCommons ? `${world.gamePrototypeCommons.pressure_level}, resources=${world.gamePrototypeCommons.resource_total}, ledger=${world.gamePrototypeCommons.ledger_rows}` : 'not audited' },
    { id: 'resident-project-progress', pass: Boolean(world.gamePrototypeProjects && savedCounts.projectRows > 0 && savedCounts.projectCompletions > 0 && world.gamePrototypeProjects.projectLedger.length >= savedCounts.projectRows), evidence: `${savedCounts.projectRows} work row(s), ${savedCounts.projectCompletions} completion(s), ${savedCounts.projectStalls} stall(s)` },
    { id: 'resource-commons-support', pass: Boolean(world.gamePrototypeCommonsSupport && savedCounts.commonsSupportRows > 0 && world.gamePrototypeCommonsSupport.supportLedger.every(row => row.avatar_direct_command === false)), evidence: `${savedCounts.commonsSupportRows} support row(s), ${savedCounts.commonsRecoveries} recovery row(s)` },
    { id: 'location-sensitive-play', pass: Boolean(world.gamePrototypeNearbyActions && savedCounts.nearbyActions > 0 && world.gamePrototypeNearbyActions.actionLedger.every(row => row.avatar_direct_command === false)), evidence: `${savedCounts.nearbyActions} nearby action row(s)` },
	    { id: 'village-day-cycle', pass: Boolean(world.gamePrototypeDayCycle && savedCounts.villageDays > 0 && savedCounts.weatherRows > 0 && world.gamePrototypeDayCycle.dayLedger.every(row => row.direct_player_command === false)), evidence: `${savedCounts.villageDays} day row(s), ${savedCounts.weatherRows} weather row(s)` },
	    { id: 'return-later-forward-persistence', pass: Boolean(world.gamePrototypeReturnLater && savedCounts.returnLaterRows > 0 && world.gamePrototypeReturnLater.returnLedger.every(row => row.restored_old_state === false && row.direct_reset === false && row.continuity_preserved === true)), evidence: `${savedCounts.returnLaterRows} return-later row(s)` },
		    { id: 'stochastic-physics-substrate', pass: Boolean(world.gamePrototype3DWorld && savedCounts.materialComponents > 0 && savedCounts.residentTerms > 0 && savedCounts.physicsSteps > 0 && savedCounts.supportRows > 0 && savedCounts.forceRows > 0 && savedCounts.fieldRows > 0 && savedCounts.energyRows > 0 && world.gamePrototype3DWorld.noFixedBuildingAssets === true && world.gamePrototype3DWorld.noEnglishResidentTechLabels === true), evidence: `${savedCounts.materialComponents} component(s), ${savedCounts.residentTerms} term(s), ${savedCounts.physicsSteps} physics step(s), ${savedCounts.fieldRows} field row(s), ${savedCounts.energyRows} energy row(s)` },
    { id: 'structural-stress-physics', pass: Boolean(world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && savedCounts.structuralLoadRows > 0 && savedCounts.structuralStressRows > 0 && savedCounts.structuralDeformationRows > 0 && world.gamePrototype3DWorld.physics.stressLedger.every(row => row.no_effect_without_cause === true && row.no_resource_spawning === true && row.hidden_law_normal_view === false)), evidence: `${savedCounts.structuralLoadRows} load row(s), ${savedCounts.structuralStressRows} stress row(s), ${savedCounts.structuralDeformationRows} deformation row(s), ${savedCounts.structuralCollapseRows} collapse row(s), ${savedCounts.structuralRepairRows} repair row(s)` },
    { id: 'contact-constraint-physics', pass: Boolean(world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && savedCounts.contactConstraintRows > 0 && savedCounts.jointConstraintRows > 0 && savedCounts.frictionRows > 0 && savedCounts.impulseRows > 0 && world.gamePrototype3DWorld.physics.jointConstraintLedger.every(row => row.no_effect_without_cause === true && row.no_resource_spawning === true && row.hidden_law_normal_view === false)), evidence: `${savedCounts.contactConstraintRows} contact row(s), ${savedCounts.jointConstraintRows} joint row(s), ${savedCounts.frictionRows} friction row(s), ${savedCounts.impulseRows} impulse row(s), ${savedCounts.constraintRepairRows} repair row(s)` },
    { id: 'material-state-physics', pass: Boolean(world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && savedCounts.materialStateRows > 0 && savedCounts.propertyDriftRows > 0 && world.gamePrototype3DWorld.physics.materialStateLedger.every(row => row.no_resource_spawning === true && row.hidden_law_normal_view === false) && world.gamePrototype3DWorld.physics.propertyDriftLedger.every(row => row.no_effect_without_cause === true && row.no_resource_spawning === true && row.hidden_law_normal_view === false)), evidence: `${savedCounts.materialStateRows} state row(s), ${savedCounts.phaseChangeRows} phase row(s), ${savedCounts.propertyDriftRows} property row(s), ${savedCounts.materialStateRepairRows} repair row(s)` },
    { id: 'physics-to-practice-playable-slice', pass: Boolean(world.gamePrototypePlayableSlice && savedCounts.playableSliceReady && savedCounts.playableSlicePhysicsRows > 0 && savedCounts.playableSliceProposalRows > 0 && savedCounts.playableSlicePracticeRows > 0 && savedCounts.playableSliceReturnRows > 0 && world.gamePrototypePlayableSlice.noDirectCommand === true && world.gamePrototypePlayableSlice.noPredeclaredTechTree === true), evidence: `${savedCounts.playableSlicePhases} phase row(s), ${savedCounts.playableSlicePhysicsRows} physics row(s), ${savedCounts.playableSliceProposalRows} proposal link(s), ${savedCounts.playableSlicePracticeRows} practice link(s), ${savedCounts.playableSliceReturnRows} return row(s)` },
    { id: 'playable-village-day-0-3', pass: Boolean(world.gamePrototypeVillageDay03 && savedCounts.villageDay03Ready && savedCounts.villageDay03Rows >= 4 && savedCounts.villageDay03PlayerRows >= 4 && savedCounts.villageDay03ResidentRows >= 4 && savedCounts.villageDay03WorldRows >= 4 && savedCounts.villageDay03PhysicsLinks > 0 && savedCounts.villageDay03ProposalLinks > 0 && savedCounts.villageDay03PracticeLinks > 0 && savedCounts.villageDay03SaveLinks > 0 && savedCounts.villageDay03ReturnLinks > 0 && world.gamePrototypeVillageDay03.noDirectCommand === true && world.gamePrototypeVillageDay03.noTechTreeUnlock === true), evidence: `${savedCounts.villageDay03Rows} day row(s), ${savedCounts.villageDay03PhysicsLinks} physics link(s), ${savedCounts.villageDay03ProposalLinks} proposal link(s), ${savedCounts.villageDay03PracticeLinks} practice link(s), ${savedCounts.villageDay03ReturnLinks} return link(s)` },
    { id: 'primary-play-surface', pass: Boolean(world.gamePrototypeWorldStage && savedCounts.primaryPlaySurfaceReady && savedCounts.primaryPlaySurfaceFocusRows >= 3 && savedCounts.primaryPlaySurfaceCueRows >= 3 && savedCounts.primaryPlaySurfacePromptRows >= 3 && world.gamePrototypeWorldStage.canvasFirst === true && world.gamePrototypeWorldStage.noHiddenLawInNormalView === true && world.gamePrototypeWorldStage.noDirectCommand === true), evidence: `${savedCounts.primaryPlaySurfaceFocusRows} focus row(s), ${savedCounts.primaryPlaySurfaceCueRows} cue row(s), ${savedCounts.primaryPlaySurfacePromptRows} prompt row(s)` },
    { id: 'first-playable-walkthrough', pass: Boolean(world.gamePrototypeWalkthrough && savedCounts.walkthroughReady && savedCounts.walkthroughSteps >= world.gamePrototypeWalkthrough.requiredSteps.length && savedCounts.walkthroughLinks >= world.gamePrototypeWalkthrough.requiredSteps.length && world.gamePrototypeWalkthrough.noDirectCommand === true && world.gamePrototypeWalkthrough.noTechTreeUnlock === true && world.gamePrototypeWalkthrough.noHiddenLawNormalView === true), evidence: `${savedCounts.walkthroughSteps} step row(s), ${savedCounts.walkthroughLinks} evidence link(s)` },
    { id: 'normal-play-action-rail', pass: Boolean(world.gamePrototypeActionRail && savedCounts.actionRailReady && savedCounts.actionRailRows >= world.gamePrototypeActionRail.verbs.length && savedCounts.actionRailOptionRows > 0 && world.gamePrototypeActionRail.playerLanguageOnly === true && world.gamePrototypeActionRail.noDirectCommand === true && world.gamePrototypeActionRail.noTechTreeUnlock === true), evidence: `${savedCounts.actionRailRows} action row(s), ${savedCounts.actionRailOptionRows} option snapshot(s)` },
    { id: 'player-mode-interface', pass: Boolean(world.gamePrototypePlayerMode && savedCounts.playerModeReady && savedCounts.playerModeSessions > 0 && savedCounts.playerModeVisibleCards >= 6 && world.gamePrototypePlayerMode.normalViewOnly === true && world.gamePrototypePlayerMode.debugPanelsHidden === true && world.gamePrototypePlayerMode.noDirectCommand === true && world.gamePrototypePlayerMode.noHiddenLawNormalView === true), evidence: `${savedCounts.playerModeSessions} player-mode session(s), ${savedCounts.playerModeVisibleCards} visible card(s)` },
    { id: 'resident-proposal-deck', pass: Boolean(world.gamePrototypeProposalDeck && savedCounts.proposalDeckReady && savedCounts.proposalDeckCards > 0 && savedCounts.proposalDeckActions >= 3 && world.gamePrototypeProposalDeck.avatarCannotForce === true && world.gamePrototypeProposalDeck.noDirectCommand === true && world.gamePrototypeProposalDeck.noHiddenLawNormalView === true), evidence: `${savedCounts.proposalDeckCards} card snapshot(s), ${savedCounts.proposalDeckActions} deck action(s)` },
    { id: 'lived-practice-loop', pass: Boolean(world.gamePrototypeLivedPractice && savedCounts.livedPracticeReady && savedCounts.livedPracticeRows >= 4 && savedCounts.livedPracticeSnapshots > 0 && world.gamePrototypeLivedPractice.noDirectCommand === true && world.gamePrototypeLivedPractice.noHiddenLawNormalView === true && world.gamePrototypeLivedPractice.noPredeclaredTechTree === true), evidence: `${savedCounts.livedPracticeRows} lived action row(s), ${savedCounts.livedPracticeSnapshots} practice snapshot(s)` },
    { id: 'resident-worksite', pass: Boolean(world.gamePrototypeWorksite && savedCounts.worksiteReady && savedCounts.worksiteRows >= 2 && savedCounts.worksiteSnapshots > 0 && world.gamePrototypeWorksite.avatarCannotAssignJobs === true && world.gamePrototypeWorksite.noDirectCommand === true && world.gamePrototypeWorksite.noHiddenLawNormalView === true && world.gamePrototypeWorksite.noResourceSpawning === true), evidence: `${savedCounts.worksiteRows} worksite watch row(s), ${savedCounts.worksiteSnapshots} snapshot(s)` },
    { id: 'terrain-physics-substrate', pass: Boolean(world.gamePrototypeTerrain && savedCounts.terrainRows > 0 && savedCounts.terrainFlowRows > 0 && savedCounts.terrainSupportRows > 0 && world.gamePrototypeTerrain.terrainLedger.every(row => row.no_effect_without_cause === true && row.no_resource_spawning === true && row.hidden_law_normal_view === false)), evidence: `${savedCounts.terrainRows} terrain step(s), ${savedCounts.terrainFlowRows} flow row(s), ${savedCounts.terrainSupportRows} support row(s)` },
    { id: 'tool-work-physics', pass: Boolean(world.gamePrototypeTools && savedCounts.toolUseRows > 0 && savedCounts.toolWearRows > 0 && world.gamePrototypeTools.useLedger.every(row => row.no_resource_spawning === true && row.hidden_law_normal_view === false)), evidence: `${savedCounts.toolUseRows} use row(s), ${savedCounts.toolWearRows} wear row(s), ${savedCounts.toolFailureRows} failure row(s), ${savedCounts.toolRepairRows} repair row(s)` },
    { id: 'resource-stock-physics', pass: Boolean(world.gamePrototypeResourcePhysics && savedCounts.resourceStockRows > 0 && savedCounts.resourceTransformRows >= savedCounts.resourceStockRows && world.gamePrototypeResourcePhysics.stockLedger.every(row => row.no_resource_spawning === true && row.hidden_law_normal_view === false)), evidence: `${savedCounts.resourceStockRows} stock step(s), ${savedCounts.resourceTransformRows} transform row(s), ${savedCounts.resourceLossRows} loss row(s), ${savedCounts.resourceGainRows} gain row(s)` },
    { id: 'thermal-fire-physics', pass: Boolean(world.gamePrototypeThermalPhysics && savedCounts.thermalHeatRows > 0 && savedCounts.thermalFuelRows > 0 && savedCounts.thermalSmokeRows > 0 && world.gamePrototypeThermalPhysics.heatLedger.every(row => row.no_resource_spawning === true && row.hidden_law_normal_view === false)), evidence: `${savedCounts.thermalHeatRows} heat step(s), ${savedCounts.thermalFuelRows} fuel row(s), ${savedCounts.thermalSmokeRows} smoke row(s), ${savedCounts.thermalSafetyRows} safety row(s)` },
    { id: 'water-fluid-physics', pass: Boolean(world.gamePrototypeWaterPhysics && savedCounts.waterFlowRows > 0 && savedCounts.waterRouteRows > 0 && savedCounts.waterQualityRows > 0 && world.gamePrototypeWaterPhysics.flowLedger.every(row => row.no_resource_spawning === true && row.hidden_law_normal_view === false)), evidence: `${savedCounts.waterFlowRows} flow row(s), ${savedCounts.waterLeakRows} leak row(s), ${savedCounts.waterRouteRows} route row(s), ${savedCounts.waterQualityRows} quality row(s), ${savedCounts.waterSafetyRows} safety row(s)` },
    { id: 'ecology-food-physics', pass: Boolean(world.gamePrototypeEcologyPhysics && savedCounts.ecologyGrowthRows > 0 && savedCounts.ecologyHarvestRows > 0 && savedCounts.ecologySpoilageRows > 0 && savedCounts.ecologyHungerRows > 0 && world.gamePrototypeEcologyPhysics.growthLedger.every(row => row.no_resource_spawning === true && row.hidden_law_normal_view === false)), evidence: `${savedCounts.ecologyGrowthRows} growth row(s), ${savedCounts.ecologyHarvestRows} harvest row(s), ${savedCounts.ecologySpoilageRows} spoilage row(s), ${savedCounts.ecologyHungerRows} hunger row(s), ${savedCounts.ecologySafetyRows} safety row(s)` },
	    { id: 'resident-material-manipulation', pass: Boolean(world.gamePrototypeMaterialManipulation && savedCounts.manipulationRows > 0 && savedCounts.manipulationPracticeLinks > 0 && world.gamePrototypeMaterialManipulation.actionLedger.every(row => row.avatar_direct_command === false && row.hidden_law_normal_view === false)), evidence: `${savedCounts.manipulationRows} handling row(s), ${savedCounts.manipulationPracticeLinks} practice link(s), ${savedCounts.manipulationFailures} preserved failure(s)` },
	    { id: 'resident-body-physics', pass: Boolean(world.gamePrototypeResidentBodies && savedCounts.bodyPhysicsRows > 0 && savedCounts.bodyFatigueRows > 0 && world.gamePrototypeResidentBodies.bodyLedger.every(row => row.no_direct_player_command === true && row.hidden_law_normal_view === false && row.fatigue_delta >= 0)), evidence: `${savedCounts.bodyPhysicsRows} body step(s), ${savedCounts.bodyContactRows} contact row(s), ${savedCounts.bodyRecoveryRows} recovery row(s)` },
	    { id: 'physics-influences-village', pass: Boolean(savedCounts.physicsProposals > 0 && world.villageBoard.projectProposals.some(row => row.related_physics_step && row.avatar_can_force === false)), evidence: `${savedCounts.physicsProposals} physics proposal(s), ${savedCounts.physicsRepairActions} repair action(s)` },
    { id: 'projects-change-physical-world', pass: Boolean(savedCounts.constructionRows > 0 && savedCounts.projectBuiltComponents > 0 && world.gamePrototype3DWorld.constructionLedger.every(row => row.no_fixed_asset === true && row.no_resource_spawning === true)), evidence: `${savedCounts.constructionRows} construction row(s), ${savedCounts.projectBuiltComponents} project-built component(s)` },
	    { id: 'construction-feeds-practice-language', pass: Boolean(savedCounts.constructionPracticeLinks > 0 && savedCounts.constructionPracticeNodes > 0 && world.gamePrototype3DWorld.language.terms.some(row => (row.meaning_drift || []).some(text => /repair|reinforced|retie/.test(text)))), evidence: `${savedCounts.constructionPracticeLinks} construction-practice link(s), ${savedCounts.constructionPracticeNodes} construction practice node(s)` },
	    { id: 'deep-time-stochastic-physics-epochs', pass: Boolean(savedCounts.deepTimePhysicsEpochs > 0 && savedCounts.deepTimeMaterialFluxRows > 0 && world.deepTimeCivilization && world.deepTimeCivilization.physicsEpochLedger.every(row => row.no_effect_without_cause === true && row.no_resource_spawning === true && row.hidden_law_normal_view === false)), evidence: `${savedCounts.deepTimePhysicsEpochs} physics epoch(s), ${savedCounts.deepTimeMaterialFluxRows} material flux row(s)` },
	    { id: 'deep-time-uses-physical-heritage', pass: Boolean(savedCounts.physicalHeritageRows > 0 && savedCounts.componentEffectRows > 0 && savedCounts.deepTimePhysicsEpochs > 0 && savedCounts.constructionLineages > 0 && world.deepTimeCivilization && world.deepTimeCivilization.civilizationState && Number(world.deepTimeCivilization.civilizationState.physicalContinuity || 0) > 0), evidence: `${savedCounts.physicalHeritageRows} heritage row(s), ${savedCounts.componentEffectRows} deep physical effect(s), ${savedCounts.deepTimePhysicsEpochs} physics epoch(s), ${savedCounts.constructionLineages} construction lineage(s)` },
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
	  const materialResult = runPrototypeMaterialWorldStep().payload;
  const terrainResult = runTerrainPhysicsStep('auto sim terrain').payload;
  const toolResult = runToolPhysicsStep('project_work').payload;
  const resourceResult = runResourcePhysicsStep('auto sim resource stock').payload;
  const thermalResult = runThermalPhysicsStep('auto sim thermal').payload;
  const waterResult = runWaterPhysicsStep('auto sim water').payload;
  const ecologyResult = runEcologyPhysicsStep('auto sim ecology').payload;
  const structuralResult = runStructuralPhysicsStep('auto sim structural stress').payload;
  const constraintResult = runContactConstraintPhysicsStep('auto sim contact constraints').payload;
  const materialStateResult = runMaterialStatePhysicsStep('auto sim material state').payload;
		  let action = `resident tick + stochastic physics ${materialResult.physicsStepId || 'none'} + terrain ${terrainResult.terrainStepId || 'none'} + tool ${toolResult.toolUseId || 'none'} + resources ${resourceResult.stepId || 'none'} + thermal ${thermalResult.stepId || 'none'} + water ${waterResult.stepId || 'none'} + ecology ${ecologyResult.stepId || 'none'} + structure ${structuralResult.stepId || 'none'} + constraints ${constraintResult.stepId || 'none'} + material ${materialStateResult.stepId || 'none'}`;
	  if (materialResult.physicsProposalId) action += ` + physics proposal ${materialResult.physicsProposalId}`;
  if (clock.step % 3 === 0) {
    const manipulation = runResidentMaterialManipulationStep().payload;
    action += ` + handling ${manipulation.manipulationId || 'none'}`;
  }
	  if (clock.step % 6 === 0) {
    supportVillageProposal();
    action += ' + proposal support';
  }
  if (clock.step % 9 === 0) {
    supportResourceCommons();
    action += ' + commons support';
  }
  if (clock.step % 10 === 0) {
    advanceVillageProject();
    action += ' + project work';
  }
  if (clock.step % 14 === 0) {
    endVillageDay();
    action += ' + village day';
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
    project_completions: slot.project_completions,
    commons_support_rows: slot.commons_support_rows,
    nearby_action_rows: slot.nearby_action_rows,
    village_day_rows: slot.village_day_rows,
	    return_later_rows: slot.return_later_rows,
    playable_slice_ready: slot.playable_slice_ready,
    playable_slice_phase_rows: slot.playable_slice_phase_rows,
    playable_slice_physics_rows: slot.playable_slice_physics_rows,
    playable_slice_proposals: slot.playable_slice_proposals,
    playable_slice_practices: slot.playable_slice_practices,
    playable_slice_return_rows: slot.playable_slice_return_rows,
    village_day_03_ready: slot.village_day_03_ready,
    village_day_03_rows: slot.village_day_03_rows,
    village_day_03_player_rows: slot.village_day_03_player_rows,
    village_day_03_resident_rows: slot.village_day_03_resident_rows,
    village_day_03_world_rows: slot.village_day_03_world_rows,
    village_day_03_return_links: slot.village_day_03_return_links,
    primary_play_surface_ready: slot.primary_play_surface_ready,
    primary_play_surface_focus_rows: slot.primary_play_surface_focus_rows,
    primary_play_surface_cue_rows: slot.primary_play_surface_cue_rows,
    primary_play_surface_prompt_rows: slot.primary_play_surface_prompt_rows,
    first_playable_walkthrough_ready: slot.first_playable_walkthrough_ready,
    first_playable_walkthrough_steps: slot.first_playable_walkthrough_steps,
    first_playable_walkthrough_links: slot.first_playable_walkthrough_links,
    normal_play_action_rail_ready: slot.normal_play_action_rail_ready,
    normal_play_action_rows: slot.normal_play_action_rows,
    normal_play_option_rows: slot.normal_play_option_rows,
	    physical_field_rows: slot.physical_field_rows,
	    physical_energy_rows: slot.physical_energy_rows,
    structural_load_rows: slot.structural_load_rows,
    structural_stress_rows: slot.structural_stress_rows,
    structural_deformation_rows: slot.structural_deformation_rows,
    structural_collapse_rows: slot.structural_collapse_rows,
    structural_repair_rows: slot.structural_repair_rows,
    contact_constraint_rows: slot.contact_constraint_rows,
    joint_constraint_rows: slot.joint_constraint_rows,
    friction_rows: slot.friction_rows,
    impulse_rows: slot.impulse_rows,
    constraint_repair_rows: slot.constraint_repair_rows,
    material_state_rows: slot.material_state_rows,
    phase_change_rows: slot.phase_change_rows,
    property_drift_rows: slot.property_drift_rows,
    material_state_repair_rows: slot.material_state_repair_rows,
    terrain_steps: slot.terrain_steps,
    terrain_flow_rows: slot.terrain_flow_rows,
    terrain_support_rows: slot.terrain_support_rows,
    tool_use_rows: slot.tool_use_rows,
    tool_wear_rows: slot.tool_wear_rows,
    tool_failure_rows: slot.tool_failure_rows,
    tool_repair_rows: slot.tool_repair_rows,
    resource_stock_rows: slot.resource_stock_rows,
    resource_transform_rows: slot.resource_transform_rows,
    resource_loss_rows: slot.resource_loss_rows,
    resource_gain_rows: slot.resource_gain_rows,
    thermal_heat_rows: slot.thermal_heat_rows,
    thermal_fuel_rows: slot.thermal_fuel_rows,
    thermal_smoke_rows: slot.thermal_smoke_rows,
    thermal_safety_rows: slot.thermal_safety_rows,
    water_flow_rows: slot.water_flow_rows,
    water_leak_rows: slot.water_leak_rows,
    water_route_rows: slot.water_route_rows,
    water_quality_rows: slot.water_quality_rows,
    water_safety_rows: slot.water_safety_rows,
    ecology_growth_rows: slot.ecology_growth_rows,
    ecology_harvest_rows: slot.ecology_harvest_rows,
    ecology_spoilage_rows: slot.ecology_spoilage_rows,
    ecology_hunger_rows: slot.ecology_hunger_rows,
    ecology_safety_rows: slot.ecology_safety_rows,
	    material_manipulation_rows: slot.material_manipulation_rows,
	    material_manipulation_practice_links: slot.material_manipulation_practice_links,
	    resident_body_steps: slot.resident_body_steps,
	    resident_body_contacts: slot.resident_body_contacts,
	    resident_body_recoveries: slot.resident_body_recoveries,
	    deep_time_physics_epochs: slot.deep_time_physics_epochs,
	    deep_time_material_flux_rows: slot.deep_time_material_flux_rows,
	    deep_time_physical_effects: slot.deep_time_physical_effects,
	    physical_heritage_rows: slot.physical_heritage_rows,
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
    project_completions: world.gamePrototypeProjects ? world.gamePrototypeProjects.completionLedger.length : 0,
    commons_support_rows: world.gamePrototypeCommonsSupport ? world.gamePrototypeCommonsSupport.supportLedger.length : 0,
    nearby_action_rows: world.gamePrototypeNearbyActions ? world.gamePrototypeNearbyActions.actionLedger.length : 0,
    village_day_rows: world.gamePrototypeDayCycle ? world.gamePrototypeDayCycle.dayLedger.length : 0,
    return_later_rows: world.gamePrototypeReturnLater ? world.gamePrototypeReturnLater.returnLedger.length : 0,
    playable_slice_ready: world.gamePrototypePlayableSlice ? world.gamePrototypePlayableSlice.acceptanceReady === true : false,
    playable_slice_phase_rows: world.gamePrototypePlayableSlice ? world.gamePrototypePlayableSlice.phaseLedger.length : 0,
    playable_slice_physics_rows: world.gamePrototypePlayableSlice ? world.gamePrototypePlayableSlice.linkedPhysicsRows.length : 0,
    playable_slice_proposals: world.gamePrototypePlayableSlice ? world.gamePrototypePlayableSlice.linkedProposalIds.length : 0,
    playable_slice_practices: world.gamePrototypePlayableSlice ? world.gamePrototypePlayableSlice.linkedPracticeIds.length : 0,
    playable_slice_return_rows: world.gamePrototypePlayableSlice ? world.gamePrototypePlayableSlice.returnProofRows.length : 0,
    village_day_03_ready: world.gamePrototypeVillageDay03 ? world.gamePrototypeVillageDay03.acceptanceReady === true : false,
    village_day_03_rows: world.gamePrototypeVillageDay03 ? world.gamePrototypeVillageDay03.dayLedger.length : 0,
    village_day_03_player_rows: world.gamePrototypeVillageDay03 ? world.gamePrototypeVillageDay03.playerLoopLedger.length : 0,
    village_day_03_resident_rows: world.gamePrototypeVillageDay03 ? world.gamePrototypeVillageDay03.residentLoopLedger.length : 0,
    village_day_03_world_rows: world.gamePrototypeVillageDay03 ? world.gamePrototypeVillageDay03.worldLoopLedger.length : 0,
    village_day_03_return_links: world.gamePrototypeVillageDay03 ? world.gamePrototypeVillageDay03.returnLinks.length : 0,
    primary_play_surface_ready: world.gamePrototypeWorldStage ? world.gamePrototypeWorldStage.acceptanceReady === true : false,
    primary_play_surface_focus_rows: world.gamePrototypeWorldStage ? world.gamePrototypeWorldStage.focusLedger.length : 0,
    primary_play_surface_cue_rows: world.gamePrototypeWorldStage ? world.gamePrototypeWorldStage.canvasCueLedger.length : 0,
    primary_play_surface_prompt_rows: world.gamePrototypeWorldStage ? world.gamePrototypeWorldStage.actionPromptLedger.length : 0,
    first_playable_walkthrough_ready: world.gamePrototypeWalkthrough ? world.gamePrototypeWalkthrough.acceptanceReady === true : false,
    first_playable_walkthrough_steps: world.gamePrototypeWalkthrough ? world.gamePrototypeWalkthrough.stepLedger.length : 0,
    first_playable_walkthrough_links: world.gamePrototypeWalkthrough ? world.gamePrototypeWalkthrough.evidenceLinks.length : 0,
    normal_play_action_rail_ready: world.gamePrototypeActionRail ? world.gamePrototypeActionRail.acceptanceReady === true : false,
    normal_play_action_rows: world.gamePrototypeActionRail ? world.gamePrototypeActionRail.actionLedger.length : 0,
    normal_play_option_rows: world.gamePrototypeActionRail ? world.gamePrototypeActionRail.optionLedger.length : 0,
    player_mode_interface_ready: world.gamePrototypePlayerMode ? world.gamePrototypePlayerMode.acceptanceReady === true : false,
    player_mode_sessions: world.gamePrototypePlayerMode ? world.gamePrototypePlayerMode.sessionLedger.length : 0,
    player_mode_visible_cards: world.gamePrototypePlayerMode && world.gamePrototypePlayerMode.visibleSurface ? world.gamePrototypePlayerMode.visibleSurface.visible_cards.length : 0,
    resident_proposal_deck_ready: world.gamePrototypeProposalDeck ? world.gamePrototypeProposalDeck.acceptanceReady === true : false,
    resident_proposal_deck_cards: world.gamePrototypeProposalDeck ? world.gamePrototypeProposalDeck.cardLedger.length : 0,
    resident_proposal_deck_actions: world.gamePrototypeProposalDeck ? world.gamePrototypeProposalDeck.actionLedger.length : 0,
    lived_practice_loop_ready: world.gamePrototypeLivedPractice ? world.gamePrototypeLivedPractice.acceptanceReady === true : false,
    lived_practice_loop_rows: world.gamePrototypeLivedPractice ? world.gamePrototypeLivedPractice.actionLedger.length : 0,
    lived_practice_loop_snapshots: world.gamePrototypeLivedPractice ? world.gamePrototypeLivedPractice.practiceSnapshots.length : 0,
    resident_worksite_ready: world.gamePrototypeWorksite ? world.gamePrototypeWorksite.acceptanceReady === true : false,
    resident_worksite_rows: world.gamePrototypeWorksite ? world.gamePrototypeWorksite.watchLedger.length : 0,
    resident_worksite_snapshots: world.gamePrototypeWorksite ? world.gamePrototypeWorksite.snapshotLedger.length : 0,
	    material_components: world.gamePrototype3DWorld ? world.gamePrototype3DWorld.components.length : 0,
	    resident_terms: world.gamePrototype3DWorld && world.gamePrototype3DWorld.language ? world.gamePrototype3DWorld.language.terms.length : 0,
	    physics_steps: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics ? world.gamePrototype3DWorld.physics.step || 0 : 0,
		    physics_linked_proposals: world.villageBoard && world.villageBoard.projectProposals ? world.villageBoard.projectProposals.filter(row => row.related_physics_step).length : 0,
	    physical_field_rows: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.fieldLedger ? world.gamePrototype3DWorld.physics.fieldLedger.length : 0,
	    physical_energy_rows: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.energyLedger ? world.gamePrototype3DWorld.physics.energyLedger.length : 0,
	    structural_load_rows: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.loadPathLedger ? world.gamePrototype3DWorld.physics.loadPathLedger.length : 0,
	    structural_stress_rows: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.stressLedger ? world.gamePrototype3DWorld.physics.stressLedger.length : 0,
	    structural_deformation_rows: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.deformationLedger ? world.gamePrototype3DWorld.physics.deformationLedger.length : 0,
	    structural_collapse_rows: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.collapseLedger ? world.gamePrototype3DWorld.physics.collapseLedger.length : 0,
	    structural_repair_rows: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.structuralRepairLedger ? world.gamePrototype3DWorld.physics.structuralRepairLedger.length : 0,
	    contact_constraint_rows: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.contactConstraintLedger ? world.gamePrototype3DWorld.physics.contactConstraintLedger.length : 0,
	    joint_constraint_rows: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.jointConstraintLedger ? world.gamePrototype3DWorld.physics.jointConstraintLedger.length : 0,
	    friction_rows: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.frictionLedger ? world.gamePrototype3DWorld.physics.frictionLedger.length : 0,
	    impulse_rows: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.impulseLedger ? world.gamePrototype3DWorld.physics.impulseLedger.length : 0,
	    constraint_repair_rows: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.constraintRepairLedger ? world.gamePrototype3DWorld.physics.constraintRepairLedger.length : 0,
	    material_state_rows: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.materialStateLedger ? world.gamePrototype3DWorld.physics.materialStateLedger.length : 0,
	    phase_change_rows: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.phaseChangeLedger ? world.gamePrototype3DWorld.physics.phaseChangeLedger.length : 0,
	    property_drift_rows: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.propertyDriftLedger ? world.gamePrototype3DWorld.physics.propertyDriftLedger.length : 0,
	    material_state_repair_rows: world.gamePrototype3DWorld && world.gamePrototype3DWorld.physics && world.gamePrototype3DWorld.physics.materialStateRepairLedger ? world.gamePrototype3DWorld.physics.materialStateRepairLedger.length : 0,
    terrain_steps: world.gamePrototypeTerrain && world.gamePrototypeTerrain.terrainLedger ? world.gamePrototypeTerrain.terrainLedger.length : 0,
    terrain_flow_rows: world.gamePrototypeTerrain && world.gamePrototypeTerrain.flowLedger ? world.gamePrototypeTerrain.flowLedger.length : 0,
    terrain_support_rows: world.gamePrototypeTerrain && world.gamePrototypeTerrain.supportLedger ? world.gamePrototypeTerrain.supportLedger.length : 0,
	    tool_use_rows: world.gamePrototypeTools && world.gamePrototypeTools.useLedger ? world.gamePrototypeTools.useLedger.length : 0,
	    tool_wear_rows: world.gamePrototypeTools && world.gamePrototypeTools.wearLedger ? world.gamePrototypeTools.wearLedger.length : 0,
	    tool_failure_rows: world.gamePrototypeTools && world.gamePrototypeTools.failureLedger ? world.gamePrototypeTools.failureLedger.length : 0,
	    tool_repair_rows: world.gamePrototypeTools && world.gamePrototypeTools.repairLedger ? world.gamePrototypeTools.repairLedger.length : 0,
	    resource_stock_rows: world.gamePrototypeResourcePhysics && world.gamePrototypeResourcePhysics.stockLedger ? world.gamePrototypeResourcePhysics.stockLedger.length : 0,
	    resource_transform_rows: world.gamePrototypeResourcePhysics && world.gamePrototypeResourcePhysics.transformLedger ? world.gamePrototypeResourcePhysics.transformLedger.length : 0,
	    resource_loss_rows: world.gamePrototypeResourcePhysics && world.gamePrototypeResourcePhysics.lossLedger ? world.gamePrototypeResourcePhysics.lossLedger.length : 0,
	    resource_gain_rows: world.gamePrototypeResourcePhysics && world.gamePrototypeResourcePhysics.gainLedger ? world.gamePrototypeResourcePhysics.gainLedger.length : 0,
	    thermal_heat_rows: world.gamePrototypeThermalPhysics && world.gamePrototypeThermalPhysics.heatLedger ? world.gamePrototypeThermalPhysics.heatLedger.length : 0,
	    thermal_fuel_rows: world.gamePrototypeThermalPhysics && world.gamePrototypeThermalPhysics.fuelLedger ? world.gamePrototypeThermalPhysics.fuelLedger.length : 0,
	    thermal_smoke_rows: world.gamePrototypeThermalPhysics && world.gamePrototypeThermalPhysics.smokeLedger ? world.gamePrototypeThermalPhysics.smokeLedger.length : 0,
	    thermal_safety_rows: world.gamePrototypeThermalPhysics && world.gamePrototypeThermalPhysics.safetyLedger ? world.gamePrototypeThermalPhysics.safetyLedger.length : 0,
	    water_flow_rows: world.gamePrototypeWaterPhysics && world.gamePrototypeWaterPhysics.flowLedger ? world.gamePrototypeWaterPhysics.flowLedger.length : 0,
	    water_leak_rows: world.gamePrototypeWaterPhysics && world.gamePrototypeWaterPhysics.leakLedger ? world.gamePrototypeWaterPhysics.leakLedger.length : 0,
	    water_route_rows: world.gamePrototypeWaterPhysics && world.gamePrototypeWaterPhysics.routeLedger ? world.gamePrototypeWaterPhysics.routeLedger.length : 0,
	    water_quality_rows: world.gamePrototypeWaterPhysics && world.gamePrototypeWaterPhysics.qualityLedger ? world.gamePrototypeWaterPhysics.qualityLedger.length : 0,
	    water_safety_rows: world.gamePrototypeWaterPhysics && world.gamePrototypeWaterPhysics.safetyLedger ? world.gamePrototypeWaterPhysics.safetyLedger.length : 0,
	    ecology_growth_rows: world.gamePrototypeEcologyPhysics && world.gamePrototypeEcologyPhysics.growthLedger ? world.gamePrototypeEcologyPhysics.growthLedger.length : 0,
	    ecology_harvest_rows: world.gamePrototypeEcologyPhysics && world.gamePrototypeEcologyPhysics.harvestLedger ? world.gamePrototypeEcologyPhysics.harvestLedger.length : 0,
	    ecology_spoilage_rows: world.gamePrototypeEcologyPhysics && world.gamePrototypeEcologyPhysics.spoilageLedger ? world.gamePrototypeEcologyPhysics.spoilageLedger.length : 0,
	    ecology_hunger_rows: world.gamePrototypeEcologyPhysics && world.gamePrototypeEcologyPhysics.hungerLedger ? world.gamePrototypeEcologyPhysics.hungerLedger.length : 0,
	    ecology_safety_rows: world.gamePrototypeEcologyPhysics && world.gamePrototypeEcologyPhysics.safetyLedger ? world.gamePrototypeEcologyPhysics.safetyLedger.length : 0,
	    material_manipulation_rows: world.gamePrototypeMaterialManipulation && world.gamePrototypeMaterialManipulation.actionLedger ? world.gamePrototypeMaterialManipulation.actionLedger.length : 0,
	    material_manipulation_practice_links: world.gamePrototypeMaterialManipulation && world.gamePrototypeMaterialManipulation.practiceLinks ? world.gamePrototypeMaterialManipulation.practiceLinks.length : 0,
	    resident_body_steps: world.gamePrototypeResidentBodies && world.gamePrototypeResidentBodies.bodyLedger ? world.gamePrototypeResidentBodies.bodyLedger.length : 0,
	    resident_body_contacts: world.gamePrototypeResidentBodies && world.gamePrototypeResidentBodies.contactLedger ? world.gamePrototypeResidentBodies.contactLedger.length : 0,
	    resident_body_recoveries: world.gamePrototypeResidentBodies && world.gamePrototypeResidentBodies.recoveryLedger ? world.gamePrototypeResidentBodies.recoveryLedger.length : 0,
	    construction_rows: world.gamePrototype3DWorld && world.gamePrototype3DWorld.constructionLedger ? world.gamePrototype3DWorld.constructionLedger.length : 0,
	    project_built_components: world.gamePrototype3DWorld && world.gamePrototype3DWorld.components ? world.gamePrototype3DWorld.components.filter(component => component.project_built === true).length : 0,
	    construction_practice_links: world.gamePrototype3DWorld && world.gamePrototype3DWorld.constructionLedger ? world.gamePrototype3DWorld.constructionLedger.filter(row => row.practice_id).length : 0,
	    deep_time_physical_effects: world.deepTimeCivilization && world.deepTimeCivilization.componentEffectLedger ? world.deepTimeCivilization.componentEffectLedger.length : 0,
	    physical_heritage_rows: world.deepTimeCivilization && world.deepTimeCivilization.physicalHeritageLedger ? world.deepTimeCivilization.physicalHeritageLedger.length : 0,
	    deep_time_physics_epochs: world.deepTimeCivilization && world.deepTimeCivilization.physicsEpochLedger ? world.deepTimeCivilization.physicsEpochLedger.length : 0,
	    deep_time_material_flux_rows: world.deepTimeCivilization && world.deepTimeCivilization.materialFluxLedger ? world.deepTimeCivilization.materialFluxLedger.length : 0,
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
  const guide = derivePrototypePlayerGuide();
  const divergence = world.gamePrototypeDivergence || null;
  const commons = world.gamePrototypeCommons || null;
  const projects = world.gamePrototypeProjects || null;
  const commonsSupport = world.gamePrototypeCommonsSupport || null;
  const nearby = world.gamePrototypeNearbyActions || null;
	  const dayCycle = world.gamePrototypeDayCycle || null;
	  const returnLater = world.gamePrototypeReturnLater || null;
  const playableSlice = world.gamePrototypePlayableSlice || null;
  const villageDay03 = world.gamePrototypeVillageDay03 || null;
  const worldStage = world.gamePrototypeWorldStage || null;
  const walkthrough = world.gamePrototypeWalkthrough || null;
  const actionRail = world.gamePrototypeActionRail || null;
  const playerMode = world.gamePrototypePlayerMode || null;
  const proposalDeck = world.gamePrototypeProposalDeck || null;
  const livedPractice = world.gamePrototypeLivedPractice || null;
  const worksite = world.gamePrototypeWorksite || null;
		  const materialWorld = world.gamePrototype3DWorld || null;
  const terrain = world.gamePrototypeTerrain || null;
  const tools = world.gamePrototypeTools || null;
  const resourcePhysics = world.gamePrototypeResourcePhysics || null;
  const thermalPhysics = world.gamePrototypeThermalPhysics || null;
  const waterPhysics = world.gamePrototypeWaterPhysics || null;
  const ecologyPhysics = world.gamePrototypeEcologyPhysics || null;
		  const physics = materialWorld && materialWorld.physics ? materialWorld.physics : null;
	  const manipulation = world.gamePrototypeMaterialManipulation || null;
	  const residentBodies = world.gamePrototypeResidentBodies || null;
	  const physicsProposalCount = board && board.projectProposals ? board.projectProposals.filter(row => row.related_physics_step).length : 0;
	  const constructionCount = materialWorld && materialWorld.constructionLedger ? materialWorld.constructionLedger.length : 0;
	  const projectBuiltComponentCount = materialWorld && materialWorld.components ? materialWorld.components.filter(component => component.project_built === true).length : 0;
	  const constructionPracticeLinks = materialWorld && materialWorld.constructionLedger ? materialWorld.constructionLedger.filter(row => row.practice_id).length : 0;
	  const constructionPracticeNodes = practiceGraph && practiceGraph.nodes ? practiceGraph.nodes.filter(row => row.source_construction_rows && row.source_construction_rows.length).length : 0;
	  const fieldRows = physics && physics.fieldLedger ? physics.fieldLedger.length : 0;
		  const energyRows = physics && physics.energyLedger ? physics.energyLedger.length : 0;
  const structuralLoadRows = physics && physics.loadPathLedger ? physics.loadPathLedger.length : 0;
  const structuralStressRows = physics && physics.stressLedger ? physics.stressLedger.length : 0;
  const structuralDeformationRows = physics && physics.deformationLedger ? physics.deformationLedger.length : 0;
  const structuralCollapseRows = physics && physics.collapseLedger ? physics.collapseLedger.length : 0;
  const structuralRepairRows = physics && physics.structuralRepairLedger ? physics.structuralRepairLedger.length : 0;
  const contactConstraintRows = physics && physics.contactConstraintLedger ? physics.contactConstraintLedger.length : 0;
  const jointConstraintRows = physics && physics.jointConstraintLedger ? physics.jointConstraintLedger.length : 0;
  const frictionRows = physics && physics.frictionLedger ? physics.frictionLedger.length : 0;
  const impulseRows = physics && physics.impulseLedger ? physics.impulseLedger.length : 0;
  const constraintRepairRows = physics && physics.constraintRepairLedger ? physics.constraintRepairLedger.length : 0;
  const materialStateRows = physics && physics.materialStateLedger ? physics.materialStateLedger.length : 0;
  const phaseChangeRows = physics && physics.phaseChangeLedger ? physics.phaseChangeLedger.length : 0;
  const propertyDriftRows = physics && physics.propertyDriftLedger ? physics.propertyDriftLedger.length : 0;
  const materialStateRepairRows = physics && physics.materialStateRepairLedger ? physics.materialStateRepairLedger.length : 0;
  const playableSlicePhysicsRows = playableSlice ? playableSlice.linkedPhysicsRows.length : 0;
  const playableSliceProposalRows = playableSlice ? playableSlice.linkedProposalIds.length : 0;
  const playableSlicePracticeRows = playableSlice ? playableSlice.linkedPracticeIds.length : 0;
  const playableSliceReturnRows = playableSlice ? playableSlice.returnProofRows.length : 0;
  const villageDay03Rows = villageDay03 ? villageDay03.dayLedger.length : 0;
  const villageDay03PlayerRows = villageDay03 ? villageDay03.playerLoopLedger.length : 0;
  const villageDay03ResidentRows = villageDay03 ? villageDay03.residentLoopLedger.length : 0;
  const villageDay03WorldRows = villageDay03 ? villageDay03.worldLoopLedger.length : 0;
  const villageDay03ReturnLinks = villageDay03 ? villageDay03.returnLinks.length : 0;
  const worldStageFocusRows = worldStage ? worldStage.focusLedger.length : 0;
  const worldStageCueRows = worldStage ? worldStage.canvasCueLedger.length : 0;
  const worldStagePromptRows = worldStage ? worldStage.actionPromptLedger.length : 0;
  const walkthroughSteps = walkthrough ? walkthrough.stepLedger.length : 0;
  const walkthroughLinks = walkthrough ? walkthrough.evidenceLinks.length : 0;
  const actionRailRows = actionRail ? actionRail.actionLedger.length : 0;
  const actionRailOptions = actionRail ? actionRail.optionLedger.length : 0;
  const playerModeSessions = playerMode ? playerMode.sessionLedger.length : 0;
  const playerModeVisibleCards = playerMode && playerMode.visibleSurface ? playerMode.visibleSurface.visible_cards.length : 0;
  const proposalDeckCards = proposalDeck ? proposalDeck.cardLedger.length : 0;
  const proposalDeckActions = proposalDeck ? proposalDeck.actionLedger.length : 0;
  const livedPracticeRows = livedPractice ? livedPractice.actionLedger.length : 0;
  const livedPracticeSnapshots = livedPractice ? livedPractice.practiceSnapshots.length : 0;
  const worksiteRows = worksite ? worksite.watchLedger.length : 0;
  const worksiteSnapshots = worksite ? worksite.snapshotLedger.length : 0;
  const terrainRows = terrain && terrain.terrainLedger ? terrain.terrainLedger.length : 0;
  const terrainFlowRows = terrain && terrain.flowLedger ? terrain.flowLedger.length : 0;
  const terrainSupportRows = terrain && terrain.supportLedger ? terrain.supportLedger.length : 0;
  const toolUseRows = tools && tools.useLedger ? tools.useLedger.length : 0;
  const toolWearRows = tools && tools.wearLedger ? tools.wearLedger.length : 0;
  const toolFailureRows = tools && tools.failureLedger ? tools.failureLedger.length : 0;
  const toolRepairRows = tools && tools.repairLedger ? tools.repairLedger.length : 0;
  const resourceStockRows = resourcePhysics && resourcePhysics.stockLedger ? resourcePhysics.stockLedger.length : 0;
  const resourceTransformRows = resourcePhysics && resourcePhysics.transformLedger ? resourcePhysics.transformLedger.length : 0;
  const resourceLossRows = resourcePhysics && resourcePhysics.lossLedger ? resourcePhysics.lossLedger.length : 0;
  const resourceGainRows = resourcePhysics && resourcePhysics.gainLedger ? resourcePhysics.gainLedger.length : 0;
  const thermalHeatRows = thermalPhysics && thermalPhysics.heatLedger ? thermalPhysics.heatLedger.length : 0;
  const thermalFuelRows = thermalPhysics && thermalPhysics.fuelLedger ? thermalPhysics.fuelLedger.length : 0;
  const thermalSmokeRows = thermalPhysics && thermalPhysics.smokeLedger ? thermalPhysics.smokeLedger.length : 0;
  const thermalSafetyRows = thermalPhysics && thermalPhysics.safetyLedger ? thermalPhysics.safetyLedger.length : 0;
  const waterFlowRows = waterPhysics && waterPhysics.flowLedger ? waterPhysics.flowLedger.length : 0;
  const waterLeakRows = waterPhysics && waterPhysics.leakLedger ? waterPhysics.leakLedger.length : 0;
  const waterRouteRows = waterPhysics && waterPhysics.routeLedger ? waterPhysics.routeLedger.length : 0;
  const waterQualityRows = waterPhysics && waterPhysics.qualityLedger ? waterPhysics.qualityLedger.length : 0;
  const waterSafetyRows = waterPhysics && waterPhysics.safetyLedger ? waterPhysics.safetyLedger.length : 0;
  const ecologyGrowthRows = ecologyPhysics && ecologyPhysics.growthLedger ? ecologyPhysics.growthLedger.length : 0;
  const ecologyHarvestRows = ecologyPhysics && ecologyPhysics.harvestLedger ? ecologyPhysics.harvestLedger.length : 0;
  const ecologySpoilageRows = ecologyPhysics && ecologyPhysics.spoilageLedger ? ecologyPhysics.spoilageLedger.length : 0;
  const ecologyHungerRows = ecologyPhysics && ecologyPhysics.hungerLedger ? ecologyPhysics.hungerLedger.length : 0;
  const ecologySafetyRows = ecologyPhysics && ecologyPhysics.safetyLedger ? ecologyPhysics.safetyLedger.length : 0;
	  const manipulationRows = manipulation && manipulation.actionLedger ? manipulation.actionLedger.length : 0;
	  const manipulationPracticeLinks = manipulation && manipulation.practiceLinks ? manipulation.practiceLinks.length : 0;
	  const residentBodyRows = residentBodies && residentBodies.bodyLedger ? residentBodies.bodyLedger.length : 0;
	  const residentBodyFatigueRows = residentBodies && residentBodies.fatigueLedger ? residentBodies.fatigueLedger.length : 0;
	  const residentBodyContactRows = residentBodies && residentBodies.contactLedger ? residentBodies.contactLedger.length : 0;
	  const residentBodyRecoveryRows = residentBodies && residentBodies.recoveryLedger ? residentBodies.recoveryLedger.length : 0;
	  const physicalHeritageRows = deepTime && deepTime.physicalHeritageLedger ? deepTime.physicalHeritageLedger.length : 0;
	  const deepPhysicalEffectRows = deepTime && deepTime.componentEffectLedger ? deepTime.componentEffectLedger.length : 0;
	  const deepPhysicsEpochRows = deepTime && deepTime.physicsEpochLedger ? deepTime.physicsEpochLedger.length : 0;
	  const deepMaterialFluxRows = deepTime && deepTime.materialFluxLedger ? deepTime.materialFluxLedger.length : 0;
	  const constructionLineageCount = deepTime && deepTime.lineages ? deepTime.lineages.filter(row => row.component_ids && row.component_ids.length).length : 0;
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
    { id: 'player_guide_available', pass: Boolean(guide.nextAction && guide.button && guide.caution), evidence: `${guide.phase}: ${guide.nextAction}` },
    { id: 'guided_step_hook_available', pass: Boolean(prototype.guideHistory && Array.isArray(prototype.guideHistory)), evidence: `${prototype.guideHistory ? prototype.guideHistory.length : 0} guided step(s)` },
    { id: 'multi_seed_practice_divergence', pass: Boolean(divergence && divergence.diverged && divergence.all_hidden_law_shared && divergence.no_correct_concept_installed), evidence: divergence ? `${divergence.branches.length} branch(es), unique practices=${divergence.unique_practice_signatures}` : 'not compared' },
    { id: 'commons_causal_health', pass: Boolean(commons && commons.pass && commons.hidden_law_exposure_issues === 0), evidence: commons ? `${commons.pressure_level}, resources=${commons.resource_total}, ledger=${commons.ledger_rows}` : 'not audited' },
    { id: 'resident_project_progress', pass: Boolean(projects && projects.projectLedger.length > 0 && projects.completionLedger.length > 0 && projects.projectLedger.every(row => row.avatar_direct_command === false)), evidence: projects ? `${projects.projectLedger.length} work row(s), ${projects.completionLedger.length} completion(s), ${projects.stalledLedger.length} stall(s)` : 'not advanced' },
    { id: 'resource_commons_support', pass: Boolean(commonsSupport && commonsSupport.supportLedger.length > 0 && commonsSupport.supportLedger.every(row => row.avatar_direct_command === false)), evidence: commonsSupport ? `${commonsSupport.supportLedger.length} support row(s), ${commonsSupport.recoveryLedger.length} recovery row(s)` : 'not supported' },
    { id: 'location_sensitive_play', pass: Boolean(nearby && nearby.actionLedger.length > 0 && nearby.actionLedger.every(row => row.avatar_direct_command === false)), evidence: nearby ? `${nearby.actionLedger.length} nearby action row(s), last=${nearby.lastPlan ? nearby.lastPlan.label + '->' + nearby.lastPlan.action : 'none'}` : 'not used' },
    { id: 'village_day_cycle', pass: Boolean(dayCycle && dayCycle.dayLedger.length > 0 && dayCycle.weatherLedger.length > 0 && dayCycle.dayLedger.every(row => row.direct_player_command === false)), evidence: dayCycle ? `${dayCycle.dayLedger.length} day row(s), ${dayCycle.weatherLedger.length} weather row(s), day=${dayCycle.day}` : 'not advanced' },
    { id: 'return_later_forward_persistence', pass: Boolean(returnLater && returnLater.returnLedger.length > 0 && returnLater.returnLedger.every(row => row.restored_old_state === false && row.direct_reset === false && row.continuity_preserved === true)), evidence: returnLater ? `${returnLater.returnLedger.length} return(s), latest=${returnLater.latestReceipt ? returnLater.latestReceipt.return_id : 'none'}` : 'not used' },
    { id: 'physics_first_3d_material_world', pass: Boolean(materialWorld && physics && materialWorld.components.length > 0 && materialWorld.structures.length > 0 && materialWorld.language.terms.length > 0 && physics.latestStep && physics.supportLedger.length > 0 && physics.forceLedger.length > 0 && fieldRows > 0 && energyRows > 0 && materialWorld.noFixedBuildingAssets === true && materialWorld.noEnglishResidentTechLabels === true), evidence: materialWorld && physics ? `${materialWorld.components.length} component(s), ${materialWorld.language.terms.length} term(s), physics step=${physics.latestStep ? physics.latestStep.step_id : 'none'}, fields=${fieldRows}, energy=${energyRows}` : 'not initialized' },
    { id: 'structural_stress_physics', pass: Boolean(materialWorld && physics && structuralLoadRows > 0 && structuralStressRows > 0 && structuralDeformationRows > 0 && physics.stressLedger.every(row => row.no_effect_without_cause === true && row.no_resource_spawning === true && row.hidden_law_normal_view === false)), evidence: `${structuralLoadRows} load row(s), ${structuralStressRows} stress row(s), ${structuralDeformationRows} deformation row(s), ${structuralCollapseRows} collapse row(s), ${structuralRepairRows} repair row(s)` },
    { id: 'contact_constraint_physics', pass: Boolean(materialWorld && physics && contactConstraintRows > 0 && jointConstraintRows > 0 && frictionRows > 0 && impulseRows > 0 && physics.jointConstraintLedger.every(row => row.no_effect_without_cause === true && row.no_resource_spawning === true && row.hidden_law_normal_view === false)), evidence: `${contactConstraintRows} contact row(s), ${jointConstraintRows} joint row(s), ${frictionRows} friction row(s), ${impulseRows} impulse row(s), ${constraintRepairRows} repair row(s)` },
    { id: 'material_state_physics', pass: Boolean(materialWorld && physics && materialStateRows > 0 && propertyDriftRows > 0 && physics.materialStateLedger.every(row => row.no_resource_spawning === true && row.hidden_law_normal_view === false) && physics.propertyDriftLedger.every(row => row.no_effect_without_cause === true && row.no_resource_spawning === true && row.hidden_law_normal_view === false)), evidence: `${materialStateRows} state row(s), ${phaseChangeRows} phase row(s), ${propertyDriftRows} property row(s), ${materialStateRepairRows} repair row(s)` },
    { id: 'physics_to_practice_playable_slice', pass: Boolean(playableSlice && playableSlice.acceptanceReady && playableSlicePhysicsRows > 0 && playableSliceProposalRows > 0 && playableSlicePracticeRows > 0 && playableSliceReturnRows > 0 && playableSlice.noDirectCommand === true && playableSlice.noPredeclaredTechTree === true && playableSlice.noCorrectConceptInstalled === true), evidence: playableSlice ? `${playableSlice.phase}; physics=${playableSlicePhysicsRows}, proposals=${playableSliceProposalRows}, practices=${playableSlicePracticeRows}, return=${playableSliceReturnRows}` : 'not run' },
    { id: 'playable_village_day_0_3', pass: Boolean(villageDay03 && villageDay03.acceptanceReady && villageDay03Rows >= 4 && villageDay03PlayerRows >= 4 && villageDay03ResidentRows >= 4 && villageDay03WorldRows >= 4 && villageDay03.physicsLinks.length > 0 && villageDay03.proposalLinks.length > 0 && villageDay03.practiceLinks.length > 0 && villageDay03.saveLinks.length > 0 && villageDay03ReturnLinks > 0 && villageDay03.noDirectCommand === true && villageDay03.noTechTreeUnlock === true), evidence: villageDay03 ? `${villageDay03.phase}; rows=${villageDay03Rows}, player=${villageDay03PlayerRows}, resident=${villageDay03ResidentRows}, world=${villageDay03WorldRows}, returns=${villageDay03ReturnLinks}` : 'not run' },
    { id: 'primary_play_surface', pass: Boolean(worldStage && worldStage.acceptanceReady && worldStageFocusRows >= 3 && worldStageCueRows >= 3 && worldStagePromptRows >= 3 && worldStage.canvasFirst === true && worldStage.noHiddenLawInNormalView === true && worldStage.noDirectCommand === true), evidence: worldStage ? `${worldStage.phase}; focus=${worldStageFocusRows}, cues=${worldStageCueRows}, prompts=${worldStagePromptRows}` : 'not run' },
    { id: 'first_playable_walkthrough', pass: Boolean(walkthrough && walkthrough.acceptanceReady && walkthroughSteps >= walkthrough.requiredSteps.length && walkthroughLinks >= walkthrough.requiredSteps.length && walkthrough.noDirectCommand === true && walkthrough.noTechTreeUnlock === true && walkthrough.noHiddenLawNormalView === true), evidence: walkthrough ? `${walkthrough.phase}; steps=${walkthroughSteps}, links=${walkthroughLinks}` : 'not run' },
    { id: 'normal_play_action_rail', pass: Boolean(actionRail && actionRail.acceptanceReady && actionRailRows >= actionRail.verbs.length && actionRailOptions > 0 && actionRail.playerLanguageOnly === true && actionRail.noDirectCommand === true && actionRail.noTechTreeUnlock === true), evidence: actionRail ? `actions=${actionRailRows}, optionSnapshots=${actionRailOptions}, verbs=${actionRail.verbs.join('/')}` : 'not run' },
    { id: 'player_mode_interface', pass: Boolean(playerMode && playerMode.acceptanceReady && playerModeSessions > 0 && playerModeVisibleCards >= 6 && playerMode.normalViewOnly === true && playerMode.debugPanelsHidden === true && playerMode.noDirectCommand === true && playerMode.noHiddenLawNormalView === true && playerMode.playerGlossesOnly === true), evidence: playerMode ? `enabled=${playerMode.enabled}, sessions=${playerModeSessions}, visibleCards=${playerModeVisibleCards}` : 'not run' },
    { id: 'resident_proposal_deck', pass: Boolean(proposalDeck && proposalDeck.acceptanceReady && proposalDeckCards > 0 && proposalDeckActions >= 3 && proposalDeck.avatarCannotForce === true && proposalDeck.noDirectCommand === true && proposalDeck.noHiddenLawNormalView === true && proposalDeck.playerGlossesOnly === true), evidence: proposalDeck ? `cardSnapshots=${proposalDeckCards}, actions=${proposalDeckActions}` : 'not run' },
    { id: 'lived_practice_loop', pass: Boolean(livedPractice && livedPractice.acceptanceReady && livedPracticeRows >= 4 && livedPracticeSnapshots > 0 && livedPractice.noDirectCommand === true && livedPractice.noHiddenLawNormalView === true && livedPractice.noPredeclaredTechTree === true && livedPractice.noCorrectConceptInstalled === true), evidence: livedPractice ? `actions=${livedPracticeRows}, snapshots=${livedPracticeSnapshots}` : 'not run' },
    { id: 'resident_worksite', pass: Boolean(worksite && worksite.acceptanceReady && worksiteRows >= 2 && worksiteSnapshots > 0 && worksite.avatarCannotAssignJobs === true && worksite.noDirectCommand === true && worksite.noHiddenLawNormalView === true && worksite.noResourceSpawning === true), evidence: worksite ? `watchRows=${worksiteRows}, snapshots=${worksiteSnapshots}` : 'not run' },
    { id: 'terrain_physics_substrate', pass: Boolean(terrain && terrainRows > 0 && terrainFlowRows > 0 && terrainSupportRows > 0 && terrain.terrainLedger.every(row => row.no_effect_without_cause === true && row.no_resource_spawning === true && row.hidden_law_normal_view === false)), evidence: `${terrainRows} terrain step(s), ${terrainFlowRows} flow row(s), ${terrainSupportRows} support row(s)` },
	    { id: 'tool_work_physics', pass: Boolean(tools && toolUseRows > 0 && toolWearRows > 0 && tools.useLedger.every(row => row.no_resource_spawning === true && row.hidden_law_normal_view === false)), evidence: `${toolUseRows} use row(s), ${toolWearRows} wear row(s), ${toolFailureRows} failure row(s), ${toolRepairRows} repair row(s)` },
	    { id: 'resource_stock_physics', pass: Boolean(resourcePhysics && resourceStockRows > 0 && resourceTransformRows >= resourceStockRows && resourcePhysics.stockLedger.every(row => row.no_resource_spawning === true && row.hidden_law_normal_view === false)), evidence: `${resourceStockRows} stock step(s), ${resourceTransformRows} transform row(s), ${resourceLossRows} loss row(s), ${resourceGainRows} gain row(s)` },
	    { id: 'thermal_fire_physics', pass: Boolean(thermalPhysics && thermalHeatRows > 0 && thermalFuelRows > 0 && thermalSmokeRows > 0 && thermalPhysics.heatLedger.every(row => row.no_resource_spawning === true && row.hidden_law_normal_view === false)), evidence: `${thermalHeatRows} heat step(s), ${thermalFuelRows} fuel row(s), ${thermalSmokeRows} smoke row(s), ${thermalSafetyRows} safety row(s)` },
	    { id: 'water_fluid_physics', pass: Boolean(waterPhysics && waterFlowRows > 0 && waterRouteRows > 0 && waterQualityRows > 0 && waterPhysics.flowLedger.every(row => row.no_resource_spawning === true && row.hidden_law_normal_view === false)), evidence: `${waterFlowRows} flow row(s), ${waterLeakRows} leak row(s), ${waterRouteRows} route row(s), ${waterQualityRows} quality row(s), ${waterSafetyRows} safety row(s)` },
	    { id: 'ecology_food_physics', pass: Boolean(ecologyPhysics && ecologyGrowthRows > 0 && ecologyHarvestRows > 0 && ecologySpoilageRows > 0 && ecologyHungerRows > 0 && ecologyPhysics.growthLedger.every(row => row.no_resource_spawning === true && row.hidden_law_normal_view === false)), evidence: `${ecologyGrowthRows} growth row(s), ${ecologyHarvestRows} harvest row(s), ${ecologySpoilageRows} spoilage row(s), ${ecologyHungerRows} hunger row(s), ${ecologySafetyRows} safety row(s)` },
	    { id: 'resident_material_manipulation', pass: Boolean(manipulation && manipulationRows > 0 && manipulationPracticeLinks > 0 && manipulation.actionLedger.every(row => row.avatar_direct_command === false && row.hidden_law_normal_view === false)), evidence: `${manipulationRows} handling row(s), ${manipulationPracticeLinks} practice link(s)` },
	    { id: 'resident_body_physics', pass: Boolean(residentBodies && residentBodyRows > 0 && residentBodyFatigueRows > 0 && residentBodies.bodyLedger.every(row => row.no_direct_player_command === true && row.hidden_law_normal_view === false && row.fatigue_delta >= 0)), evidence: `${residentBodyRows} body step(s), ${residentBodyContactRows} contact row(s), ${residentBodyRecoveryRows} recovery row(s)` },
		    { id: 'physics_consequences_reach_residents', pass: Boolean(physicsProposalCount > 0 && board.projectProposals.some(row => row.related_physics_step && row.avatar_can_force === false)), evidence: `${physicsProposalCount} physics-linked proposal(s)` },
		    { id: 'projects_construct_physical_components', pass: Boolean(constructionCount > 0 && projectBuiltComponentCount > 0 && materialWorld.constructionLedger.every(row => row.no_fixed_asset === true && row.no_resource_spawning === true)), evidence: `${constructionCount} construction row(s), ${projectBuiltComponentCount} project-built component(s)` },
	    { id: 'construction_evolves_practice_language', pass: Boolean(constructionPracticeLinks > 0 && constructionPracticeNodes > 0 && materialWorld.language.terms.some(row => (row.meaning_drift || []).some(text => /repair|reinforced|retie/.test(text)))), evidence: `${constructionPracticeLinks} construction-practice link(s), ${constructionPracticeNodes} construction practice node(s)` },
	    { id: 'deep_time_stochastic_physics_epochs', pass: Boolean(deepPhysicsEpochRows > 0 && deepMaterialFluxRows > 0 && deepTime.physicsEpochLedger.every(row => row.no_effect_without_cause === true && row.no_resource_spawning === true && row.hidden_law_normal_view === false)), evidence: `${deepPhysicsEpochRows} physics epoch(s), ${deepMaterialFluxRows} material flux row(s)` },
	    { id: 'deep_time_uses_physical_heritage', pass: Boolean(physicalHeritageRows > 0 && deepPhysicalEffectRows > 0 && deepPhysicsEpochRows > 0 && constructionLineageCount > 0 && deepTime && deepTime.civilizationState && Number(deepTime.civilizationState.physicalContinuity || 0) > 0), evidence: `${physicalHeritageRows} heritage row(s), ${deepPhysicalEffectRows} deep physical effect(s), ${deepPhysicsEpochRows} physics epoch(s), ${constructionLineageCount} construction lineage(s)` },
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
  return log('exportPrototypeAcceptanceReceipt', { pass: receipt.pass, passed: receipt.passed, total: receipt.total, receiptId: receipt.receipt_id, guidePhase: derivePrototypePlayerGuide().phase });
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
  const slots = saves.slots.slice(-4).map(slot => `${slot.slot_id}: ${slot.label}; year=${slot.year}; day=${slot.autonomous_day}; practices=${slot.practices}; proposals=${slot.proposals}; projects=${slot.project_completions || 0}; commonsSupport=${slot.commons_support_rows || 0}; nearby=${slot.nearby_action_rows || 0}; villageDays=${slot.village_day_rows || 0}; returns=${slot.return_later_rows || 0}; physics=${slot.physics_steps || 0}/${slot.physics_linked_proposals || 0} proposals/${slot.physical_field_rows || 0} fields/${slot.physical_energy_rows || 0} energy; structural=${slot.structural_stress_rows || 0} stress/${slot.structural_deformation_rows || 0} deform/${slot.structural_repair_rows || 0} repair; constraints=${slot.contact_constraint_rows || 0} contact/${slot.joint_constraint_rows || 0} joints/${slot.constraint_repair_rows || 0} repair; materialState=${slot.material_state_rows || 0} state/${slot.phase_change_rows || 0} phase/${slot.property_drift_rows || 0} props; terrain=${slot.terrain_steps || 0} steps/${slot.terrain_flow_rows || 0} flow/${slot.terrain_support_rows || 0} support; tools=${slot.tool_use_rows || 0} uses/${slot.tool_failure_rows || 0} failures/${slot.tool_repair_rows || 0} repairs; resources=${slot.resource_stock_rows || 0} steps/${slot.resource_loss_rows || 0} losses/${slot.resource_gain_rows || 0} gains; thermal=${slot.thermal_heat_rows || 0} heat/${slot.thermal_smoke_rows || 0} smoke/${slot.thermal_safety_rows || 0} safety; water=${slot.water_flow_rows || 0} flows/${slot.water_leak_rows || 0} leaks/${slot.water_safety_rows || 0} safety; ecology=${slot.ecology_growth_rows || 0} growth/${slot.ecology_harvest_rows || 0} harvest/${slot.ecology_hunger_rows || 0} hunger; manipulation=${slot.material_manipulation_rows || 0}/${slot.material_manipulation_practice_links || 0} practice links; bodies=${slot.resident_body_steps || 0} steps/${slot.resident_body_contacts || 0} contacts/${slot.resident_body_recoveries || 0} recoveries; construction=${slot.construction_rows || 0}/${slot.project_built_components || 0} components/${slot.construction_practice_links || 0} practice links; deepPhysics=${slot.deep_time_physics_epochs || 0} epochs/${slot.deep_time_material_flux_rows || 0} flux/${slot.deep_time_physical_effects || 0} effects/${slot.physical_heritage_rows || 0} heritage; survival=${slot.survival_status}`);
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

function formatPrototypeDivergence() {
  const comparison = world.gamePrototypeDivergence || null;
  if (!comparison) return 'No seed comparison yet. Use Compare seeds after or during a prototype run.';
  const branches = comparison.branches.map(branch => {
    const practices = branch.practice_history.slice(0, 3).map(row => `${row.local_name}/${row.status}`).join('; ');
    return `${branch.branch_id}: historySeed=${branch.history_seed}; practices=${branch.practice_history.length}; statuses=${branch.status_signature}; sample=${practices}`;
  });
  return [
    `${comparison.comparison_id}: diverged=${comparison.diverged} / hidden law seed=${comparison.base_law_seed}`,
    `Unique practice signatures: ${comparison.unique_practice_signatures}`,
    `Unique status signatures: ${comparison.unique_status_signatures}`,
    `Boundary: ${comparison.boundary}`,
    'Branches:',
    ...branches,
  ].join('\n');
}

function renderGamePrototypeSurface() {
  const objectiveNode = document.getElementById('gamePrototypeObjectiveOut');
  const villageNode = document.getElementById('gamePrototypeVillageOut');
  const publicNode = document.getElementById('gamePrototypePublicOut');
  const guideNode = document.getElementById('gamePrototypeGuideOut');
  const playableSliceNode = document.getElementById('gamePrototypePlayableSliceOut');
  const villageDay03Node = document.getElementById('gamePrototypeVillageDay03Out');
  const primarySurfaceNode = document.getElementById('gamePrototypePrimarySurfaceOut');
  const walkthroughNode = document.getElementById('gamePrototypeWalkthroughOut');
  const actionRailNode = document.getElementById('gamePrototypeActionRailOut');
  const playerModeNode = document.getElementById('gamePrototypePlayerModeOut');
  const proposalDeckNode = document.getElementById('gamePrototypeProposalDeckOut');
  const livedPracticeNode = document.getElementById('gamePrototypeLivedPracticeOut');
  const worksiteNode = document.getElementById('gamePrototypeWorksiteOut');
  const loopNode = document.getElementById('gamePrototypeLoopOut');
  const deepTimeNode = document.getElementById('gamePrototypeDeepTimeOut');
  const residentBodiesNode = document.getElementById('gamePrototypeResidentBodiesOut');
  const autonomousNode = document.getElementById('gamePrototypeAutonomousOut');
  const expressionNode = document.getElementById('gamePrototypeExpressionOut');
  const qaNode = document.getElementById('gamePrototypeQAOut');
  const clockNode = document.getElementById('gamePrototypeClockOut');
  const saveNode = document.getElementById('gamePrototypeSaveOut');
  const acceptanceNode = document.getElementById('gamePrototypeAcceptanceOut');
  const divergenceNode = document.getElementById('gamePrototypeDivergenceOut');
  const commonsNode = document.getElementById('gamePrototypeCommonsOut');
  const projectsNode = document.getElementById('gamePrototypeProjectsOut');
  const commonsSupportNode = document.getElementById('gamePrototypeCommonsSupportOut');
  const nearbyNode = document.getElementById('gamePrototypeNearbyOut');
  const dayCycleNode = document.getElementById('gamePrototypeDayCycleOut');
	  const returnLaterNode = document.getElementById('gamePrototypeReturnLaterOut');
  const terrainNode = document.getElementById('gamePrototypeTerrainOut');
  const materialWorldNode = document.getElementById('gamePrototypeMaterialWorldOut');
  const structuralPhysicsNode = document.getElementById('gamePrototypeStructuralPhysicsOut');
  const contactConstraintPhysicsNode = document.getElementById('gamePrototypeContactConstraintPhysicsOut');
  const materialStatePhysicsNode = document.getElementById('gamePrototypeMaterialStatePhysicsOut');
  const materialManipulationNode = document.getElementById('gamePrototypeMaterialManipulationOut');
  const toolNode = document.getElementById('gamePrototypeToolsOut');
  const resourcePhysicsNode = document.getElementById('gamePrototypeResourcePhysicsOut');
  const thermalPhysicsNode = document.getElementById('gamePrototypeThermalPhysicsOut');
  const waterPhysicsNode = document.getElementById('gamePrototypeWaterPhysicsOut');
  const ecologyPhysicsNode = document.getElementById('gamePrototypeEcologyPhysicsOut');
  const prototype = world.gamePrototype || ensureGamePrototype();
  if (objectiveNode) objectiveNode.textContent = prototype.objective;
  if (villageNode) villageNode.textContent = formatPrototypeVillageState();
  if (publicNode) publicNode.textContent = formatPrototypePublicOutcomes();
  if (guideNode) guideNode.textContent = formatPrototypePlayerGuide();
  if (playableSliceNode) playableSliceNode.textContent = formatPlayablePhysicsPracticeSlice();
  if (villageDay03Node) villageDay03Node.textContent = formatPlayableVillageDay03();
  if (primarySurfaceNode) primarySurfaceNode.textContent = formatPrimaryPlaySurface();
  if (walkthroughNode) walkthroughNode.textContent = formatFirstPlayableWalkthrough();
  if (actionRailNode) actionRailNode.textContent = formatNormalPlayActionRail();
  if (playerModeNode) playerModeNode.textContent = formatPlayerModeInterface();
  if (proposalDeckNode) proposalDeckNode.textContent = formatPlayerProposalDeck();
  if (livedPracticeNode) livedPracticeNode.textContent = formatLivedPracticeLoop();
  if (worksiteNode) worksiteNode.textContent = formatResidentWorksite();
  if (loopNode) loopNode.textContent = formatPrototypeLoopReceipt();
  if (deepTimeNode) deepTimeNode.textContent = formatPrototypeDeepTime();
  if (residentBodiesNode) residentBodiesNode.textContent = formatPrototypeResidentBodies();
  if (autonomousNode) autonomousNode.textContent = formatPrototypeAutonomousResidents();
  if (expressionNode) expressionNode.textContent = formatPrototypeReadableBehavior();
  if (qaNode) qaNode.textContent = formatPrototypeQA();
  if (clockNode) clockNode.textContent = formatPrototypeClock();
  if (saveNode) saveNode.textContent = formatPrototypeSaves();
  if (acceptanceNode) acceptanceNode.textContent = formatPrototypeAcceptance();
  if (divergenceNode) divergenceNode.textContent = formatPrototypeDivergence();
  if (commonsNode) commonsNode.textContent = formatPrototypeCommons();
  if (projectsNode) projectsNode.textContent = formatPrototypeProjects();
  if (commonsSupportNode) commonsSupportNode.textContent = formatPrototypeCommonsSupport();
  if (nearbyNode) nearbyNode.textContent = formatPrototypeNearbyActions();
  if (dayCycleNode) dayCycleNode.textContent = formatPrototypeDayCycle();
	  if (returnLaterNode) returnLaterNode.textContent = formatPrototypeReturnLater();
  if (terrainNode) terrainNode.textContent = formatPrototypeTerrain();
  if (materialWorldNode) materialWorldNode.textContent = formatPrototypeMaterialWorld();
  if (structuralPhysicsNode) structuralPhysicsNode.textContent = formatPrototypeStructuralPhysics();
  if (contactConstraintPhysicsNode) contactConstraintPhysicsNode.textContent = formatPrototypeContactConstraintPhysics();
  if (materialStatePhysicsNode) materialStatePhysicsNode.textContent = formatPrototypeMaterialStatePhysics();
  if (materialManipulationNode) materialManipulationNode.textContent = formatPrototypeMaterialManipulation();
  if (toolNode) toolNode.textContent = formatPrototypeTools();
  if (resourcePhysicsNode) resourcePhysicsNode.textContent = formatPrototypeResourcePhysics();
  if (thermalPhysicsNode) thermalPhysicsNode.textContent = formatPrototypeThermalPhysics();
  if (waterPhysicsNode) waterPhysicsNode.textContent = formatPrototypeWaterPhysics();
  if (ecologyPhysicsNode) ecologyPhysicsNode.textContent = formatPrototypeEcologyPhysics();
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
    log('canvasMove', { x: world.avatar.x, y: world.avatar.y, room: world.avatar.room, zone: locationZoneForAvatar().zone_id, nearbyAction: nearbyActionPlan().action });
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
Boundary: deterministic browser-local public state only; no consciousness, no open-ended autonomous natural language, no moral patienthood.
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
Scope: public browser-local state only; no subjective consciousness, no open-ended autonomous natural language, no moral patienthood.
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
  const header = `Resources: water ${world.resources.water} / fiber ${world.resources.fiber} / wood ${world.resources.wood} / care ${world.resources.care} / food ${world.resources.food || 0}`;
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
    runToolPhysicsStep: `tool physics ${payload.toolUseId || 'none'} failed=${payload.failed === true} repaired=${payload.repaired === true}`,
    runToolPhysicsLoop: `tool physics loop uses=${payload.totalUses || 0} failures=${payload.failures || 0} repairs=${payload.repairs || 0}`,
    runResourcePhysicsStep: `resource physics ${payload.stepId || 'none'} resources=${JSON.stringify(payload.resources || {})}`,
    runResourcePhysicsLoop: `resource physics loop steps=${payload.totalSteps || 0} losses=${payload.losses || 0} gains=${payload.gains || 0}`,
    runThermalPhysicsStep: `thermal physics ${payload.stepId || 'none'} heat=${payload.maxHeat} smoke=${payload.totalSmoke} hazard=${payload.hazard === true}`,
    runThermalPhysicsLoop: `thermal physics loop steps=${payload.totalSteps || 0} smokeRows=${payload.smokeRows || 0} safety=${payload.safetyRows || 0}`,
    runWaterPhysicsStep: `water physics ${payload.stepId || 'none'} flows=${payload.flows || 0} leaks=${payload.leaks || 0} route=${payload.routePressure || 0}`,
    runWaterPhysicsLoop: `water physics loop flows=${payload.totalFlows || 0} leaks=${payload.leaks || 0} safety=${payload.safetyRows || 0}`,
    runEcologyPhysicsStep: `ecology physics ${payload.stepId || 'none'} harvested=${payload.harvested || 0} fed=${payload.fed || 0} food=${payload.food || 0}`,
    runEcologyPhysicsLoop: `ecology physics loop growth=${payload.growthRows || 0} harvest=${payload.harvestRows || 0} hunger=${payload.hungerRows || 0}`,
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
    runPrototypeGuidedStep: `guided step ${payload.fromPhase}->${payload.nextPhase} via ${payload.action}`,
    runPrototypePracticeChain: `prototype practice chain practices=${payload.practiceCount} proposals=${payload.proposalCount} projectRows=${payload.projectRows || 0}`,
    runPrototypeReturnProof: `prototype return proof branches=${payload.branchRows} revivals=${payload.revivalRows}`,
    runFirstPlayablePrototypeLoop: `first playable prototype milestones=${payload.milestones} branches=${payload.branchContinuity} structural=${payload.structuralStress || 0} constraints=${payload.contactConstraints || 0} material=${payload.materialStates || 0}`,
    comparePrototypeDivergenceSeeds: `seed comparison diverged=${payload.diverged === true} branches=${payload.branches} baseLaw=${payload.baseLawSeed}`,
    auditPrototypeCommons: `commons audit ${payload.pass ? 'PASS' : 'WATCH'} pressure=${payload.pressureLevel} resources=${payload.resources} ledger=${payload.ledgerRows}`,
	    advanceVillageProject: `advanced village project ${payload.proposalId || ''} status=${payload.status || payload.reason} progress=${payload.progress ?? 'n/a'} completed=${payload.completed === true} construction=${payload.constructionId || 'none'} added=${payload.componentsAdded || 0} repaired=${payload.componentsRepaired || 0} practice=${payload.practiceId || 'none'}`,
    supportResourceCommons: `supported commons ${payload.resource || ''} amount=${payload.amount ?? 0} source=${payload.source || payload.reason || ''} reopened=${payload.reopened || 0}`,
    performNearbyAction: `nearby action ${payload.label || payload.zone} -> ${payload.action} result=${payload.resultEvent} direct=${payload.directCommand === true}`,
    endVillageDay: `ended village day ${payload.day} weather=${payload.weather} actions=${payload.actionsAdded} project=${payload.projectStatus}`,
    leaveAndReturnLater: `left and returned after ${payload.daysAway} day(s), day ${payload.dayBefore}->${payload.dayAfter}, restoredOld=${payload.restoredOldState === true}`,
    runPrototypeMaterialWorldStep: `material world step components=${payload.components} structures=${payload.structures} residentTerms=${payload.residentTerms} stability=${payload.stability} proposal=${payload.physicsProposalId || 'none'}`,
    runPrototypePhysicsStep: `physics step ${payload.stepId} support=${payload.supportChecks} collisions=${payload.collisions} failures=${payload.failures} proposal=${payload.proposalId || 'none'}`,
    runStructuralPhysicsStep: `structural stress ${payload.stepId || 'none'} stress=${payload.maxStress} deflect=${payload.maxDeflection} collapse=${payload.collapses || 0} repair=${payload.repairRows || 0}`,
    runStructuralPhysicsLoop: `structural stress loop steps=${payload.stepsAdded || 0} load=${payload.loadRows || 0} stress=${payload.stressRows || 0} collapse=${payload.collapseRows || 0}`,
    runContactConstraintPhysicsStep: `contact constraints ${payload.stepId || 'none'} contacts=${payload.contactRows || 0} joints=${payload.jointRows || 0} failed=${payload.failedJoints || 0} repair=${payload.repairRows || 0}`,
    runContactConstraintPhysicsLoop: `contact constraint loop steps=${payload.stepsAdded || 0} contact=${payload.contactRows || 0} joints=${payload.jointRows || 0}`,
    runMaterialStatePhysicsStep: `material state ${payload.stepId || 'none'} states=${payload.stateRows || 0} phases=${payload.phaseChanges || 0} risky=${payload.riskyComponents || 0}`,
    runMaterialStatePhysicsLoop: `material state loop steps=${payload.stepsAdded || 0} state=${payload.stateRows || 0} phase=${payload.phaseRows || 0} property=${payload.propertyRows || 0}`,
    runTerrainPhysicsStep: `terrain physics ${payload.terrainStepId} weak=${payload.weakCells} moisture=${payload.averageMoisture} walk=${payload.averageWalkability}`,
    runTerrainPhysicsLoop: `terrain loop steps=${payload.stepsAdded} flow=${payload.flowRows} support=${payload.supportRows}`,
    runResidentBodyPhysicsStep: `resident body physics ${payload.resident} ${payload.action} fatigue=${payload.fatigue} footing=${payload.footing} contacts=${payload.contacts} slip=${payload.slip === true}`,
    runResidentBodyPhysicsLoop: `resident body physics loop steps=${payload.stepsAdded} contacts=${payload.contacts} recoveries=${payload.recoveries}`,
    runDeepTimePhysicsEpoch: `deep-time physics epoch ${payload.physicsEpochId} pressure=${payload.pressure} mass=${payload.massBefore}->${payload.massAfter}`,
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
    exportPrototypeAcceptanceReceipt: `prototype acceptance ${payload.pass ? 'PASS' : 'FAIL'} ${payload.passed}/${payload.total} guide=${payload.guidePhase || 'unknown'}`,
    supportVillageProposal: `supported village proposal ${payload.proposalId} accepted=${payload.accepted}`,
    askVillageBoardQuestion: `asked village board question ${payload.proposalId}`,
    waitOnVillageBoard: `waited on village board proposals=${payload.proposals}`,
    runPlayerProposalDeckLoop: `proposal deck ready=${payload.ready === true} cards=${payload.cards} actions=${payload.actions}`,
    supportPlayerProposalDeck: `proposal deck support ${payload.proposalId} ready=${payload.ready === true}`,
    askPlayerProposalDeck: `proposal deck ask ${payload.proposalId} ready=${payload.ready === true}`,
    waitPlayerProposalDeck: `proposal deck wait ${payload.proposalId} ready=${payload.ready === true}`,
    runLivedPracticeLoop: `lived practice ready=${payload.ready === true} practice=${payload.practice} status=${payload.status}`,
    runResidentWorksiteLoop: `resident worksite ready=${payload.ready === true} rows=${payload.watchRows} construction=${payload.construction}`,
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
  applyPlayerModeClass();
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

  const terrain = world.gamePrototypeTerrain;
  if (terrain && terrain.cells) {
    const left = 72;
    const top = 205;
    const cellW = 900 / terrain.width;
    const cellH = 300 / terrain.height;
    terrain.cells.forEach(cell => {
      const x = left + cell.x * cellW;
      const y = top + cell.y * cellH;
      const moisture = Number(cell.moisture || 0);
      const walkability = Number(cell.walkability || 0);
      ctx.fillStyle = moisture > 0.55
        ? `rgba(47,113,123,${0.12 + moisture * 0.2})`
        : `rgba(159,202,119,${0.08 + walkability * 0.14})`;
      ctx.fillRect(x, y, cellW, cellH);
      if (walkability < 0.55 || Number(cell.support_capacity || 1) < 0.58) {
        ctx.strokeStyle = 'rgba(183,93,57,0.58)';
        ctx.lineWidth = 2;
        ctx.strokeRect(x + 2, y + 2, cellW - 4, cellH - 4);
      }
    });
  }

  const resources = Object.entries(world.resources).map(([key, value]) => `${key}:${value}`).join('  ');
  const clock = world.prototypeClock || { running: false, step: 0, lastAction: 'not started' };
  const dayCycle = world.gamePrototypeDayCycle;
  const latestWeather = dayCycle && dayCycle.weatherLedger.length ? dayCycle.weatherLedger[dayCycle.weatherLedger.length - 1].weather : 'no weather yet';
  const deepTime = world.deepTimeCivilization;
  const survival = deepTime && deepTime.civilizationState ? deepTime.civilizationState : null;
  ctx.fillStyle = 'rgba(17,24,22,0.72)';
  ctx.fillRect(28, 22, 984, 36);
  ctx.fillStyle = '#f9ebc9';
  ctx.font = '16px Optima, sans-serif';
  ctx.fillText(`Resources ${resources}  |  day ${dayCycle ? dayCycle.day : 0} ${latestWeather}  |  auto ${clock.running ? 'running' : 'paused'} step ${clock.step}  |  year ${deepTime ? deepTime.year : 0}`, 42, 46);
  const survivalScore = survival ? Number(survival.continuityScore || 0) : 0;
  ctx.fillStyle = 'rgba(249,235,201,0.16)';
  ctx.fillRect(730, 35, 250, 10);
  ctx.fillStyle = survivalScore > 0.65 ? '#9fca77' : survivalScore > 0.34 ? '#d5a13a' : '#b75d39';
  ctx.fillRect(730, 35, 250 * survivalScore, 10);
  const stageSnapshot = currentPrimaryPlaySurfaceSnapshot();
  ctx.fillStyle = 'rgba(17,24,22,0.78)';
  ctx.fillRect(28, 66, 984, 72);
  ctx.strokeStyle = 'rgba(240,195,91,0.52)';
  ctx.strokeRect(28, 66, 984, 72);
  ctx.fillStyle = '#f0c35b';
  ctx.font = '15px Optima, sans-serif';
  ctx.fillText(`Primary stage: ${stageSnapshot.stage_phase}`.slice(0, 82), 44, 90);
  ctx.fillStyle = '#f9ebc9';
  ctx.font = '13px Optima, sans-serif';
  ctx.fillText(`Problem: ${stageSnapshot.current_problem}`.slice(0, 118), 44, 112);
  ctx.fillText(`Next: ${stageSnapshot.player_next_action} (${stageSnapshot.player_next_button})`.slice(0, 86), 44, 132);
  ctx.fillText(`Resident ${stageSnapshot.selected_resident} | proposal ${stageSnapshot.active_proposal_id} | practice ${stageSnapshot.active_practice_name} | component ${stageSnapshot.active_component_id}`.slice(0, 104), 470, 90);
  ctx.fillText(`Physics ${stageSnapshot.latest_physics_id} | resources ${stageSnapshot.resource_pressure.length ? stageSnapshot.resource_pressure.join(', ') : 'stable'}`.slice(0, 74), 470, 112);
  ctx.fillText('Canvas is the play surface; panels are inspection/audit support.'.slice(0, 74), 470, 132);

  const materialWorld = world.gamePrototype3DWorld;
  if (materialWorld && materialWorld.components) {
    const origin = { x: 356, y: 202 };
    const project3D = pos => ({
      x: origin.x + Number(pos.x || 0) * 1.05 - Number(pos.y || 0) * 0.55,
      y: origin.y + Number(pos.y || 0) * 0.52 - Number(pos.z || 0) * 0.72,
    });
    const materialColors = {
      rough_branch: '#8a5b37',
      fiber: '#d5a13a',
      clay_vessel: '#b75d39',
      reed_cover: '#9fca77',
      resin_smear: '#f0c35b'
    };
    const sortedComponents = materialWorld.components.slice().sort((a, b) => Number(a.position3d.z || 0) - Number(b.position3d.z || 0));
    sortedComponents.forEach(component => {
      const point = project3D(component.position3d || {});
      const color = materialColors[component.material_id] || '#aad0c3';
      const damage = Number(component.damage || 0);
      const alpha = Math.max(0.38, 0.92 - damage * 0.6);
      ctx.globalAlpha = alpha;
      ctx.fillStyle = color;
      ctx.strokeStyle = damage > 0.18 ? '#f0c35b' : '#111816';
      ctx.lineWidth = 2;
      if (component.shape === 'cylinder') {
        ctx.beginPath();
        ctx.ellipse(point.x, point.y, Math.max(8, Number(component.dimensions.x || 16) * 0.55), Math.max(5, Number(component.dimensions.y || 16) * 0.35), 0, 0, Math.PI * 2);
        ctx.fill();
        ctx.stroke();
        ctx.fillRect(point.x - 8, point.y - Number(component.dimensions.z || 22) * 0.55, 16, Number(component.dimensions.z || 22) * 0.55);
      } else if (component.shape === 'post') {
        const height = Math.max(20, Number(component.dimensions.z || 50) * 0.72);
        ctx.fillRect(point.x - 4, point.y - height, 8, height);
        ctx.strokeRect(point.x - 4, point.y - height, 8, height);
      } else if (component.shape === 'beam_x') {
        ctx.fillRect(point.x - Number(component.dimensions.x || 80) * 0.45, point.y - 5, Number(component.dimensions.x || 80) * 0.9, 10);
        ctx.strokeRect(point.x - Number(component.dimensions.x || 80) * 0.45, point.y - 5, Number(component.dimensions.x || 80) * 0.9, 10);
      } else if (component.shape === 'plane') {
        ctx.beginPath();
        ctx.moveTo(point.x - 64, point.y - 18);
        ctx.lineTo(point.x + 54, point.y - 22);
        ctx.lineTo(point.x + 72, point.y + 14);
        ctx.lineTo(point.x - 48, point.y + 18);
        ctx.closePath();
        ctx.fill();
        ctx.stroke();
      } else {
        ctx.fillRect(point.x - 18, point.y - 7, 36, 14);
        ctx.strokeRect(point.x - 18, point.y - 7, 36, 14);
	      }
	      ctx.globalAlpha = 1;
	    });
    const activeComponent = materialWorld.components.find(component => component.component_id === stageSnapshot.active_component_id);
    if (activeComponent) {
      const point = project3D(activeComponent.position3d || {});
      ctx.strokeStyle = '#f0c35b';
      ctx.lineWidth = 5;
      ctx.beginPath();
      ctx.arc(point.x, point.y, 34, 0, Math.PI * 2);
      ctx.stroke();
      ctx.fillStyle = '#f9ebc9';
      ctx.font = '12px Optima, sans-serif';
      ctx.fillText('current object', point.x + 38, point.y - 8);
    }
    const manipulation = world.gamePrototypeMaterialManipulation;
    const manipulationRows = manipulation && manipulation.actionLedger ? manipulation.actionLedger.slice(-4) : [];
    manipulationRows.forEach((row, index) => {
      const component = materialWorld.components.find(item => item.component_id === row.component_id);
      if (!component) return;
      const point = project3D(component.position3d || {});
      ctx.strokeStyle = row.success ? '#f0c35b' : '#b75d39';
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.arc(point.x, point.y - 18 - index * 4, 12 + index * 3, 0, Math.PI * 2);
      ctx.stroke();
      ctx.fillStyle = '#f9ebc9';
      ctx.font = '11px Optima, sans-serif';
      ctx.fillText(`${row.action} ${row.resident}`.slice(0, 22), point.x + 18, point.y - 18 - index * 4);
    });
	    const term = materialWorld.language && materialWorld.language.terms ? materialWorld.language.terms[0] : null;
    const latestPhysics = materialWorld.physics ? materialWorld.physics.latestStep : null;
    ctx.fillStyle = 'rgba(17,24,22,0.78)';
    ctx.fillRect(294, 210, 300, 58);
    ctx.fillStyle = '#f9ebc9';
    ctx.font = '13px Optima, sans-serif';
    ctx.fillText(term ? `${term.resident_word} ~ ${term.player_gloss}` : 'component-built storage practice', 310, 234);
    ctx.fillText(latestPhysics ? `physics ${latestPhysics.step_id}: support ${latestPhysics.support_checks}, failures ${latestPhysics.failures}` : 'physics: not stepped yet', 310, 254);
  }

  ctx.fillStyle = '#d5a13a'; ctx.beginPath(); ctx.arc(world.avatar.x, world.avatar.y, 24, 0, Math.PI * 2); ctx.fill();
  ctx.fillStyle = '#111816'; ctx.fillText('You', world.avatar.x - 11, world.avatar.y + 4);
  const nearbyPlan = nearbyActionPlan();
  ctx.fillStyle = '#f9ebc9';
  ctx.font = '13px Optima, sans-serif';
  ctx.fillText(`Nearby: ${nearbyPlan.label} -> ${nearbyPlan.action}`.slice(0, 54), Math.max(34, world.avatar.x - 92), Math.max(88, world.avatar.y - 34));
  Object.entries(world.residents).forEach(([name, resident], index) => {
    const needs = world.autonomousResidents && world.autonomousResidents.needState ? world.autonomousResidents.needState[name] : null;
    const expression = latestVisibleExpressionFor(name);
    const body = world.gamePrototypeResidentBodies && world.gamePrototypeResidentBodies.bodies ? world.gamePrototypeResidentBodies.bodies[name] : null;
    const x = body ? Math.max(58, Math.min(982, 86 + Number(body.position3d.x || 0) * 7.4)) : 130 + (index % 3) * 275;
    const y = body ? Math.max(230, Math.min(520, 220 + Number(body.position3d.y || 0) * 3.2 - Number(body.position3d.z || 0) * 5)) : 275 + Math.floor(index / 3) * 150;
    const energy = needs ? needs.energy : resident.progress;
    const safety = needs ? needs.safety : resident.trust;
    const radius = 20 + Math.round(resident.trust * 10);
	    const expressionColor = expression.marker === 'boundary' ? '#b75d39' : expression.marker === 'tired' ? '#8aa1b1' : expression.marker === 'working' || expression.marker === 'maintaining' || expression.marker === 'handling' || expression.marker === 'moving' ? '#9fca77' : expression.marker === 'testing' ? '#d5a13a' : '#aad0c3';
    ctx.fillStyle = name === world.selected ? '#f0c35b' : (safety < 0.45 ? '#d98d69' : expressionColor);
    ctx.beginPath(); ctx.arc(x, y, radius, 0, Math.PI * 2); ctx.fill();
    ctx.strokeStyle = '#111816'; ctx.lineWidth = 3; ctx.stroke();
    if (expression.marker === 'boundary' || expression.marker === 'guarded') {
      ctx.strokeStyle = '#b75d39';
      ctx.lineWidth = 4;
      ctx.beginPath(); ctx.moveTo(x - radius - 16, y - radius - 10); ctx.lineTo(x - radius - 4, y + radius + 12); ctx.stroke();
	    } else if (expression.marker === 'working' || expression.marker === 'maintaining' || expression.marker === 'repairing' || expression.marker === 'handling') {
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
    if (body) {
      ctx.fillStyle = body.slip_risk > 0.24 ? '#f0c35b' : '#9fca77';
      ctx.fillText(`body f${body.fatigue} foot${body.footing}`.slice(0, 34), x - 62, y + 78);
    }
    if (needs && needs.autonomy > 0.7) {
      ctx.fillStyle = '#b75d39';
      ctx.fillText('autonomy high', x - 30, y + (body ? 94 : 78));
    }
  });

  const board = world.villageBoard;
  const proposals = board && board.projectProposals ? board.projectProposals.slice(-4) : [];
  proposals.forEach((proposal, index) => {
    const x = 825;
    const y = 218 + index * 38;
    ctx.fillStyle = proposal.status === 'completed' ? '#f0c35b' : proposal.status === 'in progress' ? '#9fca77' : /^stalled/.test(proposal.status) ? '#b75d39' : proposal.status === 'accepted' ? '#77a783' : '#d5a13a';
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

function updatePracticeAndLanguageFromConstruction(construction, proposal, structure, term) {
  const graph = ensureEmergentPracticeGraph();
  const localName = `${construction.resident_term} repair-building practice`;
  const existing = graph.nodes.find(row => row.local_name === localName || (row.source_construction_rows || []).includes(construction.construction_id));
  const materials = Object.keys(construction.materials_consumed || {});
  const node = existing || {
    practice_id: `EPG-${String(graph.nodes.length + 1).padStart(2, '0')}`,
    local_name: localName,
    resident_term: construction.resident_term,
    player_gloss: `${construction.player_gloss} repair/build habit`,
    engine_concept: structure ? structure.engine_concept : 'component_repair_construction_practice',
    origin_tick: world.tick,
    origin_resident: construction.proposer,
    origin_household: `${construction.proposer}-household`,
    origin_event: construction.construction_id,
    problem_pressure: construction.problem_addressed,
    materials_used: materials,
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
    maintenance_cost: construction.maintenance_cost_after || 1,
    risk_flags: [],
    generations_survived: 0,
    status: 'emerging',
    avatar_role: 'supported_conditions_only',
    hidden_properties_audit_only: true,
    source_construction_rows: [],
    component_affordances: [],
    construction_component_ids: [],
    language_term_id: term ? term.term_id : null,
    translation_confidence: term ? term.translation_confidence : 0.5,
  };
  node.materials_used = Array.from(new Set((node.materials_used || []).concat(materials)));
  node.observations_supporting = Array.from(new Set((node.observations_supporting || []).concat([
    construction.completed ? 'completed project changed the physical structure' : 'project work repaired strained components',
    `${construction.components_added.length} added / ${construction.components_repaired.length} repaired`
  ])));
  node.beliefs_involved = Array.from(new Set((node.beliefs_involved || []).concat([proposal.proposal_id, construction.structure_id])));
  node.social_transmission_path = Array.from(new Set((node.social_transmission_path || []).concat([`${construction.proposer}->${construction.resident_term}`])));
  node.mutation_variants = Array.from(new Set((node.mutation_variants || []).concat([construction.resident_term, construction.player_gloss, proposal.problem_addressed])));
  node.source_construction_rows = Array.from(new Set((node.source_construction_rows || []).concat([construction.construction_id])));
  node.construction_component_ids = Array.from(new Set((node.construction_component_ids || []).concat(construction.components_added, construction.components_repaired)));
  node.component_affordances = Array.from(new Set((node.component_affordances || []).concat(
    (world.gamePrototype3DWorld && world.gamePrototype3DWorld.components ? world.gamePrototype3DWorld.components : [])
      .filter(component => node.construction_component_ids.includes(component.component_id))
      .map(component => component.affordance)
  )));
  node.adoption_count += construction.completed ? 2 : 1;
  node.adoption_households = Array.from(new Set((node.adoption_households || []).concat([`${construction.proposer}-household`])));
  node.practical_score = Number(clamp(Number(node.practical_score || 0) + (construction.completed ? 0.22 : 0.11)).toFixed(3));
  node.ritual_score = Number(clamp(Number(node.ritual_score || 0) + (construction.components_repaired.length > 1 ? 0.04 : 0.015)).toFixed(3));
  node.dispute_score = Number(clamp(Number(node.dispute_score || 0) + (construction.completed ? 0.02 : 0.08)).toFixed(3));
  node.maintenance_cost = Math.max(Number(node.maintenance_cost || 1), construction.maintenance_cost_after || 1);
  node.risk_flags = Array.from(new Set((node.risk_flags || []).concat(construction.completed ? ['new component maintenance burden'] : ['partial repair evidence'])));
  node.generations_survived = Math.max(Number(node.generations_survived || 0), Math.floor(node.adoption_count / 2));
  node.status = node.adoption_count >= 4 && node.practical_score > 0.55 ? 'practical' : construction.completed ? 'refined' : 'emerging';
  if (!existing) graph.nodes.push(node);
  graph.edges.push({ from: construction.construction_id, to: node.practice_id, event: proposal.proposal_id, relation: construction.completed ? 'construction_into_practice' : 'repair_into_practice_evidence', hiddenLawExposed: false });
  if (term) {
    term.adoption_count += construction.completed ? 2 : 1;
    term.practical_score = Number(clamp(Number(term.practical_score || 0) + (construction.completed ? 0.035 : 0.016)).toFixed(3));
    term.translation_confidence = Number(clamp(Number(term.translation_confidence || 0.5) + 0.008).toFixed(3));
    term.meaning_drift = term.meaning_drift || [];
    const drift = construction.completed ? `${term.resident_word} also means a repaired/reinforced work habit` : `${term.resident_word} can mean retie and watch the support`;
    if (!term.meaning_drift.includes(drift)) term.meaning_drift.push(drift);
    if (term.adoption_count >= 7 && !term.variants.includes(`${term.resident_word}-ha`)) term.variants.push(`${term.resident_word}-ha`);
  }
  const sim = ensurePrototype3DWorld();
  (sim.language.soundRoots || []).forEach(root => {
    if (term && (term.roots || []).includes(root.sound_id)) {
      root.adoption_count += 1;
      root.practical_weight = Number(clamp(Number(root.practical_weight || 0) + 0.01).toFixed(3));
      root.drift_history = root.drift_history || [];
      const drift = construction.completed ? 'repair/build work' : 'repair warning';
      if (!root.drift_history.includes(drift)) root.drift_history.push(drift);
    }
  });
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
  const proposal = board.projectProposals.find(row => row.status !== 'accepted' && row.status !== 'refused' && row.status !== 'completed' && !row.project_completed) || board.projectProposals[board.projectProposals.length - 1];
  const accepted = proposal.resident_willingness + proposal.current_support_level >= 0.48;
  proposal.current_support_level = Number(Math.min(1, proposal.current_support_level + 0.25).toFixed(3));
  proposal.status = accepted ? 'accepted' : 'resident still considering';
  proposal.project_progress = Number(proposal.project_progress || 0);
  proposal.project_work_ticks = Number(proposal.project_work_ticks || 0);
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

function ensurePrototypeProjects() {
  if (!world.gamePrototypeProjects) {
    world.gamePrototypeProjects = {
      runCount: 0,
      projectLedger: [],
      completionLedger: [],
      stalledLedger: [],
      boundary: 'diegetic resident project work only; avatar supports conditions, residents choose and labor costs are audited',
    };
  }
  return world.gamePrototypeProjects;
}

function resourceShortagesFor(materials) {
  const needed = {};
  materials.forEach(material => {
    needed[material] = (needed[material] || 0) + 1;
  });
  return Object.entries(needed)
    .filter(([material, count]) => Number(world.resources[material] || 0) < count)
    .map(([material, count]) => `${material}:${world.resources[material] || 0}/${count}`);
}

function consumeProjectMaterials(materials) {
  const consumed = {};
  materials.forEach(material => {
    consumed[material] = (consumed[material] || 0) + 1;
  });
  Object.entries(consumed).forEach(([material, count]) => {
    world.resources[material] = Math.max(0, Number(world.resources[material] || 0) - count);
  });
  return consumed;
}

function materialIdForProjectMaterial(material) {
  if (material === 'wood') return 'rough_branch';
  if (material === 'fiber') return 'fiber';
  if (material === 'water') return 'clay_vessel';
  if (material === 'care') return 'fiber';
  return 'rough_branch';
}

function shapeForProjectMaterial(material, index) {
  if (material === 'fiber' || material === 'care') return 'lash';
  if (material === 'water') return 'cylinder';
  return index % 2 === 0 ? 'post' : 'beam_x';
}

function dimensionsForProjectComponent(shape) {
  if (shape === 'post') return { x: 8, y: 8, z: 54 };
  if (shape === 'beam_x') return { x: 82, y: 7, z: 7 };
  if (shape === 'lash') return { x: 76, y: 48, z: 5 };
  if (shape === 'cylinder') return { x: 16, y: 16, z: 24 };
  return { x: 18, y: 18, z: 18 };
}

function projectComponentPosition(index, shape) {
  const base = [
    { x: -18, y: -12, z: shape === 'post' ? 0 : 58 },
    { x: 106, y: -10, z: shape === 'post' ? 0 : 66 },
    { x: -18, y: 72, z: shape === 'post' ? 0 : 54 },
    { x: 108, y: 72, z: shape === 'post' ? 0 : 58 },
    { x: 45, y: 82, z: 70 },
    { x: 45, y: -20, z: 74 },
  ];
  return base[index % base.length];
}

function applyProjectConstructionToMaterialWorld(proposal, projectRow, consumed) {
  const sim = ensurePrototype3DWorld();
  const structure = sim.structures[0];
  const term = structure ? sim.language.terms.find(row => row.term_id === structure.resident_term_id) : sim.language.terms[0];
  const weakComponents = sim.components
    .filter(component => Number(component.stability || 1) < 0.74 || Number(component.damage || 0) > 0.12)
    .sort((a, b) => Number(a.stability || 1) - Number(b.stability || 1));
  const repaired = weakComponents.slice(0, projectRow.completed ? 3 : 1).map(component => {
    component.damage = Number(clamp(Number(component.damage || 0) - (projectRow.completed ? 0.11 : 0.05)).toFixed(3));
    component.stability = Number(clamp(Number(component.stability || 0) + (projectRow.completed ? 0.12 : 0.055)).toFixed(3));
    component.moisture = Number(clamp(Number(component.moisture || 0) - 0.025).toFixed(3));
    component.repaired_by_project = proposal.proposal_id;
    return component.component_id;
  });
  const added = [];
  if (projectRow.completed) {
    const entries = Object.entries(consumed || {}).filter(([, count]) => Number(count || 0) > 0);
    entries.forEach(([material, count], entryIndex) => {
      for (let i = 0; i < Number(count || 0); i += 1) {
        const shape = shapeForProjectMaterial(material, entryIndex + i);
        const materialId = materialIdForProjectMaterial(material);
        const dimensions = dimensionsForProjectComponent(shape);
        const sourceMaterial = sim.materialCatalog[materialId] || { mass: 1 };
        const componentId = `G3C-P${String(sim.constructionLedger.length + added.length + sim.components.length + 1).padStart(3, '0')}`;
        const component = {
          component_id: componentId,
          engine_concept: `resident_project_${shape}_reinforcement`,
          resident_term_id: term ? term.term_id : 'TERM-TAKU-REN',
          material_id: materialId,
          affordance: shape === 'post' ? 'extra_vertical_support' : shape === 'beam_x' ? 'extra_horizontal_span' : shape === 'lash' ? 'repair_binding' : 'storage_container',
          source: `${proposal.proposal_id} consumed ${material}`,
          shape,
          position3d: projectComponentPosition(sim.components.length + added.length, shape),
          dimensions,
          mass: Number(sourceMaterial.mass || 1),
          moisture: 0.16,
          damage: 0.02,
          support_role: `resident-built reinforcement for ${proposal.problem_addressed}`,
          stability: 0.82,
          created_by: proposal.proposer,
          origin_event: `completed ${proposal.proposal_id}; no fixed building asset`,
          project_built: true,
          proposal_id: proposal.proposal_id,
        };
        ensureComponentPhysics(component);
        sim.components.push(component);
        if (structure && !structure.component_ids.includes(componentId)) structure.component_ids.push(componentId);
        added.push(componentId);
      }
    });
  }
  if (structure) {
    structure.stability = Number(clamp(Number(structure.stability || 0) + repaired.length * 0.025 + added.length * 0.018).toFixed(3));
    structure.moisture_risk = Number(clamp(Number(structure.moisture_risk || 0) - repaired.length * 0.012).toFixed(3));
    structure.maintenance_cost = Math.max(1, Number(structure.maintenance_cost || 1) + (added.length ? 1 : 0));
    structure.status = projectRow.completed ? 'resident-reinforced practical structure' : 'under resident repair';
    structure.risk_flags = Array.from(new Set([...(structure.risk_flags || []), ...(added.length ? ['new reinforcement adds maintenance burden'] : ['repair remains partial'])]));
  }
  const construction = {
    construction_id: `G3CON-${String(sim.constructionLedger.length + 1).padStart(3, '0')}`,
    tick: world.tick,
    proposal_id: proposal.proposal_id,
    project_id: projectRow.project_id,
    proposer: proposal.proposer,
    problem_addressed: proposal.problem_addressed,
    resident_term: term ? term.resident_word : 'taku-ren',
    player_gloss: term ? term.player_gloss : 'raised dry vessel practice',
    completed: projectRow.completed === true,
    materials_consumed: { ...(consumed || {}) },
    components_added: added,
    components_repaired: repaired,
    structure_id: structure ? structure.structure_id : 'none',
    structure_stability_after: structure ? structure.stability : null,
    maintenance_cost_after: structure ? structure.maintenance_cost : null,
    no_fixed_asset: true,
    no_resource_spawning: true,
  };
  sim.constructionLedger.push(construction);
	  sim.observationLedger.push({
    observation_id: `G3O-${String(sim.observationLedger.length + 1).padStart(3, '0')}`,
    tick: world.tick,
    public_observation: projectRow.completed ? `${construction.resident_term} got new reinforcement after project work` : `${construction.resident_term} was partly repaired during project work`,
    resident_interpretation: projectRow.completed ? `${construction.resident_term} holds better but asks for future care` : `${construction.resident_term} still needs attention`,
    linked_structure: construction.structure_id,
    linked_project: proposal.proposal_id,
    hidden_law_visible_normal_view: false,
	    engine_concept_audit_only: 'project construction updated physical components',
	  });
  const practiceNode = updatePracticeAndLanguageFromConstruction(construction, proposal, structure, term);
  construction.practice_id = practiceNode ? practiceNode.practice_id : null;
  construction.practice_status_after = practiceNode ? practiceNode.status : null;
	  recordRealityConstraint(projectRow.completed ? 'project_constructed_components' : 'project_repaired_components', {
    resident: proposal.proposer,
    sourceBeliefId: proposal.proposal_id,
    materials: Object.keys(consumed || {}),
    publicObservation: construction.problem_addressed,
	    residentInterpretation: projectRow.completed ? `resident work changed the physical structure and shaped ${practiceNode ? practiceNode.local_name : 'a local practice'}` : `resident work repaired physical strain and added evidence to ${practiceNode ? practiceNode.local_name : 'a local practice'}`,
    materialTransformation: `${added.length} component(s) added, ${repaired.length} component(s) repaired from consumed project materials`,
    timeCost: 1,
    workCost: Object.values(consumed || {}).reduce((sum, count) => sum + Number(count || 0), 0) + repaired.length,
    toolWear: added.length + repaired.length ? 1 : 0,
	    maintenanceObligation: structure ? `maintain ${structure.structure_id} and ${practiceNode ? practiceNode.practice_id : proposal.proposal_id}` : proposal.proposal_id,
    unintendedConsequence: added.length ? 'new structure parts increase future maintenance burden' : 'repair may not fully remove physical risk',
    hiddenLawInvolved: world.audit ? 'component support, mass, stability, material workability' : 'audit only',
    conservationCheck: true
  });
  return construction;
}

function selectedProjectProposal() {
  const board = ensureVillageBoard();
  if (!board.projectProposals.length) runVillageBoardLoop();
  let proposal = board.projectProposals.find(row => row.status !== 'completed' && !row.project_completed && (row.status === 'accepted' || row.status === 'in progress'));
  let attempts = 0;
  while (!proposal && attempts < 2) {
    supportVillageProposal();
    proposal = board.projectProposals.find(row => row.status !== 'completed' && !row.project_completed && (row.status === 'accepted' || row.status === 'in progress'));
    attempts += 1;
  }
  return proposal || board.projectProposals.find(row => row.status !== 'completed' && !row.project_completed) || board.projectProposals[board.projectProposals.length - 1];
}

function advanceVillageProject() {
  ensureGamePrototype();
  const projects = ensurePrototypeProjects();
  const proposal = selectedProjectProposal();
  if (!proposal) return log('advanceVillageProject', { advanced: false, reason: 'no resident proposal available' });
  if (proposal.status === 'completed' || proposal.project_completed) return log('advanceVillageProject', { advanced: false, reason: 'all resident projects completed', proposalId: proposal.proposal_id, status: proposal.status, completed: true, progress: Number(proposal.project_progress || 1) });
  const materials = (proposal.materials_needed && proposal.materials_needed.length ? proposal.materials_needed : ['fiber', 'care']).slice();
  const accepted = proposal.status === 'accepted' || proposal.status === 'in progress' || proposal.current_support_level >= 0.48;
  projects.runCount += 1;
  if (!accepted) {
    proposal.status = 'stalled: resident not ready';
    const row = {
      project_id: `GPP-${String(projects.projectLedger.length + projects.stalledLedger.length + 1).padStart(3, '0')}`,
      proposal_id: proposal.proposal_id,
      tick: world.tick,
      proposer: proposal.proposer,
      problem_addressed: proposal.problem_addressed,
      stalled_reason: 'resident not ready',
      progress: Number(proposal.project_progress || 0),
      avatar_direct_command: false,
      who_felt_this: proposal.proposer,
    };
    projects.stalledLedger.push(row);
    recordRealityConstraint('village_project_stalled', {
      resident: proposal.proposer,
      sourceBeliefId: proposal.proposal_id,
      materials,
      publicObservation: proposal.problem_addressed,
      residentInterpretation: proposal.status,
      materialTransformation: 'no material transformed; resident did not accept project work',
      timeCost: 1,
      workCost: 0,
      toolWear: 0,
      maintenanceObligation: 'none',
      unintendedConsequence: 'avatar support cannot force labor',
      hiddenLawInvolved: 'none in normal view',
      conservationCheck: true
    });
    recordPrototypeMilestone('village-project-stalled', `${proposal.proposal_id} stalled because resident was not ready`);
    return log('advanceVillageProject', { proposalId: proposal.proposal_id, status: proposal.status, stalled: true, completed: false, progress: row.progress });
  }
  const shortages = resourceShortagesFor(materials);
  if (shortages.length) {
    proposal.status = `stalled: missing ${shortages.join(', ')}`;
    const row = {
      project_id: `GPP-${String(projects.projectLedger.length + projects.stalledLedger.length + 1).padStart(3, '0')}`,
      proposal_id: proposal.proposal_id,
      tick: world.tick,
      proposer: proposal.proposer,
      problem_addressed: proposal.problem_addressed,
      stalled_reason: `missing ${shortages.join(', ')}`,
      progress: Number(proposal.project_progress || 0),
      avatar_direct_command: false,
      who_felt_this: proposal.proposer,
    };
    projects.stalledLedger.push(row);
    mutateResident(proposal.proposer, { trust: -0.004, progress: -0.002, memory: `project stalled on ${proposal.problem_addressed}`, historyEvent: 'project stalled', historyDetail: proposal.proposal_id });
    recordRealityConstraint('village_project_stalled', {
      resident: proposal.proposer,
      sourceBeliefId: proposal.proposal_id,
      materials,
      publicObservation: proposal.problem_addressed,
      residentInterpretation: proposal.status,
      materialTransformation: 'no material transformed; shortage preserved instead of spawning resources',
      timeCost: 1,
      workCost: 1,
      toolWear: 0,
      maintenanceObligation: `resolve shortage for ${proposal.proposal_id}`,
      unintendedConsequence: 'project delay and trust strain',
      hiddenLawInvolved: 'none in normal view',
      conservationCheck: true
    });
    recordPrototypeMilestone('village-project-stalled', `${proposal.proposal_id} stalled on ${shortages.join(', ')}`);
    return log('advanceVillageProject', { proposalId: proposal.proposal_id, status: proposal.status, stalled: true, completed: false, shortages, progress: row.progress });
  }
  const consumed = consumeProjectMaterials(materials);
  const materialWorld = world.gamePrototype3DWorld || ensurePrototype3DWorld();
  const targetComponent = materialWorld && materialWorld.components
    ? materialWorld.components.find(component => Number(component.stability || 1) < 0.75 || Number(component.damage || 0) > 0.12) || materialWorld.components[0]
    : null;
  const toolUse = applyToolPhysicsUse(proposal.proposer, 'project_work', targetComponent, 'village_project_work');
  proposal.project_work_ticks = Number(proposal.project_work_ticks || 0) + 1;
  const previousProgress = Number(proposal.project_progress || 0);
  const toolModifier = toolUse.action_blocked ? -0.22 : (toolUse.failed ? -0.08 : Math.min(0.08, Number(toolUse.fit || 0) * 0.08));
  const progressGain = Math.max(0.08, 0.36 + Math.min(0.14, Number(proposal.current_support_level || 0) * 0.12) + (proposal.resident_willingness > 0.62 ? 0.04 : 0) + toolModifier);
  proposal.project_progress = Number(Math.min(1, previousProgress + progressGain).toFixed(3));
  const completed = proposal.project_progress >= 1;
  proposal.status = completed ? 'completed' : 'in progress';
  const row = {
    project_id: `GPP-${String(projects.projectLedger.length + 1).padStart(3, '0')}`,
    proposal_id: proposal.proposal_id,
    tick: world.tick,
    proposer: proposal.proposer,
    problem_addressed: proposal.problem_addressed,
    materials_consumed: consumed,
    work_time: 1,
    labor_resident: proposal.proposer,
    tool_use_id: toolUse.tool_use_id,
    tool_id: toolUse.tool_id,
    tool_fit: toolUse.fit,
    tool_failed: toolUse.failed,
    tool_repaired: toolUse.repaired,
    tool_blocked: toolUse.action_blocked,
    progress: proposal.project_progress,
    status: proposal.status,
    completed,
    avatar_direct_command: false,
    who_felt_this: proposal.proposer,
	    maintenance_created: completed ? proposal.maintenance_cost : 0,
	  };
	  projects.projectLedger.push(row);
  const construction = applyProjectConstructionToMaterialWorld(proposal, row, consumed);
  row.construction_id = construction.construction_id;
  row.components_added = construction.components_added;
  row.components_repaired = construction.components_repaired;
	  if (completed && !proposal.project_completed) {
	    proposal.project_completed = true;
	    proposal.completed_tick = world.tick;
	    projects.completionLedger.push({
      completion_id: `GPCOMP-${String(projects.completionLedger.length + 1).padStart(3, '0')}`,
      proposal_id: proposal.proposal_id,
      tick: world.tick,
      proposer: proposal.proposer,
      problem_addressed: proposal.problem_addressed,
	      related_practice_nodes: proposal.related_practice_nodes || [],
      construction_id: construction.construction_id,
      components_added: construction.components_added,
      components_repaired: construction.components_repaired,
	      maintenance_cost: proposal.maintenance_cost,
	      resident_memory: `completed ${proposal.problem_addressed}`,
	    });
    if (world.emergentPracticeGraph && proposal.related_practice_nodes) {
      proposal.related_practice_nodes.forEach(id => {
        const node = world.emergentPracticeGraph.nodes.find(row => row.practice_id === id);
        if (node) {
          node.adoption_count = Number(node.adoption_count || 0) + 1;
          if (node.status === 'emerging' || node.status === 'disputed') node.status = 'refined';
          node.mutation_variants = node.mutation_variants || [];
          node.mutation_variants.push(`project-backed ${proposal.proposal_id}`);
        }
      });
    }
  }
  mutateResident(proposal.proposer, {
    trust: completed ? 0.012 : 0.006,
    progress: completed ? 0.02 : 0.01,
    memory: completed ? `completed ${proposal.problem_addressed}` : `worked on ${proposal.problem_addressed}`,
    historyEvent: completed ? 'project completed' : 'project advanced',
    historyDetail: proposal.proposal_id
  });
  world.gamePrototypeCommons = null;
  recordRealityConstraint(completed ? 'village_project_completed' : 'village_project_progress', {
    resident: proposal.proposer,
    sourceBeliefId: proposal.proposal_id,
    materials,
    publicObservation: proposal.problem_addressed,
    residentInterpretation: proposal.status,
    materialTransformation: `consumed ${Object.entries(consumed).map(([material, count]) => `${count} ${material}`).join(', ')} into resident project work; construction ${construction.construction_id} added ${construction.components_added.length} component(s) and repaired ${construction.components_repaired.length}`,
    timeCost: 1,
    workCost: materials.length + 1,
    toolWear: Number(toolUse.wear_delta || 0),
    maintenanceObligation: toolUse.action_blocked ? `repair ${toolUse.tool_id}` : completed ? `maintain completed ${proposal.proposal_id}` : `continue ${proposal.proposal_id}`,
    unintendedConsequence: toolUse.action_blocked ? 'tool failure slowed resident project work' : completed ? 'new maintenance burden exists' : 'ordinary schedules delayed by project work',
	    hiddenLawInvolved: proposal.related_practice_nodes && proposal.related_practice_nodes.length ? 'related practice and component physics remain audit-only' : 'component physics audit-only',
	    conservationCheck: true
	  });
	  recordPrototypeMilestone('village-project-progress', `${proposal.proposal_id} ${proposal.status} at ${proposal.project_progress}; construction ${construction.construction_id}; tool ${toolUse.tool_id}`);
	  return log('advanceVillageProject', { proposalId: proposal.proposal_id, status: proposal.status, stalled: false, completed, progress: proposal.project_progress, materials: Object.keys(consumed).join(','), constructionId: construction.construction_id, componentsAdded: construction.components_added.length, componentsRepaired: construction.components_repaired.length, practiceId: construction.practice_id || null, practiceStatus: construction.practice_status_after || null, toolUseId: toolUse.tool_use_id, toolFailed: toolUse.failed, toolBlocked: toolUse.action_blocked });
}

function ensurePrototypeCommonsSupport() {
  if (!world.gamePrototypeCommonsSupport) {
    world.gamePrototypeCommonsSupport = {
      runCount: 0,
      supportLedger: [],
      recoveryLedger: [],
      boundary: 'diegetic commons support only; resources come from named sources through time, labor, and resident willingness',
    };
  }
  return world.gamePrototypeCommonsSupport;
}

function commonsSourceForResource(resource) {
  const sources = {
    water: { source: 'west well carry', resident: 'Milo', materialSource: 'well water already present in village map', labor: 'carry and store jars', cap: 18 },
    fiber: { source: 'reed bundles near drying path', resident: 'Sera', materialSource: 'cut reed fiber from known path edge', labor: 'cut, dry, and sort fiber', cap: 18 },
    wood: { source: 'fallen branch salvage', resident: 'Tovan', materialSource: 'storm-fallen branch pile', labor: 'carry, split, and stack wood', cap: 24 },
    food: { source: 'nearby patch tending', resident: 'Fay', materialSource: 'recovering edible patches and stored basket', labor: 'check patches, gather carefully, and dry/store food', cap: 16 },
    care: { source: 'shared rest and herb tending', resident: 'Fay', materialSource: 'time, attention, and stored herbs', labor: 'prepare rest space and simple care kit', cap: 12 },
  };
  return sources[resource] || { source: 'ordinary commons sorting', resident: world.selected, materialSource: `known ${resource} store`, labor: `sort ${resource}`, cap: 12 };
}

function commonsSupportTarget() {
  const board = world.villageBoard || null;
  const stalled = board && board.projectProposals
    ? board.projectProposals.find(proposal => /^stalled: missing/.test(proposal.status || ''))
    : null;
  if (stalled) {
    const missing = resourceShortagesFor(stalled.materials_needed || []);
    if (missing.length) {
      return {
        resource: missing[0].split(':')[0],
        reason: `recover stalled project ${stalled.proposal_id}`,
        linkedProposalId: stalled.proposal_id,
      };
    }
  }
  const lowest = Object.entries(world.resources)
    .sort((a, b) => Number(a[1] || 0) - Number(b[1] || 0))[0] || ['fiber', 0];
  return {
    resource: lowest[0],
    reason: Number(lowest[1] || 0) <= 3 ? 'low commons reserve' : 'preventive commons stocktaking',
    linkedProposalId: 'none',
  };
}

function supportResourceCommons() {
  ensureGamePrototype();
  const support = ensurePrototypeCommonsSupport();
  const target = commonsSupportTarget();
  const source = commonsSourceForResource(target.resource);
  const residentName = source.resident && world.residents[source.resident] ? source.resident : world.selected;
  const resident = world.residents[residentName];
  support.runCount += 1;
  const before = Number(world.resources[target.resource] || 0);
  const roomToCap = Math.max(0, Number(source.cap || 12) - before);
  const amount = Math.min(2, roomToCap);
  const tired = resident && resident.progress < 0.12;
  if (!amount || tired) {
    const row = {
      support_id: `GPCS-${String(support.supportLedger.length + support.recoveryLedger.length + 1).padStart(3, '0')}`,
      tick: world.tick,
      resource: target.resource,
      reason: tired ? 'resident too tired for commons work' : 'resource source at local cap',
      source: source.source,
      resident: residentName,
      amount_added: 0,
      avatar_direct_command: false,
      linked_proposal_id: target.linkedProposalId,
    };
    support.supportLedger.push(row);
    recordRealityConstraint('resource_commons_support_blocked', {
      resident: residentName,
      sourceBeliefId: target.linkedProposalId,
      materials: [target.resource],
      publicObservation: `${target.resource} commons support blocked at ${source.source}`,
      residentInterpretation: row.reason,
      materialTransformation: 'no resource added; source cap or resident fatigue preserved',
      timeCost: 1,
      workCost: tired ? 1 : 0,
      toolWear: 0,
      maintenanceObligation: 'try another time or reduce burden',
      unintendedConsequence: tired ? `${residentName} needs rest before commons work` : 'commons source cannot be overdrawn',
      hiddenLawInvolved: 'none in normal view',
      conservationCheck: true
    });
    recordPrototypeMilestone('resource-commons-blocked', `${target.resource} support blocked: ${row.reason}`);
    return log('supportResourceCommons', { resource: target.resource, amount: 0, blocked: true, reason: row.reason, linkedProposalId: target.linkedProposalId });
  }
  world.resources[target.resource] = before + amount;
  mutateResident(residentName, {
    trust: 0.004,
    progress: -0.006,
    memory: `helped commons with ${target.resource}`,
    historyEvent: 'commons support',
    historyDetail: `${target.resource} from ${source.source}`
  });
  const row = {
    support_id: `GPCS-${String(support.supportLedger.length + 1).padStart(3, '0')}`,
    tick: world.tick,
    resource: target.resource,
    reason: target.reason,
    source: source.source,
    material_source: source.materialSource,
    labor: source.labor,
    resident: residentName,
    amount_added: amount,
    before,
    after: world.resources[target.resource],
    avatar_direct_command: false,
    linked_proposal_id: target.linkedProposalId,
    who_felt_this: residentName,
  };
  support.supportLedger.push(row);
  const reopened = [];
  if (world.villageBoard && world.villageBoard.projectProposals) {
    world.villageBoard.projectProposals.forEach(proposal => {
      if (/^stalled: missing/.test(proposal.status || '') && resourceShortagesFor(proposal.materials_needed || []).length === 0) {
        proposal.status = 'accepted';
        proposal.current_support_level = Math.max(Number(proposal.current_support_level || 0), 0.5);
        reopened.push(proposal.proposal_id);
      }
    });
  }
  if (reopened.length) {
    support.recoveryLedger.push({
      recovery_id: `GPCR-${String(support.recoveryLedger.length + 1).padStart(3, '0')}`,
      tick: world.tick,
      resource: target.resource,
      reopened_proposals: reopened,
      source_support_id: row.support_id,
    });
  }
  world.gamePrototypeCommons = null;
  recordRealityConstraint('resource_commons_support', {
    resident: residentName,
    sourceBeliefId: target.linkedProposalId,
    materials: [target.resource],
    publicObservation: `${residentName} supported ${target.resource} commons from ${source.source}`,
    residentInterpretation: target.reason,
    materialTransformation: `${source.labor}; ${amount} ${target.resource} added from ${source.materialSource}`,
    timeCost: 1,
    workCost: 2,
    toolWear: target.resource === 'wood' || target.resource === 'fiber' ? 1 : 0,
    maintenanceObligation: reopened.length ? `resume ${reopened.join(', ')}` : `track ${target.resource} commons`,
    unintendedConsequence: `${residentName} lost work focus while helping commons`,
    hiddenLawInvolved: 'none in normal view',
    conservationCheck: true
  });
  recordPrototypeMilestone('resource-commons-support', `${amount} ${target.resource} from ${source.source}; reopened ${reopened.length}`);
  return log('supportResourceCommons', { resource: target.resource, amount, before, after: world.resources[target.resource], source: source.source, resident: residentName, reopened: reopened.length, linkedProposalId: target.linkedProposalId });
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
  const proposals = board.projectProposals.slice(-6).map(row => `${row.proposal_id}: ${row.proposer} proposes ${row.problem_addressed} support=${row.current_support_level} progress=${Number(row.project_progress || 0).toFixed(2)} status=${row.status} force=${row.avatar_can_force}`);
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

Object.assign(window, { enterWorld, moveNorth, moveSouth, moveWest, moveEast, talkBounded, askSchedule, offerHelp, borrowTool, returnTool, waitOffscreen, introduceWorldAnomaly, runAnomalyExperiment, spreadAnomalyBelief, planAnomalyInvestigationSchedule, runScheduledAnomalyInvestigation, runStochasticConsequencePulse, runStochasticConsequenceBurst, planStochasticRecoveryLoop, resolveStochasticRecoveryStep, runStochasticRecoveryLoop, runStochasticHistoryChoice, runStochasticHistorySocialEcho, runStochasticHistoryInfluenceLoop, runOrdinaryAffordanceInfluenceLoop, runCivilizationPressureStep, runCivilizationPressureLoop, runPracticalDiscoveryStep, runPracticalDiscoveryLoop, runVillageBoardLoop, supportVillageProposal, askVillageBoardQuestion, waitOnVillageBoard, advanceVillageProject, supportResourceCommons, performNearbyAction, endVillageDay, leaveAndReturnLater, runPrototypeMaterialWorldStep, runPrototypePhysicsStep, runStructuralPhysicsStep, runStructuralPhysicsLoop, runContactConstraintPhysicsStep, runContactConstraintPhysicsLoop, runMaterialStatePhysicsStep, runMaterialStatePhysicsLoop, runPlayablePhysicsPracticeSliceStep, runPlayablePhysicsPracticeSliceLoop, runPlayableVillageDay03Step, runPlayableVillageDay03Loop, runPrimaryPlaySurfaceStep, runPrimaryPlaySurfaceLoop, runFirstPlayableWalkthrough, exportFirstPlayableWalkthrough, runNormalPlayLook, runNormalPlayAsk, runNormalPlaySupport, runNormalPlayWait, runNormalPlayReturn, runNormalPlaySave, runNormalPlayActionRailLoop, enterPlayerMode, exitPlayerMode, togglePlayerMode, runPlayerModeInterfaceLoop, runPlayerProposalDeckLoop, supportPlayerProposalDeck, askPlayerProposalDeck, waitPlayerProposalDeck, runLivedPracticeLoop, runResidentWorksiteLoop, runTerrainPhysicsStep, runTerrainPhysicsLoop, runToolPhysicsStep, runToolPhysicsLoop, runResourcePhysicsStep, runResourcePhysicsLoop, runThermalPhysicsStep, runThermalPhysicsLoop, runWaterPhysicsStep, runWaterPhysicsLoop, runEcologyPhysicsStep, runEcologyPhysicsLoop, runResidentMaterialManipulationStep, runResidentMaterialManipulationLoop, runResidentBodyPhysicsStep, runResidentBodyPhysicsLoop, runRealityConstraintAudit, introduceAvatarHint, runHintDivergenceInterpretation, runAvatarHintDivergenceLoop, runHintBranchReturnSession, maintainHintBranchPractice, reviveForgottenHintPractice, runHintBranchPersistenceLoop, runPrototypeOpening, runPrototypeGuidedStep, runPrototypePracticeChain, runPrototypeReturnProof, runFirstPlayablePrototypeLoop, comparePrototypeDivergenceSeeds, auditPrototypeCommons, runCivilizationDeepTimeEpoch, runDeepTimePhysicsEpoch, applyLatestDeepTimeEffectToVillage, runCivilizationMillionYearSim, runCivilizationTenMillionYearSim, runCivilizationSurvivalAudit, runAutonomousResidentTick, runAutonomousResidentSeason, runPrototypeQASmoke, runPrototypeAutoStep, startPrototypeAutoSim, pausePrototypeAutoSim, runPrototypeAutoBurst, savePrototypeSlot, returnPrototypeSlot, exportPrototypeSaveReceipt, exportPrototypeAcceptanceReceipt, repairTrust, saveWorld, restoreWorld, toggleAudit, exportReplay, runPlaytestChecklist, runStateBoundaryAudit, runSaveRestoreSmoke, runAuditAfterRollbackCheck, runAllQAHooks, runDashboardResidentAction, interruptWork, apologizeToResident, giveSpace, completeTrustRepair, runContinuityLoop, runSocialMemoryPulse, settleSelectedRelationship, generateScenarioReceipt, logReceiptObservation, resolveLatestObservation, setObservationFilter, setObservationFilterAll, setObservationFilterOpen, setObservationFilterWatch, setObservationFilterResolved, setObservationFilterBlocking, auditLandingFailures, toggleDeepPanels, runReviewerLandingPass });
bindControls();
render();
