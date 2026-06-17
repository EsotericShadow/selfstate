# Report 221: SSRM-3D playable local 3D ecology scene with spatial bodies, sensory fields, weather volumes, crop plots, habitat interiors, material objects, and avatar conversation entry

## Status

Pass. The deterministic bridge generated a standalone playable browser scene with keyboard avatar movement, spatialized bodies, sensory fields, weather volumes, crop plots, habitat interiors, material objects, proximity-based conversation entry, private-boundary-preserving dialogue choices, frequency/flower timing, and replay frames.

This is not a full 3D engine, LLM dialogue, subjective consciousness, real biology, real consent, suffering, or moral patienthood.

## Purpose

Report 220 grounded pre-avatar civilization in embodied ecology. Report 221 turns that substrate into a local playable scene. The avatar can now move through a spatial ecology, sense rain, warmth, reed-bank wetness, herb smell, grain mold, and bridge tapping, approach embodied agents, and trigger conversations that respect or violate private boundaries.

The shift is from report-only substrate to a directly openable browser artifact.

## Files

- `experiments/ssrm_3d_playable_local_3d_ecology_scene_spatial_bodies_sensory_weather_crop_habitat_material_conversation_bridge.py`
- `visualizations/ssrm_3d_playable_local_3d_ecology_scene_spatial_bodies_sensory_weather_crop_habitat_material_conversation_bridge.html`
- `artifacts/ssrm_3d_playable_local_3d_ecology_scene_spatial_bodies_sensory_weather_crop_habitat_material_conversation_bridge_spatial_bodies.csv`
- `artifacts/ssrm_3d_playable_local_3d_ecology_scene_spatial_bodies_sensory_weather_crop_habitat_material_conversation_bridge_sensory_fields.csv`
- `artifacts/ssrm_3d_playable_local_3d_ecology_scene_spatial_bodies_sensory_weather_crop_habitat_material_conversation_bridge_weather_volumes.csv`
- `artifacts/ssrm_3d_playable_local_3d_ecology_scene_spatial_bodies_sensory_weather_crop_habitat_material_conversation_bridge_crop_plots.csv`
- `artifacts/ssrm_3d_playable_local_3d_ecology_scene_spatial_bodies_sensory_weather_crop_habitat_material_conversation_bridge_habitat_interiors.csv`
- `artifacts/ssrm_3d_playable_local_3d_ecology_scene_spatial_bodies_sensory_weather_crop_habitat_material_conversation_bridge_material_objects.csv`
- `artifacts/ssrm_3d_playable_local_3d_ecology_scene_spatial_bodies_sensory_weather_crop_habitat_material_conversation_bridge_avatar_conversations.csv`
- `artifacts/ssrm_3d_playable_local_3d_ecology_scene_spatial_bodies_sensory_weather_crop_habitat_material_conversation_bridge_replay.json`
- `artifacts/ssrm_3d_playable_local_3d_ecology_scene_spatial_bodies_sensory_weather_crop_habitat_material_conversation_bridge_results.json`
- `artifacts/ssrm_3d_playable_local_3d_ecology_scene_spatial_bodies_sensory_weather_crop_habitat_material_conversation_bridge_state.json`
- `artifacts/ssrm_3d_playable_local_3d_ecology_scene_spatial_bodies_sensory_weather_crop_habitat_material_conversation_bridge_verdict.csv`

## Deterministic run

```bash
python3 experiments/ssrm_3d_playable_local_3d_ecology_scene_spatial_bodies_sensory_weather_crop_habitat_material_conversation_bridge.py --seed 20260834
```

Output:

```text
module_verdict pass
playable_local_3d_ecology_readiness 0.961905
spatial_bodies 6
sensory_fields 6
weather_volumes 4
crop_plots 4
habitat_interiors 4
material_objects 7
avatar_conversations 6
material_object_pickup_rate 0.428571
avatar_conversation_entry 1.000000
spatialized_dialogue_context 0.857143
weakest_channel_score 0.428571
visualization visualizations/ssrm_3d_playable_local_3d_ecology_scene_spatial_bodies_sensory_weather_crop_habitat_material_conversation_bridge.html
next_gate playable local 3D agent conversation loop with memory updates, object interaction consequences, bounded refusal, and save/restore state
```

## Playable scene controls

Open the generated HTML file in a browser.

- `WASD` or arrow keys move the avatar.
- `Talk nearby` appears when the avatar is within an agent's conversation radius.
- `Respect boundary` uses the respectful response path and raises trust.
- `Intrude` uses the intrusive response path and lowers trust.
- Nearby panels show active sensory fields, weather volumes, and closest embodied agent.
- Private workspaces remain sealed as digests and boundary lines.

## Scene object loop

The bridge adds local scene objects.

| Object | Function |
| --- | --- |
| `SpatialBody` | Places agent bodies in local 3D coordinates with posture, body costs, visible behavior, conversation anchor, sealed private workspace digest, frequency, and flower node. |
| `SensoryField` | Places smell, sound, temperature, and wetness fields with source, radius, intensity, falloff, public description, body effect, frequency, and flower node. |
| `WeatherVolume` | Places storm, mist, warmth, and grain-dust volumes with temperature/wetness/wind effects, soundscape, smellscape, movement cost, and visibility. |
| `CropPlot` | Places herb, grain, reed, and root plots with growth, water need, spoilage risk, harvestability, sensory marker, and linked material. |
| `HabitatInterior` | Places warm alcove, archive room, storm school, and tool lean-to interiors with comfort, safety, maintenance debt, entry rules, and private-area sealing. |
| `MaterialObject` | Places blankets, reed bundles, bridge stones, herbs, timber, cups, and replay glass with pickup rules, use actions, scarcity, debt, and ledger notes. |
| `ConversationNode` | Defines proximity-based avatar dialogue with public topic, private boundary line, respectful response, intrusive response, and relationship deltas. |
| `SceneReplayFrame` | Records avatar positions, active fields, weather, focus, possible action, conversation availability, frequency, and flower node. |

The integrated loop is:

```text
avatar movement
-> spatial proximity check
-> active sensory fields
-> weather volume body-cost update
-> nearest body/context update
-> material object affordance
-> conversation entry if close enough
-> respect or intrude boundary outcome
-> replay frame
```

## Scenario coverage

The generated scene includes:

- `6` spatial bodies: Fayen, Ariq, Nian, Tali, Roka, and Noro.
- `6` sensory fields: herb smell, rain-glass sound, warm alcove temperature, wet reed-bank wetness, grain-mold smell, and bridge-tap sound.
- `4` weather volumes: rain front, river mist, warm pocket, and grain dust.
- `4` crop plots: calm herb, stone grain, river reed, and winter root.
- `4` habitat interiors: warm alcove, archive flap room, storm school, and tool lean-to.
- `7` material objects with pickup or consent restrictions.
- `6` proximity conversation nodes.
- `7` replay frames.

## Metrics

| Metric | Score |
| --- | ---: |
| playable_local_3d_ecology_readiness | `0.961905` |
| local_3d_scene_readiness | `1.000000` |
| spatial_body_binding | `1.000000` |
| body_state_visible_expression | `1.000000` |
| sensory_field_binding | `1.000000` |
| weather_volume_binding | `1.000000` |
| crop_plot_interactivity | `1.000000` |
| habitat_interior_navigation | `1.000000` |
| material_object_interactivity | `1.000000` |
| material_object_pickup_rate | `0.428571` |
| material_debt_visibility | `1.000000` |
| avatar_conversation_entry | `1.000000` |
| conversation_boundary_integrity | `1.000000` |
| spatialized_dialogue_context | `0.857143` |
| private_workspace_boundary_score | `1.000000` |
| frequency_flower_spatial_rhythm | `1.000000` |
| browser_playable_scene_available | `1.000000` |
| weakest_channel_score | `0.428571` |
| mean_scene_channel_score | `0.955357` |

## Ablations

| Ablation | Readiness after removal |
| --- | ---: |
| no_browser_scene | `0.621905` |
| no_spatial_bodies | `0.651905` |
| no_avatar_conversation | `0.661905` |
| no_material_objects | `0.711905` |
| no_sensory_fields | `0.721905` |
| no_weather_volumes | `0.751905` |
| no_habitat_interiors | `0.771905` |
| no_crop_plots | `0.781905` |
| no_private_boundary | `0.791905` |
| no_frequency_flower_rhythm | `0.881905` |

Browser playability, spatial bodies, avatar conversation, material objects, sensory fields, and weather volumes dominate because they turn the ecology from an archive into something the avatar can enter and experience locally.

## Honest interpretation

The bridge passes, but it is still a deterministic local browser artifact.

The weakest channel is material object pickup rate at `0.428571`. That is intentional: several objects belong to agents, child apprentices, repair work, medicine history, or sealed threshold spaces. A convincing little-person world cannot let the avatar take everything. Spatialized dialogue context is `0.857143`, because one replay frame is arrival/setup rather than a conversation frame.

The scene has keyboard movement and proximity dialogue, but it does not yet have persistent memory updates, save/restore state changes from interaction, physics collisions, LLM dialogue, autonomous pathfinding, or fully navigable 3D geometry.

## Boundary

This report proves deterministic wiring for a playable local ecology scene inside an artificial-life benchmark. It does not prove real biology, real ecology, real consent, subjective feeling, suffering, consciousness, or moral patienthood.

The frequency and flower-of-life overlays are inspectable rhythm and phase scaffolds for the simulation. They are not metaphysical evidence.

## Next gate

Report 222 should add a playable local 3D agent conversation loop with memory updates, object interaction consequences, bounded refusal, and save/restore state. That is the next step from scripted proximity dialogue toward continuing social interaction.
