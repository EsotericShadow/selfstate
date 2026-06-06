# SSRM-3D Coupled Crisis Joint-Arbitration Report

## Question

Report 112 showed a sharp failure: a recurrent diagnostic head could learn the environmental repair label offline, but using that label online disrupted social repair and validation turned it off.

This report tests the next narrower repair:

```text
Can separate learned environmental and social action heads, coordinated by validation-selected joint arbitration, preserve both repair channels during coupled post-12h crises?
```

The point is not to hand the model the crisis name. The action heads receive ordinary observation features and previous-action context. They do not receive the active crisis profile label at runtime.

## What Changed

The benchmark keeps the stricter Report 110-112 coupled-crisis world:

- no major crisis before the 12h development gate;
- post-gate crises require both environmental repair and social coordination;
- each crisis has non-substitutable environmental repair classes;
- wrong environmental actions add damage instead of repair credit;
- learned-controller inputs do not receive active crisis profile labels.

The new component is a joint coordinator around two recurrent action heads:

- an environmental action head trained on crisis-window environmental repair actions;
- a social action head trained on crisis-window social coordination actions;
- validation-selected environmental and social action quotas;
- validation-selected coordinator strength;
- fair same-seed comparison across controllers and ablations.

The report also makes channel ablations explicit. When the environmental channel is ablated, environmental crisis actions are suppressed. When the social/culture channel is ablated, social crisis actions are suppressed. This prevents fallback logits from quietly routing around the removed channel.

## What This Does Not Claim

This is not actor-critic reinforcement learning, policy-gradient training, open-ended civilization, subjective consciousness, or a production software-engineering controller.

It is a structured learned-coordination precursor: recurrent action heads plus validation-selected joint arbitration. The experiment is allowed to pass only if the selected coordinator improves held-out coupled-crisis repair and both social/environment channel ablations create specific losses.

## Canonical Command

```bash
python3 experiments/ssrm_3d_coupled_crisis_joint_arbitration_controller.py --train-seeds 20260911,20260912,20260913,20260914,20260915,20260916 --tune-seeds 20261011,20261012,20261013 --eval-seeds 20261021,20261022,20261023,20261024,20261025 --hours 72 --step-hours 0.10 --population 14 --epochs 42 --hidden-size 64 --action-epochs 64 --action-hidden-size 64 --joint-candidates 0.00:0.00:0.00,0.12:0.12:0.70,0.14:0.14:0.85,0.16:0.14:1.00,0.14:0.16:1.00,0.18:0.16:1.10,0.16:0.18:1.10,0.20:0.18:1.20 --device auto --trace-seed 20261021
```

## Result

Validation selects:

```text
selected_router = social_first
selected_env_quota = 0.14
selected_social_quota = 0.14
selected_coordinator_strength = 0.85
```

Held-out evaluation:

| Controller | Total score | Crisis score | Resolved rate | Env response | Social response | Coupled response |
|---|---:|---:|---:|---:|---:|---:|
| designed | `0.773` | `0.527` | `1.000` | `0.077` | `0.923` | `0.000` |
| joint-arbitration GRU | `0.702` | `0.380` | `0.650` | `0.646` | `1.000` | `0.646` |
| return-selected GRU | `0.519` | `0.000` | `0.100` | `0.277` | `0.313` | `0.027` |
| base GRU | `0.519` | `0.000` | `0.000` | `0.000` | `0.268` | `0.000` |
| frame MLP | `0.330` | `0.000` | `0.000` | `0.250` | `0.000` | `0.000` |
| reactive | `0.240` | `0.000` | `0.000` | `0.122` | `0.000` | `0.000` |

`coupled_response` measures whether environmental and social response are active together in the crisis window. The designed controller can resolve crises through its scripted threshold path without maximizing that same overlap metric, which is why the designed row has `1.000` resolved rate but `0.000` coupled response.

The important gains over the return-selected GRU are:

```text
total score gain = 0.183
crisis score gain = 0.380
resolved-rate gain = 0.550
coupled-response gain = 0.619
gap to designed total score = 0.071
```

The verdict is:

```text
supports_joint_selection = true
supports_social_environment_dependency = true
verdict = pass
```

## Selection Boundary

The validation table shows that the no-coordinator baseline is rejected and that larger quotas are not automatically better:

| Env quota | Social quota | Strength | Tune total | Tune crisis | Tune resolved | Tune coupled | Selected |
|---:|---:|---:|---:|---:|---:|---:|---|
| `0.00` | `0.00` | `0.00` | `0.519` | `0.000` | `0.083` | `0.015` | no |
| `0.12` | `0.12` | `0.70` | `0.735` | `0.448` | `0.667` | `0.691` | no |
| `0.14` | `0.14` | `0.85` | `0.761` | `0.502` | `0.750` | `0.706` | yes |
| `0.16` | `0.14` | `1.00` | `0.753` | `0.485` | `0.750` | `0.671` | no |
| `0.14` | `0.16` | `1.00` | `0.731` | `0.440` | `0.667` | `0.671` | no |
| `0.18` | `0.16` | `1.10` | `0.721` | `0.418` | `0.667` | `0.660` | no |
| `0.16` | `0.18` | `1.10` | `0.717` | `0.411` | `0.667` | `0.651` | no |
| `0.20` | `0.18` | `1.20` | `0.698` | `0.371` | `0.667` | `0.638` | no |

That is the useful boundary: validation finds a balance point where both repair channels are kept alive instead of letting one dominate.

## Ablation Boundary

The selected controller fails in the predicted way when either crisis channel is removed:

| Ablation | Total loss | Crisis loss | Resolved loss | Env response loss | Social response loss | Coupled response loss |
|---|---:|---:|---:|---:|---:|---:|
| `social_culture` | `0.182` | `0.380` | `0.650` | `0.315` | `1.000` | `0.646` |
| `environment` | `0.182` | `0.380` | `0.650` | `0.646` | `0.000` | `0.646` |
| `body` | `0.038` | `0.079` | `0.050` | `0.108` | `0.000` | `0.108` |
| `tools` | `0.037` | `0.077` | `0.100` | `0.146` | `0.000` | `0.146` |
| `previous_action` | `0.026` | `0.053` | `0.000` | `0.119` | `0.000` | `0.119` |
| `infrastructure` | `0.098` | `0.032` | `0.000` | `0.010` | `0.000` | `0.010` |

The strong dependency claim is bounded but clean for this benchmark: removing the environmental channel removes environmental/coupled response and zeroes crisis score; removing the social/culture channel removes social/coupled response and also zeroes crisis score.

## Interpretation

This is the first clean positive after the Report 106-112 coupled-crisis failure line.

In plain English:

```text
The learned controller stopped treating coupled crises as one generic repair problem and started allocating different agents to environmental and social repair at the same time.
```

That matters because the earlier diagnostics failed in opposite ways:

- Report 107's repair critic was selected off;
- Report 108's value bias overfit validation and hurt held-out crises;
- Report 109 improved repair but failed clean environment dependency;
- Report 110 made environmental repair non-substitutable and the learned overlay still failed;
- Report 111's rollout labels were selected off;
- Report 112's diagnostic label was accurate offline but disrupted social repair online.

Report 113 does not solve open-ended agency. It shows that the next controller needed arbitration between repair channels, not just a stronger single-channel label.

## Connection To The Software-Controller Roadmap

The software-controller version should take the same lesson:

```text
A critic or diagnostic is not enough if using it collapses another required repair channel.
```

A coding controller cannot only say "this is the likely root cause." It also has to preserve test strategy, regression risk, API compatibility, review fit, and time cost. Report 113 is a small structured example of that pattern: repair improves only when the controller keeps multiple consequence channels active together.

## Next Step

The next benchmark should move beyond structured quota arbitration:

- train a decentralized multi-agent policy or actor-critic inside the coupled-crisis world;
- learn active crisis memory from consequences rather than fixed repair-window labels;
- evaluate on randomized maps, crisis mixes, and resource layouts;
- reduce reliance on explicit channel suppression while preserving causal ablation tests;
- generate counterfactual traces that show what happens when repair is delayed, overfocused, or misallocated;
- connect the learned crisis policy to the physics kernel and live viewer as a replay/live-snapshot source.

## Artifacts

- [script](../experiments/ssrm_3d_coupled_crisis_joint_arbitration_controller.py)
- [base training CSV](../artifacts/ssrm_3d_coupled_crisis_joint_arbitration_base_training.csv)
- [action training CSV](../artifacts/ssrm_3d_coupled_crisis_joint_arbitration_action_training.csv)
- [router selection CSV](../artifacts/ssrm_3d_coupled_crisis_joint_arbitration_router_selection.csv)
- [joint selection CSV](../artifacts/ssrm_3d_coupled_crisis_joint_arbitration_joint_selection.csv)
- [evaluation CSV](../artifacts/ssrm_3d_coupled_crisis_joint_arbitration_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_coupled_crisis_joint_arbitration_summary.csv)
- [ablation CSV](../artifacts/ssrm_3d_coupled_crisis_joint_arbitration_ablations.csv)
- [verdict CSV](../artifacts/ssrm_3d_coupled_crisis_joint_arbitration_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_coupled_crisis_joint_arbitration_trace.json)
- [results JSON](../artifacts/ssrm_3d_coupled_crisis_joint_arbitration_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_coupled_crisis_joint_arbitration_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_coupled_crisis_joint_arbitration_results.js)
