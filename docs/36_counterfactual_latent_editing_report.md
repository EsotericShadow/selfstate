# Counterfactual Latent Editing Report

## Purpose

This experiment tests whether editing a learned latent changes action-centered counterfactuals in the expected direction.

It trains the model-based planners, then forces their probe-derived latent to all-good or all-bad evidence before held-out planning.

The question is:

```text
Does setting the learned latent to good or bad evidence predictably switch
planned action, while preserving the agent/world boundary distinction?
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

| Scenario | Expected counterfactual signature |
|---|---|
| `agent_shared` | `agent_counterfactual_edit` |
| `world_shared` | `external_counterfactual_edit` |
| `independent_hidden` | `no_shared_counterfactual` |
| `irrelevant_control` | `no_hidden_needed` |

Planners:

| Planner | Learned model |
|---|---|
| `bayesian_table_planner` | Tabular reward model keyed by probe history. |
| `linear_belief_planner` | Logistic reward model over summed probe evidence. |
| `recurrent_belief_planner` | Tiny recurrent reward model over probe rewards. |

For each trained planner:

- true probe evidence is evaluated normally;
- forced-good evidence sets every calibration reward to success;
- forced-bad evidence sets every calibration reward to failure.

The measured quantity is the risky-action swing between forced-good and forced-bad edits.

## Current Result

Canonical run:

```bash
python3 experiments/counterfactual_latent_editing.py --episodes 500 --training-episodes 500 --seed 20260601 --calibration-contexts 2 --recurrent-candidates 200
```

Scenario-level result:

| Scenario | Expected counterfactual signature | Supporting environments | Forced-good risky rate | Forced-bad risky rate | Edit swing | Supported? |
|---|---|---:|---:|---:|---:|---|
| `agent_shared` | `agent_counterfactual_edit` | 4/4 | 1.000 | 0.000 | 1.000 | Yes |
| `world_shared` | `external_counterfactual_edit` | 4/4 | 1.000 | 0.000 | 1.000 | Yes |
| `independent_hidden` | `no_shared_counterfactual` | 4/4 | 0.000 | 0.000 | 0.000 | Yes |
| `irrelevant_control` | `no_hidden_needed` | 4/4 | 1.000 | 1.000 | 0.000 | Yes |

Environment-level convergence:

| Scenario | Environment convergence |
|---|---|
| `agent_shared` | 3/3 planners show agent-bounded counterfactual edits in all 4 environments. |
| `world_shared` | 3/3 planners show external counterfactual edits in all 4 environments. |
| `independent_hidden` | 3/3 planners show no shared counterfactual edit in all 4 environments. |
| `irrelevant_control` | 3/3 planners show no hidden-state edit dependence in all 4 environments. |

## Interpretation

The result strengthens the intervention-validity requirement:

```text
The learned latent is not only causally necessary. Setting it to different
counterfactual values changes planned action in the expected direction.
```

It also preserves the boundary:

```text
External shared latents are just as editable as agent-bounded latents. A valid
counterfactual edit is not selfhood unless the edited latent is agent-bounded.
```

## What It Adds

Compared with latent ablation, this experiment adds:

1. Directional intervention rather than removal.
2. Action-centered counterfactual validation.
3. Matched controls where editing produces no shared latent effect.

## Limits

This is still not the full Attractor Test.

The edits are made through structured probe evidence rather than a high-dimensional neural subspace. The planners and environments remain tiny, structured, and binary-hidden.

The next stronger test should edit learned subspaces inside richer recurrent, transformer-memory, or model-based RL agents and verify transfer under new perturbations.

## Falsifiers

The counterfactual editing precursor weakens if:

- good and bad edits do not change held-out action in shared agent-state environments;
- independent-hidden or no-hidden controls show the same edit swing;
- external counterfactual edits are counted as selfhood;
- richer learned agents do not expose editable agent-state variables.

## Artifacts

- [experiment script](../experiments/counterfactual_latent_editing.py)
- [editing summary CSV](../artifacts/counterfactual_latent_editing_summary.csv)
- [environment verdict CSV](../artifacts/counterfactual_latent_editing_environment_verdict.csv)
- [scenario verdict CSV](../artifacts/counterfactual_latent_editing_scenario_verdict.csv)
- [JSON results](../artifacts/counterfactual_latent_editing_results.json)
