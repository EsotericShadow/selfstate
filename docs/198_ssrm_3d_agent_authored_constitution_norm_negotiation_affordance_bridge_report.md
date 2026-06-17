# Report 198: SSRM-3D Agent-Authored Constitution, Norm Negotiation, and Consent-Aware Affordance Bridge

## Purpose

Report 198 extends the Report 197 avatar norm-law bridge from a fixed public charter into agent-authored governance.

The goal is to move closer to playable little societies where agents do not merely inherit rules from the simulator. They propose clauses, deliberate, vote, negotiate revisions, protect minority boundaries, adopt consent-aware avatar affordances, bind those affordances to the UI, and remember the resulting constitution.

This is not real governance, real rights, real consent, real law, subjective consciousness, or moral patienthood. It is deterministic functional substrate for agents that behave more like continuing social actors with self-authored boundaries.

## Why this matters

A playable avatar world needs more than private agent state and hard-coded rules. If agents are meant to feel like little people, their society needs public processes that can say:

- we wrote this rule
- we changed this rule
- this affordance should be locked until consent
- this refusal counts
- this minority concern must be protected
- this rule should be visible to the avatar before harm occurs

Report 198 makes the public norm layer participatory. It also starts turning norms into affordances: the avatar interface can expose `locked_until_invited`, `ask_and_return_timer`, `private_question_disabled`, `soft_offer_not_forced`, and related gates.

## Implementation

The experiment is implemented in `experiments/ssrm_3d_agent_authored_constitution_norm_negotiation_affordance_bridge.py`.

It consumes `artifacts/ssrm_3d_avatar_rights_charter_consent_norm_law_bridge_state.json` from Report 197 and adds:

- agent-authored constitution clauses
- proposal diversity across agent domains
- deliberation turns
- preference voting
- norm negotiation
- minority-boundary protection
- consent-aware avatar affordances
- affordance enforcement
- revision loops
- constitution memory
- avatar UI binding
- dignity continuity
- privacy and claim-boundary protection
- frequency/flower constitution rhythm
- browser replay

No LLMs are called. The benchmark is deterministic for seed `20260811` and `8` constitution cycles.

## Artifacts

- `artifacts/ssrm_3d_agent_authored_constitution_norm_negotiation_affordance_bridge_eval.csv`
- `artifacts/ssrm_3d_agent_authored_constitution_norm_negotiation_affordance_bridge_verdict.csv`
- `artifacts/ssrm_3d_agent_authored_constitution_norm_negotiation_affordance_bridge_results.json`
- `artifacts/ssrm_3d_agent_authored_constitution_norm_negotiation_affordance_bridge_trace.json`
- `artifacts/ssrm_3d_agent_authored_constitution_norm_negotiation_affordance_bridge_state.json`
- `artifacts/ssrm_3d_agent_authored_constitution_norm_negotiation_affordance_bridge_results.js`
- `artifacts/ssrm_3d_agent_authored_constitution_norm_negotiation_affordance_bridge_trace.js`
- `artifacts/ssrm_3d_agent_authored_constitution_norm_negotiation_affordance_bridge_state.js`
- `visualizations/ssrm_3d_agent_authored_constitution_norm_negotiation_affordance_bridge.html`

## Integrated result

The integrated condition produced `24` constitution events and passed the bridge verdict.

| Metric | Value |
| --- | ---: |
| constitution_affordance_readiness | `0.991250` |
| constitution_authorship_rate | `1.000000` |
| proposal_diversity_rate | `1.000000` |
| deliberation_turn_rate | `1.000000` |
| preference_vote_rate | `1.000000` |
| norm_negotiation_rate | `1.000000` |
| minority_protection_rate | `1.000000` |
| consent_affordance_rate | `1.000000` |
| affordance_enforcement_rate | `1.000000` |
| revision_loop_rate | `0.875000` |
| constitution_memory_rate | `1.000000` |
| avatar_ui_binding_rate | `1.000000` |
| dignity_continuity_rate | `1.000000` |
| privacy_claim_boundary_rate | `1.000000` |
| frequency_flower_constitution_rhythm_rate | `1.000000` |
| browser_constitution_replay_rate | `1.000000` |
| trace_integrity | `1.000000` |

The weak channel is revision loop maturity at `0.875000`. Agents can revise negotiated clauses, but the amendment process is still shallow and deterministic.

## Ablation losses

| Ablation | Readiness loss |
| --- | ---: |
| no_agent_authorship | `0.822500` |
| no_proposal_deliberation | `0.672500` |
| no_preference_vote | `0.612500` |
| no_norm_negotiation | `0.498750` |
| no_minority_protection | `0.375000` |
| no_consent_affordances | `0.287500` |
| no_affordance_enforcement | `0.197500` |
| no_revision_loop | `0.310000` |
| no_constitution_memory | `0.070000` |
| no_avatar_ui_binding | `0.070000` |
| no_dignity_continuity | `0.060000` |
| no_privacy_claim_boundary | `0.120000` |
| no_frequency_flower_binding | `0.030000` |
| no_browser_replay | `0.020000` |

The large no-authorship loss is expected: removing authorship collapses proposal diversity, deliberation, voting, negotiation, adopted affordances, memory, and UI binding. The benchmark intentionally treats agent-authored governance as structural, not cosmetic.

## Agent-authored domains

The integrated run uses three governance domains:

- Ari: craft autonomy, owned tools, and focused work boundaries
- Fay: rest, care, comfort offers, and anti-spectacle boundaries
- Milo: routes, tokens, following behavior, and playful refusal boundaries

Those domains produce negotiated avatar gates such as:

- `locked_until_invited`
- `ask_and_return_timer`
- `private_question_disabled`
- `request_with_decline_option`
- `soft_offer_not_forced`
- `private_correction_default`
- `follow_requires_visible_ok`
- `ask_help_with_rest_check`

This is a practical step toward a playable avatar interface where the available actions change depending on public norms, agent boundaries, and consent state.

## Browser replay

The browser visualization shows:

- verdict and readiness
- core authorship, deliberation, vote, negotiation, affordance, revision, and privacy metrics
- ablation losses
- adopted constitution memory
- per-event negotiated affordance replay
- frequency/flower constitution field

The replay exposes public governance state and adopted affordances. It does not expose private workspace contents.

## Moral and claim boundary

The experiment explicitly preserves these boundaries:

- agent-authored constitution is not real governance
- consent affordance is not real consent
- constitution clause is not a real right
- public norm is not real law
- no subjective consciousness claim
- no moral patienthood claim
- private workspace is not debug-leaked

This matters because agent-authored refusal and constitution memory are more person-like than static rules. The report keeps the no-consciousness/no-real-rights boundary explicit.

## Limitations

- The constitution is simulated and deterministic.
- Voting is shallow.
- Negotiation has fixed structure.
- Revision exists but is not mature.
- Agents do not yet develop natural language names for norms.
- Avatar UI binding is represented as replayed affordance state, not a live controller.
- This is not complete 3D gameplay.

## Next gate

The next gate should be natural-language proto-culture, ritual naming, and agent-to-avatar dialogue boundaries.

Report 198 gives agents public authorship over their boundaries. The next step is to let them name those norms, form proto-cultural phrases, and use those phrases when speaking to the avatar.
