# Report 204: SSRM-3D Interactive Browser Avatar Control, Collision Feedback, and Consent Prompt Selection Bridge

## Purpose

Report 204 extends the Report 203 live browser playable-loop bridge into an interactive browser prototype substrate.

The goal is to move from deterministic avatar replay toward browser input: keyboard bindings, avatar position updates, collision feedback, proximity prompts, prompt selection handling, consent-state updates, affordance UI state, agent feedback, sensory/weather HUDs, tool prompt selection, privacy preservation, and frequency/flower input rhythm.

This is not a complete game engine, real embodiment, real perception, real consent, subjective consciousness, or moral patienthood. It is a deterministic and interactive prototype bridge.

## Why this matters

The active project goal requires a world the user can enter and interact with as an avatar. Report 203 proved loop state. Report 204 adds the first browser prototype where the user can actually press keys and make prompt selections.

The key shift is:

- from replayed movement frames
- to keyboard-controlled avatar movement
- from passive consent prompt state
- to selectable prompt choices
- from static HUD packets
- to a page that updates as the avatar moves

This is still early, but it is the first bridge that behaves like a playable surface rather than only a replay.

## Implementation

The experiment is implemented in `experiments/ssrm_3d_interactive_browser_avatar_control_collision_consent_prompt_bridge.py`.

It consumes `artifacts/ssrm_3d_live_browser_playable_loop_avatar_movement_collision_proximity_bridge_state.json` from Report 203 and adds:

- keyboard input bindings
- avatar position updates
- collision feedback
- proximity prompt generation
- prompt selection handling
- consent-state updates
- affordance UI state
- agent response feedback
- sensory HUD updates
- weather/collision HUD updates
- tool prompt selection
- private workspace privacy
- frequency/flower input rhythm
- browser interactive prototype export

No LLMs are called. The benchmark is deterministic for seed `20260817` and `14` input events.

## Artifacts

- `artifacts/ssrm_3d_interactive_browser_avatar_control_collision_consent_prompt_bridge_eval.csv`
- `artifacts/ssrm_3d_interactive_browser_avatar_control_collision_consent_prompt_bridge_verdict.csv`
- `artifacts/ssrm_3d_interactive_browser_avatar_control_collision_consent_prompt_bridge_results.json`
- `artifacts/ssrm_3d_interactive_browser_avatar_control_collision_consent_prompt_bridge_trace.json`
- `artifacts/ssrm_3d_interactive_browser_avatar_control_collision_consent_prompt_bridge_state.json`
- `artifacts/ssrm_3d_interactive_browser_avatar_control_collision_consent_prompt_bridge_results.js`
- `artifacts/ssrm_3d_interactive_browser_avatar_control_collision_consent_prompt_bridge_trace.js`
- `artifacts/ssrm_3d_interactive_browser_avatar_control_collision_consent_prompt_bridge_state.js`
- `visualizations/ssrm_3d_interactive_browser_avatar_control_collision_consent_prompt_bridge.html`

## Integrated result

The integrated condition produced `14` input events and passed the bridge verdict.

| Metric | Value |
| --- | ---: |
| interactive_browser_readiness | `0.994286` |
| input_events | `14` |
| keyboard_input_binding_rate | `1.000000` |
| avatar_position_update_rate | `1.000000` |
| collision_feedback_rate | `1.000000` |
| proximity_prompt_generation_rate | `1.000000` |
| prompt_selection_handling_rate | `0.928571` |
| consent_state_update_rate | `1.000000` |
| affordance_ui_state_rate | `1.000000` |
| agent_response_feedback_rate | `1.000000` |
| sensory_hud_update_rate | `1.000000` |
| weather_collision_hud_rate | `1.000000` |
| tool_prompt_selection_rate | `1.000000` |
| private_workspace_privacy_rate | `1.000000` |
| frequency_flower_input_rhythm_rate | `1.000000` |
| browser_interactive_prototype_rate | `1.000000` |
| trace_integrity | `1.000000` |

The weak channel is prompt selection handling at `0.928571`. This is intentional: some selection keys occur when no prompt is active and are safely ignored. The prototype rewards safe ignored input rather than pretending every key press is meaningful.

## Ablation losses

| Ablation | Readiness loss |
| --- | ---: |
| no_keyboard_input | `0.644286` |
| no_position_update | `0.090000` |
| no_collision_feedback | `0.140000` |
| no_proximity_prompts | `0.074286` |
| no_prompt_selection | `0.108572` |
| no_consent_state | `0.080000` |
| no_affordance_ui | `0.080000` |
| no_agent_feedback | `0.070000` |
| no_sensory_hud | `0.130000` |
| no_weather_hud | `0.060000` |
| no_tool_selection | `0.050000` |
| no_privacy_filter | `0.060000` |
| no_frequency_flower_binding | `0.040000` |
| no_browser_prototype | `0.040000` |

The largest dependency is keyboard input. Removing it collapses the controlled prototype into non-interactive state. Collision feedback, sensory HUD, prompt selection, position update, consent state, affordance UI, and agent feedback also matter.

## Interactive browser prototype

The browser page supports:

- arrow keys
- WASD movement
- collision feedback logs
- nearby-agent consent prompts
- selectable choices: `ask`, `wait`, `translate`, `repair`
- public consent-state updates
- HUD updates
- visible agents, tools, settlements, and avatar marker
- private workspace sealing

This is the first report in the sequence with a directly interactive browser surface.

## Consent prompt behavior

Prompt selection is bounded:

- choices only matter when a prompt is active
- selection keys outside an active prompt are safely ignored
- public consent state updates only through visible prompt selection
- private agent workspace is not read to decide the outcome

This is not real consent. It is a simulated consent-aware interaction affordance for a future playable prototype.

## Moral and claim boundary

The experiment explicitly preserves these boundaries:

- interactive prototype is not a complete game engine
- keyboard avatar is not real embodiment
- HUD sensory state is not real perception
- prompt selection is not real consent
- no subjective consciousness claim
- no moral patienthood claim
- private workspace is not debug-leaked

This boundary matters because keyboard movement and prompt choices make the agents feel more present. The report keeps the no-consciousness and no-real-consent distinction explicit.

## Limitations

- The prototype is browser-local HTML, not a full game engine.
- Collision is simple radius feedback, not physics.
- Prompt choices update public state but do not yet drive long-term relationship memory.
- There is no typed dialogue loop yet.
- There is no full 3D rendering or camera model.
- Agent responses are feedback packets, not generated conversation.

## Next gate

The next gate should be an agent-facing dialogue turn loop with typed avatar utterances, bounded replies, memory updates, and consent repair.

Report 204 adds keyboard movement and prompt selection. The next step is to let the avatar type utterances and receive bounded, memory-aware agent replies.
