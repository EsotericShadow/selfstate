# SSRM-3D Tool/Shelter Degradation Report

## Question

Does maintenance/wear create persistent control pressure without turning the world into a construction simulator?

Report 74 puts tool/shelter degradation after structured perception, sleep/rest, illness/sanitation, and weather/exposure. This experiment asks whether marker wear, shelter damage, alarm/cache decay, inspection, repair, spare parts, and restore continuity become useful only when they change future options.

The tested claim is narrow:

> Maintenance machinery should be rejected in a stable new-tools control, but selected when delayed degradation changes route finding, shelter safety, alarm reliability, resource cache value, or restore continuity.

This is not a tool-building simulation. It tests degradation as control pressure.

## Method

Canonical command:

```bash
python3 experiments/ssrm_3d_tool_shelter_degradation.py --train-episodes 72 --eval-episodes 96 --seed 20260624 --candidate-count 6
```

The experiment uses return-selected candidate policies over abstract control state. Policies can use:

| Channel | Role |
|---|---|
| degradation state | estimates tool integrity and shelter quality through time |
| inspection action | refreshes hidden wear state after shocks or drift |
| repair action | trades time and parts for restored tool or shelter function |
| tool memory | binds markers, alarms, and caches to future route/resource control |
| shelter memory | binds shelter quality to future safety and exposure control |
| material cache | supplies spare parts for repair |
| continuity memory | preserves known wear, repairs, and parts state after restore |

Evaluation conditions:

| Condition | Test |
|---|---|
| `full_control` | intact maintenance control |
| `no_degradation_state` | removes predicted wear state |
| `no_inspection_action` | removes inspection and current wear refresh |
| `no_repair_action` | removes repair |
| `no_tool_memory` | removes marker/alarm/cache identity memory |
| `no_shelter_memory` | removes shelter-quality memory |
| `no_material_cache` | removes spare parts |
| `no_continuity` | removes restore-time maintenance continuity |
| `reactive_failure_only` | waits for obvious failure instead of planned maintenance |
| `omniscient_maintenance_control` | upper-bound maintenance control |

## Results

| Scenario | Selected policy | Degradation loss | Inspection loss | Repair loss | Tool loss | Shelter loss | Parts loss | Continuity loss | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| `stable_new_tools_control` | `no_maintenance_baseline` | -0.002 | -0.014 | 0.007 | 0.009 | 0.003 | -0.002 | -0.008 | maintenance rejected in stable control |
| `route_marker_decay` | `marker_maintenance_planner` | 57.630 | -11.996 | 173.797 | 183.292 | 0.106 | 180.012 | 0.171 | route-marker degradation pressure |
| `storm_shelter_wear` | `shelter_repair_planner` | 43.636 | -1.861 | 378.175 | -0.125 | 390.413 | 384.822 | -0.124 | shelter wear repair pressure |
| `alarm_cache_wear` | `marker_maintenance_planner` | 23.205 | 20.623 | 232.840 | 245.319 | 0.511 | 266.615 | 0.475 | alarm/cache inspection repair pressure |
| `restore_maintenance_continuity` | `continuity_maintenance_planner` | 87.366 | -12.837 | 425.557 | 225.196 | 116.633 | 433.905 | 46.791 | restore maintenance continuity pressure |

All five verdict rows pass `supports_tool_shelter_degradation_precursor=True`.

Key targeted losses:

- `stable_new_tools_control`: maintenance machinery is not selected and all ablations have near-zero effect.
- `route_marker_decay`: removing degradation state loses `57.630`, repair loses `173.797`, tool memory loses `183.292`, and spare parts lose `180.012`.
- `storm_shelter_wear`: removing repair loses `378.175`, shelter memory loses `390.413`, and spare parts lose `384.822`.
- `alarm_cache_wear`: removing inspection loses `20.623`, repair loses `232.840`, tool memory loses `245.319`, and spare parts lose `266.615`.
- `restore_maintenance_continuity`: removing continuity loses `46.791`, repair loses `425.557`, tool memory loses `225.196`, shelter memory loses `116.633`, and spare parts lose `433.905`.

## Interpretation

This result supports the fifth pressure-layer step at precursor level:

- maintenance state is not globally useful;
- degradation state matters when future tool/shelter function depends on hidden wear;
- inspection matters when unpredictable shocks make forecasted wear stale;
- repair matters when decayed tools or shelter cause delayed control loss;
- spare parts matter when repair is possible but resource-bounded;
- tool and shelter memory matter because worn objects are persistent external state;
- continuity matters when restore can erase known wear, repair state, or parts state.

The boundary remains explicit:

> Tool wear is not selfhood. Degradation becomes relevant to selfhood only when the agent must model persistent external infrastructure as part of its future capability.

Some selected policies carry extra channels whose ablations are neutral or negative in that row. Those are not positive evidence for those channels. The evidence comes only from targeted losses in matching regimes.

## Limits

- Candidate policies are supplied and return-selected.
- Tool/shelter degradation dynamics are abstract control variables, not construction physics.
- Repair, inspection, marker memory, shelter memory, and spare parts are designed channels.
- The selected planner is not an online RL agent discovering maintenance from scratch.
- `marker_maintenance_planner` also handles the alarm/cache row because the current tool channel is still shared; richer tool classes remain future work.
- This does not yet include social contracts, predators, resource ecology, ownership, or irreversible loss.

## Next Test

The next pressure-layer step should add social trust/contracts:

- agents should promise to return tools, warn about hazards, share resources, or maintain shelters;
- trust should be affected by fulfilled or broken commitments;
- ablations should separate commitment memory, identity memory, tool ownership, repair debt, communication, and continuity.

## Visualization

Serve the repo root and open:

```text
http://127.0.0.1:8765/visualizations/ssrm_3d_tool_shelter_degradation.html
```

The page replays the `alarm_cache_wear` trace with tool integrity, shelter quality, spare parts, exposure, resource loss, route confusion, failures, actions, and ablation outcomes.

## Artifacts

- [experiment script](../experiments/ssrm_3d_tool_shelter_degradation.py)
- [visualization](../visualizations/ssrm_3d_tool_shelter_degradation.html)
- [evaluation CSV](../artifacts/ssrm_3d_tool_shelter_degradation_eval.csv)
- [policy-selection CSV](../artifacts/ssrm_3d_tool_shelter_degradation_policy_selection.csv)
- [summary CSV](../artifacts/ssrm_3d_tool_shelter_degradation_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_tool_shelter_degradation_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_tool_shelter_degradation_trace.json)
- [JSON results](../artifacts/ssrm_3d_tool_shelter_degradation_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_tool_shelter_degradation_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_tool_shelter_degradation_results.js)
