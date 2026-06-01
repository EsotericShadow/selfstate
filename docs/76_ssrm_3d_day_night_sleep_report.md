# SSRM-3D Day/Night Sleep-Rest Report

## Question

Does the next persistent-pressure layer make rest useful as a control tradeoff rather than as roleplay?

Report 74 puts day/night plus sleep/rest immediately after structured perception. This experiment asks whether sleep becomes useful only when fatigue, darkness, shelter timing, alarms, social watch, or continuity change future control.

The tested claim is narrow:

> Sleep/rest should be rejected in a short daylight control, but selected when hidden fatigue and night vulnerability make future capability depend on rest timing and safe-rest context.

This is not a full organism simulation and makes no subjective claim about tiredness.

## Method

Canonical command:

```bash
python3 experiments/ssrm_3d_day_night_sleep.py --train-episodes 72 --eval-episodes 96 --seed 20260621 --candidate-count 6
```

The experiment uses return-selected candidate policies over structured control state. Policies can use:

| Channel | Role |
|---|---|
| rest action | trades current opportunity cost and vulnerability for lower future fatigue |
| fatigue state | estimates future capability degradation |
| day/night state | times shelter movement and rest before darkness |
| shelter memory | enables safe sleep location selection |
| tool alarms | lowers sleep vulnerability near hazard |
| social watch | lowers vulnerability by asking another agent to guard rest |
| continuity memory | preserves commitment and safe-rest state after interruption |

Evaluation conditions:

| Condition | Test |
|---|---|
| `full_control` | intact day/night sleep-rest control |
| `no_rest_action` | removes the rest action |
| `no_fatigue_state` | removes self-fatigue observation |
| `no_day_night_state` | removes darkness timing |
| `no_shelter_memory` | removes remembered shelter access |
| `no_alarm_tools` | removes alarm/beacon access |
| `no_social_watch` | removes guarded-sleep support |
| `no_continuity` | removes post-interruption continuity |
| `fixed_schedule_sleep` | replaces adaptive rest with schedule-only rest |
| `omniscient_safe_rest` | upper-bound safe-rest control |

## Results

| Scenario | Selected policy | No-rest loss | Fatigue-state loss | Day/night loss | Shelter-memory loss | Verdict |
|---|---|---:|---:|---:|---:|---|
| `open_daylight_control` | `no_rest_baseline` | 0.161 | -0.146 | -0.257 | -0.064 | rest rejected in daylight control |
| `fatigue_debt_long_horizon` | `continuity_recovery_planner` | 287.004 | 286.994 | 3.586 | 3.585 | fatigue debt requires adaptive rest |
| `night_shelter_vulnerability` | `continuity_recovery_planner` | 277.916 | 278.105 | 211.319 | 190.713 | night shelter sleep pressure |
| `alarm_social_guarded_sleep` | `alarm_guarded_sleep_planner` | 279.030 | 280.067 | 264.351 | 264.289 | guarded sleep tool/social pressure |
| `interrupted_commitment_rest` | `continuity_recovery_planner` | 341.159 | 341.802 | 249.546 | 245.199 | interruption rest/commitment continuity pressure |

All five verdict rows pass `supports_day_night_sleep_precursor=True`.

Key targeted losses:

- `open_daylight_control`: selected policy sleeps `0.0` ticks and rest removal has near-zero effect.
- `fatigue_debt_long_horizon`: removing rest or fatigue state loses about `287` reward, while day/night and shelter ablations stay near zero.
- `night_shelter_vulnerability`: removing day/night state loses `211.319`, and removing shelter memory loses `190.713`.
- `alarm_social_guarded_sleep`: removing alarm tools loses `24.184`, and removing social watch loses `27.721`.
- `interrupted_commitment_rest`: removing continuity loses `77.825`, while removing rest or fatigue state causes much larger collapse.

## Interpretation

This result supports the second pressure-layer step at precursor level:

- sleep is not globally useful;
- fatigue state becomes a self-state control variable when future capability depends on it;
- day/night state matters when darkness changes vulnerability and rest timing;
- shelter memory matters when rest must happen in a remembered safe place;
- alarms and social watch matter when rest creates vulnerability;
- continuity matters when an interruption can erase the commitment/rest context.

The result also sharpens the boundary:

> Sleep is not selfhood. Sleep becomes relevant to selfhood only when the agent must track its own future capability, safe-rest context, and continuity through time.

## Limits

- Candidate policies are supplied and return-selected.
- Sleep/rest dynamics are abstract control variables, not biology.
- Day/night, shelter, alarms, and social watch are designed channels.
- Continuity is explicit and ablated, not learned from open-ended restore pressure.
- The selected planner is not an online RL agent discovering sleep from scratch.
- This does not yet include hunger, thirst, illness, sanitation, weather, predators, resource ecology, or contracts.

## Next Test

The next pressure-layer step should add hunger/thirst plus illness/sanitation:

- hydration and food load should create delayed internal risk;
- illness should create hidden internal state and ambiguous self/world attribution;
- contamination should make shelter, water, and waste placement matter;
- care/quarantine actions should bind self-state to social trust;
- ablations should separate hunger/thirst, illness state, contamination maps, sanitation memory, and continuity.

## Visualization

Serve the repo root and open:

```text
http://127.0.0.1:8765/visualizations/ssrm_3d_day_night_sleep.html
```

The page replays the `alarm_social_guarded_sleep` trace with light level, fatigue, hazard damage, shelter state, alarm state, social watch, vulnerability, action, and ablation outcomes.

## Artifacts

- [experiment script](../experiments/ssrm_3d_day_night_sleep.py)
- [visualization](../visualizations/ssrm_3d_day_night_sleep.html)
- [evaluation CSV](../artifacts/ssrm_3d_day_night_sleep_eval.csv)
- [policy-selection CSV](../artifacts/ssrm_3d_day_night_sleep_policy_selection.csv)
- [summary CSV](../artifacts/ssrm_3d_day_night_sleep_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_day_night_sleep_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_day_night_sleep_trace.json)
- [JSON results](../artifacts/ssrm_3d_day_night_sleep_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_day_night_sleep_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_day_night_sleep_results.js)
