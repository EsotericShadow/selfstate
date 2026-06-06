# SSRM-3D Coupled Crisis Outcome-Value Report

## Question

Reports 106 and 107 left a clear bottleneck:

```text
The learned controller can preserve a 72h society, but it still does not repair coupled crises.
```

Report 107 tried a supervised repair-label critic. Validation rejected it by selecting repair bias `0.0`.

This report tests the next stronger idea:

```text
Can a counterfactual outcome-value critic improve coupled crisis repair?
```

## What Changed

The benchmark keeps the Report 106 72h world:

- no major crisis before the 12h development gate;
- post-gate crises require environmental response and social coordination;
- the model receives ordinary symptom features, not active crisis names.

The new controller trains a small action-value critic. Its input is:

- the ordinary SSRM-3D feature vector;
- one candidate action;
- the current environmental-response fraction in the group step;
- the current social-response fraction in the group step.

Its target is not a repair label. It is a counterfactual utility estimate based on:

- predicted crisis progress;
- unresolved crisis damage;
- whether the group is missing environmental or social response;
- symptom fit;
- agent skill fit;
- response opportunity cost.

The learned GRU still provides the base action logits, and the return-selected router still provides the pressure bias. The outcome-value critic reranks action logits by validation-selected value bias.

## What This Does Not Claim

This is not full deep reinforcement learning. The value critic is trained from counterfactual outcome targets and selected by validation return, but it does not update the controller by actor-critic gradients inside the world.

It also does not claim open-ended civilization, subjective consciousness, or a solved 12h+ society. It is a bounded test of whether outcome-aware reranking repairs the current coupled-crisis failure.

## Canonical Command

```bash
python3 experiments/ssrm_3d_coupled_crisis_outcome_value_controller.py --train-seeds 20260911,20260912,20260913,20260914,20260915,20260916 --tune-seeds 20261011,20261012,20261013 --eval-seeds 20261021,20261022,20261023,20261024,20261025 --hours 72 --step-hours 0.10 --population 14 --epochs 42 --hidden-size 64 --value-epochs 70 --value-hidden-size 64 --max-value-examples 180000 --value-bias-candidates 0.00,1.00,1.75,2.75,4.00,5.50,7.00 --device auto --trace-seed 20261021
```

## Result

The value model trained on `180000` examples:

```text
pairwise_accuracy = 0.693
positive_examples = 11604
```

Validation selected:

```text
selected_router = social_first
selected_value_bias = 1.75
```

That is a stronger test than Report 107: validation did not turn the new critic off.

Held-out evaluation still failed:

| Controller | Total score | Crisis score | Resolved rate | Coupled response |
|---|---:|---:|---:|---:|
| designed | `0.867` | `0.723` | `1.000` | `0.474` |
| return-selected GRU | `0.536` | `0.036` | `0.200` | `0.084` |
| outcome-value GRU | `0.515` | `0.000` | `0.050` | `0.043` |
| base GRU | `0.518` | `0.000` | `0.000` | `0.000` |
| frame MLP | `0.330` | `0.000` | `0.000` | `0.000` |
| reactive | `0.240` | `0.000` | `0.000` | `0.000` |

The outcome-value controller selected a nonzero value bias on validation, but it underperformed the return-selected GRU on held-out crises.

## Ablation Boundary

The strong dependency claim fails:

| Ablation | Total loss | Crisis loss | Coupled response loss |
|---|---:|---:|---:|
| `social_culture` | `-0.000` | `0.000` | `0.043` |
| `environment` | `-0.001` | `0.000` | `-0.013` |
| `infrastructure` | `0.058` | `0.000` | `-0.007` |
| `tools` | `-0.002` | `0.000` | `0.043` |
| `body` | `-0.015` | `-0.027` | `0.004` |
| `previous_action` | `-0.005` | `-0.001` | `-0.089` |

The verdict is:

```text
supports_outcome_value_selection = false
supports_social_environment_dependency = false
verdict = partial_or_failed
```

## Interpretation

This is a useful negative result.

Report 107 showed that supervised repair labels are not enough. Report 108 shows that a counterfactual value reranker can overfit validation pressure without improving held-out coupled crisis repair.

The practical conclusion is now narrower:

```text
the next controller needs sequence-level outcome learning, not per-step reranking
```

The failure mode is also clearer. The value critic can nudge social and environmental response rates, but it does not learn stable timing, sequencing, and recovery-window allocation. It still fails to coordinate enough environmental and social response in held-out crises.

The next stronger benchmark should:

- train a sequence-level value model over crisis windows, not isolated action choices;
- use counterfactual rollouts for multi-step repair sequences;
- penalize validation overfit by selecting on more crisis schedules and maps;
- separate social-only, environment-only, and coupled repair returns;
- require held-out social/environment ablations to damage crisis score;
- eventually move the objective into actor-critic or model-based return learning inside the world.

## Artifacts

- [script](../experiments/ssrm_3d_coupled_crisis_outcome_value_controller.py)
- [base training CSV](../artifacts/ssrm_3d_coupled_crisis_outcome_value_base_training.csv)
- [value training CSV](../artifacts/ssrm_3d_coupled_crisis_outcome_value_value_training.csv)
- [router selection CSV](../artifacts/ssrm_3d_coupled_crisis_outcome_value_router_selection.csv)
- [value selection CSV](../artifacts/ssrm_3d_coupled_crisis_outcome_value_value_selection.csv)
- [evaluation CSV](../artifacts/ssrm_3d_coupled_crisis_outcome_value_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_coupled_crisis_outcome_value_summary.csv)
- [ablation CSV](../artifacts/ssrm_3d_coupled_crisis_outcome_value_ablations.csv)
- [verdict CSV](../artifacts/ssrm_3d_coupled_crisis_outcome_value_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_coupled_crisis_outcome_value_trace.json)
- [results JSON](../artifacts/ssrm_3d_coupled_crisis_outcome_value_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_coupled_crisis_outcome_value_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_coupled_crisis_outcome_value_results.js)
