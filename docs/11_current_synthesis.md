# Current Synthesis: Why a Self Exists

## Short Answer

A persistent self is not universally necessary.

A self-equivalent representation becomes useful, and sometimes weakly necessary, when an adaptive system must control through time under partial observability and future outcomes depend on hidden, changing properties of the system itself.

The important revision is that hidden-state tracking is not selfhood by itself. Hidden agent-state becomes self-equivalent only when it is agent-bounded, persistent, action-mediated, control/value relevant, counterfactually active, and reused across prediction or control.

In that setting, "I" is the compressed control variable for:

- what body or architecture is acting;
- what its actions currently do;
- what internal viability state it is in;
- what commitments are still its own;
- which prediction errors came from the world versus from the agent;
- which future internal states preserve future control;
- which subsystem proposal is coherent for the same continuing system.

This does not imply consciousness. It does not imply a metaphysically real self. It says that systems under certain pressures need information statistically equivalent to agent-state.

## Core Claim

Let `A_t` be hidden agent-state: body, actuator dynamics, energy, damage, competence, commitments, memory status, and other variables internal to the controlled system.

If future observations, rewards, or viable actions depend on `A_t`, then any long-horizon policy that performs well must encode information about `A_t` somewhere.

That encoding may be:

- explicit: a structured self-model;
- implicit: recurrent state, predictive state, action-effect predictions, or a commitment ledger;
- distributed: no single "self" variable, but decodable and causally useful agent-state information.

The self is therefore best treated as a persistent agent-state abstraction, not as a separate inner entity.

## Boundary Against Hidden-State Tautology

The theory should not be restated as:

```text
Any system with persistent hidden internal variables benefits from modeling those variables.
```

That statement is true in too many cases and does not explain selfhood.

The corrected boundary is:

```text
Hidden-state tracking becomes self-equivalent when the hidden state is a reusable
model of the controlled system as the entity whose state mediates action through time.
```

This yields a ladder:

| Tier | Representation | Verdict |
|---|---|---|
| Hidden external state | Weather, terrain, wind, market regime | World modeling, not selfhood. |
| Generic hidden internal state | Local cache, unused diagnostic bit, passive report variable | Internal-state tracking, not selfhood. |
| Agent-state for action | Body damage, actuator gain, sensor reliability, competence | Minimal self-equivalent. |
| Agent-state for value | Energy, fatigue, integrity, future capability | Stronger control self. |
| Continuity index | Owner/current epoch/pending commitments after interruption | Identity-like self. |

A variable should count as self-equivalent only if interventions on it change action-centered counterfactuals:

- what this system can do now;
- what will happen if this system acts;
- what future internal states preserve or reduce options;
- which prior commitments belong to this same continuing system.

## When "Me" Beats World-State-Only

Representing "me" becomes more useful than representing world-state-only when all or most of these are true:

- the agent is partially observable to itself;
- the agent changes through time;
- action effects depend on the agent's current internal state;
- feasible goals depend on the agent's current capabilities;
- future reward depends on future internal state;
- the same internal variable is reused across many predictions or tasks;
- a single internal estimate transfers across goal choice, future-option reasoning, and coherence decisions;
- early sequence evidence about the system predicts later held-out contexts;
- the advantage of one internal estimate grows as more contexts depend on the same agent property;
- interventions on the internal variable change action-centered counterfactual predictions;
- prediction errors are ambiguous between world change and self change;
- memory contains commitments that may be stale, foreign, duplicated, or contradictory;
- a compact agent-state variable predicts/control better than a long raw history.

Representing "me" is unnecessary or wasteful when:

- the body and policy are fixed;
- the task is short horizon;
- internal state has no effect on reward or action;
- simple reactive control works;
- a fixed schedule solves the regime;
- generic memory is clean and unambiguous;
- hidden variables are external rather than agent-bounded;
- internal variables are passive diagnostics with no action/value role;
- predictive state encodes all needed information without a separable self abstraction.

## Smallest Mechanism Set

The current experiments suggest this mechanism stack:

1. Persistent internal state: memory of variables slower than immediate observation.
2. Action-conditioned prediction: expected sensory/world effects for possible actions.
3. Self/world attribution: separating external drift from changed action-effect state.
4. Viability coupling: internal variables such as energy or damage affect future value.
5. Continuity index: filtering commitments by owner/current epoch/pending status.
6. Shared-state arbitration: resolving competing subsystem proposals against the same continuing agent-state.
7. Cross-context reuse: carrying the same agent-state estimate across goal choice, future-option reasoning, and coherence decisions.
8. Optional coherence layer: resolving contradictions across memory, goals, and plans.

The first three are enough for a minimal non-conscious self-equivalent only when the tracked internal state is action-mediated and causally active. Viability coupling creates stronger long-horizon pressure. Continuity indexing is needed for identity-like behavior after interruption or memory corruption.

## Hypothesis Status

### H1 - Self as Compression

Supported conditionally.

The representation-search experiment selected no-self models in static cases, world-only models in pure external drift, and self-equivalent models in self-drift. In mixed-hidden cases, self-equivalent models won when hidden action-effect state mattered.

The architecture-convergence experiment strengthens this by showing that several unlabeled learner families converge on action-effect components under self drift, bias/world components under world drift, and both under mixed hidden drift.

The cross-context reuse experiment adds that a shared self-state estimate beats repeated local probing when one persistent agent capability controls goal choice, option preservation, and commitment action. When the reusable variable is external, shared world-state wins; when hidden variables are independent, local probing wins.

The reuse-pressure sweep adds the predicted gradient: shared self-state has no advantage over local probing with one context, then gains linearly as additional contexts reuse the same agent-state. The same curve belongs to world-state when the reusable hidden variable is external.

The horizon-pressure sweep adds the temporal gradient: shared self-state has no advantage over local probing at one future step, then gains value as additional future steps reuse the same agent-state. The same curve belongs to world-state when the persistent hidden variable is external.

The partial-observability sweep adds the evidence-quality gradient: shared self-belief becomes best when noisy cues reliably reveal one persistent hidden agent-state. The same Bayesian reuse counts as world-state when the persistent hidden variable is external, and it fails when future steps have independent hidden conditions.

The learned observation-filter precursor removes the supplied posterior equation. A selector trained on noisy cue/outcome histories learns the agent-bounded cue in the self-hidden regime, the external cue in the world-hidden regime, local probing in independent-hidden control, and no-state greedy action when hidden state is irrelevant.

The recurrent observation-filter precursor replaces cue-count tables with small recurrent controllers. The selected recurrent state is causally dependent on channel A when channel A tracks persistent agent-state, causally dependent on channel B when the persistent hidden cause is external, and rejected when local probing or no-state control is better.

The unseeded recurrent-filter precursor removes seeded accumulator candidates. Random-start recurrent search still recovers the same boundary: agent-channel dependence in self-hidden regimes, world-channel dependence in external-hidden regimes, local probing for independent hidden steps, and greedy no-state control when hidden state is irrelevant.

The mixed-sensor recurrent precursor removes self-aligned input channels. Random-start recurrent search sees only rotated mixtures of noisy latent sources, then source ablation separates agent-bounded recurrent dependence from external recurrent dependence.

The learned sensor-subspace precursor removes known-source ablation from the destructive intervention. It learns an outcome-predictive projection in mixed sensor space, then shows that removing that learned projection selectively damages recurrent control in shared regimes while boundary interventions still classify the damaged dependency as agent-bounded or external.

The active boundary-discovery precursor removes supplied boundary interventions from the classification step. It learns the outcome-predictive sensor direction and the owned-action sensor direction separately, then counts the dependency as self-equivalent only when those directions align.

The action-effect boundary probe adds a controllable-world negative control. A latent can be useful and action-controllable while still external; it becomes self-equivalent only when it aligns with the body/action-effect boundary rather than a tool-action boundary.

The persistent action-boundary probe adds a transfer-context test. A detachable tool-like latent can align with an action-effect direction in the present context, but it remains external when that action-effect alignment does not persist across contexts.

The return-selected boundary probe removes supervised outcome-direction extraction from that boundary family. It proposes action-boundary policies from action-observation deltas and lets training return select or reject persistent, transient, recurrent, local, and no-hidden policies.

The end-to-end boundary probe removes the supplied boundary-policy set. It trains a recurrent controller by return, then probes whether the trained controller's own policy state moves with a persistent body-action intervention or only with a detachable external-tool intervention.

The architecture boundary stress test attacks the end-to-end result by training each recurrent architecture independently. It finds partial convergence, not strict architecture-wide convergence, so the current evidence should not be treated as a completed Attractor Test.

The architecture horizon-pressure sweep asks whether longer temporal dependence fixes that failure. It improves recoverability in shared regimes but still does not produce strict architecture-wide convergence, so horizon length is a pressure, not a proof.

The architecture capacity probe separates capacity from discovery. With supplied source-direction seeds, all tested recurrent architectures recover the expected boundary signatures and controls still reject shared recurrence, so the current failure is a training/discovery gap rather than a raw representational-capacity gap.

The architecture soft-return optimizer narrows that gap further. It removes source-direction seeds and uses cross-entropy search over a smooth expected-return surrogate. Restarts are selected by optimizer objective, not by the expected post-hoc boundary signature. Under that stronger toy optimizer, all tested recurrent architectures recover the expected boundary signatures and the controls still reject shared recurrence or hidden state.

The architecture hard-return audit removes the smooth surrogate. Hard realized-return optimization still finds useful recurrent controllers and keeps controls clean, but it only partially recovers the self and detachable boundary signatures across architectures. This is evidence that high task return is not the same thing as self-equivalent boundary discovery.

The architecture hard-return horizon sweep adds that temporal pressure helps but does not solve that limitation. Under a bounded hard-return budget, self and detachable regimes improve from no recovery to partial convergence as horizon increases, passive-world recurrence becomes strict, and controls remain clean.

The architecture online return-learner audit adds that changing the hard-objective learner is not enough by itself. Antithetic perturbation updates from sampled episode return keep the controls clean but leave self, detachable, and passive shared regimes at only 1/3 architecture convergence.

The architecture policy-gradient learner adds the positive counterpart. Stochastic score-function updates from sampled return recover strict boundary convergence across `sum_rnn`, `scalar_rnn`, and `two_unit_rnn` in all shared regimes while controls remain clean.

The architecture policy-gradient seed sweep then limits that positive result. Across five seeds, controls remain strict in every seed, but shared-regime strict convergence is only partial. Policy-gradient credit assignment is a viable discovery mechanism here, not yet a seed-stable attractor law.

The architecture policy-gradient budget sweep partially repairs that limit. A larger policy-gradient budget makes self-persistent and passive-world recurrence strict across all five seeds while preserving clean controls. Detachable-tool recurrence improves but remains partial, so the continuing-agent versus detachable-external boundary is still the hard case.

The architecture Torch actor-critic learner closes the next narrow precursor under a single canonical MPS run. PyTorch `RNN`, `GRU`, and `LSTM` actor-critics recover strict self-persistent, detachable-tool, and passive-world boundary signatures while independent-hidden and irrelevant controls stay clean.

The SSRM-3D embodied-world precursor starts the persistent 3D track. It keeps the LLM as a slow language-cortex module rather than the controller, and tests whether reflex, perception, self-state, attention, arbiter, and action layers benefit from a reusable self-state workspace under staged embodiment pressure.

The SSRM-3D recurrent-observer precursor then tests whether that workspace can be recovered from traces. GPU-backed recurrent observers watch embodied action-observation streams from all SSRM-3D source agents. The low-pressure stage remains only body-state decodability with little recurrent advantage, while stages 1-6 show stronger recurrent self-state recovery and future-viability sensitivity to self-state edits.

The SSRM-3D learned-controller precursor then moves the test into policy state. Recurrent controllers trained without self labels do not improve the low-pressure spatial task, but they strongly outperform frame-only controllers in stages 1-6 and carry decodable self-state. Direct self-edit action effects remain weak.

The modular LLM architecture boundary makes the language layer explicit. The LLM is not treated as the self or the organism; it is a slow reasoning organ that receives compressed state packets and proposes plans, explanations, hypotheses, memory summaries, or tool-use ideas. Reflex, self-state, attention, arbiter, and action layers retain control authority. The stack should be described in subsystem frequencies rather than one global cognitive tick: ticks are implementation, rates are architecture. This turns "LLM as brain" into a falsifiable ablation target instead of a hidden assumption.

The SSRM-3D tool-making precursor starts the externalized-cognition gate. Return selection rejects tools in the visible control, selects marker/beacon-style policies under hidden-route, degraded-sensor, and interruption pressure, and loses the advantage when tool access is ablated. The cache-only condition remains a live limit rather than a success.

The SSRM-3D social-pressure precursor starts the real-social-pressure gate. Return selection rejects social machinery in the visible-resource control, selects identity/reputation/vulnerability-aware policies when helpers, traders, opportunists, deceivers, or shared tools matter, and loses the advantage under identity-memory, social-self-state, or shared-tool ablation.

The SSRM-3D social-ecology precursor then asks when communication earns its cost. It does not reward talking directly. Costly communication is rejected in the visible solo control, but return selection keeps warning signals, names, gossip, and trust-maintenance check-ins when they reduce rediscovery, compress social history, protect against absent-agent deception, or preserve repair and shared-tool trust.

The SSRM-3D agent-continuity precursor asks what must be serialized for the same agent to continue after pause, restore, transplant, rollback, or fork. Model-only copies, incompatible memory transplants, social-memory resets, commitment resets, tool resets, and ambiguous forks fail in specific regimes, while the full AgentContinuityRecord preserves control.

The SSRM-3D learned-integration precursor then moves part of that gate stack into learned policy state, but only as a designed packet bridge. A frame-only policy and a recurrent policy are trained from reward-derived action choices over compressed packet traces. The seeded canonical run shows pressure-specific recurrent value, while scenario identity and feature-group structure remain supplied by the experiment.

The learned bottleneck discovery experiment adds that a shared latent can be selected from unlabeled outcome data. It is selected for both agent-state reuse and external-world reuse, which means compression alone discovers reusable hidden structure, not selfhood.

The sequence latent transfer experiment adds held-out transfer: calibration outcomes support later action only when they reveal a persistent sequence state. The same transfer works for reusable world-state, so boundary evidence remains necessary.

The heterogeneous attractor precursor adds cross-learner convergence: Bayesian, predictive-state, recurrent, evolutionary-rule, and bottleneck-cluster learners all converge on the same latent causal signature in shared-state regimes. The convergence is agent-bounded only in the self-shared stream; it is external in the world-shared stream.

The cross-environment attractor precursor adds surface diversity: body-actuator, homeostatic-viability, sensor-frame, and continuity-commitment environments all recover the same agent/world/local/no-hidden boundary pattern.

The factorial attractor precursor combines learner and environment variation: five learner families across four task surfaces recover the same four-way boundary pattern. This is still toy-scale, but it is the strongest current attractor evidence.

The raw history learning precursor removes compact outcome inputs: learners receive probe-action rewards and risky-action rewards, yet recover the same four-way boundary pattern across the four task surfaces.

The delayed return policy precursor weakens the training signal again: policies are selected by episode return after acting, not by per-context reward prediction, and still recover the same boundary pattern.

The evolved recurrent policy precursor replaces enumerated memory rules with small continuous recurrent controllers selected by episode return. Their hidden states recover the same boundary pattern across task surfaces.

The gradient recurrent policy precursor keeps the same recurrent controller family but optimizes parameters by finite-difference return gradients. It recovers the same boundary pattern across task surfaces.

The model-based planning precursor separates prediction from action: reward models learn latent probe-history structure, then planners choose held-out action by predicted value. It recovers the same boundary pattern across task surfaces.

The latent causal ablation precursor adds that the learned latent is behaviorally active. Replacing it with a marginal model causes large reward loss in shared-state regimes and no loss in independent-hidden or irrelevant controls.

The counterfactual latent editing precursor adds directional validity. Setting the learned latent to all-good evidence drives held-out risky action to 1.000 in shared regimes, while all-bad evidence drives it to 0.000.

Current interpretation: self-state is a compression of reusable agent-internal variables, but only when those variables explain future observations or rewards across contexts.

### H2 - Self as Control Variable

Supported conditionally.

The hidden-viability experiment showed that persistent energy/integrity estimates improve survival and value under hidden energy and damage stress. The ablation that estimated internal state but did not use it for control died in every stressed scenario.

The active self-information experiment adds that agent-state information is selected as an information target when it has expected control value. The bandit chooses world-state inspection under world relevance, agent-state inspection under agent relevance, both under joint relevance, and no inspection when hidden state is irrelevant.

The counterfactual option-preservation experiment adds that self-state matters when current actions can destroy future action options. A future-option self-state policy preserves capability and beats myopic agents under capability-dependent future options, while no-option and world-gate controls do not favor self-preservation.

The goal-formation experiment adds that self-state can matter before action selection: desirable goals must be filtered through what this system can actually do.

The cross-context reuse experiment adds that one persistent self estimate can guide several control contexts when they are all downstream of the same agent property.

The reuse-pressure sweep adds that this advantage increases with reuse pressure: the more decisions downstream of the same hidden agent property, the more useful one persistent estimate becomes.

The horizon-pressure sweep adds that this advantage increases with time horizon: the more future steps downstream of the same hidden agent property, the more useful one persistent estimate becomes.

The partial-observability sweep adds that this advantage increases with evidence reliability: the more informative noisy cues are about one hidden agent property, the more useful one persistent self-belief becomes for future control.

The learned observation-filter precursor adds that the posterior need not be supplied by the experimenter. A simple empirical filter can learn which noisy cue channel predicts future control and select the agent-bounded channel only when it is the control-relevant hidden cause.

The recurrent observation-filter precursor adds a causal hidden-state test: the recurrent controller wins in self-hidden and world-hidden regimes, but channel ablation separates agent-bounded recurrent filtering from external recurrent filtering.

The unseeded recurrent-filter precursor adds that this result is not dependent on hand-seeded self/world accumulators. The recurrent architecture class is still supplied, but useful channel dependence is found by random-start candidate search.

The mixed-sensor recurrent precursor adds that this result is not dependent on a self-labeled sensor channel. The controller recovers the useful latent source from mixed observations, and source ablation classifies the recovered dependency.

The learned sensor-subspace precursor adds that the destructive intervention need not be the known latent source. A learned sensor-space projection is enough to produce selective control loss; the agent-boundary test remains the criterion that separates self-equivalent dependence from useful external dependence.

The active boundary-discovery precursor adds an operational boundary criterion: the useful latent must be both outcome-predictive and moved by the agent's own action. World-hidden recurrent dependence remains useful, but it is external because its outcome direction has weak owned-action alignment.

The action-effect boundary probe adds that generic action controllability is still too broad. In a controllable-world regime, the outcome-predictive latent aligns with a tool-action direction but not with the body/action-effect direction, so it remains external.

The persistent action-boundary probe adds that present-context action controllability is still too broad. A detachable-tool regime has strong transient alignment but weak persistent alignment, so the useful latent remains external.

The return-selected boundary probe adds that the boundary can be recovered without a supervised outcome-direction label. Return selection favors the persistent action boundary in the self regime, transient action-boundary evidence in the detachable-tool regime, recurrent filtering in passive-world regimes, local probing for independent hidden state, and greedy no-state control when hidden state is irrelevant.

The end-to-end boundary probe adds that the boundary can be recovered inside a trained recurrent policy state without supplied boundary policies. The recurrent policy state has a strong positive persistent action-0 effect in `self_persistent_boundary`, a stronger transient action-1 effect in `detachable_tool_world`, no positive action-boundary effect in `passive_world_boundary`, and no selected recurrent hidden state in independent or irrelevant controls.

The architecture boundary stress test adds an important limit: only 1 of 3 independently trained recurrent architectures recovers the expected boundary signature in the three shared regimes. All 3 architectures reject shared recurrence in independent-hidden and irrelevant controls. This supports recoverability under some architectures, not architecture-independent inevitability.

The architecture horizon-pressure sweep adds that this limit is not removed by longer horizons. Shared regimes move from 0/3 convergence at horizon 2 to partial convergence at longer horizons, while controls remain stable. Temporal pressure increases recoverability but does not complete the Attractor Test.

The architecture capacity probe adds a diagnostic correction: the weaker recurrent architectures can recover the same expected signatures when source-direction seeds are supplied. That keeps the research target focused on autonomous discovery rather than claiming scalar and two-unit recurrent policies are intrinsically incapable.

The architecture soft-return optimizer adds a bounded discovery result: without source-direction seeds, a stronger toy optimizer recovers the same expected signatures across all three recurrent architectures while independent-hidden and irrelevant controls remain clean. Objective-only restart selection preserves the result, so the current evidence does not depend on choosing restarts by the expected boundary class. This does not yet replace the need for richer online RL or model-based agents.

The architecture hard-return audit adds a limit on that discovery result. With the smooth surrogate removed, hard return ranks some high-reward recurrent controllers above controllers with the expected action-boundary signature. Self and detachable regimes fall back to partial convergence, while passive-world and controls remain correctly classified.

The architecture hard-return horizon sweep shows that longer horizons improve this hard-return picture without eliminating the limitation. Self and detachable regimes move from 0/3 to 1/3 convergence, passive-world recurrence moves to 3/3, and controls stay clean.

The architecture online return-learner audit shows the same limit under a different objective-only learner. Fresh sampled return batches and validation-return restart selection preserve clean controls, but all shared regimes remain partial at 1/3 convergence.

The architecture policy-gradient learner shows that stronger sampled-return credit assignment can recover the missing boundary signatures. It reaches 3/3 convergence in self, detachable, and passive shared regimes while retaining 3/3 local/no-hidden controls.

The architecture policy-gradient seed sweep shows that the result is not yet seed-stable. Shared regimes recover most architecture-seed cells, but strict convergence appears in only 2/5 to 3/5 seeds. Controls remain 5/5 stable.

The architecture policy-gradient budget sweep shows that the seed instability is partly an optimization-budget artifact. The larger budget repairs self-persistent and passive-world strict seed convergence and preserves 5/5 controls, but detachable-tool convergence remains at 3/5 strict seeds.

The architecture Torch actor-critic learner adds a stronger neural sampled-return result. Across `torch_rnn`, `torch_gru`, and `torch_lstm`, the canonical run recovers 3/3 strict convergence in self-persistent, detachable-tool, and passive-world regimes and preserves 3/3 control rejection in independent-hidden and irrelevant regimes.

The SSRM-3D embodied-world precursor adds an embodied pressure gradient. In the low-pressure spatial stage, no-self reactive control remains sufficient. Under hidden energy, body drift, and delayed options, the layered self-state latent becomes decodable and beats the world-only model, though reactive control remains competitive in body-drift and delayed-option stages. Once commitments, subsystem arbitration, and social pressure enter, the layered self-state agent dominates and self-state ablation sharply reduces reward.

The SSRM-3D recurrent-observer precursor adds learned representation evidence on the same embodied traces. In stage 0, `torch_lstm` recovers body state but only gains 0.032 over the frame-only baseline. In stages 1-6, recurrent observers gain 0.071 to 0.362 self-state R2 over frame-only observers, and learned self-state edits move future-viability prediction.

The SSRM-3D learned-controller precursor adds learned control evidence on the same world. Recurrent controllers trained by return-weighted imitation and future-return prediction beat frame-only controllers by 50.120 to 123.950 reward points in stages 1-6 while their hidden states decode self variables. The weak self-edit action swing keeps causal policy editing as the next gap.

The SSRM-3D tool-making and social precursors add that self-state pressure is not only internal. External markers, shared tools, identity memory, reputation, costly signals, and names matter only when they preserve future options under embodied confusion or repeated social memory.

The SSRM-3D agent-continuity precursor adds a restore/fork boundary. The same agent is not identified by weights, body, or memory alone; control survives when the continuity record binds body, model, memory, social history, commitments, event log, attention, hidden state, tools, goals, and branch identity.

The SSRM-3D learned-integration precursor adds a cross-gate learned-control bridge, not a strong integration result. In visible control, recurrent memory and special channels add no value. Local tool-route, social-repair, and continuity-restore rows show recurrent gains and matching ablation losses, but the integrated gate-pressure row does not lose value under continuity-channel ablation in the canonical run.

The learned bottleneck discovery experiment adds a simple model-selection step: the learned policy chooses a shared bottleneck in reusable-hidden regimes, local probes in independent-hidden regimes, and no hidden state when hidden state is irrelevant.

The sequence latent transfer experiment adds that calibration memory without transfer is not enough. Control improves when the agent treats early outcomes as evidence about a persistent state that continues to govern later contexts.

The heterogeneous attractor precursor adds that the same control value is found by several learner families, not only by a supplied structure selector. Under self-shared pressure, all five learner families beat local probing by using one calibration-derived latent across held-out contexts.

The cross-environment attractor precursor adds that a learned selector uses the agent-bounded latent across all four self-shared environment surfaces and switches to external, local, or no-hidden structure in matched controls.

The factorial attractor precursor adds that this pattern is not limited to one learner family. In self-shared regimes, all five learner families converge in all four environment surfaces and the best learned policy beats repeated local probing.

The raw history learning precursor adds that the control signal can be learned from reward histories rather than supplied as explicit success/failure outcomes. In self-shared regimes, raw reward-memory learners beat local probing across all four surfaces.

The delayed return policy precursor adds that return-trained memory policies can discover the same reusable state from delayed evaluation. In self-shared regimes, the best delayed-return policies beat repeated local probing across all four surfaces.

The evolved recurrent policy precursor adds that the reusable state can live inside a recurrent hidden variable selected by return. In self-shared regimes, evolved recurrent policies beat repeated local probing across all four surfaces.

The gradient recurrent policy precursor adds that return-gradient optimization can shape the same reusable recurrent state. In self-shared regimes, gradient-trained recurrent policies also beat repeated local probing across all four surfaces.

The model-based planning precursor adds that the reusable state can be learned as a reward-model variable before action choice. In self-shared regimes, model-based planners beat repeated local probing across all four surfaces.

The latent causal ablation precursor adds that removing the learned agent-bounded latent destroys the planning advantage. In self-shared regimes, mean reward falls from 42568.500 to 21875.000 after ablation.

The counterfactual latent editing precursor adds that editing the agent-bounded latent predictably changes planned action. In self-shared regimes, mean edit swing is 1.000 across all four surfaces.

Current interpretation: self-state matters when future reward depends on future internal viability, future capability, future action availability, goal feasibility, or reusable agent-state transfer across contexts.

### H3 - Self as Error Attribution

Supported in the toy environment.

The self/world attribution experiment showed that factorizing actuator gain from world drift improves recovery when the agent's own action-effect state changes. The self-state ablation fails specifically when hidden actuator state matters.

The first-person-frame experiment adds a related pressure: when observations are world-relative but actions are body-relative, the agent needs a centered body-frame variable to transform perception into action. Recalibration becomes necessary when body orientation drifts.

Current interpretation: one pressure toward self is ambiguity between "the world changed," "my ability/body changed," and "my action frame changed."

### H4 - Self as Coherence Stabilizer

Supported conditionally.

Generic memory solves clean resume. It fails when memory contains foreign, stale, duplicate, or contradictory records. The identity continuity ledger matches oracle in those corrupted settings.

The competing-subsystems arbitration experiment adds a simultaneous-conflict case. Local voting collapses when immediate reward, commitment completion, and safety maintenance disagree under hidden agent energy. A self-coherence arbitrator beats local voting in that setting, while no-conflict and world-gate controls show that self-state is not generally useful.

The SSRM-3D agent-continuity precursor broadens this from corrupted memory to restored and forked control. Generic model weights, generic memory, and body state are each insufficient when the pressure requires the whole continuity record.

Current interpretation: self is useful as an index for "my current unfinished commitments" and as a shared arbitration variable for "which subsystem proposal is coherent for this continuing system," not for memory or conflict resolution in general.

### H5 - Self as Illusion or Optional Abstraction

Still live.

Several non-self alternatives work in some regimes:

- reactive policy in low-stress or static cases;
- world-only model under pure external drift;
- action-history table in small action spaces;
- fixed schedule in a predictable combined-drift survival regime;
- generic memory under clean resume;
- conservative safety heuristics in some small subsystem-conflict regimes;
- task-local probing when hidden variables do not persist across contexts;
- greedy no-state behavior when risky action is always feasible.
- calibration memory without transfer when early outcomes do not imply a persistent state.

The selfhood-boundary probe adds negative controls: hidden external state improves control, and hidden internal diagnostic state improves report prediction, but neither counts as selfhood under the stricter boundary.

The architecture-convergence experiment keeps the illusion/optional hypothesis live because the best learners are still ordinary predictive learners. The self-equivalent component appears as an action-sensitive prediction statistic, not as a separate explicit self-object.

The learned bottleneck discovery experiment also keeps the illusion/optional hypothesis honest: the same shared bottleneck is learned for reusable world-state, so no learned latent should be called self-equivalent without causal boundary evidence.

The heterogeneous attractor precursor strengthens this caution: all five learner families also converge in the external shared-state scenario. Architecture convergence is therefore not sufficient for selfhood unless the converged latent has the right causal boundary.

The cross-environment precursor adds the same caution across surfaces: world-shared environments recur just as reliably as self-shared environments, so cross-environment recurrence is not enough without agent-boundary evidence.

The factorial precursor makes this caution sharper: world-shared regimes also produce 5/5 learner convergence in all four environments. Complete convergence is still not selfhood unless the latent is agent-bounded.

The raw history learning precursor preserves the same caution under weaker inputs: world-shared reward histories converge just as cleanly as agent-shared reward histories.

The delayed return policy precursor preserves it again: return-trained policies also converge cleanly on external shared state, so delayed-return success alone is not selfhood.

The evolved recurrent policy precursor makes the same point for recurrent hidden states: recurrent convergence alone is not selfhood unless the hidden state is agent-bounded.

The gradient recurrent policy precursor preserves the same caution under return-gradient training: recurrent hidden-state learning also converges on external shared variables, so the causal boundary remains decisive.

The model-based planning precursor preserves it again: learned reward models also discover reusable external state, so prediction-plus-planning is not sufficient for selfhood without the agent-boundary test.

The latent causal ablation precursor makes the caution sharper: external shared latents are causally important too. Causal importance alone is not selfhood unless the causally important latent is agent-bounded.

The counterfactual latent editing precursor preserves the same caution: external shared latents are also directionally editable. Editability alone is not selfhood unless the edited latent is agent-bounded.

Current interpretation: explicit selfhood is optional in many environments. Self-like behavior may emerge from lower-level predictive/control mechanisms. But when the hidden agent-state variable is agent-bounded, action-mediated, control-relevant, and causally active, the information is not merely a report artifact: interventions on it change behavior.

## Relationship To Consciousness

The current evidence is orthogonal to phenomenal consciousness.

The experiments produce non-conscious self-equivalent mechanisms:

- action-effect latent state;
- centered observation/action frame;
- capability-conditioned goal formation;
- viability estimates;
- active self-state information-seeking;
- counterfactual option-preservation;
- commitment ledgers;
- shared subsystem arbitration;
- cross-context state reuse;
- reuse-pressure scaling;
- horizon-pressure scaling;
- partial-observability belief scaling;
- learned noisy-observation filtering;
- recurrent observation filtering;
- unseeded recurrent filtering;
- mixed-sensor recurrent filtering;
- learned sensor-subspace filtering;
- active boundary discovery;
- action-effect boundary probing;
- persistent action-boundary probing;
- return-selected boundary probing;
- end-to-end recurrent boundary probing;
- architecture boundary stress testing;
- architecture horizon-pressure sweeping;
- architecture capacity probing;
- architecture soft-return optimization;
- architecture hard-return auditing;
- architecture hard-return horizon sweeping;
- architecture online return learning;
- architecture policy-gradient return learning;
- architecture policy-gradient seed sweeping;
- architecture policy-gradient budget sweeping;
- architecture Torch actor-critic learning;
- SSRM-3D embodied-world layering and visualization;
- SSRM-3D recurrent-observer representation learning;
- SSRM-3D learned-controller policy-state learning;
- SSRM-3D tool-making and externalized cognition;
- SSRM-3D social pressure and costly communication;
- SSRM-3D agent-continuity serialization;
- SSRM-3D learned-integration designed packet bridge;
- learned bottleneck discovery;
- sequence latent transfer;
- heterogeneous learner convergence;
- cross-environment boundary recurrence;
- factorial learner-environment convergence;
- raw reward-history learning;
- delayed-return memory policy learning;
- evolved recurrent hidden-state learning;
- gradient-trained recurrent hidden-state learning;
- model-based reward planning;
- latent causal ablation;
- counterfactual latent editing;
- predictive-state decodability.

These may be prerequisites for some conscious self models, consequences of richer conscious architectures, or independent computational tools. The project has not shown any consciousness result.

## Current Verdict

The strongest current explanation is:

> Selfhood is a conditional attractor in adaptive systems whose own hidden state is a persistent cause of future observations, future control, future value, and future coherence. The attractor need not be explicit or conscious. It can appear as any compact, causally useful representation that tracks the system as the continuing entity whose state mediates action through time.

This means:

- necessary in a weak computational sense when agent-bounded hidden `A_t` is required for optimal long-horizon control;
- not universally necessary across all tasks;
- often optional as an explicit architecture;
- compatible with illusion-style accounts if the "self" is a readout of lower-level predictive state;
- not supported by hidden external variables or passive internal diagnostics alone;
- currently orthogonal to consciousness.

## What Would Falsify This Theory

The theory weakens or fails if future experiments show that:

- generic predictive state consistently matches self models with equal compression and no decodable agent-state factor;
- hidden external-state trackers reproduce the claimed advantages, showing that the effect was generic latent-state modeling rather than selfhood;
- learned shared latents are called self-equivalent without a causal agent-boundary signature;
- sequence latents transfer equally in independent-hidden controls;
- heterogeneous learners converge on self-equivalent signatures in hidden external or independent-hidden controls;
- cross-environment recurrence appears without the agent-boundary signature;
- factorial learner-environment convergence appears without the agent-boundary signature;
- raw reward-history learners cannot separate external shared variables from agent-bounded variables by causal boundary probes;
- delayed-return policies cannot separate external shared variables from agent-bounded variables by causal boundary probes;
- evolved recurrent hidden states cannot separate external shared variables from agent-bounded variables by causal boundary probes;
- gradient-trained recurrent hidden states cannot separate external shared variables from agent-bounded variables by causal boundary probes;
- model-based planners cannot separate external shared variables from agent-bounded variables by causal boundary probes;
- latent ablations damage external shared variables as much as agent-bounded variables and are interpreted as selfhood without boundary evidence;
- counterfactual latent edits work for external shared variables and are interpreted as selfhood without boundary evidence;
- persistent internal variables improve passive prediction but not action, value, adaptation, or continuity;
- non-self fixed schedules or local heuristics scale to diverse hidden viability regimes;
- myopic or generic-memory agents preserve future action options under capability degradation with equal value;
- payoff-only goal selection matches self-capability goal formation when capability determines feasibility;
- local arbitration or conservative safety heuristics match self-coherence arbitration under subsystem conflict;
- task-local probing matches shared self-state when one persistent agent-state controls many contexts;
- shared self-state advantage does not grow as more contexts reuse the same hidden agent property;
- shared self-state advantage does not grow as more future steps reuse the same hidden agent property;
- shared self-belief does not improve as noisy evidence about persistent hidden agent-state becomes more reliable;
- learned noisy-observation filters select self cues in world, independent, or irrelevant controls;
- recurrent observation filters depend on the same channel across self, world, independent, and irrelevant controls;
- unseeded recurrent search fails to recover agent-channel dependence unless the accumulator is hand seeded;
- mixed-sensor recurrent search fails unless self/world evidence is exposed as named input channels;
- learned sensor-space ablation does not selectively damage shared-regime recurrent control, or damages independent/no-hidden controls just as much;
- owned-action alignment appears equally in world, independent, or irrelevant controls, or fails in self-hidden controls;
- controllable external state is classified as self-equivalent merely because it is action-controllable;
- detachable tool effects are classified as self-equivalent because they are controllable in one context;
- return selection favors persistent action-boundary policies in detachable-tool, passive-world, independent, or irrelevant controls;
- end-to-end recurrent policy states receive a persistent agent-boundary signature in detachable-tool, passive-world, independent, or irrelevant controls;
- strict architecture-wide convergence fails because most independently trained architectures fall back to local probing in shared regimes;
- increasing horizon fails to improve recoverability in shared regimes or produces strict convergence in controls for the wrong signature;
- supplied source-direction seeds cannot make weaker recurrent architectures recover the expected boundary signatures;
- stronger return optimization without source-direction seeds cannot recover the expected boundary signatures, loses them under objective-only restart selection, or produces false positives in controls;
- hard realized-return optimization never recovers the missing boundary signatures even with larger budgets or richer architectures;
- hard-return horizon sweeps show no recovery gradient at all, or produce false positives in controls;
- online return learners recover no shared-regime boundary signatures, or produce false positives in controls;
- policy-gradient learners fail to reproduce strict shared-regime convergence across seeds or produce control false positives;
- policy-gradient seed sweeps show convergence collapses toward local/no-hidden strategies in shared regimes;
- policy-gradient budget sweeps fail to repair seed instability or create control false positives under larger budgets;
- Torch actor-critic seed sweeps lose strict shared-regime convergence, disagree across CPU/MPS backends, or produce false positives in controls;
- SSRM-3D reactive or world-only agents scale through commitment, arbitration, and social pressure with equal value, or self-state ablation does not damage the layered agent;
- SSRM-3D recurrent observers fail to recover stronger self-state than frame-only observers under pressure, or self-state edits do not affect future-viability prediction;
- SSRM-3D learned recurrent controllers fail to beat frame-only controllers under pressure, or their policy states carry no decodable self-state;
- SSRM-3D model-only copies, memory transplants, body-state restores, or ambiguous forks match full continuity records across restore and fork pressure;
- SSRM-3D learned recurrent integration fails to beat frame-only control under tool, social, continuity, or attention pressure, or ablations produce generic rather than pressure-specific failures;
- world-only or action-history agents scale through hidden and drifting body frames without compact centered state;
- recurrent agents solve body drift, hidden viability, and corrupted continuity with no stable agent-state information;
- interventions on decoded agent-state variables do not change prediction or control;
- agents do not seek agent-state information when agent-state has expected control value;
- self-equivalent variables do not become more useful as horizon, drift, partial observability, and internal-state complexity increase.

## What Would Strengthen It

The attractor claim becomes stronger if:

- independently trained agents converge on decodable agent-state variables without self labels;
- the same latent tracks action-effect state, viability, and commitments across tasks;
- self-state variables improve transfer after new body/viability/memory perturbations;
- causal ablation of those variables selectively harms tasks that require them;
- the compression advantage grows with action-space size, horizon length, and internal-state dimensionality;
- multiple independently trained learner families converge on the same action-effect latent under self drift and not under world-only drift;
- agents selectively seek agent-state information when it improves future control, while seeking world-state or no information in matched controls;
- agents use self-state to preserve future action options when current actions can degrade future capability;
- agents converge on centered body-frame variables when observation and action coordinates must be transformed;
- agents use capability self-state to form feasible goals rather than merely attractive goals;
- agents use shared agent-state to arbitrate among competing subsystems when local proposals conflict;
- agents reuse the same agent-state abstraction across prediction, goal choice, future options, and coherence while switching to world-state or local probes in matched controls;
- agent-state decodability or value increases with the number of contexts controlled by the same hidden agent property;
- agent-state value increases with future horizon when the same hidden agent property persists across future steps;
- agent-state value increases as noisy evidence about persistent hidden agent-state becomes more reliable under partial observability;
- learned noisy-observation filters select agent-bounded cues from training histories without being given the posterior equation;
- recurrent observation filters show selective agent-channel ablation loss in agent-hidden regimes and not in matched controls;
- random-start recurrent filters recover the same agent/world/local/no-hidden boundary without seeded accumulator candidates;
- recurrent filters recover agent-bounded dependencies from mixed noisy sensors and source ablation separates self from world dependencies;
- learned sensor-space ablation selectively damages shared-regime recurrent control while boundary tests separate agent-bounded from external dependencies;
- active boundary discovery aligns outcome-predictive sensor directions with owned-action directions in self-hidden regimes and not in world-hidden controls;
- action-effect boundary probing rejects controllable external state when it aligns with a tool action but not the body/action-effect boundary;
- persistent action-boundary probing rejects detachable external state when action-effect alignment is transient rather than context-persistent;
- return selection recovers persistent, detachable, recurrent, local, and no-hidden boundary classes without supervised outcome-direction labels;
- end-to-end recurrent policy states recover persistent, detachable, passive, local, and no-hidden boundary classes without supplied action-boundary policies;
- architecture stress tests preserve the expected controls while identifying partial, not strict, recurrent-architecture convergence;
- architecture horizon-pressure sweeps show recoverability increasing with horizon while strict architecture convergence remains absent;
- architecture capacity probes show weaker recurrent architectures can represent the expected boundaries when source-direction seeds are supplied;
- architecture soft-return optimizers discover the expected boundaries without source-direction seeds or boundary-aware restart selection while controls reject shared recurrence and hidden state;
- hard-return audits identify whether task reward alone is sufficient for boundary discovery or merely selects useful hidden-state control;
- hard-return horizon sweeps show whether temporal pressure repairs hard-return boundary failures or only improves recurrence value;
- online return learners test whether objective-only sampled-return updates repair hard-return boundary failures;
- policy-gradient learners test whether sampled-return credit assignment can recover boundary signatures without smooth reward surrogates;
- policy-gradient seed sweeps test whether that recovery is robust or only seed-specific;
- policy-gradient budget sweeps test whether remaining seed failures are optimization-budget artifacts or persistent boundary failures;
- Torch actor-critic learners test whether neural recurrent sampled-return credit assignment reproduces the same boundaries across RNN, GRU, and LSTM architectures;
- SSRM-3D tests whether the same pressure gradient appears in a persistent embodied world with layered realtime control and a non-controller language module;
- SSRM-3D recurrent observers test whether embodied self-state can be recovered from traces without reading the hand-built workspace;
- SSRM-3D learned controllers test whether policy states trained without self labels recover self-state under embodied control pressure;
- SSRM-3D done-enough gates require learned control, tool-making or externalized cognition, real social pressure, and targeted ablation before the 3D track counts as done enough;
- modular LLM architecture separates persistent self-state control from slow language reasoning and defines direct-control, no-LLM, full-world, and corrupted-packet ablations;
- SSRM-3D tool-making tests whether return-selected agents externalize memory through markers, beacons, and alarms only when embodied confusion pressure requires it;
- SSRM-3D social pressure tests whether return-selected agents use reputation, vulnerability, identity memory, and shared-tool trust only when other agents have persistent memory and policies;
- SSRM-3D social ecology tests whether costly signals, names, gossip, and trust-maintenance check-ins are selected only when communication preserves future options under social memory;
- SSRM-3D agent continuity tests whether restored or forked agents preserve control only when the whole continuity record is serialized, with component ablations failing specifically where those components matter;
- SSRM-3D learned integration tests whether tool, social, continuity, and attention evidence move into recurrent policy state; current evidence is a designed packet bridge, and the no-leak randomized multi-seed follow-up preserves some bridges while rejecting stable strong integration;
- SSRM-3D structured perception tests whether cone/FOV vision and spatial audio create ablatable partial-observability pressure before raw pixels or waveform learning;
- SSRM-3D day/night sleep-rest tests whether rest becomes useful only when hidden fatigue, darkness, shelter timing, alarms, social watch, and interruption continuity create future-control tradeoffs;
- SSRM-3D illness/sanitation tests whether hunger, thirst, latent infection, contamination, quarantine/care, immunity, and continuity create targeted hidden-state pressure without full organism simulation;
- SSRM-3D weather/exposure tests whether cold, heat, rain, wind, drought, shelter, fire/light tools, water planning, and continuity become useful only when external conditions change the agent's future capability;
- learned bottlenecks emerge without self labels and are correctly separated into agent-state, world-state, local-hidden, and no-hidden cases by causal tests.
- sequence latents inferred from early outcomes transfer to held-out contexts and are separated into agent-state versus world-state by causal tests.
- heterogeneous learner families converge on the same latent causal signature while still separating agent-bounded latents from external shared latents.
- the same agent/world/local/no-hidden signatures recur across different environment surfaces.
- learner-family and environment-surface variation can be crossed while preserving the same causal boundary signatures.
- raw action-observation-reward histories recover the same causal boundary signatures without compact outcome labels.
- memory policies selected by delayed return recover the same causal boundary signatures.
- evolved recurrent hidden states recover the same causal boundary signatures.
- recurrent hidden states optimized by return gradients recover the same causal boundary signatures.
- learned reward models used for planning recover the same causal boundary signatures.
- learned latents produce selective causal ablation losses in agent-bounded regimes and not in independent/no-hidden controls.
- learned latents can be edited to produce predictable action-centered counterfactuals under the correct boundary signature.

## Current Research Status

The program has a coherent falsifiable theory and sixty-three toy experiment families, including an executable hidden-state boundary probe, a first architecture-convergence test, active self-information, counterfactual option-preservation, first-person frame integration, goal formation under capability, competing-subsystems arbitration, cross-context self-state reuse, reuse-pressure scaling, horizon-pressure scaling, partial-observability belief scaling, learned noisy-observation filtering, recurrent observation filtering, unseeded recurrent filtering, mixed-sensor recurrent filtering, learned sensor-subspace filtering, active boundary discovery, action-effect boundary probing, persistent action-boundary probing, return-selected boundary probing, end-to-end recurrent boundary probing, architecture boundary stress testing, architecture horizon-pressure sweeping, architecture capacity probing, architecture soft-return optimization, architecture hard-return auditing, architecture hard-return horizon sweeping, architecture online return learning, architecture policy-gradient return learning, architecture policy-gradient seed sweeping, architecture policy-gradient budget sweeping, architecture Torch actor-critic learning, SSRM-3D embodied-world layering, SSRM-3D recurrent-observer representation learning, SSRM-3D learned-controller policy-state learning, SSRM-3D tool-making/externalized-cognition pressure, SSRM-3D social-pressure identity/reputation pressure, SSRM-3D social-ecology costly-communication pressure, SSRM-3D agent-continuity restore/fork pressure, SSRM-3D learned-integration policy-state pressure, SSRM-3D no-leak integration pressure, SSRM-3D structured-perception pressure, SSRM-3D day/night sleep-rest pressure, SSRM-3D illness/sanitation pressure, SSRM-3D weather/exposure pressure, learned bottleneck discovery, sequence latent transfer, heterogeneous learner convergence, cross-environment boundary recurrence, factorial learner-environment convergence, raw reward-history learning, delayed-return memory policy learning, evolved recurrent hidden-state learning, gradient-trained recurrent hidden-state learning, model-based reward planning, latent causal ablation, and counterfactual latent editing. It does not yet prove a general law of adaptive systems.

The newest evidence adds weather/exposure as the fourth persistent-pressure layer. Weather machinery is rejected in mild clear control, but cold/rain exposure, heat/drought hydration, forecast storms, shelter timing, fire/light tools, and restore-time weather continuity become useful under matching pressures. This is still a designed control-state precursor, not learned weather planning, but it adds external conditions that matter because they change internal capability and future options.

The 3D track now has an explicit done-enough gate. Gate 1 has useful learned-control precursors, Gate 2 has a partial return-selected tool-making precursor plus a learned tool-memory bridge that is not yet stable under the no-leak margin test, Gate 3 has partial return-selected social-pressure and costly-communication precursors plus a learned social-memory bridge that fails the integrated-social no-leak test, and Gate 4 has continuity-record and packet-level learned continuity/attention precursors while still lacking full-world attention mixing, LLM stream, tool-building access, and richer social memory ablations in the embodied learned-control setting. Structured perception adds a prerequisite pressure layer for those gates: tools, attention, memory, and social cues have more work to do when vision and audio are partial. The modular LLM architecture report defines the LLM-stream part of that future ablation, including multi-rate control where ticks are implementation and subsystem frequencies are the architecture.

The next practical SSRM-3D step is narrower than the full attractor test: add tool/shelter degradation after the structured perception, sleep-rest, illness/sanitation, and weather/exposure layers. The rule remains that a variable stays only if removing it changes policy, memory, tools, social behavior, or continuity.

The broader next step is still to replace linear learners and hand-coded policies with richer independent learned architectures:

- recurrent predictors;
- bottlenecked world models;
- predictive-state representations;
- model-based RL agents;
- active-inference style agents.

The full Attractor Test should then vary architectures, learning methods, and environment families at the same time. The key question for those architectures is not whether they claim a self. It is whether they converge on the same decodable, compressed, stable, and causally necessary agent-state abstraction.
