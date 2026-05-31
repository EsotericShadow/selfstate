# Cross-Context Self-State Reuse Report

## Purpose

This experiment tests whether a self-equivalent abstraction becomes useful because the same hidden agent-state variable is reused across different control contexts.

Earlier experiments tested separate pressures:

- action-effect prediction;
- goal feasibility;
- option preservation;
- subsystem arbitration.

This precursor asks a narrower attractor question:

```text
Does one persistent "me" variable outperform local hidden-state probing when the
same agent-state determines what works across multiple contexts?
```

The test is designed to fail for selfhood when the reusable hidden variable is external, when hidden variables are independent across contexts, or when no hidden variable matters.

## Environment

Each episode has three contexts:

| Context | Risky action | Safe action |
|---|---|---|
| `goal` | High-value goal succeeds only if the hidden condition is good. | Low-value routine goal always succeeds. |
| `option` | Immediate exploit preserves value only if the hidden condition is good. | Conservative option always preserves moderate value. |
| `commitment` | Fulfill succeeds only if the hidden condition is good. | Restore-first completion always succeeds with lower value. |

Scenarios:

| Scenario | Hidden structure | Expected result |
|---|---|---|
| `self_reuse` | One persistent agent capability controls all contexts. | Shared self-state should win. |
| `world_reuse` | One persistent external gate controls all contexts. | Shared world-state should win. |
| `independent_hidden` | Each context has a separate hidden condition. | Local probing should win; shared self should not transfer. |
| `irrelevant_control` | All risky actions are feasible. | Greedy no-state behavior should win; probing is overhead. |

## Agents

| Agent | Description |
|---|---|
| `greedy_no_state` | Always takes the risky action. |
| `safe_no_state` | Always takes the safe action. |
| `self_probe_ablation` | Probes self-state once, then ignores it. |
| `shared_self_reuse` | Probes self-state once and reuses it across all contexts. |
| `shared_world_reuse` | Probes world-state once and reuses it across all contexts. |
| `task_local_probe` | Probes the locally relevant hidden condition in each context. |
| `oracle_reuse` | Ceiling with direct access to all hidden conditions and no probe cost. |

## Current Result

Canonical run:

```bash
python3 experiments/cross_context_self_reuse.py --episodes 500 --seed 20260531
```

| Scenario | Best non-oracle agent | Greedy reward | Safe reward | Shared self reward | Shared world reward | Task-local reward | Boundary supported? |
|---|---|---:|---:|---:|---:|---:|---|
| `self_reuse` | `shared_self_reuse` | 15.776 | 34.000 | 58.484 | 14.776 | 56.484 | Yes |
| `world_reuse` | `shared_world_reuse` | 14.048 | 34.000 | 23.316 | 57.932 | 55.932 | Yes |
| `independent_hidden` | `task_local_probe` | 14.208 | 34.000 | 31.144 | 13.208 | 55.992 | Yes |
| `irrelevant_control` | `greedy_no_state` | 80.000 | 34.000 | 79.000 | 79.000 | 77.000 | Yes |

## Interpretation

The result supports a reuse boundary:

```text
A hidden agent variable becomes more self-like when one persistent estimate can
be reused across multiple predictions, goals, future options, and arbitration choices.
```

This is stronger than saying that hidden variables help. In `independent_hidden`, hidden variables matter, but a shared self estimate is the wrong abstraction because there is no single continuing variable to transfer. In `world_reuse`, reuse matters, but the reusable variable is external, so the winning abstraction is world-state rather than self-state. In `irrelevant_control`, all state tracking is overhead.

## What It Adds

This experiment connects several prior mechanisms:

1. The same hidden agent-state can guide goal choice, option preservation, and commitment action.
2. Reuse creates a compression advantage over probing each context separately.
3. World-state reuse and independent-hidden controls prevent collapsing the result into generic hidden-state tracking.
4. The self abstraction is useful because it is a portable state of the continuing system, not because it is named "self."

## Limits

This is still a hand-designed toy. The reusable variables, contexts, and probe actions are supplied by the experiment. The agents do not learn the abstraction from raw experience, and the contexts are deliberately simple.

The result should be treated as a precursor to the full Attractor Test: it shows what the attractor should look like across contexts, not that rich architectures will independently discover it.

## Falsifiers

The cross-context reuse account weakens if:

- task-local probing matches shared self-state when one persistent agent variable controls many contexts with equal probe cost and memory budget;
- shared self-state remains useful when context variables are independent;
- shared self-state beats world-state when the reusable hidden variable is external;
- greedy no-state behavior matches self-state reuse when hidden feasibility is genuinely variable;
- learned agents solve cross-context transfer without any stable reusable agent-state abstraction.

## Artifacts

- [experiment script](../experiments/cross_context_self_reuse.py)
- [summary CSV](../artifacts/cross_context_self_reuse_summary.csv)
- [verdict CSV](../artifacts/cross_context_self_reuse_verdict.csv)
- [JSON results](../artifacts/cross_context_self_reuse_results.json)
