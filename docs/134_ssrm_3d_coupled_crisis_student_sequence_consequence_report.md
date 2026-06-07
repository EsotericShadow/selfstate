# SSRM-3D Coupled Crisis Student-Sequence Consequence Report

## Question

Report 133 showed that relabeling the MPC student's own crisis states is still
not enough. The recovered student improved generic total score, but after
rollout scoring was removed its held-out crisis score, resolved rate, and
coupled response all stayed at `0.000`.

This report tests the next narrower claim:

```text
Can student-created active-crisis sequence windows, weighted by downstream
consequence and MPC plan value, train a recurrent policy that preserves coupled
repair without calling the planner at evaluation?
```

The benchmark keeps the hard setting:

- `96h` randomized worlds;
- no major crisis before `12h`;
- randomized post-gate crisis timing, order, repetition, and initial pressure;
- learned base GRU;
- learned environmental/social action heads;
- recurrent consequence-recovery baseline;
- MPC teacher with `14` committed actions during data generation;
- student-created active-crisis windows;
- held-out evaluation with no MPC, rollout scoring, or supplied plan templates;
- targeted social/environment ablations.

This is bounded evidence. The MPC teacher and cloned simulator rollouts still
exist during training-data generation. The final evaluated student does not call
the MPC teacher, but it still receives supplied active-crisis action candidates.
The result is not open-ended civilization, subjective consciousness, mature
deep reinforcement learning, or real-world competence.

## Canonical Command

```bash
python3 experiments/ssrm_3d_coupled_crisis_student_sequence_consequence_controller.py --train-seeds 20260911,20260912,20260913 --tune-seeds 20261111,20261112 --eval-seeds 20261121,20261122,20261123 --hours 96 --step-hours 0.10 --population 14 --epochs 14 --hidden-size 48 --action-epochs 18 --action-hidden-size 48 --consequence-epochs 8 --consequence-hidden-size 48 --consequence-return-scale 1.15 --student-sequence-iterations 1 --student-sequence-epochs 8 --student-sequence-return-scale 1.35 --student-collection-bias 0.70 --counterfactual-collection-bias 0.80 --teacher-commit-actions 14 --policy-bias-candidates 0.0,0.40,0.80,1.20 --device auto --trace-seed 20261121
```

The run is expensive because it scores MPC windows from states the student
actually creates.

## What Changed

Report 134 moves from label-only recovery to consequence-weighted
student-created sequence windows:

```text
train consequence-recovery baseline
  -> let that consequence student act in training worlds
  -> at its visited active-crisis states, ask the MPC teacher for plan labels
     and plan values
  -> weight those windows by actual crisis outcome, plan value, plan margin,
     and environmental/social balance
  -> train a recurrent student on the aggregate
  -> evaluate without MPC, rollout scoring, or plan templates
```

The key distinction is that the added windows are both off-trajectory and
consequence-weighted. They are not just imitation labels.

## Training Result

The data-generation step worked. The student-created windows had positive
counterfactual value signal.

| Source | Sequences | Examples | Mean return | Positive rate | Env fraction | Social fraction | None fraction |
|---|---:|---:|---:|---:|---:|---:|---:|
| behavior sources | `114` | `143384` | `0.353` | `0.404` | `0.515` | `0.193` | `0.292` |
| student counterfactual windows | `19` | `25615` | `0.823` | `0.789` | `0.609` | `0.280` | `0.111` |
| aggregate | `133` | `168999` | `0.420` | `0.459` | `0.529` | `0.206` | `0.264` |

The final recurrent policy did not fit those mixed windows cleanly.

| Training pass | Examples | Train accuracy | Weighted accuracy | Final loss |
|---|---:|---:|---:|---:|
| behavior consequence baseline | `143384` | `0.994` | `0.994` | `0.319` |
| student sequence consequence | `168999` | `0.481` | `0.512` | `9.856` |

This matters. The added windows are useful-looking data, but the student does
not internalize them as a stable planner-free policy.

## Student Window Diagnostics

| Train seed | Sequences | Examples | Actual return | Counterfactual return | Plan value | Plan margin |
|---:|---:|---:|---:|---:|---:|---:|
| `20260911` | `7` | `9559` | `0.702` | `0.881` | `1.060` | `0.912` |
| `20260912` | `6` | `7752` | `0.099` | `0.671` | `0.958` | `0.540` |
| `20260913` | `6` | `8304` | `0.735` | `0.907` | `1.148` | `0.607` |

The failure is not lack of training examples or lack of plan-value signal. It
is transfer from high-value windows into closed-loop recurrent action.

## Policy Selection

Validation selected policy bias `0.8`.

| Policy bias | Tune total | Tune crisis | Tune resolved | Tune env | Tune social | Tune coupled | Tune damage | Selected |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `0.0` | `0.520` | `0.000` | `0.183` | `0.184` | `1.000` | `0.184` | `1.334` | no |
| `0.4` | `0.520` | `0.000` | `0.100` | `0.184` | `0.916` | `0.099` | `1.436` | no |
| `0.8` | `0.524` | `0.009` | `0.367` | `0.310` | `1.000` | `0.310` | `1.116` | yes |
| `1.2` | `0.501` | `0.000` | `0.100` | `0.184` | `0.916` | `0.099` | `1.544` | no |

The validation result looked less collapsed than the final held-out result.
That makes the boundary sharper: the sequence consequence signal can overfit
tune worlds without producing robust held-out repair.

## Held-Out Result

| Controller | Total score | Crisis score | Resolved rate | Env response | Social response | Coupled response |
|---|---:|---:|---:|---:|---:|---:|
| designed | `0.830` | `0.694` | `1.000` | `0.720` | `0.660` | `0.451` |
| MPC sequence teacher | `0.683` | `0.348` | `0.656` | `0.645` | `0.850` | `0.565` |
| min-channel planner GRU | `0.529` | `0.020` | `0.411` | `0.410` | `1.000` | `0.410` |
| fixed joint GRU | `0.524` | `0.021` | `0.411` | `0.410` | `1.000` | `0.410` |
| consequence-recovery GRU | `0.520` | `0.000` | `0.356` | `0.355` | `1.000` | `0.355` |
| student-sequence consequence GRU | `0.508` | `0.000` | `0.000` | `0.000` | `0.944` | `0.000` |
| return-selected GRU | `0.487` | `0.000` | `0.056` | `0.299` | `0.084` | `0.040` |

The verdict is:

```text
supports_student_sequence_consequence = false
supports_teacher_transfer = false
supports_social_environment_dependency = false
verdict = partial_or_failed
```

## Interpretation

This is another failed learned-transfer boundary.

The student-created windows look good as training data:

- `19` off-trajectory student-created sequences;
- `25615` additional active-crisis examples;
- mean counterfactual return `0.823`;
- positive return rate `0.789`;
- environmental and social actions both represented.

But the held-out recurrent policy does not preserve the coupled repair:

- crisis score: `0.000`;
- resolved rate: `0.000`;
- environment response: `0.000`;
- social response: `0.944`;
- coupled response: `0.000`;
- total score is `0.012` below consequence recovery.

The policy again falls into a social-heavy shortcut instead of owning the
environmental/social repair sequence.

## Ablation Boundary

The ablations cannot support a causal social/environment claim because the base
student already has no crisis or coupled response.

| Ablation | Total score | Total loss | Crisis score | Crisis loss | Coupled response | Coupled loss |
|---|---:|---:|---:|---:|---:|---:|
| none | `0.508` | - | `0.000` | - | `0.000` | - |
| social_culture | `0.453` | `0.055` | `0.000` | `0.000` | `0.000` | `0.000` |
| environment | `0.515` | `-0.007` | `0.000` | `0.000` | `0.000` | `0.000` |
| body | `0.506` | `0.002` | `0.000` | `0.000` | `0.000` | `0.000` |
| infrastructure | `0.443` | `0.065` | `0.000` | `0.000` | `0.054` | `-0.054` |
| tools | `0.220` | `0.288` | `0.000` | `0.000` | `0.055` | `-0.055` |
| previous_action | `0.520` | `-0.012` | `0.000` | `0.000` | `0.159` | `-0.159` |

This does not mean social/environment state is irrelevant. It means the learned
student failed before reaching the behavior where those ablations would be a
clean causal test.

## Boundary

Report 134 rules out the next shortcut:

```text
Student-created counterfactual sequence windows with consequence weighting are
not enough by themselves to distill MPC sequence repair into a planner-free
recurrent policy.
```

The next useful step should stop treating the MPC teacher's chosen action as
the primary target. The learner needs a sequence-level objective that optimizes
closed-loop crisis resolution, damage, and channel balance from its own rollouts
instead of trying to imitate high-value windows after the fact.

## Artifacts

- [script](../experiments/ssrm_3d_coupled_crisis_student_sequence_consequence_controller.py)
- [schedule CSV](../artifacts/ssrm_3d_coupled_crisis_student_sequence_consequence_schedule.csv)
- [base training CSV](../artifacts/ssrm_3d_coupled_crisis_student_sequence_consequence_base_training.csv)
- [action training CSV](../artifacts/ssrm_3d_coupled_crisis_student_sequence_consequence_action_training.csv)
- [router selection CSV](../artifacts/ssrm_3d_coupled_crisis_student_sequence_consequence_router_selection.csv)
- [planner selection CSV](../artifacts/ssrm_3d_coupled_crisis_student_sequence_consequence_planner_selection.csv)
- [consequence selection CSV](../artifacts/ssrm_3d_coupled_crisis_student_sequence_consequence_consequence_selection.csv)
- [student selection CSV](../artifacts/ssrm_3d_coupled_crisis_student_sequence_consequence_student_selection.csv)
- [source summary CSV](../artifacts/ssrm_3d_coupled_crisis_student_sequence_consequence_source_summary.csv)
- [student window summary CSV](../artifacts/ssrm_3d_coupled_crisis_student_sequence_consequence_student_window_summary.csv)
- [student plan use CSV](../artifacts/ssrm_3d_coupled_crisis_student_sequence_consequence_student_plan_use.csv)
- [consequence training CSV](../artifacts/ssrm_3d_coupled_crisis_student_sequence_consequence_consequence_training.csv)
- [evaluation CSV](../artifacts/ssrm_3d_coupled_crisis_student_sequence_consequence_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_coupled_crisis_student_sequence_consequence_summary.csv)
- [ablation CSV](../artifacts/ssrm_3d_coupled_crisis_student_sequence_consequence_ablations.csv)
- [verdict CSV](../artifacts/ssrm_3d_coupled_crisis_student_sequence_consequence_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_coupled_crisis_student_sequence_consequence_trace.json)
- [results JSON](../artifacts/ssrm_3d_coupled_crisis_student_sequence_consequence_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_coupled_crisis_student_sequence_consequence_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_coupled_crisis_student_sequence_consequence_results.js)
