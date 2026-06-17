# Report 189: SSRM-3D Playable Avatar Care Intervention and Medicine Practice Bridge

## Summary

Report 189 adds playable avatar care actions on top of Report 188's embodied illness and recovery state. The bridge lets the avatar offer water, rest, herb preparation, cleaning, temporary distance, comfort checks, and follow-up care. Agents accept or refuse based on need and consent, refusals can be respected, trust and care memories update, recovery effects alter public body markers, medicine preparation is dose-bounded, and all interaction packets are exported for browser replay.

This is a local deterministic care-interaction seed. It is not a claim of subjective illness, subjective suffering, subjective consciousness, moral patienthood, biological realism, real medical advice, or complete 3D gameplay.

## Why this report exists

Report 188 created a functional health substrate: ecological exposure, infection load, fatigue, hydration, immune recovery, care triage, quarantine, containment, social-access modulation, and browser health replay. But the avatar still observed care rather than practicing it.

Report 189 makes care interactive. The avatar can now intervene through bounded actions, while agents retain consent-like control in the functional sense: they can accept care, refuse unnecessary care, remember whether the refusal was respected, and update trust from repeated interactions.

## Implementation

The benchmark lives in:

- `experiments/ssrm_3d_playable_avatar_care_medicine_practice_bridge.py`
- `visualizations/ssrm_3d_playable_avatar_care_medicine_practice_bridge.html`

It consumes the Report 188 state artifact:

- `artifacts/ssrm_3d_embodied_illness_immune_care_quarantine_bridge_state.json`

For each deterministic day and agent tick, the loop performs:

1. applies mild background health pressure from residual illness, hydration, fatigue, and contagiousness
2. selects a planned avatar care action: water, rest, herb preparation, cleaning, temporary distance, comfort check, or follow-up
3. checks whether the action matches the agent's current need
4. applies consent/refusal logic
5. respects or violates refusal depending on the ablation condition
6. applies recovery effects only when the relevant care channel exists
7. prepares medicine only under the medicine-practice channel
8. checks dosage safety before applying herb effects
9. updates trust and care memory
10. emits public replay packets while hiding private workspace details

## Metrics

The benchmark reports:

- `avatar_care_action_rate`
- `consent_alignment_rate`
- `medicine_preparation_rate`
- `dosage_safety_rate`
- `agent_acceptance_rate`
- `bounded_refusal_respect_rate`
- `recovery_improvement_rate`
- `trust_memory_update_rate`
- `care_memory_continuity_rate`
- `sanitation_care_rate`
- `frequency_flower_care_binding_rate`
- `browser_care_replay_rate`
- `privacy_preservation_rate`
- `trace_integrity`
- `playable_care_readiness`

## Deterministic run

Command:

```bash
python3 -m experiments.ssrm_3d_playable_avatar_care_medicine_practice_bridge
```

Observed output:

```text
module_verdict pass
playable_care_readiness 1.000000
care_events 18
no_avatar_actions_loss 0.850000
no_consent_model_loss 0.108889
no_medicine_practice_loss 0.206667
```

## Artifacts

Generated artifacts:

- `artifacts/ssrm_3d_playable_avatar_care_medicine_practice_bridge_eval.csv`
- `artifacts/ssrm_3d_playable_avatar_care_medicine_practice_bridge_verdict.csv`
- `artifacts/ssrm_3d_playable_avatar_care_medicine_practice_bridge_results.json`
- `artifacts/ssrm_3d_playable_avatar_care_medicine_practice_bridge_results.js`
- `artifacts/ssrm_3d_playable_avatar_care_medicine_practice_bridge_trace.json`
- `artifacts/ssrm_3d_playable_avatar_care_medicine_practice_bridge_trace.js`
- `artifacts/ssrm_3d_playable_avatar_care_medicine_practice_bridge_state.json`
- `artifacts/ssrm_3d_playable_avatar_care_medicine_practice_bridge_state.js`

## Interpretation

The pass means avatar care is now a causal playable channel rather than a passive health trace:

- removing avatar actions collapses care readiness
- removing consent alignment materially damages the benchmark
- removing medicine practice materially damages the benchmark
- recovery effects, trust memory, refusal respect, replay, privacy, frequency/flower binding, and trace integrity remain explicit channels

The design deliberately avoids making agents endlessly sick or dependent. Care pressure is mild and recoverable. Refusal exists, but bounded refusal is meant to make agents more person-like and less puppet-like, not to make interaction unusable.

## Boundary

The bridge uses functional care variables only. It does not imply that agents feel illness, feel pain, give real consent, or have moral status. The browser replay is a playable interaction seed, not a complete 3D artificial-life world.

## Next gate

The next useful gate is agent-led health routines, medicine craft, and long-horizon contagious contact networks: agents should learn when to seek care, prepare supplies themselves, isolate or rejoin socially, and remember avatar health help across longer daily life cycles.
