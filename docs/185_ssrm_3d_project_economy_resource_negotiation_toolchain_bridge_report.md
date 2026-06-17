# Report 185: SSRM-3D Multi-Agent Project Economy, Resource Scarcity, Negotiation, and Tool-Chain Bridge

## Purpose

Report 185 adds an economy layer above Report 184 local planning. Report 184 showed that agents can hold private local plans, expose public summaries, recover from interruptions, resolve dependencies, coordinate routes, and cooperate through object handoffs. This report asks whether those plans can depend on scarce resources, negotiated allocation, exchange ledgers, fair distribution, route-cost accounting, trust-price modulation, repair/reuse substitutions, and multi-step tool-chain completion.

This is economy substrate. It does not claim complete gameplay, subjective consciousness, moral patienthood, natural language emergence, or free will.

## Architecture

The bridge consumes the Report 184 planning state:

```text
local planning and cooperation state
        |
        v
scarce resource inventory
        |
        v
project recipes and tool chains
        |
        v
negotiation packets
        |
        v
exchange ledger
        |
        v
fair allocation and route costs
        |
        v
trust-price modulation
        |
        v
repair/reuse substitutions
        |
        v
persistent project outputs
        |
        v
browser-local economy replay
```

The default deterministic run uses:

- `3` agents
- `3` projects
- `7` base resources
- `2` reuse resources
- `9` economy events
- scarce resource allocation
- exchange ledger entries
- repair/reuse substitutions
- persistent project outputs

## Projects

The integrated run gives agents economy-backed projects:

- `Ari`: `durable_clay_latch`
- `Fay`: `insulated_moss_bedding`
- `Milo`: `ridge_signal_array`

Each project has a multi-step tool chain with required resources and tools. Some stages cannot complete without reuse byproducts from earlier work.

## Scarcity and reuse

The run intentionally makes some resources scarce:

- `reed_bundle`
- `glass_shard`
- `clay_mass`
- `repair_fiber`
- `signal_charge`

The economy can generate reuse resources:

- `reed_offcut`
- `glass_reading`

Those byproducts are not decorative. Without repair/reuse, later stages lose completion capacity.

## Browser surface

The browser artifact is:

- `visualizations/ssrm_3d_project_economy_resource_negotiation_toolchain_bridge.html`

It loads generated JS artifacts and lets the user:

- step through economy events
- inspect resource stock and consumption
- inspect negotiation acceptance
- inspect exchange ledger entries
- inspect route costs and trust price modifiers
- inspect reuse byproducts
- track project stages and outputs
- save, restore, and reset local browser economy state

## Conditions

The integrated condition is:

- `integrated_project_economy_resource_negotiation_toolchain`

Ablations remove one mechanism at a time:

- `no_resource_scarcity`
- `no_tool_chains`
- `no_negotiation`
- `no_exchange_ledger`
- `no_fair_allocation`
- `no_repair_reuse`
- `no_route_cost_accounting`
- `no_trust_price_modulation`
- `no_project_outputs`
- `no_frequency_flower_economy_binding`
- `no_replay_timeline`
- `no_privacy_filter`

The critical ablations are resource scarcity, tool chains, negotiation, exchange ledger, repair/reuse, and project outputs. A project economy is not meaningful if resources are infinite, outputs do not depend on recipes, scarce allocation is not negotiated, or material accounting is invisible.

## Metrics

The benchmark reports:

- `resource_scarcity_binding_rate`
- `tool_chain_completion_rate`
- `negotiation_resolution_rate`
- `exchange_ledger_integrity_rate`
- `fair_allocation_rate`
- `repair_reuse_rate`
- `route_cost_accounting_rate`
- `trust_price_modulation_rate`
- `project_output_rate`
- `resource_conservation_rate`
- `frequency_flower_economy_binding_rate`
- `browser_economy_replay_rate`
- `privacy_preservation_rate`
- `trace_integrity`
- `project_economy_readiness`

Metric weights are normalized to sum to `1.0`.

## Results

The deterministic run produced:

| Metric | Value |
| --- | ---: |
| `module_verdict` | `pass` |
| `project_economy_readiness` | `1.000000` |
| `economy_events` | `9` |
| `no_resource_scarcity_loss` | `0.270000` |
| `no_negotiation_loss` | `0.385556` |
| `no_project_outputs_loss` | `0.100000` |

Interpretation:

- Scarcity is load-bearing.
- Negotiation is load-bearing.
- Tool chains complete only when required resources or reuse substitutes are available.
- Exchange ledgers preserve material and price accountability.
- Route costs and trust modifiers affect price packets.
- Persistent project outputs are generated.
- Resource conservation is explicitly checked.

## Moral and claim boundary

This report keeps the boundary explicit:

- no subjective-consciousness claim
- no moral-patienthood claim
- no complete-3D-world claim
- no complete-playable-world claim
- no natural-language-emergence claim
- scarcity is not subjective deprivation
- negotiation policy is not moral patienthood
- prices are simulation bookkeeping, not real economy claims
- private workspace is not exposed as a debug shortcut

## Artifacts

- `artifacts/ssrm_3d_project_economy_resource_negotiation_toolchain_bridge_eval.csv`
- `artifacts/ssrm_3d_project_economy_resource_negotiation_toolchain_bridge_verdict.csv`
- `artifacts/ssrm_3d_project_economy_resource_negotiation_toolchain_bridge_results.json`
- `artifacts/ssrm_3d_project_economy_resource_negotiation_toolchain_bridge_results.js`
- `artifacts/ssrm_3d_project_economy_resource_negotiation_toolchain_bridge_trace.json`
- `artifacts/ssrm_3d_project_economy_resource_negotiation_toolchain_bridge_trace.js`
- `artifacts/ssrm_3d_project_economy_resource_negotiation_toolchain_bridge_state.json`
- `artifacts/ssrm_3d_project_economy_resource_negotiation_toolchain_bridge_state.js`
- `visualizations/ssrm_3d_project_economy_resource_negotiation_toolchain_bridge.html`

## Command

```bash
python3 -m experiments.ssrm_3d_project_economy_resource_negotiation_toolchain_bridge
```

## Verdict

Report 185 supports a deterministic multi-agent project economy seed over the Report 184 planning layer. Agents now need scarce resources, tool-chain recipes, negotiated allocation, exchange ledger accountability, route-cost and trust-price packets, repair/reuse substitutions, and persistent project outputs.

The next gate is persistent craft ecology with wear, breakage, maintenance, and supply shocks: outputs should degrade through use, tools should break, maintenance should compete with new work, and supply shocks should force plan revision.
