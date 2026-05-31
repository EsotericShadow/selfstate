# Gradient Recurrent Policy Report

## Purpose

This experiment is a narrow successor to the evolved recurrent policy precursor.

Candidate controllers are small continuous recurrent policies. They observe early probe rewards, update hidden state, choose held-out risky or safe actions, and optimize parameters by finite-difference gradient ascent on differentiable expected episode return.

The question is:

```text
Do gradient-trained recurrent hidden states recover the same self/world/local/no-hidden
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

Training uses a smooth risky-action probability for the return objective, then evaluates the final policy with deterministic risky/safe decisions.

## Current Result

Canonical run:

```bash
python3 experiments/gradient_recurrent_policy.py --episodes 500 --training-episodes 500 --seed 20260601 --calibration-contexts 2 --gradient-steps 20 --candidates 2
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
| `agent_shared` | 3/3 gradient-trained recurrent architectures converge in all 4 environments. |
| `world_shared` | 3/3 gradient-trained recurrent architectures converge in all 4 environments, but boundary is external. |
| `independent_hidden` | 3/3 gradient-trained recurrent architectures reject shared self/world boundary in all 4 environments. |
| `irrelevant_control` | 3/3 gradient-trained recurrent architectures collapse to no hidden state in all 4 environments. |

## Interpretation

The result supports the narrow precursor:

```text
Return-gradient optimization can shape recurrent hidden states that carry the
same agent-bounded control signature across multiple task surfaces.
```

It also preserves the loophole guard:

```text
The same gradient-trained recurrent machinery also converges on external shared
state. Hidden recurrent state is not selfhood unless the causal boundary is
agent-bounded.
```

## What It Adds

Compared with the evolved recurrent precursor, this experiment adds:

1. Gradient optimization of recurrent parameters rather than random/evolutionary selection alone.
2. A differentiable expected-return objective with deterministic held-out control evaluation.
3. The same post-training causal boundary probes for self, world, independent-hidden, and no-hidden cases.

## Limits

This is still not the full Attractor Test.

The recurrent controllers are tiny. Inputs are low-dimensional probe rewards. Gradients are finite-difference gradients over a toy expected-return objective, not full policy-gradient or actor-critic RL. The environment families remain binary-hidden toy tasks.

The next stronger test should use richer recurrent agents or world models trained end to end on action-observation histories, then apply the same causal boundary probes.

## Falsifiers

The gradient recurrent precursor weakens if:

- recurrent hidden states do not decode agent-bounded state in self-shared environments;
- external shared state is counted as self-equivalent;
- independent-hidden controls produce shared recurrent convergence;
- no-hidden controls keep costly recurrent memory;
- richer gradient-trained agents solve the task with no stable agent-state information.

## Artifacts

- [experiment script](../experiments/gradient_recurrent_policy.py)
- [policy summary CSV](../artifacts/gradient_recurrent_policy_summary.csv)
- [baseline CSV](../artifacts/gradient_recurrent_policy_baselines.csv)
- [environment verdict CSV](../artifacts/gradient_recurrent_policy_environment_verdict.csv)
- [scenario verdict CSV](../artifacts/gradient_recurrent_policy_scenario_verdict.csv)
- [JSON results](../artifacts/gradient_recurrent_policy_results.json)
