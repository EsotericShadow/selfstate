# Formal Core

## Factorization

Model the environment as partially observable.

Let:

- `E_t` = external world state;
- `A_t` = agent-internal state, including body, sensors, actuators, energy, damage, competence, memory-relevant commitments, and policy-relevant parameters;
- `u_t` = action;
- `o_t` = observation;
- `r_t` = reward or viability signal.

Let `L_t` be the full set of hidden variables relevant to prediction or control. `L_t` may include external variables, internal but control-irrelevant variables, and agent-state variables. The selfhood question concerns only the subset `A_t` that belongs to the controlled system and mediates action, value, adaptation, or continuity.

The transition and observation structure is:

```text
E_{t+1}, A_{t+1} ~ P(E_{t+1}, A_{t+1} | E_t, A_t, u_t)
o_t ~ P(o_t | E_t, A_t)
r_t ~ P(r_t | E_t, A_t, u_t)
```

A world-only agent attempts to act using a statistic over `E_t` or over raw history without representing `A_t` as a separable causal factor.

A self-state agent maintains a belief:

```text
b^A_t = P(A_t | o_{1:t}, u_{1:t-1}, r_{1:t-1})
```

This belief does not need to be verbal, conscious, or labeled "self." It only needs to track the agent's own hidden state as a persistent cause of future outcomes.

## Anti-Tautology Boundary

The theory must not equate all hidden-state tracking with selfhood.

Tracking a hidden variable `z_t` is hidden-state modeling. It becomes self-equivalent only if `z_t` passes these boundary tests:

- agent boundary: `z_t` is a state of the controlled system, not only the external environment;
- persistence: `z_t` affects more than one observation/action cycle;
- action mediation: `P(E_{t+1}, A_{t+1} | E_t, A_t, u_t)` depends on `z_t` in a way that changes action effects, action costs, or available actions;
- control/value relevance: policy value changes when the agent conditions on `z_t`;
- counterfactual sensitivity: interventions on `z_t` change predictions about what this system can do;
- integration: the same information is reused across prediction, control, adaptation, or memory.

Continuity-like selfhood adds one further condition:

- ownership through time: `z_t` indexes which past and future states, commitments, or memories belong to the same continuing controlled process.

Therefore the posterior `P(A_t | history)` is not automatically a self. It is an agent-state estimate. It becomes self-equivalent when it is used as a reusable action-centered control abstraction.

## Necessity Claim

If future observations, rewards, or transition dynamics depend on hidden, changing `A_t`, then any Bayes-optimal long-horizon policy must encode information equivalent to a posterior over `A_t`.

In that case, agent-state information is necessary in the weak computational sense:

```text
pi*(u_t | history) requires information about P(A_t | history)
```

It becomes self-equivalent only when the anti-tautology boundary above is met. This does not imply that the representation is explicit, reportable, conscious, narrative, or human-like.

## Collapse Cases

The self-state collapses or becomes unnecessary when:

- `A_t` is fixed;
- `A_t` is fully observable from `o_t`;
- `A_t` has no effect on future observations, transitions, rewards, or viability;
- the hidden variable is external world-state rather than agent-state;
- the hidden variable is internal but only supports passive prediction or diagnostic reporting;
- the task horizon is too short for `A_t` to matter;
- a history-only predictive representation encodes the same information with equal compression and causal effectiveness.

These collapse cases are important because they prevent the theory from claiming that every controller has a meaningful self.

## Explicit Versus Implicit Self

An explicit self-model is one where `A_t` is represented in an interpretable or structured bottleneck.

An implicit self-model is one where the same information is distributed inside a recurrent state, predictive state representation, or memory system.

The experimental question is therefore not:

```text
Does the architecture contain a module named self?
```

The better question is:

```text
Does the learned representation contain causally useful, persistent information about the agent as a distinct stateful entity through time?
```

## Attractor Claim

Selfhood becomes an attractor under optimization when `A_t` has these properties:

- slow-changing relative to observations;
- reused across many predictions and tasks;
- action-contingent;
- hidden or partially observed;
- value-relevant;
- required for error attribution;
- required for counterfactual planning.

Under these conditions, representing `A_t` is often more compressed than re-deriving its effects from raw history each time.

The attractor pressure should increase with reuse. If the same hidden `A_t` is needed by `k` distinct prediction or control contexts, a shared belief over `A_t` should become more valuable as `k` grows. If those contexts depend on unrelated hidden variables, or on external `E_t` rather than agent-state, the pressure should shift to local probes or world-state instead.

A parallel horizon pressure should appear when the same hidden `A_t` controls many future time steps. The value of one persistent estimate should grow with the number of future decisions it informs. If each future step depends on an independent hidden variable, the pressure should shift to local probes. If all future steps depend on external `E_t`, the pressure should shift to world-state.

Partial-observability pressure should appear when evidence about `A_t` is noisy but reusable. As cue reliability rises, a shared posterior over persistent agent-state should become more valuable for future control. If the same evidence concerns external `E_t`, the pressure should shift to world-state. If each future step has an independent hidden condition, a shared belief should not help.

Learned filtering is a stricter partial-observability condition. If the posterior is not supplied, training histories should still make a reusable filter over `A_t` more valuable than local probing when the same hidden agent-state controls many future steps. If the predictive cue tracks `E_t`, the learned filter should be classified as world-state; if no shared cue predicts future control, the pressure should disappear.

Recurrent filtering is stricter again. If a recurrent state integrates noisy observations about `A_t`, then ablating the relevant observation channel should selectively damage control in agent-state regimes. The same recurrent dependency is external, not self-equivalent, when the ablated channel tracks `E_t`.

Unseeded recurrent filtering removes another shortcut. If random-start recurrent candidates still discover a useful filter over `A_t`, the attractor claim becomes less dependent on hand-supplied accumulator policies. The same boundary rule remains: recurrence is self-equivalent only when causal tests show agent-bounded dependence.

Mixed-sensor recurrent filtering removes the direct channel-label shortcut. If observations are mixtures of candidate agent-state and world-state evidence, a useful recurrent filter over `A_t` should still be recoverable when `A_t` controls future action. The boundary test must then ablate the latent source rather than a named sensor channel.

Learned sensor-subspace filtering removes part of the source-ablation shortcut. If the behaviorally relevant direction can be learned in observation space from outcome variation, then removing that learned projection should damage control without using source coordinates as the ablated object. Boundary interventions are still required to decide whether the damaged subspace tracks `A_t` or external `E_t`.

Active boundary discovery removes part of the boundary-intervention shortcut. If the outcome-predictive direction in observation space also aligns with the direction produced by the agent's own action, then the latent has an operational agent-boundary signature. A useful outcome-predictive direction with weak owned-action alignment remains external hidden-state tracking, not self-equivalent state.

The action-effect boundary probe adds a stricter controllability control. Some external variables are action-controllable, so generic action alignment is still too broad. A candidate self variable must align with the body/action-effect boundary, not merely with any action that can change a useful external state.

The persistent action-boundary probe adds a temporal/contextual condition. A detachable tool can be action-controllable in one context but disappear in transfer. A candidate self variable must align with an action-effect direction that persists as part of the continuing system across contexts.

Return-selected boundary probing removes the supervised outcome-direction shortcut. Candidate action-boundary policies are proposed from action-observation deltas and selected by return. A persistent boundary counts as self-equivalent only when it wins under agent-state pressure and remains separate from detachable, passive-world, local-hidden, and no-hidden controls.

End-to-end boundary probing removes the supplied boundary-policy shortcut. A recurrent policy is trained by return first; only afterward is its own policy state probed under persistent body-action and detachable-tool interventions. A learned hidden state counts as self-equivalent only if the trained controller needs recurrence and its policy state moves with the persistent agent/action boundary across contexts.

Architecture boundary stress testing separates recoverability from convergence. If only one architecture recovers the agent-boundary signature while others fall back to local probing, the evidence supports "possible learned self-equivalent state" but not a general architecture-independent attractor.

Architecture horizon-pressure sweeping adds the temporal-pressure condition to that stress test. If longer horizons increase recoverability but still fail to produce strict convergence, then horizon length is a real pressure on self-equivalent recurrence but not by itself a proof of architecture-independent necessity.

Architecture capacity probing distinguishes representation capacity from discovery. If supplied source-direction seeds make all recurrent architectures recover the boundary while random-start training does not, the live gap is not whether the boundary can be represented; it is whether adaptive systems independently discover it under realistic training pressure.

Architecture soft-return optimization narrows the discovery gap. If stronger return optimization from Gaussian starts recovers the same boundary signatures without supplied source-direction seeds or boundary-aware restart selection, the failure of weaker random-start search should be treated as optimizer weakness rather than evidence that the boundary must be hand-coded. The result remains a toy surrogate, not a proof of full online reinforcement-learning emergence.

Architecture hard-return auditing tests that caveat directly. If realized-return optimization without the smooth surrogate produces high-value recurrent controllers but only partial boundary convergence, then task reward alone is not sufficient evidence that the self-equivalent boundary abstraction has emerged. The boundary must still be tested causally.

Hard-return horizon sweeping tests whether temporal pressure repairs that failure. Longer horizons can increase recurrent value and recover passive external recurrence while still leaving self/tool boundary convergence partial. This separates "horizon makes hidden state valuable" from "horizon alone makes the self-equivalent boundary emerge."

Online return learning tests the same caveat under a different objective-only learner. If antithetic perturbation updates from sampled episode return keep controls clean but still recover only partial shared-regime boundary signatures, then the bottleneck is not merely batch search. It is evidence that online return success and hidden-state usefulness remain weaker than causal self-boundary emergence.

Policy-gradient learning adds a positive credit-assignment condition. If stochastic policy-gradient updates from sampled return recover strict boundary convergence across architectures while controls remain clean, then the hard-return limitation is not a general impossibility of sampled return. It points to the kind of credit assignment needed for return to shape recurrent state into a causal self/tool/world boundary.

Policy-gradient seed sweeping separates recoverability from seed-stable convergence. If controls remain clean across seeds but shared-regime strict convergence appears only in some seeds, then policy-gradient credit assignment is a plausible discovery mechanism but not yet an attractor law. The stronger claim requires seed-stable convergence or a principled account of the remaining failures.

Policy-gradient budget sweeping tests whether those failures are just small-budget optimization artifacts. If a larger budget repairs self-boundary seed stability while controls remain clean, the attractor claim strengthens for agent-bounded recurrence. If detachable-tool recurrence remains partial, the remaining gap is not generic hidden-state tracking; it is the harder distinction between the continuing agent boundary and detachable external action effects.

Torch actor-critic learning tests a stronger neural sampled-return learner. If independently trained `RNN`, `GRU`, and `LSTM` actor-critics recover the self-persistent, detachable-tool, and passive-world boundary signatures while independent-hidden and irrelevant controls stay clean, the evidence supports credit-assignment-driven boundary discovery rather than generic hidden-state tracking. This still remains a toy precursor, not a consciousness result or a general attractor law.

SSRM-3D tests whether the same formal pressure survives embodiment. The language module is not part of the fast control loop; it receives compressed state packets and only recommends. The self-equivalent variable remains the persistent control state that links hidden viability, capability, prediction error, commitments, attention, and arbitration to future action.

The SSRM-3D control stack should be treated as multi-rate. A tick is only the simulator clock. Reflexes, motor correction, perception, attention, self-state updates, goal arbitration, language reasoning, and memory consolidation should have different update frequencies. This matters formally because the self-state can be a slower persistent sufficient statistic while reflexes and motor control still require high-frequency loops.

The modular LLM architecture turns that boundary into an ablation claim. Removing the LLM should damage slow abstraction more than reflex survival; bypassing the arbiter with direct language-to-motor control should damage realtime control; corrupting the self packet should produce specific recommendation and arbitration errors. If those predictions fail, the separation between language reasoning and self-state control must be revised.

SSRM-3D tool-making tests whether useful control state can be externalized into the world. A marker, beacon, alarm, or cache is not self-state by itself. It supports the formal claim only when external structure is selected because it preserves future control under partial observability, and when removing tool access produces a specific loss in those pressure regimes but not in visible controls.

SSRM-3D social pressure tests whether the agent's own continuity becomes a social control variable. A model of other agents is not selfhood by itself. It supports the formal claim only when the tested agent must track its own vulnerability, reputation, obligations, and remembered identity because other agents can help, exploit, deceive, trade, or sabotage across time.

SSRM-3D social ecology tests whether communication becomes social infrastructure only when it has a control job. A signal, name, gossip report, or check-in is not selfhood by itself. It supports the formal claim only when costly communication is rejected in no-job controls and selected because persistent social memory changes the agent's future repair, cooperation, deception-resistance, or shared-tool options.

SSRM-3D agent continuity tests whether persistence is bound by a whole control record rather than model weights alone. A restored or forked agent supports the formal claim only when body state, model version, memory, social memory, commitments, event-log position, attention, hidden state, tools, goals, and branch identity are preserved or specifically ablated under pressures that require those components.

SSRM-3D learned integration tests whether those pressures can enter learned policy state. A recurrent controller supports the formal claim only when it beats a frame-only policy under delayed tool, social, continuity, or attention evidence and when the corresponding feature-group ablation produces a specific loss. The packet-level precursor supports only a designed-channel bridge: the seeded canonical rows pass, but scenario identity and feature-group structure are supplied. The no-leak follow-up removes scenario identity and randomizes pressure combinations; it partially falsifies stable integration because `single_tool` margins are weak and `integrated_social` is not ablation-stable.

SSRM-3D structured perception removes omniscient world state from the next pressure layer. Cone/FOV vision and spatial audio support the formal claim only when they change control under partial observability and fail under targeted ablations: no-vision, no-audio, no-direction audio, memory removal, tool-alarm removal, or body-state-blind perception. A raw camera or waveform is not required until structured event packets stop being sufficient.

SSRM-3D day/night sleep-rest treats rest as a control action, not a subjective state. Sleep supports the formal claim only when future control depends on hidden fatigue, darkness timing, safe-rest context, tool alarms, social watch, or continuity after interruption, and only if the daylight control rejects rest as unnecessary. Removing sleep, fatigue state, day/night state, shelter memory, alarm access, social watch, or continuity must produce specific losses in the matching regimes.

SSRM-3D illness/sanitation treats hunger, thirst, illness, contamination, care, quarantine, immunity, and sanitation as control variables, not biology. Illness supports the formal claim only when hidden internal state, delayed consequences, self/world error attribution, contamination memory, care/quarantine, or restore-time immunity history changes control, and only if the clean-resource control rejects health machinery as unnecessary.

SSRM-3D weather/exposure treats cold, heat, rain, wind, drought, shelter, fire/light, water planning, and continuity as control variables, not climate or subjective discomfort. Weather supports the formal claim only when external conditions change the agent's own future capability through accumulated exposure, hydration loss, shelter timing, tool use, or restore-time continuity, and only if mild controls reject weather machinery as unnecessary.

SSRM-3D tool/shelter degradation treats marker wear, shelter damage, alarm/cache decay, inspection, repair, spare parts, and continuity as control variables, not construction simulation. Maintenance supports the formal claim only when persistent external infrastructure changes the agent's own future capability through route confusion, exposure, resource loss, repair constraints, or restore-time continuity, and only if stable controls reject maintenance machinery as unnecessary.

SSRM-3D social trust/contracts treats promises, tool return, warnings, sharing, shelter repair debt, trust updates, ownership, communication, and continuity as control variables, not roleplay or society simulation. Contracts support the formal claim only when delayed social consequences change the agent's own future access, help, tool use, shelter safety, or social punishment, and only if visible controls reject contract machinery as unnecessary.

SSRM-3D predator/threat agents treats trackers, threat perception, self-vulnerability, sound/scent traces, stealth, shelter, alarms, social warning, fear-like control, and continuity as control variables, not predator biology. Threats support the formal claim only when they change the agent's own future viability through trace exposure, weakness, routine predictability, shelter/alarms, group defense, or restore-time memory, and only if safe controls reject threat machinery as unnecessary.

SSRM-3D resource ecology treats resource memory, regeneration/depletion, spoilage timing, migration tracking, restraint, cache management, sharing contracts, territory ownership, and continuity as control variables, not ecology simulation. Resource ecology supports the formal claim only when delayed resource consequences change the agent's own future viability, access, obligations, or restore-time continuity, and only if abundant controls reject ecology machinery as unnecessary.

SSRM-3D injury/disability adaptation treats capability self-state, motor adaptation, sensor compensation, infection management, repair access, help-seeking, compensation tools, route adaptation, and continuity as control variables, not biology or subjective suffering. Injury/disability supports the formal claim only when changed mobility, degraded senses, wound risk, social help, tools, or route feasibility changes the agent's own future control, and only if fixed-body controls reject disability machinery as unnecessary.

SSRM-3D development/skill learning treats skill memory, practice planning, capability self-state, fatigue management, injury adaptation, transfer modeling, teaching help, training tools, goal feasibility, and continuity as control variables, not growth simulation. Skill learning supports the formal claim only when changing competence alters the agent's own future action feasibility, and only if easy fixed-skill controls reject skill machinery as unnecessary.

SSRM-3D dependent care treats dependent state, identity memory, protection planning, resource sharing, repair care, teaching support, shelter coordination, promise commitments, social trust, priority arbitration, and continuity as control variables, not reproduction or roleplay. Dependent care supports the formal claim only when another persistent vulnerable agent changes the tested agent's own future options, obligations, resource use, social access, or restore-time control, and only if no-dependent controls reject care machinery as unnecessary.

SSRM-3D irreversible loss treats loss memory, value-at-risk estimation, replacement feasibility, caution control, tool/shelter/relationship preservation, memory backup, loss response, and continuity as control variables, not grief or subjective emotion. Irreversible loss supports the formal claim only when permanent loss changes the agent's own future option space, obligations, social access, memory state, or restore-time continuity, and only if reversible-wear controls reject loss machinery as unnecessary.

SSRM-3D affective control treats fear, stress, trust, frustration, affiliation, curiosity, guilt analogue, attention mixing, memory salience, risk modulation, communication bias, and continuity as control variables, not feelings or consciousness. Affective control supports the formal claim only when compact internal summaries change the agent's own attention, risk tolerance, communication, memory salience, repair behavior, information seeking, social access, or restore-time continuity, and only if calm controls reject affective machinery as unnecessary.

SSRM-3D physics-first benchmarking shifts the evidence surface from labeled pressure rows toward sensorimotor streams. A modular physics kernel supports the formal claim only if the learned controller receives physics-derived observations rather than scenario labels, generalizes to held-out worlds, and fails under targeted ablations of the causal inputs it actually uses. The current benchmark satisfies that foundation for offline recurrent decision learning, but it does not yet satisfy closed-loop deep reinforcement learning because the trained policy is not acting and updating inside the physics world.

SSRM-3D recurrent observation tests whether that variable can be recovered from traces rather than read from the hand-built workspace. A recurrent observer supports the formal claim only if its hidden state decodes agent variables, improves over a frame-only observer under pressure, and changes future-viability prediction when edited along the learned self-state direction.

SSRM-3D learned control tests the same pressure inside policy state. A learned controller supports the formal claim only if recurrence is not useful in the low-pressure stage, but becomes useful for control as hidden agent-state pressure accumulates, and the learned recurrent policy state contains decodable agent variables without self-label training. If action edits along that state remain weak, the result supports representation-for-control but not yet robust causal editability.

A learned shared bottleneck is still not enough. If an unlabeled learner discovers a compact latent `z_t`, it is self-equivalent only after causal tests show that `z_t` is agent-bounded. A reusable external variable can produce the same compression advantage without being a self variable.

Sequence transfer is a stricter version of reuse. Early observations can support later control only when they reveal a latent that persists across contexts. That latent remains only a candidate self variable until causal boundary tests show that it tracks `A_t` rather than `E_t`.

Heterogeneous convergence is stricter again. If different learner families infer latents with the same control role, the attractor hypothesis gains support. But convergence across learners is still not sufficient for selfhood: the converged latent must also satisfy the agent-boundary test, because external `E_t` can create the same shared prediction structure.

Cross-environment recurrence is another stricter test. If body, viability, frame, and continuity tasks all produce the same candidate signature, the attractor claim becomes less dependent on one environment surface. But recurrence across environments is still only candidate evidence until the latent is separated from external `E_t`, independent local hidden variables, and no-hidden controls.

The factorial version crosses learner families with environment surfaces. If many learners in many environments recover the same causal signature, the attractor claim is stronger than either axis alone. It still remains a precursor unless richer systems reproduce the same boundary without binary hidden-state scaffolding.

Raw-history learning weakens one remaining shortcut. The learner no longer receives a compact outcome variable; it receives action-observation-reward traces and must infer whether early rewards predict later control. A reward-history latent is still only self-equivalent after the same agent-boundary test.

Delayed-return policy learning weakens the signal again. The system selects memory rules by the return obtained after acting, not by supervised labels for each held-out context. A return-trained memory state is still only self-equivalent if it is agent-bounded and control relevant.

Evolved recurrent policy learning moves the representation into a continuous hidden state. The same boundary applies: a recurrent state is not a self because it is internal or persistent; it is self-equivalent only if it tracks agent-bounded state that mediates action and value.

Gradient recurrent policy learning changes the training method rather than the boundary. A recurrent state optimized by return gradients is still only self-equivalent when causal tests show that it tracks agent-bounded state rather than external shared state, independent local state, or no hidden state.

Model-based planning separates prediction from action choice. A learned reward model can discover a compact latent that supports held-out planning, but the latent is still only self-equivalent if causal tests show that it represents `A_t` rather than reusable external `E_t`.

Latent causal ablation adds an intervention criterion. If replacing a learned latent with a marginal model selectively damages held-out control, the latent is behaviorally causal. It becomes self-equivalent only when that causal latent is also agent-bounded.

Counterfactual latent editing adds directionality. If setting a learned latent to different values changes predicted action in the expected direction, the latent has action-centered counterfactual validity. It still becomes self-equivalent only when the editable latent is agent-bounded.

## Critical Test

Train agents without hand-coded self labels.

Then ask:

1. Can internal agent variables be decoded from the learned state?
2. Are those decoded variables stable across tasks?
3. Do interventions on those variables predictably change behavior?
4. Does removing or randomizing them impair adaptation/control?
5. Does the advantage increase with horizon, drift, partial observability, and internal-state complexity?

If yes, the self-as-attractor hypothesis gains support.

If no, the optional/illusion hypothesis gains support.
