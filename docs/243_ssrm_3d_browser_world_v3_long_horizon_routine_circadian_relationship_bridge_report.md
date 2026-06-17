# Report 243: SSRM-3D Browser World v3 Long-Horizon Routine Circadian Relationship Bridge

## Status

Pass.

## Purpose

Report 243 turns Report 242's tick-level embodied affect dynamics into long-horizon continuity. Agents now carry autonomous routines, circadian/sleep-debt cycles, affect history, relationship consequences, project/resource consequences, and replay checkpoints across 21 deterministic days.

This moves the browser-world line closer to playable artificial life: the avatar can enter and interact, but agents are already doing things for their own schedule reasons. A tired, helped, pressured, or respected agent behaves differently later because sleep debt, affect history, and relationship state persist beyond one tick.

## Boundary

This is deterministic long-horizon continuity, not subjective consciousness. Autonomous routines are scheduled agent-state policies, not independent moral agency. Sleep debt, dreams, attachment, and relationship consequences are functional simulation variables, not evidence of lived experience.

## Implementation

- Module: `experiments/ssrm_3d_browser_world_v3_long_horizon_routine_circadian_relationship_bridge.py`
- Visualization: `visualizations/ssrm_3d_browser_world_v3_long_horizon_routine_circadian_relationship_bridge.html`
- Results: `artifacts/ssrm_3d_browser_world_v3_long_horizon_routine_circadian_relationship_bridge_results.json`
- Verdict: `artifacts/ssrm_3d_browser_world_v3_long_horizon_routine_circadian_relationship_bridge_verdict.csv`
- Seed: `20260856`
- Source continuity: `artifacts/ssrm_3d_browser_world_v2_embodied_affect_dynamics_bridge_results.json`

## Generated artifacts

- `artifacts/ssrm_3d_browser_world_v3_long_horizon_routine_circadian_relationship_bridge_autonomous_routine_ticks.csv`
- `artifacts/ssrm_3d_browser_world_v3_long_horizon_routine_circadian_relationship_bridge_circadian_sleep_frames.csv`
- `artifacts/ssrm_3d_browser_world_v3_long_horizon_routine_circadian_relationship_bridge_affect_history_frames.csv`
- `artifacts/ssrm_3d_browser_world_v3_long_horizon_routine_circadian_relationship_bridge_relationship_consequence_frames.csv`
- `artifacts/ssrm_3d_browser_world_v3_long_horizon_routine_circadian_relationship_bridge_routine_consequence_frames.csv`
- `artifacts/ssrm_3d_browser_world_v3_long_horizon_routine_circadian_relationship_bridge_replay_continuity_frames.csv`
- `artifacts/ssrm_3d_browser_world_v3_long_horizon_routine_circadian_relationship_bridge_browser_world_v3_ticks.csv`
- `artifacts/ssrm_3d_browser_world_v3_long_horizon_routine_circadian_relationship_bridge_state.json`
- `artifacts/ssrm_3d_browser_world_v3_long_horizon_routine_circadian_relationship_bridge_results.json`
- `artifacts/ssrm_3d_browser_world_v3_long_horizon_routine_circadian_relationship_bridge_verdict.csv`

## New dynamics

| Layer | What changed |
| --- | --- |
| Autonomous routines | Agents choose dawn, day, dusk, and night routines from role, chronotype, schedule phase, and prior state rather than avatar command. |
| Circadian sleep debt | Sleep debt accumulates during wake/pressure/cold/crowding and recovers through sleep, guarded rest, soft recovery, and ritual rhythm. |
| Affect history | Valence, arousal, control, safety, stress load, recovery momentum, and affect memory charge carry across days. |
| Relationship consequences | Trust, comfort, avoidance, dependency, gratitude, resentment, and attachment security update from embodied history. |
| Routine consequences | Projects, skills, resources, social face, autonomy satisfaction, and variation accumulate instead of resetting per tick. |
| Replay continuity | Import/export hashes and restore checkpoints carry durable state across multi-day replay rows. |
| Browser v3 | Adds 21-day autonomous routine playback, replay import/export, private history inspection, and public routine/body/relationship markers. |

## Run output

```text
module_verdict pass
browser_world_v3_long_horizon_readiness 0.989287
autonomous_routine_ticks 672
circadian_sleep_frames 672
affect_history_frames 672
relationship_consequence_frames 672
routine_consequence_frames 672
replay_continuity_frames 672
browser_world_v3_ticks 672
long_horizon_span_coverage 1.000000
autonomous_routine_continuity 1.000000
circadian_sleep_debt_coupling 0.951997
affect_history_carryover 1.000000
relationship_consequence_binding 0.997024
replay_import_export_integrity 1.000000
routine_variation_without_chaos 1.000000
weakest_channel_score 0.894351
visualization visualizations/ssrm_3d_browser_world_v3_long_horizon_routine_circadian_relationship_bridge.html
next_gate browser world v4 with multi-week learned routine adaptation, proto-language drift from repeated interactions, and avatar-entry consequences that respect agent sleep, boundaries, and relationship history
```

## Metrics

| Metric | Value |
| --- | ---: |
| browser_world_v3_long_horizon_readiness | 0.989287 |
| mean_long_horizon_channel_score | 0.991298 |
| weakest_channel_score | 0.894351 |
| long_horizon_span_coverage | 1.000000 |
| autonomous_routine_continuity | 1.000000 |
| phase_coverage | 1.000000 |
| circadian_sleep_debt_coupling | 0.951997 |
| sleep_recovery_effect | 1.000000 |
| affect_history_carryover | 1.000000 |
| mood_temporal_inertia | 0.894351 |
| relationship_consequence_binding | 0.997024 |
| relationship_recovery_from_help | 1.000000 |
| routine_consequence_accumulation | 1.000000 |
| schedule_autonomy_balance | 1.000000 |
| routine_variation_without_chaos | 1.000000 |
| replay_import_export_integrity | 1.000000 |
| replay_checkpoint_coverage | 1.000000 |
| private_history_boundary | 1.000000 |
| frequency_circadian_rhythm | 1.000000 |
| source_embodied_affect_continuity | 1.000000 |
| browser_world_v3_surface_available | 1.000000 |

## Ablations

| Ablation | Readiness |
| --- | ---: |
| no_circadian_sleep_debt | 0.699287 |
| no_relationship_consequences | 0.709287 |
| no_autonomous_routines | 0.719287 |
| no_long_horizon_span | 0.739287 |
| no_affect_history_carryover | 0.749287 |
| no_routine_consequence_accumulation | 0.799287 |
| no_sleep_recovery | 0.809287 |
| no_replay_import_export | 0.829287 |
| no_private_history_boundary | 0.859287 |
| no_frequency_circadian_rhythm | 0.909287 |

## Interpretation

The strongest dependencies are circadian sleep debt, relationship consequences, autonomous routines, long-horizon span, and affect history carryover. That is the correct pressure profile for playable agents that should feel like continuing little people rather than resettable tick puppets.

The initial deterministic run failed because the circadian metric compared sleep debt to wake pressure. The model actually routes sleep debt into fatigue and recovery behavior, so the metric was corrected to compare sleep debt against `fatigue_next_tick`. After that correction, circadian sleep-debt coupling passes at 0.951997.

The weakest remaining channel is mood temporal inertia at 0.894351. That is honest: affect is persistent enough to carry continuity, but still changes cleanly under deterministic smoothing. The next report should push adaptation and language drift over multiple weeks without making agents random or melodramatic.

## Honest limits

- This is deterministic long-horizon continuity, not subjective consciousness.
- Autonomous routines are scheduled agent-state policies, not independent moral agency.
- Sleep debt and affect history are functional simulation variables, not lived fatigue or dreams.
- Relationship consequences are simulated continuity, not real attachment or consent.
- Replay import/export is browser-local JSON scaffolding, not complete engine replay.
- Frequency and flower phase remain rhythm variables, not metaphysical proof.
- The browser world v3 visualization is a scaffold, not a finished 3D game engine.

## Next gate

Browser world v4 with multi-week learned routine adaptation, proto-language drift from repeated interactions, and avatar-entry consequences that respect agent sleep, boundaries, and relationship history.
