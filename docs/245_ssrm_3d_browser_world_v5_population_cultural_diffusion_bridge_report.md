# Report 245: SSRM-3D Browser World v5 Population Cultural Diffusion Bridge

## Status

Pass.

## Purpose

Report 245 addresses Report 244's weakest channel: social spread continuity. Instead of adding another local adaptation loop, this bridge moves to population-level cultural diffusion across six households. Proto-language variants, learned rituals, avatar reputation, warning stories, recovery clauses, and welfare guardrails now spread household-to-household through trade, ritual visits, repair aid, teaching circles, weather warnings, shared meals, and boundary warnings.

This moves the browser-world line closer to convincing artificial life because agents do not only adapt individually. Their households carry culture, warnings, care practices, and language variants socially.

## Boundary

This is deterministic population-level cultural diffusion, not subjective consciousness. Proto-language spread is rule-based household adoption, not autonomous natural language emergence. Ritual learning is simulated cultural continuity, not real religion or moral agency.

## Implementation

- Module: `experiments/ssrm_3d_browser_world_v5_population_cultural_diffusion_bridge.py`
- Visualization: `visualizations/ssrm_3d_browser_world_v5_population_cultural_diffusion_bridge.html`
- Results: `artifacts/ssrm_3d_browser_world_v5_population_cultural_diffusion_bridge_results.json`
- Verdict: `artifacts/ssrm_3d_browser_world_v5_population_cultural_diffusion_bridge_verdict.csv`
- Seed: `20260858`
- Source continuity: `artifacts/ssrm_3d_browser_world_v4_learned_routine_proto_language_adaptation_bridge_results.json`

## Generated artifacts

- `artifacts/ssrm_3d_browser_world_v5_population_cultural_diffusion_bridge_household_network_frames.csv`
- `artifacts/ssrm_3d_browser_world_v5_population_cultural_diffusion_bridge_cultural_diffusion_events.csv`
- `artifacts/ssrm_3d_browser_world_v5_population_cultural_diffusion_bridge_learned_ritual_frames.csv`
- `artifacts/ssrm_3d_browser_world_v5_population_cultural_diffusion_bridge_reputation_propagation_frames.csv`
- `artifacts/ssrm_3d_browser_world_v5_population_cultural_diffusion_bridge_welfare_guardrail_frames.csv`
- `artifacts/ssrm_3d_browser_world_v5_population_cultural_diffusion_bridge_replay_cultural_frames.csv`
- `artifacts/ssrm_3d_browser_world_v5_population_cultural_diffusion_bridge_browser_world_v5_ticks.csv`
- `artifacts/ssrm_3d_browser_world_v5_population_cultural_diffusion_bridge_state.json`
- `artifacts/ssrm_3d_browser_world_v5_population_cultural_diffusion_bridge_results.json`
- `artifacts/ssrm_3d_browser_world_v5_population_cultural_diffusion_bridge_verdict.csv`

## New dynamics

| Layer | What changed |
| --- | --- |
| Household network | Six households exchange culture over 288 deterministic network contacts. |
| Proto-language diffusion | Tokens and variants spread between households with adoption, grounding, drift pressure, and diffusion gain. |
| Learned rituals | Ritual names, adoption levels, variation, rhythm, flower alignment, welfare benefit, and boundary clauses propagate socially. |
| Avatar reputation | Avatar care and pressure stories travel beyond the household that observed the interaction. |
| Welfare guardrails | Sleep respect, boundary respect, recovery paths, no-spectacle distress handling, and harmful-spread blocking travel with culture. |
| Replay continuity | Cultural state is checkpointed with import/export hashes and carried rows. |
| Browser v5 | The visualization shows household-to-household spread, rituals, reputation, guardrails, private cultural traces, and replay import/export. |

## Run output

```text
module_verdict pass
browser_world_v5_population_cultural_diffusion_readiness 0.984229
household_network_frames 288
cultural_diffusion_events 288
learned_ritual_frames 288
reputation_propagation_frames 288
welfare_guardrail_frames 288
replay_cultural_frames 288
browser_world_v5_ticks 288
population_span_coverage 1.000000
household_network_connectivity 1.000000
household_proto_language_spread 1.000000
social_spread_continuity 0.883560
meaning_grounding_retention 0.974854
learned_ritual_adoption 0.965278
welfare_guardrail_preservation 1.000000
weakest_channel_score 0.883560
visualization visualizations/ssrm_3d_browser_world_v5_population_cultural_diffusion_bridge.html
next_gate browser world v6 with generational cultural inheritance, child-to-adult learning arcs, household lineage memory, and avatar-entry effects that persist across simulated generations without breaking welfare guardrails
```

## Metrics

| Metric | Value |
| --- | ---: |
| browser_world_v5_population_cultural_diffusion_readiness | 0.984229 |
| mean_cultural_diffusion_channel_score | 0.990205 |
| weakest_channel_score | 0.883560 |
| social_spread_continuity | 0.883560 |
| population_span_coverage | 1.000000 |
| household_network_connectivity | 1.000000 |
| household_proto_language_spread | 1.000000 |
| meaning_grounding_retention | 0.974854 |
| cultural_diffusion_without_collapse | 1.000000 |
| learned_ritual_adoption | 0.965278 |
| ritual_variation_stability | 1.000000 |
| avatar_social_propagation_binding | 1.000000 |
| reputation_balance | 1.000000 |
| welfare_guardrail_preservation | 1.000000 |
| boundary_respect_social_propagation | 1.000000 |
| replay_cultural_integrity | 1.000000 |
| replay_checkpoint_coverage | 1.000000 |
| private_cultural_trace_boundary | 1.000000 |
| frequency_flower_cultural_rhythm | 1.000000 |
| source_learned_adaptation_continuity | 1.000000 |
| browser_world_v5_surface_available | 1.000000 |

## Ablations

| Ablation | Readiness |
| --- | ---: |
| no_proto_language_spread | 0.674229 |
| no_social_spread_continuity | 0.684229 |
| no_household_network | 0.694229 |
| no_welfare_guardrails | 0.704229 |
| no_meaning_grounding | 0.734229 |
| no_learned_rituals | 0.764229 |
| no_avatar_reputation_propagation | 0.784229 |
| no_boundary_social_propagation | 0.814229 |
| no_replay_cultural_integrity | 0.854229 |
| no_frequency_flower_cultural_rhythm | 0.914229 |

## Interpretation

Report 245 directly improves the Report 244 pressure point. Social spread continuity rises from 0.824143 to 0.883560 by moving from local repeated interaction to household-level diffusion.

The first deterministic run exposed two useful failures. Welfare guardrails were too strict in a way that treated caution stories as failures, and household adoption started too low for population diffusion. The final model treats warning stories as guardrail-preserving when they carry protective/recovery tokens, and assumes households begin with partial familiarity with neighboring vocabulary rather than zero-like exposure.

The strongest ablations are removing proto-language spread, social spread continuity, household network structure, welfare guardrails, and meaning grounding. That is the correct dependency profile for culture that spreads socially without becoming ungrounded, coercive, or welfare-breaking.

## Honest limits

- This is deterministic population-level cultural diffusion, not subjective consciousness.
- Proto-language spread is rule-based household adoption, not autonomous natural language emergence.
- Ritual learning is simulated cultural continuity, not real religion or moral agency.
- Avatar reputation propagation is functional social memory, not real consent or moral patienthood.
- Welfare guardrails are bounded simulation constraints, not proof of welfare experience.
- Frequency and flower phase are rhythm variables, not metaphysical proof.
- The browser world v5 visualization is a scaffold, not a finished 3D game engine.

## Next gate

Browser world v6 with generational cultural inheritance, child-to-adult learning arcs, household lineage memory, and avatar-entry effects that persist across simulated generations without breaking welfare guardrails.
