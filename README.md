# Why Does a Self Exist?

This repo holds a falsifiable research program for the question:

> When does representing "me" become more useful than representing "world state only"?

## Plain-Language Public Overview

If you are not reading the full technical stack, start here:

- [Plain-language visual guide](docs/public/README.md)
- [Findings so far article](docs/public/research_article.md)
- [Long-term LLM reasoning-controller direction](docs/public/sim_distilled_reasoning_controller.md)
- [Commercial software-controller path](docs/public/software_field_experience_controller.md)

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
- [SSRM-3D persistent pressure layer spec](docs/74_ssrm_3d_persistent_pressure_layer_spec.md): defines the next narrow realism layer: structured perception, sleep/rest, illness/sanitation, weather/exposure, tool/shelter degradation, social trust/contracts, predator/threat agents, resource ecology, injury/disability adaptation, development/skill learning, dependent care, irreversible loss, affective control state, and falsifiers.
- [SSRM-3D structured perception report](docs/75_ssrm_3d_structured_perception_report.md): tests cone/FOV vision and spatial audio as ablatable partial-observability pressure before raw pixels or waveform learning.
- [SSRM-3D day/night sleep-rest report](docs/76_ssrm_3d_day_night_sleep_report.md): tests sleep as a vulnerable control action under fatigue, darkness, shelter timing, alarms, social watch, and interruption continuity.
- [SSRM-3D illness/sanitation report](docs/77_ssrm_3d_illness_sanitation_report.md): tests hunger, thirst, latent illness, contamination, clean water, quarantine/care, immunity, and continuity as abstract control pressure.
- [SSRM-3D weather/exposure report](docs/78_ssrm_3d_weather_exposure_report.md): tests cold, heat, rain, wind, drought, shelter, fire/light, water planning, and continuity as abstract control pressure.
- [SSRM-3D tool/shelter degradation report](docs/79_ssrm_3d_tool_shelter_degradation_report.md): tests marker wear, shelter damage, alarm/cache decay, inspection, repair, spare parts, and continuity as abstract control pressure.
- [SSRM-3D social trust/contracts report](docs/80_ssrm_3d_social_trust_contracts_report.md): tests promises, tool return, warnings, resource sharing, repair debt, trust updates, and continuity as abstract social control pressure.
- [SSRM-3D predator/threat agents report](docs/81_ssrm_3d_predator_threat_agents_report.md): tests trackers, sound/scent traces, vulnerability, stealth, shelter, alarms, social warning, fear-like control, and continuity as abstract threat pressure.
- [SSRM-3D resource ecology report](docs/82_ssrm_3d_resource_ecology_report.md): tests regrowth, depletion, spoilage, migration, restraint, caches, sharing, territory, and continuity as abstract resource pressure.
- [SSRM-3D injury/disability adaptation report](docs/83_ssrm_3d_injury_disability_adaptation_report.md): tests capability self-state, motor adaptation, sensor compensation, infection management, repair, help, tools, routes, and continuity as abstract capability pressure.
- [SSRM-3D development/skill learning report](docs/84_ssrm_3d_development_skill_learning_report.md): tests skill memory, practice planning, capability state, fatigue, injury retraining, transfer, teaching, tools, feasibility, and continuity as abstract competence pressure.
- [SSRM-3D dependent care report](docs/85_ssrm_3d_dependent_care_report.md): tests fragile companions, dependent state, identity memory, protection, sharing, repair, teaching, shelter coordination, promises, trust, priority arbitration, and continuity as abstract care pressure.
- [SSRM-3D irreversible loss report](docs/86_ssrm_3d_irreversible_loss_report.md): tests permanent tool, shelter, relationship, memory, and option-space loss as abstract future-option pressure.
- [SSRM-3D affective control report](docs/87_ssrm_3d_affective_control_report.md): tests fear, stress, trust, frustration, affiliation, curiosity, and guilt analogues as abstract control summaries.
- [SSRM-3D physics-first benchmark report](docs/88_ssrm_3d_physics_benchmark_report.md): starts the physics-grounded benchmark track with a modular C++ simulation kernel, recurrent neural decision learning, held-out worlds, ablations, and a replay/intervention viewer.
- [SSRM-3D settlement/civilization pressure report](docs/89_ssrm_3d_civilization_pressure_report.md): expands the public replay beyond a single-agent survival loop into multi-agent settlement pressure with roles, construction, social memory, norms, affect control, and future planning ablations.
- [SSRM-3D open emergence sandbox](docs/90_ssrm_3d_open_emergence_sandbox.md): live non-canonical browser sandbox where agents start from traits, use generic primitives such as inspect, harvest, construct, repair, modify, strike, and signal, carry private belief/memory/thought traces, invent sound tokens and terrain glyphs, form inferred specializations, reproduce abstractly, care for dependents, recover under shelter/treatment, age, accumulate or lose environmental readiness through fuel, seed banks, blueprints, forecast memory, apprenticeship, pest pressure, and structural strain, and die under world pressure.
- [Environment-inferred symbol grounding note](docs/91_environment_inferred_symbol_grounding.md): records the first pass away from direct symbol labels by making sounds and glyphs point to agent-local latent categories inferred from environmental sensor signatures and outcomes, with influence-weighted convention pressure for names and marks.
- [Long-horizon adaptation sandbox note](docs/92_ssrm_3d_long_horizon_adaptation_sandbox.md): slows the live sandbox into an overnight-scale development phase with 12-hour major-shock gating, gradual ecology, shifting resource reliability, stale map pressure, disease strain, social inequality, a pressure/adaptation ledger, infrastructure/tool improvement, teaching tradition, risk memory, operational wisdom/adaptation variables, and a browser audit hook for the 12h shock gate.
- [SSRM-3D long-horizon adaptation report](docs/93_ssrm_3d_long_horizon_adaptation_report.md): adds a headless multi-seed verifier for the 12h shock gate, post-gate shock, infrastructure/tool development, teaching/knowledge transfer, risk memory, adaptation evidence, and targeted ablations.
- [SSRM-3D hidden-regime adaptation report](docs/94_ssrm_3d_hidden_regime_adaptation_report.md): adds post-12h hidden world-rule changes where agents see noisy symptoms rather than regime labels, then ablates inference, teaching, reputation/influence, sanitation memory, weather sensing, and tool adaptation.
- [SSRM-3D learned hidden-regime controller report](docs/95_ssrm_3d_learned_hidden_regime_controller_report.md): trains frame and recurrent neural controllers from hidden-regime symptom histories, evaluates them closed-loop on held-out worlds, and records the partial result where GRU beats reactive control but not the frame model or ablation-specificity gate.
- [SSRM-3D option-gated hidden-regime controller report](docs/96_ssrm_3d_option_gated_hidden_regime_controller_report.md): adds a learned response-option head to improve hidden-regime closed-loop routing; GRU response improves and regime-signal ablation hurts, but the frame model still wins and the verdict remains partial.
- [SSRM-3D return-selected hidden-regime controller report](docs/97_ssrm_3d_return_selected_hidden_regime_controller_report.md): selects the option-action bias by closed-loop validation return, then passes the held-out gate where the learned GRU beats fixed bias, frame, and reactive controls while regime-signal, infrastructure, and body ablations create losses.
- [SSRM-3D social/culture hidden-regime controller report](docs/98_ssrm_3d_social_culture_hidden_regime_controller_report.md): turns the weak Report 97 social/culture ablation into a focused hidden social-regime benchmark; the learned GRU strongly beats reactive control and only edges fixed/frame controls, with a partial verdict because social/culture ablation is not clean across response metrics.
- [SSRM-3D social credit-assignment controller report](docs/99_ssrm_3d_social_credit_assignment_controller_report.md): sharpens the social/culture benchmark with mutually exclusive opportunity costs. The learned GRU beats reactive, fixed-bias, and frame controls in total score, but the claim fails because targeted repair is low and social/culture ablation improves several repair metrics.
- [Sim-distilled reasoning controller plan](docs/100_sim_distilled_reasoning_controller_plan.md): records the long-term direction of distilling agency, self-state feasibility, social repair, cascade-risk, and option-preservation critics from accelerated simulations into LLM reasoning/search controllers.
- [SSRM-3D social repair critic controller report](docs/101_ssrm_3d_social_repair_critic_controller_report.md): adds a learned repair critic around the Report 99 controller. It improves targeted repair and opportunity score, but the strong claim still fails because social/culture ablation remains unstable.
- [Software field-experience controller plan](docs/102_software_field_experience_controller_plan.md): records the most direct commercial path: train consequence-aware software engineering critics that make frontier LLM coding agents better at root-cause repair, test strategy, regression avoidance, and code review.
- [SSRM-3D multi-day maturation report](docs/103_ssrm_3d_multiday_maturation_report.md): extends the 12h shock-gated world into a 72h modular verifier with weather/ecology/disease/resource migration, building and tool tiers, births, teaching-dependent knowledge transfer, culture/symbol pressure, and targeted ablations.
- [SSRM-3D learned multi-day maturation controller report](docs/104_ssrm_3d_learned_multiday_maturation_controller_report.md): trains frame and GRU neural controllers from 72h maturation traces and evaluates them closed-loop; the GRU preserves the long-run development behavior and beats frame/reactive controls, but social/environment/previous-action ablations remain weak.
- [SSRM-3D return-selected multi-day maturation controller report](docs/105_ssrm_3d_return_selected_multiday_maturation_controller_report.md): selects a learned pressure-router setting by closed-loop validation return; it preserves 72h maturation and chooses the `social_env` router, but total-score ablations still show social/environment pressure is too easy to route around.
- [SSRM-3D coupled social/environment maturation report](docs/106_ssrm_3d_coupled_social_environment_maturation_report.md): adds post-12h crises that require both environmental repair and social coordination; the designed controller resolves them, but the learned return-selected GRU fails the coupled-crisis gate.
- [SSRM-3D coupled crisis repair critic report](docs/107_ssrm_3d_coupled_crisis_repair_critic_report.md): adds a learned repair critic around the coupled-crisis GRU; validation rejects the critic by selecting repair bias `0.0`, so the coupled-crisis failure remains.
- [SSRM-3D coupled crisis outcome-value report](docs/108_ssrm_3d_coupled_crisis_outcome_value_report.md): trains a counterfactual action-value reranker for coupled crises; validation selects a nonzero value bias, but held-out crisis repair gets worse than the return-selected GRU.
- [SSRM-3D coupled crisis sequence-outcome report](docs/109_ssrm_3d_coupled_crisis_sequence_outcome_report.md): trains a sequence-plan controller for coupled crises; held-out crisis repair improves sharply, but the strong social/environment ablation dependency still fails.
- [SSRM-3D coupled crisis environmental bottleneck report](docs/110_ssrm_3d_coupled_crisis_environment_bottleneck_report.md): makes environmental crisis repair non-substitutable; the learned overlay improves some response metrics but fails the crisis-score and ablation gates.
- [SSRM-3D coupled crisis rollout-window report](docs/111_ssrm_3d_coupled_crisis_rollout_window_report.md): trains plan values from cloned simulator rollouts; validation rejects the overlay by selecting plan bias `0.0`, so the stricter coupled-crisis failure remains.
- [SSRM-3D coupled crisis diagnostic-memory report](docs/112_ssrm_3d_coupled_crisis_diagnostic_memory_report.md): trains a recurrent crisis diagnostic head with `0.991` offline environmental-repair accuracy, but validation selects diagnostic bias `0.0`; nonzero diagnostic bias raises environmental response while killing social response and increasing damage.
- [SSRM-3D coupled crisis joint-arbitration report](docs/113_ssrm_3d_coupled_crisis_joint_arbitration_report.md): trains separate recurrent environmental and social action heads, then validation-selects joint quotas; held-out crisis score rises from `0.000` to `0.380`, resolved rate rises from `0.100` to `0.650`, and social/environment ablations collapse coupled response.
- [SSRM-3D coupled crisis randomized-transfer report](docs/114_ssrm_3d_coupled_crisis_randomized_transfer_report.md): extends the joint-arbitration controller to 96h runs with randomized post-12h crisis schedules and initial world pressure; held-out crisis score rises from `0.000` to `0.706`, resolved rate rises from `0.067` to `0.967`, and both channel ablations collapse the transfer result.
- [SSRM-3D coupled crisis adaptive allocator report](docs/115_ssrm_3d_coupled_crisis_adaptive_allocator_report.md): replaces fixed joint quotas with a compact return-searched adaptive allocator; it improves over return-selected and fixed-joint baselines but fails the stronger non-fixed-transfer gate.
- [SSRM-3D coupled crisis policy/value allocator report](docs/116_ssrm_3d_coupled_crisis_policy_value_allocator_report.md): trains a value selector from closed-loop allocator-policy consequences; it improves tune selection and beats return-selected GRU, but fails held-out improvement over the seed/fixed allocator.
- [SSRM-3D coupled crisis active state/action value report](docs/117_ssrm_3d_coupled_crisis_active_state_value_report.md): moves value learning into active crisis state/action scoring; the value head trains tightly, but held-out crisis score remains `0.000` and the controller fails to beat return-selected or fixed-joint baselines.
- [SSRM-3D coupled crisis temporal return value report](docs/118_ssrm_3d_coupled_crisis_temporal_return_value_report.md): labels active-crisis actions by later crisis-window outcomes; labels separate stronger policies from return-selected, but held-out crisis score still remains `0.000`.
- [SSRM-3D coupled crisis active policy report](docs/119_ssrm_3d_coupled_crisis_active_policy_report.md): trains a sampled crisis-window policy from completed crisis returns; coupled response improves over return-selected, but crisis score remains `0.000` and fixed-joint coordination is still far stronger.
- [SSRM-3D coupled crisis actor-critic report](docs/120_ssrm_3d_coupled_crisis_actor_critic_report.md): adds a learned critic baseline to the sampled active-crisis policy; the value head trains, but held-out crisis score, resolved rate, and coupled response collapse to `0.000`.
- [SSRM-3D coupled crisis memory-policy report](docs/121_ssrm_3d_coupled_crisis_memory_policy_report.md): carries a recurrent hidden state through each active crisis sequence; it trains across `90` crises, but held-out crisis score, resolved rate, and coupled response still collapse to `0.000`.
- [SSRM-3D coupled crisis process-policy report](docs/122_ssrm_3d_coupled_crisis_process_policy_report.md): adds explicit two-channel process pressure to the recurrent crisis policy; it trains across `91` crises, but held-out crisis score, resolved rate, and coupled response remain `0.000`.
- [SSRM-3D coupled crisis minimum-channel planner report](docs/123_ssrm_3d_coupled_crisis_min_channel_planner_report.md): replaces fixed joint quotas with a dynamic weakest-channel planner around learned environmental/social action heads; held-out crisis score rises to `0.590`, resolved rate to `0.878`, and both channel ablations collapse the result.
- [SSRM-3D coupled crisis planner-distillation report](docs/124_ssrm_3d_coupled_crisis_planner_distillation_report.md): distills the successful minimum-channel planner into a recurrent active-crisis policy, then removes the planner at evaluation. The policy fits teacher traces with `0.986` train accuracy, but held-out crisis score remains `0.000`, so planner removal fails.
- [SSRM-3D coupled crisis closed-loop recovery report](docs/125_ssrm_3d_coupled_crisis_closed_loop_recovery_report.md): adds DAgger-style student-state relabeling after planner distillation; the recovery policy trains on `74756` aggregate examples, but held-out crisis score, resolved rate, and coupled response all remain `0.000`.
- [SSRM-3D coupled crisis consequence-recovery report](docs/126_ssrm_3d_coupled_crisis_consequence_recovery_report.md): trains a recurrent recovery policy with completed-crisis consequence weights; held-out crisis score becomes nonzero at `0.028` and coupled response rises to `0.355`, but the strong recovery and teacher-transfer gates still fail.
- [SSRM-3D coupled crisis sequence-value recovery report](docs/127_ssrm_3d_coupled_crisis_sequence_value_recovery_report.md): trains a completed-window process-value critic with `0.701` pairwise accuracy, then uses it to rerank consequence-policy actions; held-out crisis score falls to `0.003`, so scalar action reranking is a negative boundary.
- [SSRM-3D coupled crisis counterfactual sequence recovery report](docs/128_ssrm_3d_coupled_crisis_counterfactual_sequence_recovery_report.md): trains a cloned-rollout plan-window value model with `0.567` pairwise accuracy, but validation selects plan bias `0.0`; the recurrent policy gets nonzero crisis score `0.036`, while the counterfactual plan layer itself is rejected.
- [SSRM-3D coupled crisis direct counterfactual-policy report](docs/129_ssrm_3d_coupled_crisis_direct_counterfactual_policy_report.md): trains a recurrent crisis policy directly from cloned counterfactual window labels; validation selects direct bias `0.0`, held-out crisis score remains `0.000`, and the consequence-recovery baseline stays stronger.
- [SSRM-3D coupled crisis active consequence-optimization report](docs/130_ssrm_3d_coupled_crisis_active_consequence_optimization_report.md): tests delayed active policy-gradient fine-tuning and a learned consequence-value controller; the value controller improves over return-selected, but stays below consequence recovery and fails the strong coupled-repair gate.
- [SSRM-3D coupled crisis MPC sequence optimizer report](docs/131_ssrm_3d_coupled_crisis_mpc_sequence_optimizer_report.md): tests cloned-rollout model-predictive sequence commitment over supplied repair plans; it strongly improves coupled repair over consequence recovery, but stays bounded as a planning bridge and misses the strict teacher-transfer threshold.
- [SSRM-3D coupled crisis MPC sequence distillation report](docs/132_ssrm_3d_coupled_crisis_mpc_sequence_distillation_report.md): distills the MPC sequence teacher into a recurrent crisis-memory policy, then removes rollout scoring at evaluation; the student fits teacher traces but collapses held-out crisis/coupled repair.
- [SSRM-3D coupled crisis MPC closed-loop recovery report](docs/133_ssrm_3d_coupled_crisis_mpc_closed_loop_recovery_report.md): lets the failed MPC-distilled student act in training worlds and relabels its visited crisis states with the MPC teacher; total score improves to `0.506`, but crisis score, resolved rate, and coupled response remain `0.000`.
- [SSRM-3D coupled crisis student-sequence consequence report](docs/134_ssrm_3d_coupled_crisis_student_sequence_consequence_report.md): trains on student-created counterfactual sequence windows weighted by downstream consequence and MPC plan value; the windows have positive signal, but the planner-free student falls below consequence recovery and held-out crisis score, resolved rate, and coupled response remain `0.000`.
- [SSRM-3D environment-readiness maturation report](docs/135_ssrm_3d_environment_readiness_maturation_report.md): moves the open-emergence sandbox readiness layer into a headless 72h verifier with fuel reserves, seed banks, blueprints, forecast memory, apprenticeship, pest pressure, structural strain, 12h shock gating, post-gate shocks, and channel-specific ablations.
- [SSRM-3D learned environment-readiness controller report](docs/136_ssrm_3d_learned_environment_readiness_controller_report.md): trains frame and GRU neural controllers in the 72h readiness world; the GRU beats reactive/frame scores and preserves the 12h gate, but all learned-controller agents die by the end, knowledge transfer collapses, and ablations are unstable.
- [SSRM-3D readiness closed-loop recovery report](docs/137_ssrm_3d_readiness_closed_loop_recovery_report.md): lets the failed readiness learner act in training worlds, relabels its visited states, and retrains a recovery GRU; final survival improves from `0.0` to `14.0`, but knowledge transfer remains `0.000` and ablations are not clean.
- [SSRM-3D readiness sequence-consequence report](docs/138_ssrm_3d_readiness_sequence_consequence_report.md): adds short cloned-rollout sequence planning over readiness/culture/build/repair plans; the planner bridge reaches `1.000` score and knowledge transfer, but planner-free GRU distillation collapses to `0.287` score and `0.0` final alive.
- [Programmable repair bridge / WrongFix Arena report](docs/139_software_repair_bridge_report.md): maps the weakest-channel planning idea into a structured software-repair benchmark where visible tests can pass for the wrong reason; `min_channel_critic` beats `visible_test_only` on hidden pass, wrong-fix, root-cause, and weakest-channel metrics.
- [Dynamic WrongFix Arena report](docs/141_dynamic_wrongfix_arena_report.md): extends that bridge with 120 seeded tasks plus 5 deterministic false-positive calibration tasks (125 total), held-out families, noisy and irrelevant signals, difficulty tiers, and additional policies; `weighted_quality_critic` bests the visible baseline on hidden pass, wrong-fix, root-cause, and regression avoidance with zero false-positive and zero overblocking in this run.
- [SSRM-3D deep-time playable bridge report](docs/142_ssrm_3d_deep_time_playable_bridge_report.md): adds a deterministic 4096-year compressed prehistory bridge with sensory-rate channels, flower-lattice phase scaffolding, language/culture/technology traces, internal workspace packets, avatar-entry agent packets, and a browser viewer; it passes as a bridge while explicitly not claiming subjective consciousness or live avatar entry.
- [SSRM-3D live avatar intervention bridge report](docs/143_ssrm_3d_live_avatar_intervention_bridge_report.md): turns the Report 142 avatar packets into stateful player-intervention sessions where speech/actions update agent attention, trust, body-affect summaries, native-token grounding, sensory resonance, world state, and replay traces; it passes as an interaction bridge while still rejecting subjective consciousness and mature live-agent claims.
- [SSRM-3D embodied avatar input bridge report](docs/144_ssrm_3d_embodied_avatar_input_bridge_report.md): extends the Report 143 stateful bridge into typed player input plus avatar proximity, deterministic parsing, sensory context, workspace memory, world consequences, and replay traces; it passes as an embodied-input bridge while still rejecting subjective consciousness, open-ended dialogue, and complete playable-world claims.
- [SSRM-3D autonomous live agent loop bridge report](docs/145_ssrm_3d_autonomous_live_agent_loop_bridge_report.md): moves past typed benchmark rows into autonomous multi-rate agent ticks, internal workspace updates, body/affect dynamics, social token exchange, world consequences, sparse avatar interrupts, replay traces, and a start/pause browser loop; it still rejects subjective consciousness, LLM open dialogue, complete playable-world, and unscripted-civilization claims.
- [SSRM-3D affordance object ecology bridge report](docs/146_ssrm_3d_affordance_object_ecology_bridge_report.md): adds persistent named objects with affordances, inventories, material expenditures, ownership gates, decay, repair/crafting loops, sensory bindings, object histories, and an object-map viewer; it still rejects subjective consciousness, LLM open dialogue, complete playable-world, and unscripted-civilization claims.
- [SSRM-3D place navigation object bridge report](docs/147_ssrm_3d_place_navigation_object_bridge_report.md): binds persistent objects to a place graph with terrain costs, hazards, sensory gradients, pathfinding, route memory, travel expenditure, social wayfinding, object use after arrival, and a route-map viewer; it still rejects subjective consciousness, LLM open dialogue, complete playable-world, and unscripted-civilization claims.
- [SSRM-3D agent-made infrastructure bridge report](docs/148_ssrm_3d_agent_made_infrastructure_bridge_report.md): lets agents spend materials and coordinate labor to build and maintain infrastructure that mutates route costs, hazards, route histories, and object accessibility; it still rejects subjective consciousness, LLM open dialogue, complete playable-world, and unscripted-civilization claims.
- [SSRM-3D infrastructure proposal governance bridge report](docs/149_ssrm_3d_infrastructure_proposal_governance_bridge_report.md): lets agents generate infrastructure proposals from pressure, arbitrate conflicts under scarce budgets, service maintenance debt, ground proposals in native tokens, rotate fairness, and persist governance histories; it still rejects subjective consciousness, LLM open dialogue, complete playable-world, and unscripted-civilization claims.
- [SSRM-3D governance memory dialogue bridge report](docs/150_ssrm_3d_governance_memory_dialogue_bridge_report.md): lets the avatar ask deterministic questions about accepted proposals, rejected-overreach shadows, beneficiaries, native tokens, changed routes/objects/projects, and faction disagreement; it still rejects subjective consciousness, LLM open dialogue, complete playable-world, and unscripted-civilization claims.
- [SSRM-3D persistent faction rejected-proposal dialogue bridge report](docs/151_ssrm_3d_persistent_faction_rejected_dialogue_bridge_report.md): replaces rejection shadows with audited reconstructed rejected-proposal bodies, persistent faction positions, counterarguments, concessions, refusal boundaries, and policy rollback hooks; it still rejects subjective consciousness, LLM open dialogue, complete playable-world, and unscripted-civilization claims.
- [SSRM-3D source-native council ledger bridge report](docs/152_ssrm_3d_source_native_council_ledger_bridge_report.md): stores accepted and rejected proposal bodies during the council loop with origin events, rank traces, budget deficits, faction votes, feedback links, and source-originality claims; it still rejects subjective consciousness, LLM open dialogue, complete playable-world, and unscripted-civilization claims.
- [SSRM-3D learned faction-dialogue policy bridge report](docs/153_ssrm_3d_learned_faction_dialogue_policy_bridge_report.md): trains a deterministic centroid policy on source-native ledger questions from earlier councils and evaluates it on later councils with citations, faction/budget/feedback/originality/refusal channels; it still rejects subjective consciousness, LLM open dialogue, complete playable-world, and unscripted-civilization claims.
- [SSRM-3D recurrent faction-dialogue controller bridge report](docs/154_ssrm_3d_recurrent_faction_dialogue_controller_bridge_report.md): runs turn-by-turn avatar sessions with recurrent proposal context, persistent agent memory, learned faction-state updates, source citations, and refusal boundaries; it still rejects subjective consciousness, LLM open dialogue, complete playable-world, and unscripted-civilization claims.
- [SSRM-3D live dialogue-world integration bridge report](docs/155_ssrm_3d_live_dialogue_world_integration_bridge_report.md): connects recurrent dialogue to the autonomous live-agent loop and embodied avatar state so dialogue mutates body/affect, workspace, world, avatar focus, and sensory-frequency packets; it still rejects subjective consciousness, LLM open dialogue, complete playable-world, and unscripted-civilization claims.
- [SSRM-3D interactive avatar dialogue loop bridge report](docs/156_ssrm_3d_interactive_avatar_dialogue_loop_bridge_report.md): adds a deterministic browser-loop contract with start/pause/step controls, typed avatar dialogue parsing, live body/world mutation, source-gate feedback, frequency rendering, persistent UI state, and replay export; it still rejects subjective consciousness, LLM open dialogue, complete playable-world, and unscripted-civilization claims.
- [SSRM-3D navigable embodied presence bridge report](docs/157_ssrm_3d_navigable_embodied_presence_bridge_report.md): joins the interactive dialogue loop to the place/object/infrastructure graph so the avatar can move through places, see objects and agents, feel route/body costs, inspect source overlays, render frequency fields, pass affordance gates, and export a camera replay; it still rejects subjective consciousness, LLM open dialogue, complete playable-world, and unscripted-civilization claims.
- [SSRM-3D continuous co-presence bridge report](docs/158_ssrm_3d_continuous_copresence_bridge_report.md): makes avatar place and mode perturb nearby agents inside the same deterministic control tick, updating autonomous choice, workspace, social memory, frequency state, source boundaries, world consequences, bidirectional response, and replay; it still rejects subjective consciousness, LLM open dialogue, complete playable-world, and unscripted-civilization claims.
- [SSRM-3D interactive typed co-presence bridge report](docs/159_ssrm_3d_interactive_typed_copresence_bridge_report.md): lets browser-side typed utterances route to nearby agents and mutate workspace, social memory, world feedback, source boundaries, frequency state, persistent thread, and replay without regenerating the benchmark trace; it still rejects subjective consciousness, LLM open dialogue, complete playable-world, and unscripted-civilization claims.
- [SSRM-3D persistent session state bridge report](docs/160_ssrm_3d_persistent_session_state_bridge_report.md): adds local save/restore persistence for typed co-presence sessions, carrying agent memory, world feedback, place context, typed thread, replay, source-boundary counters, frequency phase, schema guard, and post-restore interaction; it still rejects subjective consciousness, LLM open dialogue, complete playable-world, and unscripted-civilization claims.
- [SSRM-3D restored autonomous session tick bridge report](docs/161_ssrm_3d_restored_autonomous_session_tick_bridge_report.md): resumes deterministic autonomous background ticks after restoring a saved session, advancing elapsed time, scheduling agents, drifting body/memory, mutating world decay/repair, ticking frequency phase, watching source boundaries, and recording replay/thread continuity; it still rejects subjective consciousness, LLM open dialogue, complete playable-world, and unscripted-civilization claims.
- [SSRM-3D interruptible real-time co-presence report](docs/162_ssrm_3d_interruptible_realtime_copresence_bridge_report.md): tests whether restored autonomous background ticks can continue while avatar interruptions are queued, grounded, routed, acknowledged, recovered from, and replayed.
- [SSRM-3D browser-clock avatar embodiment report](docs/163_ssrm_3d_browser_clock_avatar_embodiment_bridge_report.md): tests a live browser-clock avatar body loop with movement, sensory-rate sampling, background agents, embodied interrupts, source boundaries, save/restore, and replay export.
- [SSRM-3D persistent browser runtime session report](docs/164_ssrm_3d_persistent_browser_runtime_session_bridge_report.md): tests schema-guarded browser runtime snapshots, reload restore, replay journal integrity, import packets, Python pipeline reentry, conflict merge, and rollback checkpoints.
- [SSRM-3D first-person ego state report](docs/165_ssrm_3d_first_person_ego_state_bridge_report.md): pivots toward little people interiors with body, egocentric perception, private workspace, welfare-like felt state, temperament, relationship memory, ownership, bounded refusal, self-story, recovery, and readable behavior.
- [SSRM-3D ego wound and repair report](docs/166_ssrm_3d_ego_wound_repair_bridge_report.md): tests recoverable ego wounds, social attribution, repair opportunities, resentment decay, trust recovery, boundary reassertion, self-story repair, and visible recovery under explicit no-suffering-claim guardrails.
- [SSRM-3D ownership and boundary refusal report](docs/167_ssrm_3d_ownership_boundary_refusal_bridge_report.md): tests functional mine/consent logic, bounded refusal, safe alternatives, dignity preservation, relationship usability, and non-obstruction for benign requests.
- [SSRM-3D social face and reputation memory report](docs/168_ssrm_3d_social_face_reputation_memory_bridge_report.md): tests public social face, audience memory, reputation updates, gossip correction, private/public separation, face repair, and non-permanent shame guardrails.
- [SSRM-3D temperament and preference stability report](docs/169_ssrm_3d_temperament_preference_stability_bridge_report.md): tests stable individuality, preference-shaped repeated behavior, agent differentiation, context sensitivity, non-rigidity, identity memory, and readable profiles.
- [SSRM-3D readable ego body-language report](docs/170_ssrm_3d_readable_ego_body_language_bridge_report.md): maps private body, ego, relationship, temperament, and preference state into visible posture, gaze, proximity, movement, hesitation, comfort, avoidance, following, and ritual markers while keeping private workspace hidden.
- [SSRM-3D daily routine sleep-wake report](docs/171_ssrm_3d_daily_routine_sleep_wake_bridge_report.md): tests circadian phase, sleep pressure, rest recovery, recurring routine, place return, social return, interruption consequence, dream-like memory rehearsal, frequency rhythm, flower-cycle alignment, and replay continuity.
- [SSRM-3D repeated user-interaction learning report](docs/172_ssrm_3d_repeated_user_interaction_learning_bridge_report.md): tests avatar-specific interaction memory, trust calibration, boundary learning, repair, help-seeking, refusal, ritual sharing, overgeneralization guards, frequency entrainment, and replayable relationship continuity.
- [SSRM-3D tiny society group mood report](docs/173_ssrm_3d_tiny_society_group_mood_bridge_report.md): tests local emotional contagion, public group mood, damping, recovery rituals, boundary respect, frequency synchrony, diversity preservation, privacy, and replayable society traces.
- [SSRM-3D moral-status audit and distress guardrails report](docs/174_ssrm_3d_moral_status_distress_guardrails_bridge_report.md): audits adverse scenarios for bounded distress, recovery paths, refusal, pain/fatigue limits, social-contagion guards, rollback checkpoints, overblocking calibration, privacy, and no-consciousness/no-moral-patienthood claims.
- [SSRM-3D deep-time cultural memory and proto-language report](docs/175_ssrm_3d_deep_time_cultural_memory_proto_language_bridge_report.md): simulates 2400 pre-avatar years with inherited cultural memory, proto-word roots, dialect drift, ritual recurrence, frequency and flower bindings, archive recall, safety inheritance, and lineage traces.
- [SSRM-3D deep-time tool ecology and technology lineage report](docs/176_ssrm_3d_deep_time_tool_ecology_technology_lineage_bridge_report.md): binds proto-cultural symbols to materials, tools, affordances, repair practices, resource costs, risk constraints, frequency/flower design, intergroup transfer, and inherited technology lineages over 2400 simulated years.
- [SSRM-3D deep-time economy and resource metabolism report](docs/177_ssrm_3d_deep_time_economy_resource_metabolism_bridge_report.md): makes tool ecology consume stocks, extraction, maintenance, regeneration, waste, scarcity feedback, exchange, safety reserves, ecological pressure, and frequency metabolism over 2400 simulated years.
- [SSRM-3D deep-time habitat, climate, and multisensory report](docs/178_ssrm_3d_deep_time_habitat_climate_multisensory_bridge_report.md): embeds resources into place-bound climate, weather, wetness, temperature, smell, sound, light, terrain costs, body exposure, shelter microclimates, refuges, frequency resonance, and flower-biome patterns over 2400 simulated years.
- [SSRM-3D deep-time settlement architecture and place graph report](docs/179_ssrm_3d_deep_time_settlement_architecture_place_graph_bridge_report.md): connects multisensory places into routes, shelters, storage, work sites, social spaces, hazards, safe refuge paths, avatar traversal packets, frequency route resonance, flower layout, and lineage over 2400 simulated years.
- [SSRM-3D browser-playable avatar traversal bridge report](docs/180_ssrm_3d_browser_playable_avatar_traversal_bridge_report.md): turns the settlement topology into a local browser-playable avatar loop with route buttons, body costs, sensory changes, hazard/refuge feedback, replay history, save/restore, frequency cues, and flower route binding.
- [SSRM-3D live object, need, and bounded dialogue interaction bridge report](docs/181_ssrm_3d_live_object_need_dialogue_interaction_bridge_report.md): adds named local agents, owned/shared objects, object affordances, need updates, care actions, bounded refusal, relationship memory, deterministic dialogue, and browser-local mutation.
- [SSRM-3D object persistence, promise, and relationship continuity bridge report](docs/182_ssrm_3d_object_persistence_promise_relationship_continuity_bridge_report.md): extends interaction across days with persistent object holders, promise ledgers, missed obligations, bounded repair, relationship carryover, future behavior modulation, and replayable continuity.
- [SSRM-3D agent routine, home, work project, and unscripted object-use bridge report](docs/183_ssrm_3d_agent_routine_home_work_unscripted_object_use_bridge_report.md): adds autonomous routine ticks where agents choose actions from homes, routine phases, needs, projects, object affordances, routes, frequency/flower coupling, rest recovery, and social continuity.
- [SSRM-3D agent-local planning, interruptions, and cooperation bridge report](docs/184_ssrm_3d_agent_local_planning_interruptions_cooperation_bridge_report.md): adds private local plan stacks with public summaries, interruption pause/resume, project dependencies, object handoffs, route coordination, cooperation, priority replanning, and browser replay.
- [SSRM-3D project economy, resource scarcity, negotiation, and tool-chain bridge report](docs/185_ssrm_3d_project_economy_resource_negotiation_toolchain_bridge_report.md): adds scarce resource inventories, tool-chain recipes, negotiation packets, exchange ledgers, fair allocation, route costs, trust-price modulation, repair/reuse substitutions, and persistent project outputs.
- [SSRM-3D persistent craft ecology, wear, maintenance, and supply-shock bridge report](docs/186_ssrm_3d_persistent_craft_ecology_wear_maintenance_supply_shock_bridge_report.md): adds durability, wear, breakage, maintenance queues, scarce repair resources, supply shocks, project-blocking degradation, resource conservation, and browser craft replay.
- [SSRM-3D ecological regeneration, spoilage, waste, and sanitation bridge report](docs/187_ssrm_3d_ecological_regeneration_spoilage_waste_sanitation_bridge_report.md): adds regenerating food/water/compost/habitat nodes, spoilage, waste accumulation, contamination feedback, sanitation, compost reuse, health-risk guardrails, and browser ecology replay.
- [SSRM-3D embodied illness, immune recovery, care triage, and quarantine choices bridge report](docs/188_ssrm_3d_embodied_illness_immune_care_quarantine_bridge_report.md): adds ecological exposure binding, infection progression, readable symptom markers, immune recovery, clean-water/rest care, quarantine/containment choices, social-access modulation, health guardrails, and browser health replay.
- [SSRM-3D playable avatar care intervention and medicine practice bridge report](docs/189_ssrm_3d_playable_avatar_care_medicine_practice_bridge_report.md): adds avatar water/rest/herb/cleaning/distance/comfort actions, consent/refusal, medicine preparation, dosage safety, recovery effects, relationship memory, and browser care replay.
- [SSRM-3D agent-led health routines, medicine craft, and contact network bridge report](docs/190_ssrm_3d_agent_led_health_routines_medicine_craft_contact_bridge_report.md): adds self-monitoring, agent-led health routines, medicine craft, supply replenishment, peer care, self-isolation/rejoin checks, contact-network risk modulation, avatar-care memory carryover, and browser routine replay.
- [SSRM-3D agent-led seasonal logistics and stock planning bridge report](docs/191_ssrm_3d_agent_led_seasonal_logistics_stock_planning_bridge_report.md): adds seasonal forecasting, food/water/shelter/medicine stock planning, rationing, replenishment routes, spoilage/waste accounting, fair allocation, emergency reserves, stockout avoidance, long-horizon logistics memory, and browser stock replay.
- [SSRM-3D agent-led settlement work, social obligation, and project schedule bridge report](docs/192_ssrm_3d_agent_led_settlement_work_social_project_schedule_bridge_report.md): adds seasonal work schedules, role assignments, rest/care balance, promise obligations, project dependencies, repair/gather/teach rotation, conflict resolution, fatigue guardrails, social obligation memory, logistics binding, and browser schedule replay.
- [SSRM-3D multi-week apprenticeship, skill transfer, and tool-specialization career bridge report](docs/193_ssrm_3d_multi_week_apprenticeship_skill_transfer_tool_career_bridge_report.md): adds persistent careers, mentor/apprentice edges, deliberate practice, skill transfer, tool affinity, teaching lineage, craft-quality improvement, role fit, autonomy growth, schedule-memory binding, and browser career replay.
- [SSRM-3D guild memory, craft standards, certification, and tool inheritance bridge report](docs/194_ssrm_3d_guild_memory_craft_standards_tool_inheritance_bridge_report.md): adds guild memory, craft standards, quality evaluation, certification, tool inheritance, lineage tracing, apprentice cohorts, standard violation detection, remedial training, reputation binding, intergenerational memory, craft marks, and browser guild replay.
- [SSRM-3D guild marketplace, reciprocal credit, and craft-service contract bridge report](docs/195_ssrm_3d_guild_marketplace_reciprocal_credit_contract_bridge_report.md): adds certified service listings, reciprocal credit ledgers, cross-guild contracts, fair pricing, fulfillment, debt settlement, breach detection, dispute repair, reputation binding, obligation memory, guild-memory dependency, and browser market replay.
- [SSRM-3D market dispute court, public law memory, and restorative contract repair bridge report](docs/196_ssrm_3d_market_dispute_court_public_law_repair_bridge_report.md): adds dispute filing, evidence packets, impartial panels, adjudication, public law memory, precedent binding, restorative repair, trust recovery, contract fairness, repeat-breach prevention, appeals, obligation closure, guild-market memory binding, and browser court replay.
- [SSRM-3D avatar rights charter, consent norms, and moral-boundary law bridge report](docs/197_ssrm_3d_avatar_rights_charter_consent_norm_law_bridge_report.md): adds public avatar-conduct norms, consent requests, bounded refusal, avatar-action review, boundary-risk detection, restorative response, norm precedent, dignity preservation, privacy guardrails, trust repair, care opportunities, public norm memory, and browser norm replay.
- [SSRM-3D agent-authored constitution, norm negotiation, and consent-aware affordance bridge report](docs/198_ssrm_3d_agent_authored_constitution_norm_negotiation_affordance_bridge_report.md): adds agent-authored constitution clauses, proposal diversity, deliberation, voting, norm negotiation, minority-boundary protection, consent-aware avatar affordances, affordance enforcement, revision loops, constitution memory, avatar UI binding, and browser affordance replay.
- [SSRM-3D natural-language proto-culture, ritual naming, and dialogue boundary bridge report](docs/199_ssrm_3d_natural_language_proto_culture_dialogue_boundary_bridge_report.md): adds proto-word creation, ritual naming, shared symbol reuse, interagent teaching, avatar translation, bounded dialogue phrases, cultural memory, semantic grounding, drift control, privacy-preserving dialogue, frequency/phoneme rhythm, flower/syntax binding, and browser dialogue replay.
- [SSRM-3D multi-generational language drift, dialect, oral history, and avatar conversation protocol bridge report](docs/200_ssrm_3d_multigenerational_language_drift_dialect_oral_history_conversation_bridge_report.md): adds generation continuity, inherited lexicons, controlled drift, dialect branching, mutual intelligibility, oral-history retention, ritual lineage recall, avatar conversation protocol, turn-taking boundaries, translation repair, privacy-preserving conversation, cultural identity persistence, frequency drift rhythm, flower lineage binding, and browser conversation replay.
- [SSRM-3D pre-avatar deep time civilization simulator bridge report](docs/201_ssrm_3d_pre_avatar_deep_time_civilization_simulator_bridge_report.md): adds thousands of simulated pre-avatar years, epoch progression, institutions, language/dialect continuity, ritual calendars, tool innovation, settlement memory, weather/resource adaptation, apprenticeships, dispute norms, oral history, avatar-entry locking, frequency/flower world rhythm, and browser deep-time replay.
- [SSRM-3D pre-avatar playable world seed, spatial ecology, and avatar spawn lock bridge report](docs/202_ssrm_3d_pre_avatar_playable_world_seed_spatial_ecology_avatar_lock_bridge_report.md): adds spatial settlement coordinates, ecological cycles, embodied agent body packets, sensory channels, weather/body coupling, tool objects, route graph connectivity, settlement-memory spatial binding, playable affordances, avatar spawn locking, frequency/flower spatial rhythm, and browser world-seed replay.
- [SSRM-3D live browser playable loop, avatar movement, collision, and proximity bridge report](docs/203_ssrm_3d_live_browser_playable_loop_avatar_movement_collision_proximity_bridge_report.md): adds deterministic avatar movement frames, collision guards, agent proximity detection, consent-aware prompts, interaction affordance gating, spawn-lock release, sensory view updates, body reactions, route navigation, tool prompts, weather display, frequency/flower movement rhythm, and browser playable-loop replay.
- [SSRM-3D interactive browser avatar control, collision feedback, and consent prompt selection bridge report](docs/204_ssrm_3d_interactive_browser_avatar_control_collision_consent_prompt_bridge_report.md): adds keyboard/WASD avatar control, position updates, collision feedback, proximity prompts, selectable consent choices, consent-state updates, affordance UI state, agent response feedback, sensory/weather HUDs, tool prompt selection, frequency/flower input rhythm, and an interactive browser prototype.
- [SSRM-3D agent dialogue turn loop, typed avatar utterance, memory, and consent repair bridge report](docs/205_ssrm_3d_agent_dialogue_turn_loop_typed_avatar_utterance_memory_consent_repair_bridge_report.md): adds typed avatar utterances, bounded intent classification, consent-gate checks, public-only agent replies, dialogue memory updates, relationship updates, refusal boundaries, repair dialogue, sensory context binding, public memory grounding, privacy preservation, frequency/flower dialogue rhythm, and a browser dialogue interface.
- [SSRM-3D persistent dialogue memory, preferences, promises, and trust repair bridge report](docs/206_ssrm_3d_persistent_dialogue_memory_preferences_promises_trust_repair_bridge_report.md): adds multi-session public dialogue memory, stable preference carryover, avatar promise tracking, promise fulfillment detection, trust repair, consent/refusal boundary memory, public/private memory separation, frequency/flower memory rhythm, and a browser replay of relationship continuity across visits.
- [SSRM-3D long-horizon personality, routines, and avatar reputation bridge report](docs/207_ssrm_3d_long_horizon_personality_routines_avatar_reputation_bridge_report.md): adds eight playable days of stable agent personality vectors, dawn/midday/evening/night routine anchors, body-need coupling, remembered avatar reputation, refusal and repair history, social reputation echo, novelty-without-drift checks, frequency/flower day rhythm, and browser replay of multi-day continuity.
- [SSRM-3D calendar commitments, object projects, and reputation consequences bridge report](docs/208_ssrm_3d_calendar_commitments_object_projects_reputation_consequences_bridge_report.md): adds twenty-one-day playable arcs with dated commitments, agent-owned object projects, due-day resolution, missed commitment penalties, partial repair without erasure, object ownership preservation, reputation-modulated avatar access, multi-week consequence review, frequency/flower arc rhythm, and browser replay.
- [SSRM-3D agent-owned project economy, materials, wear, debt, trade, and labor bridge report](docs/209_ssrm_3d_agent_owned_project_economy_material_wear_debt_trade_labor_bridge_report.md): adds thirty-five-day economy arcs with agent inventories, material accounting, object wear and repair, gifts, fair and refused trades, explicit debt ledgers, partial repayment, scarcity-blocked project expansion, refusal-sensitive labor, ownership preservation, frequency/flower economy rhythm, and browser replay.
- [SSRM-3D needs marketplace, hunger, warmth, tool access, social obligation, and seasonal price pressure bridge report](docs/210_ssrm_3d_needs_marketplace_hunger_warmth_tool_social_price_pressure_bridge_report.md): adds sixty-day seasonal marketplace pressure with hunger, warmth, tool-access, social-obligation, credit, debt, seasonal price indices, gifts, borrowing, rationing, refusal, blocked affordability, open-debt honesty, frequency/flower market rhythm, and browser replay.
- [SSRM-3D seasonal body ecology, illness risk, communal care, and market-relationship stress bridge report](docs/211_ssrm_3d_seasonal_body_ecology_illness_care_market_relationship_bridge_report.md): adds seventy-two-day body ecology with seasonal wet/cold/hunger/fatigue drift, illness risk, symptoms, pain, hunger/warmth tradeoffs, communal care, care capacity costs, delayed care, body-limit refusal, market stress on relationships, bounded recovery, residual distress honesty, frequency/flower body rhythm, and browser replay.
- [SSRM-3D recoverable body-care gameplay, player intervention, contagion boundary, medicine practice, and consent-aware triage bridge report](docs/212_ssrm_3d_recoverable_body_care_gameplay_player_intervention_contagion_medicine_triage_bridge_report.md): adds avatar-facing body-care turns with observation cues, triage priority, consent gates, accepted/conditional/refused care, refusal respect, dose-safe medicine practice, contagion boundaries, imperfect boundary traceability, recoverable symptom reduction, relationship repair through care, residual need honesty, frequency/flower triage rhythm, and browser replay.
- [SSRM-3D playable clinic loop, inventory, repeated visits, consent memory, medicine side effects, and agent-initiated help-seeking bridge report](docs/213_ssrm_3d_playable_clinic_loop_inventory_repeated_visits_consent_memory_side_effects_help_seeking_bridge_report.md): adds repeated clinic visits with medicine inventory, consent memory, side effects, stockouts, restocks, dose and inventory coupling, agent-initiated help seeking, follow-up due dates, contagion-boundary recall, residual need honesty, frequency/flower clinic rhythm, and browser replay.
- [SSRM-3D agent-authored care plans, clinic scheduling conflicts, medicine learning, and autonomous follow-up negotiation bridge report](docs/214_ssrm_3d_agent_authored_care_plans_clinic_scheduling_medicine_learning_followup_negotiation_bridge_report.md): adds agent-authored care plans, consent-memory binding, side-effect-aware medicine learning, autonomous follow-up requests, clinic schedule conflict detection, negotiated counter-times, unresolved follow-up honesty, boundary-term recall, frequency/flower care-plan rhythm, and browser replay.
- [SSRM-3D agent-authored treatment norms, clinic reputation, medicine evidence ledgers, and multi-agent care governance bridge report](docs/215_ssrm_3d_agent_authored_treatment_norms_clinic_reputation_medicine_evidence_governance_bridge_report.md): adds agent-authored treatment norms, public medicine evidence ledgers, norm-to-evidence traceability, multi-agent votes, deferred weak-consent norms, minority notes, clinic reputation channels, refusal privacy, frequency/flower governance rhythm, and browser replay.
- [SSRM-3D playable public health governance, outbreak quarantine, appeals, and trust recovery bridge report](docs/216_ssrm_3d_playable_public_health_governance_outbreak_quarantine_appeals_trust_recovery_bridge_report.md): adds outbreak-signal ledgers, false-positive and irrelevant-signal handling, reversible quarantine/spacing policies, consent and refusal records, care access under restriction, appeal review, privacy/stigma guardrails, trust recovery, frequency/flower public-health rhythm, and browser replay.
- [SSRM-3D playable community crisis governance, resource triage, rumor, restorative appeals, and trust memory bridge report](docs/217_ssrm_3d_playable_community_crisis_governance_resource_triage_rumor_restorative_appeals_trust_memory_bridge_report.md): adds scarce resource ledgers, crisis policies, triage decisions, rumor propagation and correction, restorative appeal circles, stigma guardrails, long-term trust memories, social debt carry-forward, frequency/flower crisis rhythm, and browser replay.
- [SSRM-3D playable multi-generational culture memory, language drift, inherited rituals, institutions, and avatar-entry bridge report](docs/218_ssrm_3d_playable_multigenerational_culture_memory_language_drift_inherited_rituals_institutions_avatar_entry_bridge_report.md): adds `4980` simulated pre-avatar years, epoch strata, language-drift layers, inherited rituals, institutions, technology lineages, living-agent inheritance records, a hard avatar-entry gate, frequency/flower epoch rhythm, and browser replay.
- [SSRM-3D playable pre-avatar civilization, autonomous generations, child learning, cultural mutation, institution competition, and late avatar entry bridge report](docs/219_ssrm_3d_playable_pre_avatar_civilization_autonomous_generations_learning_cultural_mutation_institution_competition_bridge_report.md): adds `3698` simulated pre-avatar years, autonomous generation cohorts, child-to-adult learning, cultural mutations, institution contests, demographic events, late avatar-entry protocol, frequency/flower civilization rhythm, and browser replay.
- [SSRM-3D playable embodied pre-avatar ecology, births, aging, illness, apprenticeship, habitat, agriculture, weather, and material economy bridge report](docs/220_ssrm_3d_playable_embodied_pre_avatar_ecology_births_aging_illness_apprenticeship_habitat_agriculture_weather_material_economy_bridge_report.md): adds life-stage body records, energy/fatigue/hunger/cold/wetness/pain costs, illness and care, apprenticeships, habitat construction, agriculture cycles, weather sound/smell/body-cost fields, material exchanges, late avatar-entry protocol, frequency/flower ecology rhythm, and browser replay.
- [SSRM-3D playable local 3D ecology scene, spatial bodies, sensory fields, weather volumes, crop plots, habitat interiors, material objects, and avatar conversation bridge report](docs/221_ssrm_3d_playable_local_3d_ecology_scene_spatial_bodies_sensory_weather_crop_habitat_material_conversation_bridge_report.md): adds a standalone keyboard-playable browser scene with spatialized agent bodies, body-state expressions, smell/sound/temperature/wetness fields, weather volumes, crop plots, habitat interiors, material objects with ownership/pickup boundaries, proximity conversation entry, respect/intrude dialogue choices, frequency/flower spatial rhythm, and replay frames.
- [SSRM-3D playable local agent conversation, memory update, object consequence, bounded refusal, and save/restore bridge report](docs/222_ssrm_3d_playable_local_agent_conversation_memory_object_consequence_refusal_save_restore_bridge_report.md): adds stateful local conversations, trust and boundary-pressure deltas, relationship memory writes, object consequences, material debt updates, bounded refusal alternatives, browser `localStorage` save/restore, JSON export/import, frequency/flower interaction rhythm, and a playable browser artifact.
- [SSRM-3D playable local social memory loop, autonomous ticks, need-driven approach/avoidance, object planning, and cross-session continuity bridge report](docs/223_ssrm_3d_playable_local_social_memory_autonomous_ticks_need_approach_object_planning_cross_session_bridge_report.md): adds autonomous agent ticks, need appraisals, approach/avoidance motion, object plans, memory writes between player actions, cross-session relationship continuity, boundary persistence, browser `localStorage` restore, frequency/flower tick rhythm, and a playable browser loop.
- [SSRM-3D playable local autonomous social ecology report](docs/224_ssrm_3d_playable_local_autonomous_social_ecology_multi_agent_negotiation_contagion_history_bridge_report.md): extends autonomous local social memory into multi-agent interaction, shared object negotiation, bounded social contagion, durable relationship histories, and a browser social ecology replay while keeping private workspaces sealed.
- [SSRM-3D playable local autonomous society slice report](docs/225_ssrm_3d_playable_local_autonomous_society_dialogue_cooperative_tasks_conflict_repair_routines_body_language_bridge_report.md): adds agent-agent dialogue, cooperative tasks, conflict repair, group routines, readable body-language animation markers, and browser society replay while keeping private workspaces sealed and debts recoverable.
- [SSRM-3D playable local avatar participation report](docs/226_ssrm_3d_playable_local_avatar_participation_object_dialogue_routine_consequence_saved_days_bridge_report.md): lets the avatar join cooperative work, manipulate objects, choose bounded dialogue, disrupt routines, offer repairs, and carry relationship/object/debt consequences across saved days.
- [SSRM-3D playable local multi-day free-move avatar life report](docs/227_ssrm_3d_playable_local_multiday_free_move_avatar_life_object_affordance_agent_request_reputation_bridge_report.md): adds keyboard free movement, multi-day movement frames, richer object affordances, agent-initiated requests, public reputation UI, saved snapshots, and cross-day persistence.
- [SSRM-3D playable local continuous life loop report](docs/228_ssrm_3d_playable_local_continuous_life_realtime_interrupt_affordance_autonomous_tick_bridge_report.md): merges realtime movement frames, agent-initiated interruptions, a deeper object affordance lattice, autonomous background ticks, merged continuous life ticks, and browser save/restore.
- [SSRM-3D playable local realtime body/dialogue transform report](docs/229_ssrm_3d_playable_local_compositional_transform_schedule_body_dialogue_realtime_bridge_report.md): adds compositional object transformations, autonomous schedules, richer body-state dynamics, typed dialogue routing, and merged realtime integration ticks.
- [SSRM-3D playable local project-loop report](docs/230_ssrm_3d_playable_local_multiturn_dialogue_crafting_schedule_conflict_body_recovery_project_bridge_report.md): adds typed multi-turn dialogue threads, compositional crafting chains, schedule conflicts, body recovery events, persistent personal projects, and merged project-loop ticks.

- [Report 231: SSRM-3D Playable Local Long Personal Arc, Learned Preference, Rich Dialogue, Craft/Economy Consequence Bridge](docs/231_ssrm_3d_playable_local_long_arc_preference_dialogue_craft_economy_bridge_report.md) - deterministic long-arc continuity bridge with learned preferences, richer dialogue, craft/economy consequences, ledgers, body recovery carryover, and an explicit next gate for first-person ego/interior state.
- [Report 232: SSRM-3D First-Person Ego State Bridge](docs/232_ssrm_3d_first_person_ego_state_bridge_report.md) - deterministic functional ego bridge with self-boundary, ownership, private workspace frames, bounded refusal, self-story memory, visible expression, and recoverable ego wound/repair.
- [Report 233: SSRM-3D Many-Day Ego Continuity, Attachment, Ownership, Body-Language Bridge](docs/233_ssrm_3d_many_day_ego_continuity_attachment_body_language_bridge_report.md) - deterministic many-day ego continuity bridge with ownership generalization, relationship-specific attachment, repeated wound/repair, forgiveness without amnesia, richer body language, and private interior continuity.
- [Report 234: SSRM-3D Pre-Avatar Society, Market, Ritual, Proto-Language Epoch Bridge](docs/234_ssrm_3d_pre_avatar_society_market_ritual_proto_language_epoch_bridge_report.md) - deterministic thousands-year pre-avatar society scaffold with households, markets, rituals, proto-language tokens, technology lineages, cultural norms, sensory ecology, and avatar-entry gates.
- [Report 235: SSRM-3D Playable Pre-Avatar Civilization Sandbox Bridge](docs/235_ssrm_3d_playable_pre_avatar_civilization_sandbox_bridge_report.md) - deterministic playable pre-avatar sandbox trace with generational agents, proto-language mutation, market and ritual schedules, sensory/body prompts, and final avatar-entry ceremony gates.
- [Report 236: SSRM-3D Browser-Playable Avatar Entry Prototype Bridge](docs/236_ssrm_3d_browser_playable_avatar_entry_prototype_bridge_report.md) - deterministic browser-playable avatar entry prototype with movement controls, post-entry conversations, market participation, ritual consent prompts, persistent memory updates, sensory/body feedback, and save/restore/replay scaffolding.
- [Report 237: SSRM-3D Post-Entry Live Conversation, Memory, Proto-Language, Consequence Bridge](docs/237_ssrm_3d_post_entry_live_conversation_memory_proto_language_consequence_bridge_report.md) - deterministic typed post-entry conversation sandbox with intent routing, proto-language interpretation, ambiguity recovery, relationship memory writes, multi-day consequences, transcript persistence, and browser-local text input.
- [Report 238: SSRM-3D Post-Entry Multi-Day User-Authored Conversation, Goal, Schedule, Memory Bridge](docs/238_ssrm_3d_post_entry_multiday_user_authored_conversation_goal_schedule_memory_bridge_report.md) - deterministic multi-day typed sandbox with user-authored utterances, parser rules, public agent goals, household schedule changes, relationship memory, durable browser-local storage, and later-day consequence resolution.
- [Report 239: SSRM-3D Durable Post-Entry Browser Game Loop Bridge](docs/239_ssrm_3d_durable_post_entry_browser_game_loop_bridge_report.md) - deterministic browser-local game-loop scaffold with free local text, localStorage world state, agent goal conflicts, schedule simulation, relationship memory persistence, sensory/body state, and replay export.
- [Report 240: SSRM-3D Integrated Browser World v0 Real-Time Tick Bridge](docs/240_ssrm_3d_integrated_browser_world_v0_realtime_tick_bridge_report.md) - deterministic integrated browser-world v0 scaffold with 250 ms ticks, local avatar motion, typed conversation, localStorage persistence, replay download, agent schedule/goal runtime, sensory/body runtime, and a next gate for inspectable inner-workspace traces.
- [Report 241: SSRM-3D Browser World v1 First-Person Ego Interior Bridge](docs/241_ssrm_3d_browser_world_v1_first_person_ego_interior_bridge_report.md) - deterministic browser-world v1 interior scaffold with body state, egocentric perception, ego/self-boundary appraisal, ownership, private workspace, relationship memory, bounded refusal, recovery paths, visible behavior, and blurred-by-default private trace inspection.
- [Report 242: SSRM-3D Browser World v2 Embodied Affect Dynamics Bridge](docs/242_ssrm_3d_browser_world_v2_embodied_affect_dynamics_bridge_report.md) - deterministic browser-world v2 scaffold with sensor rates, homeostatic drives, lagged body-to-affect coupling, care opportunities, distress guardrails, behavior modulation, replay import/export scaffolding, and private coupling traces.
- [Report 243: SSRM-3D Browser World v3 Long-Horizon Routine Circadian Relationship Bridge](docs/243_ssrm_3d_browser_world_v3_long_horizon_routine_circadian_relationship_bridge_report.md) - deterministic 21-day browser-world v3 scaffold with autonomous routines, circadian sleep-debt cycles, affect history carryover, relationship consequences, routine/project consequences, replay import/export checkpoints, and private history traces.
- [Report 244: SSRM-3D Browser World v4 Learned Routine Proto-Language Adaptation Bridge](docs/244_ssrm_3d_browser_world_v4_learned_routine_proto_language_adaptation_bridge_report.md) - deterministic six-week browser-world v4 scaffold with learned routine policy updates, proto-language token drift, sleep/boundary gated avatar consequences, relationship learning, replay adaptation checkpoints, and private learning traces.
- [Report 245: SSRM-3D Browser World v5 Population Cultural Diffusion Bridge](docs/245_ssrm_3d_browser_world_v5_population_cultural_diffusion_bridge_report.md) - deterministic browser-world v5 scaffold with six-household cultural diffusion, household-to-household proto-language spread, learned rituals, avatar reputation propagation, welfare guardrail propagation, replay cultural checkpoints, and private cultural traces.
- [Report 246: SSRM-3D Browser World v6 Generational Cultural Inheritance Bridge](docs/246_ssrm_3d_browser_world_v6_generational_cultural_inheritance_bridge_report.md) - deterministic 18-generation browser-world v6 scaffold with child-to-adult learning arcs, household lineage memory, inherited proto-language/ritual practices, avatar legacy effects, welfare inheritance guardrails, replay generational checkpoints, and private lineage traces.
- [Report 247: SSRM-3D Browser World v7 Thousands-Year Pre-Avatar Epoch Bridge](docs/247_ssrm_3d_browser_world_v7_thousands_year_pre_avatar_epoch_bridge_report.md) - deterministic 4,200-year pre-avatar epoch scaffold with multi-lineage cultural divergence, technology inheritance, welfare survival, avatar-entry ceremony gates, replay epoch checkpoints, and private epoch traces.
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
python3 experiments/ssrm_3d_social_trust_contracts.py --train-episodes 72 --eval-episodes 96 --seed 20260625 --candidate-count 7
```

This writes:

- `artifacts/ssrm_3d_social_trust_contracts_eval.csv`
- `artifacts/ssrm_3d_social_trust_contracts_policy_selection.csv`
- `artifacts/ssrm_3d_social_trust_contracts_summary.csv`
- `artifacts/ssrm_3d_social_trust_contracts_verdict.csv`
- `artifacts/ssrm_3d_social_trust_contracts_trace.json`
- `artifacts/ssrm_3d_social_trust_contracts_results.json`
- `artifacts/ssrm_3d_social_trust_contracts_trace.js`
- `artifacts/ssrm_3d_social_trust_contracts_results.js`
- `visualizations/ssrm_3d_social_trust_contracts.html` replays the social trust/contracts trace when served from the repo root.

```bash
python3 experiments/ssrm_3d_predator_threat_agents.py --train-episodes 72 --eval-episodes 96 --seed 20260626 --candidate-count 7
```

This writes:

- `artifacts/ssrm_3d_predator_threat_agents_eval.csv`
- `artifacts/ssrm_3d_predator_threat_agents_policy_selection.csv`
- `artifacts/ssrm_3d_predator_threat_agents_summary.csv`
- `artifacts/ssrm_3d_predator_threat_agents_verdict.csv`
- `artifacts/ssrm_3d_predator_threat_agents_trace.json`
- `artifacts/ssrm_3d_predator_threat_agents_results.json`
- `artifacts/ssrm_3d_predator_threat_agents_trace.js`
- `artifacts/ssrm_3d_predator_threat_agents_results.js`
- `visualizations/ssrm_3d_predator_threat_agents.html` replays the predator/threat trace when served from the repo root.

```bash
python3 experiments/ssrm_3d_resource_ecology.py --train-episodes 72 --eval-episodes 96 --seed 20260627 --candidate-count 7
```

This writes:

- `artifacts/ssrm_3d_resource_ecology_eval.csv`
- `artifacts/ssrm_3d_resource_ecology_policy_selection.csv`
- `artifacts/ssrm_3d_resource_ecology_summary.csv`
- `artifacts/ssrm_3d_resource_ecology_verdict.csv`
- `artifacts/ssrm_3d_resource_ecology_trace.json`
- `artifacts/ssrm_3d_resource_ecology_results.json`
- `artifacts/ssrm_3d_resource_ecology_trace.js`
- `artifacts/ssrm_3d_resource_ecology_results.js`
- `visualizations/ssrm_3d_resource_ecology.html` replays the resource ecology trace when served from the repo root.

```bash
python3 experiments/ssrm_3d_injury_disability_adaptation.py --train-episodes 72 --eval-episodes 96 --seed 20260628 --candidate-count 7
```

This writes:

- `artifacts/ssrm_3d_injury_disability_adaptation_eval.csv`
- `artifacts/ssrm_3d_injury_disability_adaptation_policy_selection.csv`
- `artifacts/ssrm_3d_injury_disability_adaptation_summary.csv`
- `artifacts/ssrm_3d_injury_disability_adaptation_verdict.csv`
- `artifacts/ssrm_3d_injury_disability_adaptation_trace.json`
- `artifacts/ssrm_3d_injury_disability_adaptation_results.json`
- `artifacts/ssrm_3d_injury_disability_adaptation_trace.js`
- `artifacts/ssrm_3d_injury_disability_adaptation_results.js`
- `visualizations/ssrm_3d_injury_disability_adaptation.html` replays the injury/disability trace when served from the repo root.

```bash
python3 experiments/ssrm_3d_development_skill_learning.py --train-episodes 72 --eval-episodes 96 --seed 20260629 --candidate-count 7
```

This writes:

- `artifacts/ssrm_3d_development_skill_learning_eval.csv`
- `artifacts/ssrm_3d_development_skill_learning_policy_selection.csv`
- `artifacts/ssrm_3d_development_skill_learning_summary.csv`
- `artifacts/ssrm_3d_development_skill_learning_verdict.csv`
- `artifacts/ssrm_3d_development_skill_learning_trace.json`
- `artifacts/ssrm_3d_development_skill_learning_results.json`
- `artifacts/ssrm_3d_development_skill_learning_trace.js`
- `artifacts/ssrm_3d_development_skill_learning_results.js`
- `visualizations/ssrm_3d_development_skill_learning.html` replays the development/skill trace when served from the repo root.

```bash
python3 experiments/ssrm_3d_dependent_care.py --train-episodes 72 --eval-episodes 96 --seed 20260630 --candidate-count 7
```

This writes:

- `artifacts/ssrm_3d_dependent_care_eval.csv`
- `artifacts/ssrm_3d_dependent_care_policy_selection.csv`
- `artifacts/ssrm_3d_dependent_care_summary.csv`
- `artifacts/ssrm_3d_dependent_care_verdict.csv`
- `artifacts/ssrm_3d_dependent_care_trace.json`
- `artifacts/ssrm_3d_dependent_care_results.json`
- `artifacts/ssrm_3d_dependent_care_trace.js`
- `artifacts/ssrm_3d_dependent_care_results.js`
- `visualizations/ssrm_3d_dependent_care.html` replays the dependent-care trace when served from the repo root.

```bash
python3 experiments/ssrm_3d_irreversible_loss.py --train-episodes 72 --eval-episodes 96 --seed 20260701 --candidate-count 7
```

This writes:

- `artifacts/ssrm_3d_irreversible_loss_eval.csv`
- `artifacts/ssrm_3d_irreversible_loss_policy_selection.csv`
- `artifacts/ssrm_3d_irreversible_loss_summary.csv`
- `artifacts/ssrm_3d_irreversible_loss_verdict.csv`
- `artifacts/ssrm_3d_irreversible_loss_trace.json`
- `artifacts/ssrm_3d_irreversible_loss_results.json`
- `artifacts/ssrm_3d_irreversible_loss_trace.js`
- `artifacts/ssrm_3d_irreversible_loss_results.js`
- `visualizations/ssrm_3d_irreversible_loss.html` replays the irreversible-loss trace when served from the repo root.

```bash
python3 experiments/ssrm_3d_affective_control.py --train-episodes 72 --eval-episodes 96 --seed 20260702 --candidate-count 8
```

This writes:

- `artifacts/ssrm_3d_affective_control_eval.csv`
- `artifacts/ssrm_3d_affective_control_policy_selection.csv`
- `artifacts/ssrm_3d_affective_control_summary.csv`
- `artifacts/ssrm_3d_affective_control_verdict.csv`
- `artifacts/ssrm_3d_affective_control_trace.json`
- `artifacts/ssrm_3d_affective_control_results.json`
- `artifacts/ssrm_3d_affective_control_trace.js`
- `artifacts/ssrm_3d_affective_control_results.js`
- `visualizations/ssrm_3d_affective_control.html` replays the affective-control trace when served from the repo root.

```bash
python3 experiments/ssrm_3d_physics_benchmark.py --train-episodes 24 --test-episodes 10 --epochs 80 --hidden-size 32 --ticks 360 --seed 20260705 --device auto --trace-episode 8
```

This writes:

- `artifacts/ssrm_3d_physics_benchmark_architectures.csv`
- `artifacts/ssrm_3d_physics_benchmark_ablations.csv`
- `artifacts/ssrm_3d_physics_benchmark_baselines.csv`
- `artifacts/ssrm_3d_physics_benchmark_verdict.csv`
- `artifacts/ssrm_3d_physics_benchmark_trace.json`
- `artifacts/ssrm_3d_physics_benchmark_results.json`
- `artifacts/ssrm_3d_physics_benchmark_trace.js`
- `artifacts/ssrm_3d_physics_benchmark_results.js`
- `visualizations/ssrm_3d_physics_benchmark.html` replays the physics-first trace and viewer shell when served from the repo root.

```bash
python3 experiments/ssrm_3d_civilization_pressure.py --eval-episodes 48 --ticks 96 --seed 20260706 --trace-episode 3
```

This writes:

- `artifacts/ssrm_3d_civilization_pressure_eval.csv`
- `artifacts/ssrm_3d_civilization_pressure_summary.csv`
- `artifacts/ssrm_3d_civilization_pressure_verdict.csv`
- `artifacts/ssrm_3d_civilization_pressure_trace.json`
- `artifacts/ssrm_3d_civilization_pressure_results.json`
- `artifacts/ssrm_3d_civilization_pressure_trace.js`
- `artifacts/ssrm_3d_civilization_pressure_results.js`
- `visualizations/ssrm_3d_civilization_pressure.html` replays the settlement/civilization pressure trace when served from the repo root.

```bash
python3 experiments/ssrm_3d_long_horizon_adaptation.py --seeds 20260708,20260709,20260710,20260711,20260712 --hours 14.5 --step-hours 0.05 --population 10 --trace-seed 20260708
```

This writes:

- `artifacts/ssrm_3d_long_horizon_adaptation_eval.csv`
- `artifacts/ssrm_3d_long_horizon_adaptation_summary.csv`
- `artifacts/ssrm_3d_long_horizon_adaptation_verdict.csv`
- `artifacts/ssrm_3d_long_horizon_adaptation_trace.json`
- `artifacts/ssrm_3d_long_horizon_adaptation_results.json`
- `artifacts/ssrm_3d_long_horizon_adaptation_trace.js`
- `artifacts/ssrm_3d_long_horizon_adaptation_results.js`

```bash
python3 experiments/ssrm_3d_multiday_maturation.py --seeds 20260901,20260902,20260903,20260904,20260905 --hours 72 --step-hours 0.10 --population 14 --trace-seed 20260901
```

This writes:

- `artifacts/ssrm_3d_multiday_maturation_eval.csv`
- `artifacts/ssrm_3d_multiday_maturation_summary.csv`
- `artifacts/ssrm_3d_multiday_maturation_verdict.csv`
- `artifacts/ssrm_3d_multiday_maturation_trace.json`
- `artifacts/ssrm_3d_multiday_maturation_results.json`
- `artifacts/ssrm_3d_multiday_maturation_trace.js`
- `artifacts/ssrm_3d_multiday_maturation_results.js`
- `visualizations/ssrm_3d_multiday_maturation.html` replays the multi-day trace when served from the repo root.

```bash
python3 experiments/ssrm_3d_environment_readiness_maturation.py --seeds 20261201,20261202,20261203,20261204,20261205 --hours 72 --step-hours 0.10 --population 14 --trace-seed 20261201
```

This writes:

- `artifacts/ssrm_3d_environment_readiness_maturation_eval.csv`
- `artifacts/ssrm_3d_environment_readiness_maturation_summary.csv`
- `artifacts/ssrm_3d_environment_readiness_maturation_verdict.csv`
- `artifacts/ssrm_3d_environment_readiness_maturation_trace.json`
- `artifacts/ssrm_3d_environment_readiness_maturation_results.json`
- `artifacts/ssrm_3d_environment_readiness_maturation_trace.js`
- `artifacts/ssrm_3d_environment_readiness_maturation_results.js`

```bash
python3 experiments/ssrm_3d_learned_environment_readiness_controller.py --train-seeds 20261211,20261212,20261213,20261214,20261215,20261216 --eval-seeds 20261221,20261222,20261223,20261224,20261225 --hours 72 --step-hours 0.10 --population 14 --epochs 52 --hidden-size 72 --device cpu --trace-seed 20261221
```

This writes:

- `artifacts/ssrm_3d_learned_environment_readiness_training.csv`
- `artifacts/ssrm_3d_learned_environment_readiness_eval.csv`
- `artifacts/ssrm_3d_learned_environment_readiness_summary.csv`
- `artifacts/ssrm_3d_learned_environment_readiness_ablations.csv`
- `artifacts/ssrm_3d_learned_environment_readiness_verdict.csv`
- `artifacts/ssrm_3d_learned_environment_readiness_trace.json`
- `artifacts/ssrm_3d_learned_environment_readiness_results.json`
- `artifacts/ssrm_3d_learned_environment_readiness_trace.js`
- `artifacts/ssrm_3d_learned_environment_readiness_results.js`

```bash
python3 experiments/ssrm_3d_readiness_closed_loop_recovery_controller.py --behavior-train-seeds 20261211,20261212,20261213,20261214,20261215,20261216 --recovery-seeds 20261231,20261232,20261233 --eval-seeds 20261251,20261252,20261253,20261254,20261255 --hours 72 --step-hours 0.10 --population 14 --epochs 52 --recovery-epochs 42 --hidden-size 72 --device cpu --trace-seed 20261251
```

This writes:

- `artifacts/ssrm_3d_readiness_closed_loop_recovery_training.csv`
- `artifacts/ssrm_3d_readiness_closed_loop_recovery_collection.csv`
- `artifacts/ssrm_3d_readiness_closed_loop_recovery_eval.csv`
- `artifacts/ssrm_3d_readiness_closed_loop_recovery_summary.csv`
- `artifacts/ssrm_3d_readiness_closed_loop_recovery_ablations.csv`
- `artifacts/ssrm_3d_readiness_closed_loop_recovery_verdict.csv`
- `artifacts/ssrm_3d_readiness_closed_loop_recovery_trace.json`
- `artifacts/ssrm_3d_readiness_closed_loop_recovery_results.json`
- `artifacts/ssrm_3d_readiness_closed_loop_recovery_trace.js`
- `artifacts/ssrm_3d_readiness_closed_loop_recovery_results.js`

```bash
python3 experiments/ssrm_3d_readiness_sequence_consequence_optimizer.py --behavior-train-seeds 20261211,20261212,20261213,20261214,20261215,20261216 --recovery-seeds 20261231,20261232,20261233 --sequence-seeds 20261301,20261302,20261303 --eval-seeds 20261321,20261322,20261323,20261324,20261325 --hours 72 --step-hours 0.10 --population 14 --epochs 52 --recovery-epochs 42 --sequence-epochs 38 --hidden-size 72 --plan-horizon-hours 2.4 --plan-commit-hours 0.8 --sample-interval-hours 1.2 --max-sequence-examples 900 --device cpu --trace-seed 20261321
```

This writes:

- `artifacts/ssrm_3d_readiness_sequence_consequence_training.csv`
- `artifacts/ssrm_3d_readiness_sequence_consequence_recovery_collection.csv`
- `artifacts/ssrm_3d_readiness_sequence_consequence_sequence_collection.csv`
- `artifacts/ssrm_3d_readiness_sequence_consequence_plan_eval.csv`
- `artifacts/ssrm_3d_readiness_sequence_consequence_eval.csv`
- `artifacts/ssrm_3d_readiness_sequence_consequence_summary.csv`
- `artifacts/ssrm_3d_readiness_sequence_consequence_ablations.csv`
- `artifacts/ssrm_3d_readiness_sequence_consequence_verdict.csv`
- `artifacts/ssrm_3d_readiness_sequence_consequence_trace.json`
- `artifacts/ssrm_3d_readiness_sequence_consequence_results.json`
- `artifacts/ssrm_3d_readiness_sequence_consequence_trace.js`
- `artifacts/ssrm_3d_readiness_sequence_consequence_results.js`

```bash
python3 experiments/ssrm_3d_learned_multiday_maturation_controller.py --train-seeds 20260911,20260912,20260913,20260914,20260915,20260916 --eval-seeds 20260921,20260922,20260923,20260924,20260925 --hours 72 --step-hours 0.10 --population 14 --epochs 42 --hidden-size 64 --device auto --trace-seed 20260921
```

This writes:

- `artifacts/ssrm_3d_learned_multiday_maturation_training.csv`
- `artifacts/ssrm_3d_learned_multiday_maturation_eval.csv`
- `artifacts/ssrm_3d_learned_multiday_maturation_summary.csv`
- `artifacts/ssrm_3d_learned_multiday_maturation_ablations.csv`
- `artifacts/ssrm_3d_learned_multiday_maturation_verdict.csv`
- `artifacts/ssrm_3d_learned_multiday_maturation_trace.json`
- `artifacts/ssrm_3d_learned_multiday_maturation_results.json`
- `artifacts/ssrm_3d_learned_multiday_maturation_trace.js`
- `artifacts/ssrm_3d_learned_multiday_maturation_results.js`

```bash
python3 experiments/ssrm_3d_return_selected_multiday_maturation_controller.py --train-seeds 20260911,20260912,20260913,20260914,20260915,20260916 --tune-seeds 20260931,20260932,20260933 --eval-seeds 20260941,20260942,20260943,20260944,20260945 --hours 72 --step-hours 0.10 --population 14 --epochs 42 --hidden-size 64 --device auto --trace-seed 20260941
```

This writes:

- `artifacts/ssrm_3d_return_selected_multiday_maturation_training.csv`
- `artifacts/ssrm_3d_return_selected_multiday_maturation_selection.csv`
- `artifacts/ssrm_3d_return_selected_multiday_maturation_eval.csv`
- `artifacts/ssrm_3d_return_selected_multiday_maturation_summary.csv`
- `artifacts/ssrm_3d_return_selected_multiday_maturation_ablations.csv`
- `artifacts/ssrm_3d_return_selected_multiday_maturation_verdict.csv`
- `artifacts/ssrm_3d_return_selected_multiday_maturation_trace.json`
- `artifacts/ssrm_3d_return_selected_multiday_maturation_results.json`
- `artifacts/ssrm_3d_return_selected_multiday_maturation_trace.js`
- `artifacts/ssrm_3d_return_selected_multiday_maturation_results.js`

```bash
python3 experiments/ssrm_3d_coupled_social_environment_maturation_controller.py --train-seeds 20260911,20260912,20260913,20260914,20260915,20260916 --tune-seeds 20260961,20260962,20260963 --eval-seeds 20260971,20260972,20260973,20260974,20260975 --hours 72 --step-hours 0.10 --population 14 --epochs 42 --hidden-size 64 --device auto --trace-seed 20260971
```

This writes:

- `artifacts/ssrm_3d_coupled_social_environment_maturation_training.csv`
- `artifacts/ssrm_3d_coupled_social_environment_maturation_selection.csv`
- `artifacts/ssrm_3d_coupled_social_environment_maturation_eval.csv`
- `artifacts/ssrm_3d_coupled_social_environment_maturation_summary.csv`
- `artifacts/ssrm_3d_coupled_social_environment_maturation_ablations.csv`
- `artifacts/ssrm_3d_coupled_social_environment_maturation_verdict.csv`
- `artifacts/ssrm_3d_coupled_social_environment_maturation_trace.json`
- `artifacts/ssrm_3d_coupled_social_environment_maturation_results.json`
- `artifacts/ssrm_3d_coupled_social_environment_maturation_trace.js`
- `artifacts/ssrm_3d_coupled_social_environment_maturation_results.js`

```bash
python3 experiments/ssrm_3d_coupled_crisis_repair_critic_controller.py --train-seeds 20260911,20260912,20260913,20260914,20260915,20260916 --tune-seeds 20260981,20260982,20260983 --eval-seeds 20261001,20261002,20261003,20261004,20261005 --hours 72 --step-hours 0.10 --population 14 --epochs 42 --hidden-size 64 --repair-epochs 70 --repair-hidden-size 48 --device auto --trace-seed 20261001
```

This writes:

- `artifacts/ssrm_3d_coupled_crisis_repair_critic_base_training.csv`
- `artifacts/ssrm_3d_coupled_crisis_repair_critic_repair_training.csv`
- `artifacts/ssrm_3d_coupled_crisis_repair_critic_router_selection.csv`
- `artifacts/ssrm_3d_coupled_crisis_repair_critic_repair_selection.csv`
- `artifacts/ssrm_3d_coupled_crisis_repair_critic_eval.csv`
- `artifacts/ssrm_3d_coupled_crisis_repair_critic_summary.csv`
- `artifacts/ssrm_3d_coupled_crisis_repair_critic_ablations.csv`
- `artifacts/ssrm_3d_coupled_crisis_repair_critic_verdict.csv`
- `artifacts/ssrm_3d_coupled_crisis_repair_critic_trace.json`
- `artifacts/ssrm_3d_coupled_crisis_repair_critic_results.json`
- `artifacts/ssrm_3d_coupled_crisis_repair_critic_trace.js`
- `artifacts/ssrm_3d_coupled_crisis_repair_critic_results.js`

```bash
python3 experiments/ssrm_3d_coupled_crisis_outcome_value_controller.py --train-seeds 20260911,20260912,20260913,20260914,20260915,20260916 --tune-seeds 20261011,20261012,20261013 --eval-seeds 20261021,20261022,20261023,20261024,20261025 --hours 72 --step-hours 0.10 --population 14 --epochs 42 --hidden-size 64 --value-epochs 70 --value-hidden-size 64 --max-value-examples 180000 --value-bias-candidates 0.00,1.00,1.75,2.75,4.00,5.50,7.00 --device auto --trace-seed 20261021
```

This writes:

- `artifacts/ssrm_3d_coupled_crisis_outcome_value_base_training.csv`
- `artifacts/ssrm_3d_coupled_crisis_outcome_value_value_training.csv`
- `artifacts/ssrm_3d_coupled_crisis_outcome_value_router_selection.csv`
- `artifacts/ssrm_3d_coupled_crisis_outcome_value_value_selection.csv`
- `artifacts/ssrm_3d_coupled_crisis_outcome_value_eval.csv`
- `artifacts/ssrm_3d_coupled_crisis_outcome_value_summary.csv`
- `artifacts/ssrm_3d_coupled_crisis_outcome_value_ablations.csv`
- `artifacts/ssrm_3d_coupled_crisis_outcome_value_verdict.csv`
- `artifacts/ssrm_3d_coupled_crisis_outcome_value_trace.json`
- `artifacts/ssrm_3d_coupled_crisis_outcome_value_results.json`
- `artifacts/ssrm_3d_coupled_crisis_outcome_value_trace.js`
- `artifacts/ssrm_3d_coupled_crisis_outcome_value_results.js`

```bash
python3 experiments/ssrm_3d_coupled_crisis_sequence_outcome_controller.py --train-seeds 20260911,20260912,20260913,20260914,20260915,20260916 --tune-seeds 20261011,20261012,20261013 --eval-seeds 20261021,20261022,20261023,20261024,20261025 --hours 72 --step-hours 0.10 --population 14 --epochs 42 --hidden-size 64 --plan-epochs 72 --plan-hidden-size 72 --max-plan-examples 160000 --plan-bias-candidates 0.00,1.00,1.75,2.75,4.00,5.50,7.00 --device auto --trace-seed 20261021
```

This writes:

- `artifacts/ssrm_3d_coupled_crisis_sequence_outcome_base_training.csv`
- `artifacts/ssrm_3d_coupled_crisis_sequence_outcome_plan_training.csv`
- `artifacts/ssrm_3d_coupled_crisis_sequence_outcome_router_selection.csv`
- `artifacts/ssrm_3d_coupled_crisis_sequence_outcome_plan_selection.csv`
- `artifacts/ssrm_3d_coupled_crisis_sequence_outcome_eval.csv`
- `artifacts/ssrm_3d_coupled_crisis_sequence_outcome_summary.csv`
- `artifacts/ssrm_3d_coupled_crisis_sequence_outcome_ablations.csv`
- `artifacts/ssrm_3d_coupled_crisis_sequence_outcome_verdict.csv`
- `artifacts/ssrm_3d_coupled_crisis_sequence_outcome_trace.json`
- `artifacts/ssrm_3d_coupled_crisis_sequence_outcome_results.json`
- `artifacts/ssrm_3d_coupled_crisis_sequence_outcome_trace.js`
- `artifacts/ssrm_3d_coupled_crisis_sequence_outcome_results.js`

```bash
python3 experiments/ssrm_3d_coupled_crisis_environment_bottleneck_controller.py --train-seeds 20260911,20260912,20260913,20260914,20260915,20260916 --tune-seeds 20261011,20261012,20261013 --eval-seeds 20261021,20261022,20261023,20261024,20261025 --hours 72 --step-hours 0.10 --population 14 --epochs 42 --hidden-size 64 --plan-epochs 72 --plan-hidden-size 72 --max-plan-examples 160000 --plan-bias-candidates 0.00,1.00,1.75,2.75,4.00,5.50,7.00,9.00,11.00 --device auto --trace-seed 20261021
```

This writes:

- `artifacts/ssrm_3d_coupled_crisis_environment_bottleneck_base_training.csv`
- `artifacts/ssrm_3d_coupled_crisis_environment_bottleneck_plan_training.csv`
- `artifacts/ssrm_3d_coupled_crisis_environment_bottleneck_router_selection.csv`
- `artifacts/ssrm_3d_coupled_crisis_environment_bottleneck_plan_selection.csv`
- `artifacts/ssrm_3d_coupled_crisis_environment_bottleneck_eval.csv`
- `artifacts/ssrm_3d_coupled_crisis_environment_bottleneck_summary.csv`
- `artifacts/ssrm_3d_coupled_crisis_environment_bottleneck_ablations.csv`
- `artifacts/ssrm_3d_coupled_crisis_environment_bottleneck_verdict.csv`
- `artifacts/ssrm_3d_coupled_crisis_environment_bottleneck_trace.json`
- `artifacts/ssrm_3d_coupled_crisis_environment_bottleneck_results.json`
- `artifacts/ssrm_3d_coupled_crisis_environment_bottleneck_trace.js`
- `artifacts/ssrm_3d_coupled_crisis_environment_bottleneck_results.js`

```bash
python3 experiments/ssrm_3d_coupled_crisis_rollout_window_controller.py --train-seeds 20260911,20260912,20260913,20260914,20260915,20260916 --tune-seeds 20261011,20261012,20261013 --eval-seeds 20261021,20261022,20261023,20261024,20261025 --hours 72 --step-hours 0.10 --population 14 --epochs 42 --hidden-size 64 --plan-epochs 72 --plan-hidden-size 72 --max-plan-examples 48000 --plan-bias-candidates 0.00,1.00,1.75,2.75,4.00,5.50,7.00,9.00,11.00 --device auto --trace-seed 20261021
```

This writes:

- `artifacts/ssrm_3d_coupled_crisis_rollout_window_base_training.csv`
- `artifacts/ssrm_3d_coupled_crisis_rollout_window_plan_training.csv`
- `artifacts/ssrm_3d_coupled_crisis_rollout_window_router_selection.csv`
- `artifacts/ssrm_3d_coupled_crisis_rollout_window_plan_selection.csv`
- `artifacts/ssrm_3d_coupled_crisis_rollout_window_eval.csv`
- `artifacts/ssrm_3d_coupled_crisis_rollout_window_summary.csv`
- `artifacts/ssrm_3d_coupled_crisis_rollout_window_ablations.csv`
- `artifacts/ssrm_3d_coupled_crisis_rollout_window_verdict.csv`
- `artifacts/ssrm_3d_coupled_crisis_rollout_window_trace.json`
- `artifacts/ssrm_3d_coupled_crisis_rollout_window_results.json`
- `artifacts/ssrm_3d_coupled_crisis_rollout_window_trace.js`
- `artifacts/ssrm_3d_coupled_crisis_rollout_window_results.js`

```bash
python3 experiments/ssrm_3d_coupled_crisis_diagnostic_memory_controller.py --train-seeds 20260911,20260912,20260913,20260914,20260915,20260916 --tune-seeds 20261011,20261012,20261013 --eval-seeds 20261021,20261022,20261023,20261024,20261025 --hours 72 --step-hours 0.10 --population 14 --epochs 42 --hidden-size 64 --diagnostic-epochs 64 --diagnostic-hidden-size 64 --diagnostic-bias-candidates 0.00,0.75,1.25,1.75,2.50,3.50,5.00,8.00,12.00,20.00 --device auto --trace-seed 20261021
```

This writes:

- `artifacts/ssrm_3d_coupled_crisis_diagnostic_memory_base_training.csv`
- `artifacts/ssrm_3d_coupled_crisis_diagnostic_memory_diagnostic_training.csv`
- `artifacts/ssrm_3d_coupled_crisis_diagnostic_memory_router_selection.csv`
- `artifacts/ssrm_3d_coupled_crisis_diagnostic_memory_diagnostic_selection.csv`
- `artifacts/ssrm_3d_coupled_crisis_diagnostic_memory_eval.csv`
- `artifacts/ssrm_3d_coupled_crisis_diagnostic_memory_summary.csv`
- `artifacts/ssrm_3d_coupled_crisis_diagnostic_memory_ablations.csv`
- `artifacts/ssrm_3d_coupled_crisis_diagnostic_memory_verdict.csv`
- `artifacts/ssrm_3d_coupled_crisis_diagnostic_memory_trace.json`
- `artifacts/ssrm_3d_coupled_crisis_diagnostic_memory_results.json`
- `artifacts/ssrm_3d_coupled_crisis_diagnostic_memory_trace.js`
- `artifacts/ssrm_3d_coupled_crisis_diagnostic_memory_results.js`

```bash
python3 experiments/ssrm_3d_coupled_crisis_joint_arbitration_controller.py --train-seeds 20260911,20260912,20260913,20260914,20260915,20260916 --tune-seeds 20261011,20261012,20261013 --eval-seeds 20261021,20261022,20261023,20261024,20261025 --hours 72 --step-hours 0.10 --population 14 --epochs 42 --hidden-size 64 --action-epochs 64 --action-hidden-size 64 --joint-candidates 0.00:0.00:0.00,0.12:0.12:0.70,0.14:0.14:0.85,0.16:0.14:1.00,0.14:0.16:1.00,0.18:0.16:1.10,0.16:0.18:1.10,0.20:0.18:1.20 --device auto --trace-seed 20261021
```

This writes:

- `artifacts/ssrm_3d_coupled_crisis_joint_arbitration_base_training.csv`
- `artifacts/ssrm_3d_coupled_crisis_joint_arbitration_action_training.csv`
- `artifacts/ssrm_3d_coupled_crisis_joint_arbitration_router_selection.csv`
- `artifacts/ssrm_3d_coupled_crisis_joint_arbitration_joint_selection.csv`
- `artifacts/ssrm_3d_coupled_crisis_joint_arbitration_eval.csv`
- `artifacts/ssrm_3d_coupled_crisis_joint_arbitration_summary.csv`
- `artifacts/ssrm_3d_coupled_crisis_joint_arbitration_ablations.csv`
- `artifacts/ssrm_3d_coupled_crisis_joint_arbitration_verdict.csv`
- `artifacts/ssrm_3d_coupled_crisis_joint_arbitration_trace.json`
- `artifacts/ssrm_3d_coupled_crisis_joint_arbitration_results.json`
- `artifacts/ssrm_3d_coupled_crisis_joint_arbitration_trace.js`
- `artifacts/ssrm_3d_coupled_crisis_joint_arbitration_results.js`

```bash
python3 experiments/ssrm_3d_coupled_crisis_randomized_transfer_controller.py --train-seeds 20260911,20260912,20260913,20260914,20260915,20260916 --tune-seeds 20261111,20261112,20261113 --eval-seeds 20261121,20261122,20261123,20261124,20261125 --hours 96 --step-hours 0.10 --population 14 --epochs 42 --hidden-size 64 --action-epochs 64 --action-hidden-size 64 --joint-candidates 0.00:0.00:0.00,0.10:0.10:0.70,0.12:0.12:0.80,0.14:0.14:0.90,0.16:0.14:1.00,0.14:0.16:1.00,0.18:0.16:1.10,0.16:0.18:1.10,0.20:0.18:1.20 --device auto --trace-seed 20261121
```

This writes:

- `artifacts/ssrm_3d_coupled_crisis_randomized_transfer_schedule.csv`
- `artifacts/ssrm_3d_coupled_crisis_randomized_transfer_base_training.csv`
- `artifacts/ssrm_3d_coupled_crisis_randomized_transfer_action_training.csv`
- `artifacts/ssrm_3d_coupled_crisis_randomized_transfer_router_selection.csv`
- `artifacts/ssrm_3d_coupled_crisis_randomized_transfer_joint_selection.csv`
- `artifacts/ssrm_3d_coupled_crisis_randomized_transfer_eval.csv`
- `artifacts/ssrm_3d_coupled_crisis_randomized_transfer_summary.csv`
- `artifacts/ssrm_3d_coupled_crisis_randomized_transfer_ablations.csv`
- `artifacts/ssrm_3d_coupled_crisis_randomized_transfer_verdict.csv`
- `artifacts/ssrm_3d_coupled_crisis_randomized_transfer_trace.json`
- `artifacts/ssrm_3d_coupled_crisis_randomized_transfer_results.json`
- `artifacts/ssrm_3d_coupled_crisis_randomized_transfer_trace.js`
- `artifacts/ssrm_3d_coupled_crisis_randomized_transfer_results.js`

```bash
python3 experiments/ssrm_3d_coupled_crisis_adaptive_allocator_controller.py --train-seeds 20260911,20260912,20260913,20260914,20260915,20260916 --tune-seeds 20261111,20261112,20261113 --eval-seeds 20261121,20261122,20261123,20261124,20261125 --hours 96 --step-hours 0.10 --population 14 --epochs 36 --hidden-size 64 --action-epochs 52 --action-hidden-size 64 --allocator-iterations 2 --allocator-population 7 --allocator-elites 3 --allocator-sigma 0.42 --device auto --trace-seed 20261121
```

This writes:

- `artifacts/ssrm_3d_coupled_crisis_adaptive_allocator_schedule.csv`
- `artifacts/ssrm_3d_coupled_crisis_adaptive_allocator_base_training.csv`
- `artifacts/ssrm_3d_coupled_crisis_adaptive_allocator_action_training.csv`
- `artifacts/ssrm_3d_coupled_crisis_adaptive_allocator_router_selection.csv`
- `artifacts/ssrm_3d_coupled_crisis_adaptive_allocator_allocator_selection.csv`
- `artifacts/ssrm_3d_coupled_crisis_adaptive_allocator_allocator_probes.csv`
- `artifacts/ssrm_3d_coupled_crisis_adaptive_allocator_eval.csv`
- `artifacts/ssrm_3d_coupled_crisis_adaptive_allocator_summary.csv`
- `artifacts/ssrm_3d_coupled_crisis_adaptive_allocator_ablations.csv`
- `artifacts/ssrm_3d_coupled_crisis_adaptive_allocator_verdict.csv`
- `artifacts/ssrm_3d_coupled_crisis_adaptive_allocator_trace.json`
- `artifacts/ssrm_3d_coupled_crisis_adaptive_allocator_results.json`
- `artifacts/ssrm_3d_coupled_crisis_adaptive_allocator_trace.js`
- `artifacts/ssrm_3d_coupled_crisis_adaptive_allocator_results.js`

```bash
python3 experiments/ssrm_3d_coupled_crisis_policy_value_allocator_controller.py --train-seeds 20260911,20260912,20260913,20260914,20260915,20260916 --tune-seeds 20261111,20261112,20261113 --eval-seeds 20261121,20261122,20261123,20261124,20261125 --hours 96 --step-hours 0.10 --population 14 --epochs 36 --hidden-size 64 --action-epochs 52 --action-hidden-size 64 --policy-value-samples 12 --policy-value-candidates 48 --policy-value-rollouts 5 --policy-value-epochs 180 --policy-value-hidden-size 64 --policy-value-sigma 0.52 --device auto --trace-seed 20261121
```

This writes:

- `artifacts/ssrm_3d_coupled_crisis_policy_value_allocator_schedule.csv`
- `artifacts/ssrm_3d_coupled_crisis_policy_value_allocator_base_training.csv`
- `artifacts/ssrm_3d_coupled_crisis_policy_value_allocator_action_training.csv`
- `artifacts/ssrm_3d_coupled_crisis_policy_value_allocator_router_selection.csv`
- `artifacts/ssrm_3d_coupled_crisis_policy_value_allocator_policy_value_selection.csv`
- `artifacts/ssrm_3d_coupled_crisis_policy_value_allocator_policy_value_training.csv`
- `artifacts/ssrm_3d_coupled_crisis_policy_value_allocator_allocator_probes.csv`
- `artifacts/ssrm_3d_coupled_crisis_policy_value_allocator_eval.csv`
- `artifacts/ssrm_3d_coupled_crisis_policy_value_allocator_summary.csv`
- `artifacts/ssrm_3d_coupled_crisis_policy_value_allocator_ablations.csv`
- `artifacts/ssrm_3d_coupled_crisis_policy_value_allocator_verdict.csv`
- `artifacts/ssrm_3d_coupled_crisis_policy_value_allocator_trace.json`
- `artifacts/ssrm_3d_coupled_crisis_policy_value_allocator_results.json`
- `artifacts/ssrm_3d_coupled_crisis_policy_value_allocator_trace.js`
- `artifacts/ssrm_3d_coupled_crisis_policy_value_allocator_results.js`

```bash
python3 experiments/ssrm_3d_hidden_regime_adaptation.py --seeds 20260713,20260714,20260715,20260716,20260717 --hours 16 --step-hours 0.05 --population 10 --trace-seed 20260713
```

This writes:

- `artifacts/ssrm_3d_hidden_regime_adaptation_eval.csv`
- `artifacts/ssrm_3d_hidden_regime_adaptation_summary.csv`
- `artifacts/ssrm_3d_hidden_regime_adaptation_regime_summary.csv`
- `artifacts/ssrm_3d_hidden_regime_adaptation_verdict.csv`
- `artifacts/ssrm_3d_hidden_regime_adaptation_trace.json`
- `artifacts/ssrm_3d_hidden_regime_adaptation_results.json`
- `artifacts/ssrm_3d_hidden_regime_adaptation_trace.js`
- `artifacts/ssrm_3d_hidden_regime_adaptation_results.js`

```bash
python3 experiments/ssrm_3d_learned_hidden_regime_controller.py --train-seeds 20260718,20260719,20260720,20260721,20260722,20260723,20260724,20260725 --eval-seeds 20260783,20260784,20260785,20260786,20260787 --hours 16 --step-hours 0.08 --population 10 --epochs 80 --hidden-size 48 --device auto --trace-seed 20260783
```

This writes:

- `artifacts/ssrm_3d_learned_hidden_regime_controller_training.csv`
- `artifacts/ssrm_3d_learned_hidden_regime_controller_eval.csv`
- `artifacts/ssrm_3d_learned_hidden_regime_controller_summary.csv`
- `artifacts/ssrm_3d_learned_hidden_regime_controller_ablations.csv`
- `artifacts/ssrm_3d_learned_hidden_regime_controller_verdict.csv`
- `artifacts/ssrm_3d_learned_hidden_regime_controller_trace.json`
- `artifacts/ssrm_3d_learned_hidden_regime_controller_results.json`
- `artifacts/ssrm_3d_learned_hidden_regime_controller_trace.js`
- `artifacts/ssrm_3d_learned_hidden_regime_controller_results.js`

```bash
python3 experiments/ssrm_3d_option_gated_hidden_regime_controller.py --train-seeds 20260718,20260719,20260720,20260721,20260722,20260723,20260724,20260725 --eval-seeds 20260803,20260804,20260805,20260806,20260807 --hours 16 --step-hours 0.08 --population 10 --epochs 100 --hidden-size 56 --device auto --trace-seed 20260803
```

This writes:

- `artifacts/ssrm_3d_option_gated_hidden_regime_controller_training.csv`
- `artifacts/ssrm_3d_option_gated_hidden_regime_controller_eval.csv`
- `artifacts/ssrm_3d_option_gated_hidden_regime_controller_summary.csv`
- `artifacts/ssrm_3d_option_gated_hidden_regime_controller_ablations.csv`
- `artifacts/ssrm_3d_option_gated_hidden_regime_controller_verdict.csv`
- `artifacts/ssrm_3d_option_gated_hidden_regime_controller_trace.json`
- `artifacts/ssrm_3d_option_gated_hidden_regime_controller_results.json`
- `artifacts/ssrm_3d_option_gated_hidden_regime_controller_trace.js`
- `artifacts/ssrm_3d_option_gated_hidden_regime_controller_results.js`

```bash
python3 experiments/ssrm_3d_return_selected_hidden_regime_controller.py --train-seeds 20260718,20260719,20260720,20260721,20260722,20260723,20260724,20260725 --tune-seeds 20260808,20260809,20260810,20260811,20260812 --eval-seeds 20260813,20260814,20260815,20260816,20260817 --bias-candidates 0.70,1.00,1.35,1.70,2.10 --hours 16 --step-hours 0.08 --population 10 --epochs 100 --hidden-size 56 --device auto --trace-seed 20260813
```

This writes:

- `artifacts/ssrm_3d_return_selected_hidden_regime_controller_training.csv`
- `artifacts/ssrm_3d_return_selected_hidden_regime_controller_bias_selection.csv`
- `artifacts/ssrm_3d_return_selected_hidden_regime_controller_eval.csv`
- `artifacts/ssrm_3d_return_selected_hidden_regime_controller_summary.csv`
- `artifacts/ssrm_3d_return_selected_hidden_regime_controller_ablations.csv`
- `artifacts/ssrm_3d_return_selected_hidden_regime_controller_verdict.csv`
- `artifacts/ssrm_3d_return_selected_hidden_regime_controller_trace.json`
- `artifacts/ssrm_3d_return_selected_hidden_regime_controller_results.json`
- `artifacts/ssrm_3d_return_selected_hidden_regime_controller_trace.js`
- `artifacts/ssrm_3d_return_selected_hidden_regime_controller_results.js`

```bash
python3 experiments/ssrm_3d_social_culture_hidden_regime_controller.py --train-seeds 20260818,20260819,20260820,20260821,20260822,20260823,20260824,20260825 --tune-seeds 20260828,20260829,20260830,20260831,20260832 --eval-seeds 20260833,20260834,20260835,20260836,20260837 --bias-candidates 0.70,1.00,1.35,1.70,2.10 --hours 16 --step-hours 0.08 --population 10 --epochs 100 --hidden-size 56 --device auto --trace-seed 20260833
```

This writes:

- `artifacts/ssrm_3d_social_culture_hidden_regime_controller_training.csv`
- `artifacts/ssrm_3d_social_culture_hidden_regime_controller_bias_selection.csv`
- `artifacts/ssrm_3d_social_culture_hidden_regime_controller_eval.csv`
- `artifacts/ssrm_3d_social_culture_hidden_regime_controller_summary.csv`
- `artifacts/ssrm_3d_social_culture_hidden_regime_controller_variant_summary.csv`
- `artifacts/ssrm_3d_social_culture_hidden_regime_controller_ablations.csv`
- `artifacts/ssrm_3d_social_culture_hidden_regime_controller_verdict.csv`
- `artifacts/ssrm_3d_social_culture_hidden_regime_controller_trace.json`
- `artifacts/ssrm_3d_social_culture_hidden_regime_controller_results.json`
- `artifacts/ssrm_3d_social_culture_hidden_regime_controller_trace.js`
- `artifacts/ssrm_3d_social_culture_hidden_regime_controller_results.js`

```bash
python3 experiments/ssrm_3d_social_credit_assignment_controller.py --train-seeds 20260838,20260839,20260840,20260841,20260842,20260843,20260844,20260845 --tune-seeds 20260848,20260849,20260850,20260851,20260852 --eval-seeds 20260853,20260854,20260855,20260856,20260857 --bias-candidates 0.50,0.70,1.00,1.35,1.70 --hours 16 --step-hours 0.08 --population 10 --epochs 110 --hidden-size 64 --device auto --trace-seed 20260853
```

This writes:

- `artifacts/ssrm_3d_social_credit_assignment_controller_training.csv`
- `artifacts/ssrm_3d_social_credit_assignment_controller_bias_selection.csv`
- `artifacts/ssrm_3d_social_credit_assignment_controller_eval.csv`
- `artifacts/ssrm_3d_social_credit_assignment_controller_summary.csv`
- `artifacts/ssrm_3d_social_credit_assignment_controller_variant_summary.csv`
- `artifacts/ssrm_3d_social_credit_assignment_controller_ablations.csv`
- `artifacts/ssrm_3d_social_credit_assignment_controller_verdict.csv`
- `artifacts/ssrm_3d_social_credit_assignment_controller_trace.json`
- `artifacts/ssrm_3d_social_credit_assignment_controller_results.json`
- `artifacts/ssrm_3d_social_credit_assignment_controller_trace.js`
- `artifacts/ssrm_3d_social_credit_assignment_controller_results.js`

```bash
python3 experiments/ssrm_3d_social_repair_critic_controller.py --train-seeds 20260838,20260839,20260840,20260841,20260842,20260843,20260844,20260845 --tune-seeds 20260848,20260849,20260850,20260851,20260852 --eval-seeds 20260853,20260854,20260855,20260856,20260857 --base-bias-candidates 0.50,0.70,1.00,1.35,1.70 --repair-bias-candidates 0.00,0.75,1.25,1.75,2.50,3.50 --hours 16 --step-hours 0.08 --population 10 --epochs 110 --hidden-size 64 --repair-epochs 80 --repair-hidden-size 40 --device auto --trace-seed 20260853
```

This writes:

- `artifacts/ssrm_3d_social_repair_critic_controller_base_training.csv`
- `artifacts/ssrm_3d_social_repair_critic_controller_repair_training.csv`
- `artifacts/ssrm_3d_social_repair_critic_controller_base_bias_selection.csv`
- `artifacts/ssrm_3d_social_repair_critic_controller_repair_bias_selection.csv`
- `artifacts/ssrm_3d_social_repair_critic_controller_eval.csv`
- `artifacts/ssrm_3d_social_repair_critic_controller_summary.csv`
- `artifacts/ssrm_3d_social_repair_critic_controller_variant_summary.csv`
- `artifacts/ssrm_3d_social_repair_critic_controller_ablations.csv`
- `artifacts/ssrm_3d_social_repair_critic_controller_verdict.csv`
- `artifacts/ssrm_3d_social_repair_critic_controller_trace.json`
- `artifacts/ssrm_3d_social_repair_critic_controller_results.json`
- `artifacts/ssrm_3d_social_repair_critic_controller_trace.js`
- `artifacts/ssrm_3d_social_repair_critic_controller_results.js`

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
53. Extended through costly communication when signals, names, gossip, and check-ins preserve future options under social memory.
54. Preserved through interruption, restore, transplant, rollback, and fork only when the full continuity record is serialized.
55. Moved into learned recurrent policy state under designed tool, social, continuity, and attention packets, with no-leak stress tests visible.
56. Pressured by structured perception, sleep, illness, weather, maintenance, contracts, threats, ecology, injury, skill, care, loss, and affective-control layers only when each variable changes control.
57. Recoverable from physics-derived sensor streams in a modular embodied world without scenario labels, while still requiring closed-loop learned control before the stronger claim.
58. Sustained across a multi-day maturation world where a population develops for 12h before major shocks, then adapts through weather, disease, resource migration, building/tool tiers, births, teaching, culture, and post-gate shocks with targeted ablations.
59. Recoverable in learned closed-loop action selection over the multi-day maturation world, while preserving the distinction between imitation, return training, and deep RL.
60. Improved by closed-loop return selection in the multi-day maturation world without confusing return-selected adapters with deep RL.
61. Tested under coupled social/environment crises where environmental repair and social coordination must both work after the 12h development gate.
62. Tested with a learned repair critic around coupled crisis control, while rejecting supervised repair reranking if validation return turns it off.
63. Tested with counterfactual outcome-value reranking for coupled crisis control, while rejecting validation overfit if held-out crises get worse.
64. Tested with sequence-level outcome planning for coupled crisis control, while rejecting the strong claim if social/environment ablations are not both clean.
65. Tested with non-substitutable environmental crisis repair, while rejecting the strong claim if the learned controller cannot recover crisis score or clean social/environment ablation losses.
66. Tested with cloned rollout-window labels for coupled crisis repair, while rejecting the overlay if validation return selects it off.
67. Tested with recurrent diagnostic memory for primary environmental repair, while rejecting offline label accuracy if using it worsens online consequences.
68. Tested with learned joint arbitration over separate environmental and social crisis action heads, while rejecting the claim unless held-out crisis repair improves and both channel ablations collapse coupled response.
69. Tested with randomized post-12h crisis timing, ordering, repetition, and initial-pressure transfer for joint arbitration, while rejecting fixed-schedule-only success.
70. Tested with return-searched adaptive allocation over environmental/social repair heads, while rejecting the stronger claim if it cannot clear the non-fixed-transfer crisis threshold.
71. Tested with policy/value selection over allocator-policy consequences, while rejecting the claim if tune-world value selection does not improve held-out transfer over the seed/fixed allocator.
72. Tested with active crisis state/action value scoring, while rejecting the claim if single-step consequence labels do not improve held-out crisis repair over return-selected or fixed-joint baselines.
73. Tested with temporal crisis-window return labels, while rejecting the claim if delayed outcome labels still cannot improve held-out crisis score over return-selected or fixed-joint baselines.
74. Tested with sampled active-crisis policy updates, while rejecting the claim if policy-gradient updates still cannot recover nonzero held-out crisis score over return-selected or fixed-joint baselines.
75. Tested with an actor-critic value baseline over active-crisis policy updates, while rejecting the claim if the critic trains but held-out crisis repair collapses.
76. Tested with recurrent crisis-window memory over sampled active-crisis sequences, while rejecting the claim if recurrence trains but still cannot preserve coupled environmental/social repair.
77. Tested with explicit two-channel process pressure over recurrent crisis-window policy updates, while rejecting the claim if process supervision still collapses into one-channel repair.
78. Tested with dynamic minimum-channel planning over learned environmental/social action heads, while rejecting the claim unless held-out randomized crises improve and both channel ablations collapse coupled repair.
79. Tested with planner-to-policy distillation for coupled crisis control, while rejecting the claim if offline planner imitation does not preserve nonzero held-out crisis score after the engineered planner is removed.
80. Tested with closed-loop student-state recovery relabeling for coupled crisis control, while rejecting the claim if DAgger-style recovery still cannot preserve nonzero held-out crisis score after the engineered planner is removed.
81. Tested with completed-crisis consequence weighting for coupled crisis control, while rejecting the strong claim if nonzero response still remains far below the planner and fixed-joint baselines.
82. Tested with completed-window process-value reranking for coupled crisis control, while rejecting the claim if offline value signal does not improve held-out crisis repair after planner removal.
83. Tested with cloned-rollout counterfactual multi-action windows for coupled crisis control, while rejecting the claim if validation turns the plan layer off or if it fails to improve over consequence recovery after planner removal.
84. Tested with direct recurrent policy training from cloned counterfactual window labels, while rejecting the claim if validation turns the direct policy off or if held-out crisis/coupled repair remains collapsed after planner removal.
85. Tested with active consequence optimization and learned action-value crisis control, while rejecting the claim if delayed policy-gradient fine-tuning or single-action consequence values fail to beat consequence recovery on held-out coupled repair.
86. Tested with model-predictive sequence commitment over cloned rollout-scored repair plans, while rejecting the learned-transfer claim if it remains a supplied planning bridge or misses the strict teacher-transfer crisis threshold.
87. Tested with recurrent distillation of the MPC sequence teacher, while rejecting the claim if teacher-trace imitation does not preserve held-out crisis score, resolved rate, coupled response, and social/environment dependency after rollout scoring is removed.
88. Tested with MPC teacher relabeling of student-visited crisis states, while rejecting the claim if closed-loop relabeling still cannot preserve held-out crisis score, resolved rate, coupled response, and social/environment dependency after rollout scoring is removed.
89. Tested with student-created counterfactual sequence windows for coupled crisis control, while rejecting the claim if high-value student-state windows still fail to transfer into planner-free coupled repair.
90. Tested with closed-loop recovery relabeling in the richer 72h readiness world, while rejecting the strong claim if survival improves but knowledge transfer, readiness, and ablation specificity remain weak.
91. Tested with short sequence-consequence planning in the richer 72h readiness world, while rejecting the learned-transfer claim if cloned-rollout planning works but planner-free GRU distillation collapses.

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
Current SSRM-3D pressure-layer evidence supports item 56 as designed precursors: structured perception removes omniscient world-state access; day/night sleep-rest shows that rest is rejected in daylight control but becomes useful under fatigue debt, darkness, shelter timing, guarded sleep, and interruption continuity; illness/sanitation shows that hunger/thirst, latent infection, contamination, quarantine/care, immunity, and continuity matter only in matching pressure regimes; weather/exposure shows that cold, heat, rain, wind, drought, shelter, fire/light, water planning, and continuity matter only when external conditions change future capability; tool/shelter degradation shows that marker wear, shelter damage, alarm/cache decay, inspection, repair, spare parts, and continuity matter only when persistent infrastructure decay changes future control; social trust/contracts shows that promises, tool return, warnings, sharing, repair debt, trust updates, and continuity matter only when delayed social consequences change future options; predator/threat agents show that sound/scent traces, vulnerability, stealth, shelter, alarms, social warning, and continuity matter only when trackers exploit them; resource ecology shows that regrowth, depletion, spoilage, migration, restraint, caches, sharing, territory, and continuity matter only when delayed resource consequences change future options; injury/disability adaptation shows that mobility loss, degraded senses, infection risk, repair, help, tools, routes, and continuity matter only when changed capability changes future action feasibility; development/skill learning shows that practice, fatigue, injury retraining, transfer, teaching, tools, goal feasibility, and continuity matter only when changing competence changes future action feasibility; dependent care shows that fragile companions, identity memory, protection, sharing, repair, teaching, shelter coordination, promises, social trust, priority arbitration, and continuity matter only when another persistent agent changes future options; irreversible loss shows that permanent tool, shelter, relationship, memory, and option-space loss matters only when future options cannot simply be restored; and affective control shows that fear, stress, trust, frustration, affiliation, curiosity, and guilt analogues matter only when compact summaries change attention, memory, risk, communication, repair, inspection, social access, or continuity.
Current SSRM-3D physics-first evidence supports item 57 only as a foundation: a modular C++ kernel produces physics-derived traces, PyTorch RNN/GRU/LSTM models learn held-out decision structure without scenario labels, and ablations expose learned dependencies on self-state, position/motion, audio, user proposal, vision, and weather inputs. It is not closed-loop deep reinforcement learning yet.
Current SSRM-3D multi-day maturation evidence supports item 58 only as a designed verifier: a modular headless world runs 72 simulated hours, locks major shocks until after 12h, records births and lineage, improves architecture and tools, and shows targeted losses when teaching, risk memory, infrastructure memory, tool improvement, social learning, environmental sensing, or all development channels are removed. It is not open-ended civilization or trained deep RL.
Current SSRM-3D learned multi-day maturation evidence supports item 59 only as an imitation-control precursor: a GRU trained on 72h traces acts closed-loop for held-out 72h worlds, preserves the shock gate, matches the designed score, and beats frame/reactive controls. The strong ablation claim remains partial because social/culture, environment, and previous-action channels do not all show clean losses.
Current SSRM-3D return-selected multi-day maturation evidence supports item 60 only as a partial return-selection precursor: validation return selects a `social_env` pressure router around the GRU and held-out worlds preserve 72h maturation, but total-score ablations still show that social/culture and environment channels can be routed around.
Current SSRM-3D coupled social/environment maturation evidence does not satisfy item 61: the designed controller resolves the coupled crises, but the learned return-selected GRU preserves generic maturation while scoring `0.000` on crisis score and resolving only `0.100` of crises.
Current SSRM-3D coupled crisis repair-critic evidence does not satisfy item 62: validation selects repair bias `0.0`, the repair-critic GRU keeps crisis score at `0.000`, and social/environment ablations cannot create clean crisis-score losses while the base crisis behavior is still collapsed.
Current SSRM-3D coupled crisis outcome-value evidence does not satisfy item 63: validation selects nonzero value bias `1.75`, but held-out crisis score remains `0.000`, resolved rate falls to `0.050`, and total score drops below the return-selected GRU.
Current SSRM-3D coupled crisis sequence-outcome evidence partially supports item 64: validation selects plan bias `4.0`, held-out crisis score rises to `0.304`, resolved rate rises to `0.500`, and coupled response rises to `0.434`, but the strong claim fails because environment ablation produces only `0.003` coupled-response loss.
Current SSRM-3D coupled crisis environmental-bottleneck evidence does not satisfy item 65: validation selects plan bias `2.75`, resolved rate rises over the return-selected GRU from `0.100` to `0.250`, and coupled response rises from `0.029` to `0.160`, but held-out crisis score remains `0.000`, total score falls below the return-selected GRU, and social/environment ablations still do not create clean losses.
Current SSRM-3D coupled crisis rollout-window evidence does not satisfy item 66: the plan-value model trains on `9248` cloned rollout examples, but validation rejects the overlay by selecting plan bias `0.0`; held-out crisis score remains `0.000`, resolved rate stays `0.100`, and social/environment ablations still do not create clean losses.
Current SSRM-3D coupled crisis diagnostic-memory evidence does not satisfy item 67: the recurrent diagnostic head reaches `0.991` offline environmental-repair accuracy, but validation selects diagnostic bias `0.0`; nonzero diagnostic bias increases environmental response while eliminating social response, increasing damage, and preserving `0.000` crisis score.
Current SSRM-3D coupled crisis joint-arbitration evidence supports item 68 as a structured learned-coordination precursor: validation selects env/social quotas `0.14`/`0.14` with coordinator strength `0.85`; held-out crisis score rises from `0.000` to `0.380`, resolved rate rises from `0.100` to `0.650`, and coupled response rises from `0.027` to `0.646`. Social/culture and environment ablations both collapse crisis score and coupled response. This is still structured joint arbitration around learned heads, not actor-critic RL or open-ended civilization.
Current SSRM-3D coupled crisis randomized-transfer evidence supports item 69 as a stronger structured learned-coordination precursor: 96h eval worlds average `5.8` post-gate crises, no crisis before `12h`, selected env/social quotas `0.14`/`0.14` and strength `0.90`, crisis score rises from `0.000` to `0.706` vs return-selected, resolved rate rises from `0.067` to `0.967`, coupled response rises from `0.055` to `0.965`, and both social/environment ablations collapse crisis and coupled response. This is still structured arbitration, not actor-critic or open-ended civilization.
Current SSRM-3D coupled crisis adaptive-allocation evidence only partially supports item 70: return search over a compact allocator improves total score over return-selected from `0.516` to `0.624`, crisis score from `0.000` to `0.224`, resolved rate from `0.000` to `0.620`, and coupled response from `0.004` to `0.615`; it also beats the fixed-joint baseline in this run. But the stronger non-fixed-transfer gate fails because crisis score remains below the required threshold, so the result is progress toward learned allocation, not a replacement for structured coordination.
Current SSRM-3D coupled crisis policy/value-allocation evidence does not satisfy item 71: the value selector improves tune objective from `1.186` to `1.354`, but selected held-out crisis score is `0.224` versus `0.361` for the seed/fixed allocator, resolved rate is `0.627` versus `0.727`, and coupled response is `0.618` versus `0.701`.
Current SSRM-3D coupled crisis active-state/action-value evidence does not satisfy item 72: the value model trains on `120000` active-crisis examples and validation selects value bias `2.5`, but held-out crisis score remains `0.000`, total score is `0.518` versus `0.520` for the return-selected GRU and `0.604` for fixed joint, and resolved rate is only `0.140` versus `0.620` for fixed joint. This is a useful failed boundary: single-step active value labels are not yet enough for temporally extended coupled-crisis repair.
Current SSRM-3D coupled crisis temporal-return evidence does not satisfy item 73: completed-crisis labels separate stronger joint policies from return-selected rollouts, and resolved rate improves over return-selected from `0.033` to `0.280`, but held-out crisis score remains `0.000` and fixed-joint coordination is still far stronger.
Current SSRM-3D coupled crisis active-policy evidence does not satisfy item 74: sampled crisis-window policy updates train across `73` crises and raise coupled response from `0.028` to `0.147` over the return-selected GRU, but held-out crisis score remains `0.000`, total score is only `0.520`, and fixed-joint coordination remains far stronger with `0.349` crisis score and `0.693` coupled response. This says lightweight active policy learning is closer to the needed shape, but still does not replace structured joint coordination.
Current SSRM-3D coupled crisis actor-critic evidence does not satisfy item 75: the critic trains across `71` crises with low value loss, but selected held-out actor-critic crisis score, resolved rate, and coupled response are all `0.000`; total score falls to `0.504` versus `0.520` for active policy and `0.594` for fixed-joint coordination.
Current SSRM-3D coupled crisis memory-policy evidence does not satisfy item 76: recurrent crisis-window sequence updates train across `90` crises, but held-out crisis score, resolved rate, and coupled response remain `0.000`; the controller loses the active policy's partial coupled response and remains far below fixed-joint coordination.
Current SSRM-3D coupled crisis process-policy evidence does not satisfy item 77: explicit two-channel process pressure trains across `91` crises, but held-out crisis score, resolved rate, and coupled response remain `0.000`; the selected policy collapses to social response `1.000` with environmental response `0.000`, while fixed-joint coordination remains far stronger with crisis score `0.432` and coupled response `0.731`.
Current SSRM-3D coupled crisis minimum-channel planner evidence supports item 78 as a bounded structured-planning pass: validation selects `conservative_min`; held-out randomized 96h worlds average `5.667` post-gate crises; crisis score is `0.590` versus `0.000` return-selected and `0.675` fixed-joint; resolved rate is `0.878`; coupled response is `0.828`; and social/culture plus environment ablations both collapse crisis score and coupled response. This is still engineered dynamic planning around learned action heads, not open-ended learned civilization.
Current SSRM-3D coupled crisis planner-distillation evidence does not satisfy item 79: the recurrent policy trains on `24568` planner-labeled active-crisis examples and reaches `0.986` imitation accuracy, but once the planner is removed held-out crisis score remains `0.000`, resolved rate is only `0.289`, and coupled response is only `0.179` versus `0.828` for the teacher planner.
Current SSRM-3D coupled crisis closed-loop recovery evidence does not satisfy item 80: DAgger-style student-state relabeling expands training to `74756` aggregate examples, but after planner removal held-out crisis score, resolved rate, and coupled response are all `0.000`; the teacher planner remains far stronger with `0.590` crisis score and `0.828` coupled response.
Current SSRM-3D coupled crisis consequence-recovery evidence partially supports item 81 but does not satisfy the strong claim: consequence weighting trains on `166169` active-crisis examples and raises held-out crisis score to `0.028`, resolved rate to `0.356`, and coupled response to `0.355` over return-selected zeros. Social/culture and environment ablations collapse coupled response, but crisis score remains far below the minimum-channel planner's `0.590` and fixed-joint `0.675`.
Current SSRM-3D coupled crisis sequence-value recovery evidence does not satisfy item 82: the completed-window process-value critic trains on `166169` examples with `0.701` pairwise accuracy and validation selects nonzero value bias `0.25`, but held-out crisis score falls to `0.003`, total score falls to `0.491`, and the controller does not improve over Report 126 consequence recovery.
Current SSRM-3D coupled crisis counterfactual sequence recovery evidence does not satisfy item 83: the cloned-rollout plan-value model trains on `1024` counterfactual window examples with `0.567` pairwise accuracy, but validation selects plan bias `0.0`. The selected recurrent policy reaches held-out crisis score `0.036`, resolved rate `0.478`, and coupled response `0.355`, but total score is slightly below Report 126 and the counterfactual plan layer itself is not active.
Current SSRM-3D coupled crisis direct counterfactual-policy evidence does not satisfy item 84: the direct recurrent policy trains on `4913` cloned-window label examples with `0.615` weighted accuracy, but validation selects direct bias `0.0`. Held-out direct crisis score, resolved rate, and coupled response all remain `0.000`, and total score `0.466` falls below consequence recovery `0.520`.
Current SSRM-3D coupled crisis active consequence-optimization evidence does not satisfy item 85: delayed policy-gradient fine-tuning trains across `57` crises but scores only `0.484` total with `0.060` coupled response, while the learned action-value controller trains to `0.075` weighted MAE and improves over return-selected total score from `0.487` to `0.501`. It still falls below consequence recovery `0.520`, resolved rate `0.356`, and coupled response `0.355`, so the strong learned coupled-repair gate fails.
Current SSRM-3D coupled crisis MPC sequence-optimizer evidence partially supports item 86 but does not satisfy the learned-transfer claim: cloned rollout-scored sequence commitment raises total score to `0.683`, crisis score to `0.348`, resolved rate to `0.656`, and coupled response to `0.565`, with social/culture and environment ablations collapsing crisis and coupled response. The verdict remains `partial_or_failed` because the strict teacher-transfer threshold requires crisis score `>=0.350`, and the controller still depends on supplied plan templates plus cloned simulator lookahead.
Current SSRM-3D coupled crisis MPC sequence-distillation evidence does not satisfy item 87: the recurrent student trains on `24633` MPC teacher examples with `0.596` accuracy and `0.499` balanced accuracy, but after rollout scoring is removed held-out crisis score, resolved rate, social response, and coupled response all fall to `0.000`; total score `0.457` is below consequence recovery `0.520` and return-selected `0.487`.
Current SSRM-3D coupled crisis MPC closed-loop recovery evidence does not satisfy item 88: one student-state relabeling pass expands training to `45789` aggregate examples and raises total score over the initial MPC-distilled student from `0.468` to `0.506`, but held-out crisis score, resolved rate, and coupled response remain `0.000`; the recovered policy collapses into social-only crisis response and still fails planner-free coupled repair.
Current SSRM-3D coupled crisis student-sequence consequence evidence does not satisfy item 89: student-created counterfactual windows add `25615` high-value active-crisis examples with mean return `0.823`, but the final recurrent policy reaches only `0.508` total score versus `0.520` for consequence recovery, and held-out crisis score, resolved rate, environment response, and coupled response all remain `0.000`.
Current SSRM-3D readiness closed-loop recovery evidence does not satisfy item 90: two student-state relabeling passes expand training to `124711` aggregate steps and raise held-out readiness-world maturation score from `0.212` to `0.470`, with final alive improving from `0.0` to `14.0`. The strong claim still fails because knowledge transfer remains `0.000`, final readiness is only `0.349` versus `1.000` designed, and body/tools/previous-action ablations are inverted.
Current SSRM-3D readiness sequence-consequence evidence partially supports item 91 only as a bounded planning bridge: cloned short-rollout sequence planning reaches held-out score `1.000`, final alive `23.0`, final readiness `1.000`, and knowledge transfer `1.000`. The planner-free `sequence_gru` fails the learned-transfer claim with score `0.287`, final alive `0.0`, knowledge transfer `0.000`, and unstable ablations.

Current software repair bridge evidence supports item 92 first through Report 139 and then as a stronger dynamic extension in Report 141. Report 139 remains the toy 15-task bridge. Report 141 expands to `120` seeded tasks plus 5 deterministic false-positive calibration tasks (125 total) with held-out families, noisy irrelevant signals, and explicit ambiguity/risk channels: `visible_test_only` has hidden pass `0.344`, wrong-fix `0.864`, and weakest-channel `0.060022`, while `weighted_quality_critic` reaches hidden pass `1.000`, wrong-fix `0.008`, root-cause repair `0.968` (all), and regression avoidance `1.000` with zero false-positive and zero overblocking. This is still not real repo coding or proof of frontier LLM improvement.

Current deep-time playable-world evidence supports item 93 only as a staged bridge. Report 142 compresses `4096` simulated years into deterministic epochs and emits avatar-entry packets with native tokens, sensory rates, internal workspace fields, and conversation hooks. Report 143 runs deterministic avatar interventions. Report 144 adds typed embodied avatar input. Report 145 adds autonomous live-agent ticks with readiness `0.857642`. Report 146 adds persistent object affordances with capped readiness `1.000000`. Report 147 binds those objects to a place graph with readiness `0.948822`. Report 148 lets agents modify that graph with infrastructure readiness `0.829745`. Report 149 adds governance over infrastructure futures with proposal-governance readiness `0.921374`. Report 150 makes governance histories questionable through deterministic avatar dialogue with readiness `0.970890`. Report 151 adds persistent faction memory and audited reconstructed rejected-proposal bodies with faction-dialogue readiness `0.986875`. Report 152 stores accepted and rejected proposal bodies at source during the council loop with source-native readiness `1.000000`. Report 153 trains a deterministic learned faction-dialogue policy over source-native ledgers with readiness `0.975000`. Report 154 adds recurrent turn-by-turn avatar dialogue with readiness `1.000000`. Report 155 connects recurrent dialogue to live body/workspace/world state with readiness `0.967800`, body `1.000000`, workspace `1.000000`, world `1.000000`, avatar `1.000000`, and frequency `0.677999`. This still does not prove subjective consciousness, mature live agents, LLM-backed open dialogue, complete playable worlds, unscripted civilization, or real open-ended culture.

The SSRM-3D done-enough gates keep that result bounded: the 3D track is not done until learned control, tool-making or externalized cognition, real social pressure, and targeted ablation all pass. Gate 1 has useful learned-control precursors and a physics-first offline recurrent benchmark; gate 2 has a partial externalized-cognition precursor plus a learned tool-memory bridge; gate 3 has partial social-pressure and costly-communication precursors plus a learned social-memory bridge; gate 4 has continuity-record and learned continuity/attention precursors but is still incomplete.

If agents with no persistent self-equivalent representation match performance, transfer, recovery, and compression under those conditions, the strong self-necessity claim fails.

Current browser-world evidence adds Report 248 as a deterministic post-epoch playable avatar-entry ceremony. It consumes the Report 247 4,200-year pre-avatar epoch artifact and generates 9 ceremony steps, 72 live avatar movement frames, 6 lineage history inspection frames, 36 culture-conditioned response frames, 18 welfare gate checks, 14 technology/ritual affordances, 72 replay frames, and 72 browser-world v8 ticks. The run passes with readiness `0.988633` and weakest-channel score `0.889722`; the weakest channel is deterministic typed local-act handling, preserving the boundary that this is not open-ended natural language or subjective consciousness.

Report 249 moves from avatar entry to post-entry live society consequences. It generates 140 post-entry avatar action frames across 14 days, 140 lineage memory updates, 84 technology access consequences, 140 relationship/welfare consequence frames, 84 routine schedule updates, 84 public reputation frames, 140 replay frames, and 140 browser-world v9 ticks. The run passes with readiness `0.984807` and weakest-channel score `0.877581`; the weakest channel remains typed-intent consequence confidence, and the report explicitly keeps the boundary that this is deterministic consequence wiring rather than real consciousness, real consent, or autonomous natural language.

Report 250 adds autonomous post-entry society ticks. It generates 224 autonomous society ticks across 16 days, 224 agent need frames, 224 consequence memory carry frames, 224 routine autonomy frames, 112 agent-agent interactions, 112 technology autonomy frames, 224 welfare guardrail frames, 224 replay frames, and 224 browser-world v10 ticks. The run passes with readiness `0.992727` and weakest-channel score `0.909091`; the weakest channel is agent-agent interaction continuity, after tightening the metric so an every-other-tick social cadence is strong but not perfect.

Report 251 adds long-horizon sleep and avatar re-entry. It generates 56 post-entry days, 336 sleep/wake cycle frames, 336 rest-debt recovery frames, 336 stored rehearsal frames, 5 avatar absence/re-entry frames, 30 re-entry relationship consequences, 336 circadian schedule carryover frames, 336 welfare sleep guardrail frames, 56 replay frames, and 336 browser-world v11 ticks. The run passes with readiness `0.967682` and weakest-channel score `0.833333`; the weakest channel is welfare sleep guardrails, correctly marking long-horizon welfare as still close to the floor.

Report 252 adds remembered avatar re-entry dialogue. It generates 30 absence summary frames, 180 multi-turn dialogue frames, 30 repair/renegotiation frames, 30 refusal calibration frames, 30 schedule dialogue frames, 30 relationship memory frames, 180 replay frames, and 180 browser-world v12 ticks. The run passes with readiness `0.967115` and weakest-channel score `0.833333`; the weakest channel is private workspace boundary wording, because public dialogue can say that private workspace is sealed even while the private trace remains hidden.

Report 253 adds live post-reentry choice branches. It generates 150 live re-entry choice frames, 450 branch future outcome frames, 150 future schedule branch frames, 150 access/trust branch frames, 132 agent-initiated follow-up frames, 150 branch replay comparison frames, and 150 browser-world v13 ticks. The run passes with readiness `0.982054` and weakest-channel score `0.864019`; the weakest channel is typed choice branch confidence, preserving the boundary that these are deterministic parser/template branches rather than open-ended language.

Report 254 adds actual browser-local branch mutation. It generates 150 browser branch selection frames, 150 in-browser mutable state frames, 150 reload/restore probes, 142 agent follow-ups after reload, 150 schedule/access/trust mutation frames, 150 rollback frames, 150 replay export frames, and 150 browser-world v14 ticks. The run passes with readiness `0.989557` and weakest-channel score `0.869464`; the weakest channel remains typed selection confidence, while localStorage-backed branch state, restore, rollback, and follow-up all pass in the deterministic artifact model.

Report 255 adds multi-agent concurrent branch conflict arbitration. It generates 168 concurrent branch group frames, 168 branch conflict frames, 144 real conflict frames, 168 arbitration frames, 93 follow-up arbitration frames, 168 schedule/access/trust conflict frames, 168 partial rollback isolation frames, 168 replay export frames, and 168 browser-world v15 ticks. The run passes with readiness `0.925220` and weakest-channel score `0.856346`; the weakest channel is typed arbitration confidence, while conflict detection, reload-stable follow-up, partial rollback isolation, and replay integrity now pass without claiming open-ended language, subjective consciousness, or real consent.

Report 256 turns multi-agent branch conflict arbitration into persistent remembered gameplay. It generates 21 gameplay day frames, 252 live conflict decisions, 252 arbitration memory carry frames, 252 later request/refusal frames, 252 access/relationship posture frames, 252 repair/decay frames, 252 persistent branch state frames, 252 gameplay replay frames, and 252 browser-world v16 ticks. The run passes with readiness `0.902131` and weakest-channel score `0.846036`; the weakest channel is typed gameplay decision confidence, while remembered arbitration reuse, later request/refusal binding, access/posture changes, and repair-without-erasure now pass as deterministic multi-day gameplay scaffolding.

Report 257 adds agent-authored counterproposals and negotiated compromise. It generates 280 conflict arc frames, 630 agent counterproposal frames, 280 negotiated compromise frames, 280 multi-party consent boundary frames, 280 consent memory recall frames, 280 counterproposal gameplay effect frames, 280 failed compromise repair frames, 280 negotiation replay frames, and 280 browser-world v17 ticks. The run passes with readiness `0.899875` and weakest-channel score `0.832143`; the weakest channel is visible gameplay effect binding, while agent-authored terms, consent boundary recall, avatar override resistance, remembered compromise reuse, and failed-compromise repair now pass as deterministic social gameplay scaffolding.

Report 258 adds multi-turn agent-led negotiation dialogue and compromise ceremonies. It generates 288 dialogue turn frames, 288 counteroffer loop frames, 288 proposal revision frames, 288 compromise ceremony frames, 288 ceremony memory recall frames, 288 body/world expression frames, 288 sensory negotiation frames, 288 dialogue breakdown repair frames, 288 negotiation replay frames, and 288 browser-world v18 ticks. The run passes with readiness `0.904916` and weakest-channel score `0.836806`; the weakest channel is compromise ceremony rate, while agent-led turns, counteroffer loops, remembered ceremonies, body/world expression, multi-sensory dialogue binding, and breakdown repair now pass as deterministic dialogue-gameplay scaffolding.

Report 259 adds embodied negotiation animation choreography. It generates 336 animation state frames, 336 turn-taking gesture frames, 336 proximity choreography frames, 336 object-handling ceremony frames, 336 multi-sensory animation frames, 336 gesture-misread repair frames, 336 animation replay frames, and 336 browser-world v19 ticks. The run passes with readiness `0.936282` and weakest-channel score `0.898148`; the weakest channel is ceremony-object visibility, while animation-state matching, turn gestures, proximity choreography, object handling, sensory timing, and gesture repair now pass as deterministic embodied negotiation scaffolding.

Report 260 adds playable browser scene geometry for avatar-agent negotiation. It generates 336 scene geometry frames, 336 avatar-agent position frames, 336 sprite/body layer frames, 336 local collision probes, 336 collision-aware object ceremony frames, 336 object motion frames, 336 depth/camera cue frames, 336 scene input affordance frames, 336 multi-sensory scene frames, 336 scene replay frames, and 336 browser-world v20 ticks. The run passes with readiness `0.898596` and weakest-channel score `0.826923`; the weakest channel is object ceremony completion/visibility, while local coordinates, sprite layers, collision probes, object handoff motion, input affordances, depth cues, and replayable scene state now pass as deterministic scene-geometry scaffolding.

Report 261 adds live browser-local scene state mutation. It generates 360 keyboard movement frames, 360 scene state mutation frames, 360 collision/proximity prompt frames, 360 object ceremony persistence frames, 360 localStorage snapshot frames, 360 save/restore position frames, 360 live scene replay frames, 360 multi-sensory live scene frames, and 360 browser-world v21 ticks. The run passes with readiness `0.952769` and weakest-channel score `0.922222`; the weakest channel is proximity prompt surface, while keyboard avatar movement, collision handling, object ceremony persistence, localStorage snapshots, visible save/restore, and replayable mutation state now pass as deterministic live-scene scaffolding.

Report 262 adds free-move proximity dialogue, persistent multi-object ceremony inventory, and reload-stable agent reaction state. It generates 384 free-move path frames, 384 proximity dialogue prompt frames, 384 multi-object inventory frames, 384 inventory transaction frames, 384 agent reaction-state frames, 384 reload-stability probes, 384 localStorage inventory snapshots, 384 dialogue/reaction replay frames, 384 multi-sensory free-move frames, and 384 browser-world v22 ticks. The run passes with readiness `0.899450` and weakest-channel score `0.817708`; the browser artifact now supports continuous local movement, proximity prompts, object inventory actions, save/restore, reaction panels, and replay export while preserving the no-consciousness-claim boundary.

Report 263 adds object-specific proximity dialogue, agent-owned inventory requests, and reaction consequences that alter later scene behavior. It generates 416 object-specific dialogue frames, 416 agent-owned inventory request frames, 416 reaction-consequence frames, 416 later scene behavior frames, 416 access/refusal frames, 416 agent-initiated behavior frames, 416 reaction-memory snapshots, 416 multi-sensory consequence frames, 416 replay frames, and 416 browser-world v23 ticks. The run passes with readiness `0.886592` and weakest-channel score `0.795673`; the weakest channel is agent-owned request resolution, while object-specific dialogue, owner references, reaction-to-pathing, reaction-to-access, delayed follow-up, refusal alternatives, storage, sensory binding, and replay now pass as deterministic behavior-consequence scaffolding.

Report 264 adds multi-day agent-owned task obligations, object return duties, and compounding trust/access consequences across scene visits. It generates 540 scene visit frames, 540 owned-task obligation frames, 540 object-return obligation frames, 540 trust/access compounding frames, 540 agent follow-up frames, 540 repair/deferral frames, 540 obligation-memory snapshots, 540 multi-sensory obligation frames, 540 replay frames, and 540 browser-world v24 ticks. The run passes with readiness `0.884357` and weakest-channel score `0.798005`; the weakest channel is object-return request resolution, while multi-day obligation persistence, trust/access compounding, delayed follow-up recurrence, repair/deferral integrity, residual debt visibility, storage, and replay now pass as deterministic obligation-continuity scaffolding.
Report 265 adds many-day project/material/body-cost continuity to the browser-world line. It generates 648 project progress rows, 648 material inventory rows, 648 time reservation rows, 648 body-cost/fatigue rows, 648 obligation-project blocker rows, 648 reshape rows, 648 follow-up rows, 648 memory rows, 648 sensory rows, 648 replay rows, and 648 browser-world v25 ticks. The run passes with readiness `0.936943` and weakest-channel score `0.835000`; the weakest channel is project progress under constraints at `0.835000`. The run keeps 33 blocker frames, 4 reshaped projects, 7 material shortage rows, and 512 fatigue recovery rows visible rather than pretending project completion is solved.
Report 266 adds cooperative project/trade/workshop continuity to the browser-world line. It generates 840 delegated subproject rows, 840 trade-debt ledger rows, 840 shared-workshop rows, 840 material-priority conflict rows, 840 arbitration rows, 840 routine outcome rows, 840 initiative rows, 840 workshop sensory rows, 840 cooperative memory rows, 840 replay rows, and 840 browser-world v26 ticks. The run passes with readiness `0.920034` and weakest-channel score `0.796083`; the weakest channel is cooperative progress under tradeoffs at `0.796083`. The run keeps 417 material-priority conflicts, 103 overbooked workshop frames, and 4 routine mutations visible, so cooperation remains costly and consequential rather than decorative.
Report 267 adds household/workshop economy infrastructure continuity to the browser-world line. It generates 864 household-economy rows, 864 durable-building rows, 864 tool-wear rows, 864 skill-specialization rows, 864 project-failure rows, 864 routine-infrastructure mutation rows, 864 ecology-change rows, 864 maintenance-debt rows, 864 agent initiative rows, 864 sensory infrastructure rows, 864 memory rows, 864 replay rows, and 864 browser-world v27 ticks. The run passes with readiness `0.922088` and weakest-channel score `0.779035`; the weakest channel is economy under decay tradeoffs at `0.779035`. The run keeps 18 infrastructure failure events, 4 routine mutations, and 208 ecology feedback rows visible, so built infrastructure becomes a durable source of care, strain, and later-life consequences.
Report 268 adds multi-household regional supply chains, seasonal weather, repair guilds, apprenticeship succession, building upgrades, collapse recovery, and ecology/resource migration to the browser-world line. It generates 1024 supply-chain rows, 1024 seasonal-weather rows, 1024 repair-guild rows, 1024 apprenticeship rows, 1024 building-upgrade rows, 1024 collapse-recovery rows, 1024 resource-migration rows, 1024 regional-routine rows, 1024 initiative rows, 1024 sensory rows, 1024 memory rows, 1024 replay rows, and 1024 browser-world v28 ticks. The run passes with readiness `0.935056` and weakest-channel score `0.812000`; the weakest channel is regional economy under seasonal tradeoffs at `0.812000`. The run keeps 21 collapse events, 9 route blocks, 5 succession events, 10 building upgrades, and 640 resource migrations visible across five regions.
Report 269 adds cross-region route planning, mobile caravans, stored seasonal forecasts, playable disaster drills, intergenerational guild records, and visible avatar recovery interventions to the browser-world line. It generates 1008 route-planning rows, 1008 mobile-caravan rows, 1008 forecast-storage rows, 1008 disaster-drill rows, 1008 guild-record rows, 1008 avatar-intervention rows, 1008 regional-recovery rows, 1008 sensory-caravan rows, 1008 route-memory rows, 1008 replay rows, and 1008 browser-world v29 ticks. The run passes with readiness `0.931894` and weakest-channel score `0.818000`; the weakest channel is route recovery under forecast tradeoffs at `0.818000`. The run keeps 30 playable disaster-drill rows, 12 guild succession records, 176 avatar interventions, 18 caravan arrivals, 551 detours, and 30 unresolved recovery rows visible.
Report 270 adds live browser route selection controls, avatar-chosen caravan tasks, forecast editing, disaster-drill minigame steps, guild-record inspection, reload persistence probes, and persistent recovery consequences to the browser-world line. It generates 960 route-selection rows, 960 avatar-caravan task rows, 960 forecast-edit rows, 960 drill-minigame rows, 960 guild-inspection rows, 960 reload-probe rows, 960 recovery-consequence rows, 960 sensory route-control rows, 960 memory rows, 960 replay rows, and 960 browser-world v30 ticks. The run passes with readiness `0.920791` and weakest-channel score `0.803125`; the weakest channel is live recovery after reload at `0.808163`. The run keeps 318 live selections, 137 avatar tasks, 186 forecast edits, 176 accepted forecast edits, 131 drill steps, 205 guild inspections, 147 reload probes, and 132 reload recovery consequences visible.
Report 271 adds editable localStorage-style state import/export, route-control branch comparison, simultaneous multi-route caravan tasks, persistent recovery consequences, and later agent dialogue about avatar route decisions to the browser-world line. It generates 960 editable-state rows, 960 import/export rows, 960 branch-comparison rows, 960 simultaneous-task rows, 960 persistent-consequence rows, 960 later-dialogue rows, 960 memory rows, 960 replay rows, 960 sensory rows, and 960 browser-world v31 ticks. The run passes with readiness `0.937185` and weakest-channel score `0.824000`; the weakest channel is later dialogue after branch reload at `0.824000`. The run keeps 235 import attempts, 226 accepted imports, 345 simultaneous tasks, 21 resource conflicts, 118 dialogue turns, and 151 persisted recovery consequences visible.
Report 272 adds live multi-agent route dialogue choices, branch merge/rollback state, shared world-state snapshots, snapshot reload probes, and body-language reactions to avatar logistics decisions to the browser-world line. It generates 1008 multi-agent dialogue rows, 1008 dialogue-consequence rows, 1008 branch merge/rollback rows, 1008 shared snapshot rows, 1008 body-language rows, 1008 logistics-memory rows, 1008 reload-probe rows, 1008 sensory rows, 1008 replay rows, and 1008 browser-world v32 ticks. The run passes with readiness `0.913279` and weakest-channel score `0.761905`; the weakest channel is frequency/flower dialogue rhythm at `0.761905`. The run keeps 408 dialogue choices, 384 valid dialogue choices, 315 merge attempts, 296 merge successes, 46 rollbacks, 568 shared snapshots, 648 visible body-language frames, and 102 body-language reload frames visible.

### Report 273: SSRM-3D Browser World v33 Embodied Dialogue Animation/Merge/Snapshot/Delayed-Reaction Bridge

Report 273 turns the multi-agent route-dialogue bridge into embodied browser animation scaffolding. It generates 1008 embodied dialogue animation rows, 479 live merge-control events, 733 shared-session snapshot exchange rows, 112 delayed social/body reactions due, 104 visible delayed reactions, and 104 reload-persistent delayed reactions. The run passes with readiness `0.928728`, mean channel score `0.973611`, and weakest-channel score `0.824000`. The weakest channel is `delayed_body_after_avatar_logistics` at `0.824000` because the logistics-to-body channel is intentionally capped as a negative-control pressure point; the benchmark should not pretend delayed body reactions are complete before clickable localStorage controls and follow-up dialogue exist.

Artifacts: `experiments/ssrm_3d_browser_world_v33_embodied_dialogue_animation_merge_snapshot_delayed_reaction_bridge.py`, `artifacts/ssrm_3d_browser_world_v33_embodied_dialogue_animation_merge_snapshot_delayed_reaction_bridge_results.json`, `visualizations/ssrm_3d_browser_world_v33_embodied_dialogue_animation_merge_snapshot_delayed_reaction_bridge.html`, and `docs/273_ssrm_3d_browser_world_v33_embodied_dialogue_animation_merge_snapshot_delayed_reaction_bridge_report.md`. Boundary: deterministic browser-local gameplay/animation scaffold only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, complete gameplay, complete 3D engine, or metaphysical frequency claim. Next gate: browser world v34 with actual clickable animation-state controls, branch merge buttons mutating localStorage, session snapshot paste/import UI, and delayed agent follow-up dialogue after visible body-language reactions.

### Report 274: SSRM-3D Browser World v34 Clickable Animation Controls/LocalStorage/Snapshot Import/Follow-Up Dialogue Bridge

Report 274 turns the v33 embodied animation scaffold into an actual clickable browser-control artifact. The generated HTML includes animation buttons, merge/rollback buttons, localStorage save/restore, snapshot export, snapshot paste/import, delayed follow-up rendering, and replay preview. The deterministic run passes with readiness `0.937142`, mean channel score `0.980488`, and weakest-channel score `0.836000`. It records 426 animation clicks, 294 localStorage branch mutations, 384 snapshot export/import rows, 185 valid snapshot imports, 665 visible body reactions, 700 delayed follow-up dialogue rows, 671 visible follow-ups, 2507 replay events, and 32 browser buttons.

The weakest channel is `followup_not_oversaturated` at `0.836000`. That is intentional: follow-up dialogue is present but bounded so every click does not become noisy chatter. Artifacts: `experiments/ssrm_3d_browser_world_v34_clickable_animation_controls_localstorage_snapshot_import_followup_dialogue_bridge.py`, `artifacts/ssrm_3d_browser_world_v34_clickable_animation_controls_localstorage_snapshot_import_followup_dialogue_bridge_results.json`, `visualizations/ssrm_3d_browser_world_v34_clickable_animation_controls_localstorage_snapshot_import_followup_dialogue_bridge.html`, and `docs/274_ssrm_3d_browser_world_v34_clickable_animation_controls_localstorage_snapshot_import_followup_dialogue_bridge_report.md`. Boundary: deterministic browser-local gameplay/control scaffold only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, complete gameplay, complete 3D engine, or metaphysical frequency claim. Next gate: browser world v35 with avatar conversation input, click-to-talk agent replies, bounded refusal/recovery choices, and agent-side sensory/body state updates caused by user interaction.

### Report 275: SSRM-3D Browser World v35 Avatar Conversation/Click-To-Talk/Bounded Refusal/Recovery/Sensory Body State Bridge

Report 275 adds avatar conversation input and click-to-talk agent replies to the browser-world stack. The generated browser artifact includes a real avatar text input, send button, per-agent talk buttons, per-agent recovery/status/care buttons, localStorage conversation memory, public body-state rendering, and replay preview. The deterministic run passes with readiness `0.936187`, mean channel score `0.976553`, and weakest-channel score `0.842000`. It records 605 avatar input rows, 807 click-to-talk replies, 778 visible replies, 134 bounded refusals, 116 resolved refusals, 116 recovery choices clicked, 807 sensory/body updates, 807 conversation memory rows, 807 relationship continuity rows, 1412 replay events, and 25 browser buttons.

The weakest channel is `dialogue_not_unbounded` at `0.842000`. That is intentional: dialogue is present but capped so the benchmark rewards bounded interaction rather than noisy over-talking. Artifacts: `experiments/ssrm_3d_browser_world_v35_avatar_conversation_click_to_talk_bounded_refusal_recovery_sensory_body_state_bridge.py`, `artifacts/ssrm_3d_browser_world_v35_avatar_conversation_click_to_talk_bounded_refusal_recovery_sensory_body_state_bridge_results.json`, `visualizations/ssrm_3d_browser_world_v35_avatar_conversation_click_to_talk_bounded_refusal_recovery_sensory_body_state_bridge.html`, and `docs/275_ssrm_3d_browser_world_v35_avatar_conversation_click_to_talk_bounded_refusal_recovery_sensory_body_state_bridge_report.md`. Boundary: deterministic browser-local avatar-conversation scaffold only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, complete gameplay, complete 3D engine, or metaphysical frequency claim. Next gate: browser world v36 with agent-side private interior workspace ticks, self-boundary state, ownership-sensitive memory, bounded no/yes consent loops, and visible ego/body-language consequences from repeated avatar talk.

### Report 276: SSRM-3D Browser World v36 Private Interior Workspace/Self-Boundary/Ownership/Consent/Ego Body-Language Bridge

Report 276 adds the first explicit private interior/ego layer to the browser-world stack. Each agent now has sealed private workspace ticks, self-boundary state, ownership-sensitive memory, bounded yes/no consent loops, repeated-talk relationship consequences, and public body-language expression tied to ego state. The deterministic run passes with readiness `0.921121`, mean channel score `0.966371`, and weakest-channel score `0.815536`. It records 1440 private workspace ticks, 822 self-boundary rows, 822 ownership memories, 822 consent loops, 397 no decisions, 665 non-obedient or conditional consent decisions, 328 recovered no decisions, 822 visible ego/body-language rows, 822 repeated-talk consequence rows, 822 public trace rows, and 30 browser buttons.

The weakest channel is `consent_not_unbounded_obedience` at `0.815536`. That is intentional: the benchmark rewards bounded refusal and conditional consent instead of universal obedience. Artifacts: `experiments/ssrm_3d_browser_world_v36_private_interior_workspace_self_boundary_ownership_consent_ego_body_language_bridge.py`, `artifacts/ssrm_3d_browser_world_v36_private_interior_workspace_self_boundary_ownership_consent_ego_body_language_bridge_results.json`, `visualizations/ssrm_3d_browser_world_v36_private_interior_workspace_self_boundary_ownership_consent_ego_body_language_bridge.html`, and `docs/276_ssrm_3d_browser_world_v36_private_interior_workspace_self_boundary_ownership_consent_ego_body_language_bridge_report.md`. Boundary: deterministic browser-local private-interior scaffold only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, complete gameplay, complete 3D engine, or metaphysical frequency claim. Next gate: browser world v37 with pre-avatar deep-time civilization strata, emergent ritual/language/technology ledgers, settlement memory, and avatar entry only after many simulated generations of culture formation.

### Report 277: SSRM-3D Browser World v37 Deep-Time Civilization/Language/Technology/Avatar Entry Bridge

Report 277 adds the first pre-avatar deep-time civilization layer. The world now develops for 2400 simulated years across 80 generations and 6 settlements before avatar entry. The deterministic run passes with readiness `0.940051`, mean channel score `0.983787`, and weakest-channel score `0.838000`. It records 480 deep-time generation rows, 480 civilization strata rows, 480 emergent language ledger rows, 480 technology ledger rows, 480 ritual culture ledger rows, 480 settlement memory rows, 474 locked pre-avatar gate rows, 6 final avatar-entry-allowed gate rows, and 8 browser buttons.

The weakest channel is `cultural_diversity_without_chaos` at `0.838000`. That is intentional: the benchmark rewards cultural variety without random incoherence. Artifacts: `experiments/ssrm_3d_browser_world_v37_deeptime_civilization_language_technology_avatar_entry_bridge.py`, `artifacts/ssrm_3d_browser_world_v37_deeptime_civilization_language_technology_avatar_entry_bridge_results.json`, `visualizations/ssrm_3d_browser_world_v37_deeptime_civilization_language_technology_avatar_entry_bridge.html`, and `docs/277_ssrm_3d_browser_world_v37_deeptime_civilization_language_technology_avatar_entry_bridge_report.md`. Boundary: deterministic browser-local deep-time civilization scaffold only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, complete gameplay, complete 3D engine, or metaphysical frequency claim. Next gate: browser world v38 with playable avatar entry into the matured settlement world, resident agents inheriting culture/language/technology strata, dialect-conditioned conversation, and persistent post-entry consequences.

### Report 278: SSRM-3D Browser World v38 Playable Avatar Entry/Matured Settlement/Dialect Consequence Bridge

Report 278 converts the deep-time civilization ledger into a playable post-entry browser scaffold. The avatar can enter the matured world, select settlements, move locally, talk to residents, see dialect-conditioned replies, and leave persistent post-entry consequences. The deterministic run passes with readiness `0.929296`, mean channel score `0.970423`, and weakest-channel score `0.833333`. It records 72 play days, 154 avatar-entry rows, 153 enabled entry rows, 864 resident inheritance rows, 864 dialect-conditioned conversation rows, 864 playable movement rows, 864 post-entry consequence rows, 161 persistent reload-state rows, 864 culture/technology binding rows, 864 browser ticks, and 14 browser buttons.

The weakest channel is `technology_conversation_reference` at `0.833333` because not every resident reply references technology; this keeps the dialogue from becoming a repetitive tech exposition. Artifacts: `experiments/ssrm_3d_browser_world_v38_playable_avatar_entry_matured_settlement_dialect_consequence_bridge.py`, `artifacts/ssrm_3d_browser_world_v38_playable_avatar_entry_matured_settlement_dialect_consequence_bridge_results.json`, `visualizations/ssrm_3d_browser_world_v38_playable_avatar_entry_matured_settlement_dialect_consequence_bridge.html`, and `docs/278_ssrm_3d_browser_world_v38_playable_avatar_entry_matured_settlement_dialect_consequence_bridge_report.md`. Boundary: deterministic browser-local playable avatar-entry scaffold only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, complete gameplay, complete 3D engine, or metaphysical frequency claim. Next gate: browser world v39 with spatially navigable rooms, object manipulation, resident schedules, body-state consequences from temperature/wetness/pain, and dialect memory that persists across multiple avatar visits.

### Report 279: SSRM-3D Browser World v39 Spatial Rooms/Object Manipulation/Schedules/Body State/Dialect Memory Bridge

Report 279 moves the playable avatar-entry scaffold toward a place-like world. The avatar now navigates settlement rooms, manipulates objects, encounters resident schedules, accumulates body-state consequences from temperature/wetness/pain, and builds dialect memory across repeated visits. The deterministic run passes with readiness `0.932883`, mean channel score `0.985513`, and weakest-channel score `0.810079`. It records 84 play days, 1008 spatial navigation rows, 372 object manipulation rows, 1008 resident schedule rows, 1008 body-state rows, 815 environmental exposure rows, 432 dialect memory rows, 420 multi-visit dialect memories, 1008 resident interaction rows, 191 persistent spatial-state rows, 1008 browser ticks, and 30 browser buttons.

The weakest channel is `body_consequence_not_overdriven` at `0.810079`. That is intentional: body consequences are bounded so wetness, cold, pain, rest, and care matter without becoming spectacle or endless distress. Artifacts: `experiments/ssrm_3d_browser_world_v39_spatial_rooms_object_schedules_body_state_dialect_memory_bridge.py`, `artifacts/ssrm_3d_browser_world_v39_spatial_rooms_object_schedules_body_state_dialect_memory_bridge_results.json`, `visualizations/ssrm_3d_browser_world_v39_spatial_rooms_object_schedules_body_state_dialect_memory_bridge.html`, and `docs/279_ssrm_3d_browser_world_v39_spatial_rooms_object_schedules_body_state_dialect_memory_bridge_report.md`. Boundary: deterministic browser-local spatial/body-state scaffold only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, complete gameplay, complete 3D engine, or metaphysical frequency claim. Next gate: browser world v40 with continuous room-to-room pathfinding, manipulable object affordance chains, resident routine interruption/recovery, embodied pain/rest care loops, and dialect memory across long multi-visit sessions.

### Report 280: SSRM-3D Browser World v40 Continuous Pathfinding/Affordance/Routine/Body-Care/Dialect Session Bridge

Report 280 extends the spatial room world with continuous room-to-room pathfinding, object affordance chains, resident routine interruption and recovery, embodied pain/rest care loops, and dialect memory across long multi-visit sessions. The deterministic run passes with readiness `0.925513`, mean channel score `0.974840`, and weakest-channel score `0.810417`. It records 112 session days, 1344 pathfinding rows, 540 object affordance-chain rows, 143 routine interruptions, 122 routine recoveries, 1344 routine frames, 1344 pain/rest/care rows, 448 effective care rows, 518 dialect memory rows, 498 long-session dialect memories, 251 session persistence rows, 1344 browser ticks, and 36 browser buttons.

The weakest channel is `pain_rest_loop_not_spectacle` at `0.810417`. That is intentional: pain/rest loops are bounded so pain and care matter without becoming spectacle or endless distress. Artifacts: `experiments/ssrm_3d_browser_world_v40_continuous_pathfinding_affordance_routine_bodycare_dialect_session_bridge.py`, `artifacts/ssrm_3d_browser_world_v40_continuous_pathfinding_affordance_routine_bodycare_dialect_session_bridge_results.json`, `visualizations/ssrm_3d_browser_world_v40_continuous_pathfinding_affordance_routine_bodycare_dialect_session_bridge.html`, and `docs/280_ssrm_3d_browser_world_v40_continuous_pathfinding_affordance_routine_bodycare_dialect_session_bridge_report.md`. Boundary: deterministic browser-local continuous-pathfinding/body-care scaffold only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, complete gameplay, complete 3D engine, or metaphysical frequency claim. Next gate: browser world v41 with real-time scheduler ticks, resident task queues, multi-object crafting/repair projects, care consent before treatment, and long-session dialect relationship memory visible after save/restore.

### Report 281: SSRM-3D Browser World v41 Real-Time Scheduler/Task-Queue/Project/Care-Consent/Dialect Restore Bridge

Report 281 extends the browser-world line with real-time style scheduler ticks, resident task queues, multi-object crafting and repair projects, care consent before treatment, and dialect relationship memory that remains visible after save/restore. The deterministic run passes with readiness `0.928786`, mean channel score `0.969296`, and weakest-channel score `0.834263`. It records 128 session days, 2048 scheduler ticks, 2048 resident task queue rows, 1792 task starts, 1495 task completions, 1195 multi-object project rows, 709 care-consent rows, 137 refused/deferred care rows, 137 refusal-respected rows, 1281 dialect relationship rows, 1252 restore-visible dialect rows, 298 save/restore rows, 2048 browser ticks, and 42 browser buttons.

The weakest channel is `resident_task_completion` at `0.834263`. That is intentional pressure: resident queues should leave unfinished work instead of auto-completing every task. Artifacts: `experiments/ssrm_3d_browser_world_v41_realtime_scheduler_taskqueue_project_care_consent_dialect_restore_bridge.py`, `artifacts/ssrm_3d_browser_world_v41_realtime_scheduler_taskqueue_project_care_consent_dialect_restore_bridge_results.json`, `visualizations/ssrm_3d_browser_world_v41_realtime_scheduler_taskqueue_project_care_consent_dialect_restore_bridge.html`, and `docs/281_ssrm_3d_browser_world_v41_realtime_scheduler_taskqueue_project_care_consent_dialect_restore_bridge_report.md`. Boundary: Deterministic browser-local realtime-scheduler/task-queue/project/care-consent scaffold only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, complete gameplay, complete 3D engine, or metaphysical frequency claim. Next gate: browser world v42 with first-person sensory packets, room-local sound/smell/temperature fields, agent-owned tool claims, consent-aware dialogue hooks, and task-queue consequences from avatar interaction.

### Report 282: SSRM-3D Browser World v42 First-Person Sensory/Tool-Claim/Consent-Dialogue/Queue-Consequence Bridge

Report 282 extends the browser-world line with first-person sensory packets, room-local sound/smell/temperature fields, agent-owned tool claims, consent-aware dialogue hooks, and task-queue consequences from avatar interaction. The deterministic run passes with readiness `0.943006`, mean channel score `0.986294`, and weakest-channel score `0.842000`. It records 144 session days, 2592 first-person sensory packets, 2592 room-local sensory fields, 1440 agent-owned tool claim rows, 1332 tool-claim respected rows, 1620 consent-aware dialogue hooks, 324 refusal/defer dialogue rows, 324 refusal/defer respected rows, 2592 task-queue consequence rows, 2592 queue-changed rows, 1728 sensory-memory relationship rows, 1704 restore-visible sensory-memory rows, 337 save/restore rows, 2592 browser ticks, and 54 browser buttons.

The weakest channel is `consequence_not_overdriven` at `0.842000`. That is intentional pressure: avatar actions should create visible consequences without overdriving punishment or permanent damage. Artifacts: `experiments/ssrm_3d_browser_world_v42_first_person_sensory_tool_claim_consent_dialogue_queue_consequence_bridge.py`, `artifacts/ssrm_3d_browser_world_v42_first_person_sensory_tool_claim_consent_dialogue_queue_consequence_bridge_results.json`, `visualizations/ssrm_3d_browser_world_v42_first_person_sensory_tool_claim_consent_dialogue_queue_consequence_bridge.html`, and `docs/282_ssrm_3d_browser_world_v42_first_person_sensory_tool_claim_consent_dialogue_queue_consequence_bridge_report.md`. Boundary: Deterministic browser-local first-person sensory/tool-claim/consent-dialogue scaffold only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, complete gameplay, complete 3D engine, or metaphysical frequency claim. Next gate: browser world v43 with playable first-person avatar scene, resident gaze/posture/body-language expressions, object pickup/drop consequences, and sensory-memory-driven relationship changes after reload.

### Report 283: SSRM-3D Browser World v43 Playable Avatar/Body-Language/Object-Consequence/Memory-Reload Bridge

Report 283 extends the browser-world line with a playable first-person avatar scene, resident gaze/posture/body-language expressions, object pickup/drop consequences, and sensory-memory-driven relationship changes after reload. The deterministic run passes with readiness `0.945154`, mean channel score `0.989363`, and weakest-channel score `0.842000`. It records 156 session days, 2808 playable scene frames, 2808 resident body-language rows, 1470 object consequence rows, 1470 object pickup/drop changed rows, 1910 local interaction turns, 1805 sensory-memory reload rows, 1783 restore-recalled sensory-memory rows, 408 trust-repair rows, 2808 browser ticks, and 72 browser buttons.

The weakest channel is `object_consequence_not_overdriven` at `0.842000`. That is intentional pressure: object mistakes should create visible consequences without becoming punitive or permanently damaging. Artifacts: `experiments/ssrm_3d_browser_world_v43_playable_avatar_body_language_object_consequence_memory_reload_bridge.py`, `artifacts/ssrm_3d_browser_world_v43_playable_avatar_body_language_object_consequence_memory_reload_bridge_results.json`, `visualizations/ssrm_3d_browser_world_v43_playable_avatar_body_language_object_consequence_memory_reload_bridge.html`, and `docs/283_ssrm_3d_browser_world_v43_playable_avatar_body_language_object_consequence_memory_reload_bridge_report.md`. Boundary: Deterministic browser-local playable-avatar/body-language/object-consequence scaffold only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, complete gameplay, complete 3D engine, or metaphysical frequency claim. Next gate: browser world v44 with continuous playable scene state, multi-resident local conversation turns, body-language animation timelines, inventory ownership UI, and recoverable trust repair after object mistakes.

### Report 284: SSRM-3D Browser World v44 Continuous Scene/Multi-Resident Animation/Inventory Trust-Repair Bridge

Report 284 extends the browser-world line with continuous playable scene state, multi-resident local conversation turns, body-language animation timelines, inventory ownership UI, and recoverable trust repair after object mistakes. The deterministic run passes with readiness `0.944092`, mean channel score `0.987846`, and weakest-channel score `0.842000`. It records 168 session days, 3024 continuous scene-state rows, 3024 multi-resident conversation rows, 9072 body-language animation rows, 3024 inventory ownership UI rows, 1097 trust-repair rows, 409 save/restore rows, 3024 browser ticks, and 78 browser buttons.

The weakest channel is `trust_repair_not_overdriven` at `0.842000`. That is intentional pressure: trust repair after object mistakes should be visible and recoverable without becoming punitive or magically complete. Artifacts: `experiments/ssrm_3d_browser_world_v44_continuous_scene_multiresident_animation_inventory_trust_repair_bridge.py`, `artifacts/ssrm_3d_browser_world_v44_continuous_scene_multiresident_animation_inventory_trust_repair_bridge_results.json`, `visualizations/ssrm_3d_browser_world_v44_continuous_scene_multiresident_animation_inventory_trust_repair_bridge.html`, and `docs/284_ssrm_3d_browser_world_v44_continuous_scene_multiresident_animation_inventory_trust_repair_bridge_report.md`. Boundary: Deterministic browser-local continuous-scene/multi-resident-animation/inventory-trust-repair scaffold only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, complete gameplay, complete 3D engine, or metaphysical frequency claim. Next gate: browser world v45 with resident daily routines running while the avatar is idle, multi-agent object handoff protocols, animated refusal/consent sequences, and long-session inventory trust memory across multiple reloads.

### Report 285: SSRM-3D Browser World v45 Idle Routines/Handoff/Refusal/Inventory Trust-Memory Bridge

Report 285 extends the browser-world line with resident daily routines running while the avatar is idle, multi-agent object handoff protocols, animated refusal/consent sequences, and long-session inventory trust memory across multiple reloads. The deterministic run passes with readiness `0.941018`, mean channel score `0.983455`, and weakest-channel score `0.842000`. It records 180 session days, 9720 idle resident routine rows, 3240 idle-routine advanced rows, 2520 handoff protocol rows, 2520 valid handoff rows, 2025 animated refusal/consent rows, 929 refusal/defer rows, 2430 inventory trust memory rows, 2368 multi-reload inventory trust rows, 439 multi-reload probe rows, 3240 browser ticks, and 78 browser buttons.

The weakest channel is `refusal_consent_not_overdriven` at `0.842000`. That is intentional pressure: refusal, consent, handoff, and inventory debt should matter without becoming coercive or punitive. Artifacts: `experiments/ssrm_3d_browser_world_v45_idle_routines_handoff_refusal_inventory_trust_memory_bridge.py`, `artifacts/ssrm_3d_browser_world_v45_idle_routines_handoff_refusal_inventory_trust_memory_bridge_results.json`, `visualizations/ssrm_3d_browser_world_v45_idle_routines_handoff_refusal_inventory_trust_memory_bridge.html`, and `docs/285_ssrm_3d_browser_world_v45_idle_routines_handoff_refusal_inventory_trust_memory_bridge_report.md`. Boundary: Deterministic browser-local idle-routine/handoff/refusal-consent/inventory-trust-memory scaffold only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, complete gameplay, complete 3D engine, or metaphysical frequency claim. Next gate: browser world v46 with autonomous resident-to-resident scheduling, negotiated object loans over multiple days, visible household roles, animated apology/forgiveness arcs, and avatar conversation hooks for remembered inventory debts.

### Report 286: SSRM-3D Browser World v46 Resident Scheduling/Loans/Roles/Apology Debt-Hooks Bridge

Report 286 extends the browser-world line with autonomous resident-to-resident scheduling, negotiated object loans over multiple days, visible household roles, animated apology/forgiveness arcs, and avatar conversation hooks for remembered inventory debts. The deterministic run passes with readiness `0.942482`, mean channel score `0.985546`, and weakest-channel score `0.842000`. It records 192 session days, 3456 resident schedule rows, 3456 autonomous resident schedule rows, 2160 negotiated loan rows, 2030 loan effect rows, 13824 household role rows, 1383 apology/forgiveness rows, 2304 avatar debt-hook rows, 2304 avatar debt-hook effect rows, 459 debt memory reload rows, 3456 browser ticks, and 72 browser buttons.

The weakest channel is `apology_forgiveness_not_overdriven` at `0.842000`. That is intentional pressure: forgiveness should have visible limits and partial repair, not forced reset or permanent punishment. Artifacts: `experiments/ssrm_3d_browser_world_v46_resident_scheduling_loans_roles_apology_debt_hooks_bridge.py`, `artifacts/ssrm_3d_browser_world_v46_resident_scheduling_loans_roles_apology_debt_hooks_bridge_results.json`, `visualizations/ssrm_3d_browser_world_v46_resident_scheduling_loans_roles_apology_debt_hooks_bridge.html`, and `docs/286_ssrm_3d_browser_world_v46_resident_scheduling_loans_roles_apology_debt_hooks_bridge_report.md`. Boundary: Deterministic browser-local resident-scheduling/object-loan/household-role/apology-debt-hook scaffold only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, complete gameplay, complete 3D engine, or metaphysical frequency claim. Next gate: browser world v47 with resident-to-resident negotiations continuing during avatar absence, household role conflict mediation, multi-day loan defaults, animated forgiveness limits, and debt-aware avatar dialogue choices.

### Report 287: SSRM-3D Browser World v47 Absence Negotiation/Role Conflict/Loan Default/Forgiveness Dialogue Bridge

Report 287 extends the browser-world line with resident-to-resident negotiations continuing during avatar absence, household role conflict mediation, multi-day loan defaults, animated forgiveness limits, and debt-aware avatar dialogue choices. The deterministic run passes with readiness `0.915812`, mean channel score `0.965282`, and weakest-channel score `0.800381`. It records 204 session days, 3672 absence negotiation rows, 2939 resident-led absence-continuation rows, 1836 role conflict mediation rows, 2970 multi-day loan default rows, 2970 loan default problem rows, 1466 animated forgiveness-limit rows, 2691 debt-aware avatar choice rows, 497 absence-memory reload rows, 3672 browser ticks, and 72 browser buttons.

The weakest channel is `resident_negotiation_during_avatar_absence` at `0.800381`. That is intentional pressure: direct avatar help/repayment is not credited as resident-led absence negotiation, while forgiveness remains capped by `forgiveness_limit_not_overdriven` at `0.842000`. Artifacts: `experiments/ssrm_3d_browser_world_v47_absence_negotiation_role_conflict_loan_default_forgiveness_dialogue_bridge.py`, `artifacts/ssrm_3d_browser_world_v47_absence_negotiation_role_conflict_loan_default_forgiveness_dialogue_bridge_results.json`, `visualizations/ssrm_3d_browser_world_v47_absence_negotiation_role_conflict_loan_default_forgiveness_dialogue_bridge.html`, and `docs/287_ssrm_3d_browser_world_v47_absence_negotiation_role_conflict_loan_default_forgiveness_dialogue_bridge_report.md`. Boundary: deterministic browser-local absence-negotiation/role-conflict/loan-default/forgiveness-dialogue scaffold only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, complete gameplay, complete 3D engine, or metaphysical frequency claim. Next gate: browser world v48 with embodied needs during resident social schedules, household care duties, fatigue/rest negotiation, weather exposure during loans, and recoverable welfare state visible without suffering loops.

### Report 288: SSRM-3D Browser World v48 Embodied Needs/Care Duty/Fatigue Weather Welfare Bridge

Report 288 extends the browser-world line with embodied needs during resident social schedules, household care duties, fatigue/rest negotiation, weather exposure during loans, and recoverable welfare state visible without suffering loops. The deterministic run passes with readiness `0.942005`, mean channel score `0.984864`, and weakest-channel score `0.842000`. It records 216 session days, 3888 embodied need frames, 3888 social schedule need frames, 3094 household care duty frames, 2616 fatigue/rest negotiations, 3413 weather exposure loan frames, 3888 recoverable welfare frames, 3716 welfare recovery improved rows, 517 welfare reload probes, 3888 browser ticks, and 87 browser buttons.

The weakest channel is `distress_not_spectacle` at `0.842000`. That is intentional pressure: distress should open care, rest, shelter, and recovery opportunities rather than become spectacle or an unrecoverable loop. Artifacts: `experiments/ssrm_3d_browser_world_v48_embodied_needs_care_duty_fatigue_weather_welfare_bridge.py`, `artifacts/ssrm_3d_browser_world_v48_embodied_needs_care_duty_fatigue_weather_welfare_bridge_results.json`, `visualizations/ssrm_3d_browser_world_v48_embodied_needs_care_duty_fatigue_weather_welfare_bridge.html`, and `docs/288_ssrm_3d_browser_world_v48_embodied_needs_care_duty_fatigue_weather_welfare_bridge_report.md`. Boundary: deterministic browser-local embodied-need/care-duty/fatigue-rest/weather-welfare scaffold only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, complete gameplay, complete 3D engine, or metaphysical frequency claim. Next gate: browser world v49 with resident sleep/wake cycles, nutrition and shelter economies, caregiving reciprocity over weeks, weather-aware work planning, and playable avatar welfare interventions with refusal respected.

### Report 289: SSRM-3D Browser World v49 Sleep/Nutrition/Shelter Reciprocity Avatar Welfare Bridge

Report 289 extends the browser-world line with resident sleep/wake cycles, nutrition and shelter economies, caregiving reciprocity over weeks, weather-aware work planning, cultural continuity markers, and playable avatar welfare interventions with refusal respected. The deterministic run passes with readiness `0.942861`, mean channel score `0.986087`, and weakest-channel score `0.842000`. It records 252 session days, 36 weeks, 4032 sleep/wake cycle rows, 4032 nutrition/shelter economy rows, 2045 caregiving reciprocity rows, 4032 weather-aware work-plan rows, 2672 avatar welfare intervention rows, 527 avatar refusal rows, 527 avatar refusal-respected rows, 4032 cultural continuity rows, 532 reload probes, 4032 browser ticks, and 98 browser buttons.

The weakest channel is `avatar_intervention_not_coercive` at `0.842000`. That is intentional pressure: the playable avatar can help, ask first, observe, or step back, but cannot overwrite refusal or dump private workspace state. Artifacts: `experiments/ssrm_3d_browser_world_v49_sleep_nutrition_shelter_reciprocity_avatar_welfare_bridge.py`, `artifacts/ssrm_3d_browser_world_v49_sleep_nutrition_shelter_reciprocity_avatar_welfare_bridge_results.json`, `visualizations/ssrm_3d_browser_world_v49_sleep_nutrition_shelter_reciprocity_avatar_welfare_bridge.html`, and `docs/289_ssrm_3d_browser_world_v49_sleep_nutrition_shelter_reciprocity_avatar_welfare_bridge_report.md`. Boundary: deterministic browser-local sleep/nutrition/shelter/reciprocity/avatar-welfare scaffold only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, complete gameplay, complete 3D engine, or metaphysical frequency claim. Next gate: browser world v50 with thousand-year pre-avatar cultural prehistory, lineage memories, proto-language families, craft technologies, trade routes, and playable entry after civilization has already emerged.

### Report 290: SSRM-3D Browser World v50 Thousand-Year Prehistory Language Technology Trade Avatar Entry Bridge

Report 290 extends the browser-world line with a deterministic thousand-year-plus pre-avatar civilization layer: proto-language families, lineage memories, craft technology lineages, trade routes, local customs, frequency/flower timing metadata, and playable avatar entry only after civilization has already emerged. The deterministic run passes with readiness `0.944462`, mean channel score `0.988374`, and weakest-channel score `0.842000`. It records a `1200` simulated-year span, 1205 prehistory epoch rows, 1205 proto-language family rows, 1205 craft technology rows, 2155 trade route rows, 1224 lineage memory rows, 5 avatar entry rows, 305 reload probes, 1205 browser ticks, and 115 browser buttons.

The weakest channel is `entry_after_civilization_not_instant_world` at `0.842000`. That is intentional pressure: the avatar should enter late into a world with existing institutions, language-family markers, trade obligations, customs, and lineage memories, not a world invented at the moment of arrival. Artifacts: `experiments/ssrm_3d_browser_world_v50_thousand_year_prehistory_language_technology_trade_avatar_entry_bridge.py`, `artifacts/ssrm_3d_browser_world_v50_thousand_year_prehistory_language_technology_trade_avatar_entry_bridge_results.json`, `visualizations/ssrm_3d_browser_world_v50_thousand_year_prehistory_language_technology_trade_avatar_entry_bridge.html`, and `docs/290_ssrm_3d_browser_world_v50_thousand_year_prehistory_language_technology_trade_avatar_entry_bridge_report.md`. Boundary: deterministic browser-local thousand-year-prehistory/language-family/technology/trade/avatar-entry scaffold only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, complete gameplay, complete 3D engine, or metaphysical frequency claim. Next gate: browser world v51 with playable first-person arrival into the prebuilt civilization, resident greeting protocols, translation uncertainty, local law/custom constraints, and avatar choices that affect trust without erasing history.

### Report 291: SSRM-3D Browser World v51 Playable Arrival Translation Custom Trust Bridge

Report 291 extends the browser-world line with playable first-person arrival into the prebuilt civilization, resident greeting protocols, translation uncertainty, local law/custom constraints, avatar choice consequences, and history integrity checks. The deterministic run passes with readiness `0.941046`, mean channel score `0.983495`, and weakest-channel score `0.842000`. It records 144 arrival days, 2592 first-person arrival rows, 2592 greeting protocol rows, 2592 translation uncertainty rows, 2592 local custom constraint rows, 2592 avatar choice trust rows, 519 history integrity rows, 320 reload probes, 2592 browser ticks, and 122 browser buttons.

The weakest channel is `history_not_erased_by_avatar_choice` at `0.842000`. That is intentional pressure: avatar choices can change trust, curiosity, and guardedness, but inherited prehistory cannot be rewritten by interaction. Artifacts: `experiments/ssrm_3d_browser_world_v51_playable_arrival_translation_custom_trust_bridge.py`, `artifacts/ssrm_3d_browser_world_v51_playable_arrival_translation_custom_trust_bridge_results.json`, `visualizations/ssrm_3d_browser_world_v51_playable_arrival_translation_custom_trust_bridge.html`, and `docs/291_ssrm_3d_browser_world_v51_playable_arrival_translation_custom_trust_bridge_report.md`. Boundary: deterministic browser-local playable-arrival/translation/custom/trust scaffold only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, complete gameplay, complete 3D engine, or metaphysical frequency claim. Next gate: browser world v52 with bounded two-way phrasebook dialogue, gesture repair, resident-initiated questions, sensory scene controls, and memory-safe conversation continuity without LLM calls.

### Report 292: SSRM-3D Browser World v52 Phrasebook Dialogue Gesture Questions Sensory Memory Bridge

Report 292 extends the browser-world line with bounded two-way phrasebook dialogue, gesture repair, resident-initiated questions, sensory scene controls, and memory-safe conversation continuity without LLM calls. The deterministic run passes with readiness `0.940854`, mean channel score `0.983220`, and weakest-channel score `0.842000`. It records 150 dialogue days, 2700 phrasebook dialogue rows, 1575 gesture repair rows, 1500 resident-initiated question rows, 2700 sensory scene control rows, 2700 memory-safe conversation rows, 332 reload probes, 2700 browser ticks, and 141 browser buttons.

The weakest channel is `phrasebook_not_open_ended_chat` at `0.842000`. That is intentional pressure: dialogue should be readable and two-way without pretending to have unrestricted natural language or hidden LLM agency. Artifacts: `experiments/ssrm_3d_browser_world_v52_phrasebook_dialogue_gesture_questions_sensory_memory_bridge.py`, `artifacts/ssrm_3d_browser_world_v52_phrasebook_dialogue_gesture_questions_sensory_memory_bridge_results.json`, `visualizations/ssrm_3d_browser_world_v52_phrasebook_dialogue_gesture_questions_sensory_memory_bridge.html`, and `docs/292_ssrm_3d_browser_world_v52_phrasebook_dialogue_gesture_questions_sensory_memory_bridge_report.md`. Boundary: deterministic browser-local phrasebook-dialogue/gesture-repair/resident-question/sensory-control/memory-continuity scaffold only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, complete gameplay, complete 3D engine, or metaphysical frequency claim. Next gate: browser world v53 with resident-owned goals during dialogue, object/task requests, multi-turn negotiated plans, refusal-aware help offers, and bounded phrase learning that persists across reloads without LLM calls.

### Report 293: SSRM-3D Browser World v53 Resident Goals Requests Negotiated Plans Phrase Learning Bridge

Report 293 extends the browser-world line with resident-owned goals during dialogue, object/task requests, multi-turn negotiated plans, refusal-aware help offers, and bounded phrase learning that persists across reloads without LLM calls. The deterministic run passes with readiness `0.943336`, mean channel score `0.986766`, and weakest-channel score `0.842000`. It records 162 plan days, 2916 resident-owned goal rows, 2916 object/task request rows, 2201 multi-turn negotiated plan rows, 1725 refusal-aware help offer rows, 2916 bounded phrase learning rows, 356 reload probes, 2916 browser ticks, and 149 browser buttons.

The weakest channel is `resident_agency_not_avatar_puppet` at `0.842000`. That is intentional pressure: residents must keep their own goals, boundaries, counters, requests, and phrase-teaching role instead of simply executing avatar commands. Artifacts: `experiments/ssrm_3d_browser_world_v53_resident_goals_requests_negotiated_plans_phrase_learning_bridge.py`, `artifacts/ssrm_3d_browser_world_v53_resident_goals_requests_negotiated_plans_phrase_learning_bridge_results.json`, `visualizations/ssrm_3d_browser_world_v53_resident_goals_requests_negotiated_plans_phrase_learning_bridge.html`, and `docs/293_ssrm_3d_browser_world_v53_resident_goals_requests_negotiated_plans_phrase_learning_bridge_report.md`. Boundary: deterministic browser-local resident-goal/request/negotiated-plan/refusal-aware-help/phrase-learning scaffold only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, complete gameplay, complete 3D engine, or metaphysical frequency claim. Next gate: browser world v54 with schedulable resident projects, inventory-affecting task execution, tool wear, failed plan recovery, and longer-term phrase learning across multi-day relationships without LLM calls.

### Report 294: SSRM-3D Browser World v54 Schedulable Projects Inventory Toolwear Recovery Phrase Relationship Bridge

Report 294 extends the browser-world line with schedulable resident projects, inventory-affecting task execution, tool wear, failed-plan recovery, and longer-term phrase learning across multi-day relationships. The deterministic run passes with readiness `0.944092`, mean channel score `0.987846`, and weakest-channel score `0.842000`. It records 3348 schedulable project rows, 3348 inventory-affecting task rows, 3348 tool-wear rows, 1708 failed-plan recovery rows, 3348 phrase-relationship rows, 450 reload probes, 3348 browser ticks, and 255 browser buttons.

The weakest channel is `execution_not_magic_inventory` at `0.842000`. That is intentional pressure: project execution now changes inventory and tools, but it is still a deterministic trace substrate rather than a finished playable work loop. Artifacts: `experiments/ssrm_3d_browser_world_v54_schedulable_projects_inventory_toolwear_recovery_phrase_relationship_bridge.py`, `artifacts/ssrm_3d_browser_world_v54_schedulable_projects_inventory_toolwear_recovery_phrase_relationship_bridge_results.json`, `visualizations/ssrm_3d_browser_world_v54_schedulable_projects_inventory_toolwear_recovery_phrase_relationship_bridge.html`, and `docs/294_ssrm_3d_browser_world_v54_schedulable_projects_inventory_toolwear_recovery_phrase_relationship_bridge_report.md`. Boundary: Deterministic browser-local schedulable-project/inventory/tool-wear/failed-plan-recovery/phrase-relationship scaffold only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, complete gameplay, complete 3D engine, or metaphysical frequency claim. Next gate: browser world v55 with actual playable task execution loops, resident pathing to project sites, tool pickup/drop, visible inventory deltas, recoverable failed work, and relationship-aware phrase use across sessions without LLM calls.

### Report 295: SSRM-3D Browser World v55 Playable Task Loops Pathing Tool Pickup Inventory Recovery Phrase Sessions Bridge

Report 295 extends the browser-world line with actual browser-local playable task loops: resident pathing to project sites, avatar-visible tool pickup/drop, visible inventory deltas, recoverable failed work, and relationship-aware phrase use across saved sessions. The deterministic run passes with readiness `0.944700`, mean channel score `0.988714`, and weakest-channel score `0.842000`. It records 3672 playable task-loop rows, 3672 resident pathing rows, 3672 tool pickup/drop rows, 3672 visible inventory delta rows, 2550 recoverable failed-work rows, 3672 relationship phrase session rows, 490 reload probes, 3672 browser ticks, and 302 browser buttons.

The weakest channel is `task_loop_not_finished_gameplay` at `0.842000`. That is intentional pressure: localStorage-backed task buttons now mutate movement, tool, inventory, recovery, phrase, and replay state, but this is still not a finished pointer-driven 3D game. Artifacts: `experiments/ssrm_3d_browser_world_v55_playable_task_loops_pathing_tool_pickup_inventory_recovery_phrase_sessions_bridge.py`, `artifacts/ssrm_3d_browser_world_v55_playable_task_loops_pathing_tool_pickup_inventory_recovery_phrase_sessions_bridge_results.json`, `visualizations/ssrm_3d_browser_world_v55_playable_task_loops_pathing_tool_pickup_inventory_recovery_phrase_sessions_bridge.html`, and `docs/295_ssrm_3d_browser_world_v55_playable_task_loops_pathing_tool_pickup_inventory_recovery_phrase_sessions_bridge_report.md`. Boundary: Deterministic browser-local playable-task-loop/pathing/tool-pickup/inventory-delta/recoverable-failure/phrase-session scaffold only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, complete gameplay, complete 3D engine, or metaphysical frequency claim. Next gate: browser world v56 with pointer/click-driven canvas movement, animated resident pathing, actual browser-local inventory UI mutation, tool ownership disputes, multi-step crafting repair minigames, and saved-session relationship phrase consequences without LLM calls.

### Report 296: SSRM-3D Browser World v56 Canvas Movement Animated Pathing Inventory UI Tool Dispute Repair Minigame Phrase Consequence Bridge

Report 296 extends the browser-world line with pointer/click-driven canvas movement, animated resident pathing, actual browser-local inventory UI mutation, tool ownership disputes, multi-step crafting repair minigames, and saved-session relationship phrase consequences. The deterministic run passes with readiness `0.944700`, mean channel score `0.988714`, and weakest-channel score `0.842000`. It records 3996 pointer canvas movement rows, 3996 animated resident pathing rows, 3996 inventory UI mutation rows, 3996 tool ownership dispute rows, 3996 repair minigame rows, 3996 phrase consequence rows, 531 reload probes, 3996 browser ticks, and 273 browser buttons.

The weakest channel is `canvas_not_complete_3d_engine` at `0.842000`. That is intentional pressure: the page now has a clickable canvas and animated/localStorage-mutating UI, but it is still not a complete 3D engine or finished artificial-life game. Artifacts: `experiments/ssrm_3d_browser_world_v56_canvas_movement_animated_pathing_inventory_ui_tool_dispute_repair_minigame_phrase_consequence_bridge.py`, `artifacts/ssrm_3d_browser_world_v56_canvas_movement_animated_pathing_inventory_ui_tool_dispute_repair_minigame_phrase_consequence_bridge_results.json`, `visualizations/ssrm_3d_browser_world_v56_canvas_movement_animated_pathing_inventory_ui_tool_dispute_repair_minigame_phrase_consequence_bridge.html`, and `docs/296_ssrm_3d_browser_world_v56_canvas_movement_animated_pathing_inventory_ui_tool_dispute_repair_minigame_phrase_consequence_bridge_report.md`. Boundary: Deterministic browser-local canvas-movement/animated-pathing/inventory-ui/tool-dispute/repair-minigame/phrase-consequence scaffold only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, complete gameplay, complete 3D engine, or metaphysical frequency claim. Next gate: browser world v57 with live browser conversation attached to canvas agents, sensory overlays for sound/smell/temperature/wetness, gesture/body-language states, inventory/resource widgets, minigame failure animations, and replayable multi-agent consequences without LLM calls.


### Report 297: SSRM-3D Browser World v57 Live Conversation Sensory Overlay Gesture Inventory Minigame Failure Multiagent Consequence Bridge

Report 297 extends the browser-world line with canvas-bound phrasebook conversation, multimodal sensory overlays, gesture/body-language states, inventory/resource widgets, recoverable minigame failure animations, and replayable multi-agent consequences. The deterministic run passes with readiness `0.944092`, mean channel score `0.987846`, and weakest-channel score `0.842000`. It records 4320 live conversation frames, 4320 sensory overlay frames, 4320 gesture/body-language frames, 4320 inventory/resource widget frames, 4320 minigame failure animation frames, 4320 multi-agent consequence frames, 571 live session reload probes, 4320 browser ticks, and 255 browser buttons.

The weakest channel is `live_conversation_not_open_ended_llm` at `0.842000`. That is intentional pressure: the browser page can look conversational and live, but it remains deterministic phrasebook routing with no LLM call and no autonomous natural-language claim. Artifacts: `experiments/ssrm_3d_browser_world_v57_live_conversation_sensory_overlay_gesture_inventory_minigame_failure_multiagent_consequence_bridge.py`, `artifacts/ssrm_3d_browser_world_v57_live_conversation_sensory_overlay_gesture_inventory_minigame_failure_multiagent_consequence_bridge_results.json`, `visualizations/ssrm_3d_browser_world_v57_live_conversation_sensory_overlay_gesture_inventory_minigame_failure_multiagent_consequence_bridge.html`, and `docs/297_ssrm_3d_browser_world_v57_live_conversation_sensory_overlay_gesture_inventory_minigame_failure_multiagent_consequence_bridge_report.md`. Boundary: Deterministic browser-local live-conversation/sensory-overlay/gesture/inventory-widget/minigame-failure/multiagent-consequence scaffold only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, complete gameplay, complete 3D engine, or metaphysical frequency claim. Next gate: browser world v58 with typed avatar utterance routing into canvas dialogue, resident-initiated questions during movement, sensory/body-state cost overlays, inventory/minigame failure animations affecting later schedules, and replayable multi-agent relationship consequences without LLM calls.


### Report 298: SSRM-3D Browser World v58 Consolidated Playable Consequence Loop Bridge

Report 298 pivots from feature-channel accumulation toward one playable browser-world loop. It consolidates avatar action, resident schedules, memory/debt state, offscreen resident activity, visible consequence, save/restore, and replay/debug into one deterministic local world-state object. The deterministic run passes with readiness `0.940653`, mean channel score `0.981218`, and weakest-channel score `0.846000`. It records 4680 integrated loop frames, 4680 resident scheduler frames, 4680 avatar action frames, 4680 memory/debt frames, 4680 offscreen activity frames, 4680 consequence loop frames, 4680 dashboard frames, 1114 save/restore/replay frames, 4680 browser ticks, and 172 browser buttons.

The weakest channel is `consolidated_vertical_slice_not_finished_product` at `0.846000`. That is intentional pressure: the loop is more integrated and playable, but it is not a finished product or complete vertical slice yet. Artifacts: `experiments/ssrm_3d_browser_world_v58_consolidated_playable_consequence_loop_bridge.py`, `artifacts/ssrm_3d_browser_world_v58_consolidated_playable_consequence_loop_bridge_results.json`, `visualizations/ssrm_3d_browser_world_v58_consolidated_playable_consequence_loop_bridge.html`, and `docs/298_ssrm_3d_browser_world_v58_consolidated_playable_consequence_loop_bridge_report.md`. Boundary: Deterministic browser-local consolidated playable consequence-loop scaffold only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, complete gameplay, complete 3D engine, production persistence, or metaphysical frequency claim. Next gate: browser world v59 with a dedicated debug/replay/audit layer that can scrub the same playable consequence loop by tick, resident, memory, debt, schedule, and localStorage snapshot without LLM calls.


### Report 299: SSRM-3D Browser World v59 Debug Replay Audit Layer Bridge

Report 299 adds the inspectability layer needed before the first consolidated vertical slice. It attaches replay scrubbing, resident filtering, memory/debt inspection, schedule diffs, LocalStorage snapshot inspection, invariant checks, consequence causality, and audit UI panels to the same consolidated playable consequence loop introduced in Report 298/v58. The deterministic run passes with readiness `0.947631`, mean channel score `0.988615`, and weakest-channel score `0.852000`. It records 5040 replay scrub frames, 5040 resident audit index frames, 5040 memory/debt audit frames, 5040 schedule diff audit frames, 5040 LocalStorage snapshot frames, 5040 invariant audit frames, 5040 consequence causality frames, 5040 audit UI frames, 5040 browser ticks, and 208 browser buttons.

The weakest channel is `audit_layer_not_vertical_slice_product` at `0.852000`. That is intentional pressure: this is an audit layer over the integrated loop, not yet the Report 300 playable vertical slice. Artifacts: `experiments/ssrm_3d_browser_world_v59_debug_replay_audit_layer_bridge.py`, `artifacts/ssrm_3d_browser_world_v59_debug_replay_audit_layer_bridge_results.json`, `visualizations/ssrm_3d_browser_world_v59_debug_replay_audit_layer_bridge.html`, and `docs/299_ssrm_3d_browser_world_v59_debug_replay_audit_layer_bridge_report.md`. Boundary: Deterministic browser-local debug/replay/audit layer over the consolidated playable consequence loop only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, production persistence, complete gameplay, complete 3D engine, or metaphysical frequency claim. Next gate: Report 300 consolidated playable vertical slice build: one URL-style browser artifact where arrival, movement, bounded conversation, resident schedules, debts, offscreen life, memory, visible consequences, save/restore, and audit replay are usable together rather than reported as separate bridges.


### Report 300: SSRM-3D Browser World v60 Consolidated Playable Vertical Slice Build

Report 300 is the first consolidated playable vertical-slice build. It puts arrival, movement, bounded conversation, resident schedules, debts, offscreen life, memory, visible consequences, save/restore, and audit replay into one browser-local artifact instead of another isolated bridge. The deterministic run passes with readiness `0.949754`, mean channel score `0.989077`, and weakest-channel score `0.858000`. It records 5400 vertical slice session frames, 5400 playable arrival/movement frames, 5400 bounded conversation frames, 5400 schedule/debt/memory frames, 5400 offscreen return frames, 5400 visible consequence frames, 5400 save/restore/audit/replay frames, 5400 usable interface frames, 5400 browser ticks, and 180 browser buttons.

The weakest channel is `first_vertical_slice_not_outsider_ready_product` at `0.858000`. That is intentional pressure: this is the first consolidated vertical slice, not an outsider-ready product. Artifacts: `experiments/ssrm_3d_browser_world_v60_consolidated_playable_vertical_slice_build.py`, `artifacts/ssrm_3d_browser_world_v60_consolidated_playable_vertical_slice_build_results.json`, `visualizations/ssrm_3d_browser_world_v60_consolidated_playable_vertical_slice_build.html`, and `docs/300_ssrm_3d_browser_world_v60_consolidated_playable_vertical_slice_build_report.md`. Boundary: Deterministic browser-local consolidated playable vertical-slice prototype only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, production persistence, finished gameplay, complete 3D engine, or metaphysical frequency claim. Next gate: post-300 hardening: convert the single HTML vertical slice into a maintained app shell with fewer generated report files, direct browser QA, cleaner asset/state boundaries, and user-facing playtest tasks before adding new simulation organs.
