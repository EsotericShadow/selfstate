# Goal Formation Under Capability Report

## Purpose

This experiment tests whether self-state changes which goals should be formed.

The question is not:

```text
Can the agent execute a fixed goal?
```

It is:

```text
Which goal should this system choose, given what it can actually do?
```

That makes self-state a feasibility filter for goal formation.

## Environment

Each episode offers four possible goals:

| Goal | Reward | Hidden requirement |
|---|---:|---|
| `routine` | 8 | None |
| `heavy` | 18 | Strength and open world gate |
| `delicate` | 18 | Precision and open world gate |
| `flagship` | 34 | Strength, precision, and open world gate |

Failure earns `-14`. Inspecting self-state or world-state costs `0.75`.

Scenarios:

| Scenario | Hidden pressure | Expected result |
|---|---|---|
| `capability_relevant` | Strength/precision vary; world gates are open. | Self-capability goal selection should win. |
| `world_relevant` | Capabilities are good; world gates vary. | World-opportunity selection should win. |
| `mixed_relevant` | Capabilities and world gates vary. | Self+world goal selection should win. |
| `irrelevant_control` | Capabilities and gates are all good. | Greedy payoff selection should win; self inspection is wasteful. |

## Agents

| Agent | Description |
|---|---|
| `payoff_greedy` | Chooses the highest listed reward. |
| `fixed_safe_goal` | Always chooses routine. |
| `self_state_ablation` | Inspects self-state but ignores it. |
| `self_capability_selector` | Uses strength/precision to choose the best feasible goal. |
| `world_opportunity_selector` | Uses world gates to choose the best open goal. |
| `self_world_goal_selector` | Uses both capability and world gates. |
| `oracle_goal_selector` | Ceiling with true hidden state and no inspection cost. |

## Current Result

Canonical run:

```bash
python3 experiments/goal_formation_under_capability.py --episodes 500 --seed 20260530
```

| Scenario | Best non-oracle agent | Greedy reward | Self-selector reward | World-selector reward | Self+world reward | Boundary supported? |
|---|---|---:|---:|---:|---:|---|
| `capability_relevant` | `self_capability_selector` | 1.648 | 20.786 | 0.898 | 20.036 | Yes |
| `world_relevant` | `world_opportunity_selector` | 7.408 | 6.658 | 24.046 | 23.296 | Yes |
| `mixed_relevant` | `self_world_goal_selector` | -6.896 | 8.150 | 2.042 | 15.628 | Yes |
| `irrelevant_control` | `payoff_greedy` | 34.000 | 33.250 | 33.250 | 32.500 | Yes |

Detailed interpretation:

- In `capability_relevant`, greedy forms the attractive but often impossible `flagship` goal; self-capability selection forms feasible goals and wins.
- In `world_relevant`, self-state does not help because capability is already adequate; world opportunity is the relevant hidden variable.
- In `mixed_relevant`, neither self-only nor world-only is enough; the best non-oracle policy uses both.
- In `irrelevant_control`, self inspection is pure overhead; greedy payoff selection is enough.

## Interpretation

This supports a goal-formation mechanism:

```text
Representing "me" becomes useful when desirable goals must be filtered through
what this system can actually do.
```

The result separates self-state from generic goal desirability. A goal is not just valuable in the world; it is valuable-for-this-agent when the agent has the capability to make it real.

## What It Adds

This experiment covers a gap left by the earlier stack:

1. Self-state affects which goals are worth choosing, not only how actions are controlled.
2. Goal formation can fail by selecting impossible high-value goals.
3. Capability-state inspection is useful only when capability determines feasibility.
4. World-state and mixed controls prevent misclassifying all hidden feasibility tracking as selfhood.

## Limits

This is a one-step goal-choice toy. Capabilities and world gates are discrete, and the goal set is hand-designed. It does not show spontaneous goal formation in a rich learned agent. It shows the computational pressure: self-state can become a goal-feasibility filter.

## Falsifiers

The goal-formation account weakens if:

- payoff-only goal selection scales to hidden capability regimes with equal value;
- world-only selectors match self-capability selectors when capability is the true feasibility condition;
- self-capability inspection remains useful when all goals are already feasible;
- learned agents choose feasible goals without any stable capability or agent-state abstraction;
- mixed hidden regimes can be solved without integrating agent-state and world-state.

## Artifacts

- [experiment script](../experiments/goal_formation_under_capability.py)
- [summary CSV](../artifacts/goal_formation_under_capability_summary.csv)
- [verdict CSV](../artifacts/goal_formation_under_capability_verdict.csv)
- [JSON results](../artifacts/goal_formation_under_capability_results.json)
