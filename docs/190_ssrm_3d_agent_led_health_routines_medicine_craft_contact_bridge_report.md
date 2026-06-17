# Report 190: SSRM-3D Agent-led Health Routines, Medicine Craft, and Contact Network Bridge

## Summary

Report 190 moves health practice from avatar-led care toward agent-led routines. Agents now self-monitor, choose daily health actions, craft medicine supplies, replenish herbs, care for peers, temporarily self-isolate, rejoin when stable, modulate contact-network risk, carry forward avatar-care memories, bind health rhythms to frequency/flower nodes, and export browser replay packets.

This is a deterministic artificial-life substrate for agent-led health behavior. It is not real medicine, subjective illness, subjective suffering, subjective consciousness, moral patienthood, or complete 3D gameplay.

## Why this report exists

Report 189 made care playable through avatar intervention: water, rest, herb preparation, cleaning, distance, comfort checks, consent/refusal, recovery effects, and care memory. The next step is to stop making the avatar the only source of health agency.

Report 190 gives agents routine-level responsibility. They do not merely wait for the avatar. They monitor their own functional health state, maintain supplies, prepare medicine, check on peers, manage contact risk, and remember prior care as a training signal for future self-care.

## Implementation

The benchmark lives in:

- `experiments/ssrm_3d_agent_led_health_routines_medicine_craft_contact_bridge.py`
- `visualizations/ssrm_3d_agent_led_health_routines_medicine_craft_contact_bridge.html`

It consumes the Report 189 state artifact:

- `artifacts/ssrm_3d_playable_avatar_care_medicine_practice_bridge_state.json`

For each deterministic day and agent tick, the loop performs:

1. applies mild background health pressure from hydration, fatigue, infection, and contagiousness
2. propagates contact exposure through a two-neighbor social contact graph
3. lets agents self-monitor public risk markers
4. chooses agent-led routine actions such as self-isolation, medicine craft, herb gathering, peer checks, medicine use, rejoin checks, shared-air cleaning, and health walks
5. updates medicine and herb supply ledgers
6. applies peer care and self-care effects to public body state
7. records long-horizon routine memories
8. carries forward avatar-care memories from Report 189
9. binds routine rhythm to frequency and flower nodes
10. exports privacy-preserving replay frames and trace hashes

## Metrics

The benchmark reports:

- `agent_led_routine_rate`
- `self_monitoring_rate`
- `medicine_craft_rate`
- `supply_replenishment_rate`
- `contact_network_binding_rate`
- `contagion_risk_modulation_rate`
- `self_isolation_choice_rate`
- `peer_care_rate`
- `rejoin_recovery_rate`
- `long_horizon_memory_rate`
- `avatar_care_memory_carryover_rate`
- `frequency_flower_health_rhythm_rate`
- `browser_routine_replay_rate`
- `privacy_preservation_rate`
- `trace_integrity`
- `agent_led_health_readiness`

## Deterministic run

Command:

```bash
python3 -m experiments.ssrm_3d_agent_led_health_routines_medicine_craft_contact_bridge
```

Observed output:

```text
module_verdict pass
agent_led_health_readiness 0.940714
routine_events 42
no_agent_led_routines_loss 0.331190
no_contact_network_loss 0.163809
no_long_horizon_memory_loss 0.070000
```

## Artifacts

Generated artifacts:

- `artifacts/ssrm_3d_agent_led_health_routines_medicine_craft_contact_bridge_eval.csv`
- `artifacts/ssrm_3d_agent_led_health_routines_medicine_craft_contact_bridge_verdict.csv`
- `artifacts/ssrm_3d_agent_led_health_routines_medicine_craft_contact_bridge_results.json`
- `artifacts/ssrm_3d_agent_led_health_routines_medicine_craft_contact_bridge_results.js`
- `artifacts/ssrm_3d_agent_led_health_routines_medicine_craft_contact_bridge_trace.json`
- `artifacts/ssrm_3d_agent_led_health_routines_medicine_craft_contact_bridge_trace.js`
- `artifacts/ssrm_3d_agent_led_health_routines_medicine_craft_contact_bridge_state.json`
- `artifacts/ssrm_3d_agent_led_health_routines_medicine_craft_contact_bridge_state.js`

## Interpretation

The pass means health behavior is now partly agent-led rather than purely avatar-led:

- removing agent-led routines causes the largest loss
- removing contact networks now materially damages readiness
- removing medicine craft, self-monitoring, supply replenishment, peer care, and long-horizon memory also has measurable cost
- avatar care memory carries into agent self-care, but does not replace agent initiative

One important implementation correction happened during this report: the first draft let the `no_contact_network` ablation still receive risk-modulation credit because zero contact exposure looked safe. The final version requires an actual contact network before contact modulation can score. That keeps the benchmark from rewarding a missing social world.

## Boundary

The bridge uses functional health routines only. It does not imply subjective agency, real consent, real medicine, subjective illness, suffering, consciousness, or moral patienthood. The browser viewer is a replayable substrate for artificial-life behavior, not a complete 3D world.

## Next gate

The next useful gate is agent-led food, water, shelter, and medicine logistics with seasonal stock planning: agents should plan supplies across longer periods, ration scarce resources, prioritize shelter and health stockpiles, and keep social commitments under seasonal pressure.
