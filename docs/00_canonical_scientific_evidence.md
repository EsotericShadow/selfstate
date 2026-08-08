# Canonical Scientific Evidence

## Purpose

The repository contains hundreds of numbered reports. That archive records real development history, but report count is not evidence strength. It also mixes several different artifact classes:

- theoretical statements;
- controlled experiments;
- learned-controller benchmarks;
- environment and feature specifications;
- browser demonstrations;
- reviewer workflow and handoff engineering;
- product-bridge experiments.

A scientific reviewer should not have to infer which documents carry the central argument. This index identifies the canonical evidence, the strongest limitations, and the reports that should not be counted as scientific support for self-equivalent representation.

## Scope of the current claim

The canonical claim is:

> In bounded partially observable control problems, hidden properties of the continuing controlled system can become decision-relevant when they mediate action effects, value, future options, adaptation, or continuity. A learned representation is self-equivalent only if causal tests locate the relevant information at a persistent agent/action boundary and show reuse across control problems.

The repository does not currently establish a general selfhood law, consciousness, moral patienthood, or a metaphysical theory of personal identity.

## Artifact classes

Every report should be read as one of the following types.

| Class | Meaning | Scientific role |
|---|---|---|
| T — Theory | Definitions, propositions, predictions, falsifiers | States the claim and what would count against it |
| E — Controlled experiment | Matched positive and negative conditions with declared endpoints | Primary empirical evidence inside the simulator |
| L — Learned-controller experiment | Learned representations or policies evaluated under held-out conditions | Stronger evidence when budgets, splits, seeds, and interventions are adequate |
| S — Specification | Defines a future environment, pressure layer, architecture, or benchmark | Not evidence until an executable evaluation is completed |
| D — Demonstration | Browser or visual presentation of existing mechanics | Useful for inspection; not by itself scientific validation |
| Q — Quality/review engineering | Test harness, handoff, receipt, export, defect, or reviewer workflow | Supports reproducibility and auditability; does not support the self-state hypothesis directly |
| B — Bridge/application | Maps an idea into another domain such as software repair | Exploratory transfer; not evidence for the core selfhood claim unless independently validated |

## Canonical theory

### 1. Research brief

[`01_research_brief.md`](01_research_brief.md) — **T**

Use for:

- the narrow computational thesis;
- collapse cases where self-state should not help;
- distinction between minimal control self, continuity, narrative self, and consciousness;
- current hypothesis revisions.

Do not use it as empirical proof.

### 2. Experimental program

[`03_experimental_program.md`](03_experimental_program.md) — **T**

Use for:

- comparator classes;
- environment families;
- measurement plan;
- strong support and falsification tests.

The most important standard in this document is the generic-memory attack: structured self-state is not supported merely because it beats a reactive policy.

### 3. Formal core v2

[`05_formal_core_v2.md`](05_formal_core_v2.md) — **T**

This is the normative formal statement.

It replaces the claim that an optimal policy must encode the full posterior over agent state with a decision-sufficiency claim:

- full belief is sufficient but not generally necessary;
- policy-, value-, or prediction-sufficient quotients may be smaller;
- a self-blind representation is insufficient only when it merges histories that require conflicting actions because of hidden agent-state distinctions;
- benchmark necessity should be expressed as additional regret under a declared comparator class.

### 4. Hidden-state boundary attack

[`14_hidden_state_boundary_attack.md`](14_hidden_state_boundary_attack.md) — **T/E framing**

Use for:

- the anti-tautology boundary;
- the distinction between hidden world state, passive internal state, agent-state control, and continuity;
- required positive and negative controls;
- explicit falsifiers.

This is one of the most important documents in the repository because it prevents the thesis from collapsing into “useful hidden variables are useful.”

## Canonical minimal experiments

These experiments establish mechanism possibility in controlled toy settings. They are primarily **C1 evidence**: they show that the proposed distinctions can be operationalized.

| Report | Class | Canonical question | Main evidential role | Main limitation |
|---|---|---|---|---|
| [`06_minimal_experiment_report.md`](06_minimal_experiment_report.md) | E | Can a controller distinguish self drift from world drift? | Establishes the basic attribution benchmark | Toy environment and supplied structure |
| [`07_representation_search_report.md`](07_representation_search_report.md) | E | Does model selection retain action-effect state under self drift? | Compression precursor | Candidate model family is designed |
| [`08_predictive_state_emergence_report.md`](08_predictive_state_emergence_report.md) | E | Can action-conditioned predictions encode agent-state without a self label? | Predictive-state precursor | Small controlled representation family |
| [`09_hidden_viability_survival_report.md`](09_hidden_viability_survival_report.md) | E | Does a persistent internal estimate improve delayed survival control? | Viability/control evidence | Hand-designed policies and state dynamics |
| [`10_interruption_coherence_report.md`](10_interruption_coherence_report.md) | E | Does ownership/epoch state improve continuation after corrupt memory? | Identity-like continuity precursor | Synthetic commitment records |
| [`15_selfhood_boundary_probe_report.md`](15_selfhood_boundary_probe_report.md) | E | Which hidden variables pass the self-equivalent boundary? | Negative-control evidence | Boundary construction is supplied |
| [`16_architecture_convergence_report.md`](16_architecture_convergence_report.md) | E/L precursor | Do multiple learner families recover different components under self and world drift? | Cross-architecture precursor | Learner and task families remain narrow |

These reports support the existence of a testable boundary. They do not establish natural, domain-general emergence.

## Canonical learned-representation evidence

### 1. Recurrent observer

[`61_ssrm_3d_recurrent_observer_report.md`](61_ssrm_3d_recurrent_observer_report.md) — **L**

Question:

> Can recurrent observers recover agent-state from embodied action-observation traces without making the language model the controller?

Why it matters:

- compares a frame-only model with RNN, GRU, and LSTM observers;
- probes energy, integrity, mobility, and sensor capability;
- measures recurrent gain, future-viability prediction, subspace ablation, and counterfactual edits;
- includes a low-pressure spatial control where recurrence adds little.

Positive result:

- recurrent self-state gains increase under hidden energy, body drift, delayed options, commitments, arbitration, and social pressure;
- self-subspace ablation damages future-viability prediction in the pressured stages.

Limitation:

- observers are trained on traces generated by supplied source agents;
- the future-viability target is aligned with the proposed self variables;
- linear probe directions are used for edits;
- this is representation evidence, not learned closed-loop control.

### 2. Learned controller

[`62_ssrm_3d_learned_controller_report.md`](62_ssrm_3d_learned_controller_report.md) — **L**

Question:

> Does recurrent policy state improve control and retain agent-state information when no self-state supervision is supplied?

Why it matters:

- moves the probe from an observer into policy state;
- compares frame MLP, RNN, GRU, and LSTM controllers;
- preserves a low-pressure control where recurrence does not help.

Positive result:

- recurrent controllers substantially outperform the frame model under hidden energy, body drift, delayed options, commitment recovery, arbitration, and social pressure;
- policy state contains decodable energy, integrity, mobility, and sensor capability.

Critical limitation:

- training is return-weighted behavior cloning from supplied traces, not full online reinforcement learning;
- direct counterfactual self-edit action swings are small;
- decodability and performance gain therefore exceed the current evidence for causal policy use.

This report supports learned control relevance, but not a completed attractor test.

### 3. Return-selected hidden-regime controller

[`97_ssrm_3d_return_selected_hidden_regime_controller_report.md`](97_ssrm_3d_return_selected_hidden_regime_controller_report.md) — **L**

Question:

> Can validation return select a stronger option-gated recurrent controller before held-out hidden-regime evaluation?

Positive result:

- the selected GRU improves over the fixed-bias GRU, frame controller, and reactive controller on held-out seeds;
- removing regime-signal, infrastructure, or body-state channels causes specific losses;
- major hidden regimes remain gated until after the development period.

Critical limitations:

- the neural model is still trained from designed traces;
- validation selects one option-bias hyperparameter using a custom objective;
- the canonical evaluation uses a small fixed set of tune and evaluation seeds;
- `pass` is determined by hand-set thresholds in the experiment code, not inferential statistics;
- social/culture ablation remains unstable.

This is meaningful C2/C3-style evidence inside the simulator, not proof of an optimizer-independent self-state attractor.

## Canonical negative and limiting evidence

Negative results are part of the canonical record.

### 1. Low-pressure controls

Reports 61 and 62 show that recurrent state does not improve the low-pressure spatial stage. This supports the predicted collapse case: self-equivalent memory should not be recruited when current observation is enough.

### 2. Weak direct policy editability

Report 62 records small direct action changes after editing the learned self direction. This blocks the stronger claim that the decoded self-state factor is already a robust causal policy variable.

### 3. Architecture and seed instability

The architecture stress, hard-return, online-return, and seed-sweep reports contain partial convergence. High return and useful recurrence do not reliably imply that the learned state passes the persistent agent-boundary test.

Representative documents include:

- [`47_architecture_boundary_stress_test_report.md`](47_architecture_boundary_stress_test_report.md)
- [`50_architecture_hard_return_audit_report.md`](50_architecture_hard_return_audit_report.md)
- [`52_architecture_online_return_learner_report.md`](52_architecture_online_return_learner_report.md)
- [`54_architecture_policy_gradient_seed_sweep_report.md`](54_architecture_policy_gradient_seed_sweep_report.md)

These reports should be used to limit the attractor claim, not hidden behind later positive runs.

### 4. No-leak learned-integration weakness

The no-leak integration sweep removes scenario identity and randomizes pressure combinations. It reports margin fragility and unstable integrated-social ablations. This is evidence that designed packet structure can be easier to learn than a stable reusable integration.

See [`73_ssrm_3d_learned_integration_no_leak_report.md`](73_ssrm_3d_learned_integration_no_leak_report.md).

### 5. Readiness planner succeeds; distillation fails

[`138_ssrm_3d_readiness_sequence_consequence_report.md`](138_ssrm_3d_readiness_sequence_consequence_report.md) — **L/B with negative learner result**

The explicit sequence optimizer uses cloned simulator lookahead and solves the 72-hour readiness world. The planner-free GRU does not inherit that behavior:

- final alive falls to zero;
- knowledge transfer remains zero;
- most channel ablations improve rather than damage the policy;
- planner-free distillation and ablation specificity fail.

This result is scientifically valuable. It says the world is solvable by bounded consequence planning but the current learned recurrent policy has not acquired the required control structure.

It should not be summarized as general progress toward emergent selfhood.

## Evidence that remains non-canonical or indirect

### Environment and pressure specifications

Reports that define illness, weather, trust, threat, ecology, injury, development, dependent care, loss, affect, or other pressure layers are hypotheses and benchmark specifications until a matched experiment measures the predicted representation effect.

Richness of simulation detail is not itself evidence for self-equivalent state.

### Designed policy victories

A designed integrated policy outperforming a deliberately reactive policy demonstrates that the environment contains the intended control job. It does not demonstrate that an unlabeled learner discovered the relevant abstraction.

### Browser demonstrations

Interactive worlds can expose state, replay, persistence, trust, continuity, and social mechanics. They are useful for inspection and reviewer comprehension. They do not become scientific evidence merely because behavior is visible.

### Review and handoff engineering

The reports beginning in the 300-series primarily improve:

- browser-local review flow;
- defect ledgers;
- transcript and checkpoint visibility;
- resident dashboards;
- handoff receipts;
- cross-tab and reload continuity;
- download guards;
- reviewer launch paths.

These are **Q-class artifacts**. They may improve auditability and reproducibility, but they should not be counted as new evidence for self-state, agency, autonomy, consciousness, or social cognition.

### Software repair bridge

[`139_software_repair_bridge_report.md`](139_software_repair_bridge_report.md) — **B**

The deterministic 15-task WrongFix arena illustrates a useful principle: visible success can conceal failure in a weaker correctness channel. The minimum-channel critic matches the task-bank oracle.

The task bank and critic are designed together, no real repository is edited, and no LLM coding agent is evaluated. This is a conceptual application bridge, not validation of SelfState in software engineering.

## Current claim matrix

| Claim | Best canonical evidence | Current grade |
|---|---|---|
| Hidden agent-state can matter differently from hidden world state | Reports 06, 07, 08, 14, 15, 16 | C1 with bounded controls |
| Internal viability can alter long-horizon action value | Report 09; reports 61–62 pressured stages | C1/C2 inside toy environments |
| Recurrent state can recover reusable agent variables | Reports 61–62 | C2 precursor |
| Recurrent state can improve control under agent-state pressure | Report 62; report 97 | C2/C3 precursor |
| The learned factor is causally used by policy | Report 61 edits; report 62 action edits; ablations in 97 | Partial |
| The boundary is stable across architectures and seeds | Architecture suite | Mixed |
| Compression alone finds self rather than world | Reports 07, 25 and boundary controls | Rejected without intervention |
| Natural emergence under online return | Policy-gradient and actor-critic precursors | Partial and environment-limited |
| General self-state attractor law | None | Open |
| Benchmark-relative necessity with regret lower bound | Formal Core v2 defines the test | Not yet demonstrated at strong scale |
| Identity continuity | Report 10 and restore/fork precursors | C1 synthetic evidence |
| Consciousness | None | Outside scope |

## Minimum evidence package for a new canonical result

A new report should enter this index only when it includes:

1. one primary hypothesis and one primary endpoint;
2. a declared comparator class;
3. matched observation, parameter, memory, data, and compute budgets;
4. distinct training, tuning, and held-out evaluation seeds;
5. raw per-seed outputs and uncertainty intervals;
6. a world-state or external-latent control;
7. a passive-internal or irrelevant-hidden control;
8. a detachable-tool or controllable-external control where boundary is claimed;
9. post-training intervention or targeted ablation;
10. failure and null results;
11. exact command, dependency versions, artifact hashes, and deterministic configuration where possible;
12. claim language tied to the claim ladder in [`SCIENTIFIC_STATUS.md`](../SCIENTIFIC_STATUS.md).

## Highest-value next experiments

### 1. Conflicting-history regret benchmark

Construct histories matched on world information but differing in hidden agent-state belief. Quantify the regret imposed when a representation merges histories with disjoint optimal actions. This directly tests the corrected necessity proposition.

### 2. Cross-environment learned boundary benchmark

Train one learner family across multiple embodiments and world families. Hold out both body and environment combinations. Test whether the same learned factor tracks the persistent agent boundary rather than scenario identity.

### 3. Causal policy edit benchmark

Discover a candidate self subspace without test labels, edit it after training, and measure directional changes in policy and value. Compare against equal-norm random, world-state, passive-internal, and detachable-tool directions.

### 4. Matched information-bottleneck sweep

Vary representation rate or dimension while matching policy capacity and data. Measure whether a reusable agent-state quotient appears at lower regret than local-history and world-only alternatives as reuse and horizon increase.

### 5. Independent reproduction pack

Freeze a small canonical subset, containerize dependencies, publish raw seeds and expected hashes, and invite an external researcher to rerun it without author assistance. Independent reproducibility would add more legitimacy than another large batch of internally numbered reports.

## Bottom line

The repository already contains a serious falsifiable idea, useful negative controls, substantial engineering, and several bounded learned-controller results. Its scientific credibility depends on narrower claims and stricter evidence curation—not on increasing report count.

The strongest defensible position today is:

> SelfState provides a growing set of simulation-based precursors showing when decision-relevant agent-state representations can improve partially observable control. It has not yet established a general selfhood attractor, a domain-independent necessity theorem, or consciousness.
