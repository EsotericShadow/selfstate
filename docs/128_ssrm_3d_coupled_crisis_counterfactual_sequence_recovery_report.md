# SSRM-3D Coupled Crisis Counterfactual Sequence Recovery Report

## Question

Report 127 showed that scalar completed-window action reranking has offline
signal but worsens held-out coupled-crisis repair.

This report tests the next narrower claim:

```text
If a learned plan-value model is trained from cloned simulator rollouts over
short multi-action windows, can it bias a consequence-trained recurrent crisis
policy and preserve coupled environmental/social crisis repair after the
engineered planner is removed?
```

The benchmark keeps the hard setting:

- `96h` worlds;
- no major crisis before `12h`;
- randomized post-gate crisis timing, order, repetition, and initial pressure;
- learned base GRU;
- learned environmental and social action heads;
- recurrent consequence-recovery policy from Report 126;
- cloned simulator rollouts over short plan windows;
- targeted social/environment ablations.

## What Changed

Report 127 scored individual candidate actions. Report 128 scores short plan
windows.

The plan-value model receives:

- local world/body/social observation features;
- active-crisis progress context;
- recent environmental/social response context;
- one supplied short-window plan template;
- cloned simulator rollout value for that plan window.

At evaluation, the engineered minimum-channel planner is removed. The
consequence-recovery GRU still produces active-crisis action logits. The
counterfactual plan model chooses a short plan template and can bias the policy
for several actions at a time.

This is still bounded evidence. The crisis action set and plan templates are
supplied. The plan-value target comes from cloned simulator rollouts, but the
agent is not discovering unsupplied actions, running mature deep RL, or proving
subjective consciousness.

## Canonical Command

```bash
python3 experiments/ssrm_3d_coupled_crisis_counterfactual_sequence_recovery_controller.py --train-seeds 20260911,20260912,20260913 --tune-seeds 20261111,20261112 --eval-seeds 20261121,20261122,20261123 --hours 96 --step-hours 0.10 --population 14 --epochs 24 --hidden-size 64 --action-epochs 32 --action-hidden-size 64 --consequence-epochs 14 --consequence-hidden-size 64 --consequence-return-scale 1.15 --plan-epochs 12 --plan-hidden-size 64 --max-plan-examples 1024 --student-iterations 1 --student-collection-bias 0.70 --policy-bias-candidates 0.0,0.20,0.40,0.70,1.00 --plan-bias-candidates 0.0,0.25,0.50,0.80,1.10,1.50 --plan-commit-actions 42 --device auto --trace-seed 20261121
```

The cloned-rollout plan budget is intentionally bounded at `1024` examples. A
larger `4096` example pass was still CPU-bound after about `42` minutes, and a
`60000` example pass was not practical for a repeatable report boundary.

## Training Result

The consequence-recovery policy uses the same aggregate source as Report 126:
`133` completed crisis sequences and `166169` active-crisis examples.

| Metric | Value |
|---|---:|
| consequence train accuracy | `0.986` |
| consequence weighted accuracy | `0.982` |
| aggregate examples | `166169` |
| source sequences | `114` |
| student sequences | `19` |

The cloned-rollout plan-value model trains on a bounded counterfactual window
set:

| Metric | Value |
|---|---:|
| plan examples | `1024` |
| positive plan examples | `956` |
| final plan loss | `0.032` |
| pairwise accuracy | `0.567` |
| plan epochs | `12` |

The plan-value model has weak offline ranking signal, but not enough to earn
closed-loop trust by itself.

## Bias Selection

Validation selected consequence-policy bias `1.0`.

| Policy bias | Tune total | Tune crisis | Tune resolved | Tune coupled | Damage | Selected |
|---:|---:|---:|---:|---:|---:|---|
| `0.00` | `0.520` | `0.000` | `0.267` | `0.200` | `1.404` | no |
| `0.20` | `0.542` | `0.045` | `0.350` | `0.273` | `1.355` | no |
| `0.40` | `0.561` | `0.094` | `0.333` | `0.251` | `1.537` | no |
| `0.70` | `0.530` | `0.041` | `0.433` | `0.212` | `1.481` | no |
| `1.00` | `0.582` | `0.140` | `0.333` | `0.334` | `1.591` | yes |

Then validation tested the counterfactual plan-window bias and selected
`0.0`.

| Plan bias | Tune total | Tune crisis | Tune resolved | Tune coupled | Damage | Selected |
|---:|---:|---:|---:|---:|---:|---|
| `0.00` | `0.570` | `0.142` | `0.433` | `0.435` | `1.534` | yes |
| `0.25` | `0.586` | `0.138` | `0.433` | `0.349` | `1.400` | no |
| `0.50` | `0.514` | `0.000` | `0.167` | `0.173` | `1.806` | no |
| `0.80` | `0.507` | `0.000` | `0.167` | `0.167` | `1.815` | no |
| `1.10` | `0.486` | `0.000` | `0.167` | `0.175` | `1.781` | no |
| `1.50` | `0.511` | `0.000` | `0.167` | `0.167` | `1.754` | no |

This is the central result: the multi-action counterfactual plan layer is
available, but validation rejects it.

## Held-Out Result

| Controller | Total score | Crisis score | Resolved rate | Env response | Social response | Coupled response |
|---|---:|---:|---:|---:|---:|---:|
| fixed joint GRU | `0.843` | `0.675` | `0.933` | `0.863` | `1.000` | `0.863` |
| min-channel planner GRU | `0.797` | `0.590` | `0.878` | `0.828` | `1.000` | `0.828` |
| consequence-recovery GRU | `0.532` | `0.028` | `0.356` | `0.355` | `1.000` | `0.355` |
| counterfactual sequence recovery GRU | `0.530` | `0.036` | `0.478` | `0.355` | `1.000` | `0.355` |
| return-selected GRU | `0.516` | `0.000` | `0.000` | `0.299` | `0.346` | `0.000` |
| base GRU | `0.293` | `0.000` | `0.000` | `0.299` | `0.000` | `0.000` |
| frame MLP | `0.287` | `0.000` | `0.000` | `0.299` | `0.000` | `0.000` |
| reactive | `0.090` | `0.000` | `0.000` | `0.280` | `0.000` | `0.000` |

The verdict is:

```text
mean_crisis_count = 5.667
selected_policy_bias = 1.0
selected_plan_bias = 0.0
supports_counterfactual_sequence_recovery = false
supports_teacher_transfer = false
supports_social_environment_dependency = true
verdict = partial_or_failed
```

The held-out controller has a slightly higher crisis score than Report 126
(`0.036` vs `0.028`) and a higher resolved rate (`0.478` vs `0.356`). But total
score falls from `0.532` to `0.530`, coupled response is effectively unchanged,
and the selected plan bias is `0.0`. The improvement comes from policy-bias
selection, not from the counterfactual plan-window layer.

## Ablation Boundary

| Ablation | Crisis score | Crisis loss | Coupled response | Coupled loss |
|---|---:|---:|---:|---:|
| none | `0.036` | - | `0.355` | - |
| social_culture | `0.000` | `0.036` | `0.000` | `0.355` |
| environment | `0.000` | `0.036` | `0.000` | `0.355` |
| previous_action | `0.000` | `0.036` | `0.299` | `0.056` |
| body | `0.035` | `0.001` | `0.328` | `0.027` |
| tools | `0.003` | `0.033` | `0.299` | `0.056` |
| infrastructure | `0.000` | `0.036` | `0.299` | `0.056` |

The social/environment dependency is real: either channel ablation collapses
coupled response. But the base crisis score is still far below the teacher
planner, so this remains a boundary, not a solved learned controller.

## Interpretation

This is a partial negative result.

The useful part: the bounded recurrent policy now recovers nonzero crisis score
after planner removal and preserves a clear social/environment dependency. It
also beats return-selected control by `0.014` total score and `0.036` crisis
score.

The failure: the counterfactual multi-action window layer does not yet help.
The plan-value model has only weak offline signal (`0.567` pairwise accuracy),
and validation selects plan bias `0.0`. Nonzero plan bias hurts validation by
raising damage, reducing coupled response, or collapsing crisis score.

The next credible step is not a larger cloned-window scorer by itself. The
policy needs active consequence optimization over the same windows:

- train the crisis policy directly from multi-step counterfactual outcomes;
- make plan choices update the recurrent hidden state, not just add action
  logits;
- score channel starvation over the next window, not only the current action;
- train on off-trajectory states created by the plan-biased policy;
- keep the same randomized `96h` worlds and social/environment ablations.

## Artifacts

- [script](../experiments/ssrm_3d_coupled_crisis_counterfactual_sequence_recovery_controller.py)
- [schedule CSV](../artifacts/ssrm_3d_coupled_crisis_counterfactual_sequence_recovery_schedule.csv)
- [base training CSV](../artifacts/ssrm_3d_coupled_crisis_counterfactual_sequence_recovery_base_training.csv)
- [action training CSV](../artifacts/ssrm_3d_coupled_crisis_counterfactual_sequence_recovery_action_training.csv)
- [router selection CSV](../artifacts/ssrm_3d_coupled_crisis_counterfactual_sequence_recovery_router_selection.csv)
- [planner selection CSV](../artifacts/ssrm_3d_coupled_crisis_counterfactual_sequence_recovery_planner_selection.csv)
- [source summary CSV](../artifacts/ssrm_3d_coupled_crisis_counterfactual_sequence_recovery_source_summary.csv)
- [consequence training CSV](../artifacts/ssrm_3d_coupled_crisis_counterfactual_sequence_recovery_consequence_training.csv)
- [plan training CSV](../artifacts/ssrm_3d_coupled_crisis_counterfactual_sequence_recovery_plan_training.csv)
- [policy selection CSV](../artifacts/ssrm_3d_coupled_crisis_counterfactual_sequence_recovery_policy_selection.csv)
- [plan selection CSV](../artifacts/ssrm_3d_coupled_crisis_counterfactual_sequence_recovery_plan_selection.csv)
- [evaluation CSV](../artifacts/ssrm_3d_coupled_crisis_counterfactual_sequence_recovery_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_coupled_crisis_counterfactual_sequence_recovery_summary.csv)
- [ablation CSV](../artifacts/ssrm_3d_coupled_crisis_counterfactual_sequence_recovery_ablations.csv)
- [verdict CSV](../artifacts/ssrm_3d_coupled_crisis_counterfactual_sequence_recovery_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_coupled_crisis_counterfactual_sequence_recovery_trace.json)
- [results JSON](../artifacts/ssrm_3d_coupled_crisis_counterfactual_sequence_recovery_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_coupled_crisis_counterfactual_sequence_recovery_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_coupled_crisis_counterfactual_sequence_recovery_results.js)
