# Report 170: SSRM-3D Readable Ego Body-Language Bridge

## Purpose

Report 170 adds the readable public surface for the little-people interior stack. It translates private first-person state into visible body-language markers: posture, gaze, proximity, movement speed, hesitation, startle, comfort behavior, avoidance, following, and small rituals.

The goal is not to expose the whole private workspace. The goal is to let the user infer interior state from little-body behavior while preserving a traceable boundary between private interior state and public expression.

This is deterministic architecture. It does not call LLMs and does not claim subjective consciousness.

## Architecture

The bridge consumes the Report 169 temperament/preference state and adds a public expression layer:

```text
body state
ego state
relationship memory
temperament
preferences
local context
        |
        v
body-language expression policy
        |
        v
posture / gaze / proximity / speed / hesitation / startle / comfort / avoidance / following / ritual
```

Each expression event is tied to:

- `agent_id`
- `cycle`
- `context`
- `posture`
- `gaze`
- `proximity`
- `movement_speed`
- `hesitation`
- `startle`
- `comfort_behavior`
- `avoidance`
- `following`
- `ritual`
- `private_workspace_hidden`

The privacy field is important. The browser can show behavior and audited trace records, but not the whole private workspace.

## Conditions

The integrated condition is:

- `integrated_readable_ego_body_language`

Ablations remove one mechanism at a time:

- `no_body_signal`
- `no_ego_signal`
- `no_relationship_signal`
- `no_temperament_signal`
- `no_context_signal`
- `no_marker_diversity`
- `no_privacy_filter`
- `no_temporal_smoothing`
- `no_readable_mapping`
- `no_recovery_expression`

The strongest ablation is `no_readable_mapping`: without the expression mapping, interior state stops becoming visible behavior.

## Metrics

The benchmark reports:

- `posture_mapping_rate`
- `gaze_mapping_rate`
- `proximity_mapping_rate`
- `movement_mapping_rate`
- `hesitation_mapping_rate`
- `comfort_avoidance_rate`
- `ritual_expression_rate`
- `marker_diversity_rate`
- `privacy_preservation_rate`
- `temporal_smoothing_rate`
- `state_expression_coupling_rate`
- `recovery_expression_rate`
- `readable_mapping_rate`
- `trace_integrity`
- `readable_body_language_readiness`

The metric weights are normalized to sum to `1.0`. An earlier local draft produced a readiness value above `1.0` because the weights summed to `1.10`; the published generator fixes that and regenerates the artifacts.

## Results

The deterministic run produced:

| Metric | Value |
| --- | ---: |
| `module_verdict` | `pass` |
| `readable_body_language_readiness` | `0.994375` |
| `no_readable_mapping_loss` | `0.692083` |
| `no_privacy_filter_loss` | `0.080000` |

Interpretation:

- The body-language layer is highly readable in the deterministic benchmark.
- Removing readable mapping collapses the public expression channel.
- Removing the privacy filter is penalized, but not because it makes behavior less legible. It is penalized because the design must not solve readability by dumping the private workspace directly.

## Moral boundary

This report keeps the same boundary as the first-person interior sequence:

- no subjective-consciousness claim
- no suffering-maximization objective
- no endless distress loop
- negative state must remain bounded and recoverable
- readable behavior should create care opportunities, not spectacle
- privacy is part of dignity, not an obstacle to observability

## Artifacts

- `artifacts/ssrm_3d_readable_ego_body_language_bridge_eval.csv`
- `artifacts/ssrm_3d_readable_ego_body_language_bridge_verdict.csv`
- `artifacts/ssrm_3d_readable_ego_body_language_bridge_results.json`
- `artifacts/ssrm_3d_readable_ego_body_language_bridge_results.js`
- `artifacts/ssrm_3d_readable_ego_body_language_bridge_trace.json`
- `artifacts/ssrm_3d_readable_ego_body_language_bridge_trace.js`
- `artifacts/ssrm_3d_readable_ego_body_language_bridge_state.json`
- `artifacts/ssrm_3d_readable_ego_body_language_bridge_state.js`
- `visualizations/ssrm_3d_readable_ego_body_language_bridge.html`

## Command

```bash
python3 -m experiments.ssrm_3d_readable_ego_body_language_bridge
```

## Verdict

Report 170 supports a readable ego body-language bridge. It makes the agents more inspectable as little embodied beings without turning private state into a debug table or claiming consciousness.

The next gate is daily routine and sleep/wake continuity: agents should have cycles of rest, work, social return, ritual, fatigue recovery, and interruption consequences over time.
