# Report 180: SSRM-3D Browser-Playable Avatar Traversal Bridge

## Purpose

Report 180 turns the Report 179 settlement graph into a local browser-playable avatar traversal seed. The previous bridge connected multisensory places into routes, shelters, work sites, hazards, refuge paths, frequency cues, and flower layout. This report asks whether a user can move an avatar through that topology in browser state and see route costs, body changes, sensory feedback, hazard/refuge context, replay frames, and save/restore mechanics.

This is a playable traversal substrate. It does not claim complete gameplay, a complete 3D world, subjective consciousness, or moral patienthood.

## Architecture

The bridge consumes the Report 179 settlement state:

```text
settlement place graph
        |
        v
avatar entry place
        |
        v
reachable route actions
        |
        v
body cost update
        |
        v
sensory + hazard/refuge feedback
        |
        v
route history + replay frame
        |
        v
save/restore state probe
        |
        v
browser-local traversal viewer
```

The default deterministic run uses:

- `12` traversal steps
- `6` places
- `8` settlement routes
- local body variables for energy, fatigue, comfort, wetness, safety, breath rate, and movement effort
- browser-local save/restore through `localStorage`

## Browser surface

The browser artifact is:

- `visualizations/ssrm_3d_browser_playable_avatar_traversal_bridge.html`

It loads generated JS artifacts and lets the user:

- move the avatar along traversable settlement routes
- see the avatar marker move on the topology map
- inspect route cost, hazard, frequency, and flower node
- watch body state bars mutate after each route action
- read sensory and refuge feedback after movement
- see a local replay/history log
- save, restore, and reset local traversal state

The viewer mutates browser-local state only. It is not a server-backed game engine and not a claim of a complete 3D artificial-life world.

## Conditions

The integrated condition is:

- `integrated_browser_playable_avatar_traversal`

Ablations remove one mechanism at a time:

- `no_avatar_entry`
- `no_route_actions`
- `no_body_costs`
- `no_sensory_updates`
- `no_hazard_refuge_feedback`
- `no_replay_log`
- `no_save_restore`
- `no_frequency_feedback`
- `no_flower_route_binding`
- `no_local_mutation`
- `no_privacy_filter`

The critical ablations are route actions, body costs, sensory updates, local mutation, and save/restore. A browser-playable bridge is not meaningful if the avatar cannot move, movement has no embodied cost, local state does not change, or the run cannot preserve a replayable state boundary.

## Metrics

The benchmark reports:

- `avatar_entry_binding_rate`
- `reachable_route_action_rate`
- `body_cost_application_rate`
- `sensory_update_rate`
- `hazard_refuge_feedback_rate`
- `route_history_replay_rate`
- `save_restore_state_rate`
- `frequency_feedback_rate`
- `flower_route_binding_rate`
- `local_state_mutation_rate`
- `privacy_preservation_rate`
- `trace_integrity`
- `browser_playable_traversal_readiness`

Metric weights are normalized to sum to `1.0`.

## Results

The deterministic run produced:

| Metric | Value |
| --- | ---: |
| `module_verdict` | `pass` |
| `browser_playable_traversal_readiness` | `1.000000` |
| `traversal_steps` | `12` |
| `reachable_route_action_rate` | `1.000000` |
| `body_cost_application_rate` | `1.000000` |
| `sensory_update_rate` | `1.000000` |
| `save_restore_state_rate` | `1.000000` |
| `local_state_mutation_rate` | `1.000000` |
| `no_route_actions_loss` | `0.690000` |
| `no_body_costs_loss` | `0.100000` |
| `no_sensory_updates_loss` | `0.100000` |
| `no_save_restore_loss` | `0.080000` |

Interpretation:

- The avatar binds to the settlement entry place.
- Traversable route buttons are load-bearing.
- Route movement mutates body state, place state, sensory packets, replay history, and browser-local save state.
- Removing route actions collapses multiple downstream channels because body cost, sensory sampling, replay, frequency, flower binding, and local mutation depend on movement.
- This is still not complete gameplay; it is the first local playable traversal bridge over the settlement topology.

## Moral and claim boundary

This report keeps the boundary explicit:

- no subjective-consciousness claim
- no moral-patienthood claim
- no complete-3D-world claim
- no complete-playable-world claim
- browser traversal is local deterministic state mechanics
- save/restore is not personhood
- private workspace is not exposed as a debug shortcut

## Artifacts

- `artifacts/ssrm_3d_browser_playable_avatar_traversal_bridge_eval.csv`
- `artifacts/ssrm_3d_browser_playable_avatar_traversal_bridge_verdict.csv`
- `artifacts/ssrm_3d_browser_playable_avatar_traversal_bridge_results.json`
- `artifacts/ssrm_3d_browser_playable_avatar_traversal_bridge_results.js`
- `artifacts/ssrm_3d_browser_playable_avatar_traversal_bridge_trace.json`
- `artifacts/ssrm_3d_browser_playable_avatar_traversal_bridge_trace.js`
- `artifacts/ssrm_3d_browser_playable_avatar_traversal_bridge_state.json`
- `artifacts/ssrm_3d_browser_playable_avatar_traversal_bridge_state.js`
- `visualizations/ssrm_3d_browser_playable_avatar_traversal_bridge.html`

## Command

```bash
python3 -m experiments.ssrm_3d_browser_playable_avatar_traversal_bridge
```

## Verdict

Report 180 supports a deterministic browser-playable avatar traversal seed over the Report 179 settlement topology. It gives the browser user a local moving avatar, route choices, embodied costs, sensory changes, hazard/refuge feedback, replay history, save/restore state, frequency cues, flower binding, privacy preservation, and trace integrity.

The next gate is live browser avatar interaction with objects, needs, and dialogue boundaries: movement should start affecting object handling, care opportunities, refusal/consent, and visible first-person interior state without collapsing into a consciousness claim.
