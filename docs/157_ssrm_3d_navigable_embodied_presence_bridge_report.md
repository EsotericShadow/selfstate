# Report 157: SSRM-3D Navigable Embodied Presence Bridge

Date: 2026-06-16

## Purpose

Report 156 made the live dialogue-world state interactive through a deterministic browser loop. Report 157 adds the next bridge toward a believable playable world: navigable embodied presence.

The avatar can now move through a place graph, see local objects, bind nearby agents to places, feel route costs through body-state changes, inspect infrastructure costs, receive source-grounded dialogue overlays, render frequency fields, pass through affordance/collision gates, and export a replayable camera timeline.

No LLMs are called. This is not evidence of subjective consciousness, open-ended natural language, unscripted civilization, or a complete playable world.

## Implementation

The new module is:

- `experiments/ssrm_3d_navigable_embodied_presence_bridge.py`

It consumes:

- `artifacts/ssrm_3d_interactive_avatar_dialogue_loop_bridge_state.json`
- `artifacts/ssrm_3d_agent_made_infrastructure_bridge_state.json`
- `artifacts/ssrm_3d_source_native_council_ledger_bridge_state.json`

It emits:

- `artifacts/ssrm_3d_navigable_embodied_presence_bridge_eval.csv`
- `artifacts/ssrm_3d_navigable_embodied_presence_bridge_verdict.csv`
- `artifacts/ssrm_3d_navigable_embodied_presence_bridge_results.json`
- `artifacts/ssrm_3d_navigable_embodied_presence_bridge_results.js`
- `artifacts/ssrm_3d_navigable_embodied_presence_bridge_trace.json`
- `artifacts/ssrm_3d_navigable_embodied_presence_bridge_trace.js`
- `artifacts/ssrm_3d_navigable_embodied_presence_bridge_state.json`
- `artifacts/ssrm_3d_navigable_embodied_presence_bridge_state.js`

The browser artifact is:

- `visualizations/ssrm_3d_navigable_embodied_presence_bridge.html`

## New Bridge Objects

The bridge joins three prior layers:

- Report 156 interactive avatar dialogue and live body/world state;
- Report 148 place, route, object, and infrastructure state;
- Report 152 source-native council ledger state.

The resulting local world has:

- `14` places;
- `36` routes;
- `14` objects;
- `8` agents;
- `128` deterministic navigation ticks.

## Embodied Presence Contract

The contract adds these deterministic components:

- avatar navigation through the place graph;
- local place/object rendering;
- nearby agent binding by place, role, faction, energy, stress, pain, attention, and trust;
- infrastructure route cost and hazard overlays;
- source-grounded dialogue overlays from interactive trace and source ledger;
- sensory-frequency fields for vibration, sound, vision, scent, thermal, wetness, pain, and affect;
- body expenditure rates for fatigue, wetness, cold, pain, breath rate, and trust orientation;
- affordance/collision gates for local object interactions;
- replayable camera timeline.

The flower-of-life part is represented as a deterministic phase lattice used to rotate camera yaw and frequency-field phase across navigation ticks. It is still a modeling scaffold, not a metaphysical claim.

## Results

| Condition | Readiness | Navigation | Place/object | Agents | Route costs | Source | Frequency | Body | Gate | Replay | Boundary | Trace |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `integrated_navigable_embodied_presence` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_avatar_navigation` | `0.760000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_place_object_render` | `0.880000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_agent_presence_binding` | `0.900000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_infrastructure_route_costs` | `0.900000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_source_dialogue_overlay` | `0.890000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_frequency_sensory_field` | `0.900000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_body_expenditure_model` | `0.890000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_affordance_collision_gate` | `0.920000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_replay_camera_timeline` | `0.930000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` |

The full bridge passes with navigable embodied-presence readiness `1.000000`.

## Ablation Read

The largest loss is `no_avatar_navigation`: `0.240000`. That loss includes both direct movement loss and body-expenditure loss, because the body cannot honestly spend effort if the avatar never moves.

The place/object render loss is `0.120000`, source overlay loss is `0.110000`, body expenditure loss is `0.110000`, and agent, route-cost, and frequency losses are each `0.100000`. This is a useful shape: the bridge is not just a moving dot on a map, but a coupled local scene with bodies, routes, objects, sources, and rate fields.

The affordance gate and replay timeline are smaller but still required channels. They prevent the viewer from becoming an ungated visual demo with no exportable trace.

## Honest Boundary

This report supports only this claim: the stack now has a deterministic navigable embodied-presence bridge over the live dialogue world and infrastructure graph.

It does not support:

- subjective consciousness;
- LLM-backed open dialogue;
- unscripted language or culture;
- a complete playable world;
- mature autonomous live agents.

The next gate is continuous live co-presence: avatar movement should perturb nearby agents' autonomous choices in the same loop rather than only selecting a deterministic precomputed camera trace.

## Reproduction

```bash
python3 -m experiments.ssrm_3d_navigable_embodied_presence_bridge
```

The local viewer can be served with:

```bash
python3 -m http.server 8772 --bind 127.0.0.1
```

Then open:

```text
http://127.0.0.1:8772/visualizations/ssrm_3d_navigable_embodied_presence_bridge.html
```
