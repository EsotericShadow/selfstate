# SSRM-3D Weather/Exposure Report

## Question

Does weather/exposure create persistent control pressure without turning the world into a climate simulator?

Report 74 puts weather/exposure after structured perception, sleep/rest, and illness/sanitation. This experiment asks whether cold, heat, rain, wind, drought, shelter timing, fire/light tools, water planning, and restore continuity become useful only when they change future options.

The tested claim is narrow:

> Weather machinery should be rejected in mild clear control, but selected when forecast, accumulated exposure, shelter, fire/light, water planning, or restore continuity changes future control.

This is not a full weather system and makes no subjective claim about discomfort.

## Method

Canonical command:

```bash
python3 experiments/ssrm_3d_weather_exposure.py --train-episodes 72 --eval-episodes 96 --seed 20260623 --candidate-count 6
```

The experiment uses return-selected candidate policies over abstract control state. Policies can use:

| Channel | Role |
|---|---|
| weather state | reads current and forecast cold, heat, rain, wind, and storm risk |
| exposure state | tracks accumulated body exposure distinct from outside weather |
| shelter memory | moves to shelter before or during unsafe weather |
| fire/light tools | trades time for warmth, light, and safer shelter work |
| water planning | preserves hydration under heat and drought |
| continuity memory | preserves shelter/fire/forecast state through restore |

Evaluation conditions:

| Condition | Test |
|---|---|
| `full_control` | intact weather/exposure control |
| `no_weather_state` | removes weather and forecast state |
| `no_exposure_state` | removes accumulated body-exposure state |
| `no_shelter_memory` | removes shelter route/use memory |
| `no_fire_tools` | removes fire/light tools |
| `no_water_planning` | removes heat/drought water planning |
| `no_continuity` | removes restore-time weather/shelter/fire continuity |
| `reactive_weather_only` | waits for direct exposure instead of using forecast |
| `omniscient_weather_control` | upper-bound weather/exposure control |

## Results

| Scenario | Selected policy | Weather loss | Exposure loss | Shelter loss | Fire loss | Water loss | Continuity loss | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `mild_clear_control` | `no_weather_baseline` | 0.189 | 0.028 | 0.491 | 0.197 | 0.107 | 0.088 | weather rejected in mild control |
| `cold_rain_exposure` | `continuity_weather_planner` | 13.330 | 126.813 | 361.708 | 75.128 | -0.412 | -0.874 | cold/rain exposure shelter/fire pressure |
| `heat_drought_hydration` | `continuity_weather_planner` | 45.924 | 8.968 | 157.953 | -0.367 | 97.256 | -0.876 | heat/drought water-planning pressure |
| `storm_shelter_fire` | `storm_fire_planner` | 88.413 | -0.193 | 120.201 | 21.411 | 0.134 | -0.182 | forecast storm shelter/fire pressure |
| `restore_forecast_continuity` | `continuity_weather_planner` | 75.816 | -0.757 | 236.609 | 22.544 | -0.475 | 101.439 | restore weather-continuity pressure |

All five verdict rows pass `supports_weather_exposure_precursor=True`.

Key targeted losses:

- `mild_clear_control`: weather machinery is not selected and all ablations have near-zero effect.
- `cold_rain_exposure`: removing exposure state loses `126.813`, shelter memory loses `361.708`, and fire tools lose `75.128`.
- `heat_drought_hydration`: removing water planning loses `97.256`, and removing weather state loses `45.924`.
- `storm_shelter_fire`: removing weather state loses `88.413`, shelter memory loses `120.201`, fire tools lose `21.411`, and reactive-only weather loses `147.512`.
- `restore_forecast_continuity`: removing continuity loses `101.439`, weather state loses `75.816`, shelter memory loses `236.609`, and fire tools lose `22.544`.

## Interpretation

This result supports the fourth pressure-layer step at precursor level:

- weather state is not globally useful;
- forecast matters when reacting after exposure is too late;
- exposure state matters when body state diverges from current world state;
- shelter memory matters when safe places must be reached before or during weather;
- fire/light tools matter when shelter alone does not preserve future capability;
- water planning matters when heat and drought create delayed hydration collapse;
- continuity matters when restore can erase prepared shelter/fire/weather state.

The boundary remains explicit:

> Weather is not selfhood. Weather becomes relevant to selfhood only when the agent must model how external conditions change its own future capability and continuity.

Some selected policies carry extra channels whose ablations are neutral or negative in that row. Those are not positive evidence for those channels. The evidence comes only from targeted losses in matching regimes.

## Limits

- Candidate policies are supplied and return-selected.
- Weather dynamics are abstract control variables, not meteorology.
- Shelter, fire/light tools, water planning, and continuity are designed channels.
- The selected planner is not an online RL agent discovering weather planning from scratch.
- `continuity_weather_planner` carries broad channels; only matching ablations count as evidence.
- This does not yet include tool/shelter degradation, social contracts, predators, or resource ecology.

## Next Test

The next pressure-layer step should add tool/shelter degradation:

- shelter quality, markers, caches, alarms, and fire tools should wear out;
- inspection and repair should compete with food, water, sleep, exploration, and social commitments;
- ablations should separate degradation state, repair action, tool memory, shelter memory, and continuity.

Implemented by [report 79](79_ssrm_3d_tool_shelter_degradation_report.md).

## Visualization

Serve the repo root and open:

```text
http://127.0.0.1:8765/visualizations/ssrm_3d_weather_exposure.html
```

The page replays the `storm_shelter_fire` trace with temperature, rain, wind, weather risk, hydration, exposure debt, illness risk, shelter quality, fire readiness, actions, and ablation outcomes.

## Artifacts

- [experiment script](../experiments/ssrm_3d_weather_exposure.py)
- [visualization](../visualizations/ssrm_3d_weather_exposure.html)
- [evaluation CSV](../artifacts/ssrm_3d_weather_exposure_eval.csv)
- [policy-selection CSV](../artifacts/ssrm_3d_weather_exposure_policy_selection.csv)
- [summary CSV](../artifacts/ssrm_3d_weather_exposure_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_weather_exposure_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_weather_exposure_trace.json)
- [JSON results](../artifacts/ssrm_3d_weather_exposure_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_weather_exposure_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_weather_exposure_results.js)
