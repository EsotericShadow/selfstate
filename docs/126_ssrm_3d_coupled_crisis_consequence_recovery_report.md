# SSRM-3D Coupled Crisis Consequence Recovery Report

## Question

Reports 124 and 125 showed that planner labels alone are not enough. Offline
planner imitation failed after planner removal, and DAgger-style relabeling of
student-visited states still collapsed held-out crisis repair.

This report tests the next narrower claim:

```text
If recurrent active-crisis policy training is weighted by completed crisis
outcomes, rather than only by planner labels, does the learned policy preserve
coupled environmental/social crisis repair after the engineered planner is
removed?
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

The consequence-recovery controller collects active-crisis sequences from
several behavior sources:

- return-selected GRU;
- fixed joint coordination;
- high-environment joint coordination;
- high-social joint coordination;
- balanced strong joint coordination;
- minimum-channel planner;
- one student-policy collection pass.

Each completed crisis window receives a scalar consequence return based on
later crisis progress, resolution, channel balance, and damage. The recurrent
policy is then trained with stronger weight on actions from better completed
crisis outcomes.

This is bounded consequence training. It is not open-ended deep RL,
unsupplied action discovery, subjective consciousness, or a solved civilization
simulation.

## Canonical Command

```bash
python3 experiments/ssrm_3d_coupled_crisis_consequence_recovery_controller.py --train-seeds 20260911,20260912,20260913 --tune-seeds 20261111,20261112 --eval-seeds 20261121,20261122,20261123 --hours 96 --step-hours 0.10 --population 14 --epochs 24 --hidden-size 64 --action-epochs 32 --action-hidden-size 64 --consequence-epochs 14 --consequence-hidden-size 64 --consequence-return-scale 1.15 --student-iterations 1 --student-collection-bias 0.70 --policy-bias-candidates 0.0,0.20,0.40,0.70,1.00 --device auto --trace-seed 20261121
```

## Source Consequences

The source traces are not all equivalent. The return-selected GRU produces
negative crisis-window returns, while the structured coordination sources and
minimum-channel planner produce positive returns.

| Source | Sequences | Examples | Mean return | Positive rate | Env action | Social action | None |
|---|---:|---:|---:|---:|---:|---:|---:|
| min-channel planner | `19` | `22855` | `1.892` | `0.842` | `0.460` | `0.271` | `0.269` |
| high-env joint | `19` | `25900` | `1.518` | `0.737` | `0.673` | `0.253` | `0.074` |
| high-social joint | `19` | `22615` | `1.439` | `0.737` | `0.559` | `0.307` | `0.134` |
| balanced strong joint | `19` | `25728` | `1.421` | `0.737` | `0.612` | `0.336` | `0.052` |
| fixed joint | `19` | `24842` | `1.342` | `0.737` | `0.618` | `0.270` | `0.113` |
| student iteration 1 | `19` | `21340` | `0.231` | `0.368` | `0.472` | `0.276` | `0.251` |
| return-selected | `19` | `22889` | `-1.056` | `0.000` | `0.623` | `0.221` | `0.156` |

This confirms that the consequence signal separates weak and strong behavior
sources.

## Training Result

The final aggregate training set contains `133` crisis sequences and `166169`
active-crisis examples.

| Iteration | Source | Aggregate examples | Train accuracy | Weighted accuracy | Mean return | Positive rate |
|---:|---|---:|---:|---:|---:|---:|
| `0` | behavior_sources | `144829` | `0.988` | `0.986` | `1.093` | `0.632` |
| `1` | student_iteration_1 | `166169` | `0.986` | `0.982` | `0.970` | `0.594` |

The policy can fit the return-weighted trace distribution. The real question
is whether that fit transfers into held-out closed-loop crisis repair.

## Policy Bias Selection

Validation selected policy bias `1.0`.

| Bias | Tune total | Tune crisis | Tune resolved | Tune coupled | Damage | Selected |
|---:|---:|---:|---:|---:|---:|---|
| `0.0` | `0.520` | `0.000` | `0.267` | `0.200` | `1.404` | no |
| `0.2` | `0.542` | `0.045` | `0.350` | `0.273` | `1.355` | no |
| `0.4` | `0.561` | `0.094` | `0.333` | `0.251` | `1.537` | no |
| `0.7` | `0.530` | `0.041` | `0.433` | `0.212` | `1.481` | no |
| `1.0` | `0.582` | `0.140` | `0.333` | `0.334` | `1.591` | yes |

Unlike Report 125, validation found nonzero tune crisis score for several
settings.

## Held-Out Result

The consequence-weighted policy improves over the return-selected GRU, but it
does not pass the strong recovery or teacher-transfer gates.

| Controller | Total score | Crisis score | Resolved rate | Env response | Social response | Coupled response |
|---|---:|---:|---:|---:|---:|---:|
| fixed joint GRU | `0.843` | `0.675` | `0.933` | `0.863` | `1.000` | `0.863` |
| min-channel planner GRU | `0.797` | `0.590` | `0.878` | `0.828` | `1.000` | `0.828` |
| designed | `0.830` | `0.694` | `1.000` | `0.720` | `0.660` | `0.451` |
| consequence-recovery GRU | `0.532` | `0.028` | `0.356` | `0.355` | `1.000` | `0.355` |
| return-selected GRU | `0.516` | `0.000` | `0.000` | `0.299` | `0.346` | `0.000` |
| base GRU | `0.293` | `0.000` | `0.000` | `0.299` | `0.000` | `0.000` |
| frame MLP | `0.287` | `0.000` | `0.000` | `0.299` | `0.000` | `0.000` |
| reactive | `0.090` | `0.000` | `0.000` | `0.280` | `0.000` | `0.000` |

The verdict is:

```text
mean_crisis_count = 5.667
supports_consequence_recovery = false
supports_teacher_transfer = false
supports_social_environment_dependency = true
verdict = partial_or_failed
```

This is the first post-Report-123 learned-policy attempt in this sequence that
recovers a nonzero held-out crisis score and clear coupled response after
planner removal. It still falls far short of the planner and fixed-joint
baselines.

## Ablation Boundary

The ablations now show a real social/environment dependency on coupled
response, because the unablated policy has nonzero coupled response.

| Ablation | Crisis score | Crisis loss | Coupled response | Coupled loss |
|---|---:|---:|---:|---:|
| none | `0.028` | - | `0.355` | - |
| social_culture | `0.000` | `0.028` | `0.000` | `0.355` |
| environment | `0.000` | `0.028` | `0.000` | `0.355` |
| previous_action | `0.031` | `-0.002` | `0.356` | `-0.001` |
| body | `0.000` | `0.028` | `0.400` | `-0.045` |
| tools | `0.000` | `0.028` | `0.233` | `0.122` |
| infrastructure | `0.012` | `0.016` | `0.299` | `0.056` |

This supports only the dependency subclaim, not the full recovery claim. The
main crisis score is too low.

## Interpretation

This is a partial positive and still a failed strong result.

The good news: consequence weighting does something that Reports 124 and 125
did not. It creates nonzero held-out crisis score, nonzero resolved rate, and
nonzero coupled environmental/social response after planner removal. It also
makes social/culture and environment ablations collapse the coupled response.

The bad news: the magnitude is still weak. Crisis score is only `0.028` versus
`0.590` for the minimum-channel planner and `0.675` for fixed-joint
coordination. The policy responds socially all the time and still under-solves
environmental repair, so it gets some coupled-response credit without learning
robust recovery.

The lesson is precise: completed-crisis consequence weighting is closer to the
right training shape than label-only recovery, but it still needs stronger
counterfactual sequence/value training before it can replace structured
planning.

## Next Step

Do not claim open-ended learned civilization.

The next credible step is to train a crisis-window value/process critic that
scores candidate action sequences, not only individual actions copied from
behavior traces:

- learn from counterfactual rollouts for the same active-crisis state;
- penalize one-channel policies that keep social response high while starving
  environmental repair;
- optimize for crisis score, resolution, coupled response, and damage together;
- keep the 96h randomized post-gate world;
- keep nonzero crisis score and teacher-transfer margin as the recovery gate.

Only after learned policies can preserve coupled repair should richer
settlement, territory, construction, tool chains, and social infrastructure be
treated as solved learned-control evidence rather than designed world pressure.

## Artifacts

- [script](../experiments/ssrm_3d_coupled_crisis_consequence_recovery_controller.py)
- [schedule CSV](../artifacts/ssrm_3d_coupled_crisis_consequence_recovery_schedule.csv)
- [base training CSV](../artifacts/ssrm_3d_coupled_crisis_consequence_recovery_base_training.csv)
- [action training CSV](../artifacts/ssrm_3d_coupled_crisis_consequence_recovery_action_training.csv)
- [router selection CSV](../artifacts/ssrm_3d_coupled_crisis_consequence_recovery_router_selection.csv)
- [planner selection CSV](../artifacts/ssrm_3d_coupled_crisis_consequence_recovery_planner_selection.csv)
- [source summary CSV](../artifacts/ssrm_3d_coupled_crisis_consequence_recovery_source_summary.csv)
- [consequence training CSV](../artifacts/ssrm_3d_coupled_crisis_consequence_recovery_consequence_training.csv)
- [policy selection CSV](../artifacts/ssrm_3d_coupled_crisis_consequence_recovery_policy_selection.csv)
- [evaluation CSV](../artifacts/ssrm_3d_coupled_crisis_consequence_recovery_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_coupled_crisis_consequence_recovery_summary.csv)
- [ablation CSV](../artifacts/ssrm_3d_coupled_crisis_consequence_recovery_ablations.csv)
- [verdict CSV](../artifacts/ssrm_3d_coupled_crisis_consequence_recovery_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_coupled_crisis_consequence_recovery_trace.json)
- [results JSON](../artifacts/ssrm_3d_coupled_crisis_consequence_recovery_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_coupled_crisis_consequence_recovery_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_coupled_crisis_consequence_recovery_results.js)
