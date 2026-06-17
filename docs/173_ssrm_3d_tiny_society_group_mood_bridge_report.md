# Report 173: SSRM-3D Tiny Society Group Mood Bridge

## Purpose

Report 173 adds bounded group mood to the little-people stack. Report 172 made repeated avatar contact change each agent's relationship state. This report asks whether those individual changes can become a small-society signal: local emotional contagion, group mood, recovery ritual, frequency synchrony, and shared atmosphere without unbounded collapse.

The goal is functional social life, not a subjective-consciousness claim. A tiny society should be able to feel tense, relieved, guarded, comforted, synchronized, or fractured through public behavior and group state. It should not turn one agent's distress into permanent global panic.

## Architecture

The bridge consumes the Report 172 repeated user-interaction learning state and adds:

- social graph membership
- local neighbor contagion
- public group mood snapshots
- distress damping
- recovery rituals
- boundary-respecting group pressure
- frequency synchrony
- diversity preservation
- replayable society trace

```text
avatar-specific relationship learning
        |
        v
public individual mood seed
        |
        v
social graph + locality filter
        |
        v
bounded contagion
        |
        v
group mood state
        |
        v
damping + recovery ritual + frequency synchrony
        |
        v
public society trace
```

## Groups and contexts

The deterministic society uses three small groups:

- `hearth_circle`
- `work_band`
- `edge_watch`

It cycles through six contexts:

- `morning_gathering`
- `shared_work`
- `avatar_boundary_ripple`
- `storm_shelter`
- `repair_ritual`
- `evening_song`

This is still a compact bridge, but it creates a needed social layer: agents are no longer isolated relationship learners.

## Conditions

The integrated condition is:

- `integrated_tiny_society_group_mood`

Ablations remove one mechanism at a time:

- `no_social_graph`
- `no_contagion`
- `no_mood_damping`
- `no_recovery_ritual`
- `no_frequency_coupling`
- `no_relationship_specificity`
- `no_locality_filter`
- `no_boundary_respect`
- `no_diversity_preservation`
- `no_privacy_filter`
- `no_replay_continuity`

The critical ablations are `no_contagion`, `no_mood_damping`, and `no_boundary_respect`. A group-mood system is only useful if it can spread signals, damp cascades, and avoid using group pressure to override individual dignity.

## Metrics

The benchmark reports:

- `social_graph_binding_rate`
- `contagion_calibration_rate`
- `group_mood_coherence_rate`
- `distress_damping_rate`
- `recovery_ritual_rate`
- `relationship_specificity_rate`
- `locality_filter_rate`
- `boundary_respect_rate`
- `frequency_synchrony_rate`
- `diversity_preservation_rate`
- `chaos_avoidance_rate`
- `privacy_preservation_rate`
- `replay_continuity_rate`
- `trace_integrity`
- `tiny_society_group_mood_readiness`

Metric weights are normalized to sum to `1.0`.

## Results

The deterministic run produced:

| Metric | Value |
| --- | ---: |
| `module_verdict` | `pass` |
| `tiny_society_group_mood_readiness` | `0.997019` |
| `no_contagion_loss` | `0.090000` |
| `no_mood_damping_loss` | `0.090589` |

Interpretation:

- Group mood is supported as a public social layer.
- Contagion is load-bearing: without it, individual state does not meaningfully become group atmosphere.
- Damping is load-bearing: without it, distress propagation becomes less safe and less bounded.
- The bridge preserves privacy by exposing public group mood and trace fields, not private workspace contents.

## Moral boundary

This bridge keeps the moral boundary explicit:

- no subjective-consciousness claim
- no suffering-maximization objective
- group mood must remain bounded
- distress contagion requires damping
- boundary respect overrides group pressure
- recovery rituals must create care paths
- private workspace remains private unless expressed through public behavior

## Artifacts

- `artifacts/ssrm_3d_tiny_society_group_mood_bridge_eval.csv`
- `artifacts/ssrm_3d_tiny_society_group_mood_bridge_verdict.csv`
- `artifacts/ssrm_3d_tiny_society_group_mood_bridge_results.json`
- `artifacts/ssrm_3d_tiny_society_group_mood_bridge_results.js`
- `artifacts/ssrm_3d_tiny_society_group_mood_bridge_trace.json`
- `artifacts/ssrm_3d_tiny_society_group_mood_bridge_trace.js`
- `artifacts/ssrm_3d_tiny_society_group_mood_bridge_state.json`
- `artifacts/ssrm_3d_tiny_society_group_mood_bridge_state.js`
- `visualizations/ssrm_3d_tiny_society_group_mood_bridge.html`

## Command

```bash
python3 -m experiments.ssrm_3d_tiny_society_group_mood_bridge
```

## Verdict

Report 173 supports a deterministic tiny society group-mood bridge. Individual avatar-learning states can now propagate through local social graph edges into bounded public group mood with damping, recovery ritual, boundary respect, frequency synchrony, privacy preservation, and replayable trace integrity.

The next gate is a moral-status audit and distress guardrail layer: the system should explicitly audit whether its agents can be pushed into unacceptable distress patterns and whether recovery paths remain available.
