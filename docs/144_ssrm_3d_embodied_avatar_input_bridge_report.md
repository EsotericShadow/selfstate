# Report 144: SSRM-3D Embodied Avatar Input Bridge

## Purpose

Report 143 showed that scripted avatar interventions can change mature Report 142 agent-packet state. That was still too narrow: the player could only choose prewritten intervention templates.

Report 144 adds a deterministic embodied-input bridge. It uses Report 142 avatar-entry packets and the Report 143 final agent state, then feeds typed player text through a local keyword-lattice parser while also tracking avatar position, proximity, sensory context, agent workspace memory, world consequences, and replay traces.

The Report 143 world state is intentionally saturated, so this benchmark opens a new local input session with bounded world-state headroom. That keeps the inherited mature state while making action consequences measurable instead of falsely scoring every consequence as zero because the world is already clamped at `1.0`.

This is still not subjective consciousness, not an LLM dialogue system, not mature autonomous live agents, and not a complete playable civilization.

## What changed

- Added `experiments/ssrm_3d_embodied_avatar_input_bridge.py`.
- Added deterministic player text events with ambiguous/noisy inputs, invalid out-of-range actions, observation-only inputs, promises, repairs, route requests, resource offers, comfort actions, weather reports, and symbol proposals.
- Added ablations for spatial embodiment, free-text parsing, agent memory updates, sensory context, action consequences, and persistent traces.
- Added `visualizations/ssrm_3d_embodied_avatar_input_bridge.html`, a browser surface where the user can move an avatar body, select an agent, type arbitrary text, and watch deterministic parser/proximity/world-state consequences.

## Conditions

| Condition | Embodied readiness | Parse | Proximity | Agent update | World update | Sensory context | Workspace continuity | Trace |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `integrated_embodied_avatar_input` | `0.839146` | `0.850000` | `0.937500` | `0.750000` | `0.750000` | `0.532469` | `1.000000` | `1.000000` |
| `no_spatial_body` | `0.322896` | `0.850000` | `0.000000` | `0.000000` | `0.000000` | `0.532469` | `0.000000` | `1.000000` |
| `no_free_text_parser` | `0.568148` | `0.250000` | `1.000000` | `0.250000` | `0.250000` | `0.151235` | `1.000000` | `1.000000` |
| `no_agent_memory_update` | `0.679146` | `0.850000` | `0.937500` | `0.750000` | `0.750000` | `0.532469` | `0.000000` | `1.000000` |
| `no_sensory_context` | `0.795650` | `0.850000` | `0.937500` | `0.750000` | `0.750000` | `0.170000` | `1.000000` | `1.000000` |
| `no_action_consequence` | `0.734146` | `0.850000` | `0.937500` | `0.750000` | `0.000000` | `0.532469` | `1.000000` | `1.000000` |
| `no_persistent_trace` | `0.699146` | `0.850000` | `0.937500` | `0.750000` | `0.750000` | `0.532469` | `1.000000` | `0.000000` |

## Verdict

The integrated condition reaches embodied-input readiness `0.839146`. The bridge passes its bounded gate because typed inputs are usually parsed (`0.850000`), grounded actions are mostly proximity-valid (`0.937500`), agent state updates occur (`0.750000`), world consequences occur (`0.750000`), workspace continuity is preserved (`1.000000`), and traces are complete (`1.000000`).

Ablations reduce readiness:

| Ablation | Readiness loss |
|---|---:|
| `no_spatial_body` | `0.516250` |
| `no_free_text_parser` | `0.270998` |
| `no_agent_memory_update` | `0.160000` |
| `no_sensory_context` | `0.043496` |
| `no_action_consequence` | `0.105000` |
| `no_persistent_trace` | `0.140000` |

`supports_embodied_avatar_input_bridge = true`.

`supports_subjective_consciousness = false`.

`supports_open_ended_dialogue = false`.

`supports_complete_playable_world = false`.

## Interpretation

This report moves the playable-world line from scripted buttons toward typed embodied input. The important added loop is not language intelligence. It is the closed local loop:

```text
player body position -> typed text -> deterministic parse -> proximity gate -> sensory alignment -> agent workspace update -> world consequence -> replay trace
```

That makes the viewer more useful as a live test harness, but it remains a bridge. The parser is a fixed keyword lattice, so it can reject noise, misread unusual phrasing, and cannot sustain real open-ended conversation. The next gates are richer local affordances, persistent multi-agent scheduling, learned or model-based input interpretation, and eventually a true agent loop that acts without scripted event rows.

## Artifacts

- `artifacts/ssrm_3d_embodied_avatar_input_bridge_eval.csv`
- `artifacts/ssrm_3d_embodied_avatar_input_bridge_verdict.csv`
- `artifacts/ssrm_3d_embodied_avatar_input_bridge_results.json`
- `artifacts/ssrm_3d_embodied_avatar_input_bridge_trace.json`
- `artifacts/ssrm_3d_embodied_avatar_input_bridge_state.json`
- `artifacts/ssrm_3d_embodied_avatar_input_bridge_results.js`
- `artifacts/ssrm_3d_embodied_avatar_input_bridge_trace.js`
- `artifacts/ssrm_3d_embodied_avatar_input_bridge_state.js`
- `visualizations/ssrm_3d_embodied_avatar_input_bridge.html`

## Reproduction

```bash
python3 -m experiments.ssrm_3d_deep_time_playable_bridge
python3 -m experiments.ssrm_3d_live_avatar_intervention_bridge
python3 -m experiments.ssrm_3d_embodied_avatar_input_bridge
```
