# Canonical Scientific Evidence

## Purpose

The repository contains hundreds of numbered reports. That archive records development history, but report count is not evidence strength. It mixes:

- theory;
- controlled experiments;
- learned-controller benchmarks;
- environment specifications;
- browser demonstrations;
- reviewer and handoff engineering;
- application bridges.

This index identifies the documents that carry the scientific argument, the strongest negative results, and the artifacts that should not be counted as evidence for self-equivalent representation.

## Current claim

> In bounded partially observable control problems, hidden properties of the continuing controlled system can become decision-relevant when they mediate action effects, value, future options, adaptation, or continuity. A representation counts as self-equivalent only when causal tests locate the relevant information at a persistent agent/action boundary and show reuse across control problems.

The repository does not establish a general selfhood law, consciousness, moral patienthood, or metaphysical personal identity.

## Artifact classes

| Class | Meaning | Scientific role |
|---|---|---|
| T — Theory | Definitions, propositions, predictions, falsifiers | States the claim and what would count against it |
| E — Controlled experiment | Matched positive and negative conditions | Primary simulator evidence |
| L — Learned-controller experiment | Learned representations or policies under held-out evaluation | Stronger evidence when budgets, splits, seeds, and interventions are adequate |
| S — Specification | Future environment, pressure layer, architecture, or benchmark | Not evidence until evaluated |
| D — Demonstration | Browser or visual presentation of existing mechanics | Inspection aid, not validation by itself |
| Q — Quality engineering | Tests, handoff, receipts, exports, defects, review workflow | Supports auditability, not the hypothesis directly |
| B — Bridge | Maps the idea into another domain | Exploratory transfer, not core validation |

## Canonical theory

1. [`01_research_brief.md`](01_research_brief.md) — **T**  
   Narrow thesis, collapse cases, mechanism stack, and explicit separation from consciousness.

2. [`02a_literature_positioning.md`](02a_literature_positioning.md) — **T**  
   Critical bridge to POMDPs, state abstraction, causal representation learning, robot self-modeling, motor prediction, interoception, and homeostatic control. It records what each literature can and cannot support.

3. [`03_experimental_program.md`](03_experimental_program.md) — **T**  
   Comparator classes, environment families, measurements, and strong support/falsification tests.

4. [`05_formal_core_v2.md`](05_formal_core_v2.md) — **T**  
   Normative formal statement. It replaces full-posterior necessity with policy/value/prediction sufficiency and a regret proposition against self-blind comparator classes.

5. [`14_hidden_state_boundary_attack.md`](14_hidden_state_boundary_attack.md) — **T/E framing**  
   Anti-tautology boundary separating hidden world state, passive internal state, agent-state control, detachable tools, and continuity.

## Canonical minimal experiments

These are primarily **C1 mechanism-possibility evidence**.

| Report | Question | Evidential role | Main limitation |
|---|---|---|---|
| [`06_minimal_experiment_report.md`](06_minimal_experiment_report.md) | Can control distinguish self drift from world drift? | Basic attribution benchmark | Toy environment and supplied structure |
| [`07_representation_search_report.md`](07_representation_search_report.md) | Does model selection retain action-effect state under self drift? | Compression precursor | Candidate model family is designed |
| [`08_predictive_state_emergence_report.md`](08_predictive_state_emergence_report.md) | Can action-conditioned predictions encode agent state without a self label? | Predictive-state precursor | Small controlled family |
| [`09_hidden_viability_survival_report.md`](09_hidden_viability_survival_report.md) | Does a persistent internal estimate improve delayed survival control? | Viability/control evidence | Hand-designed policies and state dynamics |
| [`10_interruption_coherence_report.md`](10_interruption_coherence_report.md) | Does ownership/epoch state improve continuation after corrupt memory? | Continuity precursor | Synthetic records |
| [`15_selfhood_boundary_probe_report.md`](15_selfhood_boundary_probe_report.md) | Which hidden variables pass the operational boundary? | Negative-control evidence | Boundary construction is supplied |
| [`16_architecture_convergence_report.md`](16_architecture_convergence_report.md) | Do multiple learner families recover different components under self and world drift? | Cross-architecture precursor | Narrow learner and task families |

These reports show that the proposed distinctions can be operationalized. They do not establish natural, domain-general emergence.

## Canonical learned-representation evidence

### Recurrent observer

[`61_ssrm_3d_recurrent_observer_report.md`](61_ssrm_3d_recurrent_observer_report.md) — **L**

Positive evidence:

- frame-only, RNN, GRU, and LSTM observers are compared;
- energy, integrity, mobility, and sensor capability are probed;
- recurrent gains increase under hidden energy, body drift, delayed options, commitments, arbitration, and social pressure;
- self-subspace ablation damages future-viability prediction;
- the low-pressure spatial control shows little recurrent advantage.

Limits:

- traces come from supplied source agents;
- future-viability targets are aligned with proposed agent variables;
- edit directions come from linear probes;
- this is observer evidence, not autonomous learned control.

### Learned controller

[`62_ssrm_3d_learned_controller_report.md`](62_ssrm_3d_learned_controller_report.md) — **L**

Positive evidence:

- policy state rather than a separate observer is probed;
- recurrent controllers outperform the frame model under hidden energy, body drift, delayed options, commitment recovery, arbitration, and social pressure;
- recurrent policy state contains decodable agent variables;
- the low-pressure control rejects unnecessary recurrence.

Limits:

- training is return-weighted behavior cloning from supplied traces, not full online reinforcement learning;
- direct counterfactual self-edit action swings are small;
- decodability and reward gain are stronger than the current evidence for causal policy use.

### Return-selected hidden-regime controller

[`97_ssrm_3d_return_selected_hidden_regime_controller_report.md`](97_ssrm_3d_return_selected_hidden_regime_controller_report.md) — **L**

Positive evidence:

- held-out evaluation improves over fixed-bias recurrent, frame, and reactive baselines;
- regime-signal, infrastructure, and body ablations create specific losses;
- major hidden regimes remain gated until after the development period.

Limits:

- the neural model is still trained from designed traces;
- validation selects one option-bias hyperparameter with a custom objective;
- tune and evaluation sets are small fixed seed lists;
- `pass` uses hand-set engineering thresholds, not inferential statistics;
- social/culture ablation remains unstable.

This is meaningful bounded C2/C3-style evidence, not proof of an optimizer-independent attractor.

## Canonical negative and limiting evidence

Negative evidence is part of the result, not a defect to hide.

### Low-pressure collapse case

Reports 61 and 62 show that recurrence does not improve the low-pressure spatial stage. This supports the prediction that persistent agent-state memory should not be recruited when current observation is enough.

### Weak direct policy editability

Report 62 records small action changes after editing the decoded self direction. This blocks the stronger claim that the factor is already a robust causal policy variable.

### Architecture and seed instability

High return and recurrence do not reliably imply agent-boundary convergence. Representative limiting reports are:

- [`49_architecture_boundary_stress_report.md`](49_architecture_boundary_stress_report.md)
- [`53_architecture_hard_return_audit_report.md`](53_architecture_hard_return_audit_report.md)
- [`55_architecture_online_return_learner_report.md`](55_architecture_online_return_learner_report.md)
- [`57_architecture_policy_gradient_seed_sweep_report.md`](57_architecture_policy_gradient_seed_sweep_report.md)

These reports limit the attractor claim and must remain visible alongside later positive runs.

### No-leak learned-integration weakness

[`73_ssrm_3d_no_leak_integration_sweep_report.md`](73_ssrm_3d_no_leak_integration_sweep_report.md) removes scenario identity and randomizes pressure combinations. It reports margin fragility and unstable integrated-social ablations. Designed packet structure is easier to learn than stable reusable integration.

### Readiness planner succeeds; distillation fails

[`138_ssrm_3d_readiness_sequence_consequence_report.md`](138_ssrm_3d_readiness_sequence_consequence_report.md) — **L/B with a negative learner result**

The explicit sequence optimizer uses cloned simulator lookahead and solves the 72-hour readiness world. The planner-free GRU does not inherit the behavior:

- final alive falls to zero;
- knowledge transfer remains zero;
- most channel ablations improve rather than damage the policy;
- planner-free distillation and ablation specificity fail.

This shows that the world is solvable by bounded consequence planning but the current recurrent policy has not learned the required control structure.

## Non-canonical or indirect evidence

### Pressure specifications

Reports defining illness, weather, trust, threat, ecology, injury, development, dependent care, loss, affect, or other pressure layers are hypotheses or benchmark specifications until a matched experiment measures the predicted representation effect.

Simulation richness is not evidence by itself.

### Designed policy victories

A designed integrated policy beating a reactive policy shows that the environment contains the intended control job. It does not show that an unlabeled learner discovered the abstraction.

### Browser demonstrations

Interactive worlds can expose state, replay, persistence, trust, and continuity. Visibility improves inspection but does not convert deterministic behavior into evidence of autonomous cognition or self-state emergence.

### Review and handoff engineering

The 300-series reports mainly improve browser review, defect ledgers, transcripts, dashboards, handoff receipts, cross-tab continuity, download guards, and reviewer launch paths. These are **Q-class artifacts**. They support auditability but should not count as new evidence for self-state, agency, consciousness, or social cognition.

### Software repair bridge

[`139_software_repair_bridge_report.md`](139_software_repair_bridge_report.md) is a useful **B-class** illustration that visible tests can conceal a weak correctness channel. The task bank and critic are designed together; no real repository or LLM coding agent is evaluated. It is not validation of the core hypothesis.

## Claim matrix

| Claim | Best evidence | Current grade |
|---|---|---|
| Hidden agent state can matter differently from hidden world state | Reports 06–08, 14–16 | C1 with bounded controls |
| Internal viability can alter long-horizon action value | Report 09; pressured stages in 61–62 | C1/C2 in simulation |
| Recurrent state can recover reusable agent variables | Reports 61–62 | C2 precursor |
| Recurrent state can improve control under agent-state pressure | Reports 62 and 97 | C2/C3 precursor |
| The learned factor is causally used by policy | Edits and ablations in 61, 62, 97 | Partial |
| The boundary is stable across architectures and seeds | Architecture suite | Mixed |
| Compression alone identifies self rather than world | Boundary controls | Rejected without intervention |
| Natural emergence under online return | Policy-gradient and actor-critic precursors | Partial and environment-limited |
| General self-state attractor law | None | Open |
| Benchmark-relative necessity with a regret lower bound | Formal Core v2 defines the test | Strong-scale demonstration open |
| Identity-like continuity | Report 10 and [`68_ssrm_3d_agent_continuity_report.md`](68_ssrm_3d_agent_continuity_report.md) | C1 synthetic evidence |
| Consciousness | None | Outside scope |

## Minimum package for a new canonical result

A report should enter this index only when it includes:

1. one primary hypothesis and endpoint;
2. a declared comparator class;
3. matched observation, parameter, memory, data, and compute budgets;
4. separate training, tuning, and held-out evaluation seeds;
5. raw per-seed outputs and uncertainty intervals;
6. world-state/external-latent controls;
7. passive-internal and irrelevant-hidden controls;
8. detachable-tool or controllable-external controls when claiming a boundary;
9. post-training intervention or targeted ablation;
10. null and failure results;
11. exact command, dependencies, hashes, and deterministic configuration where possible;
12. claim language tied to [`SCIENTIFIC_STATUS.md`](../SCIENTIFIC_STATUS.md).

## Highest-value next experiments

### 1. Conflicting-history regret benchmark

Construct histories matched on world information but differing in agent-state belief. Measure the regret imposed when a representation merges histories with disjoint optimal actions. This directly tests the corrected necessity proposition.

### 2. Cross-environment learned boundary benchmark

Train across multiple embodiments and world families, hold out body/environment combinations, and test whether one factor tracks the continuing agent boundary rather than scenario identity.

### 3. Causal policy edit benchmark

Discover a candidate self subspace without test labels. Compare directional edits against equal-norm random, world-state, passive-internal, and detachable-tool directions.

### 4. Matched information-bottleneck sweep

Vary representation rate while matching policy capacity and data. Test whether a reusable agent-state quotient reaches lower regret than local-history and world-only alternatives as reuse and horizon increase.

### 5. Independent reproduction pack

Freeze a small canonical subset, lock dependencies, publish raw seeds and expected hashes, and invite an external researcher to rerun it without author assistance. Independent reproduction would add more credibility than another large batch of internally numbered reports.

## Bottom line

The repository contains a serious falsifiable idea, useful controls, substantial engineering, and bounded learned-controller results. Its scientific credibility depends on narrower claims and stricter curation—not report count.

> SelfState is currently a research program of simulation-based precursors showing when decision-relevant agent-state representations can improve partially observable control. It has not established a general selfhood attractor, a domain-independent necessity theorem, or consciousness.
