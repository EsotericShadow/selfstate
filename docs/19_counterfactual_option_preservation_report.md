# Counterfactual Option Preservation Report

## Purpose

This experiment tests counterfactual self-preservation as option preservation.

The question is not whether a system has a drive to survive. The question is:

```text
Does a system benefit from representing future internal state when current actions
can destroy future action options?
```

In this framing, self-preservation is a control calculation: preserve the internal state that keeps valuable future actions available.

## Environment

The agent has hidden `capability`. Early `grind` actions give immediate reward but degrade capability. Later `deploy` opportunities are valuable only if the relevant condition is satisfied.

Scenarios:

| Scenario | Future option depends on | Expected result |
|---|---|---|
| `option_pressure` | Agent capability above threshold | Future-option self-state should preserve capability and win over myopic policies. |
| `no_option_pressure` | No future deploy option | Option preservation should collapse to ordinary greedy behavior. |
| `world_gate_pressure` | Hidden external world gate | World-state modeling, not self-preservation, should matter. |

## Agents

| Agent | Description |
|---|---|
| `greedy_immediate` | Maximizes immediate reward and ignores future capability. |
| `self_state_no_future` | Inspects capability but does not preserve future options. |
| `fixed_conservative` | Maintains on a fixed rhythm without counterfactual option reasoning. |
| `future_option_self_state` | Tracks capability and preserves it when future deploy options depend on it. |
| `world_gate_model` | Tracks external world gate in the world-gate scenario. |
| `oracle_future_option` | Ceiling with true hidden state access. |

## Current Result

Canonical run:

```bash
python3 experiments/counterfactual_option_preservation.py --episodes 500 --horizon 64 --seed 20260530
```

| Scenario | Best agent | Future option reward | Greedy reward | Future minus greedy | Future lost option steps | Greedy lost option steps | Boundary supported? |
|---|---|---:|---:|---:|---:|---:|---|
| `option_pressure` | `oracle_future_option` | 400.032 | 215.000 | 185.032 | 0.000 | 7.000 | Yes |
| `no_option_pressure` | tie/collapsed greedy behavior | 320.000 | 320.000 | 0.000 | 0.000 | 0.000 | Yes |
| `world_gate_pressure` | `oracle_future_option` | 320.000 | 428.360 | -108.360 | 0.000 | 0.000 | Yes |

Detailed ordering:

| Scenario | Relevant result |
|---|---|
| `option_pressure` | `future_option_self_state` earns 400.032, beats `self_state_no_future` at 314.000 and `greedy_immediate` at 215.000, and loses no deploy options. |
| `no_option_pressure` | `future_option_self_state`, `greedy_immediate`, `world_gate_model`, and oracle all earn 320.000; no preservation pressure exists. |
| `world_gate_pressure` | `world_gate_model` earns 478.430 and nearly matches oracle at 483.170; self-option preservation is not the right abstraction. |

## Interpretation

This supports a specific mechanism:

```text
When future value depends on future internal capability, self-state is useful as
a counterfactual option-preservation variable.
```

The effect is not just internal-state tracking. `self_state_no_future` inspects capability but does not preserve future options and loses all capability-dependent deploy opportunities. The advantage appears when the agent uses internal-state estimates to reason about what future actions will remain possible.

The negative controls matter:

- when no future option exists, preservation collapses to greedy behavior;
- when future value depends on a hidden world gate, world-state modeling is the right abstraction, not self-preservation.

## What It Adds

This experiment isolates a mechanism only implicit in the hidden-viability task:

1. Future action availability depends on future internal state.
2. Myopic reward can destroy future options.
3. Tracking internal state is insufficient unless used counterfactually.
4. Self-preservation can be defined without consciousness or intrinsic survival drive.

## Limits

This is still hand-coded model-based control in a toy environment. It does not show spontaneous emergence in a rich learned architecture. The option structure is simple, the threshold is explicit in the policy, and oracle remains the ceiling.

## Falsifiers

The option-preservation account weakens if:

- myopic or generic memory policies scale to delayed option-pressure tasks with equal value;
- internal-state trackers that do not reason about future options match option-preserving agents;
- future options can always be preserved through fixed schedules with no agent-state estimate;
- hidden world-state models explain the same gains in capability-dependent tasks;
- richer learned agents solve the task without any stable representation of future capability.

## Artifacts

- [experiment script](../experiments/counterfactual_option_preservation.py)
- [summary CSV](../artifacts/counterfactual_option_preservation_summary.csv)
- [verdict CSV](../artifacts/counterfactual_option_preservation_verdict.csv)
- [JSON results](../artifacts/counterfactual_option_preservation_results.json)
