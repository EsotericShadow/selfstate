# Selfhood Boundary Probe Report

## Purpose

This probe directly tests the hidden-state loophole:

```text
Maybe hidden agent-state is doing all the work, and "selfhood" only renames useful hidden-state tracking.
```

The experiment deliberately includes hidden variables that help performance but should not count as selfhood. The boundary only passes when the useful hidden variable is agent-bounded, persistent, action-mediated, control/value relevant, counterfactually active, and integrated across prediction or control.

## Scenarios

| Scenario | Hidden variable | Expected verdict |
|---|---|---|
| `hidden_world_bias` | External wind/bias changes outcomes. | Useful world model, not selfhood. |
| `internal_report_only` | Internal diagnostic improves passive report prediction. | Internal-state tracking, not selfhood. |
| `action_effect_state` | Internal gain changes what actions do. | Minimal self-equivalent. |
| `viability_state` | Hidden energy controls future options and survival. | Long-horizon control self. |
| `continuity_state` | Owner/current-epoch metadata filters commitments. | Identity-like self. |

## Current Result

Canonical run:

```bash
python3 experiments/selfhood_boundary_probe.py --episodes 500 --seed 20260530 --horizon 24
```

| Scenario | Metric | Baseline mean | Hidden-tracker mean | Gain | Counts as self-equivalent? |
|---|---:|---:|---:|---:|---|
| `hidden_world_bias` | control reward | -2.996 | -0.062 | 2.934 | No |
| `internal_report_only` | report accuracy | 0.550 | 0.852 | 0.302 | No |
| `action_effect_state` | control reward | -1.825 | -0.220 | 1.606 | Yes |
| `viability_state` | survival value | -29.690 | 30.954 | 60.644 | Yes |
| `continuity_state` | coherence score | -0.380 | 6.000 | 6.380 | Yes |

The first two rows are the key anti-tautology controls. A hidden external variable helps control, and a hidden internal variable helps report prediction. Neither counts as selfhood under the boundary.

## Interpretation

The probe supports a stricter claim:

```text
Performance gain from hidden-state tracking is not enough.
Selfhood evidence begins when the useful hidden variable belongs to the controlled system
and mediates action, future value, counterfactual control, or continuity.
```

The result does not prove that selfhood is necessary. It prevents the theory from treating every useful hidden variable as self-equivalent.

## Falsifiers

This boundary weakens if future learned agents show that:

- hidden external-state trackers produce all claimed self-model advantages;
- passive internal diagnostics scale to action, value, and continuity tasks without becoming agent-state controllers;
- generic recurrent memory matches self-boundary agents with no decodable agent-bounded latent;
- intervention on the proposed self-variable does not change action-centered counterfactuals;
- the boundary labels fail under richer bodies, sensors, goals, or multi-agent settings.

## Artifacts

- [experiment script](../experiments/selfhood_boundary_probe.py)
- [summary CSV](../artifacts/selfhood_boundary_summary.csv)
- [JSON results](../artifacts/selfhood_boundary_results.json)
