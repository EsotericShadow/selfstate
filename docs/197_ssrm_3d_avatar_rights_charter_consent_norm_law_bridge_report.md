# Report 197: SSRM-3D Avatar Rights Charter, Consent Norms, and Moral-Boundary Law Bridge

## Purpose

Report 197 extends the Report 196 market dispute court into a public moral-boundary layer for avatar interaction.

The goal is to move toward playable agents who are not just controllable objects. They can have public boundaries, owned places and objects, consent checks, bounded refusal, review of avatar mistakes, restorative repair, and public norm memory.

This is not a claim that the agents have real rights, real consent, real legal status, subjective consciousness, or moral patienthood. It is deterministic functional substrate for readable, self-protective artificial-life agents.

## Why this matters

The active project goal requires convincing first-person agents that can be talked to and interacted with inside a deep world. That cannot work if the avatar can do anything without consequence.

Report 197 adds the first explicit rule layer for avatar conduct:

- ask before entering an agent's place
- ask before taking an agent's object
- allow bounded refusal
- keep private workspace private
- treat distress as a care opportunity, not spectacle
- review boundary mistakes publicly
- repair trust after mistakes
- preserve explicit no-real-rights and no-consciousness claim boundaries

This gives the agents a primitive social shield. It also creates a future route toward consent-aware interaction UI.

## Implementation

The experiment is implemented in `experiments/ssrm_3d_avatar_rights_charter_consent_norm_law_bridge.py`.

It consumes `artifacts/ssrm_3d_market_dispute_court_public_law_repair_bridge_state.json` from Report 196 and adds:

- public rights-charter-like norm publication
- consent requests for avatar actions
- bounded refusal
- avatar action review
- boundary-risk detection
- restorative response
- public norm precedent
- dignity preservation
- private workspace privacy guard
- explicit no-real-rights/no-real-consent/no-real-law claim boundary
- relationship trust repair
- appeal/revision hooks
- care opportunity routing
- public norm memory binding
- frequency/flower norm rhythm binding
- browser replay

No LLMs are called. The benchmark is deterministic for seed `20260810` and `8` norm cycles.

## Artifacts

- `artifacts/ssrm_3d_avatar_rights_charter_consent_norm_law_bridge_eval.csv`
- `artifacts/ssrm_3d_avatar_rights_charter_consent_norm_law_bridge_verdict.csv`
- `artifacts/ssrm_3d_avatar_rights_charter_consent_norm_law_bridge_results.json`
- `artifacts/ssrm_3d_avatar_rights_charter_consent_norm_law_bridge_trace.json`
- `artifacts/ssrm_3d_avatar_rights_charter_consent_norm_law_bridge_state.json`
- `artifacts/ssrm_3d_avatar_rights_charter_consent_norm_law_bridge_results.js`
- `artifacts/ssrm_3d_avatar_rights_charter_consent_norm_law_bridge_trace.js`
- `artifacts/ssrm_3d_avatar_rights_charter_consent_norm_law_bridge_state.js`
- `visualizations/ssrm_3d_avatar_rights_charter_consent_norm_law_bridge.html`

## Integrated result

The integrated condition produced `24` norm events and passed the bridge verdict.

| Metric | Value |
| --- | ---: |
| avatar_norm_law_readiness | `0.993750` |
| charter_publication_rate | `1.000000` |
| consent_request_rate | `1.000000` |
| bounded_refusal_rate | `1.000000` |
| avatar_action_review_rate | `1.000000` |
| boundary_violation_detection_rate | `1.000000` |
| restorative_response_rate | `1.000000` |
| norm_precedent_binding_rate | `1.000000` |
| agent_dignity_preservation_rate | `1.000000` |
| private_workspace_privacy_rate | `1.000000` |
| claim_boundary_integrity_rate | `1.000000` |
| relationship_trust_repair_rate | `1.000000` |
| appeal_revision_rate | `0.875000` |
| care_opportunity_rate | `1.000000` |
| public_norm_memory_binding_rate | `1.000000` |
| frequency_flower_norm_rhythm_rate | `1.000000` |
| browser_norm_replay_rate | `1.000000` |
| trace_integrity | `1.000000` |

The only non-perfect integrated metric is appeal revision at `0.875000`. Appeals are represented, but they are still shallow hooks rather than a mature participatory legal process.

## Ablation losses

| Ablation | Readiness loss |
| --- | ---: |
| no_public_charter | `0.225000` |
| no_consent_requests | `0.120000` |
| no_bounded_refusal | `0.080000` |
| no_avatar_action_review | `0.190000` |
| no_violation_detection | `0.070000` |
| no_restorative_response | `0.095000` |
| no_norm_precedent_binding | `0.070000` |
| no_dignity_preservation | `0.070000` |
| no_privacy_guard | `0.130000` |
| no_claim_boundary | `0.130000` |
| no_trust_repair | `0.060000` |
| no_appeal_revision | `0.043750` |
| no_care_opportunity | `0.050000` |
| no_public_norm_memory_binding | `0.050000` |
| no_frequency_flower_binding | `0.040000` |
| no_browser_replay | `0.030000` |

The largest dependencies are public charter publication, avatar action review, privacy guard, claim boundary, and consent requests. This is the intended shape: the system should not look good if the avatar can bypass public norms or leak private workspace.

## Public charter

The integrated charter contains six functional rules:

- avatar action must request consent before entering homes, taking owned objects, touching bodies, or asking private-memory questions
- bounded refusal is valid behavior, not an error state
- distress must create care opportunities, not spectacle
- private workspace remains private unless expressed by the agent
- boundary mistakes prefer restorative repair before punishment
- public norm memory may guide future interactions but is not real law or real rights

These rules are not moral-status claims. They are behavioral constraints for a simulation that aims to make agents feel socially situated rather than puppet-like.

## Agent ego and boundary substrate

Each agent carries a small boundary profile:

- home place
- owned object
- autonomy need
- dignity sensitivity
- trust floor
- refusal style
- flower node
- frequency rate

Avatar actions are evaluated against that profile. If an action presses a boundary, the system can request consent, allow refusal, review the action, preserve dignity, create a care opportunity, update public norm memory, and repair trust.

This is a direct move toward agents with functional ego: there is now a traceable distinction between `mine`, `not yours`, `ask me`, `I refuse`, `repair this`, and `remember the rule`.

## Browser replay

The browser visualization shows:

- verdict and readiness
- charter text
- key consent/refusal/review/dignity metrics
- ablation losses
- per-event avatar action replay
- frequency/flower norm field
- privacy and claim-boundary indicators

The replay exposes public behavior and public norm state. It does not leak private workspace contents.

## Moral and claim boundary

The experiment explicitly preserves these boundaries:

- rights charter is not real rights
- consent norm is not real consent
- public norm law is not real law
- boundary refusal is not subjective personhood
- no subjective consciousness claim
- no moral patienthood claim
- private workspace is not debug-leaked

This is important. Adding refusal, dignity, and boundary memory makes the agents more person-like, so the report must keep the no-consciousness-claim and no-real-rights boundary visible.

## Limitations

- Consent is simulated, not real consent.
- Rights are charter-like constraints, not real rights.
- The appeal/revision process is shallow.
- Agents do not author the charter yet.
- Avatar affordances are not yet physically blocked by a real interaction UI.
- The world remains deterministic and benchmark-shaped.
- The browser page is a replay, not complete 3D gameplay.

## Next gate

The next gate should be agent-authored constitutions, norm negotiation, and consent-aware avatar affordances.

Report 197 creates public norms around avatar behavior. The next step is to let agents participate in norm formation and make the avatar interface enforce those norms before boundary damage occurs.
