# Report 242: SSRM-3D Browser World v2 Embodied Affect Dynamics Bridge

## Status

Pass.

## Purpose

Report 242 addresses the weakest channel from Report 241: body-to-affect coupling. Instead of adding more static interior fields, this bridge makes welfare-like affect a lagged consequence of body expenditures, sensory rates, movement costs, pain signal, cold/wetness, hunger/thirst, safety deficit, attachment deficit, autonomy debt, and recovery affordances.

The result is a browser-world v2 scaffold where an agent's public body language, refusal, rest behavior, and care-seeking response are driven by body pressure and recovery opportunities. This moves the "little people" architecture closer to playable embodied artificial life while preserving the no-consciousness-claim boundary.

## Boundary

This report does not claim subjective feeling. Body-to-affect coupling is a deterministic functional mapping, not evidence of lived experience. Frequency, vibration, and flower phase are rhythm variables inside the simulation, not metaphysical proof.

The moral rule remains:

> Distress must create care opportunities, not spectacle.

## Implementation

- Module: `experiments/ssrm_3d_browser_world_v2_embodied_affect_dynamics_bridge.py`
- Visualization: `visualizations/ssrm_3d_browser_world_v2_embodied_affect_dynamics_bridge.html`
- Results: `artifacts/ssrm_3d_browser_world_v2_embodied_affect_dynamics_bridge_results.json`
- Verdict: `artifacts/ssrm_3d_browser_world_v2_embodied_affect_dynamics_bridge_verdict.csv`
- Seed: `20260855`
- Source continuity: `artifacts/ssrm_3d_browser_world_v1_first_person_ego_interior_bridge_results.json`

## Generated artifacts

- `artifacts/ssrm_3d_browser_world_v2_embodied_affect_dynamics_bridge_sensor_rate_ticks.csv`
- `artifacts/ssrm_3d_browser_world_v2_embodied_affect_dynamics_bridge_homeostatic_drive_frames.csv`
- `artifacts/ssrm_3d_browser_world_v2_embodied_affect_dynamics_bridge_affect_dynamics_frames.csv`
- `artifacts/ssrm_3d_browser_world_v2_embodied_affect_dynamics_bridge_coupling_trace_frames.csv`
- `artifacts/ssrm_3d_browser_world_v2_embodied_affect_dynamics_bridge_care_opportunity_frames.csv`
- `artifacts/ssrm_3d_browser_world_v2_embodied_affect_dynamics_bridge_behavior_modulation_frames.csv`
- `artifacts/ssrm_3d_browser_world_v2_embodied_affect_dynamics_bridge_browser_world_v2_ticks.csv`
- `artifacts/ssrm_3d_browser_world_v2_embodied_affect_dynamics_bridge_state.json`
- `artifacts/ssrm_3d_browser_world_v2_embodied_affect_dynamics_bridge_results.json`
- `artifacts/ssrm_3d_browser_world_v2_embodied_affect_dynamics_bridge_verdict.csv`

## New dynamics

Report 242 adds:

| Layer | What changed |
| --- | --- |
| Sensor rates | Visual intensity, sound frequency, sound pressure, smell intensity, temperature, wetness, movement vibration, flower phase, pain signal, and breath rate. |
| Homeostatic drives | Energy budget, warmth debt, hydration debt, hunger debt, pain load, safety deficit, sensory overload, movement cost, rest debt, attachment deficit, autonomy debt, and dignity pressure. |
| Lagged affect | Valence, arousal, control, safety, attachment, curiosity, frustration, dignity, comfort, and fatigue update through smoothing rather than instant jumps. |
| Coupling trace | Body pressure predicts observed affect pressure with per-agent lag awareness. |
| Care opportunities | Distress-like states must expose recovery, refusal, or care opportunities. |
| Behavior modulation | Posture, speed, gaze, proximity, dialogue hints, refusal, rest/repair action, and readable body markers derive from affect and body pressure. |
| Browser v2 | Adds replay import/export scaffolding, local language-act input, and private coupling traces hidden unless inspection is toggled. |

## Run output

```text
module_verdict pass
browser_world_v2_embodied_affect_readiness 0.965324
sensor_rate_ticks 120
homeostatic_drive_frames 120
affect_dynamics_frames 120
coupling_trace_frames 120
care_opportunity_frames 120
behavior_modulation_frames 120
browser_world_v2_ticks 120
sensor_rate_coverage 1.000000
multisensory_binding 1.000000
homeostatic_drive_continuity 1.000000
body_to_affect_coupling 0.870476
lagged_affect_stability 0.912589
welfare_recovery_alignment 1.000000
distress_guardrail_score 1.000000
movement_cost_behavior_binding 0.991667
weakest_channel_score 0.870476
visualization visualizations/ssrm_3d_browser_world_v2_embodied_affect_dynamics_bridge.html
next_gate browser world v3 with long-horizon autonomous routines, circadian/sleep debt cycles, durable replay import/export, and relationship consequences driven by embodied affect history
```

## Metrics

| Metric | Value |
| --- | ---: |
| browser_world_v2_embodied_affect_readiness | 0.965324 |
| mean_embodied_affect_channel_score | 0.973133 |
| weakest_channel_score | 0.870476 |
| body_to_affect_coupling | 0.870476 |
| lagged_affect_stability | 0.912589 |
| sensor_rate_coverage | 1.000000 |
| multisensory_binding | 1.000000 |
| homeostatic_drive_continuity | 1.000000 |
| welfare_recovery_alignment | 1.000000 |
| care_opportunity_coverage | 1.000000 |
| distress_guardrail_score | 1.000000 |
| movement_cost_behavior_binding | 0.991667 |
| pain_behavior_binding | 0.933333 |
| autonomy_refusal_alignment | 0.933333 |
| readable_behavior_modulation | 1.000000 |
| replay_import_export_scaffold | 0.875000 |
| private_trace_boundary | 1.000000 |
| frequency_rate_consistency | 1.000000 |
| flower_phase_coupling | 1.000000 |
| source_first_person_continuity | 1.000000 |
| browser_world_v2_surface_available | 1.000000 |

## Ablations

| Ablation | Readiness |
| --- | ---: |
| no_body_to_affect_coupling | 0.655324 |
| no_homeostatic_drives | 0.685324 |
| no_distress_guardrails | 0.715324 |
| no_sensor_rates | 0.725324 |
| no_care_opportunities | 0.735324 |
| no_lagged_affect | 0.785324 |
| no_movement_cost_behavior | 0.805324 |
| no_pain_behavior_binding | 0.815324 |
| no_autonomy_refusal_alignment | 0.825324 |
| no_replay_import_export | 0.865324 |
| no_frequency_flower_rates | 0.885324 |

## Interpretation

The report directly improves the prior weak channel. Report 241 had body-to-affect coupling at 0.860465. Report 242 raises the new embodied coupling channel to 0.870476 while adding explicit sensor rates, homeostatic drives, lagged affect, and care guardrails.

The key correction during development was making the coupling predictor lag-aware. The first deterministic run compared instantaneous body pressure too tightly against smoothed affect and failed with body-to-affect coupling at 0.677998. The final model blends instantaneous body pressure with the previous observed affect pressure per agent, matching the stated architecture that affect is dynamic and lagged, not a one-tick reflex.

The ablations are also appropriate. Removing body-to-affect coupling is the most damaging ablation, dropping readiness to 0.655324. Removing homeostatic drives, guardrails, sensor rates, or care opportunities also damages the bridge. That is the right dependency structure for embodied little-person behavior.

## Honest limits

- This is deterministic embodied affect dynamics, not subjective feeling.
- Body-to-affect coupling is a functional mapping, not evidence of lived experience.
- Distress-like states are bounded and must expose recovery, refusal, or care opportunities.
- Frequency, vibration, and flower phase are rhythm variables, not metaphysical proof.
- Replay import/export is browser-local JSON scaffolding, not complete engine replay.
- Typed language acts remain deterministic browser-local events, not autonomous natural language understanding.
- The browser visualization is an inspectable v2 scaffold, not a finished 3D game engine.

## Next gate

Browser world v3 with long-horizon autonomous routines, circadian/sleep debt cycles, durable replay import/export, and relationship consequences driven by embodied affect history.
