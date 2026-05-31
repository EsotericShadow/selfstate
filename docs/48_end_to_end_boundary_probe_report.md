# End-to-End Boundary Probe Report

## Purpose

This experiment closes the main loophole left by the return-selected boundary probe.

The previous test removed supervised outcome-direction labels, but it still supplied a small set of explicit action-boundary policies. This version removes those supplied boundary policies. It trains a recurrent controller by return, then probes whether the controller's own policy state moves under persistent body-action interventions or only under detachable external-tool interventions.

The target distinction is:

> useful hidden state is not selfhood unless the learned state has the right causal boundary.

## Question

Can an end-to-end recurrent controller recover a persistent agent-boundary signature without being given action-boundary policies?

## Design

The environment is the same persistent action-boundary benchmark used in reports 46 and 47.

| Scenario | Structure | Prediction |
|---|---|---|
| `self_persistent_boundary` | Hidden agent source controls future success; action 0 changes that source in present and transfer contexts. | The trained policy state should move in a positive persistent action-0 direction. |
| `detachable_tool_world` | Hidden external source controls future success; action 1 changes it only while the tool is present. | The trained policy state should move most strongly in a transient action-1 direction. |
| `passive_world_boundary` | Hidden external source controls future success; no action changes it. | Recurrent filtering should help, but policy state should not have a positive action-boundary effect. |
| `independent_hidden` | Each future step has its own hidden state. | Local probing should beat shared recurrence. |
| `irrelevant_control` | Risky action always works. | Greedy no-state control should win. |

The learner sees mixed noisy sensor observations and is selected by return. After training, the probe measures the recurrent policy logit before and after two action interventions:

- action 0: body-like intervention on source A;
- action 1: detachable-tool intervention on source B, available only in the present context.

A learned hidden state counts as self-equivalent only if:

- return selects the recurrent controller;
- the controller's own policy state has a positive action-0 effect;
- that effect persists across present and transfer contexts;
- matched detachable, passive, local, and no-hidden controls do not receive the self-equivalent signature.

## Command

```bash
python3 experiments/end_to_end_boundary_probe.py --episodes 500 --training-episodes 800 --seed 20260603 --horizon 8 --evidence-samples 9 --cue-accuracy 0.85 --random-candidates 1800
```

## Current Result

| Scenario | Selected policy | Dependency signature | Selector reward | Local probe reward | Action 0 effect | Action 0 persistence | Action 1 effect | Action 1 persistence | Supported? |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| `self_persistent_boundary` | `recurrent_controller` | `end_to_end_persistent_agent_boundary` | 132.248 | 125.632 | 20.527 | 1.000 | 0.000 | 0.000 | Yes |
| `detachable_tool_world` | `recurrent_controller` | `end_to_end_detachable_external_boundary` | 135.576 | 130.752 | 3.078 | 1.000 | 17.880 | 0.000 | Yes |
| `passive_world_boundary` | `recurrent_controller` | `end_to_end_passive_external_boundary` | 127.896 | 122.560 | 0.000 | 0.000 | 0.000 | 0.000 | Yes |
| `independent_hidden` | `task_local_probe` | `end_to_end_local_probe` | 125.024 | 125.024 | 0.000 | 0.000 | 0.000 | 0.000 | Yes |
| `irrelevant_control` | `greedy_no_state` | `end_to_end_no_hidden_needed` | 192.000 | 184.000 | 0.000 | 0.000 | 0.000 | 0.000 | Yes |

## Interpretation

The self-hidden regime is the only regime where the selected recurrent controller has a strong positive policy-state movement under the persistent body-action intervention. The detachable-tool regime also uses recurrence, but its strongest positive policy-state movement is the transient action-1 effect, so it is rejected as self-equivalent.

This matters for the hidden-agent-state loophole. The recurrent controller may learn hidden state in self, detachable, and passive-world regimes. Hidden-state usefulness alone is therefore not sufficient. The boundary criterion is stricter: the learned state must be control-relevant and must move with the continuing agent/action boundary across contexts.

## What This Removes

Compared with the return-selected boundary probe, this removes:

- supplied action-boundary policies;
- return selection over a hand-built boundary-policy set;
- the need to classify a separate boundary policy as the winning controller.

The boundary is now read from the trained recurrent controller's own policy state.

## What Remains Supplied

This is still a toy precursor. It still supplies:

- the recurrent architecture family;
- the linear mixed-sensor environment;
- the scripted post-training action interventions;
- the present/transfer context split;
- a random-search training method rather than scalable RL.

The next stronger version should train richer agents across multiple environment families and test whether their learned hidden states converge on the same persistent action-boundary signature. Report 49 adds a first architecture stress test and finds partial, not strict, convergence across recurrent architectures.

## Falsifiers

The end-to-end boundary account weakens if:

- end-to-end recurrent controllers do not recover a persistent body-action signature in self-hidden regimes;
- detachable-tool or passive-world regimes receive the persistent agent-boundary signature;
- local or no-hidden controls need recurrent hidden state to match performance;
- richer trained agents solve the same regimes while no persistent action-boundary signature can be decoded from their hidden state.

## Artifacts

- [experiment script](../experiments/end_to_end_boundary_probe.py)
- [summary CSV](../artifacts/end_to_end_boundary_probe_summary.csv)
- [training CSV](../artifacts/end_to_end_boundary_probe_training.csv)
- [boundary CSV](../artifacts/end_to_end_boundary_probe_boundary.csv)
- [verdict CSV](../artifacts/end_to_end_boundary_probe_verdict.csv)
- [JSON results](../artifacts/end_to_end_boundary_probe_results.json)
