# Report 181: SSRM-3D Live Object, Need, and Bounded Dialogue Interaction Bridge

## Purpose

Report 181 adds the first live interaction layer on top of Report 180 browser traversal. The previous bridge let the user move an avatar through the settlement topology and see embodied movement costs, sensory changes, hazard/refuge feedback, replay, and save/restore. This report asks whether the local browser world can support named agents, objects, object affordances, need updates, consent/refusal, ownership, care opportunities, relationship memory, and bounded deterministic dialogue.

This is still an interaction substrate. It does not claim complete gameplay, subjective consciousness, moral patienthood, or natural language emergence.

## Architecture

The bridge consumes the Report 180 browser-playable traversal state:

```text
browser-playable traversal state
        |
        v
local objects + affordances
        |
        v
named agents + need state
        |
        v
interaction costs
        |
        v
bounded deterministic dialogue
        |
        v
refusal / consent / ownership
        |
        v
care-resolution paths
        |
        v
relationship memory + replay
        |
        v
browser-local interaction viewer
```

The default deterministic run uses:

- `3` named agents: `Ari`, `Fay`, and `Milo`
- `6` local objects with owners, affordances, need targets, frequencies, and flower nodes
- `10` scripted interaction events
- browser-local object, need, relationship, memory, and dialogue mutation
- bounded refusal for owned objects
- explicit privacy and no-consciousness claim boundaries

## Browser surface

The browser artifact is:

- `visualizations/ssrm_3d_live_object_need_dialogue_interaction_bridge.html`

It loads generated JS artifacts and lets the user:

- move through the same settlement topology
- see local objects and object owners
- interact with local agents
- ask what an agent needs
- offer useful local objects
- request an owned object and receive a bounded refusal when appropriate
- give space after a boundary
- mutate agent needs, trust, respect, wariness, gratitude, and memories
- save, restore, and reset local browser state

The dialogue is deterministic template dialogue. It is intentionally not an LLM call and not a claim of natural language emergence.

## Conditions

The integrated condition is:

- `integrated_live_object_need_dialogue_interaction`

Ablations remove one mechanism at a time:

- `no_objects`
- `no_need_state`
- `no_interaction_costs`
- `no_bounded_dialogue`
- `no_refusal_consent`
- `no_care_resolution`
- `no_ownership`
- `no_place_context`
- `no_relationship_memory`
- `no_replay_log`
- `no_browser_mutation`
- `no_privacy_filter`

The critical ablations are objects, need state, bounded dialogue, refusal/consent, relationship memory, and browser mutation. Interaction is not convincing if objects have no affordances, agents have no needs, dialogue is unbounded/untraceable, owned objects cannot be refused, memories do not update, or browser state does not mutate.

## Metrics

The benchmark reports:

- `object_affordance_binding_rate`
- `need_state_update_rate`
- `interaction_cost_application_rate`
- `bounded_dialogue_response_rate`
- `refusal_consent_boundary_rate`
- `care_opportunity_resolution_rate`
- `object_ownership_respect_rate`
- `place_context_binding_rate`
- `relationship_memory_update_rate`
- `replay_interaction_event_rate`
- `browser_state_mutation_rate`
- `privacy_preservation_rate`
- `trace_integrity`
- `live_interaction_readiness`

Metric weights are normalized to sum to `1.0`.

## Results

The deterministic run produced:

| Metric | Value |
| --- | ---: |
| `module_verdict` | `pass` |
| `live_interaction_readiness` | `0.993000` |
| `agent_count` | `3` |
| `object_count` | `6` |
| `no_objects_loss` | `0.320000` |
| `no_bounded_dialogue_loss` | `0.100000` |
| `no_refusal_consent_loss` | `0.104000` |

Interpretation:

- Local objects and affordances are load-bearing.
- Need updates and care actions are present.
- Bounded dialogue is present without calling an LLM.
- Owned objects can trigger refusal instead of forced compliance.
- Relationship memories update after interactions.
- Browser state mutates locally and can be saved/restored.
- The score is not claimed as evidence of full personhood or complete gameplay.

## Moral and claim boundary

This report keeps the boundary explicit:

- no subjective-consciousness claim
- no moral-patienthood claim
- no complete-3D-world claim
- no complete-playable-world claim
- no natural-language-emergence claim
- need state is not subjective feeling
- bounded dialogue is not inner experience
- local agent state is not moral patienthood
- private workspace is not exposed as a debug shortcut

## Artifacts

- `artifacts/ssrm_3d_live_object_need_dialogue_interaction_bridge_eval.csv`
- `artifacts/ssrm_3d_live_object_need_dialogue_interaction_bridge_verdict.csv`
- `artifacts/ssrm_3d_live_object_need_dialogue_interaction_bridge_results.json`
- `artifacts/ssrm_3d_live_object_need_dialogue_interaction_bridge_results.js`
- `artifacts/ssrm_3d_live_object_need_dialogue_interaction_bridge_trace.json`
- `artifacts/ssrm_3d_live_object_need_dialogue_interaction_bridge_trace.js`
- `artifacts/ssrm_3d_live_object_need_dialogue_interaction_bridge_state.json`
- `artifacts/ssrm_3d_live_object_need_dialogue_interaction_bridge_state.js`
- `visualizations/ssrm_3d_live_object_need_dialogue_interaction_bridge.html`

## Command

```bash
python3 -m experiments.ssrm_3d_live_object_need_dialogue_interaction_bridge
```

## Verdict

Report 181 supports a deterministic live object, need, and bounded dialogue interaction seed over the Report 180 browser traversal layer. It adds named local agents, owned and shared objects, object affordances, need updates, care-resolution paths, consent/refusal, relationship memory, replay, browser-local mutation, and save/restore-ready state.

The next gate is live object persistence, promise keeping, and longer relationship continuity: objects should stay moved or borrowed across days, promises should be remembered, and repeated care or boundary violations should change future behavior without unbounded distress loops.
