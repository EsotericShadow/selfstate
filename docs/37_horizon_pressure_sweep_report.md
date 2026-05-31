# Horizon Pressure Sweep Report

## Purpose

This experiment turns the horizon prediction into a pressure curve.

The question is:

```text
Does representing "me" become more valuable as more future time steps depend
on the same hidden agent-state?
```

This matters because the attractor claim predicts that self-state value should increase with long horizons, not merely appear in one-step tasks.

## Environment

The sweep varies future horizon from 1 to 12 repeated control steps.

Each step has the same payoff structure:

| Action | Outcome | Reward |
|---|---|---:|
| `risky` | Hidden condition succeeds | 24 |
| `risky` | Hidden condition fails | -16 |
| `safe` | Always succeeds | 8 |

Scenarios:

| Scenario | Hidden structure | Expected pressure curve |
|---|---|---|
| `self_persistent` | One persistent agent capability controls every future step. | Shared self-state advantage should grow with horizon. |
| `world_persistent` | One persistent external gate controls every future step. | Shared world-state advantage should grow instead. |
| `independent_steps` | Every step has its own hidden condition. | Step-local probing should win; shared self-state should degrade. |
| `irrelevant_control` | Risky action always succeeds. | Greedy no-state behavior should win; probes are overhead. |

Agents:

| Agent | Description |
|---|---|
| `greedy_no_state` | Always takes risky action. |
| `safe_no_state` | Always takes safe action. |
| `shared_self_state` | Pays one self probe and reuses it across all future steps. |
| `shared_world_state` | Pays one world probe and reuses it across all future steps. |
| `step_local_probe` | Pays one probe per step and uses the local condition. |
| `oracle_horizon` | Ceiling with true hidden conditions and no probe cost. |

## Current Result

Canonical run:

```bash
python3 experiments/horizon_pressure_sweep.py --episodes 500 --seed 20260602 --max-horizon 12
```

Pressure verdict:

| Scenario | Best at 12 steps | Self minus local at 1 | Self minus local at 12 | World minus local at 12 | Supported? |
|---|---|---:|---:|---:|---|
| `self_persistent` | `shared_self_state` | 0.000 | 11.000 | -111.112 | Yes |
| `world_persistent` | `shared_world_state` | -10.208 | -111.304 | 11.000 | Yes |
| `independent_steps` | `step_local_probe` | 0.000 | -98.040 | -105.080 | Yes |
| `irrelevant_control` | `greedy_no_state` | 0.000 | 11.000 | 11.000 | Yes |

Self-persistent curve:

| Horizon | Shared self | Step local | Self minus local |
|---:|---:|---:|---:|
| 1 | 15.864 | 15.864 | 0.000 |
| 2 | 32.920 | 31.920 | 1.000 |
| 4 | 66.840 | 63.840 | 3.000 |
| 8 | 133.656 | 126.656 | 7.000 |
| 12 | 202.904 | 191.904 | 11.000 |

Independent-step control:

| Horizon | Shared self | Step local | Self minus local |
|---:|---:|---:|---:|
| 1 | 15.960 | 15.960 | 0.000 |
| 2 | 22.536 | 31.088 | -8.552 |
| 4 | 38.152 | 62.912 | -24.760 |
| 8 | 61.704 | 124.928 | -63.224 |
| 12 | 92.104 | 190.144 | -98.040 |

## Interpretation

The result supports a horizon-pressure mechanism:

```text
Representing "me" becomes more useful as more future actions depend on the
same persistent hidden agent-state.
```

The curve is not generic hidden-state modeling:

- `self_persistent`: one self-state probe becomes better than repeated local probes as horizon grows.
- `world_persistent`: the same curve appears for external world-state, so the boundary still matters.
- `independent_steps`: shared self-state fails as horizon grows because there is no one variable to reuse.
- `irrelevant_control`: no-state greedy action wins because hidden state is irrelevant.

## What It Adds

Compared with the reuse-pressure sweep, this experiment varies time rather than context count.

It supports the prediction that self-modeling pressure should increase with long horizons, but only when the same agent-bounded state persists across those future steps.

## Limits

This is still an analytic toy sweep. The probe costs and repeated payoff structure make the curve visible by design. It does not yet show a rich learned agent increasing self-state decodability as horizon increases.

The next stronger version should train recurrent or model-based learners across horizon lengths and test whether agent-state latents become more stable, more decodable, and more causally necessary as horizon grows.

## Falsifiers

The horizon-pressure account weakens if:

- shared self-state advantage does not increase with horizon under persistent agent-state;
- shared self-state also wins when the persistent variable is external;
- shared self-state beats local probing when each step has an independent hidden condition;
- no-state greedy behavior matches shared self-state when hidden agent capability matters;
- learned agents do not show increasing agent-state decodability or ablation loss as horizon grows.

## Artifacts

- [experiment script](../experiments/horizon_pressure_sweep.py)
- [summary CSV](../artifacts/horizon_pressure_sweep_summary.csv)
- [verdict CSV](../artifacts/horizon_pressure_sweep_verdict.csv)
- [JSON results](../artifacts/horizon_pressure_sweep_results.json)
