# Report 207: SSRM-3D Long-Horizon Personality, Routines, and Avatar Reputation Bridge

## Purpose

Report 207 extends persistent dialogue memory into playable-day continuity. The target is a stronger little-person substrate: agents should not merely remember a prior sentence, but carry temperament, routines, body needs, refusal history, repair history, and avatar reputation across multiple days.

This is still a deterministic bridge. It does not claim real memory, real consent, subjective consciousness, moral patienthood, or complete artificial life.

## What changed

The bridge adds:

- stable personality vectors for Ari, Fay, and Milo
- daily routine anchors across dawn, midday, evening, and night
- body-need coupling for dry routes, warmth, quiet, rest, object security, and personal space
- remembered avatar reputation keys such as `gives_space`, `returns_objects`, `asks_first`, `protects_ownership`, and `respects_rest`
- refusal history that remains usable across days
- bounded recovery after a missed/late routine
- social reputation echo, where agents hear another agent's avatar memory but check it against their own history
- novelty handling without flattening each agent into generic compliance
- public/private separation through sealed private workspace digests
- frequency and flower-ring day rhythm for each event
- browser replay of the multi-day continuity trace

## Deterministic scenario

The run spans eight playable days and twenty-four events.

- Day 1: baseline after persistent dialogue memory.
- Day 2: rain pressure forces body-linked route, warmth, and quiet choices.
- Day 3: avatar reputation starts predicting interaction.
- Day 4: a late Fay check-in creates a bounded repair path rather than a perfect trace.
- Day 5: agents initiate from remembered reputation instead of waiting passively.
- Day 6: fatigue and sleep-wake refusals constrain useful tasks.
- Day 7: social reputation echoes across agents without overriding individual memory.
- Day 8: amber-fog novelty tests whether temperament survives unfamiliar conditions.

## Metrics

| Metric | Value |
| --- | ---: |
| long_horizon_playday_readiness | 0.987351 |
| playable_days | 8 |
| playday_events | 24 |
| personality_stability_score | 1.000000 |
| routine_continuity_rate | 0.958333 |
| avatar_reputation_recall_rate | 1.000000 |
| remembered_promise_reuse_rate | 1.000000 |
| refusal_consistency_rate | 1.000000 |
| trust_repair_across_days | 1.000000 |
| body_need_routine_coupling | 1.000000 |
| sleep_wake_cycle_binding | 0.958333 |
| social_ripple_consistency | 1.000000 |
| novelty_without_personality_drift | 1.000000 |
| public_private_boundary_score | 1.000000 |
| frequency_flower_day_rhythm | 1.000000 |
| memory_summary_traceability | 0.906250 |
| browser_playday_replay_available | 1.000000 |

The imperfect routine and sleep/wake scores are deliberate. Fay's late check-in is retained as a relationship event that can be repaired. The benchmark should preserve timing damage when it happens, not erase it to make the bridge look solved.

## Ablations

| Ablation | Readiness loss |
| --- | ---: |
| no_personality_vectors | 0.310000 |
| no_daily_routines | 0.280000 |
| no_avatar_reputation | 0.260000 |
| no_body_need_coupling | 0.180000 |
| no_refusal_repair_history | 0.155000 |
| no_sleep_wake_cycle | 0.125000 |
| no_social_ripple | 0.090000 |
| no_frequency_flower_day_rhythm | 0.060000 |

The largest losses come from removing personality vectors, routines, and avatar reputation. That is the expected result: without those three, agents stop feeling like continuing individuals and collapse back into reactive state machines.

## Artifacts

- `artifacts/ssrm_3d_long_horizon_personality_routines_avatar_reputation_bridge_events.csv`
- `artifacts/ssrm_3d_long_horizon_personality_routines_avatar_reputation_bridge_daily_summary.csv`
- `artifacts/ssrm_3d_long_horizon_personality_routines_avatar_reputation_bridge_agent_profiles.csv`
- `artifacts/ssrm_3d_long_horizon_personality_routines_avatar_reputation_bridge_reputation_ledger.csv`
- `artifacts/ssrm_3d_long_horizon_personality_routines_avatar_reputation_bridge_results.json`
- `artifacts/ssrm_3d_long_horizon_personality_routines_avatar_reputation_bridge_state.json`
- `artifacts/ssrm_3d_long_horizon_personality_routines_avatar_reputation_bridge_verdict.csv`
- `visualizations/ssrm_3d_long_horizon_personality_routines_avatar_reputation_bridge.html`

## Run command

```bash
python3 -m experiments.ssrm_3d_long_horizon_personality_routines_avatar_reputation_bridge --seed 20260820 --days 8
```

Observed output:

```text
module_verdict pass
long_horizon_playday_readiness 0.987351
playable_days 8
playday_events 24
routine_continuity_rate 0.958333
sleep_wake_cycle_binding 0.958333
next_gate agent calendar commitments, object projects, and reputation consequences that survive longer playable arcs
```

## Honest limitation

This report proves deterministic multi-day continuity wiring, not real life. The agents have scripted event conditions and bounded state updates. They do not freely understand language, form subjective experiences, or possess moral patienthood. Avatar reputation is a functional ledger, not genuine social judgment. The private workspace remains represented by a sealed digest rather than a lived inner perspective.

## Next gate

The next gate is agent calendar commitments, object projects, and reputation consequences that survive longer playable arcs.
