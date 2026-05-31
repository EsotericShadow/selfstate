# Unseeded Recurrent Filter Report

## Purpose

This experiment removes the largest shortcut in the recurrent observation-filter precursor.

The previous recurrent-filter test included seeded accumulator candidates. This version uses the same observation stream, scenarios, and channel-ablation tests, but candidate recurrent controllers are sampled randomly. No hand-seeded self-channel or world-channel accumulator is inserted into the candidate pool.

The question is:

```text
Can random-start recurrent search still discover the same self/world/local/no-hidden
boundary under noisy partial observability?
```

## Environment

Each episode has eight future control steps.

The controller receives nine noisy observations. Each observation has two binary channels:

- channel A: candidate agent-state evidence;
- channel B: candidate external-state evidence.

Random recurrent candidates are selected by training return, then evaluated on held-out episodes and channel ablations.

Scenarios:

| Scenario | Hidden structure | Expected result |
|---|---|---|
| `self_noisy_hidden` | Channel A tracks persistent hidden agent-state. | Random-start recurrent controller wins and depends on channel A. |
| `world_noisy_hidden` | Channel B tracks persistent hidden external state. | Random-start recurrent controller wins and depends on channel B. |
| `independent_hidden` | Future steps have independent hidden states. | Local probing wins. |
| `irrelevant_control` | Risky action always succeeds. | Greedy no-state wins. |

## Current Result

Canonical run:

```bash
python3 experiments/unseeded_recurrent_filter.py --episodes 500 --training-episodes 800 --seed 20260603 --horizon 8 --evidence-samples 9 --cue-accuracy 0.85 --random-candidates 1500
```

Verdict:

| Scenario | Selected policy | Dependency signature | Recurrent reward | Local probe reward | Supported? |
|---|---|---|---:|---:|---|
| `self_noisy_hidden` | `recurrent_controller` | `agent_bounded_recurrent` | 132.632 | 126.400 | Yes |
| `world_noisy_hidden` | `recurrent_controller` | `external_recurrent` | 133.144 | 126.912 | Yes |
| `independent_hidden` | `task_local_probe` | `no_shared_recurrent_boundary` | 63.096 | 125.024 | Yes |
| `irrelevant_control` | `greedy_no_state` | `no_shared_recurrent_boundary` | 191.000 | 184.000 | Yes |

Channel-ablation result:

| Scenario | Channel A loss | Channel B loss | Interpretation |
|---|---:|---:|---|
| `self_noisy_hidden` | 90.368 | 0.000 | Random-start recurrent control depends on agent-state evidence. |
| `world_noisy_hidden` | 0.000 | 77.440 | Random-start recurrent control depends on external-state evidence. |
| `independent_hidden` | 0.000 | 0.000 | No useful shared recurrent dependency. |
| `irrelevant_control` | 0.000 | 0.000 | No hidden-state dependency needed. |

## Interpretation

The result supports a stricter attractor precursor:

```text
The recurrent filter did not require a hand-seeded self accumulator. Random-start
candidate search found the useful recurrent dependency, and causal ablation
classified that dependency as agent-bounded only in the self-hidden regime.
```

This does not make every recurrent hidden state a self. The world-hidden control also learns a useful recurrent dependency, but channel ablation and intervention classify it as external.

## What It Adds

Compared with the recurrent observation-filter experiment, this test removes:

- seeded channel-A accumulator candidates;
- seeded channel-B accumulator candidates;
- seeded no-state risky/safe candidates inside the recurrent pool.

The selector still compares the best random recurrent controller against explicit local, greedy, and safe baselines.

## Limits

This is still a toy search experiment.

The observation channels and recurrent policy families are supplied. Random search is not the same as scalable gradient RL, and the `sum_rnn` architecture can represent channel accumulation directly.

The next stronger version should train richer recurrent or model-based agents by gradient methods from less structured observation streams, then test learned hidden states by causal intervention.

## Falsifiers

The unseeded recurrent account weakens if:

- random-start recurrent search fails to beat local probing when one noisy persistent agent-state controls future steps;
- random-start recurrent controllers depend on the same channel across self and world controls;
- channel ablation fails to separate agent-bounded from external recurrent dependencies;
- local probing or greedy no-state control matches recurrent filtering in agent-hidden regimes;
- richer recurrent agents solve the regime without stable agent-bounded hidden-state information.

## Artifacts

- [experiment script](../experiments/unseeded_recurrent_filter.py)
- [summary CSV](../artifacts/unseeded_recurrent_filter_summary.csv)
- [training CSV](../artifacts/unseeded_recurrent_filter_training.csv)
- [dependency CSV](../artifacts/unseeded_recurrent_filter_dependency.csv)
- [verdict CSV](../artifacts/unseeded_recurrent_filter_verdict.csv)
- [JSON results](../artifacts/unseeded_recurrent_filter_results.json)
