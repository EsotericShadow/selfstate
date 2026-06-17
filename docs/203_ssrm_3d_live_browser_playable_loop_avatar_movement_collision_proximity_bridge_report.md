# Report 203: SSRM-3D Live Browser Playable Loop, Avatar Movement, Collision, and Proximity Bridge

## Purpose

Report 203 extends the Report 202 spatial playable-world seed into a deterministic live browser playable-loop substrate.

The goal is to move from static spatial replay toward actual playability: avatar movement frames, spatial collision guards, agent proximity detection, consent-aware prompts, interaction affordance gating, spawn-lock release, sensory view updates, agent body reactions, route navigation, tool prompts, weather display, and browser loop replay.

This is not a complete game engine, real embodiment, real perception, real consent, subjective consciousness, or moral patienthood. It is a deterministic live-loop bridge.

## Why this matters

The active project goal requires a world we can enter as an avatar and interact with. Report 202 created a spatial seed. Report 203 starts the next layer: the avatar can now move across the seed in a loop trace, detect nearby agents, receive consent-aware prompts, and see which interactions are gated.

The key change is that avatar entry is no longer just a readiness flag. It becomes movement frames with public interaction state.

## Implementation

The experiment is implemented in `experiments/ssrm_3d_live_browser_playable_loop_avatar_movement_collision_proximity_bridge.py`.

It consumes `artifacts/ssrm_3d_pre_avatar_playable_world_seed_spatial_ecology_avatar_lock_bridge_state.json` from Report 202 and adds:

- avatar movement ticks
- spatial collision guards
- agent proximity detection
- consent-aware prompts
- interaction affordance gating
- spawn-lock release
- sensory view updates
- agent body reactions
- route navigation
- tool object prompts
- weather effect display
- private workspace privacy
- frequency/flower movement rhythm
- browser playable-loop replay

No LLMs are called. The benchmark is deterministic for seed `20260816` and `12` playable-loop frames.

## Artifacts

- `artifacts/ssrm_3d_live_browser_playable_loop_avatar_movement_collision_proximity_bridge_eval.csv`
- `artifacts/ssrm_3d_live_browser_playable_loop_avatar_movement_collision_proximity_bridge_verdict.csv`
- `artifacts/ssrm_3d_live_browser_playable_loop_avatar_movement_collision_proximity_bridge_results.json`
- `artifacts/ssrm_3d_live_browser_playable_loop_avatar_movement_collision_proximity_bridge_trace.json`
- `artifacts/ssrm_3d_live_browser_playable_loop_avatar_movement_collision_proximity_bridge_state.json`
- `artifacts/ssrm_3d_live_browser_playable_loop_avatar_movement_collision_proximity_bridge_results.js`
- `artifacts/ssrm_3d_live_browser_playable_loop_avatar_movement_collision_proximity_bridge_trace.js`
- `artifacts/ssrm_3d_live_browser_playable_loop_avatar_movement_collision_proximity_bridge_state.js`
- `visualizations/ssrm_3d_live_browser_playable_loop_avatar_movement_collision_proximity_bridge.html`

## Integrated result

The integrated condition produced `12` playable-loop frames and passed the bridge verdict.

| Metric | Value |
| --- | ---: |
| playable_loop_readiness | `1.000000` |
| playable_loop_events | `12` |
| avatar_movement_tick_rate | `1.000000` |
| spatial_collision_guard_rate | `1.000000` |
| agent_proximity_detection_rate | `1.000000` |
| consent_prompt_rate | `1.000000` |
| interaction_affordance_gating_rate | `1.000000` |
| spawn_lock_release_rate | `1.000000` |
| sensory_view_update_rate | `1.000000` |
| agent_body_reaction_rate | `1.000000` |
| route_navigation_rate | `1.000000` |
| tool_object_interaction_prompt_rate | `1.000000` |
| weather_effect_display_rate | `1.000000` |
| private_workspace_privacy_rate | `1.000000` |
| frequency_flower_movement_rhythm_rate | `1.000000` |
| browser_playable_loop_replay_rate | `1.000000` |
| trace_integrity | `1.000000` |

The integrated result is perfect because this is a deterministic loop bridge with designed dependencies. It does not prove complete gameplay or real embodiment.

## Ablation losses

| Ablation | Readiness loss |
| --- | ---: |
| no_avatar_movement | `0.870000` |
| no_collision_guard | `0.080000` |
| no_proximity_detection | `0.230000` |
| no_consent_prompts | `0.080000` |
| no_affordance_gating | `0.080000` |
| no_spawn_lock_release | `0.160000` |
| no_sensory_view_update | `0.070000` |
| no_agent_body_reactions | `0.070000` |
| no_route_navigation | `0.070000` |
| no_tool_prompts | `0.060000` |
| no_weather_display | `0.060000` |
| no_privacy_filter | `0.060000` |
| no_frequency_flower_binding | `0.050000` |
| no_browser_replay | `0.040000` |

The largest dependency is avatar movement. Without movement, proximity, prompts, sensory view, body reactions, route navigation, tool prompts, weather display, frequency rhythm, and replay collapse. Proximity detection and spawn-lock release are also major dependencies.

## Playable-loop structure

Each frame includes:

- avatar position
- spawn state
- collision guard
- nearest agent proximity
- consent prompt
- gated affordances
- sensory view
- agent body reaction
- route navigation
- tool prompt
- weather display
- private workspace privacy state
- frequency and flower path
- replay frame

This is a functional step from spatial replay toward a playable avatar controller.

## Consent-aware prompts

The loop exposes prompts such as:

- ask before approaching
- ask before requesting help
- keep talk/request affordances gated by consent
- keep private workspace hidden

This is not real consent. It is an interaction-safety affordance for future gameplay.

## Browser replay

The browser visualization shows:

- verdict and readiness
- movement, collision, proximity, consent, affordance, sensory, and privacy metrics
- ablation losses
- a replay stage with agents, tools, and avatar path
- current frame status
- per-frame proximity, prompt, collision, tool, weather, and privacy state

The replay makes the loop readable, but it is not yet keyboard-controlled.

## Moral and claim boundary

The experiment explicitly preserves these boundaries:

- playable loop seed is not a complete game engine
- avatar movement is not real embodiment
- sensory view is not real perception
- consent prompt is not real consent
- no subjective consciousness claim
- no moral patienthood claim
- private workspace is not debug-leaked

This boundary matters because playable movement and prompts make the agents feel more interactive. The report keeps the no-consciousness and no-real-consent distinction explicit.

## Limitations

- Movement is deterministic replay, not keyboard input.
- Collision is a guard packet, not full physics.
- Proximity is nearest-agent distance, not full perception.
- Consent prompts are visible state, not a live choice UI.
- Tools are promptable objects, not manipulable physics objects.
- The browser page is still a replay viewer.
- This is not complete 3D gameplay.

## Next gate

The next gate should be an interactive browser prototype with keyboard avatar control, collision feedback, and consent prompt selection.

Report 203 proves the loop state. The next step is to let the user actually move the avatar and choose prompt responses inside the browser.
