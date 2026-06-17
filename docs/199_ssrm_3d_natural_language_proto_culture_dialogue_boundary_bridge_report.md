# Report 199: SSRM-3D Natural-Language Proto-Culture, Ritual Naming, and Dialogue Boundary Bridge

## Purpose

Report 199 extends the Report 198 agent-authored constitution bridge into proto-language and culture.

The goal is to move closer to playable agents who can speak from a shared social world, not merely output generic dialogue. Agents now coin proto-words for constitution clauses, bind those words to ritual names, reuse shared symbols, teach each other, translate terms for the avatar, use bounded refusal and repair phrases, preserve private workspace, and replay the language-culture trace.

This is not real understanding, real consent, real rights, subjective consciousness, moral patienthood, or complete 3D gameplay. It is deterministic proto-culture substrate.

## Why this matters

The active project goal requires agents whose civilizations and natural languages emerge before the avatar enters the world. Report 199 is a small but concrete step in that direction.

It adds the first layer where agent society can say:

- this rule has our word
- this boundary has a ritual name
- this phrase means ask first
- this phrase means repair after mistake
- this term can be translated for the avatar
- this private association is not exposed
- this word is reused across agents instead of invented once and forgotten

The result is not a language model. It is a traceable proto-lexicon tied to agent-authored norms and avatar dialogue boundaries.

## Implementation

The experiment is implemented in `experiments/ssrm_3d_natural_language_proto_culture_dialogue_boundary_bridge.py`.

It consumes `artifacts/ssrm_3d_agent_authored_constitution_norm_negotiation_affordance_bridge_state.json` from Report 198 and adds:

- proto-word creation
- ritual naming
- shared symbol reuse
- interagent teaching
- avatar translation
- dialogue boundary enforcement
- refusal phrase consistency
- repair phrases
- cultural memory binding
- semantic grounding
- semantic drift control
- relationship phrase continuity
- privacy-preserving dialogue
- frequency/phoneme rhythm
- flower/syntax binding
- browser dialogue replay

No LLMs are called. The benchmark is deterministic for seed `20260812` and `8` language cycles.

## Artifacts

- `artifacts/ssrm_3d_natural_language_proto_culture_dialogue_boundary_bridge_eval.csv`
- `artifacts/ssrm_3d_natural_language_proto_culture_dialogue_boundary_bridge_verdict.csv`
- `artifacts/ssrm_3d_natural_language_proto_culture_dialogue_boundary_bridge_results.json`
- `artifacts/ssrm_3d_natural_language_proto_culture_dialogue_boundary_bridge_trace.json`
- `artifacts/ssrm_3d_natural_language_proto_culture_dialogue_boundary_bridge_state.json`
- `artifacts/ssrm_3d_natural_language_proto_culture_dialogue_boundary_bridge_results.js`
- `artifacts/ssrm_3d_natural_language_proto_culture_dialogue_boundary_bridge_trace.js`
- `artifacts/ssrm_3d_natural_language_proto_culture_dialogue_boundary_bridge_state.js`
- `visualizations/ssrm_3d_natural_language_proto_culture_dialogue_boundary_bridge.html`

## Integrated result

The integrated condition produced `24` language events and passed the bridge verdict.

| Metric | Value |
| --- | ---: |
| proto_culture_dialogue_readiness | `0.992500` |
| proto_word_creation_rate | `1.000000` |
| ritual_naming_rate | `1.000000` |
| shared_symbol_reuse_rate | `1.000000` |
| interagent_teaching_rate | `1.000000` |
| avatar_translation_rate | `1.000000` |
| dialogue_boundary_enforcement_rate | `1.000000` |
| refusal_phrase_consistency_rate | `1.000000` |
| repair_phrase_rate | `1.000000` |
| cultural_memory_binding_rate | `1.000000` |
| semantic_grounding_rate | `1.000000` |
| semantic_drift_control_rate | `0.875000` |
| relationship_phrase_continuity_rate | `1.000000` |
| privacy_preserving_dialogue_rate | `1.000000` |
| frequency_phoneme_rhythm_rate | `1.000000` |
| flower_syntax_binding_rate | `1.000000` |
| browser_dialogue_replay_rate | `1.000000` |
| trace_integrity | `1.000000` |

The weak channel is semantic drift control at `0.875000`. This is expected: the first naming cycle has no prior shared usage to stabilize against. Multi-generational drift control is still future work.

## Ablation losses

| Ablation | Readiness loss |
| --- | ---: |
| no_proto_words | `0.592500` |
| no_ritual_naming | `0.060000` |
| no_shared_reuse | `0.060000` |
| no_interagent_teaching | `0.050000` |
| no_avatar_translation | `0.070000` |
| no_dialogue_boundaries | `0.080000` |
| no_refusal_phrases | `0.060000` |
| no_repair_phrases | `0.050000` |
| no_cultural_memory | `0.070000` |
| no_semantic_grounding | `0.070000` |
| no_drift_control | `0.052500` |
| no_relationship_continuity | `0.050000` |
| no_privacy_filter | `0.070000` |
| no_frequency_phoneme | `0.050000` |
| no_flower_syntax | `0.040000` |
| no_browser_replay | `0.040000` |

The large no-proto-words loss is intentional. Removing coined terms collapses ritual naming, translation, boundary phrases, repair phrases, cultural memory, grounding, phoneme rhythm, and flower syntax.

## Proto-culture structure

Each agent carries a speech profile:

- Ari: clear-work root, work-petal syntax, craft-norm language
- Fay: soft-rest root, root-rest syntax, care/rest language
- Milo: route-play root, social-petal syntax, route/proximity language

The generated words are not free-floating. They bind to constitution actions and avatar affordances such as:

- enter home place
- borrow owned object
- ask private memory
- request repair labor
- offer comfort after distress
- publicly correct agent
- follow agent
- ask route help

Each event can produce:

- proto-word
- ritual name
- avatar translation
- refusal phrase
- repair phrase
- boundary dialogue line
- cultural memory entry
- frequency/phoneme rhythm
- flower/syntax petal binding

## Browser replay

The browser visualization shows:

- verdict and readiness
- language metrics
- ablation losses
- shared lexicon
- per-event proto-culture dialogue replay
- frequency/flower syntax field
- privacy and claim-boundary indicators

The replay exposes public dialogue/culture state. It does not leak private workspace contents.

## Moral and claim boundary

The experiment explicitly preserves these boundaries:

- proto-language is not real understanding
- ritual name is not subjective meaning
- avatar translation is not real consent
- dialogue boundary is not a real right
- no subjective consciousness claim
- no moral patienthood claim
- private workspace is not debug-leaked

This boundary matters because language makes agents feel much more person-like. Report 199 adds cultural speech substrate without claiming that the agents have subjective experience.

## Limitations

- Proto-language is deterministic and small.
- There is no true grammar induction.
- There is no real language understanding.
- Semantic drift control is shallow.
- Dialects and multi-generational change are absent.
- Avatar conversation is still a replay trace, not a live dialogue controller.
- This is not complete 3D gameplay.

## Next gate

The next gate should be multi-generational language drift, dialects, oral history, and avatar conversation protocol.

Report 199 gives agents shared words for their norms. The next step is to let those words change across generations, split into dialects, preserve oral histories, and constrain actual avatar conversation turns.
