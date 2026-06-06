# SSRM-3D Coupled Social/Environment Maturation Report

## Question

Report 105 showed that a learned GRU plus return-selected router can preserve the 72h maturation world, but social/culture and environmental ablations still do not reduce total score cleanly.

This report attacks that weakness directly:

```text
Can a learned multi-day controller handle post-12h crises that require both environmental action and social coordination?
```

## What Changed

The benchmark keeps the 72h maturation world and the Report 104/105 learned-controller family, then adds four post-gate coupled crises:

- `contaminated_water_trust`;
- `route_migration_dispute`;
- `storm_shelter_coordination`;
- `quarantine_rumor`.

Each crisis begins after the 12h development gate. No crisis label is given to the model. The agent stream only contains ordinary world symptoms such as contamination, disease, conflict, trust, route hazard, resource migration, shelter damage, visibility, and prior action.

Each crisis requires two kinds of response:

- environmental response: `sanitize`, `treat`, `scout`, `construct`, or resource actions depending on the crisis;
- social response: `social_repair`, `teach`, or `learn` depending on the crisis.

The crisis score rewards resolved crises, environmental response, social response, and coupled response. It penalizes unresolved crisis damage.

## What This Does Not Claim

This is not deep reinforcement learning. The learned controller still starts from supervised imitation over 72h traces. The return-selected step chooses a router by closed-loop validation outcome, but it does not update the neural weights by policy-gradient or actor-critic feedback.

It also does not claim consciousness or open-ended civilization. It is a sharper falsifier for whether current learned control actually handles coupled social/environmental pressure.

## Canonical Command

```bash
python3 experiments/ssrm_3d_coupled_social_environment_maturation_controller.py --train-seeds 20260911,20260912,20260913,20260914,20260915,20260916 --tune-seeds 20260961,20260962,20260963 --eval-seeds 20260971,20260972,20260973,20260974,20260975 --hours 72 --step-hours 0.10 --population 14 --epochs 42 --hidden-size 64 --device auto --trace-seed 20260971
```

## Result

Validation selected:

```text
selected_router = teaching_tradition
```

Held-out summary:

| Controller | Total score | Maturation | Crisis score | Resolved rate | Coupled response |
|---|---:|---:|---:|---:|---:|
| designed | `0.872` | `1.000` | `0.733` | `1.000` | `0.486` |
| return-selected GRU | `0.518` | `0.997` | `0.000` | `0.100` | `0.013` |
| base GRU | `0.518` | `0.996` | `0.000` | `0.000` | `0.000` |
| frame MLP | `0.331` | `0.636` | `0.000` | `0.000` | `0.000` |
| reactive | `0.240` | `0.462` | `0.000` | `0.000` | `0.000` |

The designed controller resolves the coupled crises. The learned controller mostly preserves generic maturation while failing the actual coupled crisis task.

## Ablation Boundary

The stronger dependency claim also fails:

| Ablation | Total loss | Coupled response loss | Damage increase |
|---|---:|---:|---:|
| `body` | `0.001` | `0.008` | `0.065` |
| `infrastructure` | `0.187` | `0.013` | `0.056` |
| `tools` | `0.002` | `0.013` | `0.080` |
| `social_culture` | `-0.002` | `0.013` | `0.114` |
| `environment` | `0.001` | `0.010` | `0.096` |
| `previous_action` | `-0.001` | `-0.035` | `-0.075` |

The social/culture ablation collapses environmental response but increases generic social response to `1.000`; that is not a successful social dependency. It is an action-collapse failure. The environment ablation also fails to create a clean total-score loss.

The verdict is:

```text
supports_coupled_return_selection = false
supports_social_environment_dependency = false
verdict = partial_or_failed
```

## Interpretation

This is a useful negative result.

Report 105 showed that the learned controller can keep a 72h society alive and maturing. Report 106 shows that this is not the same as understanding coupled crisis repair.

The learned GRU can preserve buildings, tools, births, and knowledge transfer while still failing crises where environmental symptoms and social coordination must be solved together. That is exactly the gap the next controller must attack.

The next stronger step should not add more scenery. It should change the learning objective:

- train on coupled-crisis return or counterfactual outcomes, not only imitation labels;
- add a value/critic head that predicts unresolved crisis damage;
- make wrong social-only and wrong environment-only responses consume the recovery window;
- evaluate on held-out crisis schedules and maps;
- require social/culture and environmental ablations to damage crisis score, not just total maturation.

## Artifacts

- [script](../experiments/ssrm_3d_coupled_social_environment_maturation_controller.py)
- [training CSV](../artifacts/ssrm_3d_coupled_social_environment_maturation_training.csv)
- [selection CSV](../artifacts/ssrm_3d_coupled_social_environment_maturation_selection.csv)
- [evaluation CSV](../artifacts/ssrm_3d_coupled_social_environment_maturation_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_coupled_social_environment_maturation_summary.csv)
- [ablation CSV](../artifacts/ssrm_3d_coupled_social_environment_maturation_ablations.csv)
- [verdict CSV](../artifacts/ssrm_3d_coupled_social_environment_maturation_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_coupled_social_environment_maturation_trace.json)
- [results JSON](../artifacts/ssrm_3d_coupled_social_environment_maturation_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_coupled_social_environment_maturation_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_coupled_social_environment_maturation_results.js)
