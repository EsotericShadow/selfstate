# SSRM-3D Coupled Crisis Environmental Bottleneck Report

## Question

Report 109 showed the first learned coupled-crisis improvement: sequence-window planning raised held-out crisis repair. The strong claim still failed because environmental ablation was too weak.

This report tests the next stricter mechanism:

```text
Can a learned sequence-plan controller repair coupled crises when generic environmental activity no longer counts?
```

## What Changed

The benchmark keeps the 72h post-gate crisis world:

- no major crisis before the 12h development gate;
- post-gate crises require environmental repair and social coordination;
- learned-controller inputs do not receive active crisis profile labels.

The new controller makes the environmental side less substitutable:

- each active crisis has one primary environmental repair class;
- wrong environmental actions add damage instead of repair credit;
- environmental repair scoring uses symptom-derived diagnosis, not a scenario ID;
- ablated environmental/social sensors are neutralized so missing sensors do not become false urgency.

The designed controller still receives the stricter target policy. That proves the pressure is representable in the world. The learned controller has to discover usable response structure from features, plan values, and response context.

## What This Does Not Claim

This is not deep reinforcement learning. The controller still starts from supervised imitation and adds a learned plan-value overlay selected by validation return.

It also does not claim subjective consciousness, open-ended civilization, or mature social/environmental understanding. It is a bounded stress test of the Report 109 weakness.

## Canonical Command

```bash
python3 experiments/ssrm_3d_coupled_crisis_environment_bottleneck_controller.py --train-seeds 20260911,20260912,20260913,20260914,20260915,20260916 --tune-seeds 20261011,20261012,20261013 --eval-seeds 20261021,20261022,20261023,20261024,20261025 --hours 72 --step-hours 0.10 --population 14 --epochs 42 --hidden-size 64 --plan-epochs 72 --plan-hidden-size 72 --max-plan-examples 160000 --plan-bias-candidates 0.00,1.00,1.75,2.75,4.00,5.50,7.00,9.00,11.00 --device auto --trace-seed 20261021
```

## Result

The plan model trained on `160000` examples:

```text
pairwise_accuracy = 0.646
selected_router = social_first
selected_plan_bias = 2.75
```

Held-out evaluation is a failed learned result:

| Controller | Total score | Crisis score | Resolved rate | Coupled response |
|---|---:|---:|---:|---:|
| designed | `0.773` | `0.528` | `1.000` | `0.000` |
| base GRU | `0.519` | `0.000` | `0.000` | `0.000` |
| return-selected GRU | `0.518` | `0.000` | `0.100` | `0.029` |
| environment-bottleneck GRU | `0.511` | `0.000` | `0.250` | `0.160` |
| frame MLP | `0.330` | `0.000` | `0.000` | `0.000` |
| reactive | `0.240` | `0.000` | `0.000` | `0.000` |

The stricter controller increases resolved rate and coupled response over the return-selected GRU, but it loses total score, keeps crisis score at `0.000`, and remains far below the designed controller.

The `coupled response` metric counts same-step environmental and social response, not whether both sides eventually finish. That is why the designed controller can resolve every crisis while showing `0.000` coupled response: it repairs the two sides sequentially.

## Ablation Boundary

The strong dependency claim fails:

| Ablation | Total loss | Crisis loss | Coupled response loss | Damage increase |
|---|---:|---:|---:|---:|
| `environment` | `-0.006` | `0.000` | `0.060` | `0.121` |
| `social_culture` | `-0.008` | `0.000` | `-0.002` | `0.036` |
| `body` | `0.011` | `0.000` | `-0.037` | `-0.136` |
| `infrastructure` | `0.054` | `0.000` | `-0.032` | `-0.070` |
| `tools` | `-0.005` | `0.000` | `0.008` | `-0.005` |
| `previous_action` | `-0.009` | `0.000` | `-0.008` | `-0.008` |

The verdict is:

```text
supports_environment_bottleneck_selection = false
supports_social_environment_dependency = false
verdict = partial_or_failed
```

## Interpretation

This is a useful failed boundary.

The stricter world fixes the Report 109 ablation artifact: generic environmental activity no longer counts as repair, and ablated sensors do not create false urgency. The designed controller still solves the task, so the pressure itself is viable.

The learned controller does not solve it. It improves some response metrics over the return-selected GRU, but it does not create enough causal repair to earn crisis score, and ablations do not show clean dependence. In plain English:

```text
the current learned sequence overlay can nudge behavior, but it still does not understand which environmental repair is actually needed
```

The next benchmark should stop adding analytic plan-bias layers and train on real consequences:

- counterfactual rollout values for repair windows;
- actor-critic or model-based return learning inside the crisis world;
- held-out crisis schedules and maps;
- explicit wrong-repair penalties in the learned objective;
- policy-state edits for active crisis memory;
- separate diagnostic heads for sanitation, route, shelter, and illness repair.

## Artifacts

- [script](../experiments/ssrm_3d_coupled_crisis_environment_bottleneck_controller.py)
- [base training CSV](../artifacts/ssrm_3d_coupled_crisis_environment_bottleneck_base_training.csv)
- [plan training CSV](../artifacts/ssrm_3d_coupled_crisis_environment_bottleneck_plan_training.csv)
- [router selection CSV](../artifacts/ssrm_3d_coupled_crisis_environment_bottleneck_router_selection.csv)
- [plan selection CSV](../artifacts/ssrm_3d_coupled_crisis_environment_bottleneck_plan_selection.csv)
- [evaluation CSV](../artifacts/ssrm_3d_coupled_crisis_environment_bottleneck_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_coupled_crisis_environment_bottleneck_summary.csv)
- [ablation CSV](../artifacts/ssrm_3d_coupled_crisis_environment_bottleneck_ablations.csv)
- [verdict CSV](../artifacts/ssrm_3d_coupled_crisis_environment_bottleneck_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_coupled_crisis_environment_bottleneck_trace.json)
- [results JSON](../artifacts/ssrm_3d_coupled_crisis_environment_bottleneck_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_coupled_crisis_environment_bottleneck_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_coupled_crisis_environment_bottleneck_results.js)
