# SSRM-3D Illness/Sanitation Report

## Question

Does hunger/thirst plus illness/sanitation create persistent self-state pressure without turning the world into roleplay biology?

Report 74 puts hunger/thirst plus illness/sanitation after structured perception and sleep/rest. This experiment asks whether hidden internal risk, contamination, exposure, care, quarantine, immunity, and continuity become useful control variables only when they change future options.

The tested claim is narrow:

> Health machinery should be rejected in a clean resource control, but selected when delayed need, latent illness, contamination, contagion, or restore-time immunity history changes future control.

This is not a full organism simulation and makes no subjective claim about sickness.

## Method

Canonical command:

```bash
python3 experiments/ssrm_3d_illness_sanitation.py --train-episodes 72 --eval-episodes 96 --seed 20260622 --candidate-count 6
```

The experiment uses return-selected candidate policies over abstract control state. Policies can use:

| Channel | Role |
|---|---|
| hunger/thirst state | estimates hydration and food-load collapse risk |
| illness state | separates latent infection from external failure |
| contamination map | remembers dirty water, food, and shelter conditions |
| sanitation action | reduces future pathogen exposure |
| clean-water tools | trades time for safer hydration |
| care/quarantine | reduces social exposure and preserves trust |
| immunity memory | preserves past infection/recovery information |
| continuity memory | preserves exposure, contamination, quarantine, and immunity state after restore |

Evaluation conditions:

| Condition | Test |
|---|---|
| `full_control` | intact illness/sanitation control |
| `no_health_state` | removes health machinery as a broad baseline |
| `no_hunger_thirst_state` | removes hydration and food-load observation |
| `no_illness_state` | removes infection/symptom attribution |
| `no_contamination_map` | removes sanitation-relevant spatial memory |
| `no_sanitation_action` | removes shelter cleaning |
| `no_clean_water_tools` | removes safe hydration tools |
| `no_care_quarantine` | removes warning, care, and quarantine behavior |
| `no_immunity_memory` | removes past exposure/recovery memory |
| `no_continuity` | removes restore-time exposure and sanitation continuity |
| `symptom_reactive_only` | waits for visible symptoms instead of hidden-state control |
| `omniscient_health_control` | upper-bound health-state control |

## Results

| Scenario | Selected policy | Need loss | Illness loss | Contamination loss | Care loss | Verdict |
|---|---|---:|---:|---:|---:|---|
| `clean_resource_control` | `no_health_baseline` | 0.027 | 0.036 | -0.035 | -0.044 | health rejected in clean control |
| `hunger_thirst_delayed_need` | `need_reactive_forager` | 187.687 | 0.009 | 0.009 | 0.000 | hunger/thirst need-state pressure |
| `latent_illness_attribution` | `quarantine_care_planner` | 72.730 | 128.838 | -0.724 | -0.959 | latent illness attribution pressure |
| `contaminated_shelter_water` | `quarantine_care_planner` | 119.420 | 145.937 | 29.028 | -1.330 | contamination/sanitation/clean-water pressure |
| `contagion_quarantine_care` | `quarantine_care_planner` | 130.593 | 294.448 | -0.538 | 103.921 | contagion quarantine/care pressure |
| `immunity_restore_continuity` | `immunity_continuity_planner` | 134.123 | 109.813 | 25.291 | -0.137 | immunity/exposure continuity pressure |

All six verdict rows pass `supports_illness_sanitation_precursor=True`.

Key targeted losses:

- `clean_resource_control`: health machinery is not selected and broad health removal has near-zero effect.
- `hunger_thirst_delayed_need`: removing hunger/thirst state loses `187.687`; illness and contamination ablations stay near zero.
- `latent_illness_attribution`: removing illness state loses `128.838`; symptom-reactive-only control loses `105.985`.
- `contaminated_shelter_water`: removing contamination map loses `29.028`, sanitation action loses `18.088`, and clean-water tools lose `21.668`.
- `contagion_quarantine_care`: removing care/quarantine loses `103.921`.
- `immunity_restore_continuity`: removing immunity memory loses `21.343`, and removing continuity loses `43.131`.

## Interpretation

This result supports the third pressure-layer step at precursor level:

- health state is not globally useful;
- hunger/thirst becomes self-state pressure when delayed internal collapse risk matters;
- latent illness creates an error-attribution problem distinct from terrain/tool failure;
- contamination and sanitation matter when dirty places create future pathogen risk;
- clean-water tools become useful when hydration and exposure compete;
- quarantine/care matters when the agent can expose or preserve a helper;
- immunity and continuity matter when restore can erase exposure/recovery history.

The result also sharpens the boundary:

> Illness is not selfhood. Illness becomes relevant to selfhood only when the agent must model hidden internal state, delayed consequences, what it can safely do, and what risk it poses to others.

Some selected policies carry extra channels whose ablations are neutral or negative in that row. Those are not positive evidence for those channels. The evidence comes only from targeted losses in matching regimes.

## Limits

- Candidate policies are supplied and return-selected.
- Health dynamics are abstract control variables, not biology.
- Contamination, clean-water tools, care, quarantine, and immunity are designed channels.
- The selected planner is not an online RL agent discovering illness/sanitation from scratch.
- Social care is simplified to one helper/trust channel, not a real social ecology.
- This does not yet include weather/exposure, tool/shelter degradation, contracts, predators, or resource ecology.

## Next Test

The next pressure-layer step should add weather/exposure:

- cold/heat/rain should change shelter, hydration, illness, and sleep safety;
- weather should make tool caches and shelter maintenance useful;
- ablations should separate weather state, exposure state, shelter quality, clothing/tool protection, and continuity.

## Visualization

Serve the repo root and open:

```text
http://127.0.0.1:8765/visualizations/ssrm_3d_illness_sanitation.html
```

The page replays the `contaminated_shelter_water` trace with hydration, food, pathogen load, symptoms, immunity, contamination, social trust, actions, and ablation outcomes.

## Artifacts

- [experiment script](../experiments/ssrm_3d_illness_sanitation.py)
- [visualization](../visualizations/ssrm_3d_illness_sanitation.html)
- [evaluation CSV](../artifacts/ssrm_3d_illness_sanitation_eval.csv)
- [policy-selection CSV](../artifacts/ssrm_3d_illness_sanitation_policy_selection.csv)
- [summary CSV](../artifacts/ssrm_3d_illness_sanitation_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_illness_sanitation_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_illness_sanitation_trace.json)
- [JSON results](../artifacts/ssrm_3d_illness_sanitation_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_illness_sanitation_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_illness_sanitation_results.js)
