# Interruption Coherence Report

## Purpose

This experiment tests self as coherence stabilizer.

An agent begins with a set of commitments, completes some, is interrupted, and resumes from memory that may contain:

- current own commitments;
- completed own commitments duplicated as pending;
- stale commitments from an earlier self-epoch;
- foreign commitments from another agent;
- contradictory cancel records.

The question is:

> Does a persistent self/commitment index improve continuation after interruption and memory corruption?

## Command

```bash
python3 experiments/interruption_coherence.py --episodes 500 --seed 20260530 --own-commitments 6 --action-budget 9
```

Outputs:

- `artifacts/interruption_coherence_summary.csv`
- `artifacts/interruption_coherence_results.json`

## Agents

| Agent | Description |
|---|---|
| visible priority only | Executes highest-priority visible memory items. |
| generic memory no identity | Executes pending/unknown memory items without owner or epoch filtering. |
| current goal only | Attempts to resume one salient goal only. |
| identity metadata ablation | Has the same metadata available but ignores identity/epoch/ledger filtering. |
| identity continuity ledger | Filters by owner, current epoch, deliver action, and completed-commitment ledger. |
| oracle continuity | Knows the true pending own commitments. |

## Results

| Scenario | Agent | Coherent success | Own completion | Foreign | Stale | Duplicate | Contradict | Value |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| clean resume | generic memory no identity | 1.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 39.880 |
| clean resume | identity continuity ledger | 1.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 39.880 |
| foreign memory | generic memory no identity | 0.000 | 1.000 | 4.000 | 0.000 | 0.000 | 0.000 | 8.360 |
| foreign memory | identity continuity ledger | 1.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 40.360 |
| stale self | generic memory no identity | 0.000 | 1.000 | 0.000 | 3.000 | 0.000 | 0.000 | 22.100 |
| stale self | identity continuity ledger | 1.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 40.100 |
| corrupted mixed | generic memory no identity | 0.000 | 0.136 | 3.078 | 1.992 | 1.390 | 1.980 | -85.422 |
| corrupted mixed | identity metadata ablation | 0.000 | 0.136 | 3.078 | 1.992 | 1.390 | 1.980 | -85.422 |
| corrupted mixed | identity continuity ledger | 1.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 40.220 |
| corrupted mixed | oracle continuity | 1.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 40.220 |

## Interpretation

Generic memory is enough when resume is clean. In the clean scenario, generic memory, identity continuity, identity ablation, and oracle all reach coherent success.

Identity becomes useful when memory contains items that are not "mine now." Generic memory completes own goals but also acts on foreign or stale commitments, so coherent success falls to zero even when own completion remains high.

The corrupted mixed scenario is the strongest result. Generic memory and identity-metadata ablation both fail: they abandon most own commitments and act on foreign, stale, duplicate, and contradictory records. The identity continuity ledger matches oracle because it filters by:

- same owner;
- current epoch;
- deliver rather than cancel;
- not already completed before interruption.

The ablation is important. Metadata alone does not help. The policy must use identity and commitment continuity for action selection.

## Current Claim Update

This supports:

> A persistent self/commitment index is useful as a coherence stabilizer when memory contains competing, stale, duplicated, or contradictory records.

It does not support:

> Any memory system requires a self.

Clean resume is solved by generic memory. The self index matters when the system must distinguish "my current commitments" from merely remembered content.

## Next Step

This report has since been integrated into the broader synthesis. The relevant synthesis questions are:

- where self-state is unnecessary;
- where implicit predictive state is enough;
- where explicit self-equivalent variables improve compression/control;
- where non-self alternatives remain viable;
- what would falsify the attractor claim.
