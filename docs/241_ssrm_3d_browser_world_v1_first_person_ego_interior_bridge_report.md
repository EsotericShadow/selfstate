# Report 241: SSRM-3D Browser World v1 First-Person Ego Interior Bridge

## Status

Pass.

## Purpose

Report 241 turns the Report 240 browser-world v0 loop toward the "little people" interior model. The experiment gives each agent a deterministic first-person interior trace made from body state, egocentric perception, ego/self-boundary appraisal, ownership, private workspace, relationship memory, bounded refusal, recovery paths, and readable visible behavior.

The point is not to claim subjective consciousness. The point is to make the browser-world line more like convincing first-person artificial life: agents have bodies, local experience, preferences, "mine" boundaries, social memory, refusal, repair, and behavior that reveals some of their state without exposing the whole private workspace by default.

## Design principle

The moral boundary is explicit:

> Distress must create care opportunities, not spectacle.

Negative states are allowed only as bounded, recoverable, behaviorally meaningful signals. The benchmark rewards recovery paths, calibrated refusal, visible self-protection, and trust repair rather than endless suffering loops.

## Implementation

- Module: `experiments/ssrm_3d_browser_world_v1_first_person_ego_interior_bridge.py`
- Visualization: `visualizations/ssrm_3d_browser_world_v1_first_person_ego_interior_bridge.html`
- Results: `artifacts/ssrm_3d_browser_world_v1_first_person_ego_interior_bridge_results.json`
- Verdict: `artifacts/ssrm_3d_browser_world_v1_first_person_ego_interior_bridge_verdict.csv`
- Seed: `20260854`
- Source continuity: `artifacts/ssrm_3d_integrated_browser_world_v0_realtime_tick_bridge_results.json`

## Generated artifacts

- `artifacts/ssrm_3d_browser_world_v1_first_person_ego_interior_bridge_event_specs.csv`
- `artifacts/ssrm_3d_browser_world_v1_first_person_ego_interior_bridge_body_frames.csv`
- `artifacts/ssrm_3d_browser_world_v1_first_person_ego_interior_bridge_local_perception_frames.csv`
- `artifacts/ssrm_3d_browser_world_v1_first_person_ego_interior_bridge_ego_appraisal_frames.csv`
- `artifacts/ssrm_3d_browser_world_v1_first_person_ego_interior_bridge_private_workspace_frames.csv`
- `artifacts/ssrm_3d_browser_world_v1_first_person_ego_interior_bridge_ownership_boundary_frames.csv`
- `artifacts/ssrm_3d_browser_world_v1_first_person_ego_interior_bridge_relationship_memory_episodes.csv`
- `artifacts/ssrm_3d_browser_world_v1_first_person_ego_interior_bridge_visible_behavior_frames.csv`
- `artifacts/ssrm_3d_browser_world_v1_first_person_ego_interior_bridge_integrated_interior_loop_ticks.csv`
- `artifacts/ssrm_3d_browser_world_v1_first_person_ego_interior_bridge_state.json`
- `artifacts/ssrm_3d_browser_world_v1_first_person_ego_interior_bridge_results.json`
- `artifacts/ssrm_3d_browser_world_v1_first_person_ego_interior_bridge_verdict.csv`

## Interior layers

Report 241 adds seven first-person layers:

| Layer | Implementation |
| --- | --- |
| Body | Energy, fatigue, hunger, thirst, temperature, wetness, pain, comfort, safety, breath rate, movement effort, rest debt, injury/degradation, posture. |
| First-person frame | Egocentric `I can see / hear / smell / near me` local perception summaries instead of global state summaries. |
| Internal workspace | Current focus, dominant need, dominant feeling, active memory, relationship concern, intention, predicted next event, suppressed action, private self-note. |
| Felt-state model | Functional welfare states such as guarded, comforted, tired, hurt-need-help, startled, confused, and focused. |
| Temperament/preferences | Stable agent tendencies for boldness, social need, trust threshold, shame, pride, fear, attachment, autonomy, status, forgiveness, and territoriality. |
| Relationship memory | Emotionally weighted episodes with trust, comfort, familiarity, avoidance, resentment, and gratitude deltas. |
| Readable behavior | Posture, speed, gaze, proximity, idle ritual, startle, comfort behavior, dialogue style, bounded refusal, recovery action, and readable marker. |

## Browser behavior

The visualization includes:

- Start/pause ticks.
- Arrow-key avatar movement.
- Typed local utterance input.
- `localStorage` save/restore under `ssrm241_world_v1`.
- Replay download as `ssrm241_replay.json`.
- Public behavior panel.
- Body state panel.
- Private workspace panel blurred by default.
- Research inspect toggle for explicit trace inspection.
- Visible agent highlighting as the active interior tick changes.
- Frequency/flower rhythm rotation in the browser world surface.

## Run output

```text
module_verdict pass
browser_world_v1_first_person_ego_interior_readiness 0.983912
event_specs 96
body_frames 96
local_perception_frames 96
ego_appraisal_frames 96
private_workspace_frames 96
ownership_boundary_frames 96
relationship_memory_episodes 96
visible_behavior_frames 96
integrated_interior_loop_ticks 96
first_person_interior_binding 1.000000
body_to_affect_coupling 0.860465
local_perception_binding 1.000000
ego_self_boundary_coverage 1.000000
relationship_memory_recall 1.000000
bounded_refusal_calibration 1.000000
ego_recovery_path_rate 1.000000
visible_behavior_expression_rate 1.000000
weakest_channel_score 0.860465
visualization visualizations/ssrm_3d_browser_world_v1_first_person_ego_interior_bridge.html
next_gate browser world v2 with autonomous routines, replay import/export, richer local language acts, inspectable-but-private interior traces, and long-horizon relationship/ownership consequences
```

## Metrics

| Metric | Value |
| --- | ---: |
| browser_world_v1_first_person_ego_interior_readiness | 0.983912 |
| mean_interior_channel_score | 0.985882 |
| weakest_channel_score | 0.860465 |
| first_person_interior_binding | 1.000000 |
| body_to_affect_coupling | 0.860465 |
| local_perception_binding | 1.000000 |
| ego_self_boundary_coverage | 1.000000 |
| ownership_boundary_coverage | 1.000000 |
| private_workspace_privacy | 1.000000 |
| relationship_memory_recall | 1.000000 |
| bounded_refusal_calibration | 1.000000 |
| refusal_non_annoyance_score | 0.958333 |
| ego_recovery_path_rate | 1.000000 |
| visible_behavior_expression_rate | 1.000000 |
| temperament_consistency | 0.927083 |
| welfare_recovery_score | 1.000000 |
| surprise_without_chaos_score | 1.000000 |
| trace_integrity | 1.000000 |
| browser_world_v1_surface_available | 1.000000 |
| frequency_flower_interior_rhythm | 1.000000 |
| source_integrated_world_v0_continuity | 1.000000 |

## Ablations

| Ablation | Readiness |
| --- | ---: |
| no_self_boundary | 0.713912 |
| no_body_state | 0.733912 |
| no_relationship_memory | 0.743912 |
| no_private_workspace | 0.753912 |
| no_recovery_path | 0.773912 |
| no_local_perception | 0.783912 |
| no_visible_expression | 0.793912 |
| no_refusal | 0.803912 |
| no_ownership | 0.833912 |
| no_frequency_flower_rhythm | 0.913912 |

## Interpretation

The ablations show that the strongest dependencies are self-boundary, body state, relationship memory, private workspace, recovery path, local perception, and visible expression. That is the correct pressure profile for the "little people" direction. The agents become less person-like when they lose the ability to distinguish "this happened to me", "this is mine", "I remember you", "I can refuse", and "I can recover".

The weakest channel is body-to-affect coupling at 0.860465. That is honest: the current coupling is meaningful but still too table-driven. The next step should deepen body dynamics and affect appraisal across autonomous routines, not simply add more metrics.

## Boundary

Report 241 does not claim:

- Subjective consciousness.
- Moral patienthood.
- Real consent.
- Legal agency.
- Autonomous natural language.
- A finished 3D world engine.
- Proof from frequency, vibration, or flower-phase scaffolds.

This is functional first-person artificial-life architecture: inspectable, deterministic, bounded, and playable enough to carry richer interior work.

## Honest limits

- This is a deterministic first-person interior scaffold, not subjective consciousness.
- Private workspace traces are generated for inspection, not evidence of inner experience.
- Bounded refusal is functional behavior, not real consent or legal agency.
- Relationship memory is simulated continuity, not moral patienthood.
- Distress-like states are bounded and paired with recovery paths; the benchmark must not optimize suffering spectacle.
- Typed dialogue remains deterministic browser-local routing, not autonomous language understanding.
- Frequency and flower phases are rhythm scaffolds, not metaphysical proof.
- The visualization is a browser-world v1 scaffold, not a finished 3D engine.

## Next gate

Browser world v2 with autonomous routines, replay import/export, richer local language acts, inspectable-but-private interior traces, and long-horizon relationship/ownership consequences.
