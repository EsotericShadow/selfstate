# SSRM-3D Coupled Crisis Minimum-Channel Planner Report

## Question

Report 122 showed that explicit two-channel process supervision can still
collapse into one-channel behavior. The selected policy produced social
response `1.000`, environmental response `0.000`, and coupled response `0.000`.

This report tests the next narrower claim:

```text
Can a dynamic weakest-channel planner preserve coupled environmental and social
repair across randomized post-12h crises better than return-selected learned
control, while staying close to fixed-joint coordination?
```

The benchmark keeps the hard setting:

- `96h` worlds;
- no major crisis before `12h`;
- randomized post-gate crisis timing, order, repetition, and initial pressure;
- learned base GRU;
- learned environmental and social crisis action heads;
- return-selected GRU and fixed-joint baselines;
- held-out eval seeds with targeted ablations.

## What Changed

Report 114 passed by using fixed validation-selected environmental/social
quotas around learned action heads. Report 115 made those quotas adaptive by
compact return search, but did not clear the stronger non-fixed-transfer gate.

This report removes the fixed quota as the main decision surface. The new
planner computes environmental and social response targets from:

- current environmental pressure;
- current social pressure;
- infrastructure/resource/weather/body pressure summaries;
- how much of the current step is already being spent on each channel;
- whether one response channel is starving.

The planner then asks the learned environmental/social action heads to fill the
weaker channel first.

This is structured dynamic planning around learned heads. It is not open-ended
role discovery, not unsupplied action discovery, not subjective consciousness,
and not mature deep reinforcement learning.

## Canonical Command

```bash
python3 experiments/ssrm_3d_coupled_crisis_min_channel_planner_controller.py --train-seeds 20260911,20260912,20260913 --tune-seeds 20261111,20261112 --eval-seeds 20261121,20261122,20261123 --hours 96 --step-hours 0.10 --population 14 --epochs 24 --hidden-size 64 --action-epochs 32 --action-hidden-size 64 --device auto --trace-seed 20261121
```

## Training Result

The learned environmental and social action heads trained on crisis-window
examples:

| Head | Train examples | Crisis accuracy | Train loss |
|---|---:|---:|---:|
| environment | `23790` | `0.348` | `1.255` |
| social | `23790` | `1.000` | `0.0007` |

The environmental head remains imperfect. The planner result therefore does
not come from an oracle environmental classifier.

## Planner Selection

Validation selected `conservative_min`.

| Planner | Tune total | Tune crisis | Tune resolved | Tune env | Tune social | Tune coupled | Selected |
|---|---:|---:|---:|---:|---:|---:|---|
| conservative_min | `0.725` | `0.476` | `0.800` | `0.730` | `1.000` | `0.730` | yes |
| balanced_min | `0.694` | `0.411` | `0.717` | `0.666` | `1.000` | `0.666` | no |
| urgent_min | `0.687` | `0.397` | `0.717` | `0.711` | `1.000` | `0.711` | no |
| env_social_guard | `0.693` | `0.411` | `0.717` | `0.717` | `1.000` | `0.717` | no |
| high_pressure_guard | `0.695` | `0.414` | `0.717` | `0.694` | `1.000` | `0.694` | no |

The selected planner is intentionally conservative. More aggressive planners
raise some response pressure but do not improve tune outcome.

## Held-Out Result

The minimum-channel planner passes the bounded transfer gate.

| Controller | Total score | Crisis score | Resolved rate | Env response | Social response | Coupled response |
|---|---:|---:|---:|---:|---:|---:|
| fixed joint GRU | `0.843` | `0.675` | `0.933` | `0.863` | `1.000` | `0.863` |
| min-channel planner GRU | `0.797` | `0.590` | `0.878` | `0.828` | `1.000` | `0.828` |
| designed | `0.760` | `0.522` | `1.000` | `0.077` | `0.923` | `0.000` |
| return-selected GRU | `0.496` | `0.000` | `0.000` | `0.299` | `0.219` | `0.000` |
| base GRU | `0.344` | `0.000` | `0.000` | `0.299` | `0.111` | `0.000` |
| frame MLP | `0.283` | `0.000` | `0.000` | `0.299` | `0.000` | `0.000` |
| reactive | `0.086` | `0.000` | `0.000` | `0.176` | `0.000` | `0.000` |

The verdict is:

```text
mean_crisis_count = 5.667
supports_min_channel_planning = true
supports_non_fixed_transfer = true
supports_social_environment_dependency = true
verdict = pass
```

## Ablation Boundary

The planner depends on both repair channels.

| Ablation | Crisis score | Crisis loss | Coupled response | Coupled loss |
|---|---:|---:|---:|---:|
| none | `0.590` | - | `0.828` | - |
| social_culture | `0.000` | `0.590` | `0.000` | `0.828` |
| environment | `0.000` | `0.590` | `0.000` | `0.828` |
| previous_action | `0.106` | `0.484` | `0.513` | `0.315` |
| body | `0.271` | `0.319` | `0.631` | `0.197` |
| tools | `0.383` | `0.207` | `0.635` | `0.193` |
| infrastructure | `0.332` | `0.258` | `0.702` | `0.125` |

This is the key result: unlike the process-policy controller, removing either
social/culture or environmental access eliminates crisis repair.

## Interpretation

This is a positive bounded result.

The minimum-channel planner does not beat the fixed-joint baseline, but it gets
close while removing the fixed quota grid:

- crisis score is `0.590` versus `0.675` fixed joint;
- resolved rate is `0.878` versus `0.933` fixed joint;
- coupled response is `0.828` versus `0.863` fixed joint;
- total-score gap to fixed joint is only `0.047`.

It also sharply beats the return-selected GRU, whose held-out crisis score and
coupled response remain `0.000`.

The scientific meaning is narrow but useful. A dynamic weakest-channel planner
can preserve coupled repair in the 96h randomized post-gate world when it is
wrapped around learned environmental/social action heads. This is stronger than
fixed schedule success and stronger than naive process supervision, but it is
still structured planning. The planner has engineered pressure summaries and
does not yet prove that an end-to-end learned policy discovered the coordination
principle by itself.

## Next Step

Do not claim open-ended learned civilization.

The next credible step is to distill the successful minimum-channel planner
into an active learned policy and then remove the planner at evaluation:

- train the recurrent crisis policy on successful min-channel trajectories;
- add counterfactual rollouts where one-channel shortcuts are explicitly worse;
- test whether the distilled policy preserves `>0` crisis score without the
  planner;
- keep social/environment ablations and held-out randomized 96h worlds;
- only then move the same principle into richer settlement/world mechanics.

## Artifacts

- [script](../experiments/ssrm_3d_coupled_crisis_min_channel_planner_controller.py)
- [schedule CSV](../artifacts/ssrm_3d_coupled_crisis_min_channel_planner_schedule.csv)
- [base training CSV](../artifacts/ssrm_3d_coupled_crisis_min_channel_planner_base_training.csv)
- [action training CSV](../artifacts/ssrm_3d_coupled_crisis_min_channel_planner_action_training.csv)
- [router selection CSV](../artifacts/ssrm_3d_coupled_crisis_min_channel_planner_router_selection.csv)
- [planner selection CSV](../artifacts/ssrm_3d_coupled_crisis_min_channel_planner_planner_selection.csv)
- [planner probes CSV](../artifacts/ssrm_3d_coupled_crisis_min_channel_planner_planner_probes.csv)
- [evaluation CSV](../artifacts/ssrm_3d_coupled_crisis_min_channel_planner_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_coupled_crisis_min_channel_planner_summary.csv)
- [ablation CSV](../artifacts/ssrm_3d_coupled_crisis_min_channel_planner_ablations.csv)
- [verdict CSV](../artifacts/ssrm_3d_coupled_crisis_min_channel_planner_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_coupled_crisis_min_channel_planner_trace.json)
- [results JSON](../artifacts/ssrm_3d_coupled_crisis_min_channel_planner_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_coupled_crisis_min_channel_planner_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_coupled_crisis_min_channel_planner_results.js)
