# Report 154: SSRM-3D recurrent faction-dialogue controller bridge

## Summary

Report 154 moves past isolated learned policy rows into turn-by-turn avatar dialogue sessions. A deterministic recurrent controller carries proposal context across follow-up questions, cites source-native council ledgers, refuses subjective-consciousness overclaims, writes persistent agent memory, and applies learned faction-state update deltas trained on earlier councils to later held-out sessions.

The integrated condition reaches recurrent-dialogue readiness `1.000000`. Turn-intent accuracy is `1.000000`, follow-up context resolution is `1.000000`, persistent memory update rate is `1.000000`, learned faction-update accuracy is `1.000000`, and refusal-boundary accuracy is `1.000000`.

This is not an LLM, not open-ended conversation, not subjective consciousness, and not a complete playable world. It is a deterministic recurrent controller bridge over source-native governance histories.

## What changed

- Added `experiments/ssrm_3d_recurrent_faction_dialogue_controller_bridge.py`.
- Uses Report 152 source-native council ledgers and Report 153 learned policy state.
- Builds six-turn avatar sessions with explicit source-body questions plus follow-ups over "that proposal".
- Carries recurrent state: last proposal, last intent, and turns seen.
- Writes persistent proposal memories across live sessions.
- Trains faction-update deltas on earlier councils and applies them to held-out sessions.
- Emits a browser viewer at `visualizations/ssrm_3d_recurrent_faction_dialogue_controller_bridge.html`.

## Conditions

| Condition | Readiness | Intent | Context | Memory | Learned update | Citation | Refusal | Cross-turn | Continuity | Held-out | Replay |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `integrated_recurrent_faction_dialogue_controller` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_recurrent_state` | `0.388333` | `0.166667` | `0.000000` | `0.000000` | `1.000000` | `0.200000` | `0.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_turn_context_resolution` | `0.388333` | `0.166667` | `0.000000` | `0.000000` | `1.000000` | `0.200000` | `0.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_persistent_agent_memory` | `0.880000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_learned_faction_updates` | `0.880000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_source_citation` | `0.900000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_refusal_boundary` | `0.881667` | `0.833333` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_heldout_session_split` | `0.920000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` |
| `no_trace_replay` | `0.930000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` |

## Recurrent controller objects

- `recurrent_dialogue_state`: last proposal, last intent, and turns seen inside each avatar session.
- `persistent_agent_memory`: proposal memories carried across live sessions.
- `learned_faction_update_model`: average train-council deltas by faction and proposal kind/decision.
- `turn_context_resolver`: follow-up questions bind to the recurrent last proposal.
- `source_grounded_response`: answers cite source-native ledger fields when available.
- `refusal_boundary_turn`: consciousness overclaim is handled as a recurrent turn, not a proof.

## Evidence and ablations

Removing recurrent state drops readiness by `0.611667`. Removing turn-context resolution drops readiness by `0.611667`. Removing persistent memory, learned faction updates, source citation, refusal boundaries, held-out session split, or replay traces produces targeted losses. This keeps the bridge honest: it tests recurrent session machinery, not open-ended thought.

## Artifacts

- `artifacts/ssrm_3d_recurrent_faction_dialogue_controller_bridge_eval.csv`
- `artifacts/ssrm_3d_recurrent_faction_dialogue_controller_bridge_verdict.csv`
- `artifacts/ssrm_3d_recurrent_faction_dialogue_controller_bridge_results.json`
- `artifacts/ssrm_3d_recurrent_faction_dialogue_controller_bridge_trace.json`
- `artifacts/ssrm_3d_recurrent_faction_dialogue_controller_bridge_state.json`
- `artifacts/ssrm_3d_recurrent_faction_dialogue_controller_bridge_results.js`
- `artifacts/ssrm_3d_recurrent_faction_dialogue_controller_bridge_trace.js`
- `artifacts/ssrm_3d_recurrent_faction_dialogue_controller_bridge_state.js`
- `visualizations/ssrm_3d_recurrent_faction_dialogue_controller_bridge.html`

## Verdict

The bridge passes as a recurrent faction-dialogue controller because it resolves follow-up turns, preserves source citations, writes persistent memory, applies learned faction-state updates, refuses overclaims, and exposes targeted recurrent-state ablations on held-out live sessions.

The next gate is to attach this recurrent dialogue controller to the autonomous live-agent loop and embodied avatar input so dialogue affects live agent body/world state in the same running simulation.
