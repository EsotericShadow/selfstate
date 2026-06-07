# SSRM-3D Learned Environment-Readiness Controller Report

## Question

Report 135 made the richer readiness world measurable with a designed policy.
This report asks whether a learned controller can take over that same 72h world.

The narrow question is:

```text
Can a recurrent neural controller trained from readiness traces preserve the
12h development gate, survive post-gate shocks, and maintain readiness over
72h without calling the designed policy?
```

## What Changed

This report adds:

- `experiments/ssrm_3d_learned_environment_readiness_controller.py`

The experiment imports the Report 135 world mechanics and adds only the learned
controller layer:

- frame MLP imitation controller;
- GRU imitation controller;
- closed-loop held-out evaluation;
- no scenario IDs;
- feature ablations for body, infrastructure, tools, social/culture,
  environment, readiness state, and previous action;
- CPU canonical run for deterministic evidence.

The controller observes physics/world-derived state variables from the
readiness world: body state, resources, shelter/architecture, tools, social and
culture state, weather/environment state, readiness channels, and previous
action. It does not receive a condition label.

## What This Does Not Claim

This is not deep reinforcement learning. It is not open-ended civilization. It
is not subjective consciousness. It is supervised imitation from a designed
controller, followed by closed-loop evaluation in the simulator.

The result is a failed learned-transfer boundary, not a solved controller.

## Canonical Command

```bash
python3 experiments/ssrm_3d_learned_environment_readiness_controller.py --train-seeds 20261211,20261212,20261213,20261214,20261215,20261216 --eval-seeds 20261221,20261222,20261223,20261224,20261225 --hours 72 --step-hours 0.10 --population 14 --epochs 52 --hidden-size 72 --device cpu --trace-seed 20261221
```

## Training Result

The learners fit the teacher traces poorly:

| Architecture | Train loss | Train accuracy | Parameters | Steps |
|---|---:|---:|---:|---:|
| `frame_mlp` | `1.941` | `0.252` | `12543` | `71936` |
| `gru` | `1.995` | `0.245` | `35439` | `71936` |

That low fit matters. The designed readiness policy is sequential, thresholded,
and partly stochastic. Straight imitation does not recover the long-horizon
action mix.

## Held-Out Result

The GRU preserves the 12h gate and beats the frame/reactive controllers in
score, but it fails the actual long-run target:

| Controller | Maturation | Final alive | Final readiness | Knowledge transfer | Structural strain |
|---|---:|---:|---:|---:|---:|
| `designed` | `1.000` | `18.4` | `1.000` | `1.000` | `0.011` |
| `gru` | `0.218` | `0.0` | `0.417` | `0.000` | `0.764` |
| `frame_mlp` | `0.185` | `0.0` | `0.299` | `0.016` | `0.536` |
| `reactive` | `0.071` | `0.0` | `0.004` | `0.000` | `1.000` |

The verdict is:

```text
supports_learned_readiness_control = false
supports_recurrent_advantage = true
supports_ablation_specificity = false
verdict = partial_or_failed
```

## Ablation Boundary

The GRU ablations do not provide clean causal support:

| Ablation | Score loss |
|---|---:|
| `body` | `-0.311` |
| `infrastructure` | `-0.002` |
| `tools` | `-0.001` |
| `social_culture` | `0.000` |
| `environment` | `0.001` |
| `readiness` | `0.000` |
| `previous_action` | `-0.218` |

Negative losses mean the ablated run scored higher than the unablated run. That
is not evidence that the removed channel is useful. It is evidence that the
learned policy is unstable and not truly using those channels for robust
long-horizon readiness control.

## Interpretation

This is a useful failure.

Report 135 showed that the designed readiness world can support 72h development,
post-gate shocks, births, tools, teaching, readiness accumulation, and
channel-specific ablations. Report 136 shows that a basic supervised GRU cannot
yet own that behavior.

The failure shape is specific:

- the 12h shock gate still holds;
- the GRU beats reactive and frame controllers by score;
- all learned-controller agents die by the end of the 72h run;
- knowledge transfer collapses to `0.000`;
- structural strain remains high;
- readiness never reaches the designed controller's level;
- feature ablations are unstable or inverted.

So the problem is no longer "the world is too visually simple." The immediate
research bottleneck is learned closed-loop control over delayed readiness
consequences.

## Next Step

The next aligned step is not another visual layer. It is a better learning
setup:

- curriculum train from 24h to 72h worlds;
- collect states from the learned controller's own failed rollouts;
- relabel or score those states with downstream survival/readiness outcomes;
- train value or sequence critics for readiness repair, teaching, and strain
  control;
- evaluate on held-out seeds with the same no-label feature boundary;
- keep failures as completed evidence instead of tuning them away.

## Artifacts

- [script](../experiments/ssrm_3d_learned_environment_readiness_controller.py)
- [training CSV](../artifacts/ssrm_3d_learned_environment_readiness_training.csv)
- [evaluation CSV](../artifacts/ssrm_3d_learned_environment_readiness_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_learned_environment_readiness_summary.csv)
- [ablation CSV](../artifacts/ssrm_3d_learned_environment_readiness_ablations.csv)
- [verdict CSV](../artifacts/ssrm_3d_learned_environment_readiness_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_learned_environment_readiness_trace.json)
- [results JSON](../artifacts/ssrm_3d_learned_environment_readiness_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_learned_environment_readiness_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_learned_environment_readiness_results.js)
