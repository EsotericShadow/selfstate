# Report 147: SSRM-3D Place Navigation Object Bridge

## Purpose

Report 146 added persistent objects with affordances, inventories, ownership, decay, and repair/crafting loops. The remaining gap was spatial: agents could interact with objects without proving that they navigated a place-based world to reach them.

Report 147 adds a deterministic place-navigation bridge. Agents begin from role-specific home places, choose object destinations, plan routes across a terrain graph, pay body-state travel costs, use sensory gradients, avoid hazards, update route memory, exchange wayfinding, arrive at object locations, and only then mutate object state.

This is still not subjective consciousness, not LLM-backed open dialogue, not a complete playable world, and not unscripted civilization emergence.

## What changed

- Added `experiments/ssrm_3d_place_navigation_object_bridge.py`.
- Added a place graph with terrain, wetness, cold, scent, sound, visibility, slope, route quality, route hazards, and route distances.
- Bound Report 146 objects to places such as `spring_hollow`, `tool_bend`, `roof_ring`, `herb_slope`, `ash_edge`, `cairn_ridge`, `archive_knoll`, and `smoke_watch`.
- Added deterministic pathfinding, travel expenditure, terrain hazard avoidance, sensory-gradient alignment, route memory, social wayfinding, and object interaction after arrival.
- Added `visualizations/ssrm_3d_place_navigation_object_bridge.html`, a place/route map viewer with trip inspection and path animation.

## Conditions

| Condition | Readiness | Route planning | Arrival | Object after arrival | Travel expenditure | Hazard avoidance | Sensory gradient | Route memory | Wayfinding | Efficiency | Trace |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `integrated_place_navigation_object_bridge` | `0.948822` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.943153` | `0.615716` | `1.000000` | `1.000000` | `0.899078` | `1.000000` |
| `no_place_graph` | `0.070000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `1.000000` |
| `no_pathfinding` | `0.558430` | `0.500000` | `0.083333` | `1.000000` | `1.000000` | `0.492813` | `0.296567` | `0.000000` | `1.000000` | `0.480833` | `1.000000` |
| `no_travel_expenditure` | `0.848822` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `0.943153` | `0.615716` | `1.000000` | `1.000000` | `0.899078` | `1.000000` |
| `no_terrain_hazard` | `0.856712` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `0.615716` | `1.000000` | `1.000000` | `0.930575` | `1.000000` |
| `no_sensory_gradient` | `0.886530` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.943153` | `0.000000` | `1.000000` | `1.000000` | `0.888785` | `1.000000` |
| `no_object_destination_binding` | `0.784352` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `0.874417` | `0.627639` | `1.000000` | `1.000000` | `0.487810` | `1.000000` |
| `no_social_wayfinding` | `0.878822` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.943153` | `0.615716` | `1.000000` | `0.000000` | `0.899078` | `1.000000` |
| `no_trace_replay` | `0.878822` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.943153` | `0.615716` | `1.000000` | `1.000000` | `0.899078` | `0.000000` |

## Verdict

The integrated condition reaches place-navigation readiness `0.948822`. It passes this bounded gate with route planning `1.000000`, destination arrival `1.000000`, object-after-arrival interaction `1.000000`, travel expenditure `1.000000`, terrain hazard avoidance `0.943153`, sensory-gradient alignment `0.615716`, route memory `1.000000`, social wayfinding `1.000000`, path efficiency `0.899078`, and trace completeness `1.000000`.

Ablations reduce readiness or directly remove their required channel:

| Ablation | Readiness loss |
|---|---:|
| `no_place_graph` | `0.878822` |
| `no_pathfinding` | `0.390392` |
| `no_travel_expenditure` | `0.100000` |
| `no_terrain_hazard` | `0.092110` |
| `no_sensory_gradient` | `0.062292` |
| `no_object_destination_binding` | `0.164470` |
| `no_social_wayfinding` | `0.070000` |
| `no_trace_replay` | `0.070000` |

`supports_place_navigation_object_bridge = true`.

`supports_subjective_consciousness = false`.

`supports_llm_open_dialogue = false`.

`supports_complete_playable_world = false`.

`supports_unscripted_civilization = false`.

## Interpretation

Report 147 makes object affordances spatially embodied. Agents cannot simply mutate an object by selecting it from a table. They must move through a route graph and incur body-state consequences:

```text
home place -> object destination -> route planning -> terrain cost -> sensory gradient -> body expenditure -> arrival -> object interaction -> route memory
```

This is still a deterministic bridge. The place graph is designed, not learned; pathfinding is algorithmic, not emergent; and language remains token-grounded rather than open-ended. The next gates are richer place-object graphs, agent-made roads/closures, learned navigation policies, multi-agent travel conflict, and language grounded in route/object histories.

## Artifacts

- `artifacts/ssrm_3d_place_navigation_object_bridge_eval.csv`
- `artifacts/ssrm_3d_place_navigation_object_bridge_verdict.csv`
- `artifacts/ssrm_3d_place_navigation_object_bridge_results.json`
- `artifacts/ssrm_3d_place_navigation_object_bridge_trace.json`
- `artifacts/ssrm_3d_place_navigation_object_bridge_state.json`
- `artifacts/ssrm_3d_place_navigation_object_bridge_results.js`
- `artifacts/ssrm_3d_place_navigation_object_bridge_trace.js`
- `artifacts/ssrm_3d_place_navigation_object_bridge_state.js`
- `visualizations/ssrm_3d_place_navigation_object_bridge.html`

## Reproduction

```bash
python3 -m experiments.ssrm_3d_deep_time_playable_bridge
python3 -m experiments.ssrm_3d_live_avatar_intervention_bridge
python3 -m experiments.ssrm_3d_embodied_avatar_input_bridge
python3 -m experiments.ssrm_3d_autonomous_live_agent_loop_bridge
python3 -m experiments.ssrm_3d_affordance_object_ecology_bridge
python3 -m experiments.ssrm_3d_place_navigation_object_bridge
```
