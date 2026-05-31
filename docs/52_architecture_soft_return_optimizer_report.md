# Architecture Soft-Return Optimizer Report

## Purpose

This experiment is a stricter companion to the architecture capacity probe.

Report 51 showed that weaker recurrent architectures can represent the expected boundary signatures when source-direction seeds are supplied. That narrowed the loophole, but it did not show autonomous discovery. The remaining question was whether a stronger optimizer can find the same boundary structures without being handed source A or source B directions.

This probe removes source-direction seeds and optimizes each recurrent architecture from random Gaussian starts with a cross-entropy method ranked mainly by a smooth expected-return surrogate, with a small realized-return term.

Restarts are selected by optimizer objective only. The expected boundary signature is not used to choose the reported candidate; the end-to-end boundary classifier is applied after training and selection.

This is still not a full Attractor Test. It is a toy, simulator-facing optimizer. Its value is narrower: it tests whether the previous architecture failure was caused by weak random-start search rather than by an unavoidable need for hand-supplied source directions.

## Question

Can independently optimized recurrent architectures recover the same end-to-end boundary signatures without source-direction seeds?

## Design

For each scenario and architecture, the experiment:

1. samples mixed noisy observations from the same boundary benchmark used in reports 48 to 51;
2. initializes raw recurrent weights from Gaussian starts;
3. optimizes those weights with cross-entropy search against a differentiable expected-return surrogate plus a small realized-return ranking term;
4. selects the restart by optimizer objective, without inspecting the expected boundary signature;
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
python3 experiments/architecture_soft_return_optimizer.py --episodes 300 --training-episodes 400 --seed 20260603 --horizon 8 --evidence-samples 9 --cue-accuracy 0.85 --iterations 16 --population 220 --restarts 10 --temperature 2.5 --initial-std 1.4
```

## Current Result

| Scenario | Expected signature | Converged architectures | Optimizer result |
|---|---|---:|---|
| `self_persistent_boundary` | `end_to_end_persistent_agent_boundary` | 3/3 | Soft optimizer discovers shared boundary. |
| `detachable_tool_world` | `end_to_end_detachable_external_boundary` | 3/3 | Soft optimizer discovers shared boundary. |
| `passive_world_boundary` | `end_to_end_passive_external_boundary` | 3/3 | Soft optimizer discovers passive external recurrence. |
| `independent_hidden` | `end_to_end_local_probe` | 3/3 | Soft optimizer rejects shared recurrence. |
| `irrelevant_control` | `end_to_end_no_hidden_needed` | 3/3 | Soft optimizer rejects hidden state. |

Architecture-level signatures:

| Scenario | `sum_rnn` | `scalar_rnn` | `two_unit_rnn` |
|---|---|---|---|
| `self_persistent_boundary` | `end_to_end_persistent_agent_boundary` | `end_to_end_persistent_agent_boundary` | `end_to_end_persistent_agent_boundary` |
| `detachable_tool_world` | `end_to_end_detachable_external_boundary` | `end_to_end_detachable_external_boundary` | `end_to_end_detachable_external_boundary` |
| `passive_world_boundary` | `end_to_end_passive_external_boundary` | `end_to_end_passive_external_boundary` | `end_to_end_passive_external_boundary` |
| `independent_hidden` | `end_to_end_local_probe` | `end_to_end_local_probe` | `end_to_end_local_probe` |
| `irrelevant_control` | `end_to_end_no_hidden_needed` | `end_to_end_no_hidden_needed` | `end_to_end_no_hidden_needed` |

## Interpretation

This narrows the discovery gap. The recurrent architectures are not merely capable of representing the boundary when source directions are supplied; under this toy optimizer, they can also discover the relevant boundary-equivalent structure from mixed observations without source-direction seeds.

The stricter audit is that this convergence survives objective-only restart selection. That removes the post-hoc shortcut where a researcher could run multiple restarts and report the one whose boundary signature matches the expected class.

The result strengthens the narrow precursor claim:

> Boundary-equivalent recurrent structure can be discovered by stronger return optimization in this toy benchmark without hand-supplied source-direction candidates.

It does not prove that selfhood is an attractor in general adaptive systems. The optimizer still uses a smooth expected-return surrogate, fixed scenario family, fixed recurrent architectures, scripted post-training interventions, and a toy linear sensor mixture.

Report 53 removes that smooth surrogate. Under hard realized return alone, the same benchmark shows only partial self and detachable boundary convergence, so this caveat is behaviorally active rather than merely philosophical.

## Falsifiers And Strengtheners

The soft-optimizer interpretation weakens if:

- the 10-restart result is unstable across seeds;
- any shared regime falls back to local probing under comparable optimization budget;
- controls receive recurrent boundary signatures;
- objective-selected restarts lose the boundary signatures even though boundary-aware restart choice can find them;
- the result depends on the end-to-end classifier rather than on return-relevant behavior.

The attractor claim strengthens if:

- the same convergence appears across seeds, richer recurrent architectures, and less simulator-facing optimizers;
- online RL or model-based learning discovers the same boundary without the smooth expected-return surrogate;
- the same result appears in non-binary environments with richer bodies, tools, viability variables, and continuity demands;
- learned boundary variables survive causal ablation and counterfactual editing tests.

## Artifacts

- [experiment script](../experiments/architecture_soft_return_optimizer.py)
- [summary CSV](../artifacts/architecture_soft_return_optimizer_summary.csv)
- [verdict CSV](../artifacts/architecture_soft_return_optimizer_verdict.csv)
- [JSON results](../artifacts/architecture_soft_return_optimizer_results.json)
