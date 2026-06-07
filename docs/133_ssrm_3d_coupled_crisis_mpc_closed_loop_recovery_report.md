# SSRM-3D Coupled Crisis MPC Closed-Loop Recovery Report

## Question

Report 132 showed that ordinary recurrent imitation of the MPC sequence teacher
does not transfer. The student fits teacher traces, but once cloned rollout
scoring is removed, held-out crisis score, resolved rate, social response, and
coupled response collapse to `0.000`.

This report tests the next narrower claim:

```text
Can the failed student act in training worlds, have the MPC teacher relabel the
states the student actually visits, and then recover coupled crisis repair
without rollout scoring at evaluation?
```

The benchmark keeps the hard setting:

- `96h` randomized worlds;
- no major crisis before `12h`;
- randomized post-gate crisis timing, order, repetition, and initial pressure;
- learned base GRU;
- learned environmental/social action heads;
- recurrent consequence-recovery baseline;
- MPC teacher with `14` committed actions;
- one closed-loop recovery pass from student-visited active-crisis states;
- held-out evaluation without MPC rollout scoring;
- targeted social/environment ablations.

This is bounded closed-loop recovery evidence. The MPC teacher still uses
supplied repair-plan templates and cloned simulator rollout scoring during
training relabeling. The recovered student still receives supplied crisis
action candidates. The result is not open-ended civilization, subjective
consciousness, mature deep reinforcement learning, or real-world competence.

## Canonical Command

```bash
python3 experiments/ssrm_3d_coupled_crisis_mpc_closed_loop_recovery_controller.py --train-seeds 20260911,20260912,20260913 --tune-seeds 20261111,20261112 --eval-seeds 20261121,20261122,20261123 --hours 96 --step-hours 0.10 --population 14 --epochs 14 --hidden-size 48 --action-epochs 18 --action-hidden-size 48 --consequence-epochs 8 --consequence-hidden-size 48 --consequence-return-scale 1.15 --distill-epochs 10 --recovery-iterations 1 --recovery-epochs 6 --distill-hidden-size 64 --class-balance-power 0.35 --teacher-commit-actions 14 --policy-bias-candidates 0.0,0.40,0.80,1.20 --device auto --trace-seed 20261121
```

The run is expensive because MPC relabeling repeatedly scores cloned rollout
plan templates while collecting student-created states.

## What Changed

Report 133 is the MPC version of a DAgger-style recovery test:

```text
collect MPC teacher traces
  -> train initial recurrent student
  -> let that student act in training worlds
  -> label the student-visited crisis states with the MPC sequence teacher
  -> retrain on teacher + student-state labels
  -> evaluate the recovered student without rollout scoring
```

The key distinction is that recovery labels come from states the student caused,
not only from the teacher's own trajectories.

## Training Result

The MPC teacher and recovery pass produced enough data for a real failed test.

| Training source | Sequences | Examples | Train accuracy | Balanced accuracy | Env fraction | Social fraction | None fraction |
|---|---:|---:|---:|---:|---:|---:|---:|
| MPC teacher | `19` | `25076` | `0.589` | `0.486` | `0.579` | `0.360` | `0.061` |
| student-state MPC relabel | `19` | `20713` | - | - | - | - | - |
| aggregate recovery | `38` | `45789` | `0.471` | `0.327` | `0.556` | `0.411` | `0.033` |

The recovery pass made the aggregate dataset larger and more social-heavy, but
the final balanced accuracy fell below the `0.35` support threshold.

## Policy Selection

Validation selected policy bias `0.8`.

| Policy bias | Tune total | Tune crisis | Tune resolved | Tune env | Tune social | Tune coupled | Tune damage | Selected |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `0.0` | `0.520` | `0.000` | `0.000` | `0.012` | `1.000` | `0.012` | `1.691` | no |
| `0.4` | `0.520` | `0.000` | `0.000` | `0.001` | `1.000` | `0.001` | `1.672` | no |
| `0.8` | `0.520` | `0.000` | `0.000` | `0.084` | `0.919` | `0.003` | `1.634` | yes |
| `1.2` | `0.501` | `0.000` | `0.000` | `0.000` | `1.000` | `0.000` | `1.716` | no |

Validation again shows the central failure: none of the candidates recover
nonzero crisis score or resolved crises.

## Held-Out Result

| Controller | Total score | Crisis score | Resolved rate | Env response | Social response | Coupled response |
|---|---:|---:|---:|---:|---:|---:|
| designed | `0.830` | `0.694` | `1.000` | `0.720` | `0.660` | `0.451` |
| MPC sequence teacher | `0.683` | `0.348` | `0.656` | `0.645` | `0.850` | `0.565` |
| min-channel planner GRU | `0.529` | `0.020` | `0.411` | `0.410` | `1.000` | `0.410` |
| fixed joint GRU | `0.524` | `0.021` | `0.411` | `0.410` | `1.000` | `0.410` |
| consequence-recovery GRU | `0.520` | `0.000` | `0.356` | `0.355` | `1.000` | `0.355` |
| MPC closed-loop recovery GRU | `0.506` | `0.000` | `0.000` | `0.000` | `1.000` | `0.000` |
| return-selected GRU | `0.487` | `0.000` | `0.056` | `0.299` | `0.084` | `0.040` |
| initial MPC-distilled GRU | `0.468` | `0.000` | `0.000` | `0.300` | `0.001` | `0.000` |

The verdict is:

```text
supports_closed_loop_recovery = false
supports_teacher_transfer = false
supports_social_environment_dependency = false
verdict = partial_or_failed
```

## Interpretation

This is another failed learned-transfer boundary.

The recovery pass improves total score over the initial MPC-distilled student:

```text
0.506 - 0.468 = +0.039
```

It also improves over the return-selected baseline by `0.019` total score.
Those are not the target behaviors. The hard coupled-crisis metrics remain
collapsed:

- crisis score: `0.000`;
- resolved rate: `0.000`;
- coupled response: `0.000`;
- social response: `1.000`;
- environment response: `0.000`.

The recovered student has learned to preserve generic maturation while routing
active crises into a social-only pattern. It still does not keep environmental
repair and social repair active together, and it does not resolve the post-12h
crises.

## Ablation Boundary

The ablations cannot support a causal social/environment claim because the
base recovered policy already has no crisis or coupled response.

| Ablation | Total score | Total loss | Crisis score | Crisis loss | Coupled response | Coupled loss |
|---|---:|---:|---:|---:|---:|---:|
| none | `0.506` | - | `0.000` | - | `0.000` | - |
| social_culture | `0.453` | `0.053` | `0.000` | `0.000` | `0.000` | `0.000` |
| environment | `0.520` | `-0.014` | `0.000` | `0.000` | `0.000` | `0.000` |
| body | `0.501` | `0.006` | `0.000` | `0.000` | `0.046` | `-0.046` |
| infrastructure | `0.454` | `0.052` | `0.000` | `0.000` | `0.000` | `0.000` |
| tools | `0.295` | `0.211` | `0.000` | `0.000` | `0.000` | `0.000` |
| previous_action | `0.520` | `-0.014` | `0.000` | `0.000` | `0.026` | `-0.026` |

This does not show that social/environment state is unneeded. It shows that
the recovered policy failed before reaching the behavior where those ablations
would be meaningful.

## Boundary

Report 133 rules out a second shortcut:

```text
Closed-loop relabeling from student-visited states is not enough by itself to
distill MPC sequence repair into a planner-free recurrent policy.
```

The next useful step should move from labels to consequence optimization over
student-created multi-action windows:

- train on downstream crisis resolution, damage, and channel balance, not only
  teacher action labels;
- preserve both environmental and social repair as an explicit sequence-level
  objective;
- collect counterfactual windows from student-created states;
- keep the final evaluation planner-free and rollout-free.

## Artifacts

- [script](../experiments/ssrm_3d_coupled_crisis_mpc_closed_loop_recovery_controller.py)
- [schedule CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_closed_loop_recovery_schedule.csv)
- [base training CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_closed_loop_recovery_base_training.csv)
- [action training CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_closed_loop_recovery_action_training.csv)
- [router selection CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_closed_loop_recovery_router_selection.csv)
- [planner selection CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_closed_loop_recovery_planner_selection.csv)
- [consequence training CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_closed_loop_recovery_consequence_training.csv)
- [consequence selection CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_closed_loop_recovery_consequence_selection.csv)
- [teacher summary CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_closed_loop_recovery_teacher_summary.csv)
- [teacher plan use CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_closed_loop_recovery_teacher_plan_use.csv)
- [student-state plan use CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_closed_loop_recovery_student_state_plan_use.csv)
- [recovery training CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_closed_loop_recovery_recovery_training.csv)
- [policy selection CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_closed_loop_recovery_policy_selection.csv)
- [evaluation CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_closed_loop_recovery_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_closed_loop_recovery_summary.csv)
- [ablation CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_closed_loop_recovery_ablations.csv)
- [verdict CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_closed_loop_recovery_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_coupled_crisis_mpc_closed_loop_recovery_trace.json)
- [results JSON](../artifacts/ssrm_3d_coupled_crisis_mpc_closed_loop_recovery_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_coupled_crisis_mpc_closed_loop_recovery_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_coupled_crisis_mpc_closed_loop_recovery_results.js)
