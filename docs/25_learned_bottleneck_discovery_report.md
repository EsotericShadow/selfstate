# Learned Bottleneck Discovery Report

## Purpose

This experiment tests whether a compact hidden-state abstraction can be discovered from context/outcome data without self labels.

It separates two claims:

```text
A shared latent was learned.
```

from:

```text
The shared latent is self-equivalent.
```

That distinction matters because a reusable hidden world variable can produce the same compression signal as a reusable hidden agent variable.

## Environment

Each episode has six contexts:

| Context | Risky success reward | Risky failure reward | Safe reward |
|---|---:|---:|---:|
| `goal` | 24 | -16 | 8 |
| `option` | 34 | -30 | 14 |
| `commitment` | 22 | -18 | 12 |
| `adaptation` | 28 | -22 | 11 |
| `prediction` | 18 | -14 | 7 |
| `arbitration` | 26 | -20 | 10 |

The learner receives unlabeled context/outcome samples. It chooses among:

- `no_hidden_needed`;
- `shared_bottleneck`;
- `local_hidden`.

Then a causal boundary probe tests which intervention changes the shared hidden condition:

- intervention A affects the reusable hidden condition only in `self_reuse`;
- intervention B affects the reusable hidden condition only in `world_reuse`;
- neither produces a shared effect in `independent_hidden` or `irrelevant_control`.

The bottleneck learner is not told these meanings. They are used only for post-hoc boundary classification.

## Scenarios

| Scenario | Hidden structure | Expected learned structure | Expected boundary |
|---|---|---|---|
| `self_reuse` | One persistent agent capability controls all contexts. | `shared_bottleneck` | `agent_bounded_shared` |
| `world_reuse` | One persistent external gate controls all contexts. | `shared_bottleneck` | `external_shared` |
| `independent_hidden` | Each context has its own hidden condition. | `local_hidden` | `no_shared_agent_boundary` |
| `irrelevant_control` | Risky action always works. | `no_hidden_needed` | `no_shared_agent_boundary` |

## Agents

| Agent | Description |
|---|---|
| `no_hidden_prior` | Uses marginal structure only; safe unless hidden state is irrelevant. |
| `shared_bottleneck_policy` | Pays one calibration cost, infers a shared latent, and reuses it across contexts. |
| `task_local_probe` | Pays one local probe per control context. |
| `learned_model_selection` | Uses the learned structure selected from unlabeled outcome data. |
| `oracle` | Ceiling with true hidden conditions and no probe cost. |

## Current Result

Canonical run:

```bash
python3 experiments/learned_bottleneck_discovery.py --episodes 500 --training-episodes 300 --seed 20260531 --calibration-contexts 2
```

| Scenario | Learned structure | Boundary signature | Learned reward | Shared reward | Local reward | Boundary supported? |
|---|---|---|---:|---:|---:|---|
| `self_reuse` | `shared_bottleneck` | `agent_bounded_shared` | 69.888 | 69.888 | 66.888 | Yes |
| `world_reuse` | `shared_bottleneck` | `external_shared` | 69.780 | 69.780 | 66.780 | Yes |
| `independent_hidden` | `local_hidden` | `no_shared_agent_boundary` | 66.606 | 23.496 | 66.606 | Yes |
| `irrelevant_control` | `no_hidden_needed` | `no_shared_agent_boundary` | 94.000 | 93.000 | 90.000 | Yes |

Causal boundary effects:

| Scenario | Intervention A effect | Intervention B effect | Interpretation |
|---|---:|---:|---|
| `self_reuse` | 0.413 | 0.000 | Shared latent is agent-bounded in this toy. |
| `world_reuse` | 0.000 | 0.503 | Shared latent is external world-state. |
| `independent_hidden` | 0.000 | 0.000 | No shared boundary variable. |
| `irrelevant_control` | 0.000 | 0.000 | No hidden variable needed. |

## Interpretation

The important result is not merely that `shared_bottleneck` is learned. It is learned in both `self_reuse` and `world_reuse`.

That means:

```text
Compression alone discovers reusable hidden structure, not selfhood.
```

Self-equivalence requires the additional causal boundary result: the learned shared latent must track a hidden state of the controlled system whose state changes action-centered counterfactuals.

## What It Adds

This experiment strengthens the anti-tautology boundary:

1. A compact shared latent can be discovered without self labels.
2. The same discovery occurs for hidden external state.
3. The self/world distinction requires causal boundary evidence, not just predictive compression.
4. When hidden conditions are independent, model selection chooses local hidden variables instead of a shared bottleneck.
5. When hidden state is irrelevant, model selection chooses no hidden state.

## Limits

This is still a toy model-selection learner, not a rich neural or RL architecture. The candidate structures are supplied, the causal interventions are supplied, and the contexts are simple. It is a stronger precursor than hand-coded self probes, but it is not the full Attractor Test.

The next version should train unrelated recurrent, predictive-state, and model-based learners on raw sequences, then probe whether a shared agent-state subspace appears without candidate structures being enumerated.

## Falsifiers

The learned-bottleneck account weakens if:

- shared bottlenecks appear equally in irrelevant controls;
- local hidden conditions are misclassified as shared self-state;
- shared external variables are misclassified as self-equivalent without boundary evidence;
- the learned shared bottleneck improves prediction but not control;
- richer learners solve reusable agent-state tasks without any stable shared latent or causal boundary signature.

## Artifacts

- [experiment script](../experiments/learned_bottleneck_discovery.py)
- [summary CSV](../artifacts/learned_bottleneck_discovery_summary.csv)
- [verdict CSV](../artifacts/learned_bottleneck_discovery_verdict.csv)
- [JSON results](../artifacts/learned_bottleneck_discovery_results.json)
