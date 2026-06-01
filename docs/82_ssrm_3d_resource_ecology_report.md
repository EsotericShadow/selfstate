# SSRM-3D Resource Ecology Report

## Question

Do slowly changing resources create persistent control pressure without turning the simulation into ecosystem roleplay?

Report 74 puts resource ecology after structured perception, sleep/rest, illness/sanitation, weather/exposure, tool/shelter degradation, social trust/contracts, and predator/threat agents. This experiment asks whether resource memory, regeneration/depletion models, spoilage timing, migration tracking, restraint, cache management, sharing contracts, territory ownership, and restore continuity become useful only when delayed resource consequences change future viability or access.

The tested claim is narrow:

> Ecology machinery should be rejected in an abundant static control, but selected when regrowth, depletion, spoilage, migration, sharing, territory, or restore-time forgetting changes future options.

This is not ecosystem simulation. It tests resources as long-horizon control pressure.

## Method

Canonical command:

```bash
python3 experiments/ssrm_3d_resource_ecology.py --train-episodes 72 --eval-episodes 96 --seed 20260627 --candidate-count 7
```

The experiment uses return-selected candidate policies over abstract resource-control state. Policies can use:

| Channel | Role |
|---|---|
| resource memory | remembers source locations, access, and depletion state |
| regeneration model | estimates whether a source should be left to regrow |
| spoilage model | estimates when cached food/water becomes waste |
| migration tracking | follows shifting food/water locations |
| restraint policy | trades immediate harvest for future source viability |
| cache management | stores and rotates surplus for later scarcity |
| sharing contract | preserves future access through reciprocal sharing |
| territory ownership | tracks defended/shared access to places |
| continuity memory | preserves depletion, cache age, migration, sharing, and territory history after restore |

Evaluation conditions:

| Condition | Test |
|---|---|
| `full_control` | intact ecology control |
| `no_resource_memory` | removes source/depletion memory |
| `no_regeneration_model` | removes regrowth timing |
| `no_spoilage_model` | removes spoilage timing |
| `no_migration_tracking` | removes shifting-source tracking |
| `no_restraint` | removes overharvest restraint |
| `no_cache_management` | removes cache storage/rotation |
| `no_sharing_contract` | removes reciprocal resource access |
| `no_territory_ownership` | removes place/access ownership memory |
| `no_continuity` | removes restore-time ecology continuity |
| `greedy_consumption_only` | consumes immediately with no ecology model |
| `omniscient_resource_control` | upper-bound ecology control |

## Results

| Scenario | Selected policy | Memory loss | Regen loss | Spoilage loss | Migration loss | Restraint loss | Cache loss | Sharing loss | Territory loss | Continuity loss | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `abundant_static_control` | `greedy_no_ecology_baseline` | -0.085 | -0.013 | -0.060 | -0.081 | -0.009 | 0.065 | 0.033 | -0.009 | 0.088 | ecology machinery rejected |
| `slow_regrowth_depletion` | `regrowth_restraint_planner` | 149.744 | 153.525 | -0.057 | -0.109 | 375.693 | -0.214 | -0.326 | -0.227 | 0.162 | slow regrowth restraint pressure |
| `spoilage_cache_timing` | `spoilage_cache_planner` | 175.369 | 0.011 | 169.149 | -0.010 | 267.014 | 176.232 | -0.105 | 0.029 | 0.090 | spoilage/cache pressure |
| `migrating_resource_sources` | `migration_tracking_planner` | 151.580 | -1.154 | -1.755 | 182.021 | 360.628 | 1.924 | -3.379 | 0.628 | -0.563 | migration/resource-memory pressure |
| `shared_territory_pressure` | `territory_sharing_planner` | 257.510 | 71.249 | 0.093 | -0.090 | 325.285 | 0.083 | 249.619 | 245.601 | 0.005 | sharing/territory pressure |
| `restore_ecology_continuity` | `continuity_ecology_planner` | 268.505 | 125.084 | 94.539 | 273.686 | 251.874 | 146.844 | 342.234 | 344.255 | 218.041 | restore ecology continuity pressure |

All six verdict rows pass `supports_resource_ecology_precursor=True`.

Key targeted losses:

- `abundant_static_control`: ecology machinery is not selected and targeted ablations have near-zero effect.
- `slow_regrowth_depletion`: removing source memory, regrowth timing, or restraint causes large loss.
- `spoilage_cache_timing`: removing source memory, spoilage timing, restraint, or cache management causes large loss.
- `migrating_resource_sources`: removing source memory, migration tracking, or restraint causes large loss.
- `shared_territory_pressure`: removing source memory, regeneration timing, restraint, sharing contracts, or territory memory causes large loss.
- `restore_ecology_continuity`: removing continuity plus resource memory, regeneration, spoilage, migration, cache, sharing, or territory state causes large loss.

## Interpretation

This result supports the eighth pressure-layer step at precursor level:

- resource ecology is not globally useful;
- restraint matters only when immediate harvest damages future source access;
- resource memory matters when source state persists across time;
- spoilage and cache management matter only when stored resources can become waste;
- migration tracking matters only when food/water locations shift;
- sharing and territory matter only when other agents can change future access;
- continuity matters when restore can erase depletion, cache age, migration, sharing, or territory history.

The boundary remains explicit:

> Resource ecology is not selfhood. It becomes relevant to selfhood only when the agent must model its own future needs, access history, restraint, caches, obligations, and place relations as future-control variables.

Some selected policies carry extra channels whose ablations are neutral in that row. Those are not positive evidence for those channels. The evidence comes only from targeted losses in matching regimes.

## Limits

- Candidate policies are supplied and return-selected.
- Resource dynamics are abstract control variables, not ecology simulation.
- Restraint, sharing, territory, and cache policies are designed channels.
- The selected planner is not an online RL agent discovering sustainable harvesting from scratch.
- This report itself does not include injury/disability adaptation, development, dependent care, or irreversible loss.

## Next Test

The implemented follow-up adds injury/disability adaptation:

- limping, hearing loss, vision damage, infection risk, and tool wear should change feasible actions;
- help-seeking, repair, tool substitution, route choice, and social trust should compete;
- ablations should separate capability self-state, sensor damage, motor degradation, repair access, help-seeking, compensation tools, and continuity.

Implemented by [report 83](83_ssrm_3d_injury_disability_adaptation_report.md).

## Visualization

Serve the repo root and open:

```text
http://127.0.0.1:8765/visualizations/ssrm_3d_resource_ecology.html
```

The page replays the `shared_territory_pressure` trace with resource/water levels, cache, scarcity, spoilage, migration confidence, social access, territory standing, conflicts, actions, and ablation outcomes.

## Artifacts

- [experiment script](../experiments/ssrm_3d_resource_ecology.py)
- [visualization](../visualizations/ssrm_3d_resource_ecology.html)
- [evaluation CSV](../artifacts/ssrm_3d_resource_ecology_eval.csv)
- [policy-selection CSV](../artifacts/ssrm_3d_resource_ecology_policy_selection.csv)
- [summary CSV](../artifacts/ssrm_3d_resource_ecology_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_resource_ecology_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_resource_ecology_trace.json)
- [JSON results](../artifacts/ssrm_3d_resource_ecology_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_resource_ecology_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_resource_ecology_results.js)
