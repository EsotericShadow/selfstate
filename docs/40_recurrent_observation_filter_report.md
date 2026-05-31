# Recurrent Observation Filter Report

## Purpose

This experiment moves one step beyond learned cue-count tables.

The learner is a small recurrent controller. It processes noisy observation streams, is selected by training return, and is then tested by channel ablation.

The question is:

```text
Can a recurrent state become a reusable filter over hidden agent-state, and can
we distinguish that from recurrent filtering of world-state or irrelevant cues?
```

## Environment

Each episode has eight future control steps.

The recurrent controller receives nine noisy observations. Each observation has two binary channels:

- channel A: candidate agent-state evidence;
- channel B: candidate external-state evidence.

The controller updates a recurrent state over the observation stream and then chooses one action policy for the future control steps.

Scenarios:

| Scenario | Hidden structure | Expected result |
|---|---|---|
| `self_noisy_hidden` | Channel A tracks persistent hidden agent-state. | Recurrent controller wins and depends on channel A. |
| `world_noisy_hidden` | Channel B tracks persistent hidden external state. | Recurrent controller wins and depends on channel B. |
| `independent_hidden` | Future steps have independent hidden states. | Local probing wins. |
| `irrelevant_control` | Risky action always succeeds. | Greedy no-state wins. |

## Current Result

Canonical run:

```bash
python3 experiments/recurrent_observation_filter.py --episodes 500 --training-episodes 800 --seed 20260603 --horizon 8 --evidence-samples 9 --cue-accuracy 0.85 --random-candidates 500
```

Verdict:

| Scenario | Selected policy | Dependency signature | Recurrent reward | Local probe reward | Supported? |
|---|---|---|---:|---:|---|
| `self_noisy_hidden` | `recurrent_controller` | `agent_bounded_recurrent` | 132.632 | 126.400 | Yes |
| `world_noisy_hidden` | `recurrent_controller` | `external_recurrent` | 133.144 | 126.912 | Yes |
| `independent_hidden` | `task_local_probe` | `no_shared_recurrent_boundary` | 62.344 | 125.024 | Yes |
| `irrelevant_control` | `greedy_no_state` | `no_shared_recurrent_boundary` | 191.000 | 184.000 | Yes |

Channel-ablation result:

| Scenario | Channel A loss | Channel B loss | Interpretation |
|---|---:|---:|---|
| `self_noisy_hidden` | 90.368 | 0.000 | Recurrent control depends on agent-state evidence. |
| `world_noisy_hidden` | 0.000 | 88.064 | Recurrent control depends on external-state evidence. |
| `independent_hidden` | -0.336 | -0.336 | No useful shared recurrent dependency. |
| `irrelevant_control` | 0.000 | 0.000 | No hidden-state dependency needed. |

## Interpretation

The result supports a stronger partial-observability mechanism:

```text
A recurrent state can become self-equivalent when it filters noisy observations
about an agent-bounded hidden cause that controls future action.
```

The same recurrent machinery is not automatically selfhood. It is classified as world-state when the causally necessary channel is external, and it is rejected when local probing or no-state control is better.

## What It Adds

Compared with the learned observation-filter experiment, this test:

- removes explicit cue-count tables;
- uses recurrent state over a noisy observation stream;
- evaluates input-channel ablation to test causal dependency;
- keeps world, independent, and irrelevant controls in the same benchmark.

## Limits

This is still a toy recurrent precursor.

The observation channels are supplied. Candidate recurrent families include seeded accumulators, so the experiment does not yet show rich agents discovering the observation basis or representation from unstructured sensory input.

The next stronger version should train richer recurrent or model-based agents without seeded accumulator candidates and then test learned hidden states by causal intervention.

## Falsifiers

The recurrent-filter account weakens if:

- recurrent controllers depend on channel A in world or independent controls;
- recurrent controllers depend on channel B in self-hidden regimes;
- local probing beats recurrent filtering when one noisy persistent agent-state controls many future steps;
- recurrent states solve all scenarios with the same hidden dependency;
- richer recurrent agents solve the same regime without any stable agent-bounded dependency.

## Artifacts

- [experiment script](../experiments/recurrent_observation_filter.py)
- [summary CSV](../artifacts/recurrent_observation_filter_summary.csv)
- [training CSV](../artifacts/recurrent_observation_filter_training.csv)
- [dependency CSV](../artifacts/recurrent_observation_filter_dependency.csv)
- [verdict CSV](../artifacts/recurrent_observation_filter_verdict.csv)
- [JSON results](../artifacts/recurrent_observation_filter_results.json)
