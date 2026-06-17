# Report 186: SSRM-3D Persistent Craft Ecology, Wear, Breakage, Maintenance, and Supply-Shock Bridge

## Purpose

Report 186 adds persistent craft ecology above Report 185 project economy. Report 185 showed that agents can allocate scarce resources, negotiate, use tool chains, reuse byproducts, conserve resources, and create durable outputs. This report asks whether those outputs and tools can keep existing after creation while degrading through use, breaking, consuming maintenance resources, reacting to supply shocks, and forcing replans.

This is craft-ecology substrate. It does not claim complete gameplay, subjective consciousness, moral patienthood, natural language emergence, or free will.

## Architecture

The bridge consumes the Report 185 economy state:

```text
project economy outputs and resources
        |
        v
persistent crafted items and tools
        |
        v
use-driven wear
        |
        v
breakage detection
        |
        v
maintenance queue
        |
        v
scarce repair resources
        |
        v
supply shocks
        |
        v
repair competition and substitutes
        |
        v
project capability coupling
        |
        v
browser-local craft replay
```

The deterministic run uses:

- `7` simulated local days
- `7` persistent craft items and tools
- `8` maintenance resources
- `68` craft events
- use-driven durability loss
- breakage detection
- maintenance and repair-resource consumption
- supply shocks at `reed_wetland`, `glass_mire`, and `stone_ridge`
- resource conservation checks
- browser replay frames

## Craft items

The integrated run tracks both outputs and tools:

- `hearth_latch_repaired`
- `dry_bedding_ready`
- `route_warning_signal_ready`
- `clay_patch_kit`
- `dry_cloak`
- `signal_shell`
- `glass_lens`

Each item carries durability, wear rate, repair requirements, owner/place context, frequency, and flower node.

## Supply shocks

The run injects deterministic shocks:

- `reed_flood` affects `repair_fiber` and `reed_bundle`
- `glass_mire_slick` affects `glass_reading`
- `ridge_silence` affects `signal_charge`

Shocks are not subjective deprivation. They are environmental constraints that force maintenance replanning and resource accounting.

## Browser surface

The browser artifact is:

- `visualizations/ssrm_3d_persistent_craft_ecology_wear_maintenance_supply_shock_bridge.html`

It loads generated JS artifacts and lets the user:

- step through craft events
- inspect item durability
- see breakage and maintenance outcomes
- inspect supply-shock losses
- inspect repair resources and consumption
- inspect project-blocking toolchain coupling
- save, restore, and reset local browser craft state

## Conditions

The integrated condition is:

- `integrated_persistent_craft_ecology_wear_maintenance_supply_shock`

Ablations remove one mechanism at a time:

- `no_wear_tracking`
- `no_breakage_detection`
- `no_maintenance`
- `no_supply_shocks`
- `no_repair_competition`
- `no_output_degradation`
- `no_toolchain_coupling`
- `no_replan_from_shock`
- `no_craft_persistence`
- `no_frequency_flower_binding`
- `no_replay_timeline`
- `no_privacy_filter`

The critical ablations are wear tracking, maintenance, supply shocks, output degradation, toolchain coupling, and persistence. A convincing craft ecology cannot let tools and outputs remain permanently perfect after creation.

## Metrics

The benchmark reports:

- `wear_tracking_rate`
- `breakage_detection_rate`
- `maintenance_action_rate`
- `supply_shock_response_rate`
- `repair_resource_competition_rate`
- `output_degradation_rate`
- `toolchain_degradation_coupling_rate`
- `replan_from_shock_rate`
- `craft_state_persistence_rate`
- `resource_conservation_rate`
- `frequency_flower_maintenance_binding_rate`
- `browser_craft_replay_rate`
- `privacy_preservation_rate`
- `trace_integrity`
- `craft_ecology_readiness`

Metric weights are normalized to sum to `1.0`. The final weighting intentionally emphasizes maintenance and supply shocks because those are the report gate, not decorative channels.

## Results

The deterministic run produced:

| Metric | Value |
| --- | ---: |
| `module_verdict` | `pass` |
| `craft_ecology_readiness` | `0.931544` |
| `craft_events` | `68` |
| `no_wear_tracking_loss` | `0.534429` |
| `no_maintenance_loss` | `0.105632` |
| `no_supply_shocks_loss` | `0.098211` |

Interpretation:

- Wear tracking is strongly load-bearing.
- Maintenance is load-bearing after repair inventory is sized to permit meaningful maintenance rather than constant failure.
- Supply shocks are load-bearing.
- Crafted outputs degrade rather than staying perfect.
- Broken or degraded items can block project capability.
- Resource conservation is checked after shock losses and repair consumption.
- The score is deliberately not perfect; maintenance remains constrained by repair resource availability.

## Moral and claim boundary

This report keeps the boundary explicit:

- no subjective-consciousness claim
- no moral-patienthood claim
- no complete-3D-world claim
- no complete-playable-world claim
- no natural-language-emergence claim
- wear and breakage are not subjective suffering
- supply shocks are not subjective deprivation
- maintenance policy is not moral patienthood
- private workspace is not exposed as a debug shortcut

## Artifacts

- `artifacts/ssrm_3d_persistent_craft_ecology_wear_maintenance_supply_shock_bridge_eval.csv`
- `artifacts/ssrm_3d_persistent_craft_ecology_wear_maintenance_supply_shock_bridge_verdict.csv`
- `artifacts/ssrm_3d_persistent_craft_ecology_wear_maintenance_supply_shock_bridge_results.json`
- `artifacts/ssrm_3d_persistent_craft_ecology_wear_maintenance_supply_shock_bridge_results.js`
- `artifacts/ssrm_3d_persistent_craft_ecology_wear_maintenance_supply_shock_bridge_trace.json`
- `artifacts/ssrm_3d_persistent_craft_ecology_wear_maintenance_supply_shock_bridge_trace.js`
- `artifacts/ssrm_3d_persistent_craft_ecology_wear_maintenance_supply_shock_bridge_state.json`
- `artifacts/ssrm_3d_persistent_craft_ecology_wear_maintenance_supply_shock_bridge_state.js`
- `visualizations/ssrm_3d_persistent_craft_ecology_wear_maintenance_supply_shock_bridge.html`

## Command

```bash
python3 -m experiments.ssrm_3d_persistent_craft_ecology_wear_maintenance_supply_shock_bridge
```

## Verdict

Report 186 supports a deterministic persistent craft ecology seed over the Report 185 project economy layer. Outputs and tools now persist, wear down, break, consume maintenance resources, respond to supply shocks, force repair competition, block project capability when degraded, and conserve material accounting.

The next gate is persistent ecological regeneration, spoilage, waste, and sanitation feedback: food, water, waste, contaminants, regrowth, spoilage, and cleaning should create delayed ecological consequences that agents must perceive and manage.
