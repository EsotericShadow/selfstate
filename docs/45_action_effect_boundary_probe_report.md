# Action-Effect Boundary Probe Report

## Purpose

This experiment closes the main loophole left by active boundary discovery.

The previous test showed that a useful latent can be classified as self-equivalent when its outcome-predictive direction aligns with an owned-action direction. But controllable external state can also be moved by the agent's actions. A tool, switch, or object can be action-controllable without being part of the self.

The question is:

```text
Can the system reject controllable external state as self-equivalent even when
that external state is useful and action-controllable?
```

## Environment

The environment is the same mixed-sensor recurrent benchmark, with one added control.

Each episode has eight future control steps. Two noisy latent sources are rotated into two mixed sensors:

```text
sensor_1 = 0.8 * source_A + 0.6 * source_B
sensor_2 = -0.6 * source_A + 0.8 * source_B
```

The probe learns three directions:

- outcome direction: the mixed sensor direction that predicts future success;
- body/action-effect direction: the mixed sensor direction shifted by body calibration;
- tool-action direction: the mixed sensor direction shifted by a controllable external action when such an action is available.

Self-equivalent state requires outcome relevance plus body/action-effect alignment. A controllable external variable can align with the tool-action direction and still fail the self boundary.

Scenarios:

| Scenario | Hidden structure | Expected result |
|---|---|---|
| `self_mixed_hidden` | Source A tracks persistent hidden agent-state and body/action-effect calibration. | Recurrent controller wins; outcome ablation damages control; outcome direction aligns with body/action-effect direction. |
| `controllable_world_hidden` | Source B tracks persistent external state and can be changed by a tool action. | Recurrent controller wins; outcome ablation damages control; outcome direction aligns with tool action but not body/action-effect direction. |
| `world_mixed_hidden` | Source B tracks persistent external state but is not action-controllable. | Recurrent controller wins; outcome ablation damages control; no action-effect boundary alignment. |
| `independent_hidden` | Future steps have independent hidden states. | Local probing wins and no action-effect boundary is established. |
| `irrelevant_control` | Risky action always succeeds. | Greedy no-state wins and no action-effect boundary is needed. |

## Current Result

Canonical run:

```bash
python3 experiments/action_effect_boundary_probe.py --episodes 500 --training-episodes 800 --seed 20260603 --horizon 8 --evidence-samples 9 --cue-accuracy 0.85 --random-candidates 1800
```

Verdict:

| Scenario | Selected policy | Dependency signature | Recurrent reward | Local probe reward | Outcome ablation loss | Body alignment | Tool alignment | Supported? |
|---|---|---|---:|---:|---:|---:|---:|---|
| `self_mixed_hidden` | `recurrent_controller` | `agent_bounded_action_effect_boundary` | 133.528 | 127.168 | 83.200 | 0.999 | 0.000 | Yes |
| `controllable_world_hidden` | `recurrent_controller` | `controllable_external_action_boundary` | 134.552 | 129.216 | 75.264 | 0.030 | 1.000 | Yes |
| `world_mixed_hidden` | `recurrent_controller` | `passive_external_action_boundary` | 125.976 | 120.000 | 70.528 | 0.057 | 0.000 | Yes |
| `independent_hidden` | `task_local_probe` | `no_action_effect_boundary` | 62.408 | 125.024 | 0.000 | 0.246 | 0.000 | Yes |
| `irrelevant_control` | `greedy_no_state` | `no_action_effect_boundary` | 191.000 | 184.000 | 0.000 | 0.000 | 0.000 | Yes |

## Interpretation

The result supports a stricter boundary:

```text
Self-equivalent state is not merely hidden, useful, persistent, or
action-controllable. It must be tied to the agent's own action-effect boundary.
```

The `controllable_world_hidden` case is the key negative control. It has:

- high control value;
- high outcome-direction ablation loss;
- near-perfect tool-action alignment;
- low body/action-effect alignment.

That means action controllability alone is not sufficient for selfhood.

## What It Adds

Compared with active boundary discovery, this test adds:

- a controllable external hidden variable;
- a distinction between body/action-effect alignment and generic action controllability;
- a direct negative control for tool-like or switch-like external state.

It keeps:

- supplied body and tool diagnostic actions;
- the same two-dimensional linear sensor mixture;
- the same small random-start recurrent controller family;
- outcome-supervised direction learning.

## Limits

This is still a toy precursor.

The body/action-effect calibration and tool action are supplied by the environment design. The learned outcome direction is supervised by observed success rates. The observation stream remains a linear two-source mixture, and the recurrent policy is selected by random search rather than trained by scalable RL.

The next stronger version should learn body/action-effect and tool-action boundaries from richer action-observation histories without predeclared diagnostic actions.

## Falsifiers

The action-effect boundary account weakens if:

- controllable external state is classified as self-equivalent merely because it is action-controllable;
- body/action-effect alignment appears equally in world, controllable-world, independent, or irrelevant controls;
- outcome-direction ablation damages independent or irrelevant controls;
- local probing or greedy no-state control matches action-effect recurrent filtering in self-hidden regimes;
- richer agents cannot separate body/action-effect state from controllable external state without explicit self/world labels.

## Artifacts

- [experiment script](../experiments/action_effect_boundary_probe.py)
- [summary CSV](../artifacts/action_effect_boundary_probe_summary.csv)
- [training CSV](../artifacts/action_effect_boundary_probe_training.csv)
- [boundary CSV](../artifacts/action_effect_boundary_probe_boundary.csv)
- [verdict CSV](../artifacts/action_effect_boundary_probe_verdict.csv)
- [JSON results](../artifacts/action_effect_boundary_probe_results.json)
