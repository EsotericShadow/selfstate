# Report 152: SSRM-3D source-native council ledger bridge

## Summary

Report 152 closes the main honesty gap left by Report 151. Instead of reconstructing rejected proposal bodies after the fact, it runs a new deterministic council loop that stores every accepted and rejected proposal body during generation and decision. The ledger records proposal origin events, rank traces, decision reasons, budget deficits, faction votes, feedback links, and source-originality claims.

The integrated condition reaches source-native readiness `1.000000`. Rejected-body storage is `1.000000`, council-queue persistence is `1.000000`, budget-failure evidence is `1.000000`, faction-vote memory is `1.000000`, and source-originality status is `1.000000`.

This is still not subjective consciousness, LLM dialogue, unscripted civilization, or a complete playable world. It is a source-native governance ledger that removes the need for reconstructed rejected-proposal bodies in the next dialogue layer.

## What changed

- Added `experiments/ssrm_3d_source_native_council_ledger_bridge.py`.
- Imports Report 149 proposal mechanics but runs a new source-native storage loop.
- Stores full rejected proposal bodies during council decision, not after the fact.
- Persists `proposal_origin_event`, `decision_trace`, `budget_deficit`, `faction_votes`, and `source_originality_claim` objects.
- Adds deterministic avatar questions over source bodies, rejection reasons, budget deficits, ranks, faction votes, feedback links, originality status, and refusal boundaries.
- Emits a browser viewer at `visualizations/ssrm_3d_source_native_council_ledger_bridge.html`.

## Conditions

| Condition | Readiness | Rejected body | Queue | Decision reason | Budget evidence | Faction votes | Dialogue | Feedback | Originality | Replay |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `integrated_source_native_council_ledger` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_source_rejected_body_storage` | `0.588889` | `0.000000` | `1.000000` | `0.465278` | `0.000000` | `0.465278` | `1.000000` | `1.000000` | `0.465278` | `1.000000` |
| `no_council_queue_persistence` | `0.890000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_rank_decision_trace` | `0.900000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_budget_failure_evidence` | `0.900000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_faction_vote_memory` | `0.900000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_dialogue_grounding` | `0.870000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_source_mutation_feedback` | `0.900000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` |
| `no_trace_replay` | `0.900000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` |

## Ledger objects

- `source_native_rejected_body`: rejected proposal body stored in the same decision loop as accepted bodies.
- `proposal_origin_event`: generation-time event before ranking and budget arbitration.
- `decision_trace`: rank, score, max-accept limit, and reason from the council loop.
- `budget_deficit_evidence`: budget snapshot and missing materials for scarce-budget rejection.
- `faction_vote_memory`: support/block/bargain stance for every faction at decision time.
- `source_originality_claim`: explicit statement that the body is stored during Report 152 rather than inferred later.

## Evidence and ablations

Removing source rejected-body storage drops readiness by `0.411111`. Removing council queue persistence drops readiness by `0.110000`. Removing rank/decision traces, budget evidence, faction votes, dialogue grounding, mutation feedback, or replay traces produces targeted losses.

## Artifacts

- `artifacts/ssrm_3d_source_native_council_ledger_bridge_eval.csv`
- `artifacts/ssrm_3d_source_native_council_ledger_bridge_verdict.csv`
- `artifacts/ssrm_3d_source_native_council_ledger_bridge_results.json`
- `artifacts/ssrm_3d_source_native_council_ledger_bridge_trace.json`
- `artifacts/ssrm_3d_source_native_council_ledger_bridge_state.json`
- `artifacts/ssrm_3d_source_native_council_ledger_bridge_results.js`
- `artifacts/ssrm_3d_source_native_council_ledger_bridge_trace.js`
- `artifacts/ssrm_3d_source_native_council_ledger_bridge_state.js`
- `visualizations/ssrm_3d_source_native_council_ledger_bridge.html`

## Verdict

The bridge passes as a source-native council ledger bridge because accepted and rejected proposal bodies are stored during the council loop with decision reasons, budget evidence, faction votes, feedback links, source-originality status, and replayable dialogue citations.

The next gate is to feed this source-native ledger into learned faction/dialogue policy, so political memory and avatar questioning are learned over persistent histories instead of scripted over deterministic records.
