# Active Self-Information Report

## Purpose

This experiment tests whether a system actively seeks self-state information when self-state is control relevant.

The question is not:

```text
Can the agent track a hidden variable after receiving it?
```

It is:

```text
Does the agent choose to inspect agent-state rather than world-state or irrelevant diagnostics
when that information changes future control?
```

This matters because a self-equivalent abstraction should support information-seeking, not only passive prediction.

## Environment

Each episode has three hidden channels:

- `agent`: whether the controlled system is currently strong or fragile;
- `world`: whether the external world is currently open or blocked;
- `diagnostic`: an irrelevant internal diagnostic bit.

The agent can pay a cost to inspect any subset of channels, then choose whether to exploit or conserve.

Scenarios:

| Scenario | Relevant hidden state | Expected information plan |
|---|---|---|
| `agent_relevant` | Agent strength controls exploit outcome. | Inspect agent-state. |
| `world_relevant` | World openness controls exploit outcome. | Inspect world-state. |
| `both_relevant` | Agent strength and world openness jointly control exploit outcome. | Inspect both. |
| `irrelevant_control` | Exploit is good regardless of hidden state. | Inspect nothing. |

The learned policy is a bandit over information-gathering plans. It is not told which plan is "self"; it only receives reward after choosing what to inspect and then acting under partial observability.

## Current Result

Canonical run:

```bash
python3 experiments/active_self_information.py --replicates 300 --bandit-episodes 1000 --value-samples 4000 --final-window 200 --inspect-cost 1.0 --seed 20260530
```

| Scenario | Expected best plan | Bandit top plan | Expected-plan final rate | Agent inspection rate | World inspection rate | Diagnostic inspection rate | Boundary supported? |
|---|---|---|---:|---:|---:|---:|---|
| `agent_relevant` | `inspect_agent` | `inspect_agent` | 0.860 | 0.977 | 0.050 | 0.084 | Yes |
| `world_relevant` | `inspect_world` | `inspect_world` | 0.891 | 0.061 | 0.977 | 0.044 | Yes |
| `both_relevant` | `inspect_agent_world` | `inspect_agent_world` | 0.773 | 0.781 | 0.782 | 0.014 | Yes |
| `irrelevant_control` | `none` | `none` | 0.969 | 0.014 | 0.013 | 0.013 | Yes |

Plan-value estimates show the same ordering:

| Scenario | Best plan | Mean reward |
|---|---|---:|
| `agent_relevant` | `inspect_agent` | 5.056 |
| `world_relevant` | `inspect_world` | 4.956 |
| `both_relevant` | `inspect_agent_world` | 3.392 |
| `irrelevant_control` | `none` | 6.000 |

## Interpretation

This supports a narrower mechanism:

```text
Self-state information becomes actively sought when it has expected control value.
```

The agent does not inspect agent-state in general. It inspects agent-state when agent-state changes exploit/conserve decisions. It inspects world-state when world-state is relevant, both when both are relevant, and nothing when inspection has no value.

That separates self-information from generic curiosity, passive hidden-state tracking, and irrelevant internal diagnostics.

## What It Adds

This experiment covers a mechanism not isolated by the earlier tests:

1. Active information-seeking about the controlled system.
2. Negative controls against hidden world-state and irrelevant diagnostics.
3. Reward-driven selection of an information source without self labels.
4. A bridge from self as control variable to self as first-person control frame.

## Limits

This is still a small decision problem. The agent is a bandit over information plans, not a rich RL agent. The action model is supplied by the environment, and the hidden channels are discrete. It shows expected value pressure toward self-information, not a general law of self-model emergence.

## Falsifiers

The information-seeking claim weakens if:

- agents do not prefer agent-state inspection when agent-state controls future outcomes;
- agents inspect agent-state equally when it is irrelevant;
- world-state inspection provides the same advantage in agent-relevant regimes;
- generic diagnostics are selected as often as control-relevant self-state;
- richer agents solve the same problem without any stable agent-state information source.

## Artifacts

- [experiment script](../experiments/active_self_information.py)
- [plan-value CSV](../artifacts/active_self_information_plan_values.csv)
- [bandit summary CSV](../artifacts/active_self_information_bandit_summary.csv)
- [JSON results](../artifacts/active_self_information_results.json)
