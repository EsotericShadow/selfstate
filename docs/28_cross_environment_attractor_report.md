# Cross-Environment Attractor Report

## Purpose

This experiment tests the environment-diversity side of the Attractor Test.

The question is:

```text
Does the same self/world/local/no-hidden boundary appear across different
task surfaces, or is the result an artifact of one environment design?
```

This is still a precursor. The environments are compact toy families. The improvement is that hidden-state pressure is tested across different surface forms rather than only one stream environment.

## Environment Families

| Environment | Surface pressure |
|---|---|
| `body_actuator` | Action effects depend on hidden body capability. |
| `homeostatic_viability` | Hidden integrity controls future option value. |
| `sensor_frame` | Hidden body frame controls observation-action mapping. |
| `continuity_commitment` | Hidden ownership state controls coherent recovery. |

Each family has two calibration contexts and four held-out control contexts.

## Scenarios

Each environment is tested under the same hidden-structure classes.

| Scenario | Hidden structure | Expected signature |
|---|---|---|
| `agent_shared` | One persistent agent-state controls all contexts. | `agent_bounded_candidate` |
| `world_shared` | One persistent external state controls all contexts. | `external_candidate` |
| `independent_hidden` | Each context has an independent hidden condition. | `no_shared_agent_boundary` |
| `irrelevant_control` | Risky action always works. | `no_hidden_needed` |

## Agents

| Agent | Role |
|---|---|
| `marginal_no_memory` | Uses only training marginal success. |
| `calibration_memory_no_transfer` | Pays to remember calibration outcomes but does not transfer them. |
| `shared_latent_filter` | Uses calibration outcomes as one shared latent. |
| `task_local_probe` | Pays a local probe cost in every held-out context. |
| `learned_environment_selector` | Selects shared latent, local hidden, or no hidden state from training statistics. |
| `oracle` | Ceiling with true hidden success in each context. |

## Current Result

Canonical run:

```bash
python3 experiments/cross_environment_attractor.py --episodes 500 --training-episodes 500 --seed 20260601 --calibration-contexts 2
```

Scenario-level result:

| Scenario | Expected signature | Supporting environments | Mean learned reward | Mean local-probe reward | Supported? |
|---|---|---:|---:|---:|---|
| `agent_shared` | `agent_bounded_candidate` | 4/4 | 42568.500 | 41068.500 | Yes |
| `world_shared` | `external_candidate` | 4/4 | 42035.250 | 40535.250 | Yes |
| `independent_hidden` | `no_shared_agent_boundary` | 4/4 | 41293.250 | 41293.250 | Yes |
| `irrelevant_control` | `no_hidden_needed` | 4/4 | 60250.000 | 58250.000 | Yes |

Boundary diagnostics for shared-state scenarios:

| Environment | Agent-shared boundary | Agent intervention | World-shared boundary | World intervention |
|---|---|---:|---|---:|
| `body_actuator` | `agent_bounded_cross_env` | 0.416 | `external_cross_env` | 0.438 |
| `homeostatic_viability` | `agent_bounded_cross_env` | 0.470 | `external_cross_env` | 0.472 |
| `sensor_frame` | `agent_bounded_cross_env` | 0.432 | `external_cross_env` | 0.466 |
| `continuity_commitment` | `agent_bounded_cross_env` | 0.440 | `external_cross_env` | 0.482 |

Environment-level signatures:

| Scenario | Environment signatures |
|---|---|
| `agent_shared` | all four environments select `agent_bounded_candidate`. |
| `world_shared` | all four environments select `external_candidate`. |
| `independent_hidden` | all four environments select `no_shared_agent_boundary`. |
| `irrelevant_control` | all four environments select `no_hidden_needed`. |

## Interpretation

The result supports a cross-environment precursor version of the attractor claim:

```text
When different task surfaces share the same hidden agent-state pressure,
the same agent-bounded causal signature recurs.
```

But the result also preserves the central warning:

```text
The same cross-environment recurrence appears for external world-state.
Convergence across environments is not selfhood unless the boundary is agent-bounded.
```

## What It Adds

Compared with the heterogeneous learner precursor, this experiment adds:

1. Multiple environment surfaces rather than one stream surface.
2. Matched positive and negative controls inside every environment.
3. Scenario-level aggregation across environments.
4. Direct evidence that the boundary test survives body, viability, frame, and continuity-style task surfaces.

## Limits

This remains a toy precursor.

The environment families differ semantically and in reward structure, but they still share a compact binary hidden-state design. The policies are still simple. The experiment does not train deep recurrent agents, model-based planners, active-inference agents, or transformer memory systems.

The next stronger test should vary architectures, learning methods, and environment families at the same time, then inspect learned recurrent or memory states for stable agent-bounded causal signatures.

## Falsifiers

The cross-environment precursor weakens if:

- any self-shared environment selects external, local, or no-hidden structure;
- any world-shared environment is counted as self-equivalent without boundary evidence;
- independent-hidden environments favor shared latents instead of local probes;
- no-hidden controls retain costly hidden-state machinery;
- richer environment surfaces remove the agent-bounded convergence pattern.

## Artifacts

- [experiment script](../experiments/cross_environment_attractor.py)
- [summary CSV](../artifacts/cross_environment_attractor_summary.csv)
- [environment verdict CSV](../artifacts/cross_environment_attractor_environment_verdict.csv)
- [scenario verdict CSV](../artifacts/cross_environment_attractor_scenario_verdict.csv)
- [JSON results](../artifacts/cross_environment_attractor_results.json)
