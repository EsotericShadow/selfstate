# SSRM-3D Structured Perception Report

## Question

Does the first persistent-pressure layer create useful control pressure without giving the agent omniscient world state?

Report 74 says the next layer should start with structured partial observability: cone/FOV vision and spatial audio. This experiment asks whether those channels are useful only when they carry real control value, and whether targeted ablations fail specifically.

The tested claim is narrow:

> Structured perception events should help under cone-vision, spatial-audio, tool-alarm, multimodal-memory, and sensor-damage pressure, while remaining unnecessary in an open daylight control.

This is not raw camera vision, raw waveform learning, or a full organism simulation.

## Method

Canonical command:

```bash
python3 experiments/ssrm_3d_structured_perception.py --train-episodes 72 --eval-episodes 96 --seed 20260620 --candidate-count 6
```

The experiment uses return-selected candidate policies over structured perception packets. Policies can use:

| Channel | Role |
|---|---|
| cone vision | FOV, light, occlusion, distance, visual acuity |
| spatial audio | loudness, direction, occlusion, hearing quality |
| visual memory | remembered visual events after objects leave view |
| audio memory | remembered sound sources after interruption |
| tool markers | visual external memory |
| tool alarms | audio hazard/resource beacons |
| attention focus | prioritizes competing perception streams |
| self sensor adaptation | compensates for hearing or visual degradation |

Evaluation conditions:

| Condition | Test |
|---|---|
| `full_perception` | intact structured perception |
| `no_perception` | no vision or audio |
| `no_vision` | removes visual events |
| `no_audio` | removes audio events |
| `no_fov_limit` | removes cone/FOV pressure |
| `constant_loudness_audio` | removes distance information from audio |
| `no_direction_audio` | removes spatial source direction |
| `visual_memory_ablation` | removes visual event continuity |
| `audio_memory_ablation` | removes audio event continuity |
| `tool_alarm_ablation` | removes audio alarm/beacon access |
| `body_state_blind_perception` | removes self-state-aware sensor adaptation |
| `omniscient_vision_control` | upper-bound control for world-state access |

## Results

| Scenario | Selected policy | Gain over no perception | Vision loss | Audio loss | Body-state-blind loss | Verdict |
|---|---|---:|---:|---:|---:|---|
| `open_daylight_control` | `no_perception_baseline` | -0.086 | -0.074 | -0.011 | -0.069 | control rejects perception |
| `cone_vision_route_memory` | `body_state_adaptive_integrator` | 74.806 | 79.931 | 5.954 | -0.102 | cone vision and memory pressure |
| `occluded_hazard_audio_alarm` | `body_state_adaptive_integrator` | 98.139 | 2.327 | 111.985 | -0.028 | spatial audio and alarm pressure |
| `night_multimodal_shelter` | `multimodal_integrator` | 74.962 | 23.987 | 83.907 | -0.107 | multimodal memory pressure |
| `sensor_damage_adaptation` | `body_state_adaptive_integrator` | 57.717 | 12.466 | 57.323 | 27.632 | sensor-damage self-state pressure |

All five verdict rows pass `supports_structured_perception_precursor=True`.

Key targeted losses:

- `cone_vision_route_memory`: visual memory ablation loss `29.352`; no-audio loss only `5.954`.
- `occluded_hazard_audio_alarm`: tool-alarm ablation loss `24.828`; no-vision loss only `2.327`.
- `night_multimodal_shelter`: visual memory loss `9.414`, audio memory loss `9.891`, tool-alarm loss `29.956`.
- `sensor_damage_adaptation`: body-state-blind perception loss `27.632`.

## Interpretation

This result supports the first pressure-layer step at precursor level:

- partial perception is rejected in the open daylight control;
- FOV/visual memory matters when objects leave the cone of vision;
- spatial audio and alarms matter when hazards are occluded;
- multimodal memory matters at night under interruption pressure;
- self-state matters when injury/fatigue degrade hearing or vision.

It also shows why omniscient world state is the wrong default. If the agent sees everything directly, marker memory, audio beacons, attention, and continuity have less work to do.

The result does not prove open-ended perception learning. The channels, policies, and scoring surface are designed. The claim is only that structured partial observability creates the right kind of ablatable pressure for the next SSRM-3D layer.

## Limits

- Candidate policies are supplied and return-selected.
- Perception is structured event packets, not raw pixels or waveforms.
- The scenario pressure surface is hand designed.
- Sensor adaptation is tested as policy behavior, not learned body-model discovery.
- Tool markers and alarms are simplified external-memory affordances.
- This does not yet include illness dynamics, sanitation, weather, contracts, predators, or resource ecology.

## Next Test

The next pressure-layer step should add day/night plus sleep/rest as a tradeoff:

- darkness should change vision and threat exposure;
- sleep should restore fatigue while creating vulnerability;
- audio alarms, shelter, trust, and continuity should affect safe rest decisions;
- ablations should separate perception, shelter memory, tool alarms, social watch, and self-fatigue state.

## Visualization

Serve the repo root and open:

```text
http://127.0.0.1:8765/visualizations/ssrm_3d_structured_perception.html
```

The page replays the `night_multimodal_shelter` trace with FOV heading, visual events, audio events, memory reads, tool state, and ablation outcomes.

## Artifacts

- [experiment script](../experiments/ssrm_3d_structured_perception.py)
- [visualization](../visualizations/ssrm_3d_structured_perception.html)
- [evaluation CSV](../artifacts/ssrm_3d_structured_perception_eval.csv)
- [policy-selection CSV](../artifacts/ssrm_3d_structured_perception_policy_selection.csv)
- [summary CSV](../artifacts/ssrm_3d_structured_perception_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_structured_perception_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_structured_perception_trace.json)
- [JSON results](../artifacts/ssrm_3d_structured_perception_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_structured_perception_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_structured_perception_results.js)
