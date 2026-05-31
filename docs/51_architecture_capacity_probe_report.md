# Architecture Capacity Probe Report

## Purpose

This experiment diagnoses the negative result from reports 49 and 50.

The architecture stress tests showed that random-start training does not make all recurrent architectures converge on the same boundary signature. That leaves two possibilities:

1. The weaker architectures cannot represent the boundary well enough.
2. The weaker architectures can represent it, but the current training search does not find the right parameters.

This probe tests the second possibility by supplying a small seed family of source-direction recurrent candidates, selecting by return, and then applying the same end-to-end boundary probe.

This is not evidence of natural emergence. It is a capacity diagnostic.

## Question

If useful source-direction seeds are supplied, can all tested recurrent architectures represent and use the correct boundary signature?

## Design

Each architecture receives the same small candidate family:

- source A direction;
- source B direction;
- negative source A direction;
- negative source B direction;
- several recurrence and output-weight values.

Then selection is by return, not by scenario label. The selected policy is tested with the same end-to-end boundary classifier used in reports 48 to 50.

Architectures:

- `sum_rnn`
- `scalar_rnn`
- `two_unit_rnn`

## Command

```bash
python3 experiments/architecture_capacity_probe.py --episodes 500 --training-episodes 800 --seed 20260603 --horizon 8 --evidence-samples 9 --cue-accuracy 0.85
```

## Current Result

| Scenario | Expected signature | Converged architectures | Capacity result |
|---|---|---:|---|
| `self_persistent_boundary` | `end_to_end_persistent_agent_boundary` | 3/3 | Seeded capacity recovers shared boundary. |
| `detachable_tool_world` | `end_to_end_detachable_external_boundary` | 3/3 | Seeded capacity recovers shared boundary. |
| `passive_world_boundary` | `end_to_end_passive_external_boundary` | 3/3 | Seeded capacity recovers shared boundary. |
| `independent_hidden` | `end_to_end_local_probe` | 3/3 | Seeded capacity rejects shared recurrence. |
| `irrelevant_control` | `end_to_end_no_hidden_needed` | 3/3 | Seeded capacity rejects hidden state. |

Architecture-level signatures:

| Scenario | `sum_rnn` | `scalar_rnn` | `two_unit_rnn` |
|---|---|---|---|
| `self_persistent_boundary` | `end_to_end_persistent_agent_boundary` | `end_to_end_persistent_agent_boundary` | `end_to_end_persistent_agent_boundary` |
| `detachable_tool_world` | `end_to_end_detachable_external_boundary` | `end_to_end_detachable_external_boundary` | `end_to_end_detachable_external_boundary` |
| `passive_world_boundary` | `end_to_end_passive_external_boundary` | `end_to_end_passive_external_boundary` | `end_to_end_passive_external_boundary` |
| `independent_hidden` | `end_to_end_local_probe` | `end_to_end_local_probe` | `end_to_end_local_probe` |
| `irrelevant_control` | `end_to_end_no_hidden_needed` | `end_to_end_no_hidden_needed` | `end_to_end_no_hidden_needed` |

## Interpretation

The prior architecture stress failure is not primarily a representational-capacity impossibility. All three recurrent architectures can express and use the correct boundary when the source-direction basis is supplied.

But this does not rescue the full attractor claim. The seed family supplies useful structure. Therefore the result means:

> The current obstacle is discovery/training search, not raw architecture capacity.

The strong attractor claim still requires independently trained systems to discover the boundary without being handed source-direction seeds.

Report 52 tests that next narrow step with a stronger toy optimizer: source-direction seeds are removed, but optimization still uses a smooth expected-return surrogate plus a small realized-return ranking term rather than full online RL.

## Falsifiers And Strengtheners

The capacity interpretation weakens if:

- seeded scalar or two-unit recurrent architectures still fail to recover the expected boundary;
- controls falsely receive persistent self-boundary signatures;
- source-direction seeds only work by using explicit scenario labels.

The attractor claim strengthens if:

- richer training methods discover the same source/boundary directions without supplied seeds;
- all architectures converge under unsupervised or return-only training;
- controls keep rejecting shared recurrence and hidden-state dependence.

## Artifacts

- [experiment script](../experiments/architecture_capacity_probe.py)
- [summary CSV](../artifacts/architecture_capacity_probe_summary.csv)
- [verdict CSV](../artifacts/architecture_capacity_probe_verdict.csv)
- [JSON results](../artifacts/architecture_capacity_probe_results.json)
