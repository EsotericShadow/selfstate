# SSRM-3D Coupled Crisis Sequence-Outcome Report

## Question

Report 108 showed that per-step outcome-value reranking is not enough for coupled crisis repair. The value path was selected on validation, but held-out crisis repair got worse.

This report tests the next stronger mechanism:

```text
Can a learned sequence-plan controller improve coupled crisis repair over multi-step repair windows?
```

## What Changed

The benchmark keeps the Report 106 coupled-crisis world:

- no major crisis before the 12h development gate;
- post-gate crises require both environmental repair and social coordination;
- the model receives ordinary symptom features, not active crisis profile names.

The new controller trains a small plan-value model. Instead of scoring one action at a time, it scores short repair-window plans such as:

- balanced repair;
- environment-first repair;
- social-first repair;
- sanitation/care window;
- route/supply window;
- storm/infrastructure window;
- teaching/repair window;
- recovery/sustain window.

Runtime input to the plan model is:

- the ordinary SSRM-3D feature vector;
- one candidate plan identity;
- current environmental and social response fractions in the group step;
- recent environmental and social response fractions in the active window;
- elapsed and remaining crisis-window time.

The plan model does not receive the active crisis profile label. During active crisis windows, the learned sequence-plan head becomes the controller and the GRU acts as a prior. Outside active crisis windows, the GRU remains primary.

## What This Does Not Claim

This is not full deep reinforcement learning. The plan-value model is trained from counterfactual sequence-window utilities and selected by validation return. It does not update the GRU by actor-critic gradients inside the world.

It also does not claim open-ended civilization, subjective consciousness, or a completed 12h+ society benchmark. It is a bounded test of whether sequence-level outcome control repairs the current coupled-crisis failure.

## Canonical Command

```bash
python3 experiments/ssrm_3d_coupled_crisis_sequence_outcome_controller.py --train-seeds 20260911,20260912,20260913,20260914,20260915,20260916 --tune-seeds 20261011,20261012,20261013 --eval-seeds 20261021,20261022,20261023,20261024,20261025 --hours 72 --step-hours 0.10 --population 14 --epochs 42 --hidden-size 64 --plan-epochs 72 --plan-hidden-size 72 --max-plan-examples 160000 --plan-bias-candidates 0.00,1.00,1.75,2.75,4.00,5.50,7.00 --device auto --trace-seed 20261021
```

## Result

The plan model trained on `160000` examples:

```text
pairwise_accuracy = 0.651
selected_router = social_first
selected_plan_bias = 4.0
```

Held-out evaluation shows a real improvement over the return-selected GRU:

| Controller | Total score | Crisis score | Resolved rate | Coupled response |
|---|---:|---:|---:|---:|
| designed | `0.867` | `0.723` | `1.000` | `0.474` |
| sequence-outcome GRU | `0.661` | `0.304` | `0.500` | `0.434` |
| return-selected GRU | `0.536` | `0.036` | `0.200` | `0.084` |
| base GRU | `0.518` | `0.000` | `0.000` | `0.000` |
| frame MLP | `0.330` | `0.000` | `0.000` | `0.000` |
| reactive | `0.240` | `0.000` | `0.000` | `0.000` |

The sequence controller is the first learned coupled-crisis variant in this series to produce substantial held-out crisis repair.

## Ablation Boundary

The strong dependency claim still fails:

| Ablation | Total loss | Crisis loss | Coupled response loss |
|---|---:|---:|---:|
| `social_culture` | `0.062` | `0.139` | `0.110` |
| `environment` | `0.015` | `0.027` | `0.003` |
| `body` | `0.162` | `0.286` | `0.192` |
| `infrastructure` | `0.204` | `0.304` | `0.235` |
| `tools` | `0.013` | `0.035` | `0.072` |
| `previous_action` | `0.062` | `0.139` | `0.120` |

The verdict is:

```text
supports_sequence_outcome_selection = true
supports_social_environment_dependency = false
verdict = partial_or_failed
```

## Interpretation

This is a partial positive result.

Report 107 showed that supervised repair labels were rejected. Report 108 showed that per-step outcome-value reranking can overfit validation and worsen held-out crises. Report 109 shows that moving the learned control target to sequence windows changes the result: held-out crisis score rises from `0.036` to `0.304`, resolved rate rises from `0.200` to `0.500`, and coupled response rises from `0.084` to `0.434`.

But the strong learned-integration claim is not satisfied. The environment ablation produces only a small coupled-response loss, so the controller has not yet shown clean dependence on environmental state under the full ablation standard.

The practical conclusion is:

```text
sequence-level outcome control is the right direction, but the next step must make environmental dependence non-substitutable
```

The next benchmark should:

- add held-out maps/crisis schedules where environmental repair cannot be substituted by social over-response;
- train sequence values from counterfactual rollouts rather than analytic utilities;
- separate sanitation, route, shelter, and resource repair windows;
- require environment ablation to damage crisis score and coupled response;
- add policy-state edits for active repair-window memory;
- eventually move the sequence objective into actor-critic or model-based return learning inside the world.

## Artifacts

- [script](../experiments/ssrm_3d_coupled_crisis_sequence_outcome_controller.py)
- [base training CSV](../artifacts/ssrm_3d_coupled_crisis_sequence_outcome_base_training.csv)
- [plan training CSV](../artifacts/ssrm_3d_coupled_crisis_sequence_outcome_plan_training.csv)
- [router selection CSV](../artifacts/ssrm_3d_coupled_crisis_sequence_outcome_router_selection.csv)
- [plan selection CSV](../artifacts/ssrm_3d_coupled_crisis_sequence_outcome_plan_selection.csv)
- [evaluation CSV](../artifacts/ssrm_3d_coupled_crisis_sequence_outcome_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_coupled_crisis_sequence_outcome_summary.csv)
- [ablation CSV](../artifacts/ssrm_3d_coupled_crisis_sequence_outcome_ablations.csv)
- [verdict CSV](../artifacts/ssrm_3d_coupled_crisis_sequence_outcome_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_coupled_crisis_sequence_outcome_trace.json)
- [results JSON](../artifacts/ssrm_3d_coupled_crisis_sequence_outcome_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_coupled_crisis_sequence_outcome_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_coupled_crisis_sequence_outcome_results.js)
