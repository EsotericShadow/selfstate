# Architecture Policy-Gradient Learner Report

## Purpose

This experiment follows report 55.

The online return-learner audit showed that antithetic perturbation learning from sampled return kept controls clean but still left all shared regimes only partially convergent. This report tests a richer objective-only learner: a stochastic recurrent policy trained by score-function policy gradient.

The question is whether sampled-return gradient training can recover the missing self/tool boundary signatures without source-direction seeds, a smooth expected-return surrogate, or boundary-aware selection.

## Question

Does stochastic policy-gradient learning converge on the expected boundary signatures across recurrent architectures?

## Design

For each scenario and recurrent architecture, the experiment:

1. initializes recurrent policy weights from Gaussian starts;
2. samples fresh training batches across epochs;
3. samples risky/safe action from the recurrent policy logit;
4. updates weights by a score-function gradient using sampled episode return and a batch baseline;
5. selects restarts by sampled validation return;
6. selects among recurrent, local-probe, greedy, and safe policies by realized return;
7. applies the same end-to-end action-boundary classifier used in reports 48 to 55.

The learner uses gradients of the policy log probability, not gradients of environment reward. It is still toy-scale, but it is a stronger sampled-return learner than the perturbation-only online audit.

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
python3 experiments/architecture_policy_gradient_learner.py --episodes 200 --training-episodes 400 --validation-episodes 240 --batch-episodes 128 --seed 20260605 --horizon 8 --evidence-samples 9 --cue-accuracy 0.85 --epochs 32 --restarts 5 --temperature 1.8 --learning-rate 0.12 --lr-decay 0.96 --initial-std 0.8 --finite-diff-epsilon 0.02 --max-grad-norm 4.0
```

## Current Result

| Scenario | Expected signature | Converged architectures | Policy-gradient result |
|---|---|---:|---|
| `self_persistent_boundary` | `end_to_end_persistent_agent_boundary` | 3/3 | Policy gradient discovers shared boundary. |
| `detachable_tool_world` | `end_to_end_detachable_external_boundary` | 3/3 | Policy gradient discovers shared boundary. |
| `passive_world_boundary` | `end_to_end_passive_external_boundary` | 3/3 | Policy gradient discovers shared boundary. |
| `independent_hidden` | `end_to_end_local_probe` | 3/3 | Policy gradient rejects shared recurrence. |
| `irrelevant_control` | `end_to_end_no_hidden_needed` | 3/3 | Policy gradient rejects hidden state. |

Architecture-level signatures:

| Scenario | `sum_rnn` | `scalar_rnn` | `two_unit_rnn` |
|---|---|---|---|
| `self_persistent_boundary` | `end_to_end_persistent_agent_boundary` | `end_to_end_persistent_agent_boundary` | `end_to_end_persistent_agent_boundary` |
| `detachable_tool_world` | `end_to_end_detachable_external_boundary` | `end_to_end_detachable_external_boundary` | `end_to_end_detachable_external_boundary` |
| `passive_world_boundary` | `end_to_end_passive_external_boundary` | `end_to_end_passive_external_boundary` | `end_to_end_passive_external_boundary` |
| `independent_hidden` | `end_to_end_local_probe` | `end_to_end_local_probe` | `end_to_end_local_probe` |
| `irrelevant_control` | `end_to_end_no_hidden_needed` | `end_to_end_no_hidden_needed` | `end_to_end_no_hidden_needed` |

## Interpretation

This is positive evidence for learner-dependent self-boundary emergence.

The perturbation-only online learner in report 55 showed that sampled return alone is not sufficient. This policy-gradient learner changes the update rule while keeping the key constraints:

- no source-direction seeds;
- no smooth expected-return surrogate;
- no boundary-aware restart selection;
- the same post-training causal boundary classifier.

Under that stronger sampled-return learner, all three recurrent architectures recover the expected boundary signatures in all shared regimes, and the controls remain clean.

Report 57 shows this one-seed success is not automatically seed-stable. Report 58 then shows that larger budgets repair self-persistent and passive-world seed stability but still leave detachable-tool recurrence partial.

The lesson is not that any hidden state is selfhood. The lesson is narrower:

> When the learner can assign credit through its stochastic policy, sampled return can shape recurrent policy state into the correct persistent agent/tool/passive boundary abstraction.

That strengthens the attractor hypothesis while preserving the hidden-state boundary. Independent hidden state still selects local probing, and irrelevant hidden state still selects no-hidden greedy action.

## Falsifiers And Strengtheners

The result weakens if:

- different seeds or larger validation sets make convergence unstable;
- richer controls produce false self-boundary positives;
- non-recurrent or generic-history policies match the same boundary behavior without a stable policy-state abstraction.

The attractor claim strengthens if:

- policy-gradient and actor-critic learners reproduce this result across richer bodies, viability states, frame shifts, and continuity tasks;
- the same boundary emerges under multiple independent credit-assignment methods;
- learned latent ablation and counterfactual editing show that the policy-gradient state is causally necessary, not only decodable.

Report 57 runs the first seed-stability audit. It keeps controls clean across five seeds, but strict shared-regime convergence is only partial. This report should therefore be read as evidence of recoverability under policy-gradient credit assignment, not proof of seed-stable inevitability.

## Artifacts

- [experiment script](../experiments/architecture_policy_gradient_learner.py)
- [summary CSV](../artifacts/architecture_policy_gradient_learner_summary.csv)
- [verdict CSV](../artifacts/architecture_policy_gradient_learner_verdict.csv)
- [JSON results](../artifacts/architecture_policy_gradient_learner_results.json)
