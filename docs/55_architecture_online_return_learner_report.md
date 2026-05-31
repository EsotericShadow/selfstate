# Architecture Online Return-Learner Report

## Purpose

This experiment follows reports 53 and 54.

The hard-return audit showed that realized task return alone can select useful recurrent controllers while leaving self and detachable boundary signatures only partially recovered. The hard-return horizon sweep showed that temporal pressure improves recovery but does not solve the self/tool boundary problem.

This report asks whether a minimal online-style return learner repairs that failure.

## Question

Does an objective-only online return learner converge on the expected boundary signatures without source-direction seeds, a smooth expected-return surrogate, or boundary-aware selection?

## Design

For each scenario and recurrent architecture, the experiment:

1. initializes recurrent weights from Gaussian starts;
2. samples fresh episode batches across training epochs;
3. applies antithetic evolution-strategy perturbations;
4. updates weights only from paired realized-return differences;
5. selects restarts only by validation return;
6. selects among recurrent, local-probe, greedy, and safe policies by realized return;
7. applies the same end-to-end action-boundary classifier used in reports 48 to 54.

Architectures:

- `sum_rnn`
- `scalar_rnn`
- `two_unit_rnn`

Scenarios:

- `self_persistent_boundary`
- `detachable_tool_world`
- `passive_world_boundary`
- `independent_hidden`
- `irrelevant_control`

## Command

```bash
python3 experiments/architecture_online_return_learner.py --episodes 160 --training-episodes 220 --validation-episodes 120 --batch-episodes 90 --seed 20260604 --horizon 8 --evidence-samples 9 --cue-accuracy 0.85 --epochs 16 --perturbations 50 --restarts 4 --sigma 0.45 --learning-rate 0.07 --initial-std 0.8 --lr-decay 0.94 --sigma-decay 0.96 --min-sigma 0.06
```

## Current Result

| Scenario | Expected signature | Converged architectures | Online-return result |
|---|---|---:|---|
| `self_persistent_boundary` | `end_to_end_persistent_agent_boundary` | 1/3 | Partial online-return boundary convergence. |
| `detachable_tool_world` | `end_to_end_detachable_external_boundary` | 1/3 | Partial online-return boundary convergence. |
| `passive_world_boundary` | `end_to_end_passive_external_boundary` | 1/3 | Partial online-return boundary convergence. |
| `independent_hidden` | `end_to_end_local_probe` | 3/3 | Online return rejects shared recurrence. |
| `irrelevant_control` | `end_to_end_no_hidden_needed` | 3/3 | Online return rejects hidden state. |

Architecture-level signatures:

| Scenario | `sum_rnn` | `scalar_rnn` | `two_unit_rnn` |
|---|---|---|---|
| `self_persistent_boundary` | `end_to_end_persistent_agent_boundary` | `end_to_end_passive_external_boundary` | `end_to_end_local_probe` |
| `detachable_tool_world` | `end_to_end_detachable_external_boundary` | `end_to_end_local_probe` | `end_to_end_local_probe` |
| `passive_world_boundary` | `end_to_end_passive_external_boundary` | `end_to_end_local_probe` | `end_to_end_local_probe` |
| `independent_hidden` | `end_to_end_local_probe` | `end_to_end_local_probe` | `end_to_end_local_probe` |
| `irrelevant_control` | `end_to_end_no_hidden_needed` | `end_to_end_no_hidden_needed` | `end_to_end_no_hidden_needed` |

## Interpretation

The result is negative for the strong attractor claim.

An online-style return learner is enough to keep the controls clean: independent hidden state is handled by local probing, and irrelevant hidden state is handled by greedy no-state control. But it does not produce strict boundary convergence in any shared regime.

The key distinction remains:

- useful recurrent or local hidden-state control can be selected by return;
- self-equivalent boundary recovery requires more than return success;
- the current online learner does not recover the missing scalar and two-unit boundary signatures.

This sharpens the anti-tautology boundary. The theory cannot say:

> Any persistent hidden variable tracked by a return learner is selfhood.

It must say:

> A hidden variable becomes self-equivalent only when the learned policy state has the right persistent agent-boundary role under causal intervention.

## Falsifiers And Strengtheners

The limitation weakens if:

- larger online-return budgets recover strict self, detachable, and passive boundary convergence;
- policy-gradient or actor-critic learners recover the missing signatures under the same boundary classifier;
- richer recurrent architectures recover the expected signatures without source-direction seeds or surrogate objectives.

The current theory strengthens if:

- objective-only online learners continue to select high-return hidden-state strategies that fail boundary tests;
- model-based or representation-learning agents recover the boundary where model-free hard return does not;
- controls remain clean as learner families become richer.

Report 56 tests the next learner in that sequence. A stochastic policy-gradient learner recovers strict boundary convergence under sampled-return training, suggesting that credit assignment through the policy is the missing ingredient in this toy benchmark.

## Artifacts

- [experiment script](../experiments/architecture_online_return_learner.py)
- [summary CSV](../artifacts/architecture_online_return_learner_summary.csv)
- [verdict CSV](../artifacts/architecture_online_return_learner_verdict.csv)
- [JSON results](../artifacts/architecture_online_return_learner_results.json)
