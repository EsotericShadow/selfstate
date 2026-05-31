# Active Boundary Discovery Report

## Purpose

This experiment closes the main loophole left by the learned sensor-subspace filter.

The previous test learned the destructive intervention direction in observed sensor space, but it still used supplied boundary interventions to classify the dependency as agent-bounded or external. This version learns a second sensor-space direction from the agent's own diagnostic action.

The question is:

```text
Can a system classify an outcome-predictive latent as self-equivalent because
that same latent is moved by its own action, rather than because an experimenter
supplies a boundary intervention label?
```

## Environment

The environment is the same mixed-sensor recurrent benchmark.

Each episode has eight future control steps. Two noisy latent sources are rotated into two mixed sensors:

```text
sensor_1 = 0.8 * source_A + 0.6 * source_B
sensor_2 = -0.6 * source_A + 0.8 * source_B
```

The recurrent controller observes only `sensor_1` and `sensor_2`.

The active-boundary test learns two directions:

- outcome direction: the mixed sensor direction that predicts future success;
- owned-action direction: the mixed sensor direction shifted by the agent's own diagnostic action.

No source labels, source ablations, or boundary intervention effects are used for classification. A dependency counts as agent-bounded only when the outcome direction is control-relevant and aligns with the owned-action direction.

Scenarios:

| Scenario | Hidden structure | Expected result |
|---|---|---|
| `self_mixed_hidden` | Source A tracks persistent hidden agent-state and is moved by owned diagnostic action. | Recurrent controller wins; outcome ablation damages control; outcome direction aligns with owned-action direction. |
| `world_mixed_hidden` | Source B tracks persistent hidden external state. | Recurrent controller wins; outcome ablation damages control; outcome direction does not align with owned-action direction. |
| `independent_hidden` | Future steps have independent hidden states. | Local probing wins and no active boundary is established. |
| `irrelevant_control` | Risky action always succeeds. | Greedy no-state wins and no active boundary is needed. |

## Current Result

Canonical run:

```bash
python3 experiments/active_boundary_discovery.py --episodes 500 --training-episodes 800 --seed 20260603 --horizon 8 --evidence-samples 9 --cue-accuracy 0.85 --random-candidates 1800
```

Verdict:

| Scenario | Selected policy | Dependency signature | Recurrent reward | Local probe reward | Outcome ablation loss | Owned-action alignment | Supported? |
|---|---|---|---:|---:|---:|---:|---|
| `self_mixed_hidden` | `recurrent_controller` | `agent_bounded_active_boundary` | 133.528 | 127.168 | 83.200 | 0.999 | Yes |
| `world_mixed_hidden` | `recurrent_controller` | `external_active_boundary` | 125.976 | 120.000 | 70.528 | 0.057 | Yes |
| `independent_hidden` | `task_local_probe` | `no_active_boundary` | 62.408 | 125.024 | 0.000 | 0.246 | Yes |
| `irrelevant_control` | `greedy_no_state` | `no_active_boundary` | 191.000 | 184.000 | 0.000 | 0.000 | Yes |

Learned active-boundary evidence:

| Scenario | Outcome direction | Owned-action direction | Alignment | Interpretation |
|---|---:|---:|---:|---|
| `self_mixed_hidden` | `(0.822, -0.569)` | `(0.800, -0.600)` | 0.999 | The outcome-predictive subspace is also owned-action-controllable. |
| `world_mixed_hidden` | `(0.645, 0.764)` | `(0.800, -0.600)` | 0.057 | The outcome-predictive subspace is useful but external. |
| `independent_hidden` | `(-0.778, -0.628)` | `(0.800, -0.600)` | 0.246 | Weak chance outcome direction is not control-relevant. |
| `irrelevant_control` | `(0.000, 0.000)` | `(0.800, -0.600)` | 0.000 | No outcome-predictive hidden dependency. |

## Interpretation

The result supports a stricter anti-tautology boundary:

```text
Hidden-state tracking becomes self-equivalent only when the tracked latent is
both control-relevant and tied to the agent's own action-conditioned boundary.
```

World-hidden structure remains useful. It wins the recurrent-control test and suffers a large outcome-direction ablation loss. It still does not count as self-equivalent because the outcome-predictive direction is not the direction moved by the agent's own action.

## What It Adds

Compared with the learned sensor-subspace filter, this test removes:

- supplied boundary intervention effects as the classification rule;
- source labels in the self/world classification step.

It keeps:

- a supplied owned diagnostic action;
- the same two-dimensional linear sensor mixture;
- the same small random-start recurrent controller family;
- outcome-supervised direction learning.

## Limits

This is still a toy precursor.

The owned diagnostic action is supplied by the environment design. The learned outcome direction is still supervised by observed success rates. The observation stream remains a linear two-source mixture, and the recurrent policy is selected by random search rather than trained by scalable RL.

The next stronger version should learn owned-action effects from richer action-observation histories and probe hidden states inside independently trained recurrent or model-based agents.

## Falsifiers

The active-boundary account weakens if:

- owned-action alignment appears equally in world, independent, or irrelevant controls;
- useful world-state dependencies are classified as self-equivalent merely because they improve reward;
- outcome-direction ablation damages independent or irrelevant controls;
- local probing or greedy no-state control matches active-boundary recurrent filtering in self-hidden regimes;
- richer agents cannot recover an action-conditioned boundary without explicit self/world labels.

## Artifacts

- [experiment script](../experiments/active_boundary_discovery.py)
- [summary CSV](../artifacts/active_boundary_discovery_summary.csv)
- [training CSV](../artifacts/active_boundary_discovery_training.csv)
- [boundary CSV](../artifacts/active_boundary_discovery_boundary.csv)
- [verdict CSV](../artifacts/active_boundary_discovery_verdict.csv)
- [JSON results](../artifacts/active_boundary_discovery_results.json)
