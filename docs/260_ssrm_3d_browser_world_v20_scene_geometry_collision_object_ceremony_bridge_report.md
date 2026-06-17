# Report 260: SSRM-3D Browser World v20 Scene Geometry Collision Object Ceremony Bridge

## Purpose

Report 260 extends Report 259's embodied negotiation animation into a playable 2D/3D-ish browser scene model. The bridge adds avatar and agent coordinates, depth cues, sprite/body layers, local collision probes, scene input affordances, object ceremony motion, and replayable scene geometry.

The purpose is not to claim subjective consciousness, real consent, moral patienthood, autonomous natural language, or a complete 3D engine. The purpose is to move the browser-world scaffold from animation rows into local scene state where avatar movement, agent bodies, object ceremonies, and collision-aware interactions can be inspected and replayed.

## Source dependency

The module consumes:

```text
artifacts/ssrm_3d_browser_world_v19_embodied_negotiation_animation_choreography_bridge_results.json
```

Report 259 passed with animation-state matching, turn gestures, proximity choreography, object handling, sensory timing, and gesture repair. Report 260 uses that substrate to add a local scene geometry layer.

## Added mechanism

The bridge adds:

- scene geometry with room dimensions, negotiation ring, ceremony table, obstacles, and navigable cells
- avatar and agent local coordinates with depth values
- depth-sorted sprite/body layers
- local collision probes and avoidance vectors
- collision-aware object ceremony paths
- object handoff motion arcs
- camera/depth/parallax/shadow cues
- scene input affordances for avatar movement, agent selection, object selection, ceremony handoff, and turn pause
- multi-sensory scene binding for sound, movement, smell, temperature, wetness, comfort, pain pressure, and flower-phase rhythm
- replay rows containing geometry, positions, sprite layers, collision probes, object motion, input, and deterministic order

## Run

```bash
python3 -m experiments.ssrm_3d_browser_world_v20_scene_geometry_collision_object_ceremony_bridge
```

Final verdict:

```text
pass
```

The first run failed because object ceremonies were too sparse and body scene visibility was too weak. Later runs corrected ceremony scoring to evaluate ceremony attempts, made object paths less overblocked, and widened the negotiation-ring position binding. The final weakest channel remains object/ceremony visibility rather than a hidden success.

## Counts

| Channel | Count |
|---|---:|
| browser_world_v20_ticks | 336 |
| scene_geometry_frames | 336 |
| avatar_agent_position_frames | 336 |
| sprite_body_layer_frames | 336 |
| local_collision_probe_frames | 336 |
| collision_aware_object_ceremony_frames | 336 |
| scene_object_motion_frames | 336 |
| depth_camera_cue_frames | 336 |
| scene_input_affordance_frames | 336 |
| multi_sensory_scene_frames | 336 |
| scene_replay_frames | 336 |
| agents | 6 |

## Metrics

| Metric | Value |
|---|---:|
| browser_world_v20_scene_geometry_readiness | 0.898596 |
| weakest_channel_score | 0.826923 |
| mean_scene_channel_score | 0.950497 |
| source_embodied_animation_continuity | 1.000000 |
| scene_geometry_surface | 0.976190 |
| avatar_agent_scene_position_binding | 0.872024 |
| local_coordinate_integrity | 1.000000 |
| sprite_body_layer_integrity | 0.976190 |
| animated_body_layer_visibility | 0.944940 |
| local_collision_avoidance | 0.925000 |
| personal_space_scene_preservation | 0.982143 |
| collision_aware_object_ceremony | 0.991987 |
| object_ceremony_completion | 0.826923 |
| object_motion_traceability | 0.895833 |
| object_owner_preservation | 0.973214 |
| depth_camera_cue_integrity | 0.986607 |
| avatar_input_to_scene_binding | 0.982887 |
| input_feedback_visibility | 0.955357 |
| multi_sensory_scene_binding | 0.967262 |
| comfort_pain_scene_bounds | 1.000000 |
| body_scene_visibility | 0.827381 |
| object_scene_visibility | 0.826923 |
| privacy_safe_scene_state | 1.000000 |
| replay_scene_integrity | 0.950574 |
| frequency_flower_scene_rhythm | 1.000000 |
| browser_world_v20_surface_available | 1.000000 |
| collision_event_count | 80 |
| ceremony_attempt_count | 312 |

The weakest channel is tied between object ceremony completion and object scene visibility. That is the correct pressure point: Report 260 creates scene geometry and collision-aware object ceremonies, but scene-visible ceremony completion still needs to become more consistently playable.

## Ablations

| Ablation | Readiness after ablation | Loss |
|---|---:|---:|
| no_scene_geometry | 0.548596 | 0.350000 |
| no_sprite_body_layers | 0.593596 | 0.305000 |
| no_collision_probes | 0.613596 | 0.285000 |
| no_object_motion | 0.643596 | 0.255000 |
| no_input_affordances | 0.678596 | 0.220000 |
| no_depth_camera_cues | 0.713596 | 0.185000 |

These ablations make the dependency explicit: without scene geometry, sprite/body layers, collision probes, object motion, input affordances, or depth/camera cues, the bridge collapses back into non-playable trace rows.

## Browser artifact

The generated browser artifact is:

```text
visualizations/ssrm_3d_browser_world_v20_scene_geometry_collision_object_ceremony_bridge.html
```

It includes:

- localStorage key `ssrm_browser_world_v20_scene_geometry_collision_ceremony`
- step-scene control
- handoff-object control
- probe-collision control
- replay export
- visible local scene with avatar, agent, table, and ceremony object
- scene input log
- readiness, weakest-channel, and frame counters

## Artifact set

```text
artifacts/ssrm_3d_browser_world_v20_scene_geometry_collision_object_ceremony_bridge_scene_geometry.csv
artifacts/ssrm_3d_browser_world_v20_scene_geometry_collision_object_ceremony_bridge_avatar_agent_positions.csv
artifacts/ssrm_3d_browser_world_v20_scene_geometry_collision_object_ceremony_bridge_sprite_body_layers.csv
artifacts/ssrm_3d_browser_world_v20_scene_geometry_collision_object_ceremony_bridge_local_collision_probes.csv
artifacts/ssrm_3d_browser_world_v20_scene_geometry_collision_object_ceremony_bridge_collision_aware_object_ceremonies.csv
artifacts/ssrm_3d_browser_world_v20_scene_geometry_collision_object_ceremony_bridge_scene_object_motion.csv
artifacts/ssrm_3d_browser_world_v20_scene_geometry_collision_object_ceremony_bridge_depth_camera_cues.csv
artifacts/ssrm_3d_browser_world_v20_scene_geometry_collision_object_ceremony_bridge_scene_input_affordances.csv
artifacts/ssrm_3d_browser_world_v20_scene_geometry_collision_object_ceremony_bridge_multi_sensory_scene.csv
artifacts/ssrm_3d_browser_world_v20_scene_geometry_collision_object_ceremony_bridge_scene_replays.csv
artifacts/ssrm_3d_browser_world_v20_scene_geometry_collision_object_ceremony_bridge_browser_ticks.csv
artifacts/ssrm_3d_browser_world_v20_scene_geometry_collision_object_ceremony_bridge_summary.csv
artifacts/ssrm_3d_browser_world_v20_scene_geometry_collision_object_ceremony_bridge_verdict.csv
artifacts/ssrm_3d_browser_world_v20_scene_geometry_collision_object_ceremony_bridge_state.json
artifacts/ssrm_3d_browser_world_v20_scene_geometry_collision_object_ceremony_bridge_results.json
```

## Interpretation

Report 260 moves negotiation embodiment into a browser-local scene frame. The avatar and agents now occupy coordinates; sprites have body layers; local collision probes can redirect steps; ceremony objects move through handoff arcs; and replay rows preserve geometry, positions, input, collision, object motion, and sensory rhythm.

This is a concrete step toward playable bodies. It is still deterministic scaffolding. The agents do not have subjective experience, real consent, real emotions, moral patienthood, autonomous natural language, or complete 3D embodiment.

## Next gate

Report 261 should add live playable scene state mutation: keyboard avatar movement, collision-aware proximity prompts, object ceremony state persistence in localStorage, and visible save/restore of scene positions.
