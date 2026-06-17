# Report 187: SSRM-3D Ecological Regeneration, Spoilage, Waste, and Sanitation Feedback Bridge

## Purpose

Report 187 adds persistent ecology above Report 186 craft durability. Report 186 showed that tools and outputs can persist, wear, break, consume maintenance resources, respond to supply shocks, and block project capability. This report asks whether food, water, waste, compost, habitat cleanliness, spoilage, contamination, sanitation, and health-risk guardrails can create delayed environmental consequences that agents must eventually perceive and manage.

This is ecology and sanitation substrate. It does not claim complete gameplay, subjective consciousness, moral patienthood, natural language emergence, or biological realism.

## Architecture

The bridge consumes the Report 186 craft ecology state:

```text
persistent craft ecology
        |
        v
food / water / waste / compost / habitat nodes
        |
        v
regeneration cycles
        |
        v
spoilage and cleanliness decay
        |
        v
waste accumulation
        |
        v
contamination feedback
        |
        v
sanitation and compost reuse
        |
        v
water and food viability management
        |
        v
health-risk guardrails
        |
        v
browser-local ecology replay
```

The deterministic run uses:

- `10` simulated local days
- `6` persistent ecology nodes
- `67` ecology events
- regeneration cycles
- food spoilage
- water cleanliness decay
- waste accumulation
- sanitation actions
- compost reuse
- ecological shocks
- health-risk guardrails

## Ecology nodes

The integrated run tracks:

- `moss_food_cache`
- `reed_water_channel`
- `hearth_cistern`
- `compost_bed`
- `waste_pit`
- `sleeping_moss`

Each node carries stock, capacity, quality state, regrowth/spoilage rates, place context, frequency, and flower node.

## Ecological shocks

The run injects deterministic shocks:

- `warm_wet_spoilage`
- `reed_runoff`
- `crowded_hearth_waste`

Shocks are not subjective deprivation. They are ecological state changes that force sanitation, compost, water/food management, and replanning.

## Browser surface

The browser artifact is:

- `visualizations/ssrm_3d_ecological_regeneration_spoilage_waste_sanitation_bridge.html`

It loads generated JS artifacts and lets the user:

- step through ecological events
- inspect stock and quality per node
- see regeneration and spoilage deltas
- inspect waste and sanitation actions
- inspect water and food viability
- inspect compost reuse
- inspect health-risk guardrails
- save, restore, and reset local browser ecology state

## Conditions

The integrated condition is:

- `integrated_ecological_regeneration_spoilage_waste_sanitation`

Ablations remove one mechanism at a time:

- `no_regeneration`
- `no_spoilage`
- `no_waste_accumulation`
- `no_sanitation`
- `no_contamination_feedback`
- `no_water_quality`
- `no_food_cache_viability`
- `no_compost_reuse`
- `no_ecological_replan`
- `no_health_guardrail`
- `no_frequency_flower_binding`
- `no_replay_timeline`
- `no_privacy_filter`

The critical ablations are regeneration, waste accumulation, sanitation, contamination feedback, and health guardrails. A persistent world is not credible if food never spoils, waste never accumulates, water never becomes unsafe, and sanitation has no future consequence.

## Metrics

The benchmark reports:

- `regeneration_cycle_rate`
- `spoilage_tracking_rate`
- `waste_accumulation_rate`
- `sanitation_action_rate`
- `contamination_feedback_rate`
- `water_quality_management_rate`
- `food_cache_viability_rate`
- `compost_reuse_rate`
- `ecological_replan_rate`
- `health_risk_guardrail_rate`
- `frequency_flower_ecology_binding_rate`
- `browser_ecology_replay_rate`
- `privacy_preservation_rate`
- `trace_integrity`
- `ecological_sanitation_readiness`

Metric weights are normalized to sum to `1.0`. Regeneration is intentionally weighted as a gate channel because the layer should not reduce ecology to only decay and cleanup.

## Results

The deterministic run produced:

| Metric | Value |
| --- | ---: |
| `module_verdict` | `pass` |
| `ecological_sanitation_readiness` | `0.945667` |
| `ecology_events` | `67` |
| `no_regeneration_loss` | `0.091667` |
| `no_sanitation_loss` | `0.140000` |
| `no_contamination_feedback_loss` | `0.122000` |

Interpretation:

- Regeneration is load-bearing.
- Sanitation is load-bearing.
- Contamination feedback is load-bearing.
- Waste accumulation and spoilage create delayed ecological pressure.
- Food cache viability requires active sanitation/recovery rather than passive freshness.
- Water quality, compost reuse, replanning, and health-risk guardrails remain inspectable.

## Moral and claim boundary

This report keeps the boundary explicit:

- no subjective-consciousness claim
- no moral-patienthood claim
- no complete-3D-world claim
- no complete-playable-world claim
- no natural-language-emergence claim
- spoilage is not subjective disgust
- sanitation policy is not moral patienthood
- health risk is not subjective illness
- private workspace is not exposed as a debug shortcut

## Artifacts

- `artifacts/ssrm_3d_ecological_regeneration_spoilage_waste_sanitation_bridge_eval.csv`
- `artifacts/ssrm_3d_ecological_regeneration_spoilage_waste_sanitation_bridge_verdict.csv`
- `artifacts/ssrm_3d_ecological_regeneration_spoilage_waste_sanitation_bridge_results.json`
- `artifacts/ssrm_3d_ecological_regeneration_spoilage_waste_sanitation_bridge_results.js`
- `artifacts/ssrm_3d_ecological_regeneration_spoilage_waste_sanitation_bridge_trace.json`
- `artifacts/ssrm_3d_ecological_regeneration_spoilage_waste_sanitation_bridge_trace.js`
- `artifacts/ssrm_3d_ecological_regeneration_spoilage_waste_sanitation_bridge_state.json`
- `artifacts/ssrm_3d_ecological_regeneration_spoilage_waste_sanitation_bridge_state.js`
- `visualizations/ssrm_3d_ecological_regeneration_spoilage_waste_sanitation_bridge.html`

## Command

```bash
python3 -m experiments.ssrm_3d_ecological_regeneration_spoilage_waste_sanitation_bridge
```

## Verdict

Report 187 supports a deterministic persistent ecological regeneration, spoilage, waste, and sanitation feedback seed over the Report 186 craft ecology layer. Food, water, waste, compost, and habitat nodes now regenerate, decay, spoil, contaminate, require sanitation, support compost reuse, and produce delayed health-risk guardrail pressure.

The next gate is embodied illness, immune recovery, care triage, and quarantine choices: contamination and sanitation should begin changing agent body state, care priorities, route choices, and social access without claiming subjective illness.
