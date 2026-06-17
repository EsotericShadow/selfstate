# Report 151: SSRM-3D persistent faction rejected-proposal dialogue bridge

## Summary

Report 151 moves past Report 150's rejection shadows. It creates a deterministic, audited rejected-proposal ledger from Report 149 council summaries, adds persistent faction memory, stores concessions and counterarguments, and lets the avatar ask broader locally routed questions about faction votes, rejected bodies, tradeoffs, benefits, policy adaptation, and evidence boundaries.

The integrated condition reaches faction-dialogue readiness `0.986875`. Rejected-proposal body coverage is `1.000000`, faction-memory persistence is `1.000000`, evidence citation is `1.000000`, refusal-boundary accuracy is `1.000000`, and answer specificity is `0.854167`.

The key honesty constraint is explicit: the rejected proposal bodies are `deterministic_reconstructed_not_original`. The bridge improves queryable governance memory, but it does not recover lost historical originals, call LLMs, prove subjective consciousness, or create a complete playable civilization.

## What changed

- Added `experiments/ssrm_3d_persistent_faction_rejected_dialogue_bridge.py`.
- Reads Report 149 governance state, Report 150 dialogue state, and Report 142 avatar packets.
- Builds full rejected-proposal ledger records with route/object/project, budget, token, faction, evidence basis, and reconstruction status.
- Adds persistent faction constitutions for safety, care, material, and archive factions.
- Stores faction votes, counterarguments, concessions, benefit-debt vectors, and dialogue-policy rollback hooks.
- Adds an audited question router that refuses exact lost-original transcript and consciousness-proof requests.
- Emits a browser viewer at `visualizations/ssrm_3d_persistent_faction_rejected_dialogue_bridge.html`.

## Conditions

| Condition | Readiness | Rejected bodies | Faction memory | Route | Evidence | Counter | Concession | Refusal | Adapt | Specificity | Replay |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `integrated_persistent_faction_rejected_dialogue` | `0.986875` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.854167` | `1.000000` |
| `no_rejected_proposal_ledger` | `0.751094` | `0.000000` | `1.000000` | `1.000000` | `0.125000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.734375` | `1.000000` |
| `no_persistent_faction_memory` | `0.550937` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `0.000000` | `0.000000` | `1.000000` | `0.000000` | `0.677083` | `1.000000` |
| `no_audited_question_router` | `0.170000` | `0.000000` | `1.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `1.000000` |
| `no_cross_faction_counterargument` | `0.885000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `0.833333` | `1.000000` |
| `no_concession_tradeoff_memory` | `0.885000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `0.833333` | `1.000000` |
| `no_evidence_refusal_boundary` | `0.869062` | `1.000000` | `1.000000` | `1.000000` | `0.875000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `0.822917` | `1.000000` |
| `no_dialogue_policy_adaptation` | `0.885000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `0.833333` | `1.000000` |
| `no_trace_replay` | `0.936875` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.854167` | `0.000000` |

## Unconventional objects

- `reconstructed_rejection_body`: a queryable rejected proposal body marked as reconstructed rather than original.
- `faction_constitution`: a persistent faction motto plus priorities, votes, concessions, and counterarguments.
- `council_grudge_vector`: benefit-debt counts by proposal kind inside each faction state.
- `audited_question_contract`: local intent routing with either evidence citation or refusal.
- `policy_rollback_hook`: a dialogue-policy adaptation update removable by session id.

## Evidence and ablations

Removing the rejected-proposal ledger drops readiness by `0.235781`. Removing persistent faction memory drops readiness by `0.435938`. Removing the audited router drops readiness by `0.816875`. Counterargument, concession, refusal-boundary, adaptation, and replay ablations produce targeted losses without claiming open-ended dialogue.

## Artifacts

- `artifacts/ssrm_3d_persistent_faction_rejected_dialogue_bridge_eval.csv`
- `artifacts/ssrm_3d_persistent_faction_rejected_dialogue_bridge_verdict.csv`
- `artifacts/ssrm_3d_persistent_faction_rejected_dialogue_bridge_results.json`
- `artifacts/ssrm_3d_persistent_faction_rejected_dialogue_bridge_trace.json`
- `artifacts/ssrm_3d_persistent_faction_rejected_dialogue_bridge_state.json`
- `artifacts/ssrm_3d_persistent_faction_rejected_dialogue_bridge_results.js`
- `artifacts/ssrm_3d_persistent_faction_rejected_dialogue_bridge_trace.js`
- `artifacts/ssrm_3d_persistent_faction_rejected_dialogue_bridge_state.js`
- `visualizations/ssrm_3d_persistent_faction_rejected_dialogue_bridge.html`

## Verdict

The bridge passes as a persistent-faction rejected-proposal dialogue bridge because it preserves rejected-body coverage, faction memory, routed questions, evidence citations, counterarguments, concessions, refusal boundaries, policy adaptation, and replay trace integrity.

The honest boundary remains: this is still deterministic bridge machinery. The next gate is to generate and store rejected proposal bodies at source during the council process, then learn faction/dialogue policy over persistent political histories rather than reconstructing them after the fact.
