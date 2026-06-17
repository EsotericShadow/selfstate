# Report 148: SSRM-3D Agent-Made Infrastructure Bridge

## Purpose

Report 147 proved that agents could navigate a designed place graph to reach object affordances. The next gap was agency over the graph itself. A convincing simulated world needs agents to change the terrain they inherit: roads, bridges, drainage, watch posts, route signs, covered walks, water channels, and maintained infrastructure.

Report 148 adds a deterministic agent-made infrastructure bridge. Agents choose projects, spend materials, coordinate labor, use sensory site selection, complete infrastructure, mutate route cost and hazard, couple projects to object accessibility, maintain decaying infrastructure, and leave persistent project histories.

This is still not subjective consciousness, not LLM-backed open dialogue, not a complete playable world, and not unscripted civilization emergence.

## What changed

- Added `experiments/ssrm_3d_agent_made_infrastructure_bridge.py`.
- Added infrastructure projects: mud causeway, ash drainage trench, ridge stone steps, smoke watchtower, covered nursery walk, herb slope switchback, tool sledge path, archive waystones, cistern water channel, and drum resonance posts.
- Added material inventories and expenditures for wood, stone, fiber, clay, resin, charcoal, ash, and hide.
- Added social labor coordination across roles.
- Added route mutation: built projects reduce route cost, reduce hazard, raise route quality, and record `built_projects` on route edges.
- Added object-route coupling: infrastructure improves access to linked objects.
- Added maintenance decay and maintenance actions.
- Added `visualizations/ssrm_3d_agent_made_infrastructure_bridge.html`, an infrastructure-map viewer.

## Conditions

| Condition | Readiness | Complete | Materials | Labor | Route mutation | Cost reduction | Hazard reduction | Maintenance | Sensory site | Object coupling | Access gain | History | Trace |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `integrated_agent_made_infrastructure` | `0.829745` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.087778` | `0.078333` | `0.768008` | `0.620519` | `1.000000` | `0.109286` | `1.000000` | `1.000000` |
| `no_infrastructure_projects` | `0.080000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `1.000000` |
| `no_material_expenditure` | `0.300059` | `0.000000` | `0.000000` | `1.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.625737` | `0.000000` | `0.000000` | `1.000000` | `1.000000` |
| `no_social_labor` | `0.301330` | `0.000000` | `1.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.641630` | `0.000000` | `0.000000` | `1.000000` | `1.000000` |
| `no_route_mutation` | `0.683134` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `0.000000` | `0.000000` | `0.768008` | `0.620519` | `1.000000` | `0.109286` | `1.000000` | `1.000000` |
| `no_maintenance_decay` | `0.760517` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.087778` | `0.078333` | `0.000000` | `0.619183` | `1.000000` | `0.109286` | `1.000000` | `1.000000` |
| `no_sensory_site_selection` | `0.766027` | `0.900000` | `1.000000` | `1.000000` | `1.000000` | `0.083333` | `0.075000` | `0.770083` | `0.000000` | `1.000000` | `0.097143` | `1.000000` | `1.000000` |
| `no_object_route_coupling` | `0.745373` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.087778` | `0.078333` | `0.768008` | `0.620519` | `0.000000` | `0.000000` | `1.000000` | `1.000000` |
| `no_trace_replay` | `0.749745` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.087778` | `0.078333` | `0.768008` | `0.620519` | `1.000000` | `0.109286` | `1.000000` | `0.000000` |

## Verdict

The integrated condition reaches infrastructure readiness `0.829745`. It passes this bounded gate with project completion `1.000000`, material expenditure `1.000000`, social labor coordination `1.000000`, route mutation `1.000000`, route cost reduction `0.087778`, hazard reduction `0.078333`, maintenance sustainability `0.768008`, sensory site alignment `0.620519`, object-route coupling `1.000000`, accessibility gain `0.109286`, infrastructure history persistence `1.000000`, and trace completeness `1.000000`.

Ablations reduce readiness or directly remove their required channel:

| Ablation | Readiness loss |
|---|---:|
| `no_infrastructure_projects` | `0.749745` |
| `no_material_expenditure` | `0.529686` |
| `no_social_labor` | `0.528415` |
| `no_route_mutation` | `0.146611` |
| `no_maintenance_decay` | `0.069228` |
| `no_sensory_site_selection` | `0.063718` |
| `no_object_route_coupling` | `0.084372` |
| `no_trace_replay` | `0.080000` |

`supports_agent_made_infrastructure_bridge = true`.

`supports_subjective_consciousness = false`.

`supports_llm_open_dialogue = false`.

`supports_complete_playable_world = false`.

`supports_unscripted_civilization = false`.

## Interpretation

Report 148 changes the route graph from a fixed designed substrate into an agent-modified substrate. The added loop is:

```text
infrastructure need -> sensory site selection -> material expenditure -> social labor -> project completion -> route/object mutation -> decay -> maintenance history
```

That moves the project closer to a playable world where the player enters after agents have not only survived in a world, but also altered it. It remains a deterministic bridge: project templates are designed, labor allocation is hand-scored, and no open-ended institution or language system invents new project categories yet. The next gates are agent-created project proposals, conflict over infrastructure priorities, long-run maintenance debt, and language grounded in built-world histories.

## Artifacts

- `artifacts/ssrm_3d_agent_made_infrastructure_bridge_eval.csv`
- `artifacts/ssrm_3d_agent_made_infrastructure_bridge_verdict.csv`
- `artifacts/ssrm_3d_agent_made_infrastructure_bridge_results.json`
- `artifacts/ssrm_3d_agent_made_infrastructure_bridge_trace.json`
- `artifacts/ssrm_3d_agent_made_infrastructure_bridge_state.json`
- `artifacts/ssrm_3d_agent_made_infrastructure_bridge_results.js`
- `artifacts/ssrm_3d_agent_made_infrastructure_bridge_trace.js`
- `artifacts/ssrm_3d_agent_made_infrastructure_bridge_state.js`
- `visualizations/ssrm_3d_agent_made_infrastructure_bridge.html`

## Reproduction

```bash
python3 -m experiments.ssrm_3d_deep_time_playable_bridge
python3 -m experiments.ssrm_3d_live_avatar_intervention_bridge
python3 -m experiments.ssrm_3d_embodied_avatar_input_bridge
python3 -m experiments.ssrm_3d_autonomous_live_agent_loop_bridge
python3 -m experiments.ssrm_3d_affordance_object_ecology_bridge
python3 -m experiments.ssrm_3d_place_navigation_object_bridge
python3 -m experiments.ssrm_3d_agent_made_infrastructure_bridge
```
