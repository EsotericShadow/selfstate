# SSRM-3D Coupled Crisis Active State/Action Value Report

## Question

Report 116 showed that a value model over whole allocator policies can improve
tune-world selection while transferring worse than the seed/fixed allocator.

This report moves the value model closer to the actual control point:

```text
Can a state/action value model trained from active crisis step consequences
improve held-out 96h coupled-crisis repair?
```

The benchmark keeps the same randomized-transfer world:

- `96h` runs;
- no major crisis before `12h`;
- randomized post-gate crisis timing, order, repetition, and initial pressure;
- learned base GRU;
- learned environmental and social action heads;
- no crisis profile name in the value model input.

## What Changed

The new controller trains a small neural value head on active-crisis examples.
Each example contains:

- ordinary agent observation features;
- active crisis progress and timing context;
- current environmental/social response fractions;
- a candidate repair action one-hot.

The candidate action set is supplied:

```text
none, sanitize, treat, scout, construct, social_repair, teach, learn
```

At runtime, the controller scores candidate crisis actions and uses the
selected `value_bias` around the learned environmental/social action heads.

## What This Does Not Claim

This is not actor-critic reinforcement learning, subjective consciousness,
open-ended civilization, or real-world competence.

The environmental and social action heads are still supervised. The candidate
repair action set is supplied. The value target is a bounded step-consequence
label, not a full learned return function over arbitrary actions.

## Canonical Command

```bash
python3 experiments/ssrm_3d_coupled_crisis_active_state_value_controller.py --train-seeds 20260911,20260912,20260913,20260914,20260915,20260916 --tune-seeds 20261111,20261112,20261113 --eval-seeds 20261121,20261122,20261123,20261124,20261125 --hours 96 --step-hours 0.10 --population 14 --epochs 36 --hidden-size 64 --action-epochs 52 --action-hidden-size 64 --value-epochs 80 --value-hidden-size 64 --max-value-examples 120000 --value-bias-candidates 0.0,0.75,1.25,1.75,2.50 --device auto --trace-seed 20261121
```

## Training Result

The value head trained tightly on the active-crisis examples:

```text
examples = 120000
final_loss = 0.00719
train_mae = 0.00547
positive_rate = 0.699
```

Validation selected the strongest tested value bias:

| Value bias | Tune total | Tune crisis | Tune resolved | Tune coupled | Selected |
|---:|---:|---:|---:|---:|---|
| `0.00` | `0.513` | `0.000` | `0.000` | `0.006` | no |
| `0.75` | `0.516` | `0.000` | `0.000` | `0.022` | no |
| `1.25` | `0.503` | `0.000` | `0.122` | `0.063` | no |
| `1.75` | `0.511` | `0.000` | `0.067` | `0.057` | no |
| `2.50` | `0.520` | `0.000` | `0.067` | `0.071` | yes |

## Held-Out Result

The active state/action value controller did not improve held-out transfer.

| Controller | Total score | Crisis score | Resolved rate | Coupled response |
|---|---:|---:|---:|---:|
| fixed joint GRU | `0.604` | `0.179` | `0.620` | `0.589` |
| return-selected GRU | `0.520` | `0.000` | `0.033` | `0.026` |
| active state/value GRU | `0.518` | `0.000` | `0.140` | `0.085` |
| designed | `0.768` | `0.522` | `1.000` | `0.000` |
| base GRU | `0.517` | `0.000` | `0.033` | `0.006` |
| frame MLP | `0.313` | `0.000` | `0.000` | `0.000` |
| reactive | `0.117` | `0.000` | `0.000` | `0.000` |

The verdict is:

```text
supports_return_baseline_improvement = false
supports_fixed_joint_improvement = false
supports_active_state_value = false
supports_social_environment_dependency = true
verdict = partial_or_failed
```

## Interpretation

This is a useful failed boundary.

Moving value learning from allocator parameters into active crisis state/action
scoring was not enough. The model learned the step target, and the selected
bias changed behavior enough to improve resolved rate over the return-selected
baseline. But it did not recover held-out crisis score, and it underperformed
the fixed joint controller.

The result rejects the stronger claim:

```text
active state/action value labels alone are sufficient to replace structured
joint crisis coordination
```

The likely bottleneck is temporal credit assignment. The model is scoring
candidate actions from short active-crisis context, but coupled crisis repair
needs delayed sequencing: repair the physical cause, preserve social response,
avoid wrong-channel overfocus, and keep later crisis windows from compounding.

## Ablation Boundary

Because the full active-value controller has `0.000` crisis score, crisis-score
losses cannot prove strong dependency. The response channels still show
specific dependence:

| Ablation | Total loss | Resolved loss | Coupled response loss | Damage increase |
|---|---:|---:|---:|---:|
| `social_culture` | `0.040` | `0.140` | `0.085` | `1.223` |
| `environment` | `-0.000` | `0.140` | `0.085` | `0.193` |
| `previous_action` | `0.031` | `0.107` | `0.054` | `0.033` |
| `tools` | `0.022` | `0.140` | `0.069` | `0.096` |
| `infrastructure` | `0.057` | `0.033` | `0.011` | `0.047` |
| `body` | `0.023` | `0.073` | `0.044` | `0.160` |

This supports only a weak dependency statement: social/culture and environment
channels matter for the partial response behavior, but the active-value
controller has not learned robust crisis repair.

## Next Step

Do not keep adding single-step value rerankers.

The next credible controller should train on temporally extended consequences:

- actor-critic or model-based return learning inside the active crisis window;
- recurrent value memory across the whole crisis, not only per-step context;
- counterfactual traces that include delayed damage, overfocus, and repair debt;
- action selection that can learn new timing, not just choose from supplied
  repair labels;
- held-out worlds where success requires beating the fixed joint controller;
- targeted social/environment ablations that collapse crisis repair after the
  controller already has nonzero crisis score.

## Artifacts

- [script](../experiments/ssrm_3d_coupled_crisis_active_state_value_controller.py)
- [schedule CSV](../artifacts/ssrm_3d_coupled_crisis_active_state_value_schedule.csv)
- [base training CSV](../artifacts/ssrm_3d_coupled_crisis_active_state_value_base_training.csv)
- [action training CSV](../artifacts/ssrm_3d_coupled_crisis_active_state_value_action_training.csv)
- [router selection CSV](../artifacts/ssrm_3d_coupled_crisis_active_state_value_router_selection.csv)
- [value example summary CSV](../artifacts/ssrm_3d_coupled_crisis_active_state_value_value_example_summary.csv)
- [value training CSV](../artifacts/ssrm_3d_coupled_crisis_active_state_value_value_training.csv)
- [value selection CSV](../artifacts/ssrm_3d_coupled_crisis_active_state_value_value_selection.csv)
- [evaluation CSV](../artifacts/ssrm_3d_coupled_crisis_active_state_value_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_coupled_crisis_active_state_value_summary.csv)
- [ablation CSV](../artifacts/ssrm_3d_coupled_crisis_active_state_value_ablations.csv)
- [verdict CSV](../artifacts/ssrm_3d_coupled_crisis_active_state_value_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_coupled_crisis_active_state_value_trace.json)
- [results JSON](../artifacts/ssrm_3d_coupled_crisis_active_state_value_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_coupled_crisis_active_state_value_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_coupled_crisis_active_state_value_results.js)
