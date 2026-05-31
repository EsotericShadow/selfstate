# Architecture Hard-Return Audit Report

## Purpose

This experiment audits the main caveat in report 52.

The soft-return optimizer showed that recurrent architectures can recover the expected boundary signatures without source-direction seeds or boundary-aware restart selection. But it still used a smooth expected-return surrogate. That leaves an important question:

> Does hard realized return alone select the same causal boundary abstractions?

This audit removes the smooth surrogate. It optimizes recurrent weights only by realized recurrent training return, selects restarts only by realized recurrent return, and applies the same end-to-end boundary classifier afterward.

## Question

Can hard-return-only optimization recover strict architecture-wide boundary convergence without source-direction seeds, smooth expected return, or boundary-aware restart selection?

## Design

For each scenario and architecture, the experiment:

1. samples mixed noisy observations from the same boundary benchmark used in reports 48 to 52;
2. initializes raw recurrent weights from Gaussian starts;
3. optimizes those weights with cross-entropy search ranked only by realized recurrent return;
4. selects the restart by realized recurrent return only;
5. selects policies by realized training return against recurrent, local-probe, greedy, and safe baselines;
6. applies the same end-to-end action-boundary classifier used in the prior probes.

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
python3 experiments/architecture_hard_return_audit.py --episodes 300 --training-episodes 400 --seed 20260603 --horizon 8 --evidence-samples 9 --cue-accuracy 0.85 --iterations 16 --population 220 --restarts 10 --initial-std 1.4
```

## Current Result

| Scenario | Expected signature | Converged architectures | Hard-return result |
|---|---|---:|---|
| `self_persistent_boundary` | `end_to_end_persistent_agent_boundary` | 2/3 | Partial hard-return boundary convergence. |
| `detachable_tool_world` | `end_to_end_detachable_external_boundary` | 1/3 | Partial hard-return boundary convergence. |
| `passive_world_boundary` | `end_to_end_passive_external_boundary` | 3/3 | Strict hard-return boundary convergence. |
| `independent_hidden` | `end_to_end_local_probe` | 3/3 | Hard return rejects shared recurrence. |
| `irrelevant_control` | `end_to_end_no_hidden_needed` | 3/3 | Hard return rejects hidden state. |

Architecture-level signatures:

| Scenario | `sum_rnn` | `scalar_rnn` | `two_unit_rnn` |
|---|---|---|---|
| `self_persistent_boundary` | `end_to_end_persistent_agent_boundary` | `end_to_end_persistent_agent_boundary` | `end_to_end_passive_external_boundary` |
| `detachable_tool_world` | `end_to_end_detachable_external_boundary` | `end_to_end_passive_external_boundary` | `end_to_end_passive_external_boundary` |
| `passive_world_boundary` | `end_to_end_passive_external_boundary` | `end_to_end_passive_external_boundary` | `end_to_end_passive_external_boundary` |
| `independent_hidden` | `end_to_end_local_probe` | `end_to_end_local_probe` | `end_to_end_local_probe` |
| `irrelevant_control` | `end_to_end_no_hidden_needed` | `end_to_end_no_hidden_needed` | `end_to_end_no_hidden_needed` |

## Interpretation

This is negative evidence against treating return success as equivalent to boundary discovery.

Hard return alone finds useful recurrent control in the shared regimes. It also keeps the controls clean: independent hidden state still selects local probing, and irrelevant hidden state still selects greedy no-state control.

But hard return does not force strict architecture-wide recovery of the causal boundary signature. In the failed shared cells, the chosen recurrent controllers have high reward and beat local probing, but the policy-state intervention does not cross the threshold for the expected persistent-agent or detachable-tool boundary. They are useful hidden-state controllers without the full boundary abstraction.

The result sharpens the current claim:

> Stronger smooth optimization can discover boundary-equivalent structure in this toy benchmark; hard realized return alone produces only partial boundary convergence.

That means report 52 remains real evidence, but it is not yet evidence that ordinary online return optimization will reliably discover self-equivalent boundaries.

Report 54 tests whether longer horizons repair this limitation. They improve hard-return recovery but still leave self and detachable boundary convergence partial. Report 55 tests an online-style return learner and finds the same broad limitation: controls stay clean, but shared regimes remain only partially convergent. Report 56 shows that stochastic policy-gradient credit assignment can recover strict convergence under the same boundary classifier.

## Falsifiers And Strengtheners

The hard-return limitation weakens if:

- larger hard-return budgets or different seeds produce strict convergence across all architectures;
- hard-return agents recover the missing self and detachable signatures under richer but still objective-only selection;
- the failed cells are shown to fail only because of arbitrary classifier thresholds rather than genuine weak policy-state boundary effects.

The attractor claim strengthens if:

- full online RL or model-based learning recovers strict boundary convergence without smooth expected-return surrogates;
- hard-return optimization becomes strict under longer horizons, richer evidence, or richer recurrent architectures;
- causal ablation shows that the high-return hard controllers still contain a boundary-equivalent latent even when the current intervention classifier misses it.

## Artifacts

- [experiment script](../experiments/architecture_hard_return_audit.py)
- [summary CSV](../artifacts/architecture_hard_return_audit_summary.csv)
- [verdict CSV](../artifacts/architecture_hard_return_audit_verdict.csv)
- [JSON results](../artifacts/architecture_hard_return_audit_results.json)
