# SSRM-3D Coupled Crisis Temporal Return Value Report

## Question

Report 117 moved value learning into active crisis state/action scoring, but the
label was still a single-step consequence.

This report tests the next narrower claim:

```text
Can Monte Carlo-style crisis-window return labels improve held-out 96h
coupled-crisis repair?
```

The benchmark keeps the same randomized-transfer world:

- `96h` runs;
- no major crisis before `12h`;
- randomized post-gate crisis timing, order, repetition, and initial pressure;
- learned base GRU;
- learned environmental and social action heads;
- no crisis profile name in runtime value inputs.

## What Changed

The value model no longer learns only a one-step repair score. During training,
actions taken inside an active crisis window are stored and then labeled after
the crisis ends.

Each training label reflects the later crisis-window outcome:

- final environmental repair fraction;
- final social repair fraction;
- final coupled repair fraction;
- whether the crisis resolved;
- progress from the stored step to the final crisis state;
- damage accumulated after the step.

This makes the label temporally extended. It still does not make the controller
full actor-critic reinforcement learning.

## What This Does Not Claim

This is not subjective consciousness, open-ended civilization, or real-world
competence.

The candidate action set is still supplied. The environmental and social action
heads are still supervised. The temporal value model learns from completed
crisis windows, not from arbitrary online exploration with policy gradients.

## Canonical Command

```bash
python3 experiments/ssrm_3d_coupled_crisis_temporal_return_value_controller.py --train-seeds 20260911,20260912,20260913,20260914,20260915,20260916 --tune-seeds 20261111,20261112,20261113 --eval-seeds 20261121,20261122,20261123,20261124,20261125 --hours 96 --step-hours 0.10 --population 14 --epochs 36 --hidden-size 64 --action-epochs 52 --action-hidden-size 64 --value-epochs 80 --value-hidden-size 64 --max-value-examples 120000 --value-bias-candidates 0.0,0.75,1.25,1.75,2.50,3.50 --device auto --trace-seed 20261121
```

## Training Result

The temporal value head trained on the full requested budget:

```text
examples = 120000
final_loss = 0.00072
train_mae = 0.03070
target_mean = 0.560
target_std = 1.554
positive_rate = 0.529
```

The temporal labels separate stronger source policies from the weak
return-selected policy:

| Source policy | Examples | Mean target | Positive rate |
|---|---:|---:|---:|
| `high_env_joint` | `24473` | `1.503` | `0.833` |
| `fixed_joint` | `47258` | `1.417` | `0.797` |
| `return_selected` | `48269` | `-0.756` | `0.113` |

That is a real label signal. It does not by itself prove online transfer.

## Selection Result

Validation selected `value_bias = 2.5`.

| Value bias | Tune total | Tune crisis | Tune resolved | Tune coupled | Selected |
|---:|---:|---:|---:|---:|---|
| `0.00` | `0.513` | `0.000` | `0.000` | `0.006` | no |
| `0.75` | `0.511` | `0.000` | `0.244` | `0.129` | no |
| `1.25` | `0.504` | `0.000` | `0.122` | `0.083` | no |
| `1.75` | `0.520` | `0.000` | `0.189` | `0.114` | no |
| `2.50` | `0.520` | `0.000` | `0.378` | `0.133` | yes |
| `3.50` | `0.520` | `0.000` | `0.178` | `0.071` | no |

## Held-Out Result

The temporal-return controller improved some response behavior over the
return-selected GRU, but it still failed the strong transfer gate.

| Controller | Total score | Crisis score | Resolved rate | Coupled response |
|---|---:|---:|---:|---:|
| fixed joint GRU | `0.652` | `0.279` | `0.687` | `0.630` |
| return-selected GRU | `0.520` | `0.000` | `0.033` | `0.026` |
| temporal-return value GRU | `0.518` | `0.000` | `0.280` | `0.085` |
| designed | `0.768` | `0.522` | `1.000` | `0.000` |
| base GRU | `0.517` | `0.000` | `0.033` | `0.006` |
| frame MLP | `0.313` | `0.000` | `0.000` | `0.000` |
| reactive | `0.117` | `0.000` | `0.000` | `0.000` |

The verdict is:

```text
supports_return_baseline_improvement = false
supports_fixed_joint_improvement = false
supports_temporal_return_value = false
supports_social_environment_dependency = false
verdict = partial_or_failed
```

## Interpretation

This is another useful boundary, not a pass.

The temporal labels are more meaningful than the one-step labels. They can
distinguish fixed/joint repair rollouts from return-selected rollouts, and the
selected controller improves held-out resolved rate over the return-selected
GRU:

```text
resolved rate: 0.033 -> 0.280
coupled response: 0.026 -> 0.085
```

But that is not enough. Held-out crisis score remains `0.000`, total score
falls slightly below the return-selected GRU, and the fixed-joint controller is
far stronger:

```text
fixed joint crisis score = 0.279
temporal-return crisis score = 0.000
```

The likely bottleneck is still credit assignment through action selection. The
value model sees delayed outcome labels, but the controller is still choosing
from supplied candidates around supervised action heads. It can nudge response,
but it does not learn a robust repair policy that balances environmental repair,
social repair, damage, and timing.

## Ablation Boundary

Because the full temporal-return controller has `0.000` crisis score, the
crisis-score ablation gate cannot pass. The response channels still show partial
dependence:

| Ablation | Total loss | Resolved loss | Coupled response loss | Damage increase |
|---|---:|---:|---:|---:|
| `social_culture` | `0.001` | `0.280` | `0.085` | `0.771` |
| `environment` | `-0.002` | `0.280` | `0.085` | `-0.029` |
| `previous_action` | `0.015` | `0.000` | `0.010` | `-0.134` |
| `body` | `0.009` | `0.107` | `0.000` | `0.486` |
| `tools` | `0.012` | `-0.033` | `-0.045` | `-0.007` |
| `infrastructure` | `0.067` | `0.067` | `-0.015` | `0.370` |

The social/culture and environment removals both collapse coupled response, but
the base crisis score is already collapsed. This means the ablation evidence
only supports a weak response-dependency statement.

## Next Step

Do not keep adding passive value labels around the same action heads.

The next credible step is active policy learning inside the crisis window:

- actor-critic or model-based return learning over crisis actions;
- recurrent value state across the whole crisis, not only stored outcome labels;
- exploration that can discover repair timing instead of only ranking supplied
  repair candidates;
- explicit penalty for high-damage "resolved but costly" repair;
- held-out transfer against the fixed-joint controller;
- targeted ablations after the learned controller has nonzero crisis score.

## Artifacts

- [script](../experiments/ssrm_3d_coupled_crisis_temporal_return_value_controller.py)
- [schedule CSV](../artifacts/ssrm_3d_coupled_crisis_temporal_return_value_schedule.csv)
- [base training CSV](../artifacts/ssrm_3d_coupled_crisis_temporal_return_value_base_training.csv)
- [action training CSV](../artifacts/ssrm_3d_coupled_crisis_temporal_return_value_action_training.csv)
- [router selection CSV](../artifacts/ssrm_3d_coupled_crisis_temporal_return_value_router_selection.csv)
- [temporal example summary CSV](../artifacts/ssrm_3d_coupled_crisis_temporal_return_value_temporal_example_summary.csv)
- [value training CSV](../artifacts/ssrm_3d_coupled_crisis_temporal_return_value_value_training.csv)
- [value selection CSV](../artifacts/ssrm_3d_coupled_crisis_temporal_return_value_value_selection.csv)
- [evaluation CSV](../artifacts/ssrm_3d_coupled_crisis_temporal_return_value_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_coupled_crisis_temporal_return_value_summary.csv)
- [ablation CSV](../artifacts/ssrm_3d_coupled_crisis_temporal_return_value_ablations.csv)
- [verdict CSV](../artifacts/ssrm_3d_coupled_crisis_temporal_return_value_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_coupled_crisis_temporal_return_value_trace.json)
- [results JSON](../artifacts/ssrm_3d_coupled_crisis_temporal_return_value_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_coupled_crisis_temporal_return_value_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_coupled_crisis_temporal_return_value_results.js)
