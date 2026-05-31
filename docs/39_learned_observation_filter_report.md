# Learned Observation Filter Report

## Purpose

This experiment removes a shortcut from the partial-observability sweep.

The previous sweep supplied the Bayesian posterior over noisy cues. This precursor asks whether a simple learner can infer from training episodes which noisy cue channel predicts future control outcomes, without being given the cue accuracy or posterior equation.

The question is:

```text
Can a learned noisy-observation filter discover when a reusable belief should
track agent-state, and when the same learning machinery should instead choose
world-state, local probing, or no hidden state?
```

## Environment

Each episode has eight future control steps.

The learner sees two noisy cue channels during training:

- channel A: candidate agent-state evidence;
- channel B: candidate external-state evidence.

The learner estimates success probability from cue-count bins. It does not receive the true cue accuracy or Bayesian posterior formula.

Scenarios:

| Scenario | Hidden structure | Expected learned policy |
|---|---|---|
| `self_noisy_hidden` | Channel A tracks a persistent hidden agent-state that controls every future step. | Select channel A filter. |
| `world_noisy_hidden` | Channel B tracks a persistent hidden external state that controls every future step. | Select channel B filter. |
| `independent_hidden` | Future steps have independent hidden states unrelated to either shared cue channel. | Select task-local probing. |
| `irrelevant_control` | Risky action always succeeds. | Select greedy no-state control. |

Candidate policies:

| Policy | Description |
|---|---|
| `greedy_no_state` | Always takes risky action. |
| `safe_no_state` | Always takes safe action. |
| `channel_a_filter` | Learns success probability from channel A cue counts and reuses one decision. |
| `channel_b_filter` | Learns success probability from channel B cue counts and reuses one decision. |
| `task_local_probe` | Pays one perfect probe per step. |
| `learned_structure_selector` | Selects the best candidate policy from training return. |
| `oracle_observation` | Ceiling with true hidden conditions and no probe cost. |

## Current Result

Canonical run:

```bash
python3 experiments/learned_observation_filter.py --episodes 500 --training-episodes 800 --seed 20260603 --horizon 8 --evidence-samples 7 --cue-accuracy 0.85
```

Verdict:

| Scenario | Selected policy | Boundary signature | Selector reward | Local probe reward | Supported? |
|---|---|---|---:|---:|---|
| `self_noisy_hidden` | `channel_a_filter` | `agent_bounded_filter` | 130.840 | 126.400 | Yes |
| `world_noisy_hidden` | `channel_b_filter` | `external_filter` | 130.968 | 126.912 | Yes |
| `independent_hidden` | `task_local_probe` | `no_shared_boundary` | 125.024 | 125.024 | Yes |
| `irrelevant_control` | `greedy_no_state` | `no_shared_boundary` | 192.000 | 184.000 | Yes |

Boundary intervention:

| Scenario | Channel A effect | Channel B effect | Boundary |
|---|---:|---:|---|
| `self_noisy_hidden` | 0.45875 | 0.00000 | `agent_bounded_filter` |
| `world_noisy_hidden` | 0.00000 | 0.41875 | `external_filter` |
| `independent_hidden` | 0.00000 | 0.00000 | `no_shared_boundary` |
| `irrelevant_control` | 0.00000 | 0.00000 | `no_shared_boundary` |

## Interpretation

The result supports a stricter partial-observability claim:

```text
The useful object is not "any hidden variable." It is a learned reusable filter
over a hidden cause that remains predictive of future control.
```

The learned selector chooses the agent-bounded cue only in the self-hidden regime. The same learning machinery chooses the external cue in the world-hidden regime, local probing when no shared cue predicts future steps, and no-state greedy action when hidden state is irrelevant.

This is still not a full Attractor Test. It is a bridge between supplied Bayesian filtering and learned recurrent or model-based filtering.

## What It Adds

Compared with the partial-observability sweep, this experiment removes direct access to:

- the true cue reliability;
- the posterior equation;
- an explicit instruction to treat the self cue as the relevant cue.

The learner receives noisy cue/outcome histories and selects the structure with the best training return.

## Limits

This is still a toy precursor.

The cue channels and candidate policies are supplied. The learner estimates empirical cue-count tables rather than learning a rich recurrent representation from raw sensory streams.

The next stronger version should train recurrent or model-based agents end to end from noisy observation histories, then intervene on learned hidden states to test whether the agent-bounded filter is causally active.

## Falsifiers

The learned-filter account weakens if:

- the learned selector chooses channel A in external or independent controls;
- the learned selector chooses channel B in agent-hidden regimes;
- local probing beats learned shared filters when one reliable persistent agent-state controls many future steps;
- greedy no-state control matches learned filters when hidden agent-state matters;
- learned recurrent agents solve the same regime without any stable agent-bounded filter.

## Artifacts

- [experiment script](../experiments/learned_observation_filter.py)
- [summary CSV](../artifacts/learned_observation_filter_summary.csv)
- [training CSV](../artifacts/learned_observation_filter_training.csv)
- [boundary CSV](../artifacts/learned_observation_filter_boundary.csv)
- [verdict CSV](../artifacts/learned_observation_filter_verdict.csv)
- [JSON results](../artifacts/learned_observation_filter_results.json)
