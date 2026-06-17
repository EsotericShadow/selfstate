# Report 178: SSRM-3D Deep-Time Habitat, Climate, and Multisensory World Metabolism Bridge

## Purpose

Report 178 embeds Report 177 resource metabolism into inhabitable places. The previous bridge made tool ecology consume finite resources, regenerate stocks, create waste, and respond to scarcity. This bridge asks whether those resources become world conditions: habitat, climate, weather, wetness, temperature, smell, sound, light, terrain cost, body exposure, shelter, refuge, frequency resonance, and flower-biome patterns.

This is a world-metabolism seed layer. It does not claim a complete 3D world, subjective consciousness, or moral patienthood.

## Architecture

The bridge consumes the Report 177 economy/resource state:

```text
resource metabolism
        |
        v
place-bound resources
        |
        v
season and weather cycle
        |
        v
temperature, wetness, wind, rain, light
        |
        v
terrain route cost + body exposure
        |
        v
sound, smell, light, wetness, temperature channels
        |
        v
shelter microclimate + safety refuge
        |
        v
frequency weather resonance + flower-biome pattern
```

The default run simulates:

- `12` eras
- `200` generations per era
- `2400` total simulated years
- `6` places
- `4` seasonal climate phases
- `6` flower nodes

## Places

The habitat layer tracks:

- `hearth_vale`
- `reed_wetland`
- `stone_ridge`
- `clay_basin`
- `moss_hollow`
- `glass_mire`

Each place carries:

- group ownership
- biome
- terrain resistance
- shelter level
- base temperature
- base wetness
- local resource bindings
- sound signature
- smell signature
- light signature
- weather state
- body exposure vector
- safety-refuge status

## Conditions

The integrated condition is:

- `integrated_deep_time_habitat_climate_multisensory`

Ablations remove one mechanism at a time:

- `no_habitat_resource_binding`
- `no_climate_cycles`
- `no_temperature_wetness_coupling`
- `no_multisensory_channels`
- `no_terrain_route_costs`
- `no_seasonal_resource_feedback`
- `no_body_exposure_binding`
- `no_shelter_microclimate`
- `no_frequency_weather_resonance`
- `no_flower_biome_pattern`
- `no_ecological_pressure_coupling`
- `no_safety_refuges`
- `no_privacy_filter`

The critical ablations are habitat-resource binding, multisensory channels, and body exposure. A world is not convincing if resources are not place-bound, places cannot be sensed, or bodies are not affected by conditions.

## Metrics

The benchmark reports:

- `habitat_resource_binding_rate`
- `climate_cycle_continuity_rate`
- `temperature_wetness_coupling_rate`
- `multisensory_channel_rate`
- `terrain_route_cost_rate`
- `seasonal_resource_feedback_rate`
- `body_exposure_binding_rate`
- `shelter_microclimate_rate`
- `frequency_weather_resonance_rate`
- `flower_biome_pattern_rate`
- `ecological_pressure_coupling_rate`
- `safety_refuge_availability_rate`
- `deep_time_continuity_rate`
- `privacy_preservation_rate`
- `trace_integrity`
- `no_world_or_consciousness_claim_rate`
- `deep_time_habitat_climate_readiness`

Metric weights are normalized to sum to `1.0`.

## Results

The deterministic run produced:

| Metric | Value |
| --- | ---: |
| `module_verdict` | `pass` |
| `deep_time_habitat_climate_readiness` | `0.976667` |
| `simulated_years` | `2400` |
| `no_habitat_resource_binding_loss` | `0.140000` |
| `no_multisensory_channels_loss` | `0.080000` |
| `no_body_exposure_binding_loss` | `0.080000` |
| `safety_refuge_availability_rate` | `0.666667` |

Interpretation:

- Habitat-resource binding is strongly load-bearing.
- Multisensory channels are load-bearing.
- Body exposure is load-bearing.
- Safety refuges exist but are not universal. That is intentional and more realistic than forcing every place to be safe in every condition.
- This remains a seed layer, not a complete navigable 3D world.

## Moral boundary

This report keeps the boundary explicit:

- no subjective-consciousness claim
- no moral-patienthood claim
- no complete-3D-world claim
- body exposure requires safety refuges
- private workspace is not exposed as a debug shortcut
- adverse weather and terrain are world constraints, not suffering spectacle

## Artifacts

- `artifacts/ssrm_3d_deep_time_habitat_climate_multisensory_bridge_eval.csv`
- `artifacts/ssrm_3d_deep_time_habitat_climate_multisensory_bridge_verdict.csv`
- `artifacts/ssrm_3d_deep_time_habitat_climate_multisensory_bridge_results.json`
- `artifacts/ssrm_3d_deep_time_habitat_climate_multisensory_bridge_results.js`
- `artifacts/ssrm_3d_deep_time_habitat_climate_multisensory_bridge_trace.json`
- `artifacts/ssrm_3d_deep_time_habitat_climate_multisensory_bridge_trace.js`
- `artifacts/ssrm_3d_deep_time_habitat_climate_multisensory_bridge_state.json`
- `artifacts/ssrm_3d_deep_time_habitat_climate_multisensory_bridge_state.js`
- `visualizations/ssrm_3d_deep_time_habitat_climate_multisensory_bridge.html`

## Command

```bash
python3 -m experiments.ssrm_3d_deep_time_habitat_climate_multisensory_bridge
```

## Verdict

Report 178 supports a deterministic deep-time habitat, climate, and multisensory world-metabolism seed bridge over `2400` simulated years. It binds resources to places, climate cycles, temperature, wetness, terrain cost, sensory fields, body exposure, shelter microclimates, safety refuges, ecological pressure, frequency weather resonance, flower-biome patterns, privacy, and trace integrity.

The next gate is deep-time settlement architecture and navigable place graph seeds: places should become connected routes, shelters, work areas, storage sites, social spaces, hazards, and avatar-traversable topology.
