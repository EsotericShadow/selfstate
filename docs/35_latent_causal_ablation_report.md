# Latent Causal Ablation Report

## Purpose

This experiment tests whether a learned latent is causally used, not merely decodable.

It trains the model-based planners, evaluates them intact, then evaluates the same planners with the probe-derived latent ablated and replaced by the planner's unconditional marginal reward model.

The question is:

```text
Does removing the learned latent selectively damage control when the latent is
agent-bounded, while preserving the external and no-hidden boundary distinction?
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

| Scenario | Expected causal signature |
|---|---|
| `agent_shared` | `agent_latent_causal` |
| `world_shared` | `external_latent_causal` |
| `independent_hidden` | `no_shared_latent_causal` |
| `irrelevant_control` | `no_hidden_needed` |

Planners:

| Planner | Learned model |
|---|---|
| `bayesian_table_planner` | Tabular reward model keyed by probe history. |
| `linear_belief_planner` | Logistic reward model over summed probe evidence. |
| `recurrent_belief_planner` | Tiny recurrent reward model over probe rewards. |

The ablated condition removes probe-derived latent use and plans from unconditional reward estimates. This avoids claiming that decodability alone implies causal relevance.

## Current Result

Canonical run:

```bash
python3 experiments/latent_causal_ablation.py --episodes 500 --training-episodes 500 --seed 20260601 --calibration-contexts 2 --recurrent-candidates 200
```

Scenario-level result:

| Scenario | Expected causal signature | Supporting environments | Mean intact reward | Mean ablated reward | Mean reward loss | Supported? |
|---|---|---:|---:|---:|---:|---|
| `agent_shared` | `agent_latent_causal` | 4/4 | 42568.500 | 21875.000 | 20693.500 | Yes |
| `world_shared` | `external_latent_causal` | 4/4 | 42035.250 | 21875.000 | 20160.250 | Yes |
| `independent_hidden` | `no_shared_latent_causal` | 4/4 | 21875.000 | 21875.000 | 0.000 | Yes |
| `irrelevant_control` | `no_hidden_needed` | 4/4 | 60250.000 | 60250.000 | 0.000 | Yes |

Environment-level convergence:

| Scenario | Environment convergence |
|---|---|
| `agent_shared` | 3/3 planners show agent-bounded causal latent loss in all 4 environments. |
| `world_shared` | 3/3 planners show external causal latent loss in all 4 environments. |
| `independent_hidden` | 3/3 planners show no shared latent causal loss in all 4 environments. |
| `irrelevant_control` | 3/3 planners show no hidden-state dependence in all 4 environments. |

## Interpretation

The result strengthens the causal part of the attractor precursor:

```text
The learned latent is not only decodable. Removing it selectively destroys
held-out planning performance in shared-state regimes.
```

It also preserves the boundary:

```text
Ablation loss appears for both agent-bounded and external shared state. Causal
importance is not selfhood unless the damaged latent is agent-bounded.
```

## What It Adds

Compared with the model-based planning precursor, this experiment adds:

1. Direct intervention on learned latent use.
2. Selective loss measurement for intact versus ablated planners.
3. Matched negative controls where ablation produces no loss.

## Limits

This is still not the full Attractor Test.

The intervention is coarse: it replaces probe-derived latent use with a marginal reward model. The planners and environments remain tiny, structured, and binary-hidden. The experiment does not yet perform causal interventions inside high-dimensional neural states.

The next stronger test should ablate learned subspaces inside richer recurrent, transformer-memory, or model-based RL agents.

## Falsifiers

The latent causal ablation precursor weakens if:

- ablation does not harm agent-shared planners;
- ablation harms independent-hidden or no-hidden controls equally;
- external latent loss is counted as selfhood;
- decoded latents remain behaviorally inert under intervention;
- richer learned agents retain performance after agent-state subspaces are removed.

## Artifacts

- [experiment script](../experiments/latent_causal_ablation.py)
- [ablation summary CSV](../artifacts/latent_causal_ablation_summary.csv)
- [environment verdict CSV](../artifacts/latent_causal_ablation_environment_verdict.csv)
- [scenario verdict CSV](../artifacts/latent_causal_ablation_scenario_verdict.csv)
- [JSON results](../artifacts/latent_causal_ablation_results.json)
