# SSRM-3D Coupled Crisis Policy/Value Allocator Report

## Question

Report 115 showed that a compact return-searched allocator can recover some coupled-crisis repair, but it does not replace structured coordination.

This report tests the next step:

```text
Can a value model trained from closed-loop allocation consequences select better allocator policies for held-out 96h crisis worlds?
```

The benchmark keeps the same randomized-transfer world:

- `96h` runs;
- no major crisis before `12h`;
- randomized post-gate crisis timing, order, repetition, and initial pressure;
- learned base GRU;
- learned environmental and social action heads;
- no scenario labels in controller inputs.

## What Changed

The experiment rolls out candidate allocator policies on tune worlds, records their actual consequences, trains a small value model over allocator-policy parameters, then uses that value model to choose which additional allocator candidates deserve expensive rollout.

The selected allocator is then evaluated on held-out worlds against:

- return-selected GRU;
- seed allocator;
- fixed-joint allocator;
- designed controller;
- frame, base GRU, and reactive controls.

This is consequence-trained selection, not supervised action labeling.

## What This Does Not Claim

This is not actor-critic reinforcement learning, subjective consciousness, open-ended civilization, or real-world competence.

The allocator still uses engineered pressure summaries, and the environmental/social action heads are still supervised. The value model is a bounded selector over allocator policies, not a full state-value critic inside an autonomous agent.

## Canonical Command

```bash
python3 experiments/ssrm_3d_coupled_crisis_policy_value_allocator_controller.py --train-seeds 20260911,20260912,20260913,20260914,20260915,20260916 --tune-seeds 20261111,20261112,20261113 --eval-seeds 20261121,20261122,20261123,20261124,20261125 --hours 96 --step-hours 0.10 --population 14 --epochs 36 --hidden-size 64 --action-epochs 52 --action-hidden-size 64 --policy-value-samples 12 --policy-value-candidates 48 --policy-value-rollouts 5 --policy-value-epochs 180 --policy-value-hidden-size 64 --policy-value-sigma 0.52 --device auto --trace-seed 20261121
```

## Result

The value selector did find a better tune-world candidate:

```text
seed tune objective = 1.186
selected tune objective = 1.354
best sample tune objective = 1.354
supports_consequence_value_selection = true
```

But the selected allocator transferred worse than the seed/fixed allocator on held-out worlds:

| Controller | Total score | Crisis score | Resolved rate | Coupled response |
|---|---:|---:|---:|---:|
| seed allocator GRU | `0.686` | `0.361` | `0.727` | `0.701` |
| fixed joint GRU | `0.686` | `0.361` | `0.727` | `0.701` |
| policy/value allocator GRU | `0.620` | `0.224` | `0.627` | `0.618` |
| return-selected GRU | `0.516` | `0.000` | `0.000` | `0.004` |
| base GRU | `0.490` | `0.000` | `0.033` | `0.034` |
| designed | `0.755` | `0.521` | `1.000` | `0.000` |
| frame MLP | `0.284` | `0.000` | `0.000` | `0.000` |
| reactive | `0.095` | `0.000` | `0.000` | `0.000` |

The verdict is:

```text
supports_return_baseline_improvement = true
supports_seed_transfer_improvement = false
supports_policy_value_allocation = false
supports_non_fixed_transfer = false
supports_social_environment_dependency = true
verdict = partial_or_failed
```

## Interpretation

This is a useful negative boundary.

The value selector learned the tune set too well. It selected a candidate that improved tune objective, but the policy did not generalize to the held-out randomized worlds. The result still beats the return-selected GRU, but that is not enough. A stronger policy/value claim has to beat the seed/fixed allocator too.

This narrows the next bottleneck:

```text
closed-loop value selection is not enough if the value model only scores allocator parameters from a small tune sample
```

The next controller needs value learning closer to the active crisis state, not just value prediction over whole allocator candidates.

## Ablation Boundary

The selected policy/value allocator still depends on both social/culture and environmental channels:

| Ablation | Crisis loss | Coupled response loss |
|---|---:|---:|
| `social_culture` | `0.224` | `0.618` |
| `environment` | `0.224` | `0.618` |
| `previous_action` | `-0.029` | `0.025` |
| `tools` | `-0.105` | `-0.048` |
| `infrastructure` | `-0.162` | `-0.116` |
| `body` | `-0.259` | `-0.177` |

The channel dependency remains clean for social/culture and environment, but several non-core ablations improve the score. That reinforces the conclusion that this is not yet a robust learned allocation policy.

## Next Step

Do not add more allocator-parameter selection.

The next benchmark should move value learning into the crisis window itself:

- train a state/action value model over active crisis observations;
- predict delayed damage, wrong-channel repair, overfocus, and timing cost;
- choose environmental/social/tool/sustain actions from state consequences, not whole-policy candidate scores;
- evaluate across held-out schedules and seeds;
- require improvement over seed/fixed allocator, not only return-selected GRU;
- keep social/culture and environment ablations as collapse tests.

## Artifacts

- [script](../experiments/ssrm_3d_coupled_crisis_policy_value_allocator_controller.py)
- [schedule CSV](../artifacts/ssrm_3d_coupled_crisis_policy_value_allocator_schedule.csv)
- [base training CSV](../artifacts/ssrm_3d_coupled_crisis_policy_value_allocator_base_training.csv)
- [action training CSV](../artifacts/ssrm_3d_coupled_crisis_policy_value_allocator_action_training.csv)
- [router selection CSV](../artifacts/ssrm_3d_coupled_crisis_policy_value_allocator_router_selection.csv)
- [policy/value selection CSV](../artifacts/ssrm_3d_coupled_crisis_policy_value_allocator_policy_value_selection.csv)
- [policy/value training CSV](../artifacts/ssrm_3d_coupled_crisis_policy_value_allocator_policy_value_training.csv)
- [allocator probes CSV](../artifacts/ssrm_3d_coupled_crisis_policy_value_allocator_allocator_probes.csv)
- [evaluation CSV](../artifacts/ssrm_3d_coupled_crisis_policy_value_allocator_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_coupled_crisis_policy_value_allocator_summary.csv)
- [ablation CSV](../artifacts/ssrm_3d_coupled_crisis_policy_value_allocator_ablations.csv)
- [verdict CSV](../artifacts/ssrm_3d_coupled_crisis_policy_value_allocator_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_coupled_crisis_policy_value_allocator_trace.json)
- [results JSON](../artifacts/ssrm_3d_coupled_crisis_policy_value_allocator_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_coupled_crisis_policy_value_allocator_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_coupled_crisis_policy_value_allocator_results.js)
