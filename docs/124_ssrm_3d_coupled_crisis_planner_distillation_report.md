# SSRM-3D Coupled Crisis Planner Distillation Report

## Question

Report 123 showed that a dynamic weakest-channel planner can preserve coupled
environmental and social crisis repair in randomized 96h worlds.

This report tests the next narrower claim:

```text
Can that successful minimum-channel planner be distilled into a recurrent
active-crisis policy, then removed at evaluation, while preserving held-out
coupled crisis repair?
```

The benchmark keeps the same hard setting:

- `96h` worlds;
- no major crisis before `12h`;
- randomized post-gate crisis timing, order, repetition, and initial pressure;
- learned base GRU;
- learned environmental and social crisis action heads;
- return-selected GRU, fixed-joint, and minimum-channel planner baselines;
- targeted social/environment ablations.

## What Changed

The distilled controller collects teacher trajectories from the selected
Report 123 minimum-channel planner. It trains a recurrent active-crisis policy
over the same policy features used by Reports 119-122.

At evaluation, the distilled policy no longer calls the minimum-channel
planner. It can choose active crisis actions directly; when it chooses `none`,
control falls back to the learned base GRU.

This tests policy distillation. It is not open-ended role discovery, not
unsupplied action discovery, not subjective consciousness, and not mature
actor-critic reinforcement learning.

## Canonical Command

```bash
python3 experiments/ssrm_3d_coupled_crisis_planner_distillation_controller.py --train-seeds 20260911,20260912,20260913 --tune-seeds 20261111,20261112 --eval-seeds 20261121,20261122,20261123 --hours 96 --step-hours 0.10 --population 14 --epochs 24 --hidden-size 64 --action-epochs 32 --action-hidden-size 64 --distill-epochs 12 --distill-hidden-size 64 --policy-bias-candidates 0.0,0.20,0.40,0.70,1.00 --device auto --trace-seed 20261121
```

## Training Result

The distilled policy imitates the planner traces very well offline:

| Metric | Value |
|---|---:|
| Teacher crisis sequences | `19` |
| Training examples | `24568` |
| Final distillation loss | `0.0405` |
| Train accuracy | `0.986` |
| Environment-label fraction | `0.186` |
| Social-label fraction | `0.237` |
| None-label fraction | `0.577` |

This is important because the failure below is not simply "the recurrent policy
could not fit the teacher labels." It can fit them. The problem appears when
the policy is placed back into closed-loop held-out worlds.

## Policy Bias Selection

Validation selected policy bias `0.7`.

| Bias | Tune total | Tune crisis | Tune resolved | Tune env | Tune social | Tune coupled | Selected |
|---:|---:|---:|---:|---:|---:|---:|---|
| `0.0` | `0.502` | `0.000` | `0.000` | `0.167` | `0.166` | `0.000` | no |
| `0.2` | `0.520` | `0.000` | `0.000` | `0.185` | `0.466` | `0.000` | no |
| `0.4` | `0.514` | `0.000` | `0.000` | `0.167` | `0.582` | `0.000` | no |
| `0.7` | `0.511` | `0.000` | `0.350` | `0.301` | `0.576` | `0.017` | yes |
| `1.0` | `0.515` | `0.000` | `0.267` | `0.227` | `0.749` | `0.083` | no |

Validation could find some response behavior, but it could not find nonzero
tune crisis score.

## Held-Out Result

The distilled policy does not pass the planner-removal gate.

| Controller | Total score | Crisis score | Resolved rate | Env response | Social response | Coupled response |
|---|---:|---:|---:|---:|---:|---:|
| fixed joint GRU | `0.843` | `0.675` | `0.933` | `0.863` | `1.000` | `0.863` |
| min-channel planner GRU | `0.797` | `0.590` | `0.878` | `0.828` | `1.000` | `0.828` |
| designed | `0.760` | `0.522` | `1.000` | `0.077` | `0.923` | `0.000` |
| planner-distilled GRU | `0.509` | `0.000` | `0.289` | `0.307` | `0.586` | `0.179` |
| return-selected GRU | `0.496` | `0.000` | `0.000` | `0.299` | `0.219` | `0.000` |
| base GRU | `0.344` | `0.000` | `0.000` | `0.299` | `0.111` | `0.000` |
| frame MLP | `0.283` | `0.000` | `0.000` | `0.299` | `0.000` | `0.000` |
| reactive | `0.086` | `0.000` | `0.000` | `0.176` | `0.000` | `0.000` |

The verdict is:

```text
mean_crisis_count = 5.667
supports_planner_distillation = false
supports_teacher_transfer = false
supports_social_environment_dependency = false
verdict = partial_or_failed
```

The distilled controller improves total score over the return-selected GRU by
only `0.014`. It raises resolved rate from `0.000` to `0.289` and coupled
response from `0.000` to `0.179`, but crisis score remains `0.000`.

## Ablation Boundary

The ablations are not sufficient to support the strong dependency claim because
the unablated distilled policy already has `0.000` crisis score.

| Ablation | Crisis score | Crisis loss | Coupled response | Coupled loss |
|---|---:|---:|---:|---:|
| none | `0.000` | - | `0.179` | - |
| social_culture | `0.000` | `0.000` | `0.000` | `0.179` |
| environment | `0.000` | `0.000` | `0.000` | `0.179` |
| previous_action | `0.000` | `0.000` | `0.028` | `0.152` |
| body | `0.000` | `0.000` | `0.006` | `0.173` |
| tools | `0.000` | `0.000` | `0.089` | `0.091` |
| infrastructure | `0.000` | `0.000` | `0.022` | `0.157` |

Removing social/culture or environment eliminates the partial coupled response,
but because the base crisis score is already zero, this does not prove
successful coupled crisis repair.

## Interpretation

This is a useful negative boundary.

The recurrent policy fits the planner traces offline, but closed-loop held-out
rollouts still fail the actual crisis objective once the engineered
minimum-channel planner is removed. That means Report 123's success is not yet
distilled into an active learned policy.

The most likely lesson is that one-step imitation of planner actions does not
capture the planner's closed-loop allocation process. The learner sees state and
teacher action, but it is not directly trained to preserve future channel
balance, diagnose starving repair channels, or recover after its own earlier
mistakes push the rollout off the teacher trajectory.

The result should not be hidden as a failed process. It is evidence that the
current learned-controller stack still needs stronger closed-loop training,
counterfactual correction, or sequence-level process/value targets before it
can retire engineered weakest-channel planning.

## Next Step

Do not claim open-ended learned civilization.

The next credible step is not another visual layer. It is to train the crisis
policy against closed-loop consequences of its own actions:

- use teacher forcing only as initialization, not the final objective;
- add DAgger-style correction where the student visits off-teacher states and
  the planner relabels recovery actions;
- train a sequence-level value or process critic for channel starvation and
  crisis resolution, not only action imitation;
- keep held-out randomized 96h worlds;
- keep social/environment ablations and require nonzero crisis score before
  counting dependency losses.

Only after that should the same principle move into richer settlement, territory,
building, and social infrastructure mechanics.

## Artifacts

- [script](../experiments/ssrm_3d_coupled_crisis_planner_distillation_controller.py)
- [schedule CSV](../artifacts/ssrm_3d_coupled_crisis_planner_distillation_schedule.csv)
- [base training CSV](../artifacts/ssrm_3d_coupled_crisis_planner_distillation_base_training.csv)
- [action training CSV](../artifacts/ssrm_3d_coupled_crisis_planner_distillation_action_training.csv)
- [router selection CSV](../artifacts/ssrm_3d_coupled_crisis_planner_distillation_router_selection.csv)
- [planner selection CSV](../artifacts/ssrm_3d_coupled_crisis_planner_distillation_planner_selection.csv)
- [policy selection CSV](../artifacts/ssrm_3d_coupled_crisis_planner_distillation_policy_selection.csv)
- [evaluation CSV](../artifacts/ssrm_3d_coupled_crisis_planner_distillation_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_coupled_crisis_planner_distillation_summary.csv)
- [ablation CSV](../artifacts/ssrm_3d_coupled_crisis_planner_distillation_ablations.csv)
- [verdict CSV](../artifacts/ssrm_3d_coupled_crisis_planner_distillation_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_coupled_crisis_planner_distillation_trace.json)
- [results JSON](../artifacts/ssrm_3d_coupled_crisis_planner_distillation_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_coupled_crisis_planner_distillation_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_coupled_crisis_planner_distillation_results.js)
