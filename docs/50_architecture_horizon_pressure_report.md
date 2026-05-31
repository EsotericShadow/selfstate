# Architecture Horizon-Pressure Report

## Purpose

This experiment follows the architecture boundary stress test.

Report 49 showed that the end-to-end boundary signature is recoverable, but not strictly convergent across independently trained recurrent architectures. This sweep asks whether the missing convergence is fixed by increasing temporal horizon.

The answer is mixed:

> Longer horizons improve recoverability in shared regimes, but they do not produce strict architecture-wide convergence.

## Question

Does increasing the number of future steps controlled by the same hidden state make independently trained recurrent architectures converge on the same boundary abstraction?

## Design

The sweep uses the persistent action-boundary benchmark and trains each architecture independently:

- `sum_rnn`
- `scalar_rnn`
- `two_unit_rnn`

It varies horizon:

- 2
- 4
- 8
- 16

For each horizon, each architecture receives the same post-training end-to-end boundary probe used in reports 48 and 49.

## Command

```bash
python3 experiments/architecture_horizon_pressure_sweep.py --horizons 2,4,8,16 --episodes 250 --training-episodes 400 --seed 20260603 --evidence-samples 9 --cue-accuracy 0.85 --random-candidates 900
```

## Current Result

| Scenario | Convergence by horizon | Strict architecture convergence? | Result |
|---|---|---|---|
| `self_persistent_boundary` | 2:0/3; 4:1/3; 8:1/3; 16:1/3 | No | Horizon improves recoverability, not strict convergence. |
| `detachable_tool_world` | 2:0/3; 4:1/3; 8:1/3; 16:1/3 | No | Horizon improves recoverability, not strict convergence. |
| `passive_world_boundary` | 2:0/3; 4:1/3; 8:1/3; 16:2/3 | No | Horizon improves recoverability, not strict convergence. |
| `independent_hidden` | 2:3/3; 4:3/3; 8:3/3; 16:3/3 | Yes, for the local-probe control signature | Controls reject shared recurrence. |
| `irrelevant_control` | 2:3/3; 4:3/3; 8:3/3; 16:3/3 | Yes, for the no-hidden control signature | Controls reject hidden state. |

The `sum_rnn` recurrent-local reward gap increases with horizon in all shared regimes:

| Scenario | Horizon-2 gap | Horizon-16 gap | Delta |
|---|---:|---:|---:|
| `self_persistent_boundary` | 0.920 | 14.360 | 13.440 |
| `detachable_tool_world` | 0.920 | 14.360 | 13.440 |
| `passive_world_boundary` | 0.800 | 13.400 | 12.600 |

## Interpretation

This result supports one part of the mission prediction and limits another.

Supported:

- Temporal pressure matters. As more future steps depend on the same hidden source, the architecture that can exploit shared recurrent state gains a larger advantage.
- Controls remain clean. Independent-hidden tasks keep favoring local probing, and irrelevant-control tasks keep favoring no-state behavior.

Limited:

- Horizon pressure alone does not make every recurrent architecture rediscover the same boundary abstraction.
- The current toy stack still depends on architecture and training-search details.

The strongest current statement is therefore:

> Longer horizons increase the value of self-equivalent recurrent state where the architecture can exploit it, but they do not by themselves prove that selfhood is an architecture-independent attractor.

## Falsifiers And Strengtheners

The attractor claim strengthens if:

- higher horizons eventually produce strict convergence across independently trained architectures;
- controls continue rejecting persistent self-boundary signatures;
- the same horizon-pressure pattern survives richer architectures and training methods.

The attractor claim weakens if:

- horizon does not increase recurrent advantage in shared agent-state regimes;
- local or no-state policies match long-horizon shared hidden-state regimes;
- strict convergence appears equally in external, independent-hidden, or irrelevant controls.

Report 51 adds a capacity diagnostic. It shows that the weaker recurrent architectures can recover the boundary when source-direction seeds are supplied, so the current failure is better interpreted as a discovery/training-search gap than as an absolute architecture-capacity gap.

## Artifacts

- [experiment script](../experiments/architecture_horizon_pressure_sweep.py)
- [summary CSV](../artifacts/architecture_horizon_pressure_summary.csv)
- [verdict CSV](../artifacts/architecture_horizon_pressure_verdict.csv)
- [JSON results](../artifacts/architecture_horizon_pressure_results.json)
