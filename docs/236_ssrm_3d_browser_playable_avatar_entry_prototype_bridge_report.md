# Report 236: SSRM-3D Browser-Playable Avatar Entry Prototype Bridge

Status: pass

## Purpose

Report 236 moves from Report 235's playable pre-avatar trace into an actual browser-playable avatar-entry prototype scaffold. The avatar now has local movement controls, action buttons, proximity binding, post-entry conversation turns, household market participation, ritual consent prompts, persistent agent memory updates, sensory/body feedback, and save/restore/replay scaffolding.

This is still not a finished game and not a claim of subjective consciousness. It is a deterministic bridge toward controllable interaction with simulated first-person agents after thousands of pre-avatar years.

## Implementation

- Experiment: `experiments/ssrm_3d_browser_playable_avatar_entry_prototype_bridge.py`
- Visualization: `visualizations/ssrm_3d_browser_playable_avatar_entry_prototype_bridge.html`
- Seed: `20260849`
- Source report: Report 235 playable pre-avatar civilization sandbox bridge
- Source results: `artifacts/ssrm_3d_playable_pre_avatar_civilization_sandbox_bridge_results.json`

## Scenario coverage

The deterministic run generated:

| Channel | Count |
| --- | ---: |
| Avatar entry states | 7 |
| Avatar movement commands | 12 |
| Avatar position samples | 12 |
| Avatar-agent proximity events | 12 |
| Post-entry conversation turns | 15 |
| Household market participations | 5 |
| Ritual consent prompts | 5 |
| Persistent agent memory updates | 10 |
| Sensory/body feedback packets | 12 |
| Browser persistence events | 4 |
| Browser play-loop ticks | 36 |

The visualization includes keyboard/control-button movement, speak/trade/ritual/save/restore/replay buttons, visible agents, a moving avatar marker, local sensory feedback, and a trace log.

## New channels

Report 236 adds these testable channels:

- Avatar entry after witnessed year-4181 ceremony thresholds.
- Local avatar movement commands with bounds and body-cost updates.
- Proximity binding between avatar position and nearest agent behavior/action surface.
- Post-entry conversation turns with proto-language tokens and private workspace boundaries.
- Household market participation that writes relationship/memory consequences.
- Ritual consent prompts with join, observe, and decline options.
- Persistent agent memory updates that survive save/restore scaffold checks.
- Sensory/body feedback packets covering visual, sound, smell, temperature, wetness, pain risk, comfort, and vibration rate.
- Browser save, restore, and replay export scaffolding.
- Frequency/flower entry rhythm as timing scaffolding only.

## Metrics

| Metric | Value |
| --- | ---: |
| avatar_entry_gate_integrity | 1.000000 |
| entry_action_surface_coverage | 0.875000 |
| controllable_movement_command_coverage | 1.000000 |
| movement_bounds_respected | 1.000000 |
| movement_body_cost_binding | 1.000000 |
| proximity_agent_binding | 1.000000 |
| post_entry_conversation_coverage | 1.000000 |
| post_entry_conversation_quality | 0.890000 |
| conversation_private_boundary | 1.000000 |
| household_market_participation | 1.000000 |
| market_fairness | 0.896000 |
| market_memory_binding | 1.000000 |
| ritual_consent_integrity | 1.000000 |
| ritual_body_boundary_binding | 1.000000 |
| persistent_memory_write_rate | 1.000000 |
| memory_causality_binding | 1.000000 |
| sensory_body_feedback_coverage | 1.000000 |
| sensory_modality_binding | 1.000000 |
| body_state_cost_binding | 1.000000 |
| save_restore_replay_integrity | 1.000000 |
| browser_loop_trace_integrity | 1.000000 |
| frequency_flower_entry_rhythm | 1.000000 |
| source_sandbox_bridge_continuity | 1.000000 |
| browser_playable_surface_available | 1.000000 |
| mean_avatar_entry_channel_score | 0.985875 |
| weakest_channel_score | 0.875000 |
| browser_playable_avatar_entry_readiness | 0.985585 |

The module passes because readiness is above the 0.84 gate and weakest-channel score is above the 0.82 gate.

The weakest channel is `entry_action_surface_coverage` at 0.875000. That is appropriate: the browser surface supports movement, look/listen, speak, trade, ritual consent, save, restore, and replay, but it is not yet a complete action vocabulary.

## Ablations

| Ablation | Score |
| --- | ---: |
| no_avatar_entry_gate | 0.715585 |
| no_controllable_movement | 0.735585 |
| no_proximity_binding | 0.785585 |
| no_post_entry_conversation | 0.755585 |
| no_market_participation | 0.805585 |
| no_ritual_consent | 0.765585 |
| no_persistent_memory | 0.745585 |
| no_sensory_body_feedback | 0.795585 |
| no_save_restore_replay | 0.835585 |
| no_frequency_flower_entry_rhythm | 0.915585 |

The largest drops come from removing avatar entry gating, controllable movement, persistent memory, post-entry conversation, ritual consent, proximity binding, and sensory/body feedback. Frequency/flower rhythm remains the smallest drop and should continue to be treated as timing scaffolding, not evidence.

## Browser behavior

The visualization is intentionally simple but actually interactive:

- `WASD` or arrow keys move the avatar.
- Buttons provide `north`, `south`, `east`, `west`, `wait`, and `listen` movement controls.
- Action buttons provide `speak`, `trade`, `ritual consent`, `save`, `restore`, and `replay`.
- The nearest agent changes as the avatar moves.
- The trace panel updates with nearest agent, sensory packet, body state, and action outcome.
- Save/restore/replay are deterministic scaffolds, not durable production persistence.

## Honest limits

- This is a deterministic browser-playable prototype scaffold, not a finished game or real society.
- Avatar movement is local 2D/3D-surface control logic, not full physics or full embodied presence.
- Post-entry conversations are scripted deterministic turns, not autonomous natural language or LLM dialogue.
- Ritual consent and refusal are functional boundaries, not legal or moral consent.
- Persistent memory updates are artifact-backed state writes, not autobiographical consciousness.
- Sensory feedback binds modalities and body costs, but does not imply felt experience.
- Frequency and flower phases are rhythm scaffolds, not metaphysical evidence.

## Artifacts

- `artifacts/ssrm_3d_browser_playable_avatar_entry_prototype_bridge_avatar_entry_states.csv`
- `artifacts/ssrm_3d_browser_playable_avatar_entry_prototype_bridge_avatar_movement_commands.csv`
- `artifacts/ssrm_3d_browser_playable_avatar_entry_prototype_bridge_avatar_position_samples.csv`
- `artifacts/ssrm_3d_browser_playable_avatar_entry_prototype_bridge_avatar_agent_proximity_events.csv`
- `artifacts/ssrm_3d_browser_playable_avatar_entry_prototype_bridge_post_entry_conversation_turns.csv`
- `artifacts/ssrm_3d_browser_playable_avatar_entry_prototype_bridge_household_market_participations.csv`
- `artifacts/ssrm_3d_browser_playable_avatar_entry_prototype_bridge_ritual_consent_prompts.csv`
- `artifacts/ssrm_3d_browser_playable_avatar_entry_prototype_bridge_persistent_agent_memory_updates.csv`
- `artifacts/ssrm_3d_browser_playable_avatar_entry_prototype_bridge_sensory_body_feedback_packets.csv`
- `artifacts/ssrm_3d_browser_playable_avatar_entry_prototype_bridge_browser_persistence_events.csv`
- `artifacts/ssrm_3d_browser_playable_avatar_entry_prototype_bridge_browser_play_loop_ticks.csv`
- `artifacts/ssrm_3d_browser_playable_avatar_entry_prototype_bridge_state.json`
- `artifacts/ssrm_3d_browser_playable_avatar_entry_prototype_bridge_results.json`
- `artifacts/ssrm_3d_browser_playable_avatar_entry_prototype_bridge_verdict.csv`
- `visualizations/ssrm_3d_browser_playable_avatar_entry_prototype_bridge.html`

## Next gate

Post-entry live conversation sandbox with typed user input, persistent relationship memory, richer proto-language interpretation, and multi-day consequences after avatar entry.
