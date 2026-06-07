# SSRM-3D Coupled Crisis Direct Counterfactual Policy Report

## Question

Report 128 showed that a cloned-rollout multi-action plan scorer is not enough
when it is used only as a runtime action-logit overlay. Validation selected
plan bias `0.0`, so the plan layer was rejected.

This report tests the next narrower claim:

```text
If cloned-rollout multi-action counterfactual windows are converted into
direct recurrent policy labels, can the active crisis policy preserve coupled
environmental/social repair after the engineered planner is removed?
```

The benchmark keeps the hard setting:

- `96h` worlds;
- no major crisis before `12h`;
- randomized post-gate crisis timing, order, repetition, and initial pressure;
- learned base GRU;
- learned environmental and social action heads;
- recurrent consequence-recovery policy;
- cloned rollout-window plan selection;
- direct recurrent crisis-policy training from selected plan actions;
- targeted social/environment ablations.

## What Changed

Report 128 kept the learned policy intact and added a separate plan-window
overlay. Report 129 moves the cloned-window target into the policy training set
itself.

During training, active-crisis states are visited by two source policies:

- `counterfactual_teacher`: follows the best cloned-rollout plan template for
  short windows;
- `consequence_policy`: visits states under the existing consequence-recovery
  policy, while cloned rollout windows still provide the direct labels.

The recurrent policy is then trained on those direct labels. At evaluation,
there is no engineered minimum-channel planner and no separate plan scorer. The
only tested direct-policy intervention is validation-selected bias around the
trained recurrent crisis policy.

This is still bounded evidence. The crisis action set and plan templates are
supplied, and cloned rollouts provide training labels. This is not mature deep
RL, open-ended civilization, subjective consciousness, or real-world
competence.

## Canonical Command

```bash
python3 experiments/ssrm_3d_coupled_crisis_direct_counterfactual_policy_controller.py --train-seeds 20260911,20260912,20260913 --tune-seeds 20261111,20261112 --eval-seeds 20261121,20261122,20261123 --hours 96 --step-hours 0.10 --population 14 --epochs 14 --hidden-size 48 --action-epochs 18 --action-hidden-size 48 --consequence-epochs 8 --consequence-hidden-size 48 --consequence-return-scale 1.15 --direct-epochs 8 --direct-hidden-size 48 --student-iterations 0 --counterfactual-windows-per-source 32 --plan-commit-actions 42 --policy-bias-candidates 0.0,0.40,0.80 --direct-bias-candidates 0.0,0.40,0.80 --device auto --trace-seed 20261121
```

An earlier heavier pass with `96` windows per source and one consequence-policy
student iteration was interrupted after roughly `36` minutes because it was
still in consequence-policy retraining. The report boundary above keeps the
same `96h` held-out crisis world but uses a repeatable bounded budget.

## Training Result

The behavior-source consequence policy trains cleanly:

| Metric | Value |
|---|---:|
| source sequences | `114` |
| student sequences | `0` |
| consequence train accuracy | `0.994` |
| consequence weighted accuracy | `0.994` |

The direct counterfactual-policy dataset contains both source types:

| Source | Sequences | Examples | Mean return | Positive return rate | Env action fraction | Social action fraction |
|---|---:|---:|---:|---:|---:|---:|
| consequence_policy | `2` | `2651` | `1.118` | `1.000` | `0.671` | `0.296` |
| counterfactual_teacher | `2` | `2262` | `1.155` | `0.500` | `0.590` | `0.393` |

The direct recurrent policy trains on `4913` examples from `64` cloned
counterfactual windows:

| Metric | Value |
|---|---:|
| direct train accuracy | `0.548` |
| direct weighted accuracy | `0.615` |
| mean plan value margin | `0.517` |
| direct epochs | `8` |

That is enough offline signal to be worth testing, but not enough by itself to
trust the learned policy online.

## Bias Selection

Validation selects consequence-policy bias `0.4`, then rejects the direct
counterfactual-policy intervention by selecting direct bias `0.0`.

| Direct bias | Tune total | Tune crisis | Tune resolved | Tune env response | Tune social response | Tune damage | Selected |
|---:|---:|---:|---:|---:|---:|---:|---|
| `0.0` | `0.485` | `0.000` | `0.000` | `0.367` | `0.000` | `2.389` | yes |
| `0.4` | `0.485` | `0.000` | `0.000` | `0.367` | `0.000` | `2.424` | no |
| `0.8` | `0.486` | `0.000` | `0.000` | `0.367` | `0.000` | `2.411` | no |

This is the central result: direct labels from cloned counterfactual windows
exist, but validation still turns the direct policy off.

## Held-Out Result

| Controller | Total score | Crisis score | Resolved rate | Env response | Social response | Coupled response |
|---|---:|---:|---:|---:|---:|---:|
| designed | `0.830` | `0.694` | `1.000` | `0.720` | `0.660` | `0.451` |
| min-channel planner GRU | `0.529` | `0.020` | `0.411` | `0.410` | `1.000` | `0.410` |
| fixed joint GRU | `0.524` | `0.021` | `0.411` | `0.410` | `1.000` | `0.410` |
| consequence-recovery GRU | `0.520` | `0.000` | `0.356` | `0.355` | `1.000` | `0.355` |
| return-selected GRU | `0.487` | `0.000` | `0.056` | `0.299` | `0.084` | `0.040` |
| direct counterfactual-policy GRU | `0.466` | `0.000` | `0.000` | `0.178` | `0.007` | `0.000` |
| base GRU | `0.290` | `0.000` | `0.000` | `0.299` | `0.000` | `0.000` |
| frame MLP | `0.287` | `0.000` | `0.000` | `0.299` | `0.000` | `0.000` |
| reactive | `0.090` | `0.000` | `0.000` | `0.280` | `0.000` | `0.000` |

The verdict is:

```text
mean_crisis_count = 5.667
selected_consequence_bias = 0.4
selected_direct_bias = 0.0
supports_direct_counterfactual_policy = false
supports_teacher_transfer = false
supports_social_environment_dependency = false
verdict = partial_or_failed
```

The direct policy does not improve held-out repair. It scores below the
consequence-recovery GRU by `0.054` total score and below return-selected GRU by
`0.021` total score. Crisis score, resolved rate, and coupled response all stay
at `0.000`.

## Ablation Boundary

| Ablation | Total score | Total loss | Crisis score | Coupled response | Coupled loss |
|---|---:|---:|---:|---:|---:|
| none | `0.466` | - | `0.000` | `0.000` | - |
| body | `0.471` | `-0.005` | `0.000` | `0.000` | `0.000` |
| infrastructure | `0.311` | `0.155` | `0.000` | `0.000` | `0.000` |
| tools | `0.196` | `0.270` | `0.000` | `0.000` | `0.000` |
| social_culture | `0.482` | `-0.016` | `0.000` | `0.000` | `0.000` |
| environment | `0.508` | `-0.042` | `0.000` | `0.000` | `0.000` |
| previous_action | `0.515` | `-0.050` | `0.000` | `0.000` | `0.000` |

Because the base direct-policy crisis behavior is already collapsed, the
social/environment dependency test cannot pass. There is no coupled response
left for those ablations to remove.

## Interpretation

This is a negative boundary.

The useful part is methodological: the report tests the exact next step after
Report 128 by putting cloned counterfactual window labels into the recurrent
policy training set instead of using a separate overlay. The dataset has some
offline signal: `0.615` weighted accuracy and positive source returns.

The failure is online transfer. Validation selects direct bias `0.0`; held-out
crisis score, resolved rate, and coupled response remain `0.000`; and the
direct policy underperforms the consequence-recovery baseline. Supervised
labels from cloned windows still do not make the learned policy preserve the
coupled environmental/social repair loop after planner removal.

The next credible step is not another direct label pass. It needs active
consequence optimization:

- optimize the policy against downstream crisis resolution and channel balance,
  not only plan-derived action labels;
- train on states created by the policy's own nonzero direct interventions;
- make multi-action choices update recurrent hidden state and future credit,
  not just the current target action;
- keep the same randomized `96h` worlds, post-12h crisis gate, and
  social/environment ablations;
- add progress logging or a cheaper staged mode before any heavier manifest
  budget.

## Artifacts

- [script](../experiments/ssrm_3d_coupled_crisis_direct_counterfactual_policy_controller.py)
- [schedule CSV](../artifacts/ssrm_3d_coupled_crisis_direct_counterfactual_policy_schedule.csv)
- [base training CSV](../artifacts/ssrm_3d_coupled_crisis_direct_counterfactual_policy_base_training.csv)
- [action training CSV](../artifacts/ssrm_3d_coupled_crisis_direct_counterfactual_policy_action_training.csv)
- [router selection CSV](../artifacts/ssrm_3d_coupled_crisis_direct_counterfactual_policy_router_selection.csv)
- [planner selection CSV](../artifacts/ssrm_3d_coupled_crisis_direct_counterfactual_policy_planner_selection.csv)
- [source summary CSV](../artifacts/ssrm_3d_coupled_crisis_direct_counterfactual_policy_source_summary.csv)
- [consequence training CSV](../artifacts/ssrm_3d_coupled_crisis_direct_counterfactual_policy_consequence_training.csv)
- [consequence selection CSV](../artifacts/ssrm_3d_coupled_crisis_direct_counterfactual_policy_consequence_selection.csv)
- [counterfactual probes CSV](../artifacts/ssrm_3d_coupled_crisis_direct_counterfactual_policy_counterfactual_probes.csv)
- [direct source summary CSV](../artifacts/ssrm_3d_coupled_crisis_direct_counterfactual_policy_direct_source_summary.csv)
- [direct training CSV](../artifacts/ssrm_3d_coupled_crisis_direct_counterfactual_policy_direct_training.csv)
- [direct selection CSV](../artifacts/ssrm_3d_coupled_crisis_direct_counterfactual_policy_direct_selection.csv)
- [evaluation CSV](../artifacts/ssrm_3d_coupled_crisis_direct_counterfactual_policy_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_coupled_crisis_direct_counterfactual_policy_summary.csv)
- [ablation CSV](../artifacts/ssrm_3d_coupled_crisis_direct_counterfactual_policy_ablations.csv)
- [verdict CSV](../artifacts/ssrm_3d_coupled_crisis_direct_counterfactual_policy_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_coupled_crisis_direct_counterfactual_policy_trace.json)
- [results JSON](../artifacts/ssrm_3d_coupled_crisis_direct_counterfactual_policy_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_coupled_crisis_direct_counterfactual_policy_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_coupled_crisis_direct_counterfactual_policy_results.js)
