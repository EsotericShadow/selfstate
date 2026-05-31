# Mixed-Sensor Recurrent Filter Report

## Purpose

This experiment removes another shortcut from the recurrent filter stack.

The previous unseeded recurrent test still gave the controller one channel aligned with candidate agent-state evidence and one channel aligned with candidate world-state evidence. This version linearly mixes both latent sources into two sensor channels. The controller sees only mixed sensors.

The question is:

```text
Can random-start recurrent search recover an agent-bounded hidden cause from
mixed noisy sensors, and can source ablation distinguish self from world?
```

## Environment

Each episode has eight future control steps.

Each observation begins with two noisy latent sources:

- source A: candidate agent-state evidence;
- source B: candidate external-state evidence.

Those sources are rotated into two mixed sensors:

```text
sensor_1 = 0.8 * source_A + 0.6 * source_B
sensor_2 = -0.6 * source_A + 0.8 * source_B
```

The recurrent controller observes only `sensor_1` and `sensor_2`. Causal ablation is performed on the latent source before mixing, not on a named input channel.

Scenarios:

| Scenario | Hidden structure | Expected result |
|---|---|---|
| `self_mixed_hidden` | Source A tracks persistent hidden agent-state. | Recurrent controller wins and depends on source A. |
| `world_mixed_hidden` | Source B tracks persistent hidden external state. | Recurrent controller wins and depends on source B. |
| `independent_hidden` | Future steps have independent hidden states. | Local probing wins. |
| `irrelevant_control` | Risky action always succeeds. | Greedy no-state wins. |

## Current Result

Canonical run:

```bash
python3 experiments/mixed_sensor_recurrent_filter.py --episodes 500 --training-episodes 800 --seed 20260603 --horizon 8 --evidence-samples 9 --cue-accuracy 0.85 --random-candidates 1800
```

Verdict:

| Scenario | Selected policy | Dependency signature | Recurrent reward | Local probe reward | Supported? |
|---|---|---|---:|---:|---|
| `self_mixed_hidden` | `recurrent_controller` | `agent_bounded_mixed_recurrent` | 133.528 | 127.168 | Yes |
| `world_mixed_hidden` | `recurrent_controller` | `external_mixed_recurrent` | 125.976 | 120.000 | Yes |
| `independent_hidden` | `task_local_probe` | `no_shared_mixed_boundary` | 62.408 | 125.024 | Yes |
| `irrelevant_control` | `greedy_no_state` | `no_shared_mixed_boundary` | 191.000 | 184.000 | Yes |

Latent-source ablation:

| Scenario | Source A loss | Source B loss | Interpretation |
|---|---:|---:|---|
| `self_mixed_hidden` | 87.936 | 0.000 | Mixed recurrent control depends on agent-state evidence. |
| `world_mixed_hidden` | -0.256 | 70.528 | Mixed recurrent control depends on external-state evidence. |
| `independent_hidden` | -0.688 | -0.688 | No useful shared recurrent dependency. |
| `irrelevant_control` | 0.000 | 0.000 | No hidden-state dependency needed. |

## Interpretation

The result supports a stronger partial-observability precursor:

```text
The useful recurrent dependency does not require a sensor channel explicitly
named self. It can be recovered from mixed observations, then classified by
causal source ablation.
```

This still does not make mixed recurrent state selfhood by default. The world-hidden regime also produces a useful recurrent dependency, but source ablation classifies it as external.

## What It Adds

Compared with the unseeded recurrent filter, this test removes:

- direct self-aligned observation channel;
- direct world-aligned observation channel;
- input-channel ablation as the main causal test.

It replaces them with mixed sensors and latent-source ablation.

## Limits

This is still a toy precursor.

The mixing matrix, recurrent architecture class, reward structure, and source-ablation oracle are supplied. The recurrent search is random-start but not scalable gradient RL.

The next stronger version should train gradient recurrent or model-based agents from less structured observation streams and test learned hidden states through causal interventions that do not rely on known source variables.

## Falsifiers

The mixed-sensor account weakens if:

- random-start recurrent search cannot beat local probing when one mixed latent agent-state controls future steps;
- source ablation cannot separate agent-bounded from external recurrent dependencies;
- the same recurrent dependency solves self, world, independent, and irrelevant controls;
- local probing or greedy no-state control matches mixed recurrent filtering in agent-hidden regimes;
- richer agents require explicit self-labeled channels to solve the regime.

## Artifacts

- [experiment script](../experiments/mixed_sensor_recurrent_filter.py)
- [summary CSV](../artifacts/mixed_sensor_recurrent_filter_summary.csv)
- [training CSV](../artifacts/mixed_sensor_recurrent_filter_training.csv)
- [dependency CSV](../artifacts/mixed_sensor_recurrent_filter_dependency.csv)
- [verdict CSV](../artifacts/mixed_sensor_recurrent_filter_verdict.csv)
- [JSON results](../artifacts/mixed_sensor_recurrent_filter_results.json)
