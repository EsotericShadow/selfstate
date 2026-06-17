# Report 179: SSRM-3D Deep-Time Settlement Architecture and Navigable Place Graph Bridge

## Purpose

Report 179 turns Report 178 place-bound habitat into navigable settlement topology. The previous bridge gave places weather, wetness, temperature, terrain, smell, sound, light, body exposure, shelters, and refuge status. This report asks whether those places can become a connected settlement graph with routes, functions, hazards, safe fallback paths, and avatar-traversal metadata.

This is a topology seed layer. It does not claim complete gameplay, a complete 3D world, subjective consciousness, or moral patienthood.

## Architecture

The bridge consumes the Report 178 habitat/climate state:

```text
place-bound habitat
        |
        v
settlement functions
        |
        v
routes and route costs
        |
        v
hazards and refuge paths
        |
        v
storage, work, shelter, social spaces
        |
        v
avatar traversal packet
        |
        v
frequency route resonance + flower layout + lineage
```

The default run simulates:

- `12` eras
- `200` generations per era
- `2400` total simulated years
- `6` places
- `8` settlement routes

## Places and routes

The settlement graph connects:

- `hearth_vale`
- `moss_hollow`
- `clay_basin`
- `reed_wetland`
- `glass_mire`
- `stone_ridge`

Route classes include:

- `shelter_path`
- `work_path`
- `watch_path`
- `soft_moss_path`
- `water_clay_path`
- `ridge_work_path`
- `wetland_glass_path`
- `edge_watch_path`

Each route carries:

- distance
- route cost
- hazard level
- avatar traversability
- frequency resonance
- flower node
- route hash

## Conditions

The integrated condition is:

- `integrated_deep_time_settlement_architecture_place_graph`

Ablations remove one mechanism at a time:

- `no_place_graph`
- `no_route_costs`
- `no_shelter_nodes`
- `no_storage_sites`
- `no_work_sites`
- `no_social_spaces`
- `no_hazard_mapping`
- `no_avatar_traversal`
- `no_safety_routing`
- `no_settlement_lineage`
- `no_frequency_route_resonance`
- `no_flower_layout`
- `no_privacy_filter`

The critical ablations are place graph, avatar traversal, and safety routing. A topology layer is not useful if places are disconnected, if the avatar cannot traverse the graph, or if there are no safe fallback paths.

## Metrics

The benchmark reports:

- `place_graph_connectivity_rate`
- `route_cost_binding_rate`
- `shelter_node_rate`
- `storage_site_rate`
- `work_site_rate`
- `social_space_rate`
- `hazard_mapping_rate`
- `avatar_traversability_rate`
- `safety_refuge_routing_rate`
- `settlement_lineage_integrity_rate`
- `frequency_route_resonance_rate`
- `flower_layout_rate`
- `deep_time_continuity_rate`
- `privacy_preservation_rate`
- `trace_integrity`
- `no_complete_world_or_consciousness_claim_rate`
- `settlement_architecture_readiness`

Metric weights are normalized to sum to `1.0`.

## Results

The deterministic run produced:

| Metric | Value |
| --- | ---: |
| `module_verdict` | `pass` |
| `settlement_architecture_readiness` | `1.000000` |
| `simulated_years` | `2400` |
| `place_graph_connectivity_rate` | `1.000000` |
| `avatar_traversability_rate` | `1.000000` |
| `safety_refuge_routing_rate` | `1.000000` |
| `no_place_graph_loss` | `0.250000` |
| `no_avatar_traversal_loss` | `0.170000` |
| `no_safety_routing_loss` | `0.080000` |

Interpretation:

- The settlement graph is connected.
- Avatar traversal metadata is present and load-bearing.
- Safety routing is present and load-bearing.
- This is not complete gameplay; it is the topology substrate needed for later playable traversal.

## Moral boundary

This report keeps the boundary explicit:

- no subjective-consciousness claim
- no moral-patienthood claim
- no complete-3D-world claim
- no complete-playable-world claim
- private workspace is not exposed as a debug shortcut
- hazards require refuge paths and route costs

## Artifacts

- `artifacts/ssrm_3d_deep_time_settlement_architecture_place_graph_bridge_eval.csv`
- `artifacts/ssrm_3d_deep_time_settlement_architecture_place_graph_bridge_verdict.csv`
- `artifacts/ssrm_3d_deep_time_settlement_architecture_place_graph_bridge_results.json`
- `artifacts/ssrm_3d_deep_time_settlement_architecture_place_graph_bridge_results.js`
- `artifacts/ssrm_3d_deep_time_settlement_architecture_place_graph_bridge_trace.json`
- `artifacts/ssrm_3d_deep_time_settlement_architecture_place_graph_bridge_trace.js`
- `artifacts/ssrm_3d_deep_time_settlement_architecture_place_graph_bridge_state.json`
- `artifacts/ssrm_3d_deep_time_settlement_architecture_place_graph_bridge_state.js`
- `visualizations/ssrm_3d_deep_time_settlement_architecture_place_graph_bridge.html`

## Command

```bash
python3 -m experiments.ssrm_3d_deep_time_settlement_architecture_place_graph_bridge
```

## Verdict

Report 179 supports a deterministic deep-time settlement architecture and navigable place graph seed bridge over `2400` simulated years. It connects multisensory places into routes, costs, functions, hazards, shelter/storage/work/social architecture, safety refuge paths, avatar traversal packets, frequency route resonance, flower layout, privacy, and lineage.

The next gate is browser-playable avatar traversal over settlement topology: the viewer should let the user move through this graph and see route costs, hazards, sensory changes, and refuge options in browser state.
