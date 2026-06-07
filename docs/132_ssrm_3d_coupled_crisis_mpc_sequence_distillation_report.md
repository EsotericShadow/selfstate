# SSRM-3D Coupled Crisis MPC Sequence Distillation Report

## Question

Report 131 showed that model-predictive sequence commitment can restore much
of the coupled environmental/social repair shape, but only by using supplied
repair-plan templates and cloned simulator rollout scoring at decision time.

This report tests the next narrower claim:

```text
Can the MPC sequence teacher be distilled into a recurrent crisis policy that
acts without cloned rollout scoring at evaluation?
```

The benchmark keeps the hard setting:

- `96h` worlds;
- no major crisis before `12h`;
- randomized post-gate crisis timing, order, repetition, and initial pressure;
- learned base GRU;
- learned environmental and social action heads;
- recurrent consequence-recovery baseline;
- MPC teacher traces generated with `14` committed actions;
- recurrent student policy trained from MPC crisis actions;
- student evaluation without MPC rollout scoring;
- targeted social/environment ablations.

This is bounded distillation evidence. The teacher still uses supplied plan
templates and cloned simulator lookahead during training-data collection. The
student still receives supplied crisis action candidates. The result is not
open-ended civilization, subjective consciousness, mature deep reinforcement
learning, or proof of real-world competence.

## Canonical Command

```bash
python3 experiments/ssrm_3d_coupled_crisis_mpc_sequence_distillation_controller.py --train-seeds 20260911,20260912,20260913 --tune-seeds 20261111,20261112 --eval-seeds 20261121,20261122,20261123 --hours 96 --step-hours 0.10 --population 14 --epochs 14 --hidden-size 48 --action-epochs 18 --action-hidden-size 48 --consequence-epochs 8 --consequence-hidden-size 48 --consequence-return-scale 1.15 --student-iterations 0 --distill-epochs 10 --distill-hidden-size 64 --class-balance-power 0.35 --teacher-commit-actions 14 --policy-bias-candidates 0.0,0.40,0.80,1.20 --device auto --trace-seed 20261121
```

## What Changed

Report 132 uses Report 131 as a teacher, not as an evaluation-time controller.

The pipeline is:

```text
run MPC teacher in training worlds
  -> record active-crisis recurrent-policy features and teacher actions
  -> train a recurrent crisis-memory policy with class-balanced imitation
  -> remove MPC rollout scoring
  -> evaluate the student closed-loop on held-out worlds
```

The student can carry recurrent state through a crisis window, but it cannot
clone the simulator or score future repair plans while acting.

## Teacher And Training Result

The MPC teacher produced balanced enough traces to make distillation a real
test rather than an empty-data failure.

| Metric | Value |
|---|---:|
| teacher sequences | `19` |
| teacher examples | `24633` |
| teacher env action fraction | `0.581` |
| teacher social action fraction | `0.357` |
| teacher none fraction | `0.062` |
| mean sequence length | `1296.474` |
| teacher commit actions | `14` |

The recurrent student fit part of the teacher behavior:

| Metric | Value |
|---|---:|
| distill epochs | `10` |
| train accuracy | `0.596` |
| balanced train accuracy | `0.499` |
| class balance power | `0.35` |
| parameters | `29640` |
| device | `mps` |

This is enough to reject the trivial explanation that the student simply had no
teacher data. The held-out question is whether imitation transfers into
closed-loop repair.

## Policy Selection

Validation selected policy bias `0.8`.

| Policy bias | Tune total | Tune crisis | Tune resolved | Tune env | Tune social | Tune coupled | Tune damage | Selected |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `0.0` | `0.459` | `0.000` | `0.000` | `0.148` | `0.000` | `0.000` | `2.678` | no |
| `0.4` | `0.473` | `0.000` | `0.000` | `0.124` | `0.000` | `0.000` | `2.718` | no |
| `0.8` | `0.459` | `0.000` | `0.000` | `0.167` | `0.000` | `0.000` | `2.624` | yes |
| `1.2` | `0.444` | `0.000` | `0.000` | `0.103` | `0.000` | `0.000` | `2.845` | no |

This is already a warning sign: none of the validation candidates recovered
nonzero crisis score or coupled response.

## Held-Out Result

| Controller | Total score | Crisis score | Resolved rate | Env response | Social response | Coupled response |
|---|---:|---:|---:|---:|---:|---:|
| designed | `0.830` | `0.694` | `1.000` | `0.720` | `0.660` | `0.451` |
| MPC sequence teacher | `0.683` | `0.348` | `0.656` | `0.645` | `0.850` | `0.565` |
| min-channel planner GRU | `0.529` | `0.020` | `0.411` | `0.410` | `1.000` | `0.410` |
| fixed joint GRU | `0.524` | `0.021` | `0.411` | `0.410` | `1.000` | `0.410` |
| consequence-recovery GRU | `0.520` | `0.000` | `0.356` | `0.355` | `1.000` | `0.355` |
| return-selected GRU | `0.487` | `0.000` | `0.056` | `0.299` | `0.084` | `0.040` |
| MPC-distilled GRU | `0.457` | `0.000` | `0.000` | `0.303` | `0.000` | `0.000` |
| base GRU | `0.290` | `0.000` | `0.000` | `0.299` | `0.000` | `0.000` |
| frame MLP | `0.287` | `0.000` | `0.000` | `0.299` | `0.000` | `0.000` |
| reactive | `0.090` | `0.000` | `0.000` | `0.280` | `0.000` | `0.000` |

The verdict is:

```text
supports_mpc_distillation = false
supports_teacher_transfer = false
supports_social_environment_dependency = false
verdict = partial_or_failed
```

## Interpretation

This is a clean failed distillation boundary.

The MPC teacher keeps both channels active:

- crisis score `0.348`;
- resolved rate `0.656`;
- coupled response `0.565`.

The recurrent student does not transfer that behavior:

- crisis score `0.000`;
- resolved rate `0.000`;
- social response `0.000`;
- coupled response `0.000`;
- total score `0.457`, below both consequence recovery `0.520` and
  return-selected `0.487`.

The important conclusion is:

```text
MPC sequence behavior is not yet captured by ordinary recurrent imitation,
even with nontrivial teacher accuracy and class-balanced training.
```

The likely failure is off-trajectory closed-loop control. The student can fit
some teacher actions from teacher states, but once it acts on its own it drops
the social channel, fails to keep both repair processes alive, and never
creates the sequence conditions that made the teacher work.

## Ablation Boundary

The ablations do not support a causal social/environment claim because the base
student already has zero crisis and coupled response.

| Ablation | Total score | Total loss | Crisis score | Crisis loss | Coupled response | Coupled loss |
|---|---:|---:|---:|---:|---:|---:|
| none | `0.457` | - | `0.000` | - | `0.000` | - |
| social_culture | `0.454` | `0.003` | `0.000` | `0.000` | `0.000` | `0.000` |
| environment | `0.515` | `-0.057` | `0.000` | `0.000` | `0.000` | `0.000` |
| body | `0.477` | `-0.019` | `0.000` | `0.000` | `0.002` | `-0.002` |
| infrastructure | `0.290` | `0.168` | `0.000` | `0.000` | `0.000` | `0.000` |
| tools | `0.295` | `0.163` | `0.000` | `0.000` | `0.000` | `0.000` |
| previous_action | `0.509` | `-0.052` | `0.000` | `0.000` | `0.003` | `-0.003` |

The student does not have enough coupled behavior for ablations to damage.
This is not evidence that social/environment channels are unnecessary; it is
evidence that the student failed before reaching that causal dependency test.

## Boundary

Report 132 rules out another tempting shortcut:

```text
It is not enough to imitate the MPC sequence teacher with a recurrent
crisis-memory policy.
```

The next useful step should not be another larger imitation run by itself. It
needs training that directly penalizes the student for its own off-trajectory
sequence failures:

- closed-loop student-state collection under the MPC teacher;
- counterfactual sequence relabeling from student-visited states;
- sequence-level value/process losses for maintaining both repair channels;
- explicit penalties for social-channel dropout and environmental-only repair;
- evaluation without cloned rollout access.

## Artifacts

- [script](../experiments/ssrm_3d_coupled_crisis_mpc_sequence_distillation_controller.py)
- [schedule CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_sequence_distillation_schedule.csv)
- [base training CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_sequence_distillation_base_training.csv)
- [action training CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_sequence_distillation_action_training.csv)
- [router selection CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_sequence_distillation_router_selection.csv)
- [planner selection CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_sequence_distillation_planner_selection.csv)
- [consequence training CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_sequence_distillation_consequence_training.csv)
- [consequence selection CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_sequence_distillation_consequence_selection.csv)
- [teacher summary CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_sequence_distillation_teacher_summary.csv)
- [teacher plan use CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_sequence_distillation_teacher_plan_use.csv)
- [distillation training CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_sequence_distillation_distillation_training.csv)
- [policy selection CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_sequence_distillation_policy_selection.csv)
- [evaluation CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_sequence_distillation_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_sequence_distillation_summary.csv)
- [ablation CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_sequence_distillation_ablations.csv)
- [verdict CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_sequence_distillation_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_coupled_crisis_mpc_sequence_distillation_trace.json)
- [results JSON](../artifacts/ssrm_3d_coupled_crisis_mpc_sequence_distillation_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_coupled_crisis_mpc_sequence_distillation_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_coupled_crisis_mpc_sequence_distillation_results.js)
