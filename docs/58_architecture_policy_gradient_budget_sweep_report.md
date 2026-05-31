# Architecture Policy-Gradient Budget Sweep Report

## Purpose

This experiment audits report 57.

The policy-gradient seed sweep showed that sampled-return credit assignment can recover the expected boundary signatures, but strict convergence was not seed-stable at the standard budget.

This report asks a narrower question:

> Is the seed instability a small-budget optimization artifact?

## Question

Do larger policy-gradient budgets repair seed-stable boundary convergence without creating control false positives?

## Design

The experiment repeats the report 57 seed sweep under two budgets:

| Budget | Epochs | Restarts | Batch episodes |
|---|---:|---:|---:|
| `standard` | 32 | 5 | 128 |
| `larger` | 64 | 8 | 192 |

For each budget, each seed in `20260605,20260606,20260607,20260608,20260609`, each scenario, and each recurrent architecture, the experiment:

1. trains the same stochastic policy-gradient learner;
2. selects restarts by sampled validation return;
3. selects among recurrent, local-probe, greedy, and safe policies by realized return;
4. applies the same end-to-end boundary classifier;
5. reports whether the larger budget repairs strict seed stability.

The test is intentionally not allowed to pass by averaging away failures. A scenario is seed-stable only if every seed reaches `3/3` architecture convergence.

## Command

```bash
python3 experiments/architecture_policy_gradient_budget_sweep.py --seeds 20260605,20260606,20260607,20260608,20260609 --budgets 'standard:32:5:128;larger:64:8:192' --episodes 200 --training-episodes 400 --validation-episodes 240 --horizon 8 --evidence-samples 9 --cue-accuracy 0.85 --temperature 1.8 --learning-rate 0.12 --lr-decay 0.96 --initial-std 0.8 --finite-diff-epsilon 0.02 --max-grad-norm 4.0
```

## Current Result

| Scenario | Standard budget | Larger budget | Result |
|---|---:|---:|---|
| `self_persistent_boundary` | strict `2/5`, cells `12/15` | strict `5/5`, cells `15/15` | Repairs seed instability. |
| `detachable_tool_world` | strict `3/5`, cells `12/15` | strict `3/5`, cells `13/15` | Improves but remains not seed-stable. |
| `passive_world_boundary` | strict `3/5`, cells `13/15` | strict `5/5`, cells `15/15` | Repairs seed instability. |
| `independent_hidden` | strict `5/5`, cells `15/15` | strict `5/5`, cells `15/15` | Stable rejection of shared recurrence. |
| `irrelevant_control` | strict `5/5`, cells `15/15` | strict `5/5`, cells `15/15` | Stable rejection of hidden state. |

The architecture-level failure that remains is specific:

- `detachable_tool_world` still fails in seed `20260607` for `two_unit_rnn`;
- `detachable_tool_world` still fails in seed `20260608` for `two_unit_rnn`;
- both failures occur while `sum_rnn` and `scalar_rnn` recover the detachable external-boundary signature.

## Interpretation

The result strengthens the policy-gradient attractor precursor, but it does not close it.

The positive evidence is that larger budgets repair seed stability for the self-persistent and passive-world shared regimes while preserving perfectly clean controls. That makes the report 57 instability partly attributable to optimization budget rather than to a hard impossibility of sampled-return policy-gradient learning.

The limiting evidence is that detachable-tool/world recurrence still does not reach strict seed stability. This is important for the hidden-state boundary attack: the abstraction is not simply "track any hidden internal variable." The learner must also separate persistent agent-bounded recurrence from detachable external action effects. That boundary is still harder than the self and passive-world cases in this toy stack.

The current claim should therefore be:

> Larger policy-gradient budgets make self-boundary recovery seed-stable in this toy benchmark and keep controls clean, but they do not yet produce seed-stable convergence for all self-equivalent boundary distinctions.

Report 59 tests the next narrow repair: a Torch actor-critic learner closes the detachable-tool boundary for `RNN`, `GRU`, and `LSTM` architectures in a single canonical MPS run. That does not retroactively make this budget sweep seed-stable; it identifies the next mechanism to seed-sweep.

## Falsifiers And Strengtheners

The attractor claim weakens if:

- wider budget sweeps leave detachable-tool convergence partial;
- larger budgets create false positives in independent-hidden or irrelevant controls;
- actor-critic or model-based learners recover reward without the causal boundary signature.

The attractor claim strengthens if:

- detachable-tool convergence becomes seed-stable under a principled learner improvement;
- actor-critic seed sweeps reproduce the self/tool/passive repairs without control false positives;
- the same budget-sensitive repair appears across richer body, viability, frame, and continuity environments.

## Artifacts

- [experiment script](../experiments/architecture_policy_gradient_budget_sweep.py)
- [summary CSV](../artifacts/architecture_policy_gradient_budget_sweep_summary.csv)
- [verdict CSV](../artifacts/architecture_policy_gradient_budget_sweep_verdict.csv)
- [JSON results](../artifacts/architecture_policy_gradient_budget_sweep_results.json)
