# Return-Selected Boundary Probe Report

## Purpose

This experiment closes the main loophole left by the persistent action-boundary probe.

The previous test still learned an outcome-predictive direction from observed success rates, then compared it with persistent and transient action effects. This version removes that outcome-supervised direction. It learns generic action-effect directions from action-observation deltas, turns them into candidate policies, and lets training return select the useful boundary.

The question is:

```text
Can return selection recover the right boundary class without being given an
outcome-predictive direction label?
```

## Environment

The environment is the same persistent action-boundary benchmark.

Each episode has eight future control steps. Two noisy latent sources are rotated into two mixed sensors:

```text
sensor_1 = 0.8 * source_A + 0.6 * source_B
sensor_2 = -0.6 * source_A + 0.8 * source_B
```

The learner receives generic action-effect directions from present and transfer contexts. It builds candidate policies from those directions and compares them with recurrent filtering, local probing, greedy no-state control, and safe no-state control by training return.

The boundary evidence and the selected controller are tracked separately. A recurrent controller may be the highest-return controller while return-derived boundary evidence still shows that the useful action-effect policy is detachable external.

Scenarios:

| Scenario | Hidden structure | Expected result |
|---|---|---|
| `self_persistent_boundary` | Persistent agent-state source controls future success and action 0 has the same effect across contexts. | Return selection favors the persistent action-boundary policy. |
| `detachable_tool_world` | External source controls future success and action 1 changes it only while the tool is present. | Return-derived boundary evidence favors a transient action-boundary policy; recurrent control may still be best. |
| `passive_world_boundary` | External source controls future success but no action changes it. | Recurrent filtering wins; action-boundary policies do not beat local probing. |
| `independent_hidden` | Future steps have independent hidden states. | Local probing wins. |
| `irrelevant_control` | Risky action always succeeds. | Greedy no-state control wins. |

## Current Result

Canonical run:

```bash
python3 experiments/return_selected_boundary_probe.py --episodes 500 --training-episodes 800 --seed 20260603 --horizon 8 --evidence-samples 9 --cue-accuracy 0.85 --random-candidates 1800
```

Verdict:

| Scenario | Selected controller | Selected boundary | Dependency signature | Selector reward | Local probe reward | Supported? |
|---|---|---|---|---:|---:|---|
| `self_persistent_boundary` | `action_0_boundary_policy` | `action_0_boundary_policy` | `return_selected_persistent_agent_boundary` | 132.248 | 125.632 | Yes |
| `detachable_tool_world` | `recurrent_controller` | `action_1_boundary_policy` | `return_selected_detachable_external_boundary` | 135.576 | 130.752 | Yes |
| `passive_world_boundary` | `recurrent_controller` | `action_0_boundary_policy` | `return_selected_passive_external_boundary` | 127.896 | 122.560 | Yes |
| `independent_hidden` | `task_local_probe` | `action_0_boundary_policy` | `return_selected_local_probe` | 125.024 | 125.024 | Yes |
| `irrelevant_control` | `greedy_no_state` | `action_1_boundary_policy` | `return_selected_no_hidden_needed` | 192.000 | 184.000 | Yes |

Policy returns:

| Scenario | Action 0 reward | Action 1 reward | Recurrent reward | Local probe reward | Greedy reward |
|---|---:|---:|---:|---:|---:|
| `self_persistent_boundary` | 132.248 | 45.080 | 132.248 | 125.632 | 46.080 |
| `detachable_tool_world` | 56.984 | 136.088 | 135.576 | 130.752 | 58.880 |
| `passive_world_boundary` | 54.808 | 37.400 | 127.896 | 122.560 | 38.400 |
| `independent_hidden` | 53.832 | 43.560 | 62.408 | 125.024 | 44.560 |
| `irrelevant_control` | 134.936 | 191.000 | 191.000 | 184.000 | 192.000 |

## Interpretation

The result supports a stricter learning condition:

```text
The system does not need a supervised outcome-direction label to find the
candidate self boundary. Action-effect directions can be proposed from
observation deltas and selected or rejected by return.
```

The detachable-tool case is still rejected as self-equivalent. The best boundary policy is transient action 1, but the best controller is recurrent; either way, the boundary is external because the useful action effect does not persist across contexts.

## What It Adds

Compared with the persistent action-boundary probe, this test removes:

- outcome-supervised direction extraction;
- direct comparison between a precomputed outcome direction and action-effect directions.

It keeps:

- scripted action-effect histories;
- the same two-dimensional linear sensor mixture;
- the same small random-start recurrent controller family;
- return selection over a small supplied policy set.

## Limits

This is still a toy precursor.

The action-effect histories are generated by simple scripted actions, the candidate policy family is small, and the transfer context is hand designed. The recurrent policy is selected by random search rather than trained by scalable RL.

The next stronger version should train policies end to end and then probe whether persistent action-boundary structure is recoverable from their hidden states. Report 48 implements a first toy version of that step for small recurrent controllers.

## Falsifiers

The return-selected boundary account weakens if:

- return selection favors persistent action-boundary policies in detachable-tool, passive-world, independent, or irrelevant controls;
- return selection cannot favor persistent action-boundary policies in self-hidden regimes;
- recurrent policies solve self-hidden regimes while all action-boundary policies fail and no persistent boundary can be decoded;
- richer agents cannot recover persistent action-boundary structure without supervised outcome-direction labels.

## Artifacts

- [experiment script](../experiments/return_selected_boundary_probe.py)
- [summary CSV](../artifacts/return_selected_boundary_probe_summary.csv)
- [training CSV](../artifacts/return_selected_boundary_probe_training.csv)
- [verdict CSV](../artifacts/return_selected_boundary_probe_verdict.csv)
- [JSON results](../artifacts/return_selected_boundary_probe_results.json)
