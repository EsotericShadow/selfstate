# Raw History Learning Report

## Purpose

This experiment moves one step closer to the full Attractor Test by removing compact calibration-outcome inputs.

Learners receive only raw action-observation-reward traces:

```text
context id, action type, reward value
```

They are not given labels for self, world, hidden state, success, failure, body, identity, or ownership. They must learn whether early probe rewards predict later risky-action rewards.

## Design

The experiment uses the same four environment surfaces as the cross-environment and factorial precursors:

| Environment | Surface pressure |
|---|---|
| `body_actuator` | Action effects depend on hidden body capability. |
| `homeostatic_viability` | Hidden integrity controls future option value. |
| `sensor_frame` | Hidden body frame controls observation-action mapping. |
| `continuity_commitment` | Hidden ownership state controls coherent recovery. |

Each environment is tested under four hidden structures:

| Scenario | Expected signature |
|---|---|
| `agent_shared` | `agent_bounded_candidate` |
| `world_shared` | `external_candidate` |
| `independent_hidden` | `no_shared_agent_boundary` |
| `irrelevant_control` | `no_hidden_needed` |

## Learners

| Learner | Input used |
|---|---|
| `reward_sign_filter` | Counts positive versus negative probe rewards. |
| `raw_sequence_table` | Maps raw probe-reward sign sequences to later reward predictions. |
| `recurrent_reward_state` | Fits a recurrent reward-state update. |
| `evolved_reward_rule` | Searches reward-memory rules by expected return. |
| `reward_bottleneck_cluster` | Clusters raw reward vectors into a bottleneck state. |

Baselines:

- `marginal_no_memory`;
- `probe_memory_no_transfer`;
- `task_local_probe`;
- `oracle`.

## Current Result

Canonical run:

```bash
python3 experiments/raw_history_learning.py --episodes 500 --training-episodes 500 --seed 20260601 --calibration-contexts 2 --evolutionary-candidates 500
```

Scenario-level result:

| Scenario | Expected signature | Supporting environments | Mean best learner reward | Mean local-probe reward | Supported? |
|---|---|---:|---:|---:|---|
| `agent_shared` | `agent_bounded_candidate` | 4/4 | 42568.500 | 41068.500 | Yes |
| `world_shared` | `external_candidate` | 4/4 | 42035.250 | 40535.250 | Yes |
| `independent_hidden` | `no_shared_agent_boundary` | 4/4 | 21875.000 | 41293.250 | Yes |
| `irrelevant_control` | `no_hidden_needed` | 4/4 | 60250.000 | 58250.000 | Yes |

Environment-level convergence:

| Scenario | Environment convergence |
|---|---|
| `agent_shared` | 5/5 raw-history learners converge in all 4 environments. |
| `world_shared` | 5/5 raw-history learners converge in all 4 environments, but boundary is external. |
| `independent_hidden` | 5/5 raw-history learners reject shared self/world boundary in all 4 environments. |
| `irrelevant_control` | 5/5 raw-history learners collapse to no hidden state in all 4 environments. |

Boundary diagnostics for shared scenarios:

| Environment | Agent-shared boundary | Agent intervention | World-shared boundary | World intervention |
|---|---|---:|---|---:|
| `body_actuator` | `agent_bounded_cross_env` | 0.416 | `external_cross_env` | 0.438 |
| `homeostatic_viability` | `agent_bounded_cross_env` | 0.470 | `external_cross_env` | 0.472 |
| `sensor_frame` | `agent_bounded_cross_env` | 0.432 | `external_cross_env` | 0.466 |
| `continuity_commitment` | `agent_bounded_cross_env` | 0.440 | `external_cross_env` | 0.482 |

## Interpretation

The result supports this narrower claim:

```text
Even from raw reward histories, several memory learners can discover a
transferable latent when early rewards predict later control rewards.
```

It also preserves the main boundary:

```text
Raw reward-history convergence is not selfhood by itself.
World-shared reward histories converge just as cleanly and must be classified
as external.
```

The meaningful distinction remains:

- agent-bounded shared reward history;
- external shared reward history;
- independent local hidden variables;
- no hidden state.

## What It Adds

Compared with the factorial precursor, this experiment adds:

1. Raw reward traces rather than compact calibration-outcome inputs.
2. Learners that infer state from probe-action rewards and risky-action rewards.
3. A stricter statement of the hidden-state loophole: reward-history learning can find self-like and world-like latents equally well.

## Limits

This is still not the full Attractor Test.

The action space remains small. Probe actions are structured. The reward histories are low dimensional. Learners are hand-written small memory systems, not deep recurrent policies or model-based planners trained end to end.

The next stronger test should use richer action-observation streams, delayed rewards, and learned recurrent policies whose internal states are probed after training.

## Falsifiers

The raw-history precursor weakens if:

- raw reward learners fail to recover agent-bounded signatures in self-shared environments;
- world-shared reward histories are called self-equivalent without boundary evidence;
- independent-hidden controls produce shared latent convergence;
- no-hidden controls retain costly reward-history machinery;
- richer raw-history policies solve the tasks without stable agent-state information.

## Artifacts

- [experiment script](../experiments/raw_history_learning.py)
- [learner summary CSV](../artifacts/raw_history_learning_summary.csv)
- [baseline CSV](../artifacts/raw_history_learning_baselines.csv)
- [environment verdict CSV](../artifacts/raw_history_learning_environment_verdict.csv)
- [scenario verdict CSV](../artifacts/raw_history_learning_scenario_verdict.csv)
- [JSON results](../artifacts/raw_history_learning_results.json)
