# SSRM-3D Coupled Crisis MPC Sequence Optimizer Report

## Question

Report 130 showed that delayed active policy-gradient fine-tuning and
single-action consequence-value scoring still do not preserve robust coupled
environmental/social crisis repair. The value controller improved over weak
return-selected control, but it stayed below consequence recovery and did not
clear the coupled-repair gate.

This report tests the next narrower claim:

```text
If the controller evaluates and commits to multi-step repair sequences, can it
recover the coupled environmental/social repair shape that single-action
consequence scoring misses?
```

The benchmark keeps the hard setting:

- `96h` worlds;
- no major crisis before `12h`;
- randomized post-gate crisis timing, order, repetition, and initial pressure;
- learned base GRU;
- learned environmental and social action heads;
- recurrent consequence-recovery baseline;
- model-predictive scoring of supplied repair-plan templates through cloned
  simulator rollout;
- tuned sequence-commitment window;
- targeted social/environment ablations.

This is bounded evidence. The controller uses supplied plan templates and
cloned simulator rollout scoring. It is not open-ended civilization, not
subjective consciousness, not deep RL, and not a learned policy that has already
internalized the planner.

## Canonical Command

```bash
python3 experiments/ssrm_3d_coupled_crisis_mpc_sequence_optimizer_controller.py --train-seeds 20260911,20260912,20260913 --tune-seeds 20261111,20261112 --eval-seeds 20261121,20261122,20261123 --hours 96 --step-hours 0.10 --population 14 --epochs 14 --hidden-size 48 --action-epochs 18 --action-hidden-size 48 --consequence-epochs 8 --consequence-hidden-size 48 --consequence-return-scale 1.15 --student-iterations 0 --policy-bias-candidates 0.0,0.40,0.80 --commit-candidates 14,42 --device auto --trace-seed 20261121
```

## What Changed

Report 131 does not add another single-action reranker. It clones the current
simulator state, scores candidate repair-plan templates over short future
windows, chooses the strongest sequence, and commits to that plan for a tuned
number of agent actions before replanning.

The practical change is temporal commitment:

```text
single action value -> choose one action now
sequence optimizer -> choose and sustain a repair sequence long enough to keep
both environmental and social channels active
```

This is a model-predictive planning bridge. It uses the same benchmark pressure
as the learned recovery line, but it does not claim that the GRU has learned the
planning rule internally.

## Training And Selection

The behavior-source consequence policy again trains cleanly:

| Metric | Value |
|---|---:|
| source sequences | `114` |
| student sequences | `0` |
| aggregate examples | `143384` |
| consequence train accuracy | `0.992` |
| consequence weighted accuracy | `0.990` |

Validation selected the high-pressure router, the `conservative_min` planner
family, consequence bias `0.0`, and `14` committed actions per sequence.

| Commit actions | Tune total | Tune crisis | Tune resolved | Tune coupled | Tune damage | Selected |
|---:|---:|---:|---:|---:|---:|---|
| `14` | `0.656` | `0.283` | `0.633` | `0.489` | `0.838` | yes |
| `42` | `0.651` | `0.273` | `0.633` | `0.508` | `0.889` | no |

The shorter commitment wins by a small margin. It gives the controller enough
time to execute a sequence without locking it into stale plans for too long.

## Held-Out Result

| Controller | Total score | Crisis score | Resolved rate | Env response | Social response | Coupled response |
|---|---:|---:|---:|---:|---:|---:|
| designed | `0.830` | `0.694` | `1.000` | `0.720` | `0.660` | `0.451` |
| MPC sequence optimizer GRU | `0.683` | `0.348` | `0.656` | `0.645` | `0.850` | `0.565` |
| min-channel planner GRU | `0.524` | `0.022` | `0.411` | `0.411` | `1.000` | `0.411` |
| fixed joint GRU | `0.524` | `0.021` | `0.411` | `0.411` | `1.000` | `0.411` |
| consequence-recovery GRU | `0.512` | `0.004` | `0.356` | `0.356` | `1.000` | `0.356` |
| return-selected GRU | `0.487` | `0.000` | `0.056` | `0.299` | `0.084` | `0.040` |
| base GRU | `0.290` | `0.000` | `0.000` | `0.299` | `0.000` | `0.000` |
| frame MLP | `0.287` | `0.000` | `0.000` | `0.299` | `0.000` | `0.000` |
| reactive | `0.090` | `0.000` | `0.000` | `0.280` | `0.000` | `0.000` |

The verdict is:

```text
mean_crisis_count = 5.667
selected_commit_actions = 14
mpc_gain_over_consequence = 0.171
mpc_gain_over_return_selected = 0.196
supports_mpc_sequence_optimization = true
supports_teacher_transfer = false
supports_social_environment_dependency = true
verdict = partial_or_failed
```

## Interpretation

This is the first materially positive result after the active consequence
boundary. Multi-step sequence optimization improves the held-out controller
over consequence recovery:

- total score rises from `0.512` to `0.683`;
- crisis score rises from `0.004` to `0.348`;
- resolved rate rises from `0.356` to `0.656`;
- coupled response rises from `0.356` to `0.565`.

It also sharply beats the return-selected baseline:

- total score rises from `0.487` to `0.683`;
- crisis score rises from `0.000` to `0.348`;
- resolved rate rises from `0.056` to `0.656`;
- coupled response rises from `0.040` to `0.565`.

The result still records `partial_or_failed`, not `pass`, because the strict
teacher-transfer gate is missed. The crisis score is `0.348`; the run threshold
requires `>= 0.350`. The miss is only about `0.002`, but the threshold should
not be moved after the result.

The supported claim is narrow:

```text
Multi-step consequence planning can restore the coupled repair shape that
single-action value scoring and supervised labels failed to preserve.
```

The unsupported claim remains:

```text
A learned recurrent policy has internalized this sequence optimizer without
cloned simulator lookahead.
```

## Ablation Boundary

The sequence optimizer depends on both social/culture and environment channels.

| Ablation | Total score | Total loss | Crisis score | Crisis loss | Coupled response | Coupled loss |
|---|---:|---:|---:|---:|---:|---:|
| none | `0.683` | - | `0.348` | - | `0.565` | - |
| social_culture | `0.490` | `0.193` | `0.000` | `0.348` | `0.000` | `0.565` |
| environment | `0.520` | `0.163` | `0.000` | `0.348` | `0.000` | `0.565` |
| body | `0.675` | `0.009` | `0.322` | `0.025` | `0.531` | `0.034` |
| infrastructure | `0.699` | `-0.015` | `0.466` | `-0.119` | `0.659` | `-0.094` |
| tools | `0.661` | `0.022` | `0.347` | `0.000` | `0.595` | `-0.030` |
| previous_action | `0.684` | `-0.001` | `0.348` | `-0.001` | `0.572` | `-0.007` |

The social/culture and environment ablations collapse the exact channels that
define the coupled-crisis requirement. Other ablations are weaker or mixed,
which reinforces that this report is about the social/environment coupling
boundary rather than every possible state channel.

## Boundary

Report 131 rules out one pessimistic interpretation of Reports 124-130:

```text
The coupled crisis task is not inherently impossible after planner removal.
When the controller is allowed to evaluate and commit to multi-step
consequence sequences, the missing coupled repair shape reappears.
```

It also defines the next hard target:

```text
Distill or learn the sequence optimizer itself. The next controller must
recover this multi-step consequence behavior without cloned simulator rollout
access, supplied plan-template scoring, or engineered weakest-channel planning.
```

## Artifacts

- [script](../experiments/ssrm_3d_coupled_crisis_mpc_sequence_optimizer_controller.py)
- [schedule CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_sequence_optimizer_schedule.csv)
- [base training CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_sequence_optimizer_base_training.csv)
- [action training CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_sequence_optimizer_action_training.csv)
- [consequence training CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_sequence_optimizer_consequence_training.csv)
- [source summary CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_sequence_optimizer_source_summary.csv)
- [router selection CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_sequence_optimizer_router_selection.csv)
- [planner selection CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_sequence_optimizer_planner_selection.csv)
- [consequence selection CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_sequence_optimizer_consequence_selection.csv)
- [commit selection CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_sequence_optimizer_commit_selection.csv)
- [plan use CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_sequence_optimizer_plan_use.csv)
- [evaluation CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_sequence_optimizer_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_sequence_optimizer_summary.csv)
- [ablation CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_sequence_optimizer_ablations.csv)
- [verdict CSV](../artifacts/ssrm_3d_coupled_crisis_mpc_sequence_optimizer_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_coupled_crisis_mpc_sequence_optimizer_trace.json)
- [results JSON](../artifacts/ssrm_3d_coupled_crisis_mpc_sequence_optimizer_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_coupled_crisis_mpc_sequence_optimizer_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_coupled_crisis_mpc_sequence_optimizer_results.js)
