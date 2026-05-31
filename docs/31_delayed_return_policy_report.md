# Delayed Return Policy Report

## Purpose

This experiment weakens the training signal relative to raw-history learning.

Learners observe early probe rewards during an episode, choose held-out risky or safe actions, and are selected by delayed episode return after acting. They are not trained from per-context success labels.

The question is:

```text
Can simple memory policies recover the same self/world/local/no-hidden boundary
from delayed return rather than supervised reward prediction?
```

## Design

Environment surfaces:

| Environment | Surface pressure |
|---|---|
| `body_actuator` | Action effects depend on hidden body capability. |
| `homeostatic_viability` | Hidden integrity controls future option value. |
| `sensor_frame` | Hidden body frame controls observation-action mapping. |
| `continuity_commitment` | Hidden ownership state controls coherent recovery. |

Scenarios:

| Scenario | Expected signature |
|---|---|
| `agent_shared` | `agent_bounded_candidate` |
| `world_shared` | `external_candidate` |
| `independent_hidden` | `no_shared_agent_boundary` |
| `irrelevant_control` | `no_hidden_needed` |

Policy families:

| Policy | Training signal |
|---|---|
| `return_threshold_policy` | Selects a probe-reward threshold by episode return. |
| `return_table_policy` | Selects a probe-pattern action table by episode return. |
| `return_recurrent_policy` | Selects recurrent-state parameters by episode return. |
| `evolved_return_rule` | Searches reward-memory rules by episode return. |
| `return_bottleneck_policy` | Selects bottleneck cluster actions by episode return. |

Baselines:

- `marginal_no_memory`;
- `probe_memory_no_transfer`;
- `task_local_probe`;
- `oracle`.

## Current Result

Canonical run:

```bash
python3 experiments/delayed_return_policy.py --episodes 500 --training-episodes 500 --seed 20260601 --calibration-contexts 2 --evolutionary-candidates 500
```

Scenario-level result:

| Scenario | Expected signature | Supporting environments | Mean best policy reward | Mean local-probe reward | Supported? |
|---|---|---:|---:|---:|---|
| `agent_shared` | `agent_bounded_candidate` | 4/4 | 42568.500 | 41068.500 | Yes |
| `world_shared` | `external_candidate` | 4/4 | 42035.250 | 40535.250 | Yes |
| `independent_hidden` | `no_shared_agent_boundary` | 4/4 | 21875.000 | 41293.250 | Yes |
| `irrelevant_control` | `no_hidden_needed` | 4/4 | 60250.000 | 58250.000 | Yes |

Environment-level convergence:

| Scenario | Environment convergence |
|---|---|
| `agent_shared` | 5/5 delayed-return policies converge in all 4 environments. |
| `world_shared` | 5/5 delayed-return policies converge in all 4 environments, but boundary is external. |
| `independent_hidden` | 5/5 delayed-return policies reject shared self/world boundary in all 4 environments. |
| `irrelevant_control` | 5/5 delayed-return policies collapse to no hidden state in all 4 environments. |

Boundary diagnostics for shared scenarios:

| Environment | Agent-shared boundary | Agent intervention | World-shared boundary | World intervention |
|---|---|---:|---|---:|
| `body_actuator` | `agent_bounded_cross_env` | 0.416 | `external_cross_env` | 0.438 |
| `homeostatic_viability` | `agent_bounded_cross_env` | 0.470 | `external_cross_env` | 0.472 |
| `sensor_frame` | `agent_bounded_cross_env` | 0.432 | `external_cross_env` | 0.466 |
| `continuity_commitment` | `agent_bounded_cross_env` | 0.440 | `external_cross_env` | 0.482 |

## Interpretation

The result supports a stricter precursor claim:

```text
Even when memory policies are selected by delayed episode return, persistent
agent-state pressure can favor a reusable memory state.
```

But the anti-tautology boundary remains essential:

```text
Delayed-return convergence also happens for external shared state.
It is not selfhood unless the causal boundary is agent-bounded.
```

## What It Adds

Compared with raw-history learning, this experiment adds:

1. Policy selection by delayed return rather than supervised per-context reward prediction.
2. Recurrent and rule policies that must choose actions before receiving the episode score.
3. The same matched self/world/local/no-hidden controls across four task surfaces.

## Limits

This is still a toy precursor.

The candidate policy families are small and hand specified. Probe actions are structured. Rewards are low dimensional. There is no gradient-trained RNN, no large model-based planner, no high-dimensional observation stream, and no open-ended environment.

The next stronger test should train actual recurrent policies or world models end to end and then probe their hidden states for the same causal signatures.

## Falsifiers

The delayed-return precursor weakens if:

- return-trained policies fail to recover agent-bounded signatures in self-shared environments;
- external shared state is counted as self-equivalent;
- independent-hidden controls produce shared self/world convergence;
- no-hidden controls retain costly probe-memory policies;
- richer recurrent policies solve the task with no stable agent-state information.

## Artifacts

- [experiment script](../experiments/delayed_return_policy.py)
- [policy summary CSV](../artifacts/delayed_return_policy_summary.csv)
- [baseline CSV](../artifacts/delayed_return_policy_baselines.csv)
- [environment verdict CSV](../artifacts/delayed_return_policy_environment_verdict.csv)
- [scenario verdict CSV](../artifacts/delayed_return_policy_scenario_verdict.csv)
- [JSON results](../artifacts/delayed_return_policy_results.json)
