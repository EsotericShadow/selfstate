# Report 153: SSRM-3D learned faction-dialogue policy bridge

## Summary

Report 153 moves past purely scripted source-ledger questions. It trains a deterministic centroid-style policy on earlier source-native council ledgers and evaluates the policy on later held-out councils. The learned policy predicts question intent, selects which source-ledger fields can be cited, grounds faction votes, budget evidence, feedback links, originality status, and refusal boundaries, and records replay traces.

The integrated condition reaches learned-dialogue readiness `0.975000`. Held-out intent accuracy is `1.000000`, held-out council generalization is `1.000000`, source-citation rate is `1.000000`, refusal-boundary accuracy is `1.000000`, and response specificity is `0.687500`.

This is not an LLM, not open-ended conversation, not subjective consciousness, and not a complete playable world. It is a deterministic learned local policy over source-native governance histories.

## What changed

- Added `experiments/ssrm_3d_learned_faction_dialogue_policy_bridge.py`.
- Uses Report 152 source-native council ledgers as training/evaluation data.
- Splits earlier councils for training from later councils for evaluation.
- Trains a centroid intent router from question and ledger features.
- Selects response plans for source body, rejection reason, budget deficit, rank trace, faction vote, feedback link, originality status, and refusal boundary questions.
- Adds a learned-router safety gate so refusal requires consciousness/mind-proof language rather than accidentally capturing faction-vote questions.
- Emits a browser viewer at `visualizations/ssrm_3d_learned_faction_dialogue_policy_bridge.html`.

## Conditions

| Condition | Readiness | Intent | Held-out | Citation | Faction | Budget | Feedback | Refusal | Originality | Specificity | Replay |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `integrated_learned_faction_dialogue_policy` | `0.975000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.687500` | `1.000000` |
| `no_learned_router` | `0.170000` | `0.000000` | `1.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `1.000000` |
| `no_source_native_ledger_features` | `0.746000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `0.575000` | `1.000000` |
| `no_faction_vote_features` | `0.873000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.662500` | `1.000000` |
| `no_budget_evidence_features` | `0.873000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `0.662500` | `1.000000` |
| `no_feedback_features` | `0.883000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `0.662500` | `1.000000` |
| `no_refusal_training` | `0.840500` | `0.875000` | `1.000000` | `0.875000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `0.662500` | `1.000000` |
| `no_heldout_council_split` | `0.731750` | `0.843750` | `0.000000` | `0.843750` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `0.654687` | `1.000000` |
| `no_trace_replay` | `0.905000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.687500` | `0.000000` |

## Learned policy objects

- `centroid_intent_router`: mean feature vector per intent trained on source-native ledger questions.
- `response_plan_selector`: predicted intent chooses which ledger fields may be cited.
- `heldout_council_split`: earlier councils train, later councils evaluate.
- `source_citation_gate`: answers count only when `source_native_original` ledger fields are present.
- `refusal_boundary_centroid`: trained refusal intent blocks consciousness/open-mind proof requests.

## Evidence and ablations

Removing the learned router drops readiness by `0.805000`. Removing source-native ledger features drops readiness by `0.229000`. Removing faction votes, budget evidence, feedback features, refusal training, held-out split, or replay traces produces targeted losses. This keeps the result bounded: the learned policy survives held-out council questions, but only inside the source-ledger task family.

## Artifacts

- `artifacts/ssrm_3d_learned_faction_dialogue_policy_bridge_eval.csv`
- `artifacts/ssrm_3d_learned_faction_dialogue_policy_bridge_verdict.csv`
- `artifacts/ssrm_3d_learned_faction_dialogue_policy_bridge_results.json`
- `artifacts/ssrm_3d_learned_faction_dialogue_policy_bridge_trace.json`
- `artifacts/ssrm_3d_learned_faction_dialogue_policy_bridge_state.json`
- `artifacts/ssrm_3d_learned_faction_dialogue_policy_bridge_results.js`
- `artifacts/ssrm_3d_learned_faction_dialogue_policy_bridge_trace.js`
- `artifacts/ssrm_3d_learned_faction_dialogue_policy_bridge_state.js`
- `visualizations/ssrm_3d_learned_faction_dialogue_policy_bridge.html`

## Verdict

The bridge passes as a learned faction-dialogue policy bridge because a deterministic trained policy predicts held-out council question intent, cites source-native ledger fields, preserves faction/budget/feedback/refusal/originality channels, and exposes targeted ablation losses.

The next gate is to move from a local centroid policy to a recurrent dialogue controller with persistent agent memory, turn-by-turn avatar interaction, and learned updates to faction state across live sessions.
