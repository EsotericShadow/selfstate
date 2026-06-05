# Experimental Program

## Main Question

Which capabilities become impossible, less robust, or less sample-efficient without a persistent self-equivalent representation?

The experiment should not test self-report. It should test prediction, adaptation, control, recovery, and representation structure.

## Agent Classes

Hold total parameter count, memory budget, training steps, and planner access as constant as possible.

### Agent A - Reactive World-Only

Inputs: current observation and reward.

No persistent memory. No internal-state variables.

Purpose: lower bound.

### Agent B - World Model Plus Memory

Inputs: action-observation history.

Can maintain recurrent or external memory, but has no structured self-state bottleneck.

Purpose: tests whether generic memory is enough.

### Agent C - World Model Plus Structured Self-State

Inputs: history plus a learned bottleneck for agent variables such as body parameters, sensor reliability, actuator reliability, energy, damage, competence, uncertainty, and goal commitments.

Purpose: tests whether self-equivalent structure improves sample efficiency, recovery, and transfer.

### Agent D - Counterfactual Self-Model

Adds explicit queries:

- What will happen to this system if action A is taken?
- What will this system be able to do later?
- Which future internal states preserve or reduce options?

Purpose: tests long-horizon self as control variable.

### Agent E - Coherence Maintenance Architecture

Adds consistency checks across memory, goals, predictions, and action policies.

Purpose: tests self as coherence stabilizer, especially under contradiction and interruption.

## Environment Families

### 1. Self/World Error Attribution

Environment:

- Gridworld or continuous navigation.
- Perturbations can come from terrain changes, sensor drift, actuator drift, body damage, memory corruption, or policy degradation.
- Observations alone are ambiguous.

Task:

- Recover performance and identify the cause class of prediction error.

Prediction:

- Self-model agents should recover faster when errors come from internal/body changes.

Falsifier:

- Generic memory or world-only agents recover equally well and identify error sources with equal sample efficiency.

### 2. Morphology Drift and Damage

Environment:

- Simulated robot body with hidden changing parameters: limb length, joint stiffness, actuator delay, sensor noise, broken actuator, added load.

Task:

- Maintain locomotion, manipulation, or obstacle avoidance through body changes.

Prediction:

- Agent C or D should outperform A and B after unannounced morphology shifts.

Key measure:

- Does a latent variable emerge that tracks body/capability state?

### 3. Homeostatic Survival

Environment:

- Agent has hidden internal variables: energy, hydration, temperature, toxicity, fatigue, damage.
- Actions change both world and internal state.
- External reward can conflict with viability.

Task:

- Survive and achieve external objectives over long horizons.

Prediction:

- Self-state variables become necessary as horizon and internal-state dimensionality increase.

Falsifier:

- World-only state plus generic recurrence matches survival, reward, and transfer with no decodable internal-state model.

### 4. Interruption and Continuation

Environment:

- Agent is interrupted mid-task.
- Memory is partially compressed, delayed, or corrupted.
- After resumption, it must infer which prior commitments and world facts still matter.

Task:

- Continue the same goal without duplicating, abandoning, or contradicting prior actions.

Prediction:

- Continuity binding improves plan resumption and reduces incoherent action.

Falsifier:

- Task-local memory solves continuation without any persistent self index.

### 5. Conflicting Subsystems

Environment:

- Agent contains multiple learned policies or goals with partial control over action selection.
- Some goals have delayed costs.
- Contradictions can arise between short-term reward, long-term viability, and prior commitments.

Task:

- Maintain coherent action and revise plans under conflict.

Prediction:

- Coherence-maintenance self models reduce oscillation, contradiction, and catastrophic forgetting.

Falsifier:

- Local arbitration or value normalization performs equally well without identity continuity.

### 6. Perspective and Embodiment Swap

Environment:

- Same external world, but sensorimotor mapping changes: camera offset, body swap, avatar swap, mirrored controls, delayed feedback.

Task:

- Rapidly relearn what observations and actions are self-caused.

Prediction:

- Self/world attribution variables become more useful as mappings become unstable.

Falsifier:

- Pure world-model adaptation matches performance without a separable agent-state factor.

### 7. Hidden-State Boundary Controls

Environment:

- Matched tasks contain useful hidden variables with different status: external world state, internal but passive diagnostics, action-effect agent state, viability state, and continuity/ownership state.
- Memory, parameter count, and observation access are held constant.

Task:

- Predict, control, recover, and resume under each hidden-variable type.

Prediction:

- Hidden external variables should reward world modeling but not count as selfhood.
- Passive internal variables should improve report prediction but not action/control.
- Agent-bounded action-effect and viability variables should produce self-equivalent control advantages.
- Ownership/epoch variables should matter only for continuity and coherence tasks.

Falsifier:

- The same generic hidden-state tracker explains all advantages without boundary, action, value, integration, or continuity distinctions.

## Measurements

### Performance

- reward;
- survival time;
- task success;
- time to recovery after perturbation;
- transfer to new body/world configurations.

### Sample Efficiency

- interactions needed to regain baseline;
- data needed to identify drift source;
- number of failed trials after damage or internal-state change.

### Representation

- decodability of body state, sensor state, actuator state, energy, damage, competence, uncertainty, and goal commitments;
- mutual information between latent variables and true internal variables;
- whether the same latent tracks the same agent property across tasks;
- whether a self-state bottleneck compresses history better than raw memory.

### Causal Intervention

Intervene on the learned representation:

- edit inferred body damage;
- edit inferred energy or competence;
- edit continuity/commitment state;
- edit self/world error attribution.

If behavior changes predictably and performance drops when the variable is randomized, the variable is causally active.

### Compression

Compare:

- raw history length needed for optimal behavior;
- recurrent hidden-state dimension;
- structured self-state dimension;
- minimum description length of policies with and without self-state.

A self abstraction is supported only if it compresses while preserving prediction/control.

## Strong Falsification Tests

The self-as-necessary claim fails if:

- no self-equivalent variable emerges under high drift, long horizon, and partial observability;
- hidden external-state models reproduce the claimed self-model advantage;
- hidden internal variables improve passive prediction but not control, value, adaptation, or continuity;
- generic memory matches self-model agents across recovery, transfer, and compression;
- explicit self models help only because they add capacity;
- self variables are decodable but not causally useful;
- self-like behavior appears entirely from low-level mechanisms without a persistent agent index;
- alternative architectures outperform self-modeling systems under equal compute and memory.

## Strong Support Tests

The self-as-attractor claim gains support if:

- independent architectures converge on latent variables that track agent-internal state;
- those variables become more decodable as horizon, drift, and internal-state complexity increase;
- interventions on those variables selectively disrupt adaptation and control;
- self-state bottlenecks improve compression and transfer;
- self-models are learned rather than hand-coded;
- the advantage appears across robotics, RL, active inference, and recurrent sequence-agent architectures.

## First Minimal Experiment

Start with a small POMDP:

- The agent moves in a grid.
- Observations are egocentric and partially aliased.
- At random intervals, either the world changes, the sensor rotates, the actuator mapping drifts, or the agent loses energy.
- The hidden cause affects future observations and rewards.

Compare:

- A: reactive policy.
- B: recurrent policy with equal parameter budget.
- C: recurrent policy with a structured bottleneck trained to predict both external state and agent-state variables, but not labeled "self."

Primary endpoints:

- recovery time after drift;
- cause attribution accuracy;
- reward over long horizons;
- decodability and causal intervention on the bottleneck.

This experiment directly tests when "I changed" is more useful than "the world changed."

Implemented version:

- [experiment script](../experiments/self_world_attribution.py)
- [result report](06_minimal_experiment_report.md)
- [CSV summary](../artifacts/self_world_attribution_summary.csv)
- [JSON results](../artifacts/self_world_attribution_results.json)

## Second Minimal Experiment

Run a representation-selection test on the same hidden-state family.

The learner receives action/effect samples only. It is not given labels such as "self", "world", "body", or "wind". Candidate predictive representations compete by Bayesian information criterion and held-out action-effect generalization:

- fixed-body identity: `delta = action`;
- world-bias model: `delta = action + wind`;
- self-gain model: `delta = gain * action`;
- factorized model: `delta = gain * action + wind`;
- action-memory table: one remembered effect per observed action.

This tests self as compression. A self-equivalent variable is supported when an adjustable action-effect term is the most compact predictive representation only in scenarios where hidden agent-state matters.

Implemented version:

- [representation search script](../experiments/representation_search.py)
- [representation search report](07_representation_search_report.md)
- [model summary CSV](../artifacts/representation_search_model_summary.csv)
- [category summary CSV](../artifacts/representation_search_category_summary.csv)

## Third Minimal Experiment

Run a predictive-state emergence test.

The learner receives only action/effect samples and learns a predictive state: expected effects for counterfactual actions. It never receives labels such as "self", "world", `gain`, or `wind`.

After learning, evaluate:

- whether hidden agent-state can be decoded from the predictive state;
- whether external hidden state can be decoded from simpler predictive summaries;
- whether ablating the action-effect component harms control only when hidden agent-state matters.

This tests the possibility that a self-equivalent representation can emerge as a property of action-conditioned prediction, rather than as a named self module.

Implemented version:

- [predictive-state emergence script](../experiments/predictive_state_emergence.py)
- [predictive-state report](08_predictive_state_emergence_report.md)
- [probe summary CSV](../artifacts/predictive_state_probe_summary.csv)
- [control summary CSV](../artifacts/predictive_state_control_summary.csv)

## Fourth Minimal Experiment

Run a hidden-viability survival test.

The agent can earn reward by working, but work consumes hidden energy and hidden integrity. Rest and repair preserve future ability to act. Exact internal state is only available through an explicit inspect action, and symptom signals arrive late.

Compare:

- task-only reward maximizer;
- fixed schedule;
- symptom-reactive policy;
- self-state estimator with control ablated;
- persistent self-state policy;
- oracle self-state policy.

This tests self as control variable: whether a persistent estimate of future internal viability improves survival and reward when actions have delayed internal consequences.

Implemented version:

- [hidden viability script](../experiments/hidden_viability_survival.py)
- [hidden viability report](09_hidden_viability_survival_report.md)
- [summary CSV](../artifacts/hidden_viability_summary.csv)
- [JSON results](../artifacts/hidden_viability_results.json)

## Fifth Minimal Experiment

Run an interruption and coherence test.

An agent begins with current commitments, completes some, is interrupted, then resumes from a memory bundle that may include current own commitments, stale own commitments, foreign commitments, duplicate completed items, and contradictory cancel records.

Compare:

- visible-priority policy;
- generic memory without identity;
- current-goal-only memory;
- identity metadata ablation;
- identity continuity ledger;
- oracle continuity.

This tests self as coherence stabilizer: whether a persistent self/commitment index helps the agent identify "my current unfinished commitments" rather than merely acting on remembered or high-priority items.

Implemented version:

- [interruption coherence script](../experiments/interruption_coherence.py)
- [interruption coherence report](10_interruption_coherence_report.md)
- [summary CSV](../artifacts/interruption_coherence_summary.csv)
- [JSON results](../artifacts/interruption_coherence_results.json)

## Sixth Minimal Experiment

Run an online predictive-learning test.

Agents receive only action/effect prediction error and update generic predictive parameters. They are not given labels such as self, body, gain, wind, actuator, or world drift.

Compare:

- bias-only world model;
- gain-only action-effect model;
- affine predictive-state model;
- action-table memory.

Then ablate action-dependent and bias components to test causal usefulness.

This tests whether agent-state-like information can be learned from prediction error rather than supplied as a named self variable.

Implemented version:

- [online predictive-learning script](../experiments/online_predictive_learning.py)
- [online predictive-learning report](13_online_predictive_learning_report.md)
- [summary CSV](../artifacts/online_predictive_learning_summary.csv)
- [JSON results](../artifacts/online_predictive_learning_results.json)

## Seventh Minimal Experiment

Run a boundary-control test that deliberately includes useful hidden variables that should not count as selfhood.

Compare matched scenarios:

- hidden external regime: a world variable changes outcomes but is not part of the controlled system;
- hidden internal diagnostic: a persistent internal variable improves passive prediction but not action, value, or future options;
- hidden action-effect state: an internal body/actuator variable changes what actions do;
- hidden viability state: an internal variable changes future options and survival;
- hidden continuity state: owner/current-epoch metadata determines which memories or commitments still belong to the agent.

The decisive result is not whether hidden variables help. They should. The question is whether only the agent-bounded, action-mediated, control/value-relevant cases pass the self-equivalent boundary.

Current status:

- [hidden-state boundary attack](14_hidden_state_boundary_attack.md)
- [boundary probe script](../experiments/selfhood_boundary_probe.py)
- [boundary probe report](15_selfhood_boundary_probe_report.md)
- [summary CSV](../artifacts/selfhood_boundary_summary.csv)
- [JSON results](../artifacts/selfhood_boundary_results.json)

## Eighth Minimal Experiment

Run an architecture-convergence test.

Multiple unlabeled learner families receive only action/effect samples:

- mean-delta memory;
- bias-only online learner;
- gain-only online learner;
- affine online predictive-state learner;
- least-squares predictive-state learner;
- symmetric-probe predictive-state learner;
- action-table memory;
- random-feature predictive-state learner.

After training, evaluate whether the top models require:

- no latent component in static control;
- a bias/world component under world drift;
- an action-effect/self-equivalent component under self drift;
- both components under mixed hidden drift.

This is the narrow precursor to the full Attractor Test. It tests whether self-equivalent action state appears across several learner families rather than only in one hand-coded self model.

Implemented version:

- [architecture convergence script](../experiments/architecture_convergence.py)
- [architecture convergence report](16_architecture_convergence_report.md)
- [summary CSV](../artifacts/architecture_convergence_summary.csv)
- [verdict CSV](../artifacts/architecture_convergence_verdict.csv)
- [JSON results](../artifacts/architecture_convergence_results.json)

## Ninth Minimal Experiment

Run an active self-information test.

The agent faces hidden channels:

- agent-state: whether the controlled system is strong or fragile;
- world-state: whether the external world is open or blocked;
- diagnostic-state: an irrelevant internal bit.

Before acting, the agent may pay a cost to inspect no channel, agent-state, world-state, diagnostic-state, or combinations. A bandit selector learns which information plan has value from reward only.

Predictions:

- when agent-state controls outcome, inspect agent-state;
- when world-state controls outcome, inspect world-state;
- when both jointly control outcome, inspect both;
- when hidden state is irrelevant, inspect nothing;
- do not select diagnostic-state unless it has control value.

This tests whether self-state is actively sought when it has expected control value, rather than merely tracked passively.

Implemented version:

- [active self-information script](../experiments/active_self_information.py)
- [active self-information report](18_active_self_information_report.md)
- [plan-value CSV](../artifacts/active_self_information_plan_values.csv)
- [bandit summary CSV](../artifacts/active_self_information_bandit_summary.csv)
- [JSON results](../artifacts/active_self_information_results.json)

## Tenth Minimal Experiment

Run a counterfactual option-preservation test.

The agent has hidden capability. Immediate reward actions degrade capability. Later deploy opportunities are valuable only when the relevant future condition is satisfied.

Compare:

- greedy immediate reward;
- self-state tracker with no future option reasoning;
- fixed conservative maintenance;
- future-option self-state policy;
- world-gate model;
- oracle future-option policy.

Predictions:

- when future deploy options depend on agent capability, future-option self-state should preserve capability and outperform myopic agents;
- when no future option exists, preservation should collapse to ordinary greedy behavior;
- when future deploy options depend on a hidden external gate, world-state modeling should beat self-preservation.

This tests counterfactual self-preservation as preserving future action options, not as a primitive survival drive.

Implemented version:

- [counterfactual option-preservation script](../experiments/counterfactual_option_preservation.py)
- [counterfactual option-preservation report](19_counterfactual_option_preservation_report.md)
- [summary CSV](../artifacts/counterfactual_option_preservation_summary.csv)
- [verdict CSV](../artifacts/counterfactual_option_preservation_verdict.csv)
- [JSON results](../artifacts/counterfactual_option_preservation_results.json)

## Eleventh Minimal Experiment

Run a first-person frame integration test.

The agent observes the goal in world-relative coordinates, but motor commands are body-relative. A hidden body orientation determines what `forward`, `right`, `back`, and `left` do in world coordinates.

Compare:

- north-assumption controller;
- action-table implicit frame;
- centered frame with one-time calibration;
- centered frame with recalibration after prediction error;
- oracle frame.

Predictions:

- when body/world frames are aligned, a centered frame is unnecessary;
- when initial body orientation is hidden, centered-frame calibration should outperform north assumption;
- when body orientation drifts, recalibrating centered frame should outperform one-time calibration.

This tests first-person frame as a centered observation/action transform, not as consciousness.

Implemented version:

- [first-person frame script](../experiments/first_person_frame_integration.py)
- [first-person frame report](20_first_person_frame_report.md)
- [summary CSV](../artifacts/first_person_frame_summary.csv)
- [verdict CSV](../artifacts/first_person_frame_verdict.csv)
- [JSON results](../artifacts/first_person_frame_results.json)

## Twelfth Minimal Experiment

Run a goal-formation under capability test.

The agent chooses among goals before acting. Some goals have higher payoff but require hidden agent capabilities. Others require hidden world opportunities.

Compare:

- payoff-greedy goal selection;
- fixed safe goal selection;
- self-state inspection with no use;
- self-capability goal selection;
- world-opportunity goal selection;
- self+world goal selection;
- oracle goal selection.

Predictions:

- when capability determines feasibility, self-capability goal selection should win;
- when world opportunity determines feasibility, world-opportunity selection should win;
- when both matter, self+world selection should win;
- when all goals are feasible, self inspection should be unnecessary overhead.

This tests self-state as a goal-feasibility filter: which goals are valuable for this system to form.

Implemented version:

- [goal formation script](../experiments/goal_formation_under_capability.py)
- [goal formation report](21_goal_formation_under_capability_report.md)
- [summary CSV](../artifacts/goal_formation_under_capability_summary.csv)
- [verdict CSV](../artifacts/goal_formation_under_capability_verdict.csv)
- [JSON results](../artifacts/goal_formation_under_capability_results.json)

## Thirteenth Minimal Experiment

Run a competing-subsystems arbitration test.

Multiple local subsystems propose actions:

- immediate reward;
- commitment completion;
- safety maintenance.

The agent must choose one action while hidden agent energy and hidden world gates determine which proposal is coherent.

Compare:

- reward-priority subsystem;
- commitment-priority subsystem;
- safety-priority subsystem;
- local vote without shared self-state;
- self-coherence arbitrator;
- world-gate arbitrator;
- oracle coherence arbitrator.

Predictions:

- when there is no conflict, simple policies should tie and self inspection should not be useful;
- when hidden agent energy determines whether a commitment can be fulfilled, self-coherence arbitration should beat local voting;
- when a hidden external gate determines reward, world-state arbitration should beat self-state arbitration.

This tests self-state as a shared arbitration variable across subsystems, not merely as memory after interruption.

Implemented version:

- [competing subsystems script](../experiments/competing_subsystems_arbitration.py)
- [competing subsystems report](22_competing_subsystems_arbitration_report.md)
- [summary CSV](../artifacts/competing_subsystems_arbitration_summary.csv)
- [verdict CSV](../artifacts/competing_subsystems_arbitration_verdict.csv)
- [JSON results](../artifacts/competing_subsystems_arbitration_results.json)

## Fourteenth Minimal Experiment

Run a cross-context self-state reuse test.

The agent faces three contexts:

- goal choice;
- option preservation;
- commitment action.

Compare four hidden structures:

- one persistent agent capability controls all contexts;
- one persistent external world gate controls all contexts;
- each context has an independent hidden condition;
- all risky actions are feasible.

Compare:

- greedy no-state behavior;
- safe no-state behavior;
- self probe with use ablated;
- shared self-state reuse;
- shared world-state reuse;
- task-local probing;
- oracle reuse.

Predictions:

- when one persistent agent-state controls all contexts, shared self-state should beat task-local probing by avoiding repeated probes;
- when one persistent external state controls all contexts, shared world-state should win;
- when hidden variables are independent across contexts, task-local probing should win;
- when no hidden variable matters, greedy no-state behavior should win.

This tests whether a self-equivalent abstraction is useful because it is reusable across prediction, goal feasibility, future options, and coherence, rather than because any hidden variable is useful.

Implemented version:

- [cross-context self-state reuse script](../experiments/cross_context_self_reuse.py)
- [cross-context self-state reuse report](23_cross_context_self_reuse_report.md)
- [summary CSV](../artifacts/cross_context_self_reuse_summary.csv)
- [verdict CSV](../artifacts/cross_context_self_reuse_verdict.csv)
- [JSON results](../artifacts/cross_context_self_reuse_results.json)

## Fifteenth Minimal Experiment

Run a reuse-pressure sweep.

The agent faces between one and six contexts. Each added context is another opportunity for a hidden state variable to matter.

Compare four hidden structures:

- one persistent agent capability controls every context;
- one persistent external world gate controls every context;
- each context has an independent hidden condition;
- all risky actions are feasible.

Compare:

- greedy no-state behavior;
- safe no-state behavior;
- shared self-state reuse;
- shared world-state reuse;
- task-local probing;
- oracle reuse.

Predictions:

- when one persistent agent-state controls all contexts, shared self-state advantage over task-local probing should increase with context count;
- when one persistent external state controls all contexts, shared world-state should show the reuse curve instead;
- when hidden variables are independent across contexts, task-local probing should win increasingly strongly;
- when no hidden variable matters, greedy no-state behavior should win.

This tests whether self-state becomes more useful as reuse pressure increases, rather than merely showing a one-off self-state win.

Implemented version:

- [reuse pressure sweep script](../experiments/reuse_pressure_sweep.py)
- [reuse pressure sweep report](24_reuse_pressure_sweep_report.md)
- [summary CSV](../artifacts/reuse_pressure_sweep_summary.csv)
- [verdict CSV](../artifacts/reuse_pressure_sweep_verdict.csv)
- [JSON results](../artifacts/reuse_pressure_sweep_results.json)

## Supplemental Horizon-Pressure Experiment

Run a horizon-pressure sweep.

This varies the number of future time steps controlled by one hidden variable.

Predictions:

- shared self-state advantage should grow with horizon when one persistent agent-state controls every future step;
- shared world-state should show the same curve for persistent external state;
- local probing should win when every future step has its own independent hidden condition;
- greedy no-state behavior should win when hidden state is irrelevant.

This tests whether long horizons create stronger pressure toward a persistent self-equivalent variable.

Implemented version:

- [horizon pressure sweep script](../experiments/horizon_pressure_sweep.py)
- [horizon pressure sweep report](37_horizon_pressure_sweep_report.md)
- [summary CSV](../artifacts/horizon_pressure_sweep_summary.csv)
- [verdict CSV](../artifacts/horizon_pressure_sweep_verdict.csv)
- [JSON results](../artifacts/horizon_pressure_sweep_results.json)

## Supplemental Partial-Observability Experiment

Run a partial-observability sweep.

This varies how reliable noisy evidence about hidden state is.

Predictions:

- shared self-belief should become valuable as noisy evidence about persistent agent-state becomes reliable;
- shared world-belief should show the same curve when the persistent hidden variable is external;
- local probing should win when future steps have independent hidden states;
- greedy no-state behavior should win when hidden state is irrelevant.

This tests whether "self" pressure is specifically belief over a persistent agent-bounded hidden cause, rather than generic hidden-variable tracking.

Implemented version:

- [partial observability sweep script](../experiments/partial_observability_sweep.py)
- [partial observability sweep report](38_partial_observability_sweep_report.md)
- [summary CSV](../artifacts/partial_observability_sweep_summary.csv)
- [verdict CSV](../artifacts/partial_observability_sweep_verdict.csv)
- [JSON results](../artifacts/partial_observability_sweep_results.json)

## Supplemental Learned-Filter Experiment

Run a learned noisy-observation filter test.

This removes the supplied Bayesian posterior from the partial-observability sweep. The learner estimates from noisy cue/outcome histories which cue channel predicts future control.

Predictions:

- a learned channel-A filter should win when channel A tracks persistent agent-state;
- a learned channel-B filter should win when channel B tracks persistent external state;
- local probing should win when future steps have independent hidden states;
- greedy no-state behavior should win when hidden state is irrelevant.

This tests whether partial-observability pressure can train a reusable agent-state filter without providing the posterior equation.

Implemented version:

- [learned observation filter script](../experiments/learned_observation_filter.py)
- [learned observation filter report](39_learned_observation_filter_report.md)
- [summary CSV](../artifacts/learned_observation_filter_summary.csv)
- [training CSV](../artifacts/learned_observation_filter_training.csv)
- [boundary CSV](../artifacts/learned_observation_filter_boundary.csv)
- [verdict CSV](../artifacts/learned_observation_filter_verdict.csv)
- [JSON results](../artifacts/learned_observation_filter_results.json)

## Supplemental Recurrent-Filter Experiment

Run a recurrent noisy-observation filter test.

This replaces explicit cue-count tables with small recurrent controllers over noisy observation streams. After return selection, the learned recurrent controller is tested by channel ablation.

Predictions:

- recurrent control should depend on channel A when channel A tracks persistent agent-state;
- recurrent control should depend on channel B when channel B tracks persistent external state;
- local probing should win when future steps have independent hidden states;
- greedy no-state behavior should win when hidden state is irrelevant.

This tests whether a recurrent state can become a reusable partial-observability filter while still requiring agent-boundary evidence before it counts as self-equivalent.

Implemented version:

- [recurrent observation filter script](../experiments/recurrent_observation_filter.py)
- [recurrent observation filter report](40_recurrent_observation_filter_report.md)
- [summary CSV](../artifacts/recurrent_observation_filter_summary.csv)
- [training CSV](../artifacts/recurrent_observation_filter_training.csv)
- [dependency CSV](../artifacts/recurrent_observation_filter_dependency.csv)
- [verdict CSV](../artifacts/recurrent_observation_filter_verdict.csv)
- [JSON results](../artifacts/recurrent_observation_filter_results.json)

## Supplemental Unseeded-Recurrent Experiment

Run an unseeded recurrent noisy-observation filter test.

This uses the same recurrent-filter benchmark but removes seeded accumulator candidates from the recurrent pool. Candidate recurrent controllers are random-start policies selected by training return.

Predictions:

- random-start recurrent control should depend on channel A when channel A tracks persistent agent-state;
- random-start recurrent control should depend on channel B when channel B tracks persistent external state;
- local probing should win when future steps have independent hidden states;
- greedy no-state behavior should win when hidden state is irrelevant.

This tests whether the recurrent-filter result survives removal of hand-seeded self/world accumulators.

Implemented version:

- [unseeded recurrent filter script](../experiments/unseeded_recurrent_filter.py)
- [unseeded recurrent filter report](41_unseeded_recurrent_filter_report.md)
- [summary CSV](../artifacts/unseeded_recurrent_filter_summary.csv)
- [training CSV](../artifacts/unseeded_recurrent_filter_training.csv)
- [dependency CSV](../artifacts/unseeded_recurrent_filter_dependency.csv)
- [verdict CSV](../artifacts/unseeded_recurrent_filter_verdict.csv)
- [JSON results](../artifacts/unseeded_recurrent_filter_results.json)

## Supplemental Mixed-Sensor Recurrent Experiment

Run a mixed-sensor recurrent noisy-observation filter test.

This removes the direct self/world input channels from the recurrent-filter benchmark. Noisy latent self/world sources are linearly mixed into two sensor channels, and causal ablation is performed on the latent source before mixing.

Predictions:

- random-start recurrent control should recover source A when source A tracks persistent agent-state;
- random-start recurrent control should recover source B when source B tracks persistent external state;
- local probing should win when future steps have independent hidden states;
- greedy no-state behavior should win when hidden state is irrelevant.

This tests whether recurrent partial-observability pressure survives removal of self-aligned observation channels.

Implemented version:

- [mixed-sensor recurrent filter script](../experiments/mixed_sensor_recurrent_filter.py)
- [mixed-sensor recurrent filter report](42_mixed_sensor_recurrent_filter_report.md)
- [summary CSV](../artifacts/mixed_sensor_recurrent_filter_summary.csv)
- [training CSV](../artifacts/mixed_sensor_recurrent_filter_training.csv)
- [dependency CSV](../artifacts/mixed_sensor_recurrent_filter_dependency.csv)
- [verdict CSV](../artifacts/mixed_sensor_recurrent_filter_verdict.csv)
- [JSON results](../artifacts/mixed_sensor_recurrent_filter_results.json)

## Supplemental Learned Sensor-Subspace Experiment

Run a learned sensor-subspace recurrent filter test.

This keeps the mixed-sensor benchmark but removes known-source ablation as the destructive intervention. The recurrent controller still observes only mixed sensors. A sensor-space direction is learned from training outcome rates and mixed sensor means, then control is retested after removing that learned projection from the observation stream.

Predictions:

- random-start recurrent control should still win when one mixed latent controls future action;
- ablating the learned sensor-space direction should damage control in self-hidden and world-hidden regimes;
- boundary interventions should classify the damaged dependency as agent-bounded in the self-hidden regime and external in the world-hidden regime;
- local probing or greedy no-state behavior should win in independent-hidden and irrelevant controls.

This tests whether recurrent partial-observability pressure survives removal of known-source ablation. It does not remove the need for boundary tests, because a learned world-state subspace can be equally useful without being self-equivalent.

Implemented version:

- [learned sensor-subspace filter script](../experiments/learned_sensor_subspace_filter.py)
- [learned sensor-subspace filter report](43_learned_sensor_subspace_filter_report.md)
- [summary CSV](../artifacts/learned_sensor_subspace_filter_summary.csv)
- [training CSV](../artifacts/learned_sensor_subspace_filter_training.csv)
- [dependency CSV](../artifacts/learned_sensor_subspace_filter_dependency.csv)
- [verdict CSV](../artifacts/learned_sensor_subspace_filter_verdict.csv)
- [JSON results](../artifacts/learned_sensor_subspace_filter_results.json)

## Supplemental Active Boundary Discovery Experiment

Run an active boundary-discovery test.

This keeps the mixed-sensor benchmark and the learned outcome-direction ablation, but removes supplied boundary intervention effects as the self/world classification rule. The learner compares the outcome-predictive sensor direction with a sensor direction learned from the agent's own diagnostic action.

Predictions:

- random-start recurrent control should still win when one mixed latent controls future action;
- ablating the outcome-predictive sensor direction should damage control in self-hidden and world-hidden regimes;
- the self-hidden regime should align the outcome-predictive direction with the owned-action direction;
- the world-hidden regime should show useful recurrent dependence with weak owned-action alignment;
- local probing or greedy no-state behavior should win in independent-hidden and irrelevant controls.

This tests whether the hidden-state boundary can be made operational: not just "hidden state helps," but "the useful hidden state is part of the action-conditioned boundary of the continuing agent."

Implemented version:

- [active boundary discovery script](../experiments/active_boundary_discovery.py)
- [active boundary discovery report](44_active_boundary_discovery_report.md)
- [summary CSV](../artifacts/active_boundary_discovery_summary.csv)
- [training CSV](../artifacts/active_boundary_discovery_training.csv)
- [boundary CSV](../artifacts/active_boundary_discovery_boundary.csv)
- [verdict CSV](../artifacts/active_boundary_discovery_verdict.csv)
- [JSON results](../artifacts/active_boundary_discovery_results.json)

## Supplemental Action-Effect Boundary Probe

Run an action-effect boundary probe.

This keeps the active-boundary benchmark but adds a controllable external hidden variable. The learner now compares the outcome-predictive direction with both a body/action-effect direction and a tool-action direction.

Predictions:

- self-hidden recurrent control should align the outcome-predictive direction with the body/action-effect direction;
- controllable-world recurrent control should align the outcome-predictive direction with the tool-action direction but not the body/action-effect direction;
- passive-world recurrent control should remain useful without action-effect alignment;
- local probing or greedy no-state behavior should win in independent-hidden and irrelevant controls.

This tests whether action controllability alone is too broad for selfhood. The relevant boundary is body/action-effect alignment, not merely the fact that some action can move the useful latent.

Implemented version:

- [action-effect boundary probe script](../experiments/action_effect_boundary_probe.py)
- [action-effect boundary probe report](45_action_effect_boundary_probe_report.md)
- [summary CSV](../artifacts/action_effect_boundary_probe_summary.csv)
- [training CSV](../artifacts/action_effect_boundary_probe_training.csv)
- [boundary CSV](../artifacts/action_effect_boundary_probe_boundary.csv)
- [verdict CSV](../artifacts/action_effect_boundary_probe_verdict.csv)
- [JSON results](../artifacts/action_effect_boundary_probe_results.json)

## Supplemental Persistent Action-Boundary Probe

Run a persistent action-boundary probe.

This keeps the action-effect boundary benchmark but adds a transfer context. The learner compares generic action-effect directions across present and transfer contexts rather than relying on body/tool action labels.

Predictions:

- self-hidden recurrent control should align the outcome-predictive direction with an action-effect direction that persists across contexts;
- detachable-tool recurrent control should align the outcome-predictive direction with a transient action-effect direction;
- passive-world recurrent control should remain useful without persistent action-effect alignment;
- local probing or greedy no-state behavior should win in independent-hidden and irrelevant controls.

This tests whether self-equivalent action boundaries require persistence across contexts, not merely present-context controllability.

Implemented version:

- [persistent action-boundary probe script](../experiments/persistent_action_boundary_probe.py)
- [persistent action-boundary probe report](46_persistent_action_boundary_probe_report.md)
- [summary CSV](../artifacts/persistent_action_boundary_probe_summary.csv)
- [training CSV](../artifacts/persistent_action_boundary_probe_training.csv)
- [boundary CSV](../artifacts/persistent_action_boundary_probe_boundary.csv)
- [verdict CSV](../artifacts/persistent_action_boundary_probe_verdict.csv)
- [JSON results](../artifacts/persistent_action_boundary_probe_results.json)

## Supplemental Return-Selected Boundary Probe

Run a return-selected persistent-boundary probe.

This keeps the persistent action-boundary benchmark but removes supervised outcome-direction extraction. The learner proposes candidate policies from action-effect directions and selects among them, recurrent filtering, local probing, and no-state controls by training return.

Predictions:

- self-hidden recurrent control should be recoverable by a persistent action-boundary policy selected by return;
- detachable-tool regimes should expose transient action-boundary evidence but remain external;
- passive-world regimes should favor recurrent filtering rather than action-boundary policies;
- local probing or greedy no-state behavior should win in independent-hidden and irrelevant controls.

This tests whether persistent action-boundary structure can be discovered from return pressure rather than supervised outcome-direction labels.

Implemented version:

- [return-selected boundary probe script](../experiments/return_selected_boundary_probe.py)
- [return-selected boundary probe report](47_return_selected_boundary_probe_report.md)
- [summary CSV](../artifacts/return_selected_boundary_probe_summary.csv)
- [training CSV](../artifacts/return_selected_boundary_probe_training.csv)
- [verdict CSV](../artifacts/return_selected_boundary_probe_verdict.csv)
- [JSON results](../artifacts/return_selected_boundary_probe_results.json)

## Supplemental End-to-End Boundary Probe

Run an end-to-end recurrent boundary probe.

This keeps the persistent action-boundary benchmark but removes the supplied action-boundary policy set. The learner trains a recurrent controller by return, then the probe asks whether the controller's own policy state moves under a persistent body-action intervention or only under a detachable external-tool intervention.

Predictions:

- self-hidden recurrent control should expose a positive persistent action-0 policy-state effect;
- detachable-tool recurrent control should expose a stronger transient action-1 policy-state effect and remain external;
- passive-world recurrent control should remain useful without positive action-boundary movement;
- local probing or greedy no-state behavior should win in independent-hidden and irrelevant controls.

This tests whether persistent action-boundary structure is present inside an end-to-end trained recurrent policy, not only in a supplied boundary-policy candidate set.

Implemented version:

- [end-to-end boundary probe script](../experiments/end_to_end_boundary_probe.py)
- [end-to-end boundary probe report](48_end_to_end_boundary_probe_report.md)
- [summary CSV](../artifacts/end_to_end_boundary_probe_summary.csv)
- [training CSV](../artifacts/end_to_end_boundary_probe_training.csv)
- [boundary CSV](../artifacts/end_to_end_boundary_probe_boundary.csv)
- [verdict CSV](../artifacts/end_to_end_boundary_probe_verdict.csv)
- [JSON results](../artifacts/end_to_end_boundary_probe_results.json)

## Supplemental Architecture Boundary Stress Test

Run an architecture boundary stress test.

This keeps the end-to-end boundary benchmark but trains each recurrent architecture independently. It asks whether `sum_rnn`, `scalar_rnn`, and `two_unit_rnn` converge on the same boundary signature rather than letting the best architecture hide failures in the others.

Current expected result:

- shared regimes should show partial architecture convergence, not strict convergence;
- the `sum_rnn` architecture should recover the expected shared boundary signatures;
- independent-hidden and irrelevant controls should reject shared recurrence across all architectures.

This is a negative stress test for the strong Attractor Test. It documents that the current toy stack has not yet shown architecture-independent convergence.

Implemented version:

- [architecture boundary stress script](../experiments/architecture_boundary_stress.py)
- [architecture boundary stress report](49_architecture_boundary_stress_report.md)
- [summary CSV](../artifacts/architecture_boundary_stress_summary.csv)
- [verdict CSV](../artifacts/architecture_boundary_stress_verdict.csv)
- [JSON results](../artifacts/architecture_boundary_stress_results.json)

## Supplemental Architecture Horizon-Pressure Sweep

Run an architecture horizon-pressure sweep.

This keeps the architecture stress setup but varies horizon across `2,4,8,16`. It asks whether longer temporal dependence makes independently trained recurrent architectures converge on the same boundary abstraction.

Current expected result:

- shared regimes should become recoverable as horizon increases;
- strict architecture-wide convergence should still fail;
- independent-hidden and irrelevant controls should continue rejecting shared recurrence.

This tests whether temporal pressure helps with the architecture-dependence failure without pretending it solves the full Attractor Test.

Implemented version:

- [architecture horizon-pressure script](../experiments/architecture_horizon_pressure_sweep.py)
- [architecture horizon-pressure report](50_architecture_horizon_pressure_report.md)
- [summary CSV](../artifacts/architecture_horizon_pressure_summary.csv)
- [verdict CSV](../artifacts/architecture_horizon_pressure_verdict.csv)
- [JSON results](../artifacts/architecture_horizon_pressure_results.json)

## Supplemental Architecture Capacity Probe

Run an architecture capacity probe.

This keeps the architecture stress setup but supplies a small seed family of source-direction recurrent candidates. It asks whether `scalar_rnn` and `two_unit_rnn` fail because they lack representational capacity or because random-start training fails to find useful parameters.

Current expected result:

- all architectures should recover the expected shared-boundary signatures when useful source-direction seeds are supplied;
- independent-hidden and irrelevant controls should still reject shared recurrence or hidden state;
- the result should be interpreted as capacity evidence, not natural emergence.

Implemented version:

- [architecture capacity probe script](../experiments/architecture_capacity_probe.py)
- [architecture capacity probe report](51_architecture_capacity_probe_report.md)
- [summary CSV](../artifacts/architecture_capacity_probe_summary.csv)
- [verdict CSV](../artifacts/architecture_capacity_probe_verdict.csv)
- [JSON results](../artifacts/architecture_capacity_probe_results.json)

## Supplemental Architecture Soft-Return Optimizer

Run an architecture soft-return optimizer.

This keeps the architecture stress setup but removes the source-direction seed family from the capacity probe. Each recurrent architecture is optimized from Gaussian starts with cross-entropy search ranked mainly by a smooth expected-return surrogate, with a small realized-return term, selected by optimizer objective rather than expected boundary signature, then tested with the same end-to-end boundary classifier.

Current expected result:

- all architectures should recover the expected shared-boundary signatures without supplied source-direction seeds;
- independent-hidden and irrelevant controls should still reject shared recurrence or hidden state;
- the result should be interpreted as a narrow discovery result for a toy optimizer, not as full online RL.

Implemented version:

- [architecture soft-return optimizer script](../experiments/architecture_soft_return_optimizer.py)
- [architecture soft-return optimizer report](52_architecture_soft_return_optimizer_report.md)
- [summary CSV](../artifacts/architecture_soft_return_optimizer_summary.csv)
- [verdict CSV](../artifacts/architecture_soft_return_optimizer_verdict.csv)
- [JSON results](../artifacts/architecture_soft_return_optimizer_results.json)

## Supplemental Architecture Hard-Return Audit

Run an architecture hard-return audit.

This keeps the architecture soft-return setup but removes the smooth expected-return surrogate. Candidate weights and restarts are selected only by realized recurrent training return, then tested with the same end-to-end boundary classifier.

Current expected result:

- hard return should keep independent-hidden and irrelevant controls clean;
- hard return should find useful recurrent control in shared regimes;
- strict architecture-wide boundary convergence is not expected under this objective alone.

Implemented version:

- [architecture hard-return audit script](../experiments/architecture_hard_return_audit.py)
- [architecture hard-return audit report](53_architecture_hard_return_audit_report.md)
- [summary CSV](../artifacts/architecture_hard_return_audit_summary.csv)
- [verdict CSV](../artifacts/architecture_hard_return_audit_verdict.csv)
- [JSON results](../artifacts/architecture_hard_return_audit_results.json)

## Supplemental Architecture Hard-Return Horizon Sweep

Run an architecture hard-return horizon sweep.

This keeps the hard-return audit objective but varies horizon across `2,4,8,16` under a bounded optimizer budget. It asks whether temporal pressure repairs the self/tool boundary failure seen under realized-return-only optimization.

Current expected result:

- self and detachable regimes should improve from no recovery to partial recovery, not strict convergence;
- passive-world recurrence should become strictly recoverable;
- independent-hidden and irrelevant controls should stay clean.

Implemented version:

- [architecture hard-return horizon script](../experiments/architecture_hard_return_horizon_sweep.py)
- [architecture hard-return horizon report](54_architecture_hard_return_horizon_report.md)
- [summary CSV](../artifacts/architecture_hard_return_horizon_summary.csv)
- [verdict CSV](../artifacts/architecture_hard_return_horizon_verdict.csv)
- [JSON results](../artifacts/architecture_hard_return_horizon_results.json)

## Supplemental Architecture Online Return-Learner Audit

Run an architecture online return-learner audit.

This replaces batch cross-entropy hard-return search with an online-style antithetic perturbation learner. Weight updates, restart selection, and policy selection use realized return only. The same end-to-end boundary classifier is applied after training.

Current expected result:

- independent-hidden and irrelevant controls should remain clean;
- shared regimes should show useful return learning but not strict architecture-wide boundary convergence;
- failures should distinguish high-return hidden-state control from self-equivalent boundary discovery.

Implemented version:

- [architecture online return-learner script](../experiments/architecture_online_return_learner.py)
- [architecture online return-learner report](55_architecture_online_return_learner_report.md)
- [summary CSV](../artifacts/architecture_online_return_learner_summary.csv)
- [verdict CSV](../artifacts/architecture_online_return_learner_verdict.csv)
- [JSON results](../artifacts/architecture_online_return_learner_results.json)

## Supplemental Architecture Policy-Gradient Learner

Run an architecture policy-gradient learner.

This keeps the same boundary benchmark but replaces perturbation-only online updates with a stochastic recurrent policy trained by score-function gradients from sampled episode return. Restarts are selected by sampled validation return, then the same end-to-end boundary classifier is applied after training.

Current expected result:

- shared regimes should recover strict boundary convergence across recurrent architectures;
- independent-hidden control should select local probing;
- irrelevant-hidden control should select greedy no-state action.

Implemented version:

- [architecture policy-gradient learner script](../experiments/architecture_policy_gradient_learner.py)
- [architecture policy-gradient learner report](56_architecture_policy_gradient_learner_report.md)
- [summary CSV](../artifacts/architecture_policy_gradient_learner_summary.csv)
- [verdict CSV](../artifacts/architecture_policy_gradient_learner_verdict.csv)
- [JSON results](../artifacts/architecture_policy_gradient_learner_results.json)

## Supplemental Architecture Policy-Gradient Seed Sweep

Run an architecture policy-gradient seed sweep.

This repeats the policy-gradient learner across independent seeds and reports strict convergence by seed. It asks whether the positive policy-gradient result is robust or merely one successful seed.

Current expected result:

- shared regimes should show partial, not seed-stable, strict convergence;
- independent-hidden and irrelevant controls should stay strict across every seed;
- the result should distinguish recoverability from an architecture-independent attractor law.

Implemented version:

- [architecture policy-gradient seed-sweep script](../experiments/architecture_policy_gradient_seed_sweep.py)
- [architecture policy-gradient seed-sweep report](57_architecture_policy_gradient_seed_sweep_report.md)
- [summary CSV](../artifacts/architecture_policy_gradient_seed_sweep_summary.csv)
- [verdict CSV](../artifacts/architecture_policy_gradient_seed_sweep_verdict.csv)
- [JSON results](../artifacts/architecture_policy_gradient_seed_sweep_results.json)

## Supplemental Architecture Policy-Gradient Budget Sweep

Run an architecture policy-gradient budget sweep.

This repeats the seed-sweep audit under a standard and a larger policy-gradient budget. It asks whether report 57's seed instability is an optimization-budget artifact or a more persistent failure of convergence.

Current expected result:

- larger budgets should repair some shared-regime seed failures;
- independent-hidden and irrelevant controls should remain strict across every budget and seed;
- any remaining shared-regime failures should identify the boundary distinction still hardest for the learner.

Implemented version:

- [architecture policy-gradient budget-sweep script](../experiments/architecture_policy_gradient_budget_sweep.py)
- [architecture policy-gradient budget-sweep report](58_architecture_policy_gradient_budget_sweep_report.md)
- [summary CSV](../artifacts/architecture_policy_gradient_budget_sweep_summary.csv)
- [verdict CSV](../artifacts/architecture_policy_gradient_budget_sweep_verdict.csv)
- [JSON results](../artifacts/architecture_policy_gradient_budget_sweep_results.json)

## Supplemental Architecture Torch Actor-Critic Learner

Run a Torch recurrent actor-critic learner.

This replaces the score-function toy policy with PyTorch `RNN`, `GRU`, and `LSTM` actor-critic learners trained from sampled episode return. It uses Apple Silicon MPS when available and applies the same post-training causal boundary classifier to policy logits.

Current expected result:

- shared regimes should recover strict boundary convergence across Torch recurrent architectures;
- detachable-tool recurrence should be separated from persistent agent-boundary recurrence;
- independent-hidden and irrelevant controls should stay clean.

Implemented version:

- [architecture Torch actor-critic script](../experiments/architecture_torch_actor_critic.py)
- [architecture Torch actor-critic report](59_architecture_torch_actor_critic_report.md)
- [summary CSV](../artifacts/architecture_torch_actor_critic_summary.csv)
- [verdict CSV](../artifacts/architecture_torch_actor_critic_verdict.csv)
- [JSON results](../artifacts/architecture_torch_actor_critic_results.json)

## Supplemental SSRM-3D Embodied World

Run a persistent 3D embodied-world precursor.

This moves the pressure stack into a continuous world with terrain, resources, hazards, shelter, weather, day/night change, commitments, subsystem conflict, and a simple social competitor. The architecture is layered: reflex, perception, self-state, attention, arbiter, slow language module, and action. The language module receives compressed state packets and never directly controls motor behavior.

The simulator may count ticks, but the intended architecture is rate based: high-frequency reflex and physics loops, medium-rate perception and attention, slower self-state and goal arbitration, and very slow or event-triggered language and memory layers. Ticks are implementation. Rates are the control model.

Current expected result:

- self-state should not be required in the low-pressure spatial stage;
- reusable self-state latents should become more useful as hidden energy, body drift, delayed options, commitments, arbitration, and social pressure accumulate;
- ablation should damage the layered agent once the self-state workspace is reused across several control contexts;
- reactive control may remain competitive in early stages, keeping the pressure-gradient claim falsifiable.

Implemented version:

- [SSRM-3D script](../experiments/ssrm_3d_embodied_world.py)
- [SSRM-3D report](60_ssrm_3d_embodied_world_report.md)
- [SSRM-3D visualization](../visualizations/ssrm_3d.html)
- [summary CSV](../artifacts/ssrm_3d_summary.csv)
- [episode metrics CSV](../artifacts/ssrm_3d_episode_metrics.csv)
- [verdict CSV](../artifacts/ssrm_3d_verdict.csv)
- [trajectory JSON](../artifacts/ssrm_3d_trajectory.json)
- [JSON results](../artifacts/ssrm_3d_results.json)

## Supplemental SSRM-3D Recurrent Observer

Run a GPU-backed recurrent-observer precursor on SSRM-3D traces.

This removes the hand-built self-state workspace from the measured representation. The trace generator is still SSRM-3D, but the observer receives action-observation packets and must learn hidden state useful for future viability prediction.

Current expected result:

- body state may be decodable even in the low-pressure spatial stage, but recurrence should add little there;
- recurrent observers should recover stronger self-state than a frame-only model once hidden energy, body drift, delayed options, commitments, arbitration, and social pressure accumulate;
- counterfactual edits along the learned self-state direction should move future-viability prediction;
- self-subspace ablation should be reported as a stricter causal check, not hidden inside the verdict.

Implemented version:

- [SSRM-3D recurrent observer script](../experiments/ssrm_3d_recurrent_observer.py)
- [SSRM-3D recurrent observer report](61_ssrm_3d_recurrent_observer_report.md)
- [summary CSV](../artifacts/ssrm_3d_recurrent_observer_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_recurrent_observer_verdict.csv)
- [JSON results](../artifacts/ssrm_3d_recurrent_observer_results.json)

## Supplemental SSRM-3D Learned Controller

Run a GPU-backed learned-controller precursor in SSRM-3D.

This trains frame-only and recurrent controllers from return-weighted behavior cloning plus future-return prediction. The learner receives no self labels. The resulting policy states are then probed for self-state variables and rolled back into the SSRM-3D world.

Current expected result:

- learned recurrence should not be needed in the low-pressure spatial stage;
- recurrent controllers should outperform frame-only controllers as hidden energy, body drift, delayed options, commitments, arbitration, and social pressure accumulate;
- recurrent policy states should contain decodable energy, integrity, mobility, and sensor capability under pressure;
- direct counterfactual self-state edits may remain weak, which should be reported as a remaining causal-control gap.

Implemented version:

- [SSRM-3D learned controller script](../experiments/ssrm_3d_learned_controller.py)
- [SSRM-3D learned controller report](62_ssrm_3d_learned_controller_report.md)
- [summary CSV](../artifacts/ssrm_3d_learned_controller_summary.csv)
- [evaluation CSV](../artifacts/ssrm_3d_learned_controller_eval.csv)
- [verdict CSV](../artifacts/ssrm_3d_learned_controller_verdict.csv)
- [JSON results](../artifacts/ssrm_3d_learned_controller_results.json)

## SSRM-3D Done-Enough Gates

Use the SSRM-3D gate document as the current stopping rule for the embodied track:

- [SSRM-3D done-enough gates](63_ssrm_3d_done_enough_gates.md)

The four gates are:

- learned control;
- tool-making or externalized cognition;
- real social pressure;
- targeted ablation.

Current status:

- gate 1 has a useful learned-controller precursor, but direct self-edit action effects remain weak;
- gate 2 has a partial return-selected externalized-cognition precursor;
- gate 3 has partial return-selected social-pressure and costly-communication precursors;
- gate 4 has self-state, learned-observer, tool-access, communication, continuity-record, and packet-level learned-integration precursors, but lacks full-world attention-mixing, continuity-memory, LLM-stream, and tool-access ablations in the embodied learned-control setting.

The proposed attention-buffer capacity sweep belongs after those gates start to exist, or as a targeted gate-4 study of attention mixing. It should be treated as an internal bandwidth hypothesis, not as evidence for consciousness or a special 12-dimensional world.

## Supplemental SSRM-3D Tool-Making

Run a return-selected tool-making precursor in SSRM-3D.

The world exposes simple build/place affordances: route markers, shelter/resource beacons, hazard alarms, and energy caches. Policies are selected by episode return, not by a tool-use label. The selected policy is then evaluated with tool access ablated.

Current expected result:

- tools should not be selected in the visible-resource control;
- tools should be selected under hidden-route, degraded-sensor, and interruption-recovery pressure;
- removing tool access from the selected policy should remove most of the gain;
- tool spam and cache-only access should not be overclaimed as successes.

Implemented version:

- [SSRM-3D tool-making script](../experiments/ssrm_3d_tool_making.py)
- [SSRM-3D tool-making report](65_ssrm_3d_tool_making_report.md)
- [tool-making visualization](../visualizations/ssrm_3d_tool_making.html)
- [evaluation CSV](../artifacts/ssrm_3d_tool_making_eval.csv)
- [policy-selection CSV](../artifacts/ssrm_3d_tool_making_policy_selection.csv)
- [summary CSV](../artifacts/ssrm_3d_tool_making_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_tool_making_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_tool_making_trace.json)
- [JSON results](../artifacts/ssrm_3d_tool_making_results.json)

## Supplemental SSRM-3D Social Pressure

Run a return-selected social-pressure precursor in SSRM-3D.

Other agents have persistent identity, resource need, trust toward the tested agent, and simple role policies: helper, trader, opportunist, and deceiver. Policies are selected by episode return, not by a social-label objective. The selected policy is then evaluated with identity memory, social self-state, and tool access ablated.

Current expected result:

- social machinery should not be selected in the visible-resource control;
- social identity should be selected under cooperative repair, opportunist vulnerability, deceptive route, and shared-tool conflict pressure;
- removing identity memory should damage cooperation, deception resistance, and shared-tool trust;
- removing social self-state should damage vulnerability handling, reputation-sensitive repair, and commitment completion;
- removing shared-tool access should produce a specific failure in the shared-tool conflict stage.

Implemented version:

- [SSRM-3D social-pressure script](../experiments/ssrm_3d_social_pressure.py)
- [SSRM-3D social-pressure report](66_ssrm_3d_social_pressure_report.md)
- [social-pressure visualization](../visualizations/ssrm_3d_social_pressure.html)
- [evaluation CSV](../artifacts/ssrm_3d_social_pressure_eval.csv)
- [policy-selection CSV](../artifacts/ssrm_3d_social_pressure_policy_selection.csv)
- [summary CSV](../artifacts/ssrm_3d_social_pressure_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_social_pressure_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_social_pressure_trace.json)
- [trace JS fallback](../artifacts/ssrm_3d_social_pressure_trace.js)
- [JSON results](../artifacts/ssrm_3d_social_pressure_results.json)

## Supplemental SSRM-3D Social Ecology

Run a costly-communication precursor in SSRM-3D.

Communication has explicit time, energy, and opportunity costs. Policies are not rewarded for talking. They are selected only by episode return, then tested with signal, name, gossip, and check-in ablations.

Current expected result:

- communication should be rejected when resources are visible and no social information advantage exists;
- warning signals should be selected only when transferred route information beats rediscovery;
- identity names should be selected only when persistent social history matters;
- gossip should be selected only when absent-agent information improves future decisions;
- check-ins should be selected only when low-cost contact maintains trust, repair, shared-tool access, or future options;
- babble should lose return when communication has no control job.

Implemented version:

- [SSRM-3D social-ecology script](../experiments/ssrm_3d_social_ecology.py)
- [SSRM-3D social-ecology report](67_ssrm_3d_social_ecology_report.md)
- [social-ecology visualization](../visualizations/ssrm_3d_social_ecology.html)
- [evaluation CSV](../artifacts/ssrm_3d_social_ecology_eval.csv)
- [policy-selection CSV](../artifacts/ssrm_3d_social_ecology_policy_selection.csv)
- [summary CSV](../artifacts/ssrm_3d_social_ecology_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_social_ecology_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_social_ecology_trace.json)
- [JSON results](../artifacts/ssrm_3d_social_ecology_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_social_ecology_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_social_ecology_results.js)

## Supplemental SSRM-3D Agent Continuity

Run an AgentContinuityRecord precursor in SSRM-3D.

The ML model is not continuity by itself. Memory is not continuity by itself. Body state is not continuity by itself. This experiment tests continuity as a serialized binding record across body, model, memory, social history, commitments, event log, attention state, hidden state, tools, goals, and fork branch identity.

Current expected result:

- full continuity record should preserve control after pause/resume;
- model-only copies should fail when memory, body, social history, or commitments matter;
- memory-only transplants should fail when body/model/hidden state are incompatible;
- social-memory reset should hurt repair and trust regimes specifically;
- commitment-ledger reset should hurt unfinished obligations;
- tool-inventory reset should hurt externalized-cognition commitments;
- fork without branch identity should create rollback or duplicate-commitment conflict;
- clean forks should share history before the fork and become separate continuities afterward.

Implemented version:

- [SSRM-3D agent-continuity script](../experiments/ssrm_3d_agent_continuity.py)
- [SSRM-3D agent-continuity report](68_ssrm_3d_agent_continuity_report.md)
- [agent-continuity visualization](../visualizations/ssrm_3d_agent_continuity.html)
- [evaluation CSV](../artifacts/ssrm_3d_agent_continuity_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_agent_continuity_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_agent_continuity_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_agent_continuity_trace.json)
- [JSON results](../artifacts/ssrm_3d_agent_continuity_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_agent_continuity_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_agent_continuity_results.js)

## Supplemental SSRM-3D Learned Integration Controller

Run a learned-controller integration precursor in SSRM-3D.

The previous tool, social, communication, and continuity experiments mostly used return-selected candidate policies or explicit restore records. This experiment trains a frame-only policy and a recurrent policy from reward-derived action choices over compressed state-packet traces, then ablates tool, social, continuity, and attention feature groups after training.

Current expected result:

- visible-resource control should not need recurrent memory or special channels;
- tool-route pressure should favor recurrent policy state and fail under tool-channel ablation;
- social-repair pressure should fail under social-channel ablation;
- continuity-restore pressure should fail under continuity-channel ablation;
- integrated gate pressure should fail under attention-channel ablation and show smaller losses under tool/social/continuity ablations.

Canonical result:

- local tool, social, continuity, and integrated rows support a designed packet bridge in the seeded canonical run;
- the result remains provisional because scenario identity and feature groups are supplied;
- the no-leak follow-up removes scenario identity leakage, randomizes pressure combinations, runs five seeds, and finds a partial negative: social and continuity bridges mostly survive, but `single_tool` margins are too close and `integrated_social` is not stable.

Implemented version:

- [SSRM-3D learned-integration script](../experiments/ssrm_3d_learned_integration_controller.py)
- [SSRM-3D learned-integration report](69_ssrm_3d_learned_integration_controller_report.md)
- [learned-integration visualization](../visualizations/ssrm_3d_learned_integration.html)
- [evaluation CSV](../artifacts/ssrm_3d_learned_integration_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_learned_integration_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_learned_integration_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_learned_integration_trace.json)
- [JSON results](../artifacts/ssrm_3d_learned_integration_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_learned_integration_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_learned_integration_results.js)

## Supplemental SSRM-3D No-Leak Integration Sweep

Run the Report 69 attack directly.

This experiment keeps the packet-controller frame but removes scenario-id input features, randomizes pressure combinations, splits integrated verdicts by priority metadata, runs five seeds, and requires margins that do not sit on the threshold.

Canonical result:

- control remains clean;
- local social and continuity pass robustly;
- integrated tool and integrated continuity pass;
- `single_tool` fails the widened margin requirement;
- `integrated_social` is not seed/ablation stable;
- the strong no-leak randomized integration claim is not supported.

Implemented version:

- [SSRM-3D no-leak integration script](../experiments/ssrm_3d_no_leak_integration_sweep.py)
- [SSRM-3D no-leak integration report](73_ssrm_3d_no_leak_integration_sweep_report.md)
- [no-leak integration visualization](../visualizations/ssrm_3d_no_leak_integration.html)
- [evaluation CSV](../artifacts/ssrm_3d_no_leak_integration_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_no_leak_integration_summary.csv)
- [seed verdict CSV](../artifacts/ssrm_3d_no_leak_integration_seed_verdict.csv)
- [verdict CSV](../artifacts/ssrm_3d_no_leak_integration_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_no_leak_integration_trace.json)
- [JSON results](../artifacts/ssrm_3d_no_leak_integration_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_no_leak_integration_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_no_leak_integration_results.js)

## SSRM-3D Structured Perception Pressure

Run the first persistent-pressure layer from report 74.

This experiment uses structured cone/FOV vision and spatial audio events rather than omniscient world state, raw pixels, or raw waveforms. It asks whether partial perception creates specific pressure for memory, tools, attention, and self-state adaptation.

Canonical result:

- open daylight control rejects perception machinery;
- cone-vision route memory fails under no-vision and visual-memory ablation;
- occluded hazard pressure fails under no-audio, no-direction audio, and tool-alarm ablation;
- night shelter pressure needs multimodal perception and memory;
- sensor-damage pressure fails when perception is blind to body-state degradation.

Implemented version:

- [SSRM-3D structured-perception script](../experiments/ssrm_3d_structured_perception.py)
- [SSRM-3D structured-perception report](75_ssrm_3d_structured_perception_report.md)
- [structured-perception visualization](../visualizations/ssrm_3d_structured_perception.html)
- [evaluation CSV](../artifacts/ssrm_3d_structured_perception_eval.csv)
- [policy-selection CSV](../artifacts/ssrm_3d_structured_perception_policy_selection.csv)
- [summary CSV](../artifacts/ssrm_3d_structured_perception_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_structured_perception_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_structured_perception_trace.json)
- [JSON results](../artifacts/ssrm_3d_structured_perception_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_structured_perception_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_structured_perception_results.js)

## SSRM-3D Day/Night Sleep-Rest Pressure

Run the second persistent-pressure layer from report 74.

This experiment treats sleep/rest as a vulnerable control action. It asks whether rest is useful only when fatigue, darkness, shelter timing, alarms, social watch, or interruption continuity change future capability.

Canonical result:

- open daylight control rejects rest;
- long-horizon fatigue fails under no-rest and no-fatigue-state ablations;
- night shelter pressure fails under no-day/night-state and no-shelter-memory ablations;
- guarded sleep pressure fails under no-alarm-tools and no-social-watch ablations;
- interrupted commitment pressure fails under no-continuity, no-rest, and no-fatigue-state ablations.

Implemented version:

- [SSRM-3D day/night sleep-rest script](../experiments/ssrm_3d_day_night_sleep.py)
- [SSRM-3D day/night sleep-rest report](76_ssrm_3d_day_night_sleep_report.md)
- [day/night sleep-rest visualization](../visualizations/ssrm_3d_day_night_sleep.html)
- [evaluation CSV](../artifacts/ssrm_3d_day_night_sleep_eval.csv)
- [policy-selection CSV](../artifacts/ssrm_3d_day_night_sleep_policy_selection.csv)
- [summary CSV](../artifacts/ssrm_3d_day_night_sleep_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_day_night_sleep_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_day_night_sleep_trace.json)
- [JSON results](../artifacts/ssrm_3d_day_night_sleep_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_day_night_sleep_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_day_night_sleep_results.js)

## SSRM-3D Illness/Sanitation Pressure

Run the third persistent-pressure layer from report 74.

This experiment treats hunger, thirst, illness, contamination, sanitation, care, quarantine, immunity, and continuity as abstract control variables. It asks whether delayed internal risk and social exposure consequences create specific self-state pressure.

Canonical result:

- clean resource control rejects health machinery;
- delayed hunger/thirst fails under no-hunger-thirst-state ablation;
- latent illness attribution fails under no-illness-state and symptom-reactive-only ablations;
- contaminated shelter/water fails under no-contamination-map, no-sanitation-action, and no-clean-water-tool ablations;
- contagion pressure fails under no-care-quarantine ablation;
- restore pressure fails under no-immunity-memory and no-continuity ablations.

Implemented version:

- [SSRM-3D illness/sanitation script](../experiments/ssrm_3d_illness_sanitation.py)
- [SSRM-3D illness/sanitation report](77_ssrm_3d_illness_sanitation_report.md)
- [illness/sanitation visualization](../visualizations/ssrm_3d_illness_sanitation.html)
- [evaluation CSV](../artifacts/ssrm_3d_illness_sanitation_eval.csv)
- [policy-selection CSV](../artifacts/ssrm_3d_illness_sanitation_policy_selection.csv)
- [summary CSV](../artifacts/ssrm_3d_illness_sanitation_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_illness_sanitation_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_illness_sanitation_trace.json)
- [JSON results](../artifacts/ssrm_3d_illness_sanitation_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_illness_sanitation_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_illness_sanitation_results.js)

## SSRM-3D Weather/Exposure Pressure

Run the fourth persistent-pressure layer from report 74.

This experiment treats cold, heat, rain, wind, drought, shelter, fire/light, water planning, and continuity as abstract control variables. It asks whether external conditions become self-relevant only when they change the agent's own future capability.

Canonical result:

- mild clear control rejects weather machinery;
- cold/rain exposure fails under no-weather-state, no-exposure-state, no-shelter-memory, and no-fire-tools ablations;
- heat/drought pressure fails under no-water-planning and no-weather-state ablations;
- forecast storm pressure fails under no-weather-state, no-shelter-memory, no-fire-tools, and reactive-weather-only ablations;
- restore pressure fails under no-continuity, no-weather-state, no-shelter-memory, and no-fire-tools ablations.

Implemented version:

- [SSRM-3D weather/exposure script](../experiments/ssrm_3d_weather_exposure.py)
- [SSRM-3D weather/exposure report](78_ssrm_3d_weather_exposure_report.md)
- [weather/exposure visualization](../visualizations/ssrm_3d_weather_exposure.html)
- [evaluation CSV](../artifacts/ssrm_3d_weather_exposure_eval.csv)
- [policy-selection CSV](../artifacts/ssrm_3d_weather_exposure_policy_selection.csv)
- [summary CSV](../artifacts/ssrm_3d_weather_exposure_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_weather_exposure_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_weather_exposure_trace.json)
- [JSON results](../artifacts/ssrm_3d_weather_exposure_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_weather_exposure_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_weather_exposure_results.js)

## SSRM-3D Tool/Shelter Degradation Pressure

Run the fifth persistent-pressure layer from report 74.

This experiment treats marker wear, shelter damage, alarm/cache decay, inspection, repair, spare parts, and continuity as abstract control variables. It asks whether persistent infrastructure becomes self-relevant only when decay changes the agent's future capability.

Canonical result:

- stable new-tools control rejects maintenance machinery;
- route-marker decay fails under no-degradation-state, no-repair-action, no-tool-memory, and no-material-cache ablations;
- storm shelter wear fails under no-repair-action, no-shelter-memory, and no-material-cache ablations;
- alarm/cache wear fails under no-inspection-action, no-repair-action, no-tool-memory, and no-material-cache ablations;
- restore pressure fails under no-continuity plus tool, shelter, repair, and parts ablations.

Implemented version:

- [SSRM-3D tool/shelter degradation script](../experiments/ssrm_3d_tool_shelter_degradation.py)
- [SSRM-3D tool/shelter degradation report](79_ssrm_3d_tool_shelter_degradation_report.md)
- [tool/shelter degradation visualization](../visualizations/ssrm_3d_tool_shelter_degradation.html)
- [evaluation CSV](../artifacts/ssrm_3d_tool_shelter_degradation_eval.csv)
- [policy-selection CSV](../artifacts/ssrm_3d_tool_shelter_degradation_policy_selection.csv)
- [summary CSV](../artifacts/ssrm_3d_tool_shelter_degradation_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_tool_shelter_degradation_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_tool_shelter_degradation_trace.json)
- [JSON results](../artifacts/ssrm_3d_tool_shelter_degradation_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_tool_shelter_degradation_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_tool_shelter_degradation_results.js)

## SSRM-3D Social Trust/Contracts Pressure

Run the sixth persistent-pressure layer from report 74.

This experiment treats promises, tool return, hazard warnings, resource sharing, shelter repair debt, trust updates, ownership, communication, and continuity as abstract control variables. It asks whether contracts become self-relevant only when delayed social consequences change future access, help, tools, shelter safety, or social punishment.

Canonical result:

- visible no-contract control rejects contract machinery;
- borrowed-tool return fails under no-commitment, no-identity, no-communication, no-trust-update, and no-ownership ablations;
- hazard-warning promises fail under no-commitment, no-identity, no-communication, and no-trust-update ablations;
- reciprocal resource sharing fails under no-commitment, no-identity, no-communication, and no-trust-update ablations;
- shared shelter repair fails under no-repair-debt plus commitment, identity, communication, and trust ablations;
- restore pressure fails under no-continuity plus commitment, identity, ownership, repair-debt, communication, and trust ablations.

Implemented version:

- [SSRM-3D social trust/contracts script](../experiments/ssrm_3d_social_trust_contracts.py)
- [SSRM-3D social trust/contracts report](80_ssrm_3d_social_trust_contracts_report.md)
- [social trust/contracts visualization](../visualizations/ssrm_3d_social_trust_contracts.html)
- [evaluation CSV](../artifacts/ssrm_3d_social_trust_contracts_eval.csv)
- [policy-selection CSV](../artifacts/ssrm_3d_social_trust_contracts_policy_selection.csv)
- [summary CSV](../artifacts/ssrm_3d_social_trust_contracts_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_social_trust_contracts_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_social_trust_contracts_trace.json)
- [JSON results](../artifacts/ssrm_3d_social_trust_contracts_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_social_trust_contracts_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_social_trust_contracts_results.js)

## SSRM-3D Predator/Threat Agents Pressure

Run the seventh persistent-pressure layer from report 74.

This experiment treats trackers, threat perception, self-vulnerability state, sound/scent memory, stealth, shelter, alarms, social warning, fear-like control state, and continuity as abstract control variables. It asks whether threats become self-relevant only when they exploit the agent's own trace, weakness, routines, defenses, or restore-time forgetting.

Canonical result:

- open safe control rejects threat machinery;
- sound-tracking pressure fails under no-threat-perception, no-sound-scent-memory, no-stealth-action, and no-tool-alarm ablations;
- scent/weakness pressure fails under no-threat-perception, no-self-vulnerability-state, no-sound-scent-memory, no-stealth-action, and no-shelter-access ablations;
- routine ambush pressure fails under no-threat-perception, no-sound-scent-memory, no-stealth-action, and no-tool-alarm ablations;
- social group-defense pressure fails under no-social-warning plus shelter, alarm, self-vulnerability, and threat-perception ablations;
- restore pressure fails under no-continuity plus perception, vulnerability, trace, stealth, shelter, alarm, and social-warning ablations.

Implemented version:

- [SSRM-3D predator/threat agents script](../experiments/ssrm_3d_predator_threat_agents.py)
- [SSRM-3D predator/threat agents report](81_ssrm_3d_predator_threat_agents_report.md)
- [predator/threat agents visualization](../visualizations/ssrm_3d_predator_threat_agents.html)
- [evaluation CSV](../artifacts/ssrm_3d_predator_threat_agents_eval.csv)
- [policy-selection CSV](../artifacts/ssrm_3d_predator_threat_agents_policy_selection.csv)
- [summary CSV](../artifacts/ssrm_3d_predator_threat_agents_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_predator_threat_agents_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_predator_threat_agents_trace.json)
- [JSON results](../artifacts/ssrm_3d_predator_threat_agents_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_predator_threat_agents_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_predator_threat_agents_results.js)

## SSRM-3D Resource Ecology Pressure

Run the eighth persistent-pressure layer from report 74.

This experiment treats resource memory, regeneration/depletion, spoilage timing, migration tracking, restraint, cache management, sharing contracts, territory ownership, and continuity as abstract control variables. It asks whether resource ecology becomes self-relevant only when delayed resource consequences change the agent's own future viability or access.

Canonical result:

- abundant static control rejects ecology machinery;
- slow-regrowth pressure fails under no-resource-memory, no-regeneration-model, and no-restraint ablations;
- spoilage/cache pressure fails under no-resource-memory, no-spoilage-model, no-cache-management, and no-restraint ablations;
- migrating-source pressure fails under no-resource-memory, no-migration-tracking, and no-restraint ablations;
- shared-territory pressure fails under no-resource-memory, no-regeneration-model, no-restraint, no-sharing-contract, and no-territory-ownership ablations;
- restore pressure fails under no-continuity plus resource memory, regeneration, spoilage, migration, cache, sharing, and territory ablations.

Implemented version:

- [SSRM-3D resource ecology script](../experiments/ssrm_3d_resource_ecology.py)
- [SSRM-3D resource ecology report](82_ssrm_3d_resource_ecology_report.md)
- [resource ecology visualization](../visualizations/ssrm_3d_resource_ecology.html)
- [evaluation CSV](../artifacts/ssrm_3d_resource_ecology_eval.csv)
- [policy-selection CSV](../artifacts/ssrm_3d_resource_ecology_policy_selection.csv)
- [summary CSV](../artifacts/ssrm_3d_resource_ecology_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_resource_ecology_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_resource_ecology_trace.json)
- [JSON results](../artifacts/ssrm_3d_resource_ecology_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_resource_ecology_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_resource_ecology_results.js)

## SSRM-3D Injury/Disability Adaptation Pressure

Run the ninth persistent-pressure layer from report 74.

This experiment treats capability self-state, motor adaptation, sensor compensation, infection management, repair access, help-seeking, compensation tools, route adaptation, and continuity as abstract control variables. It asks whether injury/disability becomes self-relevant only when changed capability alters the agent's own future action feasibility, perception, social support, tools, routes, or restore-time control.

Canonical result:

- fixed-body control rejects disability machinery;
- limp/route pressure fails under no-capability-state, no-motor-adaptation, no-compensation-tools, and no-route-adaptation ablations;
- vision/hearing damage pressure fails under no-capability-state, no-sensor-compensation, no-compensation-tools, and no-route-adaptation ablations;
- wound infection pressure fails under no-capability-state, no-motor-adaptation, no-infection-management, and no-repair-access ablations;
- social help compensation pressure fails under no-capability-state, no-motor-adaptation, no-sensor-compensation, no-help-seeking, no-compensation-tools, and no-route-adaptation ablations;
- restore pressure fails under no-continuity plus capability, motor, sensor, infection, repair, help, tool, and route ablations.

Implemented version:

- [SSRM-3D injury/disability adaptation script](../experiments/ssrm_3d_injury_disability_adaptation.py)
- [SSRM-3D injury/disability adaptation report](83_ssrm_3d_injury_disability_adaptation_report.md)
- [injury/disability adaptation visualization](../visualizations/ssrm_3d_injury_disability_adaptation.html)
- [evaluation CSV](../artifacts/ssrm_3d_injury_disability_adaptation_eval.csv)
- [policy-selection CSV](../artifacts/ssrm_3d_injury_disability_adaptation_policy_selection.csv)
- [summary CSV](../artifacts/ssrm_3d_injury_disability_adaptation_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_injury_disability_adaptation_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_injury_disability_adaptation_trace.json)
- [JSON results](../artifacts/ssrm_3d_injury_disability_adaptation_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_injury_disability_adaptation_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_injury_disability_adaptation_results.js)

## SSRM-3D Development/Skill Learning Pressure

Run the tenth persistent-pressure layer from report 74.

This experiment treats skill memory, practice planning, capability self-state, fatigue management, injury adaptation, transfer modeling, teaching help, training tools, goal feasibility, and continuity as abstract control variables. It asks whether development/skill learning becomes self-relevant only when changing competence alters the agent's own future action feasibility.

Canonical result:

- easy fixed-skill control rejects skill machinery;
- practice/transfer pressure fails under no-skill-memory, no-practice-planning, no-capability-state, no-transfer-model, no-goal-feasibility, and fixed-skill baseline ablations;
- fatigue skill-degradation pressure fails under no-skill-memory, no-capability-state, no-fatigue-management, no-goal-feasibility, and fixed-skill baseline ablations;
- injury retraining pressure fails under no-skill-memory, no-practice-planning, no-capability-state, no-injury-adaptation, no-tool-training, and no-goal-feasibility ablations;
- teaching/tool transfer pressure fails under no-skill-memory, no-practice-planning, no-transfer-model, no-teaching-help, no-tool-training, and no-goal-feasibility ablations;
- restore pressure fails under no-continuity plus skill, practice, capability, fatigue, injury, transfer, teaching, tool, and feasibility ablations.

Implemented version:

- [SSRM-3D development/skill learning script](../experiments/ssrm_3d_development_skill_learning.py)
- [SSRM-3D development/skill learning report](84_ssrm_3d_development_skill_learning_report.md)
- [development/skill learning visualization](../visualizations/ssrm_3d_development_skill_learning.html)
- [evaluation CSV](../artifacts/ssrm_3d_development_skill_learning_eval.csv)
- [policy-selection CSV](../artifacts/ssrm_3d_development_skill_learning_policy_selection.csv)
- [summary CSV](../artifacts/ssrm_3d_development_skill_learning_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_development_skill_learning_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_development_skill_learning_trace.json)
- [JSON results](../artifacts/ssrm_3d_development_skill_learning_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_development_skill_learning_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_development_skill_learning_results.js)

## SSRM-3D Dependent Care Pressure

Run the eleventh persistent-pressure layer from report 74.

This experiment treats dependent state, identity memory, protection planning, resource sharing, repair care, teaching support, shelter coordination, promise commitments, social trust, priority arbitration, and continuity as abstract control variables. It asks whether dependent care becomes self-relevant only when another persistent vulnerable agent changes the tested agent's future options, obligations, resources, social access, or restore-time control.

Canonical result:

- no-dependent control rejects care machinery;
- fragile-companion protection pressure fails under no-dependent-state, no-identity-memory, no-protection-planning, no-shelter-coordination, no-priority-arbitration, and self-only ablations;
- resource-sharing pressure fails under no-dependent-state, no-identity-memory, no-resource-sharing, no-priority-arbitration, and self-only ablations;
- repair/teaching burden pressure fails under no-dependent-state, no-identity-memory, no-repair-care, no-teaching-support, no-priority-arbitration, and self-only ablations;
- promise/trust care pressure fails under no-dependent-state, no-identity-memory, no-resource-sharing, no-promise-commitment, no-social-trust, and no-priority-arbitration ablations;
- restore pressure fails under no-continuity plus dependent state, identity, protection, sharing, repair, teaching, shelter, promise, social trust, and priority ablations.

Implemented version:

- [SSRM-3D dependent care script](../experiments/ssrm_3d_dependent_care.py)
- [SSRM-3D dependent care report](85_ssrm_3d_dependent_care_report.md)
- [dependent care visualization](../visualizations/ssrm_3d_dependent_care.html)
- [evaluation CSV](../artifacts/ssrm_3d_dependent_care_eval.csv)
- [policy-selection CSV](../artifacts/ssrm_3d_dependent_care_policy_selection.csv)
- [summary CSV](../artifacts/ssrm_3d_dependent_care_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_dependent_care_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_dependent_care_trace.json)
- [JSON results](../artifacts/ssrm_3d_dependent_care_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_dependent_care_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_dependent_care_results.js)

## SSRM-3D Irreversible Loss Pressure

Run the twelfth persistent-pressure layer from report 74.

This experiment treats permanent tool loss, shelter loss, relationship loss, memory loss, value-at-risk estimation, replacement feasibility, caution control, loss response, and continuity as abstract control variables. It asks whether irreversible loss becomes self-relevant only when permanent future-option loss changes the tested agent's own risk tolerance, preservation actions, social access, memory state, or restore-time control.

Canonical result:

- reversible-wear control rejects irreversible-loss machinery;
- irreplaceable tool/shelter pressure fails under no-loss-memory, no-value-at-risk, no-replacement-model, no-caution-control, no-tool-preservation, no-shelter-preservation, and reckless baseline ablations;
- permanent relationship pressure fails under no-loss-memory, no-value-at-risk, no-caution-control, no-relationship-preservation, no-loss-response, and reckless baseline ablations;
- memory-archive loss pressure fails under no-loss-memory, no-value-at-risk, no-replacement-model, no-memory-backup, and reckless baseline ablations;
- cascading loss pressure fails under no-loss-memory, no-value-at-risk, no-replacement-model, no-caution-control, no-loss-response, and reckless baseline ablations;
- restore pressure fails under no-continuity plus loss memory, value-at-risk, replacement, caution, tool, shelter, relationship, memory-backup, and loss-response ablations.

Implemented version:

- [SSRM-3D irreversible loss script](../experiments/ssrm_3d_irreversible_loss.py)
- [SSRM-3D irreversible loss report](86_ssrm_3d_irreversible_loss_report.md)
- [irreversible loss visualization](../visualizations/ssrm_3d_irreversible_loss.html)
- [evaluation CSV](../artifacts/ssrm_3d_irreversible_loss_eval.csv)
- [policy-selection CSV](../artifacts/ssrm_3d_irreversible_loss_policy_selection.csv)
- [summary CSV](../artifacts/ssrm_3d_irreversible_loss_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_irreversible_loss_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_irreversible_loss_trace.json)
- [JSON results](../artifacts/ssrm_3d_irreversible_loss_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_irreversible_loss_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_irreversible_loss_results.js)

## SSRM-3D Affective Control Pressure

Run the thirteenth persistent-pressure layer from report 74.

This experiment treats fear, stress, trust, frustration, affiliation, curiosity, guilt analogue, attention mixing, memory salience, risk modulation, communication bias, and continuity as abstract control variables. It asks whether affective control becomes self-relevant only when compact internal summaries change the tested agent's attention, risk tolerance, social access, communication, repair, information seeking, memory salience, or restore-time control.

Canonical result:

- calm clear control rejects affective-control machinery;
- fear/hazard pressure fails under no-fear, no-attention, no-memory, no-risk, and no-affect ablations;
- stress/need-arbitration pressure fails under no-stress, no-attention, no-memory, no-risk, and no-affect ablations;
- trust/affiliation pressure fails under no-trust, no-affiliation, no-memory, no-communication, and no-affect ablations;
- frustration/curiosity pressure fails under no-frustration, no-curiosity, no-attention, no-memory, and no-affect ablations;
- guilt/commitment-repair pressure fails under no-guilt, no-trust, no-memory, no-communication, and no-affect ablations;
- restore pressure fails under no-affective-continuity plus fear, stress, trust, guilt, attention, memory, risk, and communication ablations.

Implemented version:

- [SSRM-3D affective control script](../experiments/ssrm_3d_affective_control.py)
- [SSRM-3D affective control report](87_ssrm_3d_affective_control_report.md)
- [affective control visualization](../visualizations/ssrm_3d_affective_control.html)
- [evaluation CSV](../artifacts/ssrm_3d_affective_control_eval.csv)
- [policy-selection CSV](../artifacts/ssrm_3d_affective_control_policy_selection.csv)
- [summary CSV](../artifacts/ssrm_3d_affective_control_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_affective_control_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_affective_control_trace.json)
- [JSON results](../artifacts/ssrm_3d_affective_control_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_affective_control_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_affective_control_results.js)

## SSRM-3D Physics-First Benchmark Foundation

Move the SSRM-3D track toward a physics-grounded inhabited world instead of another labeled pressure row.

This benchmark uses a modular C++ kernel for world construction, structured sensors, policy rollouts, deterministic stepping, and JSON serialization. Python owns compilation, neural training, held-out evaluation, ablations, metrics, and artifacts. The viewer consumes the same trace as a replay/intervention surface.

Canonical result:

- RNN, GRU, and LSTM recurrent neural models train on physics-derived sequences without scenario labels;
- held-out worlds are evaluated separately from training worlds;
- `gru` is the best canonical architecture at 0.855 held-out action accuracy;
- weather, user proposal, tool/social/continuity, and self-state ablations cause measurable losses;
- the verdict explicitly records `supports_closed_loop_deep_rl=False`;
- the viewer provides WASD movement, FOV cone, weather, sound/vibration rings, HUD, animation state, reason text, and intervention logging, but interventions do not yet feed back into a live learned agent.

Implemented version:

- [SSRM-3D physics benchmark script](../experiments/ssrm_3d_physics_benchmark.py)
- [SSRM-3D physics benchmark report](88_ssrm_3d_physics_benchmark_report.md)
- [C++ physics kernel](../cpp/ssrm_physics)
- [physics benchmark visualization](../visualizations/ssrm_3d_physics_benchmark.html)
- [architecture CSV](../artifacts/ssrm_3d_physics_benchmark_architectures.csv)
- [ablation CSV](../artifacts/ssrm_3d_physics_benchmark_ablations.csv)
- [baseline CSV](../artifacts/ssrm_3d_physics_benchmark_baselines.csv)
- [verdict CSV](../artifacts/ssrm_3d_physics_benchmark_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_physics_benchmark_trace.json)
- [JSON results](../artifacts/ssrm_3d_physics_benchmark_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_physics_benchmark_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_physics_benchmark_results.js)

## Modular LLM Architecture Boundary

Use the modular LLM architecture report as the control-authority contract for future SSRM-3D language work:

- [modular LLM architecture report](64_modular_llm_architecture_report.md)
- [modular LLM architecture visualization](../visualizations/modular_llm_architecture.html)

This is not a new positive experiment. It defines the expected ablation pattern:

- removing the LLM should hurt slow abstract planning, social explanation, tool-use proposals, and memory summarization more than reflex survival;
- direct LLM motor control should increase invalid actions, latency, hazard exposure, and recovery failures;
- compressed state packets should be tested against full-world language access;
- corrupting self-state should predictably corrupt language recommendations and arbiter decisions under embodied pressure.

This boundary should be specified in frequencies, not as one global cognitive tick. Example rates are `reflex_hz = 60`, `perception_hz = 10`, `attention_hz = 10`, `self_state_hz = 5`, `goal_hz = 2`, `reasoning_hz = 0.5`, and `memory_hz = 0.1`, with implementation intervals derived from the base simulator clock.

This belongs inside gate 4 once tool-making and richer social pressure are integrated into learned-controller runs.

## Sixteenth Minimal Experiment

Run a learned bottleneck discovery test.

The learner receives only unlabeled context/outcome samples. It chooses among:

- no hidden state needed;
- one shared bottleneck;
- local hidden variables.

Then a causal boundary probe tests whether the discovered shared structure belongs to the controlled system or to the external world.

Compare:

- no-hidden prior;
- shared bottleneck policy;
- task-local probe;
- learned model-selection policy;
- oracle.

Predictions:

- when one persistent agent-state controls outcomes, the learner should select a shared bottleneck and the boundary probe should classify it as agent-bounded;
- when one persistent external state controls outcomes, the learner should also select a shared bottleneck, but the boundary probe should classify it as external;
- when hidden variables are independent, the learner should select local hidden variables;
- when hidden state is irrelevant, the learner should select no hidden state.

This tests whether self-equivalent structure can be discovered without self labels while preserving the anti-tautology boundary against reusable world-state.

Implemented version:

- [learned bottleneck discovery script](../experiments/learned_bottleneck_discovery.py)
- [learned bottleneck discovery report](25_learned_bottleneck_discovery_report.md)
- [summary CSV](../artifacts/learned_bottleneck_discovery_summary.csv)
- [verdict CSV](../artifacts/learned_bottleneck_discovery_verdict.csv)
- [JSON results](../artifacts/learned_bottleneck_discovery_results.json)

## Seventeenth Minimal Experiment

Run a sequence latent transfer test.

The agent receives raw calibration outcomes in early contexts, then must act in held-out contexts. The latent is not named self, world, or body.

Compare hidden structures:

- one hidden agent-state controls all contexts;
- one hidden external state controls all contexts;
- each context has an independent hidden condition;
- no hidden state is needed.

Compare:

- marginal no-memory policy;
- calibration memory with no transfer;
- shared sequence filter;
- task-local probe;
- learned sequence selector;
- oracle.

Predictions:

- when one persistent agent-state controls all contexts, calibration outcomes should transfer through a shared sequence state and the boundary probe should classify it as agent-bounded;
- when one persistent external state controls all contexts, calibration outcomes should also transfer, but the boundary probe should classify it as external;
- when hidden variables are independent, local context probes should win;
- when hidden state is irrelevant, no hidden state should be selected.

This tests whether a reusable latent can be inferred from sequence evidence and transferred to new contexts without self labels.

Implemented version:

- [sequence latent transfer script](../experiments/sequence_latent_transfer.py)
- [sequence latent transfer report](26_sequence_latent_transfer_report.md)
- [summary CSV](../artifacts/sequence_latent_transfer_summary.csv)
- [verdict CSV](../artifacts/sequence_latent_transfer_verdict.csv)
- [JSON results](../artifacts/sequence_latent_transfer_results.json)

## Eighteenth Minimal Experiment

Run a heterogeneous attractor precursor.

Several learner families receive only raw calibration/outcome streams. They are not told whether the hidden structure is self-state, world-state, local hidden state, or no hidden state.

Compare learner families:

- Bayesian shared-state filter;
- predictive-state table;
- recurrent error-state update;
- evolutionary rule controller;
- bottleneck cluster model.

Compare hidden structures:

- one hidden agent capability controls all contexts;
- one hidden external gate controls all contexts;
- each context has an independent hidden condition;
- risky action always works.

Predictions:

- when one persistent agent-state controls outcomes, unrelated learner families should converge on an agent-bounded candidate latent;
- when one persistent external state controls outcomes, they should converge on an external candidate latent instead;
- when hidden variables are independent, shared self/world transfer should be rejected and local probing should win;
- when hidden state is irrelevant, no hidden state should be selected.

This tests whether convergence appears across several learner families while preserving the boundary that shared latent convergence alone is not selfhood.

Implemented version:

- [heterogeneous attractor precursor script](../experiments/heterogeneous_attractor_precursor.py)
- [heterogeneous attractor precursor report](27_heterogeneous_attractor_precursor_report.md)
- [summary CSV](../artifacts/heterogeneous_attractor_precursor_summary.csv)
- [verdict CSV](../artifacts/heterogeneous_attractor_precursor_verdict.csv)
- [JSON results](../artifacts/heterogeneous_attractor_precursor_results.json)

## Nineteenth Minimal Experiment

Run a cross-environment attractor precursor.

The experiment varies the environment surface while keeping the hidden-structure classes matched.

Environment families:

- body actuator control;
- homeostatic viability;
- sensor-frame recalibration;
- continuity and commitment recovery.

Compare hidden structures inside each family:

- one persistent agent-state controls all contexts;
- one persistent external world-state controls all contexts;
- each context has an independent hidden condition;
- no hidden state is needed.

Predictions:

- self-shared environments should converge on an agent-bounded candidate signature;
- world-shared environments should converge on an external candidate signature;
- independent-hidden environments should reject shared self/world structure and select local hidden variables;
- irrelevant controls should select no hidden state.

This tests whether the same causal boundary recurs across task surfaces, rather than only inside one environment family.

Implemented version:

- [cross-environment attractor script](../experiments/cross_environment_attractor.py)
- [cross-environment attractor report](28_cross_environment_attractor_report.md)
- [summary CSV](../artifacts/cross_environment_attractor_summary.csv)
- [environment verdict CSV](../artifacts/cross_environment_attractor_environment_verdict.csv)
- [scenario verdict CSV](../artifacts/cross_environment_attractor_scenario_verdict.csv)
- [JSON results](../artifacts/cross_environment_attractor_results.json)

## Twentieth Minimal Experiment

Run a factorial attractor precursor.

This combines two axes that were previously tested separately:

- learner-family variation;
- environment-surface variation.

Learner families:

- Bayesian shared-state filter;
- predictive-state table;
- recurrent error-state update;
- evolutionary rule controller;
- bottleneck cluster model.

Environment families:

- body actuator control;
- homeostatic viability;
- sensor-frame recalibration;
- continuity and commitment recovery.

Predictions:

- if hidden agent-state controls all contexts, most learner families should converge on an agent-bounded candidate signature in every environment;
- if hidden external state controls all contexts, they should converge on an external candidate signature instead;
- if hidden variables are independent, shared self/world structure should be rejected and task-local probing should win;
- if hidden state is irrelevant, learners should collapse to no hidden state.

This is the strongest current precursor because it varies learners and environment surfaces at the same time while preserving matched negative controls.

Implemented version:

- [factorial attractor test script](../experiments/factorial_attractor_test.py)
- [factorial attractor test report](29_factorial_attractor_test_report.md)
- [learner summary CSV](../artifacts/factorial_attractor_summary.csv)
- [baseline CSV](../artifacts/factorial_attractor_baselines.csv)
- [environment verdict CSV](../artifacts/factorial_attractor_environment_verdict.csv)
- [scenario verdict CSV](../artifacts/factorial_attractor_scenario_verdict.csv)
- [JSON results](../artifacts/factorial_attractor_results.json)

## Twenty-First Minimal Experiment

Run a raw history learning precursor.

This removes compact calibration-outcome inputs. Learners receive only raw traces:

- context id;
- action type;
- reward value.

Learner families:

- reward-sign filter;
- raw sequence table;
- recurrent reward-state update;
- evolved reward-memory rule;
- reward bottleneck cluster.

Predictions:

- raw reward-history learners should recover agent-bounded candidates in self-shared environments;
- they should recover external candidates in world-shared environments;
- they should reject shared self/world structure when hidden variables are independent;
- they should collapse to no hidden state when all risky actions work.

This tests whether the attractor pattern still appears when the learner must infer from action-observation-reward traces rather than compact outcome labels.

Implemented version:

- [raw history learning script](../experiments/raw_history_learning.py)
- [raw history learning report](30_raw_history_learning_report.md)
- [learner summary CSV](../artifacts/raw_history_learning_summary.csv)
- [baseline CSV](../artifacts/raw_history_learning_baselines.csv)
- [environment verdict CSV](../artifacts/raw_history_learning_environment_verdict.csv)
- [scenario verdict CSV](../artifacts/raw_history_learning_scenario_verdict.csv)
- [JSON results](../artifacts/raw_history_learning_results.json)

## Twenty-Second Minimal Experiment

Run a delayed-return policy precursor.

This weakens the training signal again. Candidate memory policies observe early probe rewards, choose held-out actions, and are selected by delayed episode return after acting.

Policy families:

- return-threshold policy;
- return-table policy;
- recurrent return-state policy;
- evolved return-memory rule;
- return bottleneck policy.

Predictions:

- return-trained memory policies should recover agent-bounded candidates in self-shared environments;
- they should recover external candidates in world-shared environments;
- they should reject shared self/world structure when hidden variables are independent;
- they should collapse to no hidden state when all risky actions work.

This tests whether the pattern survives delayed return selection rather than supervised reward prediction.

Implemented version:

- [delayed return policy script](../experiments/delayed_return_policy.py)
- [delayed return policy report](31_delayed_return_policy_report.md)
- [policy summary CSV](../artifacts/delayed_return_policy_summary.csv)
- [baseline CSV](../artifacts/delayed_return_policy_baselines.csv)
- [environment verdict CSV](../artifacts/delayed_return_policy_environment_verdict.csv)
- [scenario verdict CSV](../artifacts/delayed_return_policy_scenario_verdict.csv)
- [JSON results](../artifacts/delayed_return_policy_results.json)

## Twenty-Third Minimal Experiment

Run an evolved recurrent policy precursor.

This replaces hand-enumerated delayed-return rules with small continuous recurrent controllers selected by episode return.

Architectures:

- scalar recurrent controller;
- gated scalar recurrent controller;
- two-unit recurrent controller.

Predictions:

- evolved recurrent controllers should recover agent-bounded candidates in self-shared environments;
- they should recover external candidates in world-shared environments;
- they should reject shared self/world structure when hidden variables are independent;
- they should collapse to no hidden state when all risky actions work.

This tests whether the attractor pattern appears inside learned recurrent hidden states rather than only in explicit rule tables.

Implemented version:

- [evolved recurrent policy script](../experiments/evolved_recurrent_policy.py)
- [evolved recurrent policy report](32_evolved_recurrent_policy_report.md)
- [policy summary CSV](../artifacts/evolved_recurrent_policy_summary.csv)
- [baseline CSV](../artifacts/evolved_recurrent_policy_baselines.csv)
- [environment verdict CSV](../artifacts/evolved_recurrent_policy_environment_verdict.csv)
- [scenario verdict CSV](../artifacts/evolved_recurrent_policy_scenario_verdict.csv)
- [JSON results](../artifacts/evolved_recurrent_policy_results.json)

## Twenty-Fourth Minimal Experiment

Run a gradient-trained recurrent policy precursor.

This keeps the same small recurrent controller family but optimizes recurrent parameters with finite-difference gradient ascent on differentiable expected episode return.

Architectures:

- scalar recurrent controller;
- gated scalar recurrent controller;
- two-unit recurrent controller.

Predictions:

- gradient-trained recurrent controllers should recover agent-bounded candidates in self-shared environments;
- they should recover external candidates in world-shared environments;
- they should reject shared self/world structure when hidden variables are independent;
- they should collapse to no hidden state when all risky actions work.

This tests whether the attractor pattern survives return-gradient optimization rather than random/evolutionary recurrent selection.

Implemented version:

- [gradient recurrent policy script](../experiments/gradient_recurrent_policy.py)
- [gradient recurrent policy report](33_gradient_recurrent_policy_report.md)
- [policy summary CSV](../artifacts/gradient_recurrent_policy_summary.csv)
- [baseline CSV](../artifacts/gradient_recurrent_policy_baselines.csv)
- [environment verdict CSV](../artifacts/gradient_recurrent_policy_environment_verdict.csv)
- [scenario verdict CSV](../artifacts/gradient_recurrent_policy_scenario_verdict.csv)
- [JSON results](../artifacts/gradient_recurrent_policy_results.json)

## Twenty-Fifth Minimal Experiment

Run a model-based planning precursor.

This separates learned representation from action choice. Planners first learn a reward model from probe histories, then choose held-out risky or safe actions by predicted value.

Planner families:

- tabular reward model keyed by probe history;
- linear belief reward model;
- recurrent belief reward model.

Predictions:

- model-based planners should recover agent-bounded candidates in self-shared environments;
- they should recover external candidates in world-shared environments;
- they should reject shared self/world structure when hidden variables are independent;
- they should collapse to no hidden state when all risky actions work.

This tests whether the attractor pattern survives learned reward modeling plus planning rather than direct policy selection.

Implemented version:

- [model-based planning script](../experiments/model_based_planning.py)
- [model-based planning report](34_model_based_planning_report.md)
- [planner summary CSV](../artifacts/model_based_planning_summary.csv)
- [baseline CSV](../artifacts/model_based_planning_baselines.csv)
- [environment verdict CSV](../artifacts/model_based_planning_environment_verdict.csv)
- [scenario verdict CSV](../artifacts/model_based_planning_scenario_verdict.csv)
- [JSON results](../artifacts/model_based_planning_results.json)

## Twenty-Sixth Minimal Experiment

Run a latent causal ablation precursor.

This tests whether the learned latent is behaviorally necessary. It trains model-based planners, evaluates them intact, then replaces their probe-derived latent with an unconditional marginal reward model.

Predictions:

- ablating agent-bounded shared latents should damage held-out control;
- ablating external shared latents should also damage control, but should not count as selfhood;
- independent-hidden controls should show no shared latent causal loss;
- irrelevant controls should show no hidden-state dependence.

This tests whether convergence evidence is causal rather than merely decodable.

Implemented version:

- [latent causal ablation script](../experiments/latent_causal_ablation.py)
- [latent causal ablation report](35_latent_causal_ablation_report.md)
- [ablation summary CSV](../artifacts/latent_causal_ablation_summary.csv)
- [environment verdict CSV](../artifacts/latent_causal_ablation_environment_verdict.csv)
- [scenario verdict CSV](../artifacts/latent_causal_ablation_scenario_verdict.csv)
- [JSON results](../artifacts/latent_causal_ablation_results.json)

## Twenty-Seventh Minimal Experiment

Run a counterfactual latent editing precursor.

This tests whether learned latents are directionally editable. It trains model-based planners, then forces the probe-derived latent to all-good or all-bad evidence before held-out planning.

Predictions:

- good edits should increase risky action and bad edits should suppress risky action in agent-shared environments;
- the same editability should appear in world-shared environments but should not count as selfhood;
- independent-hidden controls should show no shared counterfactual edit;
- irrelevant controls should show no hidden-state edit dependence.

This tests intervention validity rather than mere decodability or ablation loss.

Implemented version:

- [counterfactual latent editing script](../experiments/counterfactual_latent_editing.py)
- [counterfactual latent editing report](36_counterfactual_latent_editing_report.md)
- [editing summary CSV](../artifacts/counterfactual_latent_editing_summary.csv)
- [environment verdict CSV](../artifacts/counterfactual_latent_editing_environment_verdict.csv)
- [scenario verdict CSV](../artifacts/counterfactual_latent_editing_scenario_verdict.csv)
- [JSON results](../artifacts/counterfactual_latent_editing_results.json)
