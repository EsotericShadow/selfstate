# SSRM-3D Coupled Crisis Actor-Critic Report

## Question

Report 119 moved from passive labels to sampled action updates inside active
crisis windows. It improved coupled response, but it still could not recover
nonzero held-out crisis score.

This report tests the next narrower claim:

```text
Does adding a learned value baseline to the sampled active-crisis policy make
the controller solve held-out coupled social/environment crises?
```

The benchmark keeps the same stress boundary:

- `96h` worlds;
- no major crisis before `12h`;
- randomized post-gate crisis timing, order, repetition, and initial pressure;
- learned base GRU;
- fixed-joint learned action-head baseline;
- no crisis profile name in actor-critic inputs;
- held-out eval seeds with targeted ablations.

## What Changed

The active policy from Report 119 is extended with a critic head. During active
crises, the actor samples from the same candidate action set:

```text
none, sanitize, treat, scout, construct, social_repair, teach, learn
```

At crisis end, completed-crisis return is used to train:

- an actor loss from advantage-weighted sampled actions;
- a value loss from predicted crisis return;
- entropy regularization for exploration.

This is a bounded actor-critic value-baseline test. It is not full recurrent
backpropagation through the crisis trajectory, not model-based planning, not
open-ended civilization, and not evidence of subjective consciousness.

## Canonical Command

```bash
python3 experiments/ssrm_3d_coupled_crisis_actor_critic_controller.py --train-seeds 20260911,20260912,20260913 --tune-seeds 20261111,20261112 --eval-seeds 20261121,20261122,20261123 --hours 96 --step-hours 0.10 --population 14 --epochs 24 --hidden-size 64 --action-epochs 32 --action-hidden-size 64 --policy-epochs 4 --policy-hidden-size 64 --actor-critic-epochs 4 --actor-critic-hidden-size 64 --actor-critic-learning-rate 0.003 --entropy-coef 0.008 --value-coef 0.45 --policy-temperature 1.0 --policy-bias-candidates 0.0,0.20,0.40,0.70,1.00 --device auto --trace-seed 20261121
```

## Training Result

The actor-critic loop executed over completed crises:

```text
episodes = 12
training_crises = 71
actor_critic_epochs = 4
parameters = 10377
mean_return = 2.256
return_std = 0.449
mean_value_prediction = 2.300
mean_abs_advantage = 0.386
mean_entropy = 1.989
final_loss = 0.117
final_policy_loss = 0.132
final_value_loss = 0.004
device = mps
```

The critic did learn a tight return baseline on the sampled training windows.
That did not translate into useful held-out crisis action.

## Selection Result

Validation selected `policy_bias = 0.20`.

| Policy bias | Tune total | Tune crisis | Tune resolved | Tune coupled | Tune damage | Selected |
|---:|---:|---:|---:|---:|---:|---|
| `0.00` | `0.499` | `0.000` | `0.000` | `0.000` | `2.756` | no |
| `0.20` | `0.502` | `0.000` | `0.000` | `0.000` | `2.756` | yes |
| `0.40` | `0.520` | `0.000` | `0.000` | `0.000` | `2.783` | no |
| `0.70` | `0.510` | `0.000` | `0.000` | `0.000` | `2.877` | no |
| `1.00` | `0.511` | `0.000` | `0.000` | `0.000` | `2.773` | no |

The selected bias is not a pass. All actor-critic tune rows still have `0.000`
crisis score, `0.000` resolved rate, and `0.000` coupled response.

## Held-Out Result

The actor-critic value baseline underperforms the previous active-policy
controller and the fixed-joint structured baseline.

| Controller | Total score | Crisis score | Resolved rate | Coupled response |
|---|---:|---:|---:|---:|
| designed | `0.770` | `0.522` | `1.000` | `0.000` |
| fixed joint GRU | `0.594` | `0.155` | `0.589` | `0.552` |
| active policy GRU | `0.520` | `0.000` | `0.178` | `0.147` |
| return-selected GRU | `0.520` | `0.000` | `0.111` | `0.028` |
| actor-critic GRU | `0.504` | `0.000` | `0.000` | `0.000` |
| base GRU | `0.323` | `0.000` | `0.000` | `0.009` |
| frame MLP | `0.315` | `0.000` | `0.000` | `0.000` |
| reactive | `0.104` | `0.000` | `0.000` | `0.000` |

The verdict is:

```text
supports_active_policy_improvement = false
supports_return_baseline_improvement = false
supports_fixed_joint_improvement = false
supports_actor_critic_learning = false
supports_social_environment_dependency = false
verdict = partial_or_failed
```

## Interpretation

This is a useful negative boundary.

The value head trained, but adding it did not make the sampled crisis policy
field-competent. The actor-critic controller lost the partial behavior that
Report 119 had:

- active policy coupled response was `0.147`;
- actor-critic coupled response fell to `0.000`;
- active policy resolved rate was `0.178`;
- actor-critic resolved rate fell to `0.000`;
- fixed-joint coordination remains much stronger.

The likely lesson is that this budget and architecture are reducing variance
without solving the temporal credit-assignment problem. The crisis requires a
sequence of compatible environmental and social repairs. A per-step actor with
a compact critic baseline can still collapse into actions that look locally
reasonable but do not preserve both repair channels across the window.

## Ablation Boundary

The actor-critic controller has no nonzero crisis behavior to ablate cleanly.
All crisis-score and coupled-response losses are `0.000`.

| Ablation | Total loss | Crisis loss | Resolved loss | Coupled response loss |
|---|---:|---:|---:|---:|
| `body` | `0.013` | `0.000` | `0.000` | `0.000` |
| `infrastructure` | `0.092` | `0.000` | `0.000` | `0.000` |
| `tools` | `0.018` | `0.000` | `0.000` | `0.000` |
| `social_culture` | `0.222` | `0.000` | `0.000` | `0.000` |
| `environment` | `-0.016` | `0.000` | `0.000` | `0.000` |
| `previous_action` | `-0.016` | `0.000` | `0.000` | `0.000` |

Because the base behavior is collapsed, these ablations cannot support a
dependency claim.

## Next Step

Do not claim actor-critic learning solved the coupled-crisis problem.

The next credible controller needs stronger sequential credit assignment, such
as:

- recurrent actor-critic state carried across the whole active crisis;
- backpropagation through crisis-window hidden trajectories;
- generalized advantage estimation or better advantage normalization;
- model-based search over repair sequences;
- explicit comparison to structured fixed-joint coordination on held-out
  worlds;
- targeted ablations only after the learned policy has nonzero crisis score.

## Artifacts

- [script](../experiments/ssrm_3d_coupled_crisis_actor_critic_controller.py)
- [schedule CSV](../artifacts/ssrm_3d_coupled_crisis_actor_critic_schedule.csv)
- [base training CSV](../artifacts/ssrm_3d_coupled_crisis_actor_critic_base_training.csv)
- [action training CSV](../artifacts/ssrm_3d_coupled_crisis_actor_critic_action_training.csv)
- [router selection CSV](../artifacts/ssrm_3d_coupled_crisis_actor_critic_router_selection.csv)
- [active-policy training CSV](../artifacts/ssrm_3d_coupled_crisis_actor_critic_active_policy_training.csv)
- [active-policy selection CSV](../artifacts/ssrm_3d_coupled_crisis_actor_critic_active_policy_selection.csv)
- [actor-critic training CSV](../artifacts/ssrm_3d_coupled_crisis_actor_critic_actor_critic_training.csv)
- [actor-critic selection CSV](../artifacts/ssrm_3d_coupled_crisis_actor_critic_actor_critic_selection.csv)
- [evaluation CSV](../artifacts/ssrm_3d_coupled_crisis_actor_critic_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_coupled_crisis_actor_critic_summary.csv)
- [ablation CSV](../artifacts/ssrm_3d_coupled_crisis_actor_critic_ablations.csv)
- [verdict CSV](../artifacts/ssrm_3d_coupled_crisis_actor_critic_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_coupled_crisis_actor_critic_trace.json)
- [results JSON](../artifacts/ssrm_3d_coupled_crisis_actor_critic_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_coupled_crisis_actor_critic_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_coupled_crisis_actor_critic_results.js)
