# Reuse Pressure Sweep Report

## Purpose

This experiment turns the cross-context reuse result into a pressure curve.

The question is:

```text
Does the advantage of representing "me" increase as the same hidden agent-state
is reused across more contexts?
```

This matters because the attractor claim predicts a gradient, not merely a single win. If selfhood is a natural compression/control solution, its advantage should grow when one persistent agent variable explains more future choices.

## Environment

The sweep varies context count from 1 to 6.

Contexts are added in this order:

| Context | Risky success reward | Risky failure reward | Safe reward |
|---|---:|---:|---:|
| `goal` | 24 | -16 | 8 |
| `option` | 34 | -30 | 14 |
| `commitment` | 22 | -18 | 12 |
| `adaptation` | 28 | -22 | 11 |
| `prediction` | 18 | -14 | 7 |
| `arbitration` | 26 | -20 | 10 |

Scenarios:

| Scenario | Hidden structure | Expected pressure curve |
|---|---|---|
| `self_reuse` | One persistent agent capability controls every context. | Shared self-state advantage should grow with context count. |
| `world_reuse` | One persistent external gate controls every context. | Shared world-state advantage should grow instead. |
| `independent_hidden` | Every context has its own hidden condition. | Task-local probing should win; shared self should degrade. |
| `irrelevant_control` | All risky actions are feasible. | Greedy no-state behavior should win; probes are overhead. |

## Agents

| Agent | Description |
|---|---|
| `greedy_no_state` | Always takes risky action. |
| `safe_no_state` | Always takes safe action. |
| `shared_self_reuse` | Pays one self probe and reuses the result across all contexts. |
| `shared_world_reuse` | Pays one world probe and reuses the result across all contexts. |
| `task_local_probe` | Pays one probe per context and uses the local hidden condition. |
| `oracle_reuse` | Ceiling with true hidden conditions and no probe cost. |

## Current Result

Canonical run:

```bash
python3 experiments/reuse_pressure_sweep.py --episodes 500 --seed 20260531 --max-contexts 6
```

Pressure verdict:

| Scenario | Best at 6 contexts | Self minus local at 1 | Self minus local at 6 | World minus local at 6 | Boundary supported? |
|---|---|---:|---:|---:|---|
| `self_reuse` | `shared_self_reuse` | 0.000 | 5.000 | -75.080 | Yes |
| `world_reuse` | `shared_world_reuse` | -9.424 | -56.408 | 5.000 | Yes |
| `independent_hidden` | `task_local_probe` | 0.000 | -54.506 | -77.250 | Yes |
| `irrelevant_control` | `greedy_no_state` | 0.000 | 5.000 | 5.000 | Yes |

Self-reuse curve:

| Context count | Shared self | Task local | Self minus local |
|---:|---:|---:|---:|
| 1 | 15.992 | 15.992 | 0.000 |
| 2 | 40.584 | 39.584 | 1.000 |
| 3 | 58.944 | 56.944 | 2.000 |
| 4 | 77.894 | 74.894 | 3.000 |
| 5 | 93.920 | 89.920 | 4.000 |
| 6 | 111.400 | 106.400 | 5.000 |

World-reuse control:

| Context count | Shared world | Task local | World minus local |
|---:|---:|---:|---:|
| 1 | 15.448 | 15.448 | 0.000 |
| 2 | 40.728 | 39.728 | 1.000 |
| 3 | 57.748 | 55.748 | 2.000 |
| 4 | 79.658 | 76.658 | 3.000 |
| 5 | 89.776 | 85.776 | 4.000 |
| 6 | 114.100 | 109.100 | 5.000 |

Independent-hidden control:

| Context count | Shared self | Task local | Self minus local |
|---:|---:|---:|---:|
| 1 | 15.000 | 15.000 | 0.000 |
| 2 | 24.456 | 39.784 | -15.328 |
| 3 | 32.688 | 56.720 | -24.032 |
| 4 | 41.716 | 75.168 | -33.452 |
| 5 | 46.268 | 87.492 | -41.224 |
| 6 | 51.048 | 105.554 | -54.506 |

## Interpretation

The result supports a reuse-pressure mechanism:

```text
Representing "me" becomes more useful as one persistent agent-state variable
explains more future control contexts.
```

The pressure curve is not generic hidden-state modeling:

- `self_reuse`: shared self-state gains exactly as repeated local probes become redundant.
- `world_reuse`: the same curve appears for world-state when the reusable variable is external, so this is not selfhood.
- `independent_hidden`: shared self-state fails as contexts accumulate because there is no one variable to reuse.
- `irrelevant_control`: probes are unnecessary because risky action always works.

## What It Adds

This experiment adds a quantitative gradient to the boundary:

1. One context is not enough to distinguish shared self from local probing.
2. Reuse pressure creates the advantage: each additional context increases the value of one persistent agent-state estimate.
3. The same shape can belong to world-state, so agent boundary remains necessary.
4. If hidden variables do not persist across contexts, local probing beats self-state.

## Limits

The sweep is analytic and hand-designed. The probe costs make the reuse advantage visible by construction. It does not show that a learned agent discovers the abstraction, only that the computational pressure has the expected shape.

The next stronger version should train bottlenecked or recurrent agents with no named self/world probes and test whether the learned representation changes as the number of reusable agent-state contexts increases.

## Falsifiers

The reuse-pressure account weakens if:

- shared self-state advantage does not increase as reusable agent-state contexts increase;
- shared self-state also wins when the reusable variable is external;
- shared self-state beats local probing when hidden variables are independent;
- greedy no-state behavior matches shared self-state under variable hidden agent capability;
- learned agents do not show increasing agent-state decodability as context reuse increases.

## Artifacts

- [experiment script](../experiments/reuse_pressure_sweep.py)
- [summary CSV](../artifacts/reuse_pressure_sweep_summary.csv)
- [verdict CSV](../artifacts/reuse_pressure_sweep_verdict.csv)
- [JSON results](../artifacts/reuse_pressure_sweep_results.json)
