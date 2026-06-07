# SSRM-3D Coupled Crisis Process Policy Report

## Question

Report 121 showed that recurrent hidden state across the active crisis window
did not solve coupled repair. The policy trained, but held-out crisis score,
resolved rate, and coupled response all stayed at `0.000`.

This report tests the next narrower claim:

```text
Does explicit two-channel process pressure make sampled crisis-policy learning
preserve both environmental and social repair during held-out crises?
```

The benchmark keeps the hard setting:

- `96h` worlds;
- no major crisis before `12h`;
- randomized post-gate crisis timing, order, repetition, and initial pressure;
- learned base GRU;
- fixed-joint learned action-head baseline;
- recurrent active-crisis policy state;
- no crisis profile name in process-policy inputs;
- held-out eval seeds with targeted ablations.

## What Changed

The controller still samples from the same supplied candidate actions:

```text
none, sanitize, treat, scout, construct, social_repair, teach, learn
```

The new part is a two-channel process target. During each active crisis, the
policy receives an auxiliary loss that tries to keep environmental and social
repair pressure active instead of letting the policy collapse to one channel.
The completed crisis-window return also penalizes imbalance and rewards coupled
progress.

This directly tests the Report 121 hypothesis that the failure was not only
model memory, but training pressure that failed to punish one-channel repair.
It is still not open-ended civilization, not unsupplied action discovery, and
not evidence of subjective consciousness.

## Canonical Command

```bash
python3 experiments/ssrm_3d_coupled_crisis_process_policy_controller.py --train-seeds 20260911,20260912,20260913 --tune-seeds 20261111,20261112 --eval-seeds 20261121,20261122,20261123 --hours 96 --step-hours 0.10 --population 14 --epochs 24 --hidden-size 64 --action-epochs 32 --action-hidden-size 64 --policy-epochs 4 --policy-hidden-size 64 --memory-epochs 5 --memory-hidden-size 64 --process-epochs 5 --process-hidden-size 64 --process-learning-rate 0.003 --process-loss-coef 0.35 --entropy-coef 0.008 --policy-temperature 1.0 --policy-bias-candidates 0.0,0.20,0.40,0.70,1.00 --device auto --trace-seed 20261121
```

## Training Result

The process policy trained across completed crisis sequences:

```text
episodes = 15
training_crises = 91
process_epochs = 5
parameters = 29640
mean_return = 2.859
return_std = 0.926
moving_baseline = 3.145
mean_sequence_length = 1312.9
mean_entropy = 1.634
process_loss_coef = 0.35
final_loss = 0.442
final_policy_loss = 0.082
final_process_loss = 1.027
device = mps
```

This confirms that the auxiliary process-learning path executed. It does not
prove that the policy learned transferable coupled repair.

## Selection Result

Validation selected `policy_bias = 0.40`.

| Policy bias | Tune total | Tune crisis | Tune resolved | Tune env | Tune social | Tune coupled | Tune damage | Selected |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `0.00` | `0.520` | `0.000` | `0.000` | `0.002` | `1.000` | `0.002` | `1.668` | no |
| `0.20` | `0.520` | `0.000` | `0.000` | `0.003` | `1.000` | `0.003` | `1.649` | no |
| `0.40` | `0.516` | `0.000` | `0.000` | `0.003` | `1.000` | `0.003` | `1.640` | yes |
| `0.70` | `0.511` | `0.000` | `0.000` | `0.000` | `1.000` | `0.000` | `1.703` | no |
| `1.00` | `0.520` | `0.000` | `0.000` | `0.000` | `1.000` | `0.000` | `1.731` | no |

Every selected/tune row still has `0.000` crisis score and `0.000` resolved
rate. Selection again optimizes around partial side effects rather than actual
coupled repair.

## Held-Out Result

The process policy does not improve over the recurrent memory policy, the
active-policy baseline, the return-selected GRU, or fixed-joint coordination.

| Controller | Total score | Crisis score | Resolved rate | Env response | Social response | Coupled response |
|---|---:|---:|---:|---:|---:|---:|
| designed | `0.770` | `0.522` | `1.000` | `0.077` | `0.923` | `0.000` |
| fixed joint GRU | `0.727` | `0.432` | `0.756` | `0.731` | `1.000` | `0.731` |
| active policy GRU | `0.520` | `0.000` | `0.178` | `0.270` | `0.229` | `0.147` |
| return-selected GRU | `0.520` | `0.000` | `0.111` | `0.299` | `0.372` | `0.028` |
| memory policy GRU | `0.517` | `0.000` | `0.000` | `0.178` | `0.000` | `0.000` |
| process policy GRU | `0.504` | `0.000` | `0.000` | `0.000` | `1.000` | `0.000` |
| base GRU | `0.323` | `0.000` | `0.000` | `0.299` | `0.009` | `0.009` |
| frame MLP | `0.315` | `0.000` | `0.000` | `0.299` | `0.000` | `0.000` |
| reactive | `0.104` | `0.000` | `0.000` | `0.205` | `0.000` | `0.000` |

The verdict is:

```text
supports_memory_policy_improvement = false
supports_active_policy_improvement = false
supports_return_baseline_improvement = false
supports_fixed_joint_improvement = false
supports_process_policy_learning = false
supports_social_environment_dependency = false
verdict = partial_or_failed
```

## Interpretation

This is a useful negative boundary.

The process loss did not produce two-channel repair. It produced the opposite
one-channel collapse from Report 121:

- memory-policy environmental response was `0.178`;
- memory-policy social response was `0.000`;
- process-policy environmental response is `0.000`;
- process-policy social response is `1.000`;
- process-policy coupled response is `0.000`;
- fixed-joint coupled response is `0.731`.

So the failure is now sharper. The learner can receive an explicit process
target, train recurrently inside the active crisis window, and still learn a
policy that looks highly responsive in one channel while failing the coupled
task. This means the current auxiliary objective is not enough. It does not
make environmental and social repair inseparable in the learned policy.

The public lesson is important: adding richer world mechanics or more internal
state is not the same as solving mature agency. The benchmark still needs
training pressure and architecture that make coordinated consequence repair
transfer across held-out worlds.

## Ablation Boundary

Because the full process policy has `0.000` crisis score and `0.000` coupled
response, targeted crisis dependency cannot pass.

| Ablation | Total loss | Crisis loss | Resolved loss | Env response loss | Social response loss | Coupled response loss |
|---|---:|---:|---:|---:|---:|---:|
| `body` | `0.011` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` |
| `infrastructure` | `0.012` | `0.000` | `0.000` | `-0.007` | `0.061` | `-0.006` |
| `tools` | `-0.001` | `0.000` | `0.000` | `-0.012` | `0.075` | `-0.007` |
| `social_culture` | `0.247` | `0.000` | `0.000` | `-0.122` | `1.000` | `0.000` |
| `environment` | `0.010` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` |
| `previous_action` | `-0.010` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` |

The social/culture ablation has a large total-score effect because the selected
process policy leans entirely into the social channel. That does not count as a
successful coupled-crisis dependency, because environmental response and
coupled response are still absent.

## Next Step

Do not claim that two-channel process pressure solved the coupled-crisis
problem.

The next credible step should stop treating the crisis learner as a shallow
overlay around supplied action probabilities. Stronger options:

- train a model-based repair planner on counterfactual crisis rollouts, then
  distill multi-step plans rather than per-step process labels;
- train with explicit minimum-channel objectives where reward is bounded by the
  weaker of environmental and social progress;
- expand active exploration so the policy sees successful coupled trajectories,
  not only damaged one-channel recoveries;
- add causal state edits during active crises to test whether the learned policy
  actually binds environmental and social repair variables;
- keep fixed-joint coordination as the comparison baseline until the learned
  controller recovers nonzero held-out crisis score.

## Artifacts

- [script](../experiments/ssrm_3d_coupled_crisis_process_policy_controller.py)
- [schedule CSV](../artifacts/ssrm_3d_coupled_crisis_process_policy_schedule.csv)
- [base training CSV](../artifacts/ssrm_3d_coupled_crisis_process_policy_base_training.csv)
- [action training CSV](../artifacts/ssrm_3d_coupled_crisis_process_policy_action_training.csv)
- [router selection CSV](../artifacts/ssrm_3d_coupled_crisis_process_policy_router_selection.csv)
- [active-policy training CSV](../artifacts/ssrm_3d_coupled_crisis_process_policy_active_policy_training.csv)
- [active-policy selection CSV](../artifacts/ssrm_3d_coupled_crisis_process_policy_active_policy_selection.csv)
- [memory-policy training CSV](../artifacts/ssrm_3d_coupled_crisis_process_policy_memory_policy_training.csv)
- [memory-policy selection CSV](../artifacts/ssrm_3d_coupled_crisis_process_policy_memory_policy_selection.csv)
- [process-policy training CSV](../artifacts/ssrm_3d_coupled_crisis_process_policy_process_policy_training.csv)
- [process-policy selection CSV](../artifacts/ssrm_3d_coupled_crisis_process_policy_process_policy_selection.csv)
- [evaluation CSV](../artifacts/ssrm_3d_coupled_crisis_process_policy_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_coupled_crisis_process_policy_summary.csv)
- [ablation CSV](../artifacts/ssrm_3d_coupled_crisis_process_policy_ablations.csv)
- [verdict CSV](../artifacts/ssrm_3d_coupled_crisis_process_policy_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_coupled_crisis_process_policy_trace.json)
- [results JSON](../artifacts/ssrm_3d_coupled_crisis_process_policy_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_coupled_crisis_process_policy_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_coupled_crisis_process_policy_results.js)
