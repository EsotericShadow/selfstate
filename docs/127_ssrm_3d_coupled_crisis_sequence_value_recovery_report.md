# SSRM-3D Coupled Crisis Sequence-Value Recovery Report

## Question

Report 126 showed that completed-crisis consequence weighting is closer than
planner-label imitation, but still far below the structured minimum-channel
planner.

This report tests the next narrower claim:

```text
If a learned process-value critic is trained from completed crisis-window
outcomes, can it rerank consequence-policy actions and preserve coupled
environmental/social crisis repair after the engineered planner is removed?
```

The benchmark keeps the hard setting:

- `96h` worlds;
- no major crisis before `12h`;
- randomized post-gate crisis timing, order, repetition, and initial pressure;
- learned base GRU;
- learned environmental and social crisis action heads;
- completed-crisis behavior traces from Report 126 sources;
- targeted social/environment ablations.

## What Changed

Report 126 trained a recurrent policy by weighting copied active-crisis actions
by their completed crisis outcome. Report 127 adds a separate process-value
critic.

For every action inside a completed crisis window, the critic receives:

- current active-crisis process features;
- one candidate action from the bounded action set;
- the completed crisis-window return as the target.

At evaluation, the engineered planner is removed. The consequence policy still
produces active-crisis logits, but the process-value critic adds a learned
reranking bias to candidate actions.

This is still bounded process-value learning. The action set, behavior sources,
and value target are supplied. It is not open-ended deep RL, unsupplied action
discovery, subjective consciousness, or solved civilization.

## Canonical Command

```bash
python3 experiments/ssrm_3d_coupled_crisis_sequence_value_recovery_controller.py --train-seeds 20260911,20260912,20260913 --tune-seeds 20261111,20261112 --eval-seeds 20261121,20261122,20261123 --hours 96 --step-hours 0.10 --population 14 --epochs 24 --hidden-size 64 --action-epochs 32 --action-hidden-size 64 --consequence-epochs 14 --consequence-hidden-size 64 --process-value-epochs 18 --process-value-hidden-size 64 --max-process-value-examples 180000 --student-iterations 1 --policy-bias-candidates 0.0,0.20,0.40,0.70,1.00 --process-value-bias-candidates 0.0,0.25,0.50,0.80,1.10,1.50 --device auto --trace-seed 20261121
```

## Training Result

The process-value critic trains on the same aggregate source as Report 126:
`133` completed crisis sequences and `166169` active-crisis examples.

| Metric | Value |
|---|---:|
| process-value examples | `166169` |
| source sequences | `133` |
| final process-value loss | `0.383` |
| train MAE | `1.480` |
| pairwise accuracy | `0.701` |
| positive example rate | `0.595` |
| env action fraction | `0.578` |
| social action fraction | `0.277` |
| none fraction | `0.145` |

The critic has real offline signal. It can rank higher-return examples better
than chance. The closed-loop question is whether that signal improves held-out
recovery after planner removal.

## Bias Selection

Validation selected process-value bias `0.25`.

| Bias | Tune total | Tune crisis | Tune resolved | Tune coupled | Damage | Selected |
|---:|---:|---:|---:|---:|---:|---|
| `0.00` | `0.512` | `0.017` | `0.250` | `0.171` | `1.479` | no |
| `0.25` | `0.503` | `0.048` | `0.533` | `0.167` | `1.434` | yes |
| `0.50` | `0.518` | `0.008` | `0.350` | `0.186` | `1.439` | no |
| `0.80` | `0.520` | `0.000` | `0.167` | `0.167` | `1.516` | no |
| `1.10` | `0.520` | `0.000` | `0.250` | `0.181` | `1.634` | no |
| `1.50` | `0.520` | `0.000` | `0.167` | `0.167` | `1.753` | no |

The selected setting improves validation resolved rate, but it does not
transfer into a stronger held-out recovery policy.

## Held-Out Result

| Controller | Total score | Crisis score | Resolved rate | Env response | Social response | Coupled response |
|---|---:|---:|---:|---:|---:|---:|
| fixed joint GRU | `0.843` | `0.675` | `0.933` | `0.863` | `1.000` | `0.863` |
| min-channel planner GRU | `0.797` | `0.590` | `0.878` | `0.828` | `1.000` | `0.828` |
| consequence-recovery GRU | `0.532` | `0.028` | `0.356` | `0.355` | `1.000` | `0.355` |
| return-selected GRU | `0.516` | `0.000` | `0.000` | `0.299` | `0.346` | `0.000` |
| sequence-value recovery GRU | `0.491` | `0.003` | `0.356` | `0.355` | `1.000` | `0.355` |
| base GRU | `0.293` | `0.000` | `0.000` | `0.299` | `0.000` | `0.000` |
| frame MLP | `0.287` | `0.000` | `0.000` | `0.299` | `0.000` | `0.000` |
| reactive | `0.090` | `0.000` | `0.000` | `0.280` | `0.000` | `0.000` |

The verdict is:

```text
mean_crisis_count = 5.667
supports_process_value_recovery = false
supports_teacher_transfer = false
supports_social_environment_dependency = true
verdict = partial_or_failed
```

The process-value critic does not improve Report 126. It keeps the same
resolved rate and coupled response, but crisis score falls from `0.028` to
`0.003`, total score falls from `0.532` to `0.491`, and the planner remains far
stronger.

## Ablation Boundary

| Ablation | Crisis score | Crisis loss | Coupled response | Coupled loss |
|---|---:|---:|---:|---:|
| none | `0.003` | - | `0.355` | - |
| social_culture | `0.000` | `0.003` | `0.000` | `0.355` |
| environment | `0.000` | `0.003` | `0.000` | `0.355` |
| previous_action | `0.024` | `-0.020` | `0.280` | `0.075` |
| body | `0.092` | `-0.089` | `0.534` | `-0.178` |
| tools | `0.000` | `0.003` | `0.233` | `0.122` |
| infrastructure | `0.000` | `0.003` | `0.299` | `0.056` |

The social/environment dependency is visible on coupled response, but the
base crisis score is too low for the recovery claim. The body ablation also
improves several metrics, which is another sign that the learned reranking is
not stable enough to interpret as robust recovery.

## Interpretation

This is a negative boundary.

The useful part: completed-window process-value labels contain signal. The
critic reaches `0.701` pairwise accuracy across `166169` examples, and
validation chooses a nonzero process-value bias.

The failure: a critic that scores individual candidate actions by completed
window outcome is still too myopic. It does not learn the actual sequence
allocation behavior that makes the minimum-channel planner work. It preserves
some coupled-response behavior but worsens total score, crisis score, damage,
and survival relative to Report 126.

The next credible step is not more scalar action reranking. The benchmark needs
explicit counterfactual sequence search or learned rollout evaluation over
multi-action windows:

- evaluate candidate action sequences, not independent single actions;
- model how one action changes the next response context;
- penalize policies that keep social response high while starving environmental
  repair;
- train from counterfactual rollouts over the same active-crisis state;
- require improvement over Report 126 and transfer margin against the planner.

## Artifacts

- [script](../experiments/ssrm_3d_coupled_crisis_sequence_value_recovery_controller.py)
- [schedule CSV](../artifacts/ssrm_3d_coupled_crisis_sequence_value_recovery_schedule.csv)
- [base training CSV](../artifacts/ssrm_3d_coupled_crisis_sequence_value_recovery_base_training.csv)
- [action training CSV](../artifacts/ssrm_3d_coupled_crisis_sequence_value_recovery_action_training.csv)
- [router selection CSV](../artifacts/ssrm_3d_coupled_crisis_sequence_value_recovery_router_selection.csv)
- [planner selection CSV](../artifacts/ssrm_3d_coupled_crisis_sequence_value_recovery_planner_selection.csv)
- [source summary CSV](../artifacts/ssrm_3d_coupled_crisis_sequence_value_recovery_source_summary.csv)
- [consequence training CSV](../artifacts/ssrm_3d_coupled_crisis_sequence_value_recovery_consequence_training.csv)
- [process-value training CSV](../artifacts/ssrm_3d_coupled_crisis_sequence_value_recovery_process_value_training.csv)
- [policy selection CSV](../artifacts/ssrm_3d_coupled_crisis_sequence_value_recovery_policy_selection.csv)
- [process-value selection CSV](../artifacts/ssrm_3d_coupled_crisis_sequence_value_recovery_process_value_selection.csv)
- [evaluation CSV](../artifacts/ssrm_3d_coupled_crisis_sequence_value_recovery_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_coupled_crisis_sequence_value_recovery_summary.csv)
- [ablation CSV](../artifacts/ssrm_3d_coupled_crisis_sequence_value_recovery_ablations.csv)
- [verdict CSV](../artifacts/ssrm_3d_coupled_crisis_sequence_value_recovery_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_coupled_crisis_sequence_value_recovery_trace.json)
- [results JSON](../artifacts/ssrm_3d_coupled_crisis_sequence_value_recovery_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_coupled_crisis_sequence_value_recovery_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_coupled_crisis_sequence_value_recovery_results.js)
