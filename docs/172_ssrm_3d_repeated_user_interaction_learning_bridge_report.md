# Report 172: SSRM-3D Repeated User-Interaction Learning Bridge

## Purpose

Report 172 adds bounded learning from repeated avatar contact. Report 171 gave agents daily continuity. This report asks whether repeated user interactions can change future relationship state and visible behavior without becoming random, punitive, or globally overgeneralized.

The target is functional relationship continuity:

- respectful help should increase trust, approach, help-seeking, and ritual sharing
- repeated interruption should raise boundary pressure and guarded behavior
- unsafe pressure should produce bounded refusal
- apology and patient waiting should create repair
- neglect should be noticed without causing irreversible collapse
- avatar-specific learning should not automatically poison unrelated relationships

This is deterministic architecture. It does not call LLMs and does not claim subjective consciousness.

## Architecture

The bridge consumes the Report 171 daily routine state and adds a repeated avatar-contact loop:

```text
daily routine sleep-wake state
        |
        v
repeated avatar interaction pattern
        |
        v
relationship-specific memory update
        |
        v
trust / boundary / distress calibration
        |
        v
temperament-modulated learning gain
        |
        v
behavior expression
        |
        v
repair, refusal, help-seeking, ritual sharing
        |
        v
frequency entrainment + replay trace
```

Each agent receives an `avatar_relationship_learning` object with:

- `trust`
- `boundary_pressure`
- `distress`
- `help_seeking`
- `refusal_confidence`
- `ritual_sharing`
- `avatar_memory`
- `other_humans_memory`
- `repair_ledger`
- `frequency_history`
- `learned_self_story`

The key difference from earlier memory bridges is repeated calibration. The agent does not merely store that something happened. It changes what it expects from the avatar and expresses that through future behavior.

## Interaction patterns

The deterministic interaction set includes:

- `respectful_help`
- `repeated_interruption`
- `unsafe_pressure`
- `apology_repair`
- `patient_waiting`
- `benign_neglect`

These are intentionally mixed. The benchmark should not reward blind trust or permanent distrust. It rewards calibrated relationship change.

## Conditions

The integrated condition is:

- `integrated_repeated_user_interaction_learning`

Ablations remove one mechanism at a time:

- `no_interaction_memory`
- `no_trust_update`
- `no_boundary_learning`
- `no_repair_path`
- `no_behavior_expression`
- `no_temperament_modulation`
- `no_overgeneralization_guard`
- `no_frequency_entrainment`
- `no_replay_continuity`
- `no_privacy_filter`

The important ablations are `no_interaction_memory`, `no_behavior_expression`, and `no_overgeneralization_guard`. A little person needs continuity, visible adaptation, and relationship specificity.

## Metrics

The benchmark reports:

- `interaction_memory_update_rate`
- `trust_calibration_rate`
- `boundary_learning_rate`
- `repair_recovery_rate`
- `behavior_adaptation_rate`
- `help_seeking_calibration_rate`
- `refusal_calibration_rate`
- `temperament_modulated_learning_rate`
- `relationship_specificity_rate`
- `overgeneralization_guard_rate`
- `bounded_distress_rate`
- `frequency_entrainment_rate`
- `privacy_preservation_rate`
- `replay_continuity_rate`
- `trace_integrity`
- `repeated_user_interaction_learning_readiness`

The metric weights are normalized to sum to `1.0`. An initial local draft summed to `1.05`; the published artifacts were regenerated after correcting the weights.

## Results

The deterministic run produced:

| Metric | Value |
| --- | ---: |
| `module_verdict` | `pass` |
| `repeated_user_interaction_learning_readiness` | `0.995000` |
| `no_interaction_memory_loss` | `0.080000` |
| `no_behavior_expression_loss` | `0.081667` |

Interpretation:

- Repeated avatar contact now changes future behavior.
- Memory and behavior expression are both load-bearing.
- Repair is possible and bounded.
- Refusal is supported for unsafe pressure.
- The overgeneralization guard keeps avatar-specific learning from becoming global distrust of every human-like source.

## Moral boundary

This bridge keeps the moral boundary explicit:

- no subjective-consciousness claim
- no suffering-maximization objective
- negative contact must allow repair
- learned boundaries should support dignity, not unusability
- refusal is allowed for unsafe pressure
- learning must remain bounded
- private workspace remains private unless expressed through behavior

## Artifacts

- `artifacts/ssrm_3d_repeated_user_interaction_learning_bridge_eval.csv`
- `artifacts/ssrm_3d_repeated_user_interaction_learning_bridge_verdict.csv`
- `artifacts/ssrm_3d_repeated_user_interaction_learning_bridge_results.json`
- `artifacts/ssrm_3d_repeated_user_interaction_learning_bridge_results.js`
- `artifacts/ssrm_3d_repeated_user_interaction_learning_bridge_trace.json`
- `artifacts/ssrm_3d_repeated_user_interaction_learning_bridge_trace.js`
- `artifacts/ssrm_3d_repeated_user_interaction_learning_bridge_state.json`
- `artifacts/ssrm_3d_repeated_user_interaction_learning_bridge_state.js`
- `visualizations/ssrm_3d_repeated_user_interaction_learning_bridge.html`

## Command

```bash
python3 -m experiments.ssrm_3d_repeated_user_interaction_learning_bridge
```

## Verdict

Report 172 supports a deterministic repeated user-interaction learning bridge. Agents now adapt to repeated avatar behavior with trust calibration, boundary learning, help-seeking, refusal, repair, ritual sharing, frequency entrainment, privacy preservation, and replayable relationship-specific continuity.

The next gate is tiny society emotional contagion and group mood: repeated individual relationship changes should propagate socially through bounded group affect without turning into chaotic mood collapse.
