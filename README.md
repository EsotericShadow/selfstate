# Why Does a Self Exist?

This repo holds a falsifiable research program for the question:

> When does representing "me" become more useful than representing "world state only"?

The working claim is deliberately narrow:

> A persistent self is not required for all prediction or control. It becomes computationally favored when an adaptive system must predict and regulate future outcomes that depend on its own hidden, changing internal state, body, capabilities, memory, and action effects across time.

Hidden-state tracking alone is not treated as selfhood. A hidden variable only becomes self-equivalent when it is agent-bounded, persistent, action-mediated, control/value relevant, counterfactually active, and reused across prediction or control.

That claim does not define consciousness and does not require that the self be metaphysically real. It treats "self" as a candidate predictive-control abstraction.

## Core Artifacts

- [Research brief](docs/01_research_brief.md): current strongest falsifiable explanation.
- [Literature map](docs/02_literature_map.md): source anchors and what each source can and cannot support.
- [Experimental program](docs/03_experimental_program.md): agent comparisons, environments, measurements, and failure tests.
- [Phenomenology to model variables](docs/04_phenomenology_to_model_variables.md): how the author's observations can generate model features without being treated as proof.
- [Formal core](docs/05_formal_core.md): a POMDP-style statement of when self-state is necessary.
- [Minimal experiment report](docs/06_minimal_experiment_report.md): first executable self/world attribution test and current results.
- [Representation search report](docs/07_representation_search_report.md): compression/model-selection test for whether self-equivalent variables are selected without self labels.
- [Predictive-state emergence report](docs/08_predictive_state_emergence_report.md): tests whether hidden self-state is decodable and causally useful from action-effect predictions alone.
- [Hidden viability survival report](docs/09_hidden_viability_survival_report.md): tests self as a long-horizon control variable for hidden energy/integrity.
- [Interruption coherence report](docs/10_interruption_coherence_report.md): tests self as a continuity and coherence index after interruption and memory corruption.
- [Current synthesis](docs/11_current_synthesis.md): integrated provisional theory and what would falsify it.
- [Evidence matrix](docs/12_evidence_matrix.md): claim-to-evidence map across all experiment families.
- [Online predictive learning report](docs/13_online_predictive_learning_report.md): tests whether prediction-error learning produces causally useful action-effect state without labels.
- [Hidden-state boundary attack](docs/14_hidden_state_boundary_attack.md): anti-tautology boundary between hidden-state tracking and selfhood.
- [Selfhood boundary probe report](docs/15_selfhood_boundary_probe_report.md): executable negative controls for hidden-state tracking that should not count as selfhood.
- [Architecture convergence report](docs/16_architecture_convergence_report.md): tests whether multiple unlabeled learner families converge on action-effect state under self-drift pressure.
- [Attractor test design](docs/17_attractor_test_design.md): full future benchmark design and current precursor stack.
- [Active self-information report](docs/18_active_self_information_report.md): tests whether agents seek self-state information when it has control value.
- [Counterfactual option preservation report](docs/19_counterfactual_option_preservation_report.md): tests self-preservation as preserving future action options.
- [First-person frame integration report](docs/20_first_person_frame_report.md): tests centered body-frame variables for observation/action integration.
- [Goal formation under capability report](docs/21_goal_formation_under_capability_report.md): tests self-state as a goal-feasibility filter.
- [Competing subsystems arbitration report](docs/22_competing_subsystems_arbitration_report.md): tests shared self-state as an arbitration variable under subsystem conflict.
- [Cross-context self-state reuse report](docs/23_cross_context_self_reuse_report.md): tests whether one persistent agent-state abstraction transfers across multiple control contexts.
- [Reuse pressure sweep report](docs/24_reuse_pressure_sweep_report.md): tests whether shared self-state advantage grows as more contexts reuse the same agent-state.
- [Horizon pressure sweep report](docs/37_horizon_pressure_sweep_report.md): tests whether shared self-state advantage grows as more future steps reuse the same agent-state.
- [Partial observability sweep report](docs/38_partial_observability_sweep_report.md): tests whether shared self-belief becomes useful as noisy evidence about persistent hidden agent-state becomes reliable.
- [Learned observation filter report](docs/39_learned_observation_filter_report.md): tests whether noisy cue/outcome histories can train a reusable agent-state filter without a supplied posterior equation.
- [Recurrent observation filter report](docs/40_recurrent_observation_filter_report.md): tests whether small recurrent controllers learn causally ablatable filters over noisy self or world evidence.
- [Unseeded recurrent filter report](docs/41_unseeded_recurrent_filter_report.md): tests whether random-start recurrent search recovers the same boundary without seeded accumulator candidates.
- [Mixed-sensor recurrent filter report](docs/42_mixed_sensor_recurrent_filter_report.md): tests whether random-start recurrent search recovers agent/world source dependencies from mixed noisy sensors.
- [Learned sensor-subspace filter report](docs/43_learned_sensor_subspace_filter_report.md): tests whether the damaging intervention direction can be learned in mixed sensor space without known-source ablation.
- [Active boundary discovery report](docs/44_active_boundary_discovery_report.md): tests whether the learned outcome-predictive subspace aligns with an owned-action effect before counting as self-equivalent.
- [Action-effect boundary probe report](docs/45_action_effect_boundary_probe_report.md): tests whether controllable external state is rejected when it lacks body/action-effect alignment.
- [Persistent action-boundary probe report](docs/46_persistent_action_boundary_probe_report.md): tests whether detachable external action effects are rejected when action-effect alignment does not persist across contexts.
- [Return-selected boundary probe report](docs/47_return_selected_boundary_probe_report.md): tests whether return selection can recover persistent action-boundary structure without supervised outcome-direction labels.
- [End-to-end boundary probe report](docs/48_end_to_end_boundary_probe_report.md): tests whether trained recurrent policy states recover persistent action-boundary structure without supplied boundary policies.
- [Architecture boundary stress report](docs/49_architecture_boundary_stress_report.md): tests whether the end-to-end boundary signature converges across independently trained recurrent architectures.
- [Architecture horizon-pressure report](docs/50_architecture_horizon_pressure_report.md): tests whether longer horizons improve cross-architecture boundary convergence.
- [Architecture capacity probe report](docs/51_architecture_capacity_probe_report.md): tests whether weaker recurrent architectures can represent the boundary when source-direction seeds are supplied.
- [Architecture soft-return optimizer report](docs/52_architecture_soft_return_optimizer_report.md): tests whether stronger return optimization discovers the boundary without supplied source-direction seeds.
- [Architecture hard-return audit report](docs/53_architecture_hard_return_audit_report.md): tests whether hard realized return alone recovers the same boundary without the smooth surrogate.
- [Architecture hard-return horizon report](docs/54_architecture_hard_return_horizon_report.md): tests whether longer horizons repair hard-return boundary failure.
- [Architecture online return-learner report](docs/55_architecture_online_return_learner_report.md): tests whether an online-style objective-only return learner repairs hard-return boundary failure.
- [Architecture policy-gradient learner report](docs/56_architecture_policy_gradient_learner_report.md): tests whether stochastic policy-gradient learning recovers the missing boundary signatures.
- [Architecture policy-gradient seed sweep report](docs/57_architecture_policy_gradient_seed_sweep_report.md): tests whether policy-gradient boundary recovery is seed-stable.
- [Architecture policy-gradient budget sweep report](docs/58_architecture_policy_gradient_budget_sweep_report.md): tests whether larger policy-gradient budgets repair seed instability.
- [Architecture Torch actor-critic report](docs/59_architecture_torch_actor_critic_report.md): tests whether GPU-backed recurrent actor-critic learners recover the boundary signatures.
- [SSRM-3D embodied world report](docs/60_ssrm_3d_embodied_world_report.md): tests the same pressures in a persistent 3D world with layered realtime control and visualization.
- [SSRM-3D recurrent observer report](docs/61_ssrm_3d_recurrent_observer_report.md): tests whether GPU-backed recurrent observers recover self-state from embodied traces.
- [SSRM-3D learned controller report](docs/62_ssrm_3d_learned_controller_report.md): tests whether recurrent controllers trained without self labels use self-state under embodied pressure.
- [SSRM-3D done-enough gates](docs/63_ssrm_3d_done_enough_gates.md): defines the four gates still needed before the 3D track counts as done enough.
- [Modular LLM architecture report](docs/64_modular_llm_architecture_report.md): separates persistent self-state control from slow language reasoning and defines LLM ablation predictions.
- [SSRM-3D tool-making report](docs/65_ssrm_3d_tool_making_report.md): tests whether return-selected agents discover external markers, beacons, alarms, or caches under embodied confusion pressure.
- [SSRM-3D social pressure report](docs/66_ssrm_3d_social_pressure_report.md): tests whether return-selected agents use identity memory, reputation, vulnerability, and shared-tool state under real social pressure.
- [SSRM-3D social ecology report](docs/67_ssrm_3d_social_ecology_report.md): tests when costly signals, names, gossip, and trust-maintenance check-ins become useful social infrastructure.
- [SSRM-3D agent continuity report](docs/68_ssrm_3d_agent_continuity_report.md): tests what must be serialized for a restored or forked agent to remain the same continuing control process.
- [SSRM-3D learned integration controller report](docs/69_ssrm_3d_learned_integration_controller_report.md): tests whether designed tool, social, continuity, and attention packet channels move into learned recurrent policy state while keeping the result bounded as a packet bridge.
- [SSRM-3D no-leak integration sweep report](docs/73_ssrm_3d_no_leak_integration_sweep_report.md): removes scenario identity leakage, randomizes pressure combinations, and records the partial negative multi-seed result.
- [Repository weakness audit](docs/70_repo_weakness_audit.md): records the strongest current objections, including the Report 69 shortcut and the unstable attractor claim.
- [Live demo MVP plan](docs/71_live_demo_mvp_plan.md): defines the smallest 3D demonstration where an agent can reject a user command for continuity-grounded reasons.
- [Framework extraction plan](docs/72_framework_extraction_plan.md): identifies reusable primitives such as `AgentContinuityRecord`, `AttentionMixer`, `Arbiter`, `EventLog`, `WorldSnapshot`, `LLMPacketBoundary`, and `MultiRateScheduler`.
- [SSRM-3D persistent pressure layer spec](docs/74_ssrm_3d_persistent_pressure_layer_spec.md): defines the next narrow realism layer: structured perception, sleep/rest, illness/sanitation, weather/exposure, tool/shelter degradation, affective control state, and falsifiers.
- [SSRM-3D structured perception report](docs/75_ssrm_3d_structured_perception_report.md): tests cone/FOV vision and spatial audio as ablatable partial-observability pressure before raw pixels or waveform learning.
- [SSRM-3D day/night sleep-rest report](docs/76_ssrm_3d_day_night_sleep_report.md): tests sleep as a vulnerable control action under fatigue, darkness, shelter timing, alarms, social watch, and interruption continuity.
- [SSRM-3D illness/sanitation report](docs/77_ssrm_3d_illness_sanitation_report.md): tests hunger, thirst, latent illness, contamination, clean water, quarantine/care, immunity, and continuity as abstract control pressure.
- [SSRM-3D weather/exposure report](docs/78_ssrm_3d_weather_exposure_report.md): tests cold, heat, rain, wind, drought, shelter, fire/light, water planning, and continuity as abstract control pressure.
- [SSRM-3D tool/shelter degradation report](docs/79_ssrm_3d_tool_shelter_degradation_report.md): tests marker wear, shelter damage, alarm/cache decay, inspection, repair, spare parts, and continuity as abstract control pressure.
- [Learned bottleneck discovery report](docs/25_learned_bottleneck_discovery_report.md): tests whether shared latent structure can be learned without self labels and then separated by causal boundary.
- [Sequence latent transfer report](docs/26_sequence_latent_transfer_report.md): tests whether an unlabeled sequence state inferred from calibration outcomes transfers to held-out contexts.
- [Heterogeneous attractor precursor report](docs/27_heterogeneous_attractor_precursor_report.md): tests whether several learner families converge on the same latent causal signature.
- [Cross-environment attractor report](docs/28_cross_environment_attractor_report.md): tests whether the same causal signatures recur across different task surfaces.
- [Factorial attractor test report](docs/29_factorial_attractor_test_report.md): crosses learner-family and environment-surface variation in one precursor.
- [Raw history learning report](docs/30_raw_history_learning_report.md): tests whether reward-history learners recover the same boundary without compact outcome inputs.
- [Delayed return policy report](docs/31_delayed_return_policy_report.md): tests whether return-trained memory policies recover the same boundary after acting.
- [Evolved recurrent policy report](docs/32_evolved_recurrent_policy_report.md): tests whether continuous recurrent controllers recover the same boundary after return-based selection.
- [Gradient recurrent policy report](docs/33_gradient_recurrent_policy_report.md): tests whether finite-difference return gradients recover the same recurrent boundary.
- [Model-based planning report](docs/34_model_based_planning_report.md): tests whether learned reward models recover the same boundary before planning held-out action.
- [Latent causal ablation report](docs/35_latent_causal_ablation_report.md): tests whether removing learned latents selectively damages control.
- [Counterfactual latent editing report](docs/36_counterfactual_latent_editing_report.md): tests whether editing learned latents predictably changes planned action.

## Running Experiments

Run the full canonical evidence stack:

```bash
python3 scripts/run_experiments.py
```

This writes `artifacts/experiment_manifest.json` and regenerates all canonical result files.

```bash
python3 experiments/self_world_attribution.py --episodes 500 --seed 20260530 --max-action 15
```

This writes:

- `artifacts/self_world_attribution_summary.csv`
- `artifacts/self_world_attribution_results.json`

```bash
python3 experiments/representation_search.py --episodes 500 --seed 20260530 --max-action 15 --calibration-samples 8
```

This writes:

- `artifacts/representation_search_model_summary.csv`
- `artifacts/representation_search_category_summary.csv`
- `artifacts/representation_search_results.json`

```bash
python3 experiments/predictive_state_emergence.py --episodes 500 --seed 20260530 --max-action 15 --calibration-samples 7 --control-horizon 10
```

This writes:

- `artifacts/predictive_state_probe_summary.csv`
- `artifacts/predictive_state_control_summary.csv`
- `artifacts/predictive_state_emergence_results.json`

```bash
python3 experiments/hidden_viability_survival.py --episodes 500 --seed 20260530 --horizon 80
```

This writes:

- `artifacts/hidden_viability_summary.csv`
- `artifacts/hidden_viability_results.json`

```bash
python3 experiments/interruption_coherence.py --episodes 500 --seed 20260530 --own-commitments 6 --action-budget 9
```

This writes:

- `artifacts/interruption_coherence_summary.csv`
- `artifacts/interruption_coherence_results.json`

```bash
python3 experiments/online_predictive_learning.py --episodes 500 --seed 20260530 --max-action 15 --calibration-steps 14 --control-steps 12
```

This writes:

- `artifacts/online_predictive_learning_summary.csv`
- `artifacts/online_predictive_learning_results.json`

```bash
python3 experiments/selfhood_boundary_probe.py --episodes 500 --seed 20260530 --horizon 24
```

This writes:

- `artifacts/selfhood_boundary_summary.csv`
- `artifacts/selfhood_boundary_results.json`

```bash
python3 experiments/architecture_convergence.py --episodes 500 --seed 20260530 --max-action 15 --calibration-steps 14 --control-steps 12
```

This writes:

- `artifacts/architecture_convergence_summary.csv`
- `artifacts/architecture_convergence_verdict.csv`
- `artifacts/architecture_convergence_results.json`

```bash
python3 experiments/active_self_information.py --replicates 300 --bandit-episodes 1000 --value-samples 4000 --final-window 200 --inspect-cost 1.0 --seed 20260530
```

This writes:

- `artifacts/active_self_information_plan_values.csv`
- `artifacts/active_self_information_bandit_summary.csv`
- `artifacts/active_self_information_results.json`

```bash
python3 experiments/counterfactual_option_preservation.py --episodes 500 --horizon 64 --seed 20260530
```

This writes:

- `artifacts/counterfactual_option_preservation_summary.csv`
- `artifacts/counterfactual_option_preservation_verdict.csv`
- `artifacts/counterfactual_option_preservation_results.json`

```bash
python3 experiments/first_person_frame_integration.py --episodes 500 --horizon 36 --drift-step 5 --target-radius 12 --seed 20260530
```

This writes:

- `artifacts/first_person_frame_summary.csv`
- `artifacts/first_person_frame_verdict.csv`
- `artifacts/first_person_frame_results.json`

```bash
python3 experiments/goal_formation_under_capability.py --episodes 500 --seed 20260530
```

This writes:

- `artifacts/goal_formation_under_capability_summary.csv`
- `artifacts/goal_formation_under_capability_verdict.csv`
- `artifacts/goal_formation_under_capability_results.json`

```bash
python3 experiments/competing_subsystems_arbitration.py --episodes 500 --horizon 14 --seed 20260530
```

This writes:

- `artifacts/competing_subsystems_arbitration_summary.csv`
- `artifacts/competing_subsystems_arbitration_verdict.csv`
- `artifacts/competing_subsystems_arbitration_results.json`

```bash
python3 experiments/cross_context_self_reuse.py --episodes 500 --seed 20260531
```

This writes:

- `artifacts/cross_context_self_reuse_summary.csv`
- `artifacts/cross_context_self_reuse_verdict.csv`
- `artifacts/cross_context_self_reuse_results.json`

```bash
python3 experiments/reuse_pressure_sweep.py --episodes 500 --seed 20260531 --max-contexts 6
```

This writes:

- `artifacts/reuse_pressure_sweep_summary.csv`
- `artifacts/reuse_pressure_sweep_verdict.csv`
- `artifacts/reuse_pressure_sweep_results.json`

```bash
python3 experiments/horizon_pressure_sweep.py --episodes 500 --seed 20260602 --max-horizon 12
```

This writes:

- `artifacts/horizon_pressure_sweep_summary.csv`
- `artifacts/horizon_pressure_sweep_verdict.csv`
- `artifacts/horizon_pressure_sweep_results.json`

```bash
python3 experiments/partial_observability_sweep.py --episodes 500 --seed 20260602 --horizon 6 --evidence-samples 3 --min-accuracy 0.50 --max-accuracy 0.95 --accuracy-step 0.05
```

This writes:

- `artifacts/partial_observability_sweep_summary.csv`
- `artifacts/partial_observability_sweep_verdict.csv`
- `artifacts/partial_observability_sweep_results.json`

```bash
python3 experiments/learned_observation_filter.py --episodes 500 --training-episodes 800 --seed 20260603 --horizon 8 --evidence-samples 7 --cue-accuracy 0.85
```

This writes:

- `artifacts/learned_observation_filter_summary.csv`
- `artifacts/learned_observation_filter_training.csv`
- `artifacts/learned_observation_filter_boundary.csv`
- `artifacts/learned_observation_filter_verdict.csv`
- `artifacts/learned_observation_filter_results.json`

```bash
python3 experiments/recurrent_observation_filter.py --episodes 500 --training-episodes 800 --seed 20260603 --horizon 8 --evidence-samples 9 --cue-accuracy 0.85 --random-candidates 500
```

This writes:

- `artifacts/recurrent_observation_filter_summary.csv`
- `artifacts/recurrent_observation_filter_training.csv`
- `artifacts/recurrent_observation_filter_dependency.csv`
- `artifacts/recurrent_observation_filter_verdict.csv`
- `artifacts/recurrent_observation_filter_results.json`

```bash
python3 experiments/unseeded_recurrent_filter.py --episodes 500 --training-episodes 800 --seed 20260603 --horizon 8 --evidence-samples 9 --cue-accuracy 0.85 --random-candidates 1500
```

This writes:

- `artifacts/unseeded_recurrent_filter_summary.csv`
- `artifacts/unseeded_recurrent_filter_training.csv`
- `artifacts/unseeded_recurrent_filter_dependency.csv`
- `artifacts/unseeded_recurrent_filter_verdict.csv`
- `artifacts/unseeded_recurrent_filter_results.json`

```bash
python3 experiments/mixed_sensor_recurrent_filter.py --episodes 500 --training-episodes 800 --seed 20260603 --horizon 8 --evidence-samples 9 --cue-accuracy 0.85 --random-candidates 1800
```

This writes:

- `artifacts/mixed_sensor_recurrent_filter_summary.csv`
- `artifacts/mixed_sensor_recurrent_filter_training.csv`
- `artifacts/mixed_sensor_recurrent_filter_dependency.csv`
- `artifacts/mixed_sensor_recurrent_filter_verdict.csv`
- `artifacts/mixed_sensor_recurrent_filter_results.json`

```bash
python3 experiments/learned_sensor_subspace_filter.py --episodes 500 --training-episodes 800 --seed 20260603 --horizon 8 --evidence-samples 9 --cue-accuracy 0.85 --random-candidates 1800
```

This writes:

- `artifacts/learned_sensor_subspace_filter_summary.csv`
- `artifacts/learned_sensor_subspace_filter_training.csv`
- `artifacts/learned_sensor_subspace_filter_dependency.csv`
- `artifacts/learned_sensor_subspace_filter_verdict.csv`
- `artifacts/learned_sensor_subspace_filter_results.json`

```bash
python3 experiments/active_boundary_discovery.py --episodes 500 --training-episodes 800 --seed 20260603 --horizon 8 --evidence-samples 9 --cue-accuracy 0.85 --random-candidates 1800
```

This writes:

- `artifacts/active_boundary_discovery_summary.csv`
- `artifacts/active_boundary_discovery_training.csv`
- `artifacts/active_boundary_discovery_boundary.csv`
- `artifacts/active_boundary_discovery_verdict.csv`
- `artifacts/active_boundary_discovery_results.json`

```bash
python3 experiments/action_effect_boundary_probe.py --episodes 500 --training-episodes 800 --seed 20260603 --horizon 8 --evidence-samples 9 --cue-accuracy 0.85 --random-candidates 1800
```

This writes:

- `artifacts/action_effect_boundary_probe_summary.csv`
- `artifacts/action_effect_boundary_probe_training.csv`
- `artifacts/action_effect_boundary_probe_boundary.csv`
- `artifacts/action_effect_boundary_probe_verdict.csv`
- `artifacts/action_effect_boundary_probe_results.json`

```bash
python3 experiments/persistent_action_boundary_probe.py --episodes 500 --training-episodes 800 --seed 20260603 --horizon 8 --evidence-samples 9 --cue-accuracy 0.85 --random-candidates 1800
```

This writes:

- `artifacts/persistent_action_boundary_probe_summary.csv`
- `artifacts/persistent_action_boundary_probe_training.csv`
- `artifacts/persistent_action_boundary_probe_boundary.csv`
- `artifacts/persistent_action_boundary_probe_verdict.csv`
- `artifacts/persistent_action_boundary_probe_results.json`

```bash
python3 experiments/return_selected_boundary_probe.py --episodes 500 --training-episodes 800 --seed 20260603 --horizon 8 --evidence-samples 9 --cue-accuracy 0.85 --random-candidates 1800
```

This writes:

- `artifacts/return_selected_boundary_probe_summary.csv`
- `artifacts/return_selected_boundary_probe_training.csv`
- `artifacts/return_selected_boundary_probe_verdict.csv`
- `artifacts/return_selected_boundary_probe_results.json`

```bash
python3 experiments/end_to_end_boundary_probe.py --episodes 500 --training-episodes 800 --seed 20260603 --horizon 8 --evidence-samples 9 --cue-accuracy 0.85 --random-candidates 1800
```

This writes:

- `artifacts/end_to_end_boundary_probe_summary.csv`
- `artifacts/end_to_end_boundary_probe_training.csv`
- `artifacts/end_to_end_boundary_probe_boundary.csv`
- `artifacts/end_to_end_boundary_probe_verdict.csv`
- `artifacts/end_to_end_boundary_probe_results.json`

```bash
python3 experiments/architecture_boundary_stress.py --episodes 500 --training-episodes 800 --seed 20260603 --horizon 8 --evidence-samples 9 --cue-accuracy 0.85 --random-candidates 1800
```

This writes:

- `artifacts/architecture_boundary_stress_summary.csv`
- `artifacts/architecture_boundary_stress_verdict.csv`
- `artifacts/architecture_boundary_stress_results.json`

```bash
python3 experiments/architecture_horizon_pressure_sweep.py --horizons 2,4,8,16 --episodes 250 --training-episodes 400 --seed 20260603 --evidence-samples 9 --cue-accuracy 0.85 --random-candidates 900
```

This writes:

- `artifacts/architecture_horizon_pressure_summary.csv`
- `artifacts/architecture_horizon_pressure_verdict.csv`
- `artifacts/architecture_horizon_pressure_results.json`

```bash
python3 experiments/architecture_capacity_probe.py --episodes 500 --training-episodes 800 --seed 20260603 --horizon 8 --evidence-samples 9 --cue-accuracy 0.85
```

This writes:

- `artifacts/architecture_capacity_probe_summary.csv`
- `artifacts/architecture_capacity_probe_verdict.csv`
- `artifacts/architecture_capacity_probe_results.json`

```bash
python3 experiments/architecture_soft_return_optimizer.py --episodes 300 --training-episodes 400 --seed 20260603 --horizon 8 --evidence-samples 9 --cue-accuracy 0.85 --iterations 16 --population 220 --restarts 10 --temperature 2.5 --initial-std 1.4
```

This writes:

- `artifacts/architecture_soft_return_optimizer_summary.csv`
- `artifacts/architecture_soft_return_optimizer_verdict.csv`
- `artifacts/architecture_soft_return_optimizer_results.json`

```bash
python3 experiments/architecture_hard_return_audit.py --episodes 300 --training-episodes 400 --seed 20260603 --horizon 8 --evidence-samples 9 --cue-accuracy 0.85 --iterations 16 --population 220 --restarts 10 --initial-std 1.4
```

This writes:

- `artifacts/architecture_hard_return_audit_summary.csv`
- `artifacts/architecture_hard_return_audit_verdict.csv`
- `artifacts/architecture_hard_return_audit_results.json`

```bash
python3 experiments/architecture_hard_return_horizon_sweep.py --horizons 2,4,8,16 --episodes 180 --training-episodes 240 --seed 20260603 --evidence-samples 9 --cue-accuracy 0.85 --iterations 8 --population 120 --restarts 5 --initial-std 1.4
```

This writes:

- `artifacts/architecture_hard_return_horizon_summary.csv`
- `artifacts/architecture_hard_return_horizon_verdict.csv`
- `artifacts/architecture_hard_return_horizon_results.json`

```bash
python3 experiments/architecture_online_return_learner.py --episodes 160 --training-episodes 220 --validation-episodes 120 --batch-episodes 90 --seed 20260604 --horizon 8 --evidence-samples 9 --cue-accuracy 0.85 --epochs 16 --perturbations 50 --restarts 4 --sigma 0.45 --learning-rate 0.07 --initial-std 0.8 --lr-decay 0.94 --sigma-decay 0.96 --min-sigma 0.06
```

This writes:

- `artifacts/architecture_online_return_learner_summary.csv`
- `artifacts/architecture_online_return_learner_verdict.csv`
- `artifacts/architecture_online_return_learner_results.json`

```bash
python3 experiments/architecture_policy_gradient_learner.py --episodes 200 --training-episodes 400 --validation-episodes 240 --batch-episodes 128 --seed 20260605 --horizon 8 --evidence-samples 9 --cue-accuracy 0.85 --epochs 32 --restarts 5 --temperature 1.8 --learning-rate 0.12 --lr-decay 0.96 --initial-std 0.8 --finite-diff-epsilon 0.02 --max-grad-norm 4.0
```

This writes:

- `artifacts/architecture_policy_gradient_learner_summary.csv`
- `artifacts/architecture_policy_gradient_learner_verdict.csv`
- `artifacts/architecture_policy_gradient_learner_results.json`

```bash
python3 experiments/architecture_policy_gradient_seed_sweep.py --seeds 20260605,20260606,20260607,20260608,20260609 --episodes 200 --training-episodes 400 --validation-episodes 240 --batch-episodes 128 --horizon 8 --evidence-samples 9 --cue-accuracy 0.85 --epochs 32 --restarts 5 --temperature 1.8 --learning-rate 0.12 --lr-decay 0.96 --initial-std 0.8 --finite-diff-epsilon 0.02 --max-grad-norm 4.0
```

This writes:

- `artifacts/architecture_policy_gradient_seed_sweep_summary.csv`
- `artifacts/architecture_policy_gradient_seed_sweep_verdict.csv`
- `artifacts/architecture_policy_gradient_seed_sweep_results.json`

```bash
python3 experiments/architecture_policy_gradient_budget_sweep.py --seeds 20260605,20260606,20260607,20260608,20260609 --budgets 'standard:32:5:128;larger:64:8:192' --episodes 200 --training-episodes 400 --validation-episodes 240 --horizon 8 --evidence-samples 9 --cue-accuracy 0.85 --temperature 1.8 --learning-rate 0.12 --lr-decay 0.96 --initial-std 0.8 --finite-diff-epsilon 0.02 --max-grad-norm 4.0
```

This writes:

- `artifacts/architecture_policy_gradient_budget_sweep_summary.csv`
- `artifacts/architecture_policy_gradient_budget_sweep_verdict.csv`
- `artifacts/architecture_policy_gradient_budget_sweep_results.json`

```bash
python3 experiments/architecture_torch_actor_critic.py --episodes 200 --training-episodes 400 --validation-episodes 240 --batch-episodes 512 --seed 20260606 --horizon 8 --evidence-samples 9 --cue-accuracy 0.85 --epochs 300 --restarts 8 --hidden-size 12 --learning-rate 0.02 --entropy-weight 0.0 --value-weight 0.35 --max-grad-norm 2.0 --device auto
```

This writes:

- `artifacts/architecture_torch_actor_critic_summary.csv`
- `artifacts/architecture_torch_actor_critic_verdict.csv`
- `artifacts/architecture_torch_actor_critic_results.json`

```bash
python3 experiments/ssrm_3d_embodied_world.py --episodes 48 --ticks 540 --seed 20260607 --stage-min 0 --stage-max 6 --world-size 80 --perception-hz 10 --goal-hz 2 --reasoning-hz 0.5 --trace-stage 6 --trace-episode 0
```

This writes:

- `artifacts/ssrm_3d_summary.csv`
- `artifacts/ssrm_3d_episode_metrics.csv`
- `artifacts/ssrm_3d_verdict.csv`
- `artifacts/ssrm_3d_trajectory.json`
- `artifacts/ssrm_3d_results.json`
- `visualizations/ssrm_3d.html` replays the trajectory when served from the repo root.
- `visualizations/modular_llm_architecture.html` shows the LLM-as-module control boundary and ablation modes.

SSRM-3D counts ticks internally, but the architecture should be read as multi-rate control: reflex and physics run fast, perception and attention run at medium rates, self-state and goal arbitration run slower, and language reasoning or memory consolidation run much slower. Ticks are the simulator metronome; subsystem rates are the cognitive architecture.

```bash
python3 experiments/ssrm_3d_recurrent_observer.py --episodes-per-stage 42 --ticks 540 --seed 20260608 --hidden-size 32 --epochs 180 --batch-size 64 --learning-rate 0.004 --device auto
```

This writes:

- `artifacts/ssrm_3d_recurrent_observer_summary.csv`
- `artifacts/ssrm_3d_recurrent_observer_verdict.csv`
- `artifacts/ssrm_3d_recurrent_observer_results.json`

```bash
python3 experiments/ssrm_3d_learned_controller.py --episodes-per-stage 48 --eval-episodes 24 --ticks 540 --seed 20260609 --hidden-size 32 --epochs 160 --batch-size 64 --learning-rate 0.004 --device auto
```

This writes:

- `artifacts/ssrm_3d_learned_controller_summary.csv`
- `artifacts/ssrm_3d_learned_controller_eval.csv`
- `artifacts/ssrm_3d_learned_controller_verdict.csv`
- `artifacts/ssrm_3d_learned_controller_results.json`

```bash
python3 experiments/ssrm_3d_tool_making.py --train-episodes 48 --eval-episodes 72 --ticks 300 --candidate-count 180 --seed 20260610
```

This writes:

- `artifacts/ssrm_3d_tool_making_eval.csv`
- `artifacts/ssrm_3d_tool_making_policy_selection.csv`
- `artifacts/ssrm_3d_tool_making_summary.csv`
- `artifacts/ssrm_3d_tool_making_verdict.csv`
- `artifacts/ssrm_3d_tool_making_trace.json`
- `artifacts/ssrm_3d_tool_making_results.json`
- `visualizations/ssrm_3d_tool_making.html` replays the tool-making trace when served from the repo root.

```bash
python3 experiments/ssrm_3d_social_pressure.py --train-episodes 64 --eval-episodes 96 --candidate-count 160 --seed 20260611
```

This writes:

- `artifacts/ssrm_3d_social_pressure_eval.csv`
- `artifacts/ssrm_3d_social_pressure_policy_selection.csv`
- `artifacts/ssrm_3d_social_pressure_summary.csv`
- `artifacts/ssrm_3d_social_pressure_verdict.csv`
- `artifacts/ssrm_3d_social_pressure_trace.json`
- `artifacts/ssrm_3d_social_pressure_trace.js`
- `artifacts/ssrm_3d_social_pressure_results.json`
- `visualizations/ssrm_3d_social_pressure.html` replays the social-pressure trace when served from the repo root.

```bash
python3 experiments/ssrm_3d_social_ecology.py --train-episodes 80 --eval-episodes 120 --candidate-count 180 --seed 20260612
```

This writes:

- `artifacts/ssrm_3d_social_ecology_eval.csv`
- `artifacts/ssrm_3d_social_ecology_policy_selection.csv`
- `artifacts/ssrm_3d_social_ecology_summary.csv`
- `artifacts/ssrm_3d_social_ecology_verdict.csv`
- `artifacts/ssrm_3d_social_ecology_trace.json`
- `artifacts/ssrm_3d_social_ecology_results.json`
- `artifacts/ssrm_3d_social_ecology_trace.js`
- `artifacts/ssrm_3d_social_ecology_results.js`
- `visualizations/ssrm_3d_social_ecology.html` replays the costly-communication social-ecology trace when served from the repo root.

```bash
python3 experiments/ssrm_3d_agent_continuity.py --episodes 120 --seed 20260613
```

This writes:

- `artifacts/ssrm_3d_agent_continuity_eval.csv`
- `artifacts/ssrm_3d_agent_continuity_summary.csv`
- `artifacts/ssrm_3d_agent_continuity_verdict.csv`
- `artifacts/ssrm_3d_agent_continuity_trace.json`
- `artifacts/ssrm_3d_agent_continuity_results.json`
- `artifacts/ssrm_3d_agent_continuity_trace.js`
- `artifacts/ssrm_3d_agent_continuity_results.js`
- `visualizations/ssrm_3d_agent_continuity.html` replays the pause/restore/fork continuity trace when served from the repo root.

```bash
python3 experiments/ssrm_3d_learned_integration_controller.py --train-episodes 320 --eval-episodes 140 --epochs 160 --seed 20260614 --device auto
```

This writes:

- `artifacts/ssrm_3d_learned_integration_eval.csv`
- `artifacts/ssrm_3d_learned_integration_summary.csv`
- `artifacts/ssrm_3d_learned_integration_verdict.csv`
- `artifacts/ssrm_3d_learned_integration_trace.json`
- `artifacts/ssrm_3d_learned_integration_results.json`
- `artifacts/ssrm_3d_learned_integration_trace.js`
- `artifacts/ssrm_3d_learned_integration_results.js`
- `visualizations/ssrm_3d_learned_integration.html` replays the learned integration trace when served from the repo root.

```bash
python3 experiments/ssrm_3d_no_leak_integration_sweep.py --seeds 20260615,20260616,20260617,20260618,20260619 --train-episodes 1200 --eval-episodes 400 --epochs 400 --hidden-size 64 --device cpu
```

This writes:

- `artifacts/ssrm_3d_no_leak_integration_eval.csv`
- `artifacts/ssrm_3d_no_leak_integration_summary.csv`
- `artifacts/ssrm_3d_no_leak_integration_seed_verdict.csv`
- `artifacts/ssrm_3d_no_leak_integration_verdict.csv`
- `artifacts/ssrm_3d_no_leak_integration_trace.json`
- `artifacts/ssrm_3d_no_leak_integration_results.json`
- `artifacts/ssrm_3d_no_leak_integration_trace.js`
- `artifacts/ssrm_3d_no_leak_integration_results.js`
- `visualizations/ssrm_3d_no_leak_integration.html` replays the no-leak integration trace when served from the repo root.

```bash
python3 experiments/ssrm_3d_structured_perception.py --train-episodes 72 --eval-episodes 96 --seed 20260620 --candidate-count 6
```

This writes:

- `artifacts/ssrm_3d_structured_perception_eval.csv`
- `artifacts/ssrm_3d_structured_perception_policy_selection.csv`
- `artifacts/ssrm_3d_structured_perception_summary.csv`
- `artifacts/ssrm_3d_structured_perception_verdict.csv`
- `artifacts/ssrm_3d_structured_perception_trace.json`
- `artifacts/ssrm_3d_structured_perception_results.json`
- `artifacts/ssrm_3d_structured_perception_trace.js`
- `artifacts/ssrm_3d_structured_perception_results.js`
- `visualizations/ssrm_3d_structured_perception.html` replays the structured perception trace when served from the repo root.

```bash
python3 experiments/ssrm_3d_day_night_sleep.py --train-episodes 72 --eval-episodes 96 --seed 20260621 --candidate-count 6
```

This writes:

- `artifacts/ssrm_3d_day_night_sleep_eval.csv`
- `artifacts/ssrm_3d_day_night_sleep_policy_selection.csv`
- `artifacts/ssrm_3d_day_night_sleep_summary.csv`
- `artifacts/ssrm_3d_day_night_sleep_verdict.csv`
- `artifacts/ssrm_3d_day_night_sleep_trace.json`
- `artifacts/ssrm_3d_day_night_sleep_results.json`
- `artifacts/ssrm_3d_day_night_sleep_trace.js`
- `artifacts/ssrm_3d_day_night_sleep_results.js`
- `visualizations/ssrm_3d_day_night_sleep.html` replays the day/night sleep-rest trace when served from the repo root.

```bash
python3 experiments/ssrm_3d_illness_sanitation.py --train-episodes 72 --eval-episodes 96 --seed 20260622 --candidate-count 6
```

This writes:

- `artifacts/ssrm_3d_illness_sanitation_eval.csv`
- `artifacts/ssrm_3d_illness_sanitation_policy_selection.csv`
- `artifacts/ssrm_3d_illness_sanitation_summary.csv`
- `artifacts/ssrm_3d_illness_sanitation_verdict.csv`
- `artifacts/ssrm_3d_illness_sanitation_trace.json`
- `artifacts/ssrm_3d_illness_sanitation_results.json`
- `artifacts/ssrm_3d_illness_sanitation_trace.js`
- `artifacts/ssrm_3d_illness_sanitation_results.js`
- `visualizations/ssrm_3d_illness_sanitation.html` replays the illness/sanitation trace when served from the repo root.

```bash
python3 experiments/ssrm_3d_weather_exposure.py --train-episodes 72 --eval-episodes 96 --seed 20260623 --candidate-count 6
```

This writes:

- `artifacts/ssrm_3d_weather_exposure_eval.csv`
- `artifacts/ssrm_3d_weather_exposure_policy_selection.csv`
- `artifacts/ssrm_3d_weather_exposure_summary.csv`
- `artifacts/ssrm_3d_weather_exposure_verdict.csv`
- `artifacts/ssrm_3d_weather_exposure_trace.json`
- `artifacts/ssrm_3d_weather_exposure_results.json`
- `artifacts/ssrm_3d_weather_exposure_trace.js`
- `artifacts/ssrm_3d_weather_exposure_results.js`
- `visualizations/ssrm_3d_weather_exposure.html` replays the weather/exposure trace when served from the repo root.

```bash
python3 experiments/ssrm_3d_tool_shelter_degradation.py --train-episodes 72 --eval-episodes 96 --seed 20260624 --candidate-count 6
```

This writes:

- `artifacts/ssrm_3d_tool_shelter_degradation_eval.csv`
- `artifacts/ssrm_3d_tool_shelter_degradation_policy_selection.csv`
- `artifacts/ssrm_3d_tool_shelter_degradation_summary.csv`
- `artifacts/ssrm_3d_tool_shelter_degradation_verdict.csv`
- `artifacts/ssrm_3d_tool_shelter_degradation_trace.json`
- `artifacts/ssrm_3d_tool_shelter_degradation_results.json`
- `artifacts/ssrm_3d_tool_shelter_degradation_trace.js`
- `artifacts/ssrm_3d_tool_shelter_degradation_results.js`
- `visualizations/ssrm_3d_tool_shelter_degradation.html` replays the tool/shelter degradation trace when served from the repo root.

```bash
python3 experiments/learned_bottleneck_discovery.py --episodes 500 --training-episodes 300 --seed 20260531 --calibration-contexts 2
```

This writes:

- `artifacts/learned_bottleneck_discovery_summary.csv`
- `artifacts/learned_bottleneck_discovery_verdict.csv`
- `artifacts/learned_bottleneck_discovery_results.json`

```bash
python3 experiments/sequence_latent_transfer.py --episodes 500 --training-episodes 500 --seed 20260531 --calibration-contexts 2
```

This writes:

- `artifacts/sequence_latent_transfer_summary.csv`
- `artifacts/sequence_latent_transfer_verdict.csv`
- `artifacts/sequence_latent_transfer_results.json`

```bash
python3 experiments/heterogeneous_attractor_precursor.py --episodes 500 --training-episodes 600 --seed 20260601 --calibration-contexts 2 --evolutionary-candidates 600
```

This writes:

- `artifacts/heterogeneous_attractor_precursor_summary.csv`
- `artifacts/heterogeneous_attractor_precursor_verdict.csv`
- `artifacts/heterogeneous_attractor_precursor_results.json`

```bash
python3 experiments/cross_environment_attractor.py --episodes 500 --training-episodes 500 --seed 20260601 --calibration-contexts 2
```

This writes:

- `artifacts/cross_environment_attractor_summary.csv`
- `artifacts/cross_environment_attractor_environment_verdict.csv`
- `artifacts/cross_environment_attractor_scenario_verdict.csv`
- `artifacts/cross_environment_attractor_results.json`

```bash
python3 experiments/factorial_attractor_test.py --episodes 500 --training-episodes 500 --seed 20260601 --calibration-contexts 2 --evolutionary-candidates 500
```

This writes:

- `artifacts/factorial_attractor_summary.csv`
- `artifacts/factorial_attractor_baselines.csv`
- `artifacts/factorial_attractor_environment_verdict.csv`
- `artifacts/factorial_attractor_scenario_verdict.csv`
- `artifacts/factorial_attractor_results.json`

```bash
python3 experiments/raw_history_learning.py --episodes 500 --training-episodes 500 --seed 20260601 --calibration-contexts 2 --evolutionary-candidates 500
```

This writes:

- `artifacts/raw_history_learning_summary.csv`
- `artifacts/raw_history_learning_baselines.csv`
- `artifacts/raw_history_learning_environment_verdict.csv`
- `artifacts/raw_history_learning_scenario_verdict.csv`
- `artifacts/raw_history_learning_results.json`

```bash
python3 experiments/delayed_return_policy.py --episodes 500 --training-episodes 500 --seed 20260601 --calibration-contexts 2 --evolutionary-candidates 500
```

This writes:

- `artifacts/delayed_return_policy_summary.csv`
- `artifacts/delayed_return_policy_baselines.csv`
- `artifacts/delayed_return_policy_environment_verdict.csv`
- `artifacts/delayed_return_policy_scenario_verdict.csv`
- `artifacts/delayed_return_policy_results.json`

```bash
python3 experiments/evolved_recurrent_policy.py --episodes 500 --training-episodes 500 --seed 20260601 --calibration-contexts 2 --random-candidates 700
```

This writes:

- `artifacts/evolved_recurrent_policy_summary.csv`
- `artifacts/evolved_recurrent_policy_baselines.csv`
- `artifacts/evolved_recurrent_policy_environment_verdict.csv`
- `artifacts/evolved_recurrent_policy_scenario_verdict.csv`
- `artifacts/evolved_recurrent_policy_results.json`

```bash
python3 experiments/gradient_recurrent_policy.py --episodes 500 --training-episodes 500 --seed 20260601 --calibration-contexts 2 --gradient-steps 20 --candidates 2
```

This writes:

- `artifacts/gradient_recurrent_policy_summary.csv`
- `artifacts/gradient_recurrent_policy_baselines.csv`
- `artifacts/gradient_recurrent_policy_environment_verdict.csv`
- `artifacts/gradient_recurrent_policy_scenario_verdict.csv`
- `artifacts/gradient_recurrent_policy_results.json`

```bash
python3 experiments/model_based_planning.py --episodes 500 --training-episodes 500 --seed 20260601 --calibration-contexts 2 --recurrent-candidates 200
```

This writes:

- `artifacts/model_based_planning_summary.csv`
- `artifacts/model_based_planning_baselines.csv`
- `artifacts/model_based_planning_environment_verdict.csv`
- `artifacts/model_based_planning_scenario_verdict.csv`
- `artifacts/model_based_planning_results.json`

```bash
python3 experiments/latent_causal_ablation.py --episodes 500 --training-episodes 500 --seed 20260601 --calibration-contexts 2 --recurrent-candidates 200
```

This writes:

- `artifacts/latent_causal_ablation_summary.csv`
- `artifacts/latent_causal_ablation_environment_verdict.csv`
- `artifacts/latent_causal_ablation_scenario_verdict.csv`
- `artifacts/latent_causal_ablation_results.json`

```bash
python3 experiments/counterfactual_latent_editing.py --episodes 500 --training-episodes 500 --seed 20260601 --calibration-contexts 2 --recurrent-candidates 200
```

This writes:

- `artifacts/counterfactual_latent_editing_summary.csv`
- `artifacts/counterfactual_latent_editing_environment_verdict.csv`
- `artifacts/counterfactual_latent_editing_scenario_verdict.csv`
- `artifacts/counterfactual_latent_editing_results.json`

## Decisive Standard

The project should not ask whether an agent says it has a self. It should ask whether self-equivalent state variables become:

1. Decodable from learned representations.
2. Causally useful for prediction, adaptation, and control.
3. More compressed than equivalent world-only histories.
4. More necessary as horizon length, body drift, internal degradation, and subsystem conflict increase.
5. Distinct from hidden external variables, passive internal diagnostics, and generic memory.
6. Actively sought when agent-state information has expected control value.
7. Useful for preserving future action options when current actions can degrade future capability.
8. Useful as a centered observation/action frame when body-relative action must be linked to world-relative prediction.
9. Useful as a feasibility filter when choosing which goals are worth forming.
10. Useful as a shared arbitration variable when competing subsystems must choose coherent action for the same continuing system.
11. Reusable across multiple contexts when the same hidden agent-state determines prediction, goal feasibility, future options, and coherence.
12. Increasingly useful as the number of contexts controlled by the same hidden agent-state grows.
13. Increasingly useful as the number of future steps controlled by the same hidden agent-state grows.
14. Increasingly useful as noisy evidence about persistent hidden agent-state becomes more reliable under partial observability.
15. Learnable from noisy cue/outcome histories without a supplied posterior equation.
16. Recoverable in recurrent observation filters with causal channel-ablation evidence.
17. Recoverable by random-start recurrent search without seeded accumulator candidates.
18. Recoverable from mixed noisy sensors without self-aligned input channels.
19. Recoverable when the damaging intervention direction is learned in mixed sensor space rather than supplied as a known source ablation.
20. Distinguishable from external hidden-state tracking by alignment between an outcome-predictive subspace and an owned-action effect subspace.
21. Distinguishable from controllable external state by requiring body/action-effect alignment rather than generic action controllability.
22. Distinguishable from detachable external state by requiring action-effect alignment to persist across contexts.
23. Recoverable by return selection without supervised outcome-direction labels.
24. Recoverable in trained recurrent policy state without supplied action-boundary policies.
25. Learnable without self labels, while still requiring causal boundary tests to distinguish self-state from reusable world-state.
26. Transferable from early sequence evidence to held-out contexts when the same hidden agent-state persists through the episode.
27. Convergent across several different learner families while still separating agent-bounded latents from external shared latents.
28. Recurring across different environment surfaces while preserving the same agent/world/local/no-hidden boundary.
29. Robust to learner-family and environment-surface variation at the same time in a matched factorial precursor.
30. Recoverable from raw action-observation-reward histories rather than compact labeled outcome inputs.
31. Recoverable when memory policies are selected by delayed episode return after acting.
32. Recoverable in small continuous recurrent hidden states selected by episode return.
33. Recoverable in small recurrent hidden states optimized by return gradients.
34. Recoverable when learned reward models are used for model-based held-out planning.
35. Causally necessary when removing the learned latent selectively damages held-out control.
36. Counterfactually editable when setting the learned latent predictably changes planned action.
37. Strictly convergent across independently trained recurrent architectures.
38. Increasingly recoverable across architectures as temporal horizon grows.
39. Representable by weaker recurrent architectures when training search is no longer the bottleneck.
40. Discoverable by stronger return optimization without supplied source-direction seeds.
41. Recoverable under hard realized-return optimization without a smooth expected-return surrogate.
42. Increasingly recoverable under hard realized-return optimization as horizon grows.
43. Recoverable under online-style objective-only return learning.
44. Recoverable under stochastic policy-gradient return learning.
45. Seed-stable under stochastic policy-gradient return learning.
46. More seed-stable under larger stochastic policy-gradient budgets.
47. Recoverable under GPU-backed recurrent actor-critic learning.
48. Recoverable in a persistent 3D embodied world with layered realtime control.
49. Recoverable by GPU-backed recurrent observers trained on persistent 3D embodied traces.
50. Recoverable in learned recurrent controllers trained without self labels in the persistent 3D embodied world.
51. Extended through externalized cognition when return-selected agents build markers, beacons, or alarms only under embodied confusion pressure.
52. Extended through social identity pressure when return-selected agents use reputation, vulnerability, identity memory, and shared-tool trust only when other agents have persistent policies and memory.

Current stress evidence does not yet satisfy item 37. The architecture boundary stress test finds partial convergence in shared regimes, not strict architecture-wide convergence. Current horizon-pressure evidence partially supports item 38: recoverability improves with horizon, but strict convergence still does not appear.
Current capacity evidence supports item 39, but only as a diagnostic: source-direction seeds are supplied, so this is not natural emergence.
Current soft-optimizer evidence supports item 40 in a narrow toy sense: a cross-entropy optimizer over smooth expected return discovers the expected boundaries without source-direction seeds or boundary-aware restart selection, but this is still not full online RL or a rich embodied Attractor Test.
Current hard-return evidence does not satisfy item 41: hard realized-return optimization preserves clean controls but only partially recovers the self and detachable boundary signatures across architectures.
Current hard-return horizon evidence partially supports item 42: longer horizons improve hard-return recovery from none to partial in self/tool regimes and strict in passive-world recurrence, but still do not produce strict self/tool boundary convergence.
Current online-return evidence does not satisfy item 43: an antithetic perturbation learner with validation-return restart selection preserves clean controls but only recovers 1/3 architectures in each shared regime.
Current policy-gradient evidence supports item 44 in this toy benchmark: stochastic score-function updates recover 3/3 expected boundary signatures across all shared regimes while independent-hidden and irrelevant controls remain clean.
Current policy-gradient seed-sweep evidence does not satisfy item 45: controls remain clean across 5/5 seeds, but shared regimes reach strict convergence in only 2/5 to 3/5 seeds.
Current policy-gradient budget evidence partially supports item 46: the larger budget repairs self-persistent and passive-world seed stability and keeps controls clean, but detachable-tool convergence remains only 3/5 strict seeds.
Current Torch actor-critic evidence supports item 47 in the single-seed canonical run: `torch_rnn`, `torch_gru`, and `torch_lstm` recover strict boundary signatures for self-persistent, detachable-tool, and passive-world regimes while independent-hidden and irrelevant controls remain clean on MPS.
Current SSRM-3D evidence supports item 48 as a first embodied precursor: self-state is not needed in the low-pressure spatial stage, becomes decodable under hidden energy, beats world-only under body drift and delayed options, and dominates after commitments, subsystem conflict, and social pressure enter. Reactive control remains competitive in stages 2 and 3, so the result is a pressure gradient, not a solved Attractor Test.
Current SSRM-3D recurrent-observer evidence supports item 49 as a representation-learning precursor: in the low-pressure stage, body state is decodable without meaningful recurrent advantage; in stages 1-6, recurrent observers recover stronger self-state than the frame-only baseline, and self-state edits move future-viability prediction.
Current SSRM-3D learned-controller evidence supports item 50 as a policy-state precursor: recurrent controllers trained without self labels match the low-pressure frame-only control but strongly beat it under hidden energy, body drift, delayed options, commitments, arbitration, and social pressure while carrying decodable self-state. Direct counterfactual self-edit action effects remain weak.
Current SSRM-3D tool-making evidence supports item 51 as a Gate 2 precursor: tools are rejected in the visible control, selected under hidden-route, degraded-sensor, and interruption pressure, and tool-access ablation removes most of the gain. The cache-only control remains a limit, not a pass.
Current SSRM-3D social-pressure evidence supports item 52 as a Gate 3 precursor: social machinery is rejected in the visible-resource control, selected under cooperative repair, opportunist vulnerability, deceptive-route, and shared-tool pressure, and identity/self-state/tool ablations produce specific losses.
Current SSRM-3D social-ecology evidence supports item 53 as a Gate 3 extension: costly communication is rejected when it has no job, then selected as warning signals, identity names, gossip, or trust-maintenance check-ins only when it preserves survival, repair, deception resistance, shared tools, or future options.
Current SSRM-3D agent-continuity evidence supports item 54 as a Gate 4 precursor: restored agents preserve future control only when body, model, memory, social history, commitments, event log, attention, hidden state, tools, goals, and branch identity are serialized as a coherent continuity record.
Current SSRM-3D learned-integration evidence supports item 55 only as a designed packet bridge: a recurrent controller trained from reward-derived action choices carries early tool, social, continuity, and attention evidence in the seeded canonical run. The no-leak sweep removes scenario identity, randomizes pressure combinations, and runs five seeds; it preserves some bridges but rejects the strong stable-integration claim because `single_tool` margins are too close and `integrated_social` is not ablation-stable.
Current SSRM-3D pressure-layer evidence supports item 56 as designed precursors: structured perception removes omniscient world-state access; day/night sleep-rest shows that rest is rejected in daylight control but becomes useful under fatigue debt, darkness, shelter timing, guarded sleep, and interruption continuity; illness/sanitation shows that hunger/thirst, latent infection, contamination, quarantine/care, immunity, and continuity matter only in matching pressure regimes; weather/exposure shows that cold, heat, rain, wind, drought, shelter, fire/light, water planning, and continuity matter only when external conditions change future capability; and tool/shelter degradation shows that marker wear, shelter damage, alarm/cache decay, inspection, repair, spare parts, and continuity matter only when persistent infrastructure decay changes future control.

The SSRM-3D done-enough gates keep that result bounded: the 3D track is not done until learned control, tool-making or externalized cognition, real social pressure, and targeted ablation all pass. Gate 1 has useful learned-control precursors; gate 2 has a partial externalized-cognition precursor plus a learned tool-memory bridge; gate 3 has partial social-pressure and costly-communication precursors plus a learned social-memory bridge; gate 4 has continuity-record and learned continuity/attention precursors but is still incomplete.

If agents with no persistent self-equivalent representation match performance, transfer, recovery, and compression under those conditions, the strong self-necessity claim fails.
