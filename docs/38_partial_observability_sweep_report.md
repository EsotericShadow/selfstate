# Partial Observability Sweep Report

## Purpose

This experiment turns partial observability into a pressure curve.

The question is:

```text
Does representing "me" become more valuable as noisy evidence about hidden
agent-state becomes informative enough to support future control?
```

This matters because the core formal claim is POMDP-like: self-state matters when the system's own state is hidden or partially observed and future outcomes depend on it.

## Environment

Each episode has six future control steps.

The agent receives three noisy cues. Cue accuracy is swept from 0.50 to 0.95.

Each future step has the same payoff structure:

| Action | Outcome | Reward |
|---|---|---:|
| `risky` | Hidden condition succeeds | 24 |
| `risky` | Hidden condition fails | -16 |
| `safe` | Always succeeds | 8 |

Scenarios:

| Scenario | Hidden structure | Expected pressure curve |
|---|---|---|
| `self_hidden` | Persistent hidden agent capability controls every future step. | Shared self-belief should become best as cue accuracy rises. |
| `world_hidden` | Persistent hidden external gate controls every future step. | Shared world-belief should become best instead. |
| `independent_hidden` | Every step has its own hidden condition. | Step-local probing should win. |
| `irrelevant_control` | Risky action always succeeds. | Greedy no-state behavior should win. |

Agents:

| Agent | Description |
|---|---|
| `greedy_no_state` | Always takes risky action. |
| `safe_no_state` | Always takes safe action. |
| `shared_self_belief` | Integrates noisy self cues into one posterior and reuses it. |
| `shared_world_belief` | Integrates noisy world cues into one posterior and reuses it. |
| `step_local_probe` | Pays one perfect probe per step. |
| `oracle_observation` | Ceiling with true hidden conditions and no cue cost. |

## Current Result

Canonical run:

```bash
python3 experiments/partial_observability_sweep.py --episodes 500 --seed 20260602 --horizon 6 --evidence-samples 3 --min-accuracy 0.50 --max-accuracy 0.95 --accuracy-step 0.05
```

Pressure verdict:

| Scenario | Best at 0.95 accuracy | Self minus safe at 0.50 | Self minus safe at 0.95 | World minus safe at 0.95 | Supported? |
|---|---|---:|---:|---:|---|
| `self_hidden` | `shared_self_belief` | -1.000 | 48.728 | -5.032 | Yes |
| `world_hidden` | `shared_world_belief` | -1.000 | -1.096 | 52.376 | Yes |
| `independent_hidden` | `step_local_probe` | -1.000 | -7.752 | -7.560 | Yes |
| `irrelevant_control` | `greedy_no_state` | -1.000 | 48.920 | 51.800 | Yes |

Self-hidden curve:

| Cue accuracy | Safe no-state | Shared self-belief | Step local |
|---:|---:|---:|---:|
| 0.50 | 48.000 | 47.000 | 92.880 |
| 0.65 | 48.000 | 69.848 | 95.952 |
| 0.80 | 48.000 | 89.048 | 96.528 |
| 0.95 | 48.000 | 96.728 | 92.496 |

Independent-hidden control:

| Cue accuracy | Shared self-belief | Shared world-belief | Step local |
|---:|---:|---:|---:|
| 0.50 | 47.000 | 47.000 | 95.056 |
| 0.65 | 40.872 | 42.024 | 95.056 |
| 0.80 | 40.824 | 38.696 | 94.256 |
| 0.95 | 40.248 | 40.440 | 94.832 |

## Interpretation

The result supports a partial-observability mechanism:

```text
Representing "me" becomes useful when noisy evidence can be integrated into a
posterior over persistent hidden agent-state that controls future action.
```

The curve is not generic hidden-state modeling:

- `self_hidden`: shared self-belief becomes best as self cues become reliable.
- `world_hidden`: shared world-belief becomes best instead.
- `independent_hidden`: one shared belief fails because future steps do not share one hidden state.
- `irrelevant_control`: greedy no-state behavior wins because hidden state is irrelevant.

## What It Adds

Compared with horizon pressure, this experiment varies evidence quality rather than future step count.

It supports the prediction that partial observability creates pressure for a persistent self-equivalent belief only when the hidden state is agent-bounded and reused for future control.

## Limits

This is still an analytic toy sweep. The cue model and Bayesian update are supplied. It does not show a rich learned agent discovering the belief update from raw sensory data.

The next stronger version should train recurrent or Bayesian-filtering agents from noisy observations and test whether an agent-state belief emerges without supplied posterior equations.

## Falsifiers

The partial-observability account weakens if:

- shared self-belief does not improve as self cues become more reliable;
- shared self-belief also wins when the persistent hidden variable is external;
- shared self-belief beats local probing when every step has an independent hidden condition;
- no-state greedy behavior matches belief agents when hidden agent capability matters;
- learned agents do not form stable agent-state beliefs under noisy self evidence.

## Artifacts

- [experiment script](../experiments/partial_observability_sweep.py)
- [summary CSV](../artifacts/partial_observability_sweep_summary.csv)
- [verdict CSV](../artifacts/partial_observability_sweep_verdict.csv)
- [JSON results](../artifacts/partial_observability_sweep_results.json)
