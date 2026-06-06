# SSRM-3D Coupled Crisis Diagnostic-Memory Report

## Question

Report 111 trained plan values from cloned simulator rollouts, but validation turned the overlay off. This report tests the narrower follow-up:

```text
Can a recurrent diagnostic-memory head learn which environmental repair action matters during coupled post-12h crises?
```

The point is not to add another hand-coded scenario shortcut. The diagnostic GRU receives ordinary observation features and previous-action context. It does not receive the active crisis profile label at runtime.

## What Changed

The benchmark keeps the Report 110/111 coupled-crisis world:

- no major crisis before the 12h development gate;
- post-gate crises require both environmental repair and social coordination;
- each crisis has one primary environmental repair class;
- wrong environmental actions add damage instead of repair credit;
- learned-controller inputs do not receive active crisis profile labels.

The new component is a recurrent diagnostic action head trained on crisis-window traces. Its training target is the primary environmental repair action for the active crisis, such as `sanitize`, `treat`, `scout`, or `construct`. Validation then decides whether the diagnostic head should bias the held-out controller at all.

The script also uses fair seed discipline for this report: the same numeric seed starts from the same world across controllers, ablations, and diagnostic-bias candidates. That keeps controller comparisons from being mixed with different random initial worlds.

## What This Does Not Claim

This is not actor-critic reinforcement learning, policy-gradient training, open-ended civilization, subjective consciousness, or a production software-engineering controller.

It is supervised recurrent diagnostic imitation wrapped around a return-selected GRU. The experiment is allowed to fail if the diagnostic label is learned offline but does not improve online action consequences.

## Canonical Command

```bash
python3 experiments/ssrm_3d_coupled_crisis_diagnostic_memory_controller.py --train-seeds 20260911,20260912,20260913,20260914,20260915,20260916 --tune-seeds 20261011,20261012,20261013 --eval-seeds 20261021,20261022,20261023,20261024,20261025 --hours 72 --step-hours 0.10 --population 14 --epochs 42 --hidden-size 64 --diagnostic-epochs 64 --diagnostic-hidden-size 64 --diagnostic-bias-candidates 0.00,0.75,1.25,1.75,2.50,3.50,5.00,8.00,12.00,20.00 --device auto --trace-seed 20261021
```

## Result

The diagnostic head trains well offline:

```text
diagnostic_accuracy = 0.991
diagnostic_crisis_accuracy = 0.991
diagnostic_env_accuracy = 0.991
diagnostic_train_examples = 30732
selected_router = social_first
selected_diagnostic_bias = 0.0
```

That is the key negative result. The model learns the supervised crisis-window label, but validation rejects using it online.

Held-out evaluation:

| Controller | Total score | Crisis score | Resolved rate | Env response | Social response | Coupled response |
|---|---:|---:|---:|---:|---:|---:|
| designed | `0.773` | `0.528` | `1.000` | `0.077` | `0.923` | `0.000` |
| diagnostic-memory GRU | `0.519` | `0.000` | `0.100` | `0.135` | `0.353` | `0.025` |
| return-selected GRU | `0.519` | `0.000` | `0.100` | `0.135` | `0.353` | `0.025` |
| base GRU | `0.518` | `0.000` | `0.000` | `0.000` | `0.312` | `0.000` |
| frame MLP | `0.330` | `0.000` | `0.000` | `0.250` | `0.000` | `0.000` |
| reactive | `0.240` | `0.000` | `0.000` | `0.125` | `0.000` | `0.000` |

With selected diagnostic bias `0.0`, the diagnostic-memory controller is behaviorally identical to the return-selected GRU. It adds no held-out gain.

## Selection Boundary

The validation table explains why:

| Diagnostic bias | Tune total | Tune resolved | Tune env response | Tune social response | Tune coupled response | Tune damage | Selected |
|---:|---:|---:|---:|---:|---:|---:|---|
| `0.00` | `0.517` | `0.083` | `0.186` | `0.354` | `0.033` | `1.353` | yes |
| `0.75` | `0.519` | `0.000` | `0.417` | `0.000` | `0.000` | `1.746` | no |
| `1.25` | `0.519` | `0.000` | `0.417` | `0.000` | `0.000` | `1.746` | no |
| `1.75` | `0.519` | `0.000` | `0.417` | `0.000` | `0.000` | `1.746` | no |
| `2.50` | `0.519` | `0.000` | `0.417` | `0.000` | `0.000` | `1.734` | no |
| `3.50` | `0.519` | `0.000` | `0.500` | `0.000` | `0.000` | `1.858` | no |
| `5.00` | `0.519` | `0.000` | `0.500` | `0.000` | `0.000` | `1.860` | no |
| `8.00` | `0.519` | `0.000` | `0.500` | `0.000` | `0.000` | `1.860` | no |
| `12.00` | `0.519` | `0.000` | `0.500` | `0.000` | `0.000` | `1.860` | no |
| `20.00` | `0.519` | `0.000` | `0.500` | `0.000` | `0.000` | `1.860` | no |

Nonzero diagnostic bias does what the narrow label asked for: it increases environmental response. But it wipes out social response, earns no crisis score, and raises damage. The validation objective correctly rejects it.

## Ablation Boundary

The selected controller still shows small social/environment dependency in the selected return-selected baseline:

| Ablation | Total loss | Crisis loss | Coupled response loss |
|---|---:|---:|---:|
| `social_culture` | `0.001` | `0.000` | `0.025` |
| `environment` | `0.001` | `0.000` | `0.021` |
| `body` | `0.002` | `0.000` | `0.018` |
| `tools` | `0.002` | `0.000` | `0.025` |
| `infrastructure` | `0.189` | `0.000` | `0.025` |
| `previous_action` | `-0.001` | `0.000` | `-0.006` |

This cannot rescue the diagnostic-memory claim because the diagnostic head itself was selected off.

The verdict is:

```text
supports_environment_response_gain = false
supports_diagnostic_memory_selection = false
supports_social_environment_dependency = true
verdict = partial_or_failed
```

## Interpretation

This is a completed negative bridge.

In plain English:

```text
The model can learn the diagnostic label, but that label is not enough to produce a better online crisis controller.
```

The failure is useful because it separates offline label accuracy from field usefulness. A diagnostic or critic does not count just because it predicts the right class in training. It has to change action in a way that improves held-out consequences.

For the longer software-controller roadmap, this is the same warning in miniature. A coding critic that predicts a plausible root cause is not enough. It must improve hidden-test pass rate, reduce regressions, lower review burden, and survive live repo outcomes.

## Next Step

The next coupled-crisis benchmark should stop using post-hoc logit overlays and train a repair policy directly from consequence:

- actor-critic or model-based return learning inside the coupled-crisis world;
- learned active-crisis belief state that can preserve both environmental and social repair demands;
- multi-head action arbitration where environmental repair cannot zero social coordination;
- counterfactual traces that include wrong-repair penalties and delayed damage;
- intervention tests that edit the learned crisis state and check whether action changes predictably;
- held-out crisis schedules, maps, and crisis mixes.

## Artifacts

- [script](../experiments/ssrm_3d_coupled_crisis_diagnostic_memory_controller.py)
- [base training CSV](../artifacts/ssrm_3d_coupled_crisis_diagnostic_memory_base_training.csv)
- [diagnostic training CSV](../artifacts/ssrm_3d_coupled_crisis_diagnostic_memory_diagnostic_training.csv)
- [router selection CSV](../artifacts/ssrm_3d_coupled_crisis_diagnostic_memory_router_selection.csv)
- [diagnostic selection CSV](../artifacts/ssrm_3d_coupled_crisis_diagnostic_memory_diagnostic_selection.csv)
- [evaluation CSV](../artifacts/ssrm_3d_coupled_crisis_diagnostic_memory_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_coupled_crisis_diagnostic_memory_summary.csv)
- [ablation CSV](../artifacts/ssrm_3d_coupled_crisis_diagnostic_memory_ablations.csv)
- [verdict CSV](../artifacts/ssrm_3d_coupled_crisis_diagnostic_memory_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_coupled_crisis_diagnostic_memory_trace.json)
- [results JSON](../artifacts/ssrm_3d_coupled_crisis_diagnostic_memory_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_coupled_crisis_diagnostic_memory_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_coupled_crisis_diagnostic_memory_results.js)
