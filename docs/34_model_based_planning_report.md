# Model-Based Planning Report

## Purpose

This experiment moves away from direct policy selection.

Small planners first learn a reward model from early probe histories, then choose held-out risky or safe actions by comparing predicted risky value against safe value.

The question is:

```text
Do model-based planners learn the same self/world/local/no-hidden boundary
pattern when action choice is mediated by a learned reward model?
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

Planner families:

| Planner | Learned model |
|---|---|
| `bayesian_table_planner` | Tabular reward model keyed by probe history. |
| `linear_belief_planner` | Logistic reward model over summed probe evidence. |
| `recurrent_belief_planner` | Tiny recurrent reward model over probe rewards. |

Each planner is evaluated after training by causal boundary probes and held-out control reward.

## Current Result

Canonical run:

```bash
python3 experiments/model_based_planning.py --episodes 500 --training-episodes 500 --seed 20260601 --calibration-contexts 2 --recurrent-candidates 200
```

Scenario-level result:

| Scenario | Expected signature | Supporting environments | Mean best planner reward | Mean local-probe reward | Supported? |
|---|---|---:|---:|---:|---|
| `agent_shared` | `agent_bounded_candidate` | 4/4 | 42568.500 | 41068.500 | Yes |
| `world_shared` | `external_candidate` | 4/4 | 42035.250 | 40535.250 | Yes |
| `independent_hidden` | `no_shared_agent_boundary` | 4/4 | 21875.000 | 41293.250 | Yes |
| `irrelevant_control` | `no_hidden_needed` | 4/4 | 60250.000 | 58250.000 | Yes |

Environment-level convergence:

| Scenario | Environment convergence |
|---|---|
| `agent_shared` | 3/3 model-based planners converge in all 4 environments. |
| `world_shared` | 3/3 model-based planners converge in all 4 environments, but boundary is external. |
| `independent_hidden` | 3/3 model-based planners reject shared self/world boundary in all 4 environments. |
| `irrelevant_control` | 3/3 model-based planners collapse to no hidden state in all 4 environments. |

## Interpretation

The result supports a stronger planning-mediated precursor:

```text
Reward-model learners can form a reusable latent from probe history and use it
for planning held-out action across several task surfaces.
```

It also keeps the same anti-tautology boundary:

```text
The model-based planners learn reusable external state just as cleanly as
agent-state. Model-based planning is not selfhood unless the useful latent is
agent-bounded.
```

## What It Adds

Compared with direct policy-selection precursors, this experiment adds:

1. A learned reward model before action choice.
2. Explicit planning by expected risky value versus safe value.
3. Three model families that reach the same causal verdict from different predictive forms.

## Limits

This is still not the full Attractor Test.

The reward models are tiny. Probe histories are low-dimensional. The planners do not learn rich transition dynamics, high-dimensional observations, or open-ended goals. The environments remain binary-hidden toy tasks.

The next stronger test should use richer world models or model-based RL agents trained end to end on action-observation histories, then apply the same causal boundary probes.

## Falsifiers

The model-based planning precursor weakens if:

- reward models do not learn agent-bounded latents in self-shared environments;
- reusable external state is counted as self-equivalent;
- independent-hidden controls produce shared planner convergence;
- no-hidden controls keep costly probe-state models;
- richer model-based agents solve the task with no stable agent-state information.

## Artifacts

- [experiment script](../experiments/model_based_planning.py)
- [planner summary CSV](../artifacts/model_based_planning_summary.csv)
- [baseline CSV](../artifacts/model_based_planning_baselines.csv)
- [environment verdict CSV](../artifacts/model_based_planning_environment_verdict.csv)
- [scenario verdict CSV](../artifacts/model_based_planning_scenario_verdict.csv)
- [JSON results](../artifacts/model_based_planning_results.json)
