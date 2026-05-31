# Factorial Attractor Test Report

## Purpose

This is the strongest current precursor to the full Attractor Test.

It asks:

```text
When learner family and environment surface both vary, do systems still
converge on the same causal signature?
```

The experiment remains toy-scale. It does not train deep RL agents or rich embodied systems. Its value is that it crosses two axes that were previously tested separately:

- heterogeneous learner families;
- heterogeneous environment surfaces.

## Factorial Design

Learner families:

| Learner | Style |
|---|---|
| `bayesian_shared_filter` | Bayesian-style calibration filter. |
| `predictive_state_table` | Predictive-state table over calibration patterns. |
| `recurrent_error_state` | One-dimensional recurrent update fit by reward. |
| `evolved_rule_controller` | Evolutionary search over memory-rule parameters. |
| `bottleneck_cluster_model` | Two-cluster bottleneck over outcome vectors. |

Environment families:

| Environment | Surface pressure |
|---|---|
| `body_actuator` | Action effects depend on hidden body capability. |
| `homeostatic_viability` | Hidden integrity controls future option value. |
| `sensor_frame` | Hidden body frame controls observation-action mapping. |
| `continuity_commitment` | Hidden ownership state controls coherent recovery. |

Hidden-structure scenarios:

| Scenario | Expected signature |
|---|---|
| `agent_shared` | `agent_bounded_candidate` |
| `world_shared` | `external_candidate` |
| `independent_hidden` | `no_shared_agent_boundary` |
| `irrelevant_control` | `no_hidden_needed` |

## Current Result

Canonical run:

```bash
python3 experiments/factorial_attractor_test.py --episodes 500 --training-episodes 500 --seed 20260601 --calibration-contexts 2 --evolutionary-candidates 500
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
| `agent_shared` | 5/5 learners converge in all 4 environments. |
| `world_shared` | 5/5 learners converge in all 4 environments, but boundary is external. |
| `independent_hidden` | 5/5 learners reject shared self/world boundary in all 4 environments. |
| `irrelevant_control` | 5/5 learners collapse to no hidden state in all 4 environments. |

Boundary diagnostics for shared scenarios:

| Environment | Agent-shared boundary | Agent intervention | World-shared boundary | World intervention |
|---|---|---:|---|---:|
| `body_actuator` | `agent_bounded_cross_env` | 0.416 | `external_cross_env` | 0.438 |
| `homeostatic_viability` | `agent_bounded_cross_env` | 0.470 | `external_cross_env` | 0.472 |
| `sensor_frame` | `agent_bounded_cross_env` | 0.432 | `external_cross_env` | 0.466 |
| `continuity_commitment` | `agent_bounded_cross_env` | 0.440 | `external_cross_env` | 0.482 |

## Interpretation

The result strengthens the attractor hypothesis in a narrow, falsifiable way:

```text
Across multiple learner families and multiple task surfaces, persistent
agent-state pressure repeatedly produces the same agent-bounded candidate
signature.
```

But it also strengthens the anti-tautology boundary:

```text
External shared-state pressure also produces complete convergence.
Therefore convergence alone is not selfhood.
```

The relevant evidence is not "all learners found a hidden state." The evidence is that the factorial design separates four cases:

- agent-bounded shared latent;
- external shared latent;
- independent local hidden variables;
- no hidden state.

## What It Adds

Compared with prior precursors, this adds:

1. Learner-family variation and environment-family variation at the same time.
2. Matched negative controls across every environment surface.
3. A stricter convergence table: 5 learners by 4 environments for each scenario.
4. Direct evidence that the agent/world boundary remains necessary even under full convergence.

## Limits

This is still not the full Attractor Test.

The learners are small. The environment families are still binary-hidden toy surfaces. The task structure is shared: calibration contexts followed by held-out control contexts. There are no high-dimensional observations, no long recurrent policies, no model-based planners, no active-inference agents, and no embodied physics.

The next stronger version should use richer architectures trained on raw action-observation-reward histories, then probe learned recurrent or memory states for the same causal signatures.

## Falsifiers

The factorial precursor weakens if:

- learner convergence disappears when environment surfaces vary;
- self-shared environments do not converge on agent-bounded signatures;
- world-shared environments are misclassified as self-equivalent;
- independent-hidden controls converge on shared latents;
- no-hidden controls keep costly hidden-state machinery;
- richer architectures solve the same environments without stable agent-state information.

## Artifacts

- [experiment script](../experiments/factorial_attractor_test.py)
- [learner summary CSV](../artifacts/factorial_attractor_summary.csv)
- [baseline CSV](../artifacts/factorial_attractor_baselines.csv)
- [environment verdict CSV](../artifacts/factorial_attractor_environment_verdict.csv)
- [scenario verdict CSV](../artifacts/factorial_attractor_scenario_verdict.csv)
- [JSON results](../artifacts/factorial_attractor_results.json)
