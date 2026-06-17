# Report 188: SSRM-3D Embodied Illness, Immune Recovery, Care Triage, and Quarantine Choices Bridge

## Summary

Report 188 adds a deterministic embodied-health layer on top of Report 187's ecological regeneration, spoilage, waste, and sanitation substrate. The bridge binds ecological exposure to agent body state, progresses functional illness variables, expresses readable symptom markers, allocates clean-water and rest care, applies immune recovery, chooses bounded quarantine, modulates social access, and exports replayable health traces for browser inspection.

The result is a health-state seed for playable artificial life. It is not a claim of subjective illness, suffering, consciousness, moral patienthood, or complete 3D gameplay.

## Why this report exists

Reports 180 through 187 made the world increasingly playable and persistent: traversal, objects, promises, routines, planning, economy, craft wear, and ecological sanitation. The next missing body consequence was illness-like functional state. If sanitation, contaminated water, spoilage, and waste can affect future behavior, agents need a body-level health channel that can become impaired, receive care, recover, and temporarily change social access without turning distress into spectacle.

This report therefore adds:

- ecological exposure binding from water, waste, spoilage, and habitat risk
- infection load, fever, fatigue, hydration, immune strength, contagiousness, and quarantine state
- readable symptom markers from mild body degradation, not only severe infection
- care triage, clean-water care, rest slots, and immune recovery
- temporary quarantine and contagion containment
- social-access modulation during health risk
- privacy-preserving replay events that hide private health internals while exposing public behavior markers
- deterministic ablations showing that exposure, care triage, immune recovery, and quarantine choices are load-bearing

## Design boundary

The moral boundary is explicit:

- Health risk is a functional control state, not subjective illness.
- Quarantine is temporary protective separation, not punishment.
- Distress-like health pressure must create care opportunities and recovery paths.
- The system does not optimize for suffering-like states.
- Private health details remain hidden unless expressed through public markers.
- No result here supports subjective consciousness, moral patienthood, or complete playable-world claims.

## Implementation

The benchmark lives in:

- `experiments/ssrm_3d_embodied_illness_immune_care_quarantine_bridge.py`
- `visualizations/ssrm_3d_embodied_illness_immune_care_quarantine_bridge.html`

It consumes the Report 187 state artifact:

- `artifacts/ssrm_3d_ecological_regeneration_spoilage_waste_sanitation_bridge_state.json`

For each deterministic day and agent tick, the loop performs:

1. sample ecological exposure from food, water, waste, compost, and habitat nodes
2. update infection load from exposure, immunity, and quarantine containment
3. express readable symptom markers from infection, fatigue, or hydration pressure
4. compute care triage priority from infection, fever, fatigue, and hydration
5. allocate clean water and rest when triage is active
6. apply immune recovery through care-amplified recovery and bounded spontaneous recovery
7. choose temporary quarantine from infection or triage context
8. reduce contagiousness under containment
9. modulate social access without treating quarantine as social punishment
10. apply health guardrails and privacy-preserving replay packets

The scoring was deliberately corrected during implementation. Early versions wrongly rewarded more raw sickness, so the `no_immune_recovery` ablation could look better merely because it produced more symptoms, quarantine, and triage events. The final benchmark scores care and quarantine as calibrated-success channels: active intervention under risk, and deliberate non-intervention when the agent is safely recovered. This prevents the benchmark from confusing unresolved illness with better health modeling.

## Metrics

The benchmark reports:

- `ecological_exposure_binding_rate`
- `illness_progression_rate`
- `symptom_expression_rate`
- `immune_recovery_rate`
- `care_triage_rate`
- `quarantine_choice_rate`
- `contagion_containment_rate`
- `clean_water_care_rate`
- `rest_recovery_coupling_rate`
- `sanitation_feedback_binding_rate`
- `social_access_modulation_rate`
- `health_guardrail_rate`
- `frequency_flower_health_binding_rate`
- `browser_health_replay_rate`
- `privacy_preservation_rate`
- `trace_integrity`
- `embodied_health_readiness`

## Deterministic run

Command:

```bash
python3 -m experiments.ssrm_3d_embodied_illness_immune_care_quarantine_bridge
```

Observed output:

```text
module_verdict pass
embodied_health_readiness 0.975185
health_events 27
no_exposure_binding_loss 0.129629
no_care_triage_loss 0.515185
no_quarantine_choices_loss 0.150741
```

## Artifacts

Generated artifacts:

- `artifacts/ssrm_3d_embodied_illness_immune_care_quarantine_bridge_eval.csv`
- `artifacts/ssrm_3d_embodied_illness_immune_care_quarantine_bridge_verdict.csv`
- `artifacts/ssrm_3d_embodied_illness_immune_care_quarantine_bridge_results.json`
- `artifacts/ssrm_3d_embodied_illness_immune_care_quarantine_bridge_results.js`
- `artifacts/ssrm_3d_embodied_illness_immune_care_quarantine_bridge_trace.json`
- `artifacts/ssrm_3d_embodied_illness_immune_care_quarantine_bridge_trace.js`
- `artifacts/ssrm_3d_embodied_illness_immune_care_quarantine_bridge_state.json`
- `artifacts/ssrm_3d_embodied_illness_immune_care_quarantine_bridge_state.js`

## Interpretation

The pass means the deterministic health bridge now has a working causal shape:

- ecological exposure affects body state
- visible symptom markers appear without requiring severe illness
- care triage, water, rest, and immune recovery are connected
- quarantine choices reduce social exposure and support containment
- removing care triage or quarantine materially damages readiness
- removing immune recovery no longer appears better merely because it creates more unresolved sickness

This is still a seeded simulation bridge. It does not yet include medicine craft, chronic conditions, learned health policy, rich contagious contact networks, user-driven care in the browser, or unscripted long-horizon recovery behavior.

## Next gate

The next useful gate is playable care intervention and medicine practice: let the browser avatar offer water, rest space, cleaning, herbs/tools, or social distance, and test whether agents accept, refuse, remember, recover, or revise trust from those health interactions.
