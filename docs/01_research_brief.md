# Research Brief: Why a Self Exists

## Current Best Explanation

A self exists, in the minimal computational sense, when an adaptive controller benefits from modeling itself as a persistent hidden cause of future observations, future action effects, and future value.

The minimal self is not a little person inside the system. It is a compact latent abstraction that tracks:

- the system boundary: what is inside the controlled system versus outside it;
- the system dynamics: what actions this body or architecture can actually perform;
- internal viability variables: needs, degradation, fatigue, energy, damage, uncertainty, competence;
- action-conditioned prediction: which sensory changes were caused by the system's own action;
- continuity: which past and future states belong to the same controlled process.

In ordinary language this abstraction becomes "I". In engineering language it is a persistent agent-state model.

This does not mean every useful hidden variable is a self. Hidden-state tracking is the broad category. Selfhood begins only when the tracked state is agent-bounded, persistent, action-mediated, control/value relevant, counterfactually active, and reused across prediction or control. Identity-like selfhood additionally requires continuity binding across owned past, present, and projected future states.

## Why World-State-Only Is Sometimes Enough

No self is needed when:

- the task is short horizon;
- the agent is fixed and non-degrading;
- the world is fully observable;
- the reward depends only on external state;
- the controller can use a reactive policy;
- an external designer supplies all body and actuator state;
- a recurrent black-box policy stores all needed state implicitly and no self-equivalent factor is causally separable.

This matters because the hypothesis must not define selfhood so broadly that every memory, hidden world variable, or unused internal diagnostic counts as a self.

## When Self Becomes Useful

Self-representation becomes useful when the agent's own changing state is part of the causal structure of the task.

Examples:

- A robot with damaged limbs must infer whether failure comes from the terrain or from its own body.
- A homeostatic agent must choose actions based on hidden internal variables, not only visible world state.
- A goal selector must choose goals that are feasible for this agent, not merely valuable in the abstract.
- A long-horizon planner must reason about future versions of itself with different energy, damage, information, commitments, or capabilities.
- A multi-module agent must preserve coherence across conflicting goals, memories, and predictions.
- A mobile animal must distinguish externally caused sensory changes from self-generated sensory changes.
- A restored or forked agent must preserve which body, memories, social history, commitments, tools, event history, and branch identity belong to the same continuing control process.

In these settings, "me" is useful because it compresses many variables that jointly determine future control.

## Smallest Mechanism Set

The smallest candidate mechanism set is:

1. Boundary tracking: a partition between internal controllable state, sensory interface, active interface, and external state.
2. Persistent internal state: memory of agent variables that change more slowly than immediate observations.
3. Action-conditioned prediction: a forward model of how actions change sensory inputs and future agent state.
4. Error attribution: a comparator that separates "the world changed" from "I changed" or "I acted."
5. Viability/value coupling: future outcomes depend on future internal state.
6. Continuity binding: past, present, and projected future agent states are treated as one process for planning.
7. Cross-context reuse: the same agent-state estimate is used across different control contexts.
8. Optional coherence maintenance: higher-level arbitration when subsystems conflict.
9. Multi-rate control: fast reflex and motor loops remain separate from slower perception, self-state, goal, language, and memory loops.

Only the first five are likely needed for a minimal non-conscious self-equivalent. The later mechanisms may be needed for identity, narrative self, or the apparent continuity described in human phenomenology. Persistent internal state by itself is not enough; it must affect action, value, or future control.

## Hypothesis Revisions

### H1 - Self as Compression

Revised claim: self is a low-dimensional sufficient statistic over internal variables that would otherwise require long action-observation histories.

Prediction: under compression pressure, learned representations should form self-like bottlenecks when body state, competence, or viability variables affect future reward.

Falsifier: an equally compact world-only/history-only representation matches prediction and control across drift and damage.

Current evidence: representation search and architecture convergence both select action-effect components under self drift, but world/bias components under world drift.

Additional evidence: cross-context reuse shows a compression-style advantage when one self-state probe can be reused across goal choice, option preservation, and commitment action; task-local probing wins when hidden variables are independent.

The reuse-pressure sweep adds the expected gradient: shared self-state has no advantage over local probing with one context, then gains value as more contexts depend on the same hidden agent-state. The same curve belongs to world-state when the reusable variable is external.

The horizon-pressure sweep adds the time version of the same prediction: shared self-state has no advantage over local probing at one future step, then gains value as more future steps depend on the same hidden agent-state. External world-state has the same curve when the persistent variable is outside the agent.

The partial-observability sweep adds the evidence-quality version: shared self-belief becomes best only when noisy cues reveal a persistent hidden agent-state, while external hidden state, independent hidden steps, and irrelevant-hidden controls select world-belief, local probing, or no-state behavior.

The learned observation-filter precursor removes the supplied posterior equation. From noisy cue/outcome histories, the selector learns the agent-state cue in the self-hidden regime, the world-state cue in the external-hidden regime, local probing in independent-hidden control, and no-state greedy action when hidden state is irrelevant.

The recurrent observation-filter precursor replaces cue-count tables with small recurrent controllers. In self-hidden regimes, the selected recurrent state depends causally on the agent-state observation channel; in world-hidden regimes, the same recurrent dependency is external rather than self-equivalent.

The unseeded recurrent-filter precursor removes seeded accumulator candidates. Random-start recurrent search still finds the agent-state dependency in self-hidden regimes, the external dependency in world-hidden regimes, and rejects shared recurrence in independent or irrelevant controls.

The mixed-sensor recurrent precursor removes self-aligned input channels. Random-start recurrent search recovers the relevant latent source from mixed noisy sensors, and latent-source ablation separates agent-bounded from external dependencies.

The learned sensor-subspace precursor removes known-source ablation from the destructive intervention. A behaviorally relevant direction is learned in mixed sensor space from outcome variation; ablating that learned direction damages control in shared regimes, while boundary interventions still separate agent-bounded from external dependencies.

The active boundary-discovery precursor removes supplied boundary interventions from the classification step. It compares the outcome-predictive sensor direction with the direction produced by the agent's own diagnostic action; only the self-hidden regime aligns both directions.

The action-effect boundary probe adds the missing controllable-world negative control. A controllable external latent can be useful and action-controllable, but it is rejected as self-equivalent when it aligns with a tool action rather than the body/action-effect boundary.

The persistent action-boundary probe adds a transfer test. A detachable tool-like latent aligns with an action-effect direction in the present context but not in transfer, so it is rejected as self-equivalent despite being useful and controllable.

The return-selected boundary probe removes supervised outcome-direction extraction. It proposes action-boundary policies from action-observation deltas and lets training return choose among persistent boundary, transient boundary, recurrent filtering, local probing, and no-state control.

The end-to-end boundary probe removes the supplied boundary-policy set. It trains a recurrent controller by return, then probes whether the controller's own policy state moves under persistent body-action interventions or only under detachable external-tool interventions.

The architecture boundary stress test then attacks that result. It trains `sum_rnn`, `scalar_rnn`, and `two_unit_rnn` independently and asks whether they converge on the same boundary signature. They do not: current evidence is partial convergence, not architecture-independent convergence.

The architecture horizon-pressure sweep asks whether longer horizons repair that failure. They help but do not solve it: shared-regime convergence rises from 0/3 at horizon 2 to partial convergence at longer horizons, while strict architecture-wide convergence still does not appear.

The architecture capacity probe asks whether the remaining failure is capacity or training search. With supplied source-direction seeds, all three recurrent architectures recover the expected boundary signatures and controls still reject shared recurrence. That result is diagnostic only; it does not show natural emergence.

The architecture soft-return optimizer removes those source-direction seeds. With a stronger cross-entropy search over smooth expected return, all three recurrent architectures recover the expected self, detachable, passive-world, local, and no-hidden signatures in this toy benchmark. Objective-only restart selection preserves the result, so the reported convergence is not chosen by the expected boundary class. This supports discovery under a narrow optimizer surrogate, not full natural emergence.

The architecture hard-return audit removes the smooth surrogate. It keeps controls clean and finds useful recurrent controllers, but self and detachable shared regimes show only partial cross-architecture boundary convergence. This is negative evidence against treating high task return as sufficient evidence for self-equivalent boundary discovery.

The architecture hard-return horizon sweep adds that temporal pressure helps but does not solve the hard-return boundary problem. Longer horizons move self and detachable regimes from no recovery to partial recovery and recover passive external recurrence, while controls stay clean.

The architecture online return-learner audit adds a second hard-objective limitation. An antithetic perturbation learner trained on sampled episode return keeps independent-hidden and irrelevant controls clean, but all shared regimes remain only 1/3 convergent across architectures. Online return learning therefore does not by itself collapse useful hidden-state control into self-equivalent boundary discovery.

The architecture policy-gradient learner then shows that the limitation is not sampled return itself. With stochastic score-function updates, all three recurrent architectures recover the expected self, detachable, and passive boundary signatures, while independent-hidden and irrelevant controls stay clean.

The architecture policy-gradient seed sweep adds the necessary caution. Controls remain clean across all five seeds, but shared-regime strict convergence is only partial: self is strict in 2/5 seeds, detachable in 3/5, and passive in 3/5.

The architecture policy-gradient budget sweep then tests whether that instability is merely a small-budget artifact. A larger budget repairs seed stability for self-persistent and passive-world recurrence and keeps both controls clean, but detachable-tool/world recurrence remains partial at 3/5 strict seeds.

The architecture Torch actor-critic learner then closes that narrow single-seed precursor. With GPU-backed PyTorch `RNN`, `GRU`, and `LSTM` actor-critics, self-persistent, detachable-tool, and passive-world regimes all reach 3/3 strict boundary convergence, while independent-hidden and irrelevant controls remain clean.

The SSRM-3D embodied-world precursor then moves the pressure stack into a persistent 3D world with terrain, resources, hazards, shelter, weather, day/night change, commitments, subsystem conflict, and a simple social competitor. It keeps the LLM as a slow language module that reads compressed state packets; reflex, perception, attention, arbitration, and motor layers remain in control.

The SSRM-3D recurrent-observer precursor then removes the hand-built self-state workspace from the measured representation. GPU-backed `RNN`, `GRU`, and `LSTM` observers watch embodied action-observation traces from all SSRM-3D source agents. In the low-pressure spatial stage, body state is decodable but recurrence adds little. In hidden-energy through multiagent-social stages, recurrent observers recover stronger self-state than the frame-only baseline, and edits along the learned self direction move future-viability prediction.

The SSRM-3D learned-controller precursor then moves from observer state to policy state. Recurrent controllers trained without self labels do not improve the low-pressure spatial task, but they strongly outperform frame-only controllers under hidden energy, body drift, delayed options, commitments, arbitration, and social pressure. Their policy states carry decodable self-state, while direct counterfactual self-edit action effects remain weak.

The SSRM-3D done-enough gates keep this from being overclaimed. The embodied track is not done until learned control, discovered tool-making or externalized cognition, real social pressure, and targeted ablation all pass. The current result is a useful gate-1 precursor; Gate 2 now has a partial externalized-cognition precursor, Gate 3 now has partial social-pressure and costly-communication precursors, and Gate 4 is only partial.

The modular LLM architecture report makes the language boundary explicit. The LLM is treated as a slow reasoning organ that reads compressed state packets and proposes; the self-equivalent object under test remains persistent control state in the reflex, self-state, attention, arbiter, and action stack.

The SSRM-3D tool-making precursor then starts Gate 2. It gives the world external marker, beacon, alarm, and cache affordances, selects policies by return, and ablates tool access after selection. Tools are rejected in the visible control but selected under hidden-route, degraded-sensor, and interruption pressure. The cache-only condition remains a limit control.

The SSRM-3D social-pressure precursor then starts Gate 3. It gives other agents persistent identities, resource needs, trust toward the tested agent, and simple helper, trader, opportunist, and deceiver policies. Social machinery is rejected in the visible-resource control but selected under cooperative repair, opportunist vulnerability, deceptive-route, and shared-tool pressure. Identity-memory, social-self-state, and tool-access ablations produce specific losses.

The SSRM-3D social-ecology precursor then asks when communication earns its cost. It does not reward talking directly. Costly communication is rejected in the visible solo control, but return selection keeps warning signals, names, gossip, and check-ins when they reduce rediscovery, compress social history, protect against absent-agent deception, or maintain repair/shared-tool trust.

Learned bottleneck discovery adds a sharper boundary: a shared latent is selected from unlabeled outcomes in both agent-state and world-state reuse. Compression alone discovers reusable hidden structure, not selfhood; selfhood requires the causal boundary test.

Sequence latent transfer adds held-out transfer: early calibration outcomes support later control only when they reveal a persistent episode state. The same transfer works for external world-state, so boundary evidence remains necessary.

The heterogeneous attractor precursor adds cross-learner convergence: five different small learner families converge on agent-bounded latents in a self-shared stream and external latents in a world-shared stream.

The cross-environment attractor precursor adds that the same boundary pattern recurs across body-actuator, homeostatic-viability, sensor-frame, and continuity-commitment task surfaces.

The factorial attractor precursor crosses learner families with environment surfaces: five learner families across four environments recover the same agent/world/local/no-hidden boundary pattern.

The raw history learning precursor shows the same pattern when learners receive only action-observation-reward traces instead of compact calibration outcomes.

The delayed return policy precursor shows the same pattern when candidate memory policies are selected by episode return after acting rather than by supervised reward prediction.

The evolved recurrent policy precursor shows the same pattern inside small continuous recurrent hidden states selected by episode return.

The gradient recurrent policy precursor shows the same pattern when recurrent parameters are optimized by finite-difference return gradients.

The model-based planning precursor shows the same pattern when learners first estimate reward models from probe histories and then plan held-out action from predicted value.

The latent causal ablation precursor adds direct intervention: removing the learned latent damages shared agent-state planning, while independent-hidden and irrelevant controls show no shared-latent loss.

The counterfactual latent editing precursor adds directional intervention: setting the learned latent to good or bad evidence predictably changes held-out action in shared agent-state regimes.

### H2 - Self as Control Variable

Revised claim: self appears when future outcomes depend on future internal states.

Prediction: self-state decodability and causal usefulness should increase with horizon length and delayed consequences.

Falsifier: long-horizon agents do not encode internal future-state variables, or interventions on those variables do not change planning quality.

Current evidence: hidden viability control supports persistent internal-state estimates, active information seeking selects agent-state inspection when agent-state has expected control value, and option-preservation control uses capability estimates to preserve future action availability.

Additional evidence: goal-formation under capability shows that self-state can filter which goals are worth forming when hidden capability determines feasibility. Cross-context reuse shows the same persistent agent-state estimate can guide several control contexts when the hidden condition is genuinely the same continuing system property.

The reuse-pressure sweep shows that this control advantage grows with the number of contexts controlled by the same agent property, while independent hidden variables favor local probes instead.

The horizon-pressure sweep shows that the control advantage also grows with future time steps controlled by the same agent property, while independent step-hidden variables favor local probes instead.

The partial-observability sweep shows that the control advantage also grows with cue reliability when noisy evidence tracks one persistent hidden agent property; the same belief machinery counts as world-state when the persistent hidden variable is external.

The learned observation-filter precursor shows that this need not rely on a supplied Bayesian posterior: empirical cue-count filters can select the agent-bounded channel only when that channel predicts future control.

The recurrent observation-filter precursor shows the same control role inside a recurrent state: channel-A ablation causes large reward loss only when channel A tracks hidden agent-state, while channel-B ablation causes loss when the persistent hidden cause is external.

The unseeded recurrent-filter precursor shows that this recurrent dependency does not require a hand-seeded accumulator candidate. Random-start search recovers the same boundary, though the observation channels and architecture class remain supplied.

The mixed-sensor recurrent precursor shows that the dependency does not require a self-labeled input channel. The recurrent controller sees rotated sensor mixtures, and source ablation still identifies whether the useful dependency is agent-bounded or external.

The learned sensor-subspace precursor shows that the damaging intervention does not have to be a known source ablation. Removing a learned sensor-space projection causes large control loss in self-hidden and world-hidden regimes, and the causal boundary test decides which one is self-equivalent.

The active boundary-discovery precursor shows that a self/world distinction can be inferred from action-conditioned boundary evidence. In self-hidden regimes, the outcome-predictive direction aligns with the owned-action direction; in world-hidden regimes, useful recurrent control remains external because that alignment is absent.

The action-effect boundary probe further shows that generic controllability is still not enough. In `controllable_world_hidden`, the outcome-predictive direction aligns with the tool-action direction at 1.000 but only 0.030 with the body/action-effect direction, so it remains external.

The persistent action-boundary probe shows that present-context controllability is still not enough. In `detachable_tool_world`, transient alignment is 0.999 but persistent alignment is 0.043, so the useful latent remains detachable external state.

The return-selected boundary probe shows that this boundary can be recovered without a supervised outcome-direction label. In `self_persistent_boundary`, return selects the persistent action-0 boundary policy; in `detachable_tool_world`, return-derived boundary evidence selects transient action 1, while the best controller can still be recurrent.

The end-to-end boundary probe shows the same distinction inside the trained recurrent controller's own policy state. In `self_persistent_boundary`, the recurrent policy logit has a positive persistent action-0 effect of 20.527. In `detachable_tool_world`, the strongest policy-state movement is transient action 1 at 17.880, while passive-world, independent-hidden, and irrelevant controls do not receive the persistent agent-boundary signature.

The architecture boundary stress test keeps the attractor claim honest. In shared regimes, only 1 of 3 independently trained recurrent architectures recovers the expected boundary signature. In controls, all 3 architectures reject shared recurrence. That means the current result supports recoverability under some architectures, not strict architecture-wide convergence.

The architecture horizon-pressure sweep adds that longer horizons increase recoverability without completing convergence. In `self_persistent_boundary` and `detachable_tool_world`, convergence moves from 0/3 at horizon 2 to 1/3 at horizons 4, 8, and 16. In `passive_world_boundary`, it reaches 2/3 by horizon 16. Controls remain clean across horizons.

The architecture capacity probe adds that this is probably not a raw architecture-capacity limit. When source-direction seeds are supplied, `sum_rnn`, `scalar_rnn`, and `two_unit_rnn` all recover the expected self, detachable, passive-world, local, and no-hidden signatures. The unresolved problem is autonomous discovery.

The architecture soft-return optimizer narrows that unresolved problem. Without source-direction seeds, a stronger toy return optimizer recovers the same boundary signatures across all three architectures while controls still reject shared recurrence or hidden state. This survives selection by optimizer objective alone. The remaining gap is richer online learning, not this bounded optimizer.

The architecture hard-return audit shows why that gap matters. Removing the smooth surrogate and ranking only by realized recurrent return leaves clean controls and useful recurrence, but only partial recovery of the self and detachable boundary signatures. Hard return can reward task success without selecting the boundary abstraction sharply enough.

The architecture hard-return horizon sweep adds the temporal-pressure version of that limit. Increasing horizon makes hard-return recurrence more valuable and restores passive external recurrence, but it still leaves self and detachable boundary convergence partial under the bounded hard-return objective.

The architecture online return-learner audit tests a different objective-only learner. Fresh sampled return batches, antithetic perturbation updates, and validation-return restart selection still leave all shared regimes at partial architecture convergence, while controls remain clean. This is direct evidence that online return success remains weaker than self-boundary emergence.

The architecture policy-gradient learner adds the corresponding positive result. Stochastic policy gradients from sampled return recover strict boundary convergence across `sum_rnn`, `scalar_rnn`, and `two_unit_rnn`, and the controls still choose local probing or no-state action. Credit assignment through the stochastic policy appears sufficient in this toy benchmark.

The architecture policy-gradient seed sweep shows that this sufficiency is not yet seed-stable. Across five seeds, the shared regimes recover most architecture-seed cells, but strict architecture-wide convergence fails in several seeds. This keeps the attractor claim provisional.

The architecture policy-gradient budget sweep partially repairs that limitation. With more epochs, restarts, and batch episodes, self-persistent and passive-world regimes become strict across all five seeds while controls remain strict. The detachable-tool regime improves from 12/15 to 13/15 architecture-seed cells but still fails strict seed stability, which keeps the boundary between continuing agent state and detachable external action effects open.

The architecture Torch actor-critic learner adds the strongest current neural RL precursor. Under the canonical MPS run, `torch_rnn`, `torch_gru`, and `torch_lstm` recover the expected self-persistent, detachable-tool, and passive-world signatures, while local-probe and no-hidden controls reject shared recurrence.

The SSRM-3D precursor adds embodied pressure. No-self control remains sufficient in the low-pressure spatial stage. The layered self-state latent becomes decodable under hidden energy, beats world-only under body drift and delayed-option pressure, and becomes strongly performance-relevant after commitments, interruption recovery, subsystem arbitration, and social pressure enter.

The SSRM-3D recurrent-observer precursor adds learned representation evidence on the same embodied traces. The strongest pattern is not generic hidden-state tracking: stage 0 remains a low-pressure control with only a 0.032 recurrent self-state gain, while stages 1-6 show recurrent gains from 0.071 to 0.362 and self-state edits with large future-viability swings.

The SSRM-3D learned-controller precursor adds policy-state evidence. Learned recurrent controllers trained by return-weighted imitation and future-return prediction beat frame-only controllers by 50.120 to 123.950 reward points in stages 1-6 and carry decodable self-state. The weak action-edit swing keeps the causal-editability claim open.

The SSRM-3D social-pressure precursor adds a first real social gate test. Other agents now have persistent memory, needs, trust, and role policies; social self-state helps only when the tested agent can be helped, exploited, deceived, remembered, or trusted.

The SSRM-3D social-ecology precursor adds the first costly-communication test. Signals, names, gossip, and check-ins are useful only when they preserve future options under social memory; babble is punished when it has no control job.

Learned bottleneck discovery shows the control policy selected from unlabeled data matches the right abstraction: shared bottleneck for reusable hidden causes, local hidden variables for independent contexts, and no hidden state when all risky actions work.

Sequence latent transfer shows that calibration memory alone is not enough; the learner must treat early outcomes as evidence about a persistent state that continues to affect later contexts.

Heterogeneous learner convergence shows that this control value is not limited to one hand-coded selector: Bayesian, predictive-state, recurrent, evolutionary-rule, and bottleneck-cluster learners all use the same calibration-derived latent when it controls held-out action.

Cross-environment recurrence shows that this control value is not limited to one task surface: the learned selector uses shared agent-state in self-shared versions of body, viability, frame, and continuity environments while switching to world, local, or no-hidden structure in controls.

The factorial precursor shows the same pattern when learner-family and environment-surface variation are crossed. In self-shared regimes, all five learners converge in all four environments and the best learner beats repeated local probing.

The raw history learning precursor shows that this is recoverable from reward histories: probe-action rewards and risky-action rewards are enough for small memory learners to infer the transferable latent.

The delayed return policy precursor shows that memory policies can be selected by delayed return and still discover when probe rewards should control held-out action.

The evolved recurrent policy precursor shows that the reusable state can be represented as a learned hidden variable, not only as a table or explicit rule.

The gradient recurrent policy precursor shows that the same recurrent boundary pattern can be shaped by return-gradient optimization, not only evolutionary selection.

The model-based planning precursor shows that the reusable state can mediate prediction before control: reward models learn the latent, then planners use it for action.

The latent causal ablation precursor shows that the reward-model latent is behaviorally necessary in shared-state regimes, not just decodable.

The counterfactual latent editing precursor shows that the learned latent can be edited as an action-centered counterfactual variable, not merely removed.

### H3 - Self as Error Attribution

Revised claim: self is needed to assign prediction error to the right cause: external world, sensor, actuator, body, memory, or policy.

Prediction: self-modeling advantage should spike under body drift, sensor drift, actuator drift, or internal degradation.

Falsifier: drift source identification and recovery remain equally strong without self-equivalent variables.

Current evidence: self/world attribution separates actuator drift from world drift, and first-person frame integration shows that hidden or drifting body orientation requires a centered observation/action frame.

### H4 - Self as Coherence Stabilizer

Revised claim: self is an index used to maintain consistency across competing subsystems over time.

Prediction: self-model architectures recover faster from contradictory memories, incompatible goals, and interrupted plans.

Falsifier: coherence repair is solved equally well by local conflict-resolution mechanisms with no persistent agent index.

Current evidence: interruption coherence supports identity indexing after corrupted resume, and competing-subsystems arbitration shows shared self-state beating local voting when hidden agent energy determines which subsystem proposal is coherent.

### H5 - Self as Illusion

Revised claim: self-like behavior may be produced by lower-level predictive, recurrent, and control mechanisms without any explicit self-object.

Prediction: black-box recurrent policies or predictive state representations may match self-model agents while still containing no interpretable self abstraction.

Falsifier: across architectures, the best systems converge on separable, causally active self-equivalent variables even when not hand-coded.

Current evidence: simple unlabeled predictive learners do converge on action-effect variables under self drift, and several learner families converge on shared latents under stream-transfer pressure, factorial environment variation, raw reward-history learning, delayed-return policy selection, evolved recurrent hidden-state learning, gradient-trained recurrent hidden-state learning, model-based planning, latent causal ablation, counterfactual latent editing, partial-observability belief scaling, learned noisy-observation filtering, recurrent observation filtering, unseeded recurrent filtering, mixed-sensor recurrent filtering, learned sensor-subspace filtering, active boundary discovery, action-effect boundary probing, persistent action-boundary probing, return-selected boundary probing, and end-to-end recurrent boundary probing. The architecture boundary stress and horizon-pressure tests add a limit: weak random-start search did not produce strict convergence across independently trained recurrent architectures. The capacity probe shows the weaker architectures can represent the boundary when source directions are supplied, and the soft-return optimizer shows a stronger toy optimizer can discover it without those seeds or boundary-aware restart selection. The hard-return audit adds a caution: realized return alone can select useful recurrent controllers without strict boundary convergence, longer horizons only partially repair that failure, and the online return-learner audit still leaves shared regimes only partially convergent. The policy-gradient learner partly answers that caution by recovering strict convergence from sampled-return credit assignment. The seed sweep shows that this is not automatically seed-stable; the budget sweep repairs self and passive recurrence but not detachable-tool seed stability. The Torch actor-critic learner adds a positive single-seed neural RL result across `RNN`, `GRU`, and `LSTM` architectures with clean controls. The SSRM-3D precursor adds a first embodied realtime control surface where the LLM is only a reasoning organ, not the organism. The SSRM-3D recurrent-observer and learned-controller precursors add learned representation and policy-state evidence on those traces. This supports an implicit-self account more than a symbolic self-object account, but it also keeps the optional/illusion hypothesis live: convergence, causal usefulness, belief updating, editability, generic action controllability, detachable action effects, return-selected transient boundaries, end-to-end recurrent hidden-state usefulness, objective-only online return success, weak learned-controller action edits, and early-stage embodied reactive success alone are not selfhood.

## Strongest Current Answer

Selfhood is probably not universally necessary. It is conditionally necessary as an abstraction when a system must control through time under partial observability and its own internal state is a hidden cause of future observations and rewards.

The strongest form of the claim is:

> In environments where future outcomes depend on unobserved, changing properties of the agent itself, any optimal long-horizon policy must encode information statistically equivalent to a self-state. Whether that encoding is explicit, verbal, spatial, narrative, or conscious is a separate question.

The anti-tautology version is stricter:

> Hidden internal variable tracking becomes selfhood only when the variable functions as a reusable control abstraction for the same continuing system.

This makes selfhood an attractor for adaptive systems under the right pressures, but not a proof of consciousness.

## Relationship To Consciousness

The current program separates these layers:

- world model;
- agent-state model;
- self/world error attribution;
- first-person frame;
- coherence maintenance;
- identity continuity;
- global availability or workspace;
- subjective continuity;
- phenomenal consciousness.

The self-model may be prerequisite for some forms of consciousness, consequence of some forms of consciousness, or orthogonal to phenomenal consciousness. The experimental program should not assume any of those.
