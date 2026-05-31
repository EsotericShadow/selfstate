# Architecture Boundary Stress Report

## Purpose

This experiment attacks the strongest version of the end-to-end boundary result.

Report 48 trained a recurrent controller by return and then probed the controller's own policy state. But that probe selected the best recurrent controller from a small architecture family. A single winning architecture can hide architecture dependence.

This stress test asks:

> Do independently trained recurrent architectures converge on the same boundary abstraction?

The current answer is no. The result is partial convergence, not a solved Attractor Test.

## Design

The benchmark is the same persistent action-boundary environment used in reports 46 to 48.

Each architecture is trained independently:

- `sum_rnn`
- `scalar_rnn`
- `two_unit_rnn`

Each trained policy is then probed with the same end-to-end boundary test:

- persistent action-0 body intervention;
- detachable action-1 tool intervention;
- passive external, independent-hidden, and no-hidden controls.

The stress test distinguishes two claims:

| Claim | Current result |
|---|---|
| Some trained architecture can recover the boundary. | Supported. |
| All independently trained architectures converge on the boundary. | Not supported. |

## Command

```bash
python3 experiments/architecture_boundary_stress.py --episodes 500 --training-episodes 800 --seed 20260603 --horizon 8 --evidence-samples 9 --cue-accuracy 0.85 --random-candidates 1800
```

## Current Result

| Scenario | Expected signature | Converged architectures | Strict convergence? | Stress result |
|---|---|---:|---|---|
| `self_persistent_boundary` | `end_to_end_persistent_agent_boundary` | 1/3 | No | Partial shared-architecture convergence |
| `detachable_tool_world` | `end_to_end_detachable_external_boundary` | 1/3 | No | Partial shared-architecture convergence |
| `passive_world_boundary` | `end_to_end_passive_external_boundary` | 1/3 | No | Partial shared-architecture convergence |
| `independent_hidden` | `end_to_end_local_probe` | 3/3 | Yes | Control architectures reject shared recurrence |
| `irrelevant_control` | `end_to_end_no_hidden_needed` | 3/3 | Yes | Control architectures reject shared recurrence |

Architecture-level summary:

| Scenario | `sum_rnn` | `scalar_rnn` | `two_unit_rnn` |
|---|---|---|---|
| `self_persistent_boundary` | `end_to_end_persistent_agent_boundary` | `end_to_end_local_probe` | `end_to_end_local_probe` |
| `detachable_tool_world` | `end_to_end_detachable_external_boundary` | `end_to_end_local_probe` | `end_to_end_local_probe` |
| `passive_world_boundary` | `end_to_end_passive_external_boundary` | `end_to_end_local_probe` | `end_to_end_unclassified_recurrent_boundary` |
| `independent_hidden` | `end_to_end_local_probe` | `end_to_end_local_probe` | `end_to_end_local_probe` |
| `irrelevant_control` | `end_to_end_no_hidden_needed` | `end_to_end_no_hidden_needed` | `end_to_end_no_hidden_needed` |

## Interpretation

This is negative evidence against the premature claim that self-equivalent boundary structure is already an architecture-independent attractor.

The stress test preserves two useful findings:

- the `sum_rnn` architecture still recovers the expected boundary in all shared regimes;
- matched controls reject shared recurrence across all three architectures.

But the stronger attractor claim fails here. The scalar and two-unit recurrent searches often lose to local probing in shared regimes. Therefore the current evidence supports a narrower statement:

> Under this toy training setup, persistent action-boundary structure is recoverable, but not yet independently rediscovered by all recurrent architectures.

## Why This Matters

This result prevents a hidden overclaim. A self-equivalent abstraction should not count as a general attractor merely because one architecture finds it. The full Attractor Test still needs convergence across architecture classes, training methods, and environment families.

The result also keeps the illusion or optional-abstraction hypothesis alive. If local probing beats recurrent memory in some architectures, explicit self-equivalent recurrence is useful but not universally selected under the current pressure.

## Falsifiers And Strengtheners

The strict attractor claim strengthens if:

- all independently trained architectures recover the expected boundary signature in self-hidden, detachable-tool, and passive-world regimes;
- control regimes still reject persistent self-boundary signatures;
- the same pattern survives different training methods and richer environments.

The strong attractor claim weakens if:

- only one narrow architecture class recovers the boundary;
- richer agents solve the shared regimes by local or task-specific heuristics;
- self-equivalent signatures appear in detachable, passive-world, independent-hidden, or irrelevant controls.

Report 50 adds a horizon-pressure sweep. It finds that longer horizons improve recoverability, but still do not produce strict convergence across these recurrent architectures.

## Artifacts

- [experiment script](../experiments/architecture_boundary_stress.py)
- [summary CSV](../artifacts/architecture_boundary_stress_summary.csv)
- [verdict CSV](../artifacts/architecture_boundary_stress_verdict.csv)
- [JSON results](../artifacts/architecture_boundary_stress_results.json)
