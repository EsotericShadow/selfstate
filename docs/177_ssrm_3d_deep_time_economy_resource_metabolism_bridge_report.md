# Report 177: SSRM-3D Deep-Time Economy and Resource Metabolism Bridge

## Purpose

Report 177 adds resource metabolism to the deep-time stack. Report 176 attached cultural symbols to tools, materials, affordances, repair protocols, costs, and technology lineages. This report asks whether those tools draw from finite resources, create waste, require maintenance, respond to scarcity, exchange between groups, and generate ecological pressure over compressed deep time.

This is still a seed layer. It does not claim full civilization, subjective consciousness, or moral patienthood.

## Architecture

The bridge consumes the Report 176 tool ecology state and creates a deterministic resource economy:

```text
deep-time tool ecology
        |
        v
tool resource costs + maintenance wear
        |
        v
resource stocks and extraction
        |
        v
regeneration + waste streams
        |
        v
scarcity feedback + safety reserves
        |
        v
intergroup exchange + ecological pressure
        |
        v
frequency metabolism + economy hashes
```

The default run simulates:

- `12` eras
- `200` generations per era
- `2400` total simulated years
- `3` groups
- `10` resource classes

## Resource classes

The model tracks:

- `wood`
- `stone`
- `fiber`
- `clay`
- `metal_seed`
- `glass_reed`
- `soft_moss`
- `water`
- `food`
- `heat`

Each group carries:

- stocks
- extraction
- maintenance use
- regeneration
- waste stock
- scarcity actions
- exchange ledger
- ecological pressure
- frequency metabolism
- safety reserve status

## Conditions

The integrated condition is:

- `integrated_deep_time_economy_resource_metabolism`

Ablations remove one mechanism at a time:

- `no_resource_stocks`
- `no_extraction_costs`
- `no_regeneration`
- `no_waste_streams`
- `no_maintenance_metabolism`
- `no_scarcity_feedback`
- `no_exchange_network`
- `no_ecological_pressure`
- `no_cultural_value_binding`
- `no_safety_reserve`
- `no_frequency_metabolism`
- `no_privacy_filter`

The critical ablations are resource stocks, extraction costs, and scarcity feedback. A long-lived society cannot be credible if resources never deplete, tool use costs nothing, or scarcity does not feed back into behavior.

## Metrics

The benchmark reports:

- `resource_stock_accounting_rate`
- `extraction_cost_binding_rate`
- `regeneration_balance_rate`
- `waste_stream_tracking_rate`
- `maintenance_load_rate`
- `scarcity_feedback_rate`
- `intergroup_exchange_rate`
- `ecological_pressure_rate`
- `cultural_value_binding_rate`
- `safety_reserve_rate`
- `frequency_metabolism_rate`
- `bounded_depletion_rate`
- `deep_time_continuity_rate`
- `privacy_preservation_rate`
- `trace_integrity`
- `no_civilization_or_consciousness_claim_rate`
- `deep_time_economy_resource_metabolism_readiness`

Metric weights are normalized to sum to `1.0`.

## Results

The deterministic run produced:

| Metric | Value |
| --- | ---: |
| `module_verdict` | `pass` |
| `deep_time_economy_resource_metabolism_readiness` | `0.960000` |
| `simulated_years` | `2400` |
| `no_resource_stocks_loss` | `0.150000` |
| `no_extraction_costs_loss` | `0.080000` |
| `no_scarcity_feedback_loss` | `0.080000` |

Interpretation:

- The bridge supports a deterministic resource metabolism seed over deep time.
- Resource stocks are strongly load-bearing.
- Extraction costs are load-bearing.
- Scarcity feedback is load-bearing after correction.
- Regeneration, waste streams, safety reserves, ecological pressure, maintenance, and frequency metabolism are all represented in the trace.

## Correction during development

The first local draft failed. Integrated readiness was `0.900000`, but scarcity feedback was too intermittent: it only fired when reserves were already threatened. The published benchmark changes scarcity feedback into a continuous reserve-monitoring loop, with rationing only when needed. That makes scarcity an active control channel rather than an emergency afterthought.

## Moral boundary

This report keeps the boundary explicit:

- no subjective-consciousness claim
- no moral-patienthood claim
- no full-civilization claim
- scarcity must feed back into resource behavior
- safety reserves must protect water, food, and heat
- private workspace is not exposed as a debug shortcut

## Artifacts

- `artifacts/ssrm_3d_deep_time_economy_resource_metabolism_bridge_eval.csv`
- `artifacts/ssrm_3d_deep_time_economy_resource_metabolism_bridge_verdict.csv`
- `artifacts/ssrm_3d_deep_time_economy_resource_metabolism_bridge_results.json`
- `artifacts/ssrm_3d_deep_time_economy_resource_metabolism_bridge_results.js`
- `artifacts/ssrm_3d_deep_time_economy_resource_metabolism_bridge_trace.json`
- `artifacts/ssrm_3d_deep_time_economy_resource_metabolism_bridge_trace.js`
- `artifacts/ssrm_3d_deep_time_economy_resource_metabolism_bridge_state.json`
- `artifacts/ssrm_3d_deep_time_economy_resource_metabolism_bridge_state.js`
- `visualizations/ssrm_3d_deep_time_economy_resource_metabolism_bridge.html`

## Command

```bash
python3 -m experiments.ssrm_3d_deep_time_economy_resource_metabolism_bridge
```

## Verdict

Report 177 supports a deterministic deep-time economy and resource metabolism seed bridge over `2400` simulated years. It binds tool use to resource stocks, extraction costs, regeneration, waste streams, maintenance, scarcity feedback, intergroup exchange, ecological pressure, safety reserves, frequency metabolism, privacy, and economy trace hashes.

The next gate is deep-time habitat, climate, and multisensory world metabolism seeds: resources should be embedded in weather, terrain, smell, sound, wetness, temperature, seasonal risk, and place-specific sensory conditions.
