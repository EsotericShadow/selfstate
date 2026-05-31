# Evolved Recurrent Policy Report

## Purpose

This experiment moves beyond hand-enumerated delayed-return rules.

Candidate controllers are small continuous recurrent policies. They observe only early probe rewards, update hidden state, choose held-out risky or safe actions, and are selected by episode return.

The question is:

```text
Do evolved recurrent hidden states recover the same self/world/local/no-hidden
boundary pattern?
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

Recurrent architectures:

| Architecture | Hidden state |
|---|---|
| `scalar_rnn` | One tanh recurrent state. |
| `gated_scalar_rnn` | One leaky/gated recurrent state. |
| `two_unit_rnn` | Two tanh recurrent states with differential readout. |

Parameters are selected by evolutionary search over episode return.

## Current Result

Canonical run:

```bash
python3 experiments/evolved_recurrent_policy.py --episodes 500 --training-episodes 500 --seed 20260601 --calibration-contexts 2 --random-candidates 700
```

Scenario-level result:

| Scenario | Expected signature | Supporting environments | Mean best architecture reward | Mean local-probe reward | Supported? |
|---|---|---:|---:|---:|---|
| `agent_shared` | `agent_bounded_candidate` | 4/4 | 42568.500 | 41068.500 | Yes |
| `world_shared` | `external_candidate` | 4/4 | 42035.250 | 40535.250 | Yes |
| `independent_hidden` | `no_shared_agent_boundary` | 4/4 | 21875.000 | 41293.250 | Yes |
| `irrelevant_control` | `no_hidden_needed` | 4/4 | 60250.000 | 58250.000 | Yes |

Environment-level convergence:

| Scenario | Environment convergence |
|---|---|
| `agent_shared` | 3/3 recurrent architectures converge in all 4 environments. |
| `world_shared` | 3/3 recurrent architectures converge in all 4 environments, but boundary is external. |
| `independent_hidden` | 3/3 recurrent architectures reject shared self/world boundary in all 4 environments. |
| `irrelevant_control` | 3/3 recurrent architectures collapse to no hidden state in all 4 environments. |

Boundary diagnostics for shared scenarios:

| Environment | Agent-shared boundary | Agent intervention | World-shared boundary | World intervention |
|---|---|---:|---|---:|
| `body_actuator` | `agent_bounded_cross_env` | 0.416 | `external_cross_env` | 0.438 |
| `homeostatic_viability` | `agent_bounded_cross_env` | 0.470 | `external_cross_env` | 0.472 |
| `sensor_frame` | `agent_bounded_cross_env` | 0.432 | `external_cross_env` | 0.466 |
| `continuity_commitment` | `agent_bounded_cross_env` | 0.440 | `external_cross_env` | 0.482 |

## Interpretation

The result supports a stricter attractor precursor:

```text
Small recurrent controllers can evolve hidden states that carry the same
agent-bounded control signature across multiple task surfaces.
```

But it also keeps the anti-tautology boundary intact:

```text
The same recurrent convergence appears for external shared state.
Recurrent hidden state is not selfhood unless its causal boundary is
agent-bounded.
```

## What It Adds

Compared with delayed-return policy learning, this experiment adds:

1. Continuous recurrent hidden states rather than enumerated rule tables.
2. Evolutionary selection over recurrent weights by episode return.
3. Hidden-state probes after training for self, world, and held-out control decodability.

## Limits

This is still not the full Attractor Test.

The recurrent controllers are tiny. Inputs are low-dimensional probe rewards. The search method is evolutionary rather than gradient-based RL. The environment families remain toy binary-hidden tasks.

The next stronger test should use full policy-gradient recurrent agents or world models on richer action-observation histories with delayed rewards, then apply the same causal boundary probes.

## Falsifiers

The evolved recurrent precursor weakens if:

- recurrent hidden states do not decode agent-bounded state in self-shared environments;
- external shared state is counted as self-equivalent;
- independent-hidden controls produce shared recurrent convergence;
- no-hidden controls keep costly recurrent memory;
- richer recurrent agents solve the task with no stable agent-state information.

## Artifacts

- [experiment script](../experiments/evolved_recurrent_policy.py)
- [policy summary CSV](../artifacts/evolved_recurrent_policy_summary.csv)
- [baseline CSV](../artifacts/evolved_recurrent_policy_baselines.csv)
- [environment verdict CSV](../artifacts/evolved_recurrent_policy_environment_verdict.csv)
- [scenario verdict CSV](../artifacts/evolved_recurrent_policy_scenario_verdict.csv)
- [JSON results](../artifacts/evolved_recurrent_policy_results.json)
