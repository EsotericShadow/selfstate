# SSRM-3D Coupled Crisis Closed-Loop Recovery Report

## Question

Report 124 showed that offline planner imitation is not enough. A recurrent
active-crisis policy could fit the successful minimum-channel planner's labels
with high accuracy, but it failed once the planner was removed and the policy
had to act in its own held-out rollouts.

This report tests the next narrower claim:

```text
If the learner acts in training worlds, and the successful planner relabels the
off-trajectory states the learner actually visits, does that closed-loop
recovery training preserve coupled crisis repair after the planner is removed?
```

The benchmark keeps the hard setting from Reports 123 and 124:

- `96h` worlds;
- no major crisis before `12h`;
- randomized post-gate crisis timing, order, repetition, and initial pressure;
- learned base GRU;
- learned environmental and social crisis action heads;
- return-selected GRU, fixed-joint, and minimum-channel planner baselines;
- targeted social/environment ablations.

## What Changed

The closed-loop recovery controller starts from the Report 124 distillation
setup, then adds a DAgger-style correction loop:

1. collect teacher trajectories from the selected Report 123 minimum-channel
   planner;
2. train an initial recurrent recovery policy from those trajectories;
3. let the student act in training worlds;
4. relabel the active-crisis states the student actually visits using the
   successful planner;
5. aggregate the original teacher data and student-visited recovery data;
6. retrain the recurrent policy;
7. remove the planner at held-out evaluation.

This is a closed-loop recovery test, not open-ended role discovery, not
unsupplied action discovery, not subjective consciousness, and not mature deep
reinforcement learning.

## Canonical Command

```bash
python3 experiments/ssrm_3d_coupled_crisis_closed_loop_recovery_controller.py --train-seeds 20260911,20260912,20260913 --tune-seeds 20261111,20261112 --eval-seeds 20261121,20261122,20261123 --hours 96 --step-hours 0.10 --population 14 --epochs 24 --hidden-size 64 --action-epochs 32 --action-hidden-size 64 --distill-epochs 12 --distill-hidden-size 64 --recovery-iterations 2 --recovery-epochs 6 --recovery-hidden-size 64 --recovery-collection-bias 0.70 --policy-bias-candidates 0.0,0.20,0.40,0.70,1.00 --device auto --trace-seed 20261121
```

## Recovery Training Result

The first teacher-imitation pass still fits planner labels tightly. The
student-recovery passes add off-trajectory states, but accuracy falls as the
aggregate data starts covering the student's own bad crisis states.

| Iteration | Source | Collected sequences | Aggregate examples | Final loss | Train accuracy | Env fraction | Social fraction | None fraction |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| `0` | planner_teacher | `19` | `24568` | `0.033` | `0.986` | `0.186` | `0.237` | `0.577` |
| `1` | student_recovery | `19` | `50846` | `0.445` | `0.477` | `0.231` | `0.477` | `0.292` |
| `2` | student_recovery | `19` | `74756` | `0.739` | `0.381` | `0.467` | `0.334` | `0.199` |

The aggregate set grows to `74756` examples across `57` crisis sequences. That
means this is not just the Report 124 offline trace again. The learner is being
shown states created by its own policy.

## Policy Bias Selection

Validation selected policy bias `0.7`, but every candidate still had `0.000`
tune crisis score and `0.000` tune resolved rate.

| Bias | Tune total | Tune crisis | Tune resolved | Tune env | Tune social | Tune coupled | Selected |
|---:|---:|---:|---:|---:|---:|---:|---|
| `0.0` | `0.500` | `0.000` | `0.000` | `0.351` | `0.000` | `0.000` | no |
| `0.2` | `0.520` | `0.000` | `0.000` | `0.351` | `0.000` | `0.000` | no |
| `0.4` | `0.508` | `0.000` | `0.000` | `0.268` | `0.000` | `0.000` | no |
| `0.7` | `0.511` | `0.000` | `0.000` | `0.268` | `0.000` | `0.000` | yes |
| `1.0` | `0.510` | `0.000` | `0.000` | `0.342` | `0.000` | `0.000` | no |

This already signals the final boundary: closed-loop relabeling did not find a
policy setting with working crisis repair.

## Held-Out Result

The closed-loop recovery policy does not pass the planner-removal gate.

| Controller | Total score | Crisis score | Resolved rate | Env response | Social response | Coupled response |
|---|---:|---:|---:|---:|---:|---:|
| fixed joint GRU | `0.843` | `0.675` | `0.933` | `0.863` | `1.000` | `0.863` |
| min-channel planner GRU | `0.797` | `0.590` | `0.878` | `0.828` | `1.000` | `0.828` |
| designed | `0.760` | `0.522` | `1.000` | `0.077` | `0.923` | `0.000` |
| planner-recovery GRU | `0.511` | `0.000` | `0.000` | `0.178` | `0.000` | `0.000` |
| return-selected GRU | `0.496` | `0.000` | `0.000` | `0.299` | `0.219` | `0.000` |
| base GRU | `0.344` | `0.000` | `0.000` | `0.299` | `0.111` | `0.000` |
| frame MLP | `0.283` | `0.000` | `0.000` | `0.299` | `0.000` | `0.000` |
| reactive | `0.086` | `0.000` | `0.000` | `0.176` | `0.000` | `0.000` |

The verdict is:

```text
mean_crisis_count = 5.667
supports_closed_loop_recovery = false
supports_teacher_transfer = false
supports_social_environment_dependency = false
verdict = partial_or_failed
```

The recovery controller improves total score over return-selected GRU by only
`0.015`, but it loses Report 124's partial resolved/coupled response and still
gets `0.000` crisis score. The teacher planner remains far ahead with crisis
score `0.590` and coupled response `0.828`.

## Ablation Boundary

The ablations cannot support the strong dependency claim because the unablated
recovery policy already has `0.000` crisis score and `0.000` coupled response.

| Ablation | Total score | Total loss | Crisis loss | Coupled loss |
|---|---:|---:|---:|---:|
| none | `0.511` | - | - | - |
| social_culture | `0.256` | `0.254` | `0.000` | `0.000` |
| environment | `0.484` | `0.026` | `0.000` | `0.000` |
| previous_action | `0.489` | `0.021` | `0.000` | `0.000` |
| body | `0.498` | `0.013` | `0.000` | `0.000` |
| tools | `0.453` | `0.057` | `0.000` | `0.000` |
| infrastructure | `0.401` | `0.110` | `0.000` | `0.000` |

The social/culture ablation has a large total-score effect, but because the
main crisis behavior is already collapsed, that is not evidence that the
learned recovery policy solved coupled crisis repair.

## Interpretation

This is another useful negative boundary.

Closed-loop student-state relabeling was the right next test after Report 124,
but it does not solve the core problem. The learner can preserve generic
maturation and survival behavior, yet it still fails when post-gate crises need
environmental and social repair at the same time.

The likely lesson is that planner labels alone are still too weak, even when
they are collected on student-visited states. The policy receives corrected
actions, but it is not directly optimized for later crisis resolution, channel
balance, damage reduction, or recovery from the compounding effects of its own
earlier choices.

The result should stay visible. It says that the successful Report 123 dynamic
planner has not yet been distilled into an autonomous learned crisis policy.

## Next Step

Do not claim open-ended learned civilization.

The next credible step is to stop treating the planner as only a labeler and
make crisis consequence the training objective:

- train a sequence-level value/process model over whole crisis windows;
- score action candidates by predicted future crisis resolution, damage, and
  channel balance;
- use planner trajectories as initialization, not as the only supervision;
- include student-generated counterfactual rollouts, not just relabeled visited
  states;
- keep held-out randomized 96h worlds;
- keep nonzero crisis score as a prerequisite before counting ablation losses.

Only after that learned policy can preserve coupled repair should richer
settlement, territory, building, and social infrastructure mechanics be treated
as canonical learned-control evidence rather than visualization or designed
world pressure.

## Artifacts

- [script](../experiments/ssrm_3d_coupled_crisis_closed_loop_recovery_controller.py)
- [schedule CSV](../artifacts/ssrm_3d_coupled_crisis_closed_loop_recovery_schedule.csv)
- [base training CSV](../artifacts/ssrm_3d_coupled_crisis_closed_loop_recovery_base_training.csv)
- [action training CSV](../artifacts/ssrm_3d_coupled_crisis_closed_loop_recovery_action_training.csv)
- [router selection CSV](../artifacts/ssrm_3d_coupled_crisis_closed_loop_recovery_router_selection.csv)
- [planner selection CSV](../artifacts/ssrm_3d_coupled_crisis_closed_loop_recovery_planner_selection.csv)
- [recovery training CSV](../artifacts/ssrm_3d_coupled_crisis_closed_loop_recovery_recovery_training.csv)
- [policy selection CSV](../artifacts/ssrm_3d_coupled_crisis_closed_loop_recovery_policy_selection.csv)
- [evaluation CSV](../artifacts/ssrm_3d_coupled_crisis_closed_loop_recovery_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_coupled_crisis_closed_loop_recovery_summary.csv)
- [ablation CSV](../artifacts/ssrm_3d_coupled_crisis_closed_loop_recovery_ablations.csv)
- [verdict CSV](../artifacts/ssrm_3d_coupled_crisis_closed_loop_recovery_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_coupled_crisis_closed_loop_recovery_trace.json)
- [results JSON](../artifacts/ssrm_3d_coupled_crisis_closed_loop_recovery_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_coupled_crisis_closed_loop_recovery_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_coupled_crisis_closed_loop_recovery_results.js)
