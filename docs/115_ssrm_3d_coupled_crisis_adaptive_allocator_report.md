# SSRM-3D Coupled Crisis Adaptive Allocator Report

## Question

Report 114 showed that a structured joint-arbitration controller transfers beyond one fixed post-12h crisis schedule.

This report tests the next weakness:

```text
Can allocation between environmental repair and social repair be trained from closed-loop return instead of selected as a fixed quota triple?
```

The benchmark keeps the 96h randomized-transfer world from Report 114. No major crisis is allowed before `12h`; after that gate, crisis timing, order, repetition, and initial world pressure vary by seed.

## What Changed

The experiment keeps the learned base GRU and the separate learned environmental/social action heads, but replaces the fixed joint quota grid with a compact adaptive allocator.

The allocator receives engineered pressure summaries from ordinary observation features:

- environmental pressure;
- social pressure;
- infrastructure need;
- tool need;
- teaching need;
- body need;
- weather pressure;
- resource need;
- current environmental/social response fractions;
- response imbalance.

It outputs dynamic environmental target, social target, and coordinator strength. Those parameters are optimized by closed-loop return search over tune worlds, not by supervised action labels.

This reduces one piece of structural help. It does not remove all structure.

## What This Does Not Claim

This is not actor-critic reinforcement learning, subjective consciousness, open-ended civilization, or a real-world competence claim.

The allocator features are engineered summaries, and the environmental/social action heads remain supervised. The result is a bounded adaptive-allocation precursor.

## Canonical Command

```bash
python3 experiments/ssrm_3d_coupled_crisis_adaptive_allocator_controller.py --train-seeds 20260911,20260912,20260913,20260914,20260915,20260916 --tune-seeds 20261111,20261112,20261113 --eval-seeds 20261121,20261122,20261123,20261124,20261125 --hours 96 --step-hours 0.10 --population 14 --epochs 36 --hidden-size 64 --action-epochs 52 --action-hidden-size 64 --allocator-iterations 2 --allocator-population 7 --allocator-elites 3 --allocator-sigma 0.42 --device auto --trace-seed 20261121
```

## Result

Validation selects router:

```text
selected_router = social_first
allocator_iterations = 2
allocator_population = 7
```

Held-out randomized evaluation:

| Controller | Total score | Crisis score | Resolved rate | Coupled response |
|---|---:|---:|---:|---:|
| adaptive allocator GRU | `0.624` | `0.224` | `0.620` | `0.615` |
| fixed joint GRU | `0.594` | `0.162` | `0.580` | `0.576` |
| return-selected GRU | `0.516` | `0.000` | `0.000` | `0.004` |
| base GRU | `0.490` | `0.000` | `0.033` | `0.034` |
| designed | `0.755` | `0.521` | `1.000` | `0.000` |
| frame MLP | `0.284` | `0.000` | `0.000` | `0.000` |
| reactive | `0.095` | `0.000` | `0.000` | `0.000` |

The adaptive allocator improves over both return-selected and fixed-joint baselines in this canonical run:

```text
adaptive gain over return-selected total score = 0.108
adaptive crisis gain over return-selected = 0.224
adaptive resolved-rate gain over return-selected = 0.620
adaptive coupled-response gain over return-selected = 0.611
adaptive total-score advantage over fixed joint = 0.030
adaptive crisis-score advantage over fixed joint = 0.063
```

But the stronger non-fixed-transfer gate fails:

```text
supports_adaptive_allocation = true
supports_non_fixed_transfer = false
supports_social_environment_dependency = true
verdict = partial_or_failed
```

The reason is simple: `0.224` crisis score is a real improvement, but it is not high enough to claim that adaptive allocation has replaced the structured fixed-quota bridge.

## Ablation Boundary

The adaptive result still depends on both channels:

| Ablation | Crisis loss | Coupled response loss |
|---|---:|---:|
| `social_culture` | `0.224` | `0.615` |
| `environment` | `0.224` | `0.615` |
| `previous_action` | `0.117` | `0.211` |
| `tools` | `0.120` | `0.124` |
| `body` | `0.171` | `0.108` |
| `infrastructure` | `0.120` | `0.095` |

Removing either social/culture or environment collapses crisis score and coupled response. That part of the boundary remains clean.

## Allocation Probe

The selected allocator produces dynamic targets rather than one fixed quota:

| Eval seed | Hour | Env target | Social target | Strength |
|---:|---:|---:|---:|---:|
| `20261121` | `15.985` | `0.126` | `0.261` | `1.038` |
| `20261121` | `77.641` | `0.123` | `0.273` | `1.024` |
| `20261122` | `15.283` | `0.127` | `0.260` | `1.039` |
| `20261123` | `87.749` | `0.124` | `0.275` | `1.022` |
| `20261125` | `13.720` | `0.127` | `0.260` | `1.039` |

The variation is present but modest. That matters: the allocator is not simply a grid-selected quota, but it has not yet learned a strong enough allocation rule to match the best structured transfer result.

## Interpretation

This report is progress, not a pass.

It shows that return search over a compact allocator can recover some coupled-crisis behavior in the 96h randomized world:

```text
return-selected GRU: no crisis repair
fixed joint GRU: partial repair
adaptive allocator GRU: better partial repair
```

It also shows the next bottleneck. The current allocator improves allocation but remains too weak and too engineered. A mature version should learn allocation from policy/value consequences directly, with less feature engineering and without supervised action heads.

## Next Step

The next benchmark should move from compact return-searched allocation to a direct consequence-trained policy:

- train actor-critic or model-based policy over crisis windows;
- let the policy allocate agents to environmental/social/tool/sustain/teaching actions directly;
- keep randomized schedules, initial pressure, and held-out seeds;
- add stronger crisis-family randomization;
- train against delayed damage, overfocus, wrong-channel repair, and repair timing;
- require social/environment ablations to collapse the learned policy while preserving the 12h shock gate.

## Artifacts

- [script](../experiments/ssrm_3d_coupled_crisis_adaptive_allocator_controller.py)
- [schedule CSV](../artifacts/ssrm_3d_coupled_crisis_adaptive_allocator_schedule.csv)
- [base training CSV](../artifacts/ssrm_3d_coupled_crisis_adaptive_allocator_base_training.csv)
- [action training CSV](../artifacts/ssrm_3d_coupled_crisis_adaptive_allocator_action_training.csv)
- [router selection CSV](../artifacts/ssrm_3d_coupled_crisis_adaptive_allocator_router_selection.csv)
- [allocator selection CSV](../artifacts/ssrm_3d_coupled_crisis_adaptive_allocator_allocator_selection.csv)
- [allocator probes CSV](../artifacts/ssrm_3d_coupled_crisis_adaptive_allocator_allocator_probes.csv)
- [evaluation CSV](../artifacts/ssrm_3d_coupled_crisis_adaptive_allocator_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_coupled_crisis_adaptive_allocator_summary.csv)
- [ablation CSV](../artifacts/ssrm_3d_coupled_crisis_adaptive_allocator_ablations.csv)
- [verdict CSV](../artifacts/ssrm_3d_coupled_crisis_adaptive_allocator_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_coupled_crisis_adaptive_allocator_trace.json)
- [results JSON](../artifacts/ssrm_3d_coupled_crisis_adaptive_allocator_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_coupled_crisis_adaptive_allocator_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_coupled_crisis_adaptive_allocator_results.js)
