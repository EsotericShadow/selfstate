# SSRM-3D Coupled Crisis Active Policy Report

## Question

Report 118 showed that delayed crisis-window labels have real signal, but still
do not produce robust held-out repair.

This report tests the next narrower claim:

```text
Can sampled policy-gradient updates inside active crisis windows learn better
held-out coupled-crisis repair than passive value labels?
```

The benchmark keeps the same basic stress shape:

- `96h` worlds;
- no major crisis before `12h`;
- randomized post-gate crisis timing, order, repetition, and initial pressure;
- learned base GRU;
- fixed-joint learned action-head baseline;
- no crisis profile name in active policy inputs;
- held-out eval seeds with targeted ablations.

## What Changed

The controller no longer only ranks active-crisis actions from supervised or
passive labels. During an active crisis, the policy samples from a supplied
candidate action set:

```text
none, sanitize, treat, scout, construct, social_repair, teach, learn
```

When the crisis ends, the sampled state/action choices receive a return based
on:

- final environmental repair fraction;
- final social repair fraction;
- final coupled repair fraction;
- whether the crisis resolved;
- coupled response during the crisis;
- damage accumulated during the crisis.

The update is a bounded score-function policy-gradient step over the crisis
window. This is a step toward active consequence learning, but it is still not
a full actor-critic system, not open-ended civilization, and not evidence of
subjective consciousness.

## Runtime Boundary

An earlier full-budget attempt with `6` train seeds, `3` tune seeds, `5` eval
seeds, and `10` policy epochs was too slow for a maintainable canonical suite
entry. It was stopped after exposing excessive runtime.

The implementation was then fixed to store compact sampled state/action pairs
and recompute log-probs in one batched crisis-end update. The canonical Report
119 budget below keeps `96h` worlds but uses a smaller seed/epoch budget so the
experiment remains rerunnable.

## Canonical Command

```bash
python3 experiments/ssrm_3d_coupled_crisis_active_policy_controller.py --train-seeds 20260911,20260912,20260913 --tune-seeds 20261111,20261112 --eval-seeds 20261121,20261122,20261123 --hours 96 --step-hours 0.10 --population 14 --epochs 24 --hidden-size 64 --action-epochs 32 --action-hidden-size 64 --policy-epochs 4 --policy-hidden-size 64 --policy-learning-rate 0.003 --entropy-coef 0.008 --policy-temperature 1.0 --policy-bias-candidates 0.0,0.20,0.40,0.70,1.00 --device auto --trace-seed 20261121
```

## Training Result

The active policy trained on the reduced target budget:

```text
episodes = 12
training_crises = 73
policy_parameters = 10312
mean_return = 1.488
return_std = 1.090
mean_entropy = 1.510
final_loss = 0.555
device = mps
```

This confirms that the policy-gradient loop is executing over completed crisis
windows. It does not prove that the learned policy transfers.

## Selection Result

Validation selected `policy_bias = 0.0`.

| Policy bias | Tune total | Tune crisis | Tune resolved | Tune coupled | Tune damage | Selected |
|---:|---:|---:|---:|---:|---:|---|
| `0.00` | `0.520` | `0.000` | `0.000` | `0.000` | `2.564` | yes |
| `0.20` | `0.519` | `0.000` | `0.000` | `0.000` | `2.625` | no |
| `0.40` | `0.506` | `0.000` | `0.000` | `0.000` | `2.555` | no |
| `0.70` | `0.496` | `0.000` | `0.000` | `0.000` | `2.647` | no |
| `1.00` | `0.503` | `0.000` | `0.000` | `0.000` | `2.660` | no |

The selected policy is not "policy disabled"; it means no extra bias is added
to non-`none` actions. The policy logits still choose active-crisis candidates.

## Held-Out Result

The active policy improves coupled response over the return-selected GRU, but
it still fails the strong repair gate.

| Controller | Total score | Crisis score | Resolved rate | Coupled response |
|---|---:|---:|---:|---:|
| designed | `0.770` | `0.522` | `1.000` | `0.000` |
| fixed joint GRU | `0.688` | `0.349` | `0.700` | `0.693` |
| active policy GRU | `0.520` | `0.000` | `0.178` | `0.147` |
| return-selected GRU | `0.520` | `0.000` | `0.111` | `0.028` |
| base GRU | `0.323` | `0.000` | `0.000` | `0.009` |
| frame MLP | `0.315` | `0.000` | `0.000` | `0.000` |
| reactive | `0.104` | `0.000` | `0.000` | `0.000` |

The verdict is:

```text
supports_return_baseline_improvement = false
supports_fixed_joint_improvement = false
supports_active_policy_learning = false
supports_social_environment_dependency = false
verdict = partial_or_failed
```

## Interpretation

This is a useful boundary, not a pass.

The active policy does something real: coupled response rises from `0.028` in
the return-selected GRU to `0.147`, and resolved rate rises from `0.111` to
`0.178`.

But the strong claim still fails:

- crisis score remains `0.000`;
- total score only improves over return-selected by `0.0003`;
- fixed-joint coordination is far stronger, with crisis score `0.349`,
  resolved rate `0.700`, and coupled response `0.693`;
- social/environment ablations collapse coupled response, but the base crisis
  score is already collapsed, so the ablation gate cannot pass.

This says sampled active policy updates are closer to the right training
shape, but the current lightweight score-function policy is not enough. The
crisis repair problem still needs stronger sequential credit assignment,
probably actor-critic or model-based return learning with recurrent crisis
state.

## Ablation Boundary

Because the full active-policy controller has `0.000` crisis score, the
crisis-score dependency gate cannot pass. The response channels show partial
dependence:

| Ablation | Total loss | Resolved loss | Coupled response loss | Damage increase |
|---|---:|---:|---:|---:|
| `social_culture` | `0.058` | `0.178` | `0.147` | `0.272` |
| `environment` | `0.015` | `0.178` | `0.147` | `-0.534` |
| `infrastructure` | `0.143` | `0.178` | `0.146` | `0.345` |
| `body` | `0.028` | `0.122` | `0.115` | `0.147` |
| `previous_action` | `0.003` | `0.000` | `0.072` | `0.099` |
| `tools` | `0.001` | `0.000` | `0.010` | `0.037` |

The policy has learned some dependence on social/environment channels for
coupled response. It has not learned enough to make crisis repair succeed.

## Next Step

Do not claim active policy learning solved the coupled-crisis problem.

The next credible experiment should use a stronger learner:

- recurrent actor-critic state across the full active crisis;
- model-based return search over repair sequences;
- critic/value baselines that reduce policy-gradient variance;
- action discovery pressure beyond the supplied candidate set;
- held-out transfer against fixed-joint arbitration;
- targeted ablations only after the learned controller has nonzero crisis
  score.

## Artifacts

- [script](../experiments/ssrm_3d_coupled_crisis_active_policy_controller.py)
- [schedule CSV](../artifacts/ssrm_3d_coupled_crisis_active_policy_schedule.csv)
- [base training CSV](../artifacts/ssrm_3d_coupled_crisis_active_policy_base_training.csv)
- [action training CSV](../artifacts/ssrm_3d_coupled_crisis_active_policy_action_training.csv)
- [router selection CSV](../artifacts/ssrm_3d_coupled_crisis_active_policy_router_selection.csv)
- [policy training CSV](../artifacts/ssrm_3d_coupled_crisis_active_policy_policy_training.csv)
- [policy selection CSV](../artifacts/ssrm_3d_coupled_crisis_active_policy_policy_selection.csv)
- [evaluation CSV](../artifacts/ssrm_3d_coupled_crisis_active_policy_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_coupled_crisis_active_policy_summary.csv)
- [ablation CSV](../artifacts/ssrm_3d_coupled_crisis_active_policy_ablations.csv)
- [verdict CSV](../artifacts/ssrm_3d_coupled_crisis_active_policy_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_coupled_crisis_active_policy_trace.json)
- [results JSON](../artifacts/ssrm_3d_coupled_crisis_active_policy_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_coupled_crisis_active_policy_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_coupled_crisis_active_policy_results.js)
