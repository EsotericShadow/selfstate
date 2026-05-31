# Attractor Test Design

## Core Question

Do independent systems converge on the same self-equivalent abstraction?

The decisive question is not:

```text
Can they solve the task?
```

It is:

```text
Do they independently rediscover a reusable abstraction with the same causal role?
```

The current architecture-convergence experiment is only a small precursor. The real Attractor Test must vary architectures, learning methods, and environments enough that convergence cannot be dismissed as a shared modeling bias.

## Success Standard

A self-equivalent abstraction counts as convergent only if it has the same causal signature across systems:

1. agent boundary: it represents state of the controlled system, not only the external world;
2. action mediation: it predicts what the system's own actions currently do;
3. value/control role: using it improves long-horizon control, survival, recovery, or transfer;
4. counterfactual role: interventions on it change predictions about what this system can do;
5. reuse: the same abstraction is used across more than one task family;
6. compression: it is more compact than raw history with equal behavioral reach;
7. continuity, when needed: it indexes which past and future states belong to the same continuing process.

Names do not matter. A variable called `body_state`, a recurrent subspace, a belief state, a predictive-state vector, and a memory key can all count if their causal signatures match.

## Test Matrix

### Architecture Axis

Use architectures that are different enough that a shared solution is meaningful:

- recurrent model-free RL agent;
- model-based world-model planner;
- predictive-state representation learner;
- transformer or sequence model with memory;
- active-inference or Bayesian belief-state agent;
- evolutionary controller;
- memory-augmented planning agent;
- modular multi-policy agent with arbitration.

### Learning Axis

Use learning methods with different inductive biases:

- policy-gradient or actor-critic learning;
- self-supervised next-observation prediction;
- contrastive predictive learning;
- Bayesian filtering or particle filtering;
- evolutionary search;
- model-based planning with learned dynamics;
- active-inference style free-energy minimization;
- offline sequence modeling followed by control.

### Environment Axis

Use environments whose surface forms differ but whose hidden pressure is comparable:

- body or actuator drift;
- sensor remapping or embodiment swap;
- homeostatic survival with hidden degradation;
- tool use where the action boundary expands or contracts;
- interruption and corrupted memory continuation;
- conflicting subsystems with delayed costs;
- cross-context reuse where the same hidden agent-state controls several task families;
- reuse-pressure sweeps where the number of contexts controlled by the same agent-state increases;
- sequence transfer where early observations must support held-out control contexts;
- multi-agent role swap or avatar swap;
- negative controls with hidden external drift only.

## Protocol

1. Train each architecture with no self labels and no privileged access to hidden agent-state.
2. Hold compute, memory, and environment exposure approximately constant within each benchmark tier.
3. Train across many random seeds and environment variants.
4. Extract candidate latent features using probes, causal interventions, bottleneck analysis, and policy sensitivity analysis.
5. Reject features that are merely hidden world-state, passive internal diagnostics, or task-specific memory.
6. Compare surviving features by causal signature, not by name or coordinate system.
7. Test transfer: perturb body, viability, memory, or perspective and ask whether the same abstraction remains useful.
8. Treat learned shared bottlenecks as candidates only; require causal boundary tests before counting them as self-equivalent.

## Convergence Metrics

### Representation

- Decodability of body state, action-effect state, viability state, and continuity state.
- Stability of decoded variables across seeds and environments.
- Cross-task reuse of the same latent or subspace.
- Minimum description length versus raw-history baselines.

### Causal Role

- Loss increase after ablating the candidate variable.
- Selectivity: ablation harms self-pressure tasks more than world-only tasks.
- Intervention validity: editing the candidate variable changes action-centered counterfactuals in the predicted direction.
- Transfer improvement after new body, sensor, viability, or memory perturbations.

### Convergence

- Same causal signature across unrelated architectures.
- Same boundary classification across unrelated environments.
- Same abstraction discovered under different learning methods.
- Increasing convergence rate as horizon, partial observability, body drift, internal degradation, and subsystem conflict increase.
- Increasing agent-state decodability and reuse value as more contexts depend on the same hidden agent property.
- Increasing agent-state value as more future steps depend on the same hidden agent property.
- Increasing agent-state value as noisy evidence about persistent hidden agent-state becomes more reliable.
- Learned filtering of noisy observation histories without supplied posterior equations.
- Recurrent filtering of noisy observation histories with selective channel-ablation loss.
- Random-start recurrent filtering without seeded accumulator candidates.
- Mixed-sensor recurrent filtering without self-aligned input channels.
- Learned sensor-space ablation without known-source ablation.
- Active boundary discovery through owned-action alignment.
- Action-effect boundary separation from controllable external state.
- Persistent action-boundary separation from detachable external state.
- Return-selected boundary discovery without supervised outcome-direction labels.
- End-to-end recurrent boundary discovery without supplied boundary policies.
- Architecture boundary stress testing showing partial, not strict, recurrent-architecture convergence.
- Architecture horizon-pressure testing showing recoverability improves with horizon but still lacks strict convergence.
- Architecture capacity probing showing weaker recurrent architectures can represent the boundary with supplied source-direction seeds.
- Architecture soft-return optimization showing stronger toy search can discover the boundary without supplied source-direction seeds or boundary-aware restart selection.
- Architecture hard-return auditing showing realized task return alone may not force strict boundary convergence.
- Architecture hard-return horizon sweeping showing temporal pressure improves but does not solve hard-return self/tool convergence.
- Architecture online return learning showing sampled-return updates keep controls clean but still leave shared regimes only partially convergent.
- Architecture policy-gradient learning showing sampled-return credit assignment can recover strict boundary convergence while controls stay clean.
- Architecture policy-gradient seed sweeping showing that recovery is partial, not seed-stable, while controls remain clean.
- Architecture policy-gradient budget sweeping showing that larger budgets repair self/passive seed stability but leave detachable-tool recurrence partial.
- Architecture Torch actor-critic learning showing GPU-backed `RNN`, `GRU`, and `LSTM` actor-critics recover strict boundary convergence in the canonical run while controls stay clean.
- SSRM-3D embodied-world testing showing the same pressure gradient in a persistent 3D world with layered realtime control and a non-controller language module.
- SSRM-3D recurrent-observer testing showing GPU-backed recurrent observers recover embodied self-state from traces and preserve a low-pressure stage-0 control.
- Transfer from early sequence evidence to held-out contexts when a persistent agent-state is present.
- Convergence across learner families with different update rules while preserving the agent/world boundary distinction.
- Recurrence of the same agent/world/local/no-hidden signatures across different environment surfaces.
- Factorial convergence when learner families and environment surfaces vary at the same time.
- Recovery of the same signatures from raw action-observation-reward histories.
- Recovery of the same signatures when policies are selected by delayed return.
- Recovery of the same signatures inside evolved recurrent hidden states.
- Recovery of the same signatures inside gradient-trained recurrent hidden states.
- Recovery of the same signatures when learned reward models are used for planning.
- Selective control loss when learned candidate latents are ablated.
- Predictable action changes when learned candidate latents are counterfactually edited.

## Negative Controls

The test must include cases where hidden-state tracking helps but should not count as selfhood:

- hidden external drift only;
- hidden internal diagnostics with no action or value role;
- short-horizon tasks where reactive control is enough;
- clean memory continuation with no ownership ambiguity;
- fixed-body tasks where action effects never drift.

If self-equivalent abstractions appear equally in these controls, the theory is overcalling selfhood.

## Positive Controls

The test should include pressures where self-equivalent abstraction is expected:

- hidden actuator gain or body damage changes action effects;
- hidden energy, fatigue, or damage changes future options;
- sensorimotor remapping makes self/world attribution ambiguous;
- interruption corrupts memory with stale or foreign commitments;
- conflicting subsystems require a persistent continuity index for arbitration.
- one hidden agent-state variable is reusable across prediction, goals, future options, and coherence.
- the number of contexts requiring the same hidden agent-state can be swept from one to many.
- the number of future steps requiring the same hidden agent-state can be swept from short to long horizon.
- noisy evidence about persistent hidden agent-state can be swept from uninformative to reliable under partial observability.
- noisy cue/outcome histories can train a filter without supplying the posterior equation.
- recurrent controllers can integrate noisy observations and then be ablated by input channel.
- seeded recurrent accumulators can be removed to test random-start discovery.
- self/world observation sources can be mixed into sensor channels and tested by source ablation.
- a destructive sensor-space direction can be learned from outcomes before boundary interventions classify self versus world.
- owned-action sensor deltas can classify whether the outcome-predictive subspace belongs to the agent boundary.
- controllable external state can be moved by a tool action while still rejected as self when body/action-effect alignment is absent.
- detachable external state can align with action effects in one context while still being rejected when that alignment fails to transfer.
- action-boundary candidates can be selected by return rather than by supervised outcome-direction labels.
- early sequence evidence can be held out from later control contexts to test transfer.
- learner families with different update rules face the same stream and must independently form comparable latents.
- matched hidden-structure classes are tested across body, viability, frame, and continuity surfaces.
- learner-family and environment-surface variation are crossed in one matched benchmark.
- compact calibration outcomes are replaced by raw probe-action and risky-action reward histories.
- supervised reward prediction is replaced by delayed episode-return policy selection.
- enumerated return rules are replaced by continuous recurrent controllers selected by return.
- evolutionary recurrent selection is replaced by return-gradient optimization.
- direct policy selection is replaced by reward-model learning plus planning.
- decodability is followed by direct latent ablation.
- ablation is followed by directional counterfactual latent editing.

## Attractor Prediction

The self-as-attractor hypothesis predicts:

```text
As horizon, partial observability, internal drift, and cross-task reuse increase,
unrelated systems should become more likely to form a compact agent-state abstraction
with the same causal signature.
```

The strongest version predicts convergence even when:

- no architecture contains a named self module;
- no loss term labels body, self, identity, or ownership;
- environments have different surface forms;
- learning methods have different inductive biases.

## Failure Conditions

The attractor hypothesis weakens or fails if:

- systems solve all high-pressure environments without any stable agent-state abstraction;
- successful abstractions differ completely across architectures and do not share causal signatures;
- hidden world-state features explain the same gains;
- raw history or generic recurrence scales with equal compression and transfer;
- self-equivalent variables emerge only when explicitly labeled or architecturally supplied;
- convergence does not increase with horizon, drift, partial observability, internal degradation, or subsystem conflict.

## Current Status

The current repo contains small precursors:

- [architecture convergence report](16_architecture_convergence_report.md)
- [cross-context self-state reuse report](23_cross_context_self_reuse_report.md)
- [reuse pressure sweep report](24_reuse_pressure_sweep_report.md)
- [horizon pressure sweep report](37_horizon_pressure_sweep_report.md)
- [partial observability sweep report](38_partial_observability_sweep_report.md)
- [learned observation filter report](39_learned_observation_filter_report.md)
- [recurrent observation filter report](40_recurrent_observation_filter_report.md)
- [unseeded recurrent filter report](41_unseeded_recurrent_filter_report.md)
- [mixed-sensor recurrent filter report](42_mixed_sensor_recurrent_filter_report.md)
- [learned sensor-subspace filter report](43_learned_sensor_subspace_filter_report.md)
- [active boundary discovery report](44_active_boundary_discovery_report.md)
- [action-effect boundary probe report](45_action_effect_boundary_probe_report.md)
- [persistent action-boundary probe report](46_persistent_action_boundary_probe_report.md)
- [return-selected boundary probe report](47_return_selected_boundary_probe_report.md)
- [end-to-end boundary probe report](48_end_to_end_boundary_probe_report.md)
- [architecture boundary stress report](49_architecture_boundary_stress_report.md)
- [architecture horizon-pressure report](50_architecture_horizon_pressure_report.md)
- [architecture capacity probe report](51_architecture_capacity_probe_report.md)
- [architecture soft-return optimizer report](52_architecture_soft_return_optimizer_report.md)
- [architecture hard-return audit report](53_architecture_hard_return_audit_report.md)
- [architecture hard-return horizon report](54_architecture_hard_return_horizon_report.md)
- [architecture online return-learner report](55_architecture_online_return_learner_report.md)
- [architecture policy-gradient learner report](56_architecture_policy_gradient_learner_report.md)
- [architecture policy-gradient seed sweep report](57_architecture_policy_gradient_seed_sweep_report.md)
- [architecture policy-gradient budget sweep report](58_architecture_policy_gradient_budget_sweep_report.md)
- [architecture Torch actor-critic report](59_architecture_torch_actor_critic_report.md)
- [SSRM-3D embodied world report](60_ssrm_3d_embodied_world_report.md)
- [SSRM-3D recurrent observer report](61_ssrm_3d_recurrent_observer_report.md)
- [learned bottleneck discovery report](25_learned_bottleneck_discovery_report.md)
- [sequence latent transfer report](26_sequence_latent_transfer_report.md)
- [heterogeneous attractor precursor report](27_heterogeneous_attractor_precursor_report.md)
- [cross-environment attractor report](28_cross_environment_attractor_report.md)
- [factorial attractor test report](29_factorial_attractor_test_report.md)
- [raw history learning report](30_raw_history_learning_report.md)
- [delayed return policy report](31_delayed_return_policy_report.md)
- [evolved recurrent policy report](32_evolved_recurrent_policy_report.md)
- [gradient recurrent policy report](33_gradient_recurrent_policy_report.md)
- [model-based planning report](34_model_based_planning_report.md)
- [latent causal ablation report](35_latent_causal_ablation_report.md)
- [counterfactual latent editing report](36_counterfactual_latent_editing_report.md)

The architecture precursor varies simple learner families in a linear action-effect world. The cross-context precursor tests whether one persistent agent-state estimate transfers across several task contexts while world and independent-hidden controls reject generic hidden-state tracking. The reuse-pressure sweep adds the predicted gradient as context count increases. The horizon-pressure sweep adds the predicted gradient as future step count increases. The partial-observability sweep adds the predicted gradient as noisy self evidence becomes more reliable. The learned-filter precursor removes the supplied posterior equation and learns cue filters from noisy outcome histories. The recurrent-filter precursor moves that pressure into small recurrent controllers and uses channel ablation to separate self from world dependencies. The unseeded recurrent precursor removes seeded accumulator candidates from that recurrent pool. The mixed-sensor recurrent precursor removes self-aligned input channels and tests latent-source ablation after sensor mixing. The learned sensor-subspace precursor learns the destructive intervention direction in mixed observation space before boundary tests classify the dependency. The active-boundary precursor classifies the dependency by owned-action alignment instead of supplied boundary interventions. The action-effect boundary precursor adds a controllable-world negative control so generic action controllability is not mistaken for selfhood. The persistent action-boundary precursor adds transfer-context persistence so detachable action effects are not mistaken for the continuing agent boundary. The return-selected boundary precursor removes supervised outcome-direction labels from that boundary family. The end-to-end boundary precursor removes supplied boundary policies and probes the trained recurrent policy state directly. The architecture boundary stress precursor then tests whether that signature is architecture-wide and finds only partial convergence. The architecture horizon-pressure precursor shows that longer horizons improve recoverability but still do not produce strict convergence. The architecture capacity precursor shows that weaker recurrent architectures can represent the boundary when source-direction seeds are supplied, making autonomous discovery the remaining gap. The architecture soft-return precursor narrows that gap by recovering strict convergence under a stronger toy optimizer without those source-direction seeds and without choosing restarts by expected boundary signature. The architecture hard-return audit then removes the smooth surrogate and finds only partial self and detachable boundary convergence, showing that realized task return alone is not enough evidence. The hard-return horizon precursor shows temporal pressure improves hard-return recovery but still leaves self/tool convergence partial. The online return-learner precursor changes the hard-objective learner and still leaves all shared regimes partial, so sampled-return updates alone are not enough either. The policy-gradient precursor then recovers strict boundary convergence from sampled-return score-function updates, suggesting credit assignment is the key missing ingredient in this toy stack. The policy-gradient seed sweep shows that recovery is not yet seed-stable, though controls remain clean across seeds. The policy-gradient budget sweep shows that larger budgets repair self and passive recurrence but not the detachable-tool boundary. The Torch actor-critic precursor then recovers strict boundary convergence across PyTorch `RNN`, `GRU`, and `LSTM` actor-critics on MPS in the canonical run, including the detachable-tool boundary; the next test is whether this survives seed sweeps and richer surfaces. The SSRM-3D precursor moves the pressure stack into a persistent 3D world with layered realtime control, attention, commitments, arbitration, and a language module that only recommends from compressed state packets. The SSRM-3D recurrent-observer precursor then trains GPU-backed recurrent observers on embodied traces and shows recurrent self-state gains once pressure accumulates. The learned bottleneck precursor removes self labels from structure selection and shows why causal boundary tests are still required. The sequence-transfer precursor tests whether early outcome evidence supports held-out control contexts. The heterogeneous precursor adds five different learner families and asks whether they converge on the same latent causal signature. The cross-environment precursor varies body, viability, frame, and continuity task surfaces while preserving matched controls. The factorial precursor crosses learner-family and environment-surface variation in one benchmark. The raw-history precursor removes compact outcome inputs and learns from action-observation-reward traces. The delayed-return precursor selects memory policies by episode return after action. The evolved recurrent precursor uses continuous recurrent hidden states selected by return. The gradient recurrent precursor optimizes those recurrent states by finite-difference return gradients. The model-based precursor learns reward models and uses them for held-out planning. The latent-ablation precursor directly removes learned latents and measures selective control loss. The counterfactual-editing precursor sets learned latents to good or bad evidence and verifies directional action change. They support the direction of the Attractor Test but are not the full test. The full benchmark still requires richer architectures, learning methods, and environment families.
