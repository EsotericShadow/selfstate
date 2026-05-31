# Architecture Convergence Report

## Purpose

This experiment addresses a remaining gap in the research program:

```text
Do independent unlabeled learner families converge on self-equivalent state,
or are the existing results artifacts of hand-designed self variables?
```

The test is intentionally narrow. It uses the same linear action-effect family as the earlier experiments, but compares multiple predictor/controller families that receive only action/effect samples. They are not given labels such as self, world, body, actuator, gain, or wind.

This is the narrow precursor to the full Attractor Test. It tests convergence across simple learner families before expanding to wildly different architectures, learning methods, and environments.

## Learner Families

The canonical run compares:

- mean-delta memory;
- bias-only online learner;
- gain-only online learner;
- affine online predictive-state learner;
- least-squares predictive-state learner;
- symmetric-probe predictive-state learner;
- action-table memory;
- random-feature predictive-state learner.

After training, the analysis probes each learned prediction function for two causal components:

- action component: whether changing the learned action-effect slope is necessary for control;
- bias component: whether changing the learned world-bias term is necessary for control.

The action component is the self-equivalent candidate because it describes what the agent's own actions currently do.

## Current Result

Canonical run:

```bash
python3 experiments/architecture_convergence.py --episodes 500 --seed 20260530 --max-action 15 --calibration-steps 14 --control-steps 12
```

| Scenario | Top models | Top action-component count | Top bias-component count | Boundary supported? |
|---|---|---:|---:|---|
| `static_goal_switch` | affine SGD; bias SGD; gain SGD | 0 | 0 | Yes |
| `world_drift` | affine SGD; bias SGD; least squares | 0 | 3 | Yes |
| `self_drift` | least squares; symmetric probe; gain SGD | 3 | 0 | Yes |
| `mixed_hidden` | least squares; symmetric probe; affine SGD | 3 | 3 | Yes |

The strongest result is the contrast:

- Under pure world drift, top learners converge on bias/world components and do not require action-component changes.
- Under pure self drift, top learners converge on action-effect components and action-component ablation is damaging.
- Under mixed hidden drift, top learners require both components.
- Under static control, neither component is needed.

## Interpretation

This supports the conditional attractor claim in a limited setting:

```text
When the pressure is action-mediated agent-state drift, multiple unlabeled
predictor families converge on an action-effect component.
When the pressure is external drift, they converge on world-state components instead.
```

This is stronger than a single hand-coded self model, but still not a general proof. The environment is linear, the action-effect feature is easy to recover, and the model family still contains linear or nearly linear predictors.

## What It Adds

This experiment adds three pieces of evidence:

1. The self-equivalent component can be found by different learner families, not only one bespoke model.
2. The same analysis distinguishes world-state pressure from self-state pressure.
3. Causal ablation identifies whether the action-mediated component is behaviorally necessary.

## Remaining Falsifiers

The attractor claim remains vulnerable if:

- richer recurrent agents solve the same self-drift tasks without a stable action-effect latent;
- nonparametric memory scales better than compact action-state models as action spaces grow;
- nonlinear bodies require different abstractions that do not resemble a persistent self-state;
- multi-task agents do not reuse the same agent-state variable across action, viability, and continuity tasks;
- the component detected here is only a convenient linear statistic rather than an architecture-independent attractor.

## Artifacts

- [experiment script](../experiments/architecture_convergence.py)
- [summary CSV](../artifacts/architecture_convergence_summary.csv)
- [verdict CSV](../artifacts/architecture_convergence_verdict.csv)
- [JSON results](../artifacts/architecture_convergence_results.json)
