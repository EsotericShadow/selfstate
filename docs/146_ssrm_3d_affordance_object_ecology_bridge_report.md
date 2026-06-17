# Report 146: SSRM-3D Affordance Object Ecology Bridge

## Purpose

Report 145 added autonomous live-agent ticks, but the world was still mostly scalar variables. Report 146 adds the next bridge toward a convincing playable world: persistent objects with affordances, locations, integrity, stock, wetness, heat, pathogen risk, owners, required materials, inventory expenditure, repair/crafting loops, sensory bindings, and replayable object histories.

This is still not subjective consciousness, not LLM-backed open dialogue, not a complete playable world, and not unscripted civilization emergence. It is a deterministic object-affordance bridge.

## What changed

- Added `experiments/ssrm_3d_affordance_object_ecology_bridge.py`.
- Added persistent named objects: spring pool, clay cistern, tool cache, shelter roof, fire hearth, herb garden, grain store, waste pit, route cairn, signal drum, loom frame, archive stone, nursery mat, and smoke marker.
- Added affordance tasks such as `collect_water`, `patch_cistern`, `repair_tool_cache`, `repair_roof`, `feed_fire`, `harvest_herbs`, `clean_waste`, `grind_grain`, `repaint_marker`, `tune_drum`, `craft_cloak`, `teach_object_name`, `dry_mat`, and `refresh_smoke_marker`.
- Added inventory consumption and production, social ownership gates, object decay, object repair, object sensory binding, and object-level replay traces.
- Added `visualizations/ssrm_3d_affordance_object_ecology_bridge.html`, an object map and local object-state console.

## Conditions

| Condition | Readiness | Object interaction | Affordance valid | Inventory expenditure | Craft/repair | Decay recovery | Ownership respect | Sensory binding | Persistence | Task chains | Depth | Trace |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `integrated_affordance_object_ecology` | `1.000000` | `0.987868` | `1.000000` | `1.000000` | `0.961538` | `0.626719` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.920009` | `1.000000` |
| `no_persistent_objects` | `0.105180` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.800000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.228907` | `0.000000` |
| `no_inventory_expenditures` | `0.911018` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `0.501098` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.826437` | `1.000000` |
| `no_affordance_dependencies` | `0.972067` | `1.000000` | `0.300000` | `1.000000` | `1.000000` | `0.531991` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.898802` | `1.000000` |
| `no_decay_pressure` | `0.980009` | `0.974003` | `1.000000` | `1.000000` | `0.923469` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.930114` | `1.000000` |
| `no_sensory_object_binding` | `0.960643` | `0.989601` | `1.000000` | `1.000000` | `0.967914` | `0.633192` | `1.000000` | `0.121500` | `1.000000` | `1.000000` | `0.911567` | `1.000000` |
| `no_social_ownership` | `0.854407` | `0.504333` | `1.000000` | `1.000000` | `0.373206` | `0.467450` | `0.504333` | `1.000000` | `1.000000` | `1.000000` | `0.836462` | `1.000000` |
| `no_repair_crafting_loop` | `0.660611` | `0.091854` | `1.000000` | `1.000000` | `0.000000` | `0.350000` | `1.000000` | `0.562143` | `0.850000` | `0.600000` | `0.489761` | `1.000000` |
| `no_trace_replay` | `0.967802` | `0.987868` | `1.000000` | `1.000000` | `0.961538` | `0.626719` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.920009` | `0.000000` |

## Verdict

The integrated condition reaches capped affordance-ecology readiness `1.000000`. The bridge passes its bounded gate with object interaction `0.987868`, affordance validity `1.000000`, inventory expenditure `1.000000`, craft/repair success `0.961538`, decay recovery `0.626719`, ownership respect `1.000000`, sensory-object binding `1.000000`, object persistence `1.000000`, task-chain completion `1.000000`, world-depth score `0.920009`, and trace completeness `1.000000`.

Because the integrated condition saturates the capped readiness scale, not every ablation is judged only by aggregate readiness loss. Direct channel failures also matter: dependency-disabled runs must lose affordance-validity credit, no-decay runs must lose decay-recovery credit, no-sensory runs must lose sensory-object binding, and no-trace runs must lose replay completeness.

Ablation readiness losses:

| Ablation | Readiness loss |
|---|---:|
| `no_persistent_objects` | `0.894820` |
| `no_inventory_expenditures` | `0.088982` |
| `no_affordance_dependencies` | `0.027933` |
| `no_decay_pressure` | `0.019991` |
| `no_sensory_object_binding` | `0.039357` |
| `no_social_ownership` | `0.145593` |
| `no_repair_crafting_loop` | `0.339389` |
| `no_trace_replay` | `0.032198` |

`supports_affordance_object_ecology_bridge = true`.

`supports_subjective_consciousness = false`.

`supports_llm_open_dialogue = false`.

`supports_complete_playable_world = false`.

`supports_unscripted_civilization = false`.

## Interpretation

Report 146 makes the live world more concrete. Agents are no longer acting only on scalar world health. They interact with persistent objects that can be depleted, repaired, owned, made wet, heated, contaminated, remembered, and used as inputs to future affordances.

The added loop is:

```text
object decay -> sensory object binding -> affordance selection -> ownership check -> inventory expenditure -> object/world mutation -> object history trace
```

The next gates are larger object graphs, place-based navigation/pathfinding between objects, learned affordance choice, and open-ended language grounded in these persistent object histories.

## Artifacts

- `artifacts/ssrm_3d_affordance_object_ecology_bridge_eval.csv`
- `artifacts/ssrm_3d_affordance_object_ecology_bridge_verdict.csv`
- `artifacts/ssrm_3d_affordance_object_ecology_bridge_results.json`
- `artifacts/ssrm_3d_affordance_object_ecology_bridge_trace.json`
- `artifacts/ssrm_3d_affordance_object_ecology_bridge_state.json`
- `artifacts/ssrm_3d_affordance_object_ecology_bridge_results.js`
- `artifacts/ssrm_3d_affordance_object_ecology_bridge_trace.js`
- `artifacts/ssrm_3d_affordance_object_ecology_bridge_state.js`
- `visualizations/ssrm_3d_affordance_object_ecology_bridge.html`

## Reproduction

```bash
python3 -m experiments.ssrm_3d_deep_time_playable_bridge
python3 -m experiments.ssrm_3d_live_avatar_intervention_bridge
python3 -m experiments.ssrm_3d_embodied_avatar_input_bridge
python3 -m experiments.ssrm_3d_autonomous_live_agent_loop_bridge
python3 -m experiments.ssrm_3d_affordance_object_ecology_bridge
```
