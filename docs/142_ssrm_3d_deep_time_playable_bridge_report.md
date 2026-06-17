# SSRM-3D Deep-Time Playable Agent Bridge Report

## Question

Can the open-emergence/civilization track expose a deterministic bridge from thousands of simulated years into playable avatar-entry agents with internal workspace packets, sensory-rate channels, language/culture/technology traces, and conversation hooks?

This is not the final playable world. It is a bridge artifact for the larger goal: entering a mature simulated world after long prehistory and interacting with agents whose state is grounded in embodied pressure rather than a static character sheet.

## What changed

This report adds:

- `experiments/ssrm_3d_deep_time_playable_bridge.py`
- `visualizations/ssrm_3d_deep_time_playable_bridge.html`
- `artifacts/ssrm_3d_deep_time_playable_bridge_eval.csv`
- `artifacts/ssrm_3d_deep_time_playable_bridge_verdict.csv`
- `artifacts/ssrm_3d_deep_time_playable_bridge_results.json`
- `artifacts/ssrm_3d_deep_time_playable_bridge_avatar_agents.json`
- `artifacts/ssrm_3d_deep_time_playable_bridge_trace.json`
- JS mirrors of the results, agent packets, and trace for the browser viewer.

The experiment compresses `4096` simulated years into `64`-year epochs. It tracks:

- civilization depth;
- natural-language emergence proxy;
- technology depth;
- culture depth;
- internal workspace score;
- sensory-frequency score;
- seven-node flower-lattice phase coherence;
- avatar playability score.

The agent packets include:

- name, role, lineage year, and 3D map position;
- native invented tokens and translation hints;
- sensory rates for visual, audio, olfactory, thermal, wetness, pain, affect, and vestibular channels;
- internal workspace fields for attention, motive, body state, affect, and private thought;
- conversation hooks for later live interaction.

## What this does not claim

This does not prove subjective consciousness.

This does not prove open-ended civilization or natural language.

This does not yet provide live LLM-backed conversation, true multi-agent RL, raw audiovisual perception, or a complete playable world.

The frequency/flower-lattice scaffold is treated as a deterministic rate-encoding geometry for sensory and timing channels, not as evidence of metaphysical structure.

## Canonical command

```bash
python3 experiments/ssrm_3d_deep_time_playable_bridge.py --years 4096 --epoch-years 64 --seed 20260616 --population 12 --trace-epochs 18
```

## Conditions

- `integrated_deep_time_world`
- `no_internal_workspace`
- `no_frequency_sensory_bus`
- `no_symbol_inheritance`
- `no_technology_memory`
- `no_culture_memory`
- `no_avatar_protocol`

## Result

The integrated condition reaches:

```text
overall_readiness = 0.872065
language_emergence = 0.827521
technology_depth = 0.855737
culture_depth = 1.000000
internal_workspace_score = 1.000000
sensory_frequency_score = 0.879003
avatar_playability_score = 0.950984
```

Targeted ablations reduce readiness:

```text
no_internal_workspace_loss = 0.352293
no_frequency_bus_loss = 0.221703
no_symbol_inheritance_loss = 0.298812
no_technology_memory_loss = 0.278911
no_culture_memory_loss = 0.165514
no_avatar_protocol_loss = 0.165272
```

Verdict:

```text
supports_deep_time_playable_bridge = true
supports_subjective_consciousness = false
supports_live_avatar_entry = false
verdict = pass
```

## Interpretation

This is a useful bridge because the later playable surface now has concrete state to consume: mature agents, sensory-rate channels, invented tokens, internal workspace packets, and interaction hooks.

The negative flags matter. A browser can inspect and lightly converse with the generated packets, but the system still lacks true live avatar entry, embodied online learning during player interaction, and real language conversation. Those remain the next gates.

The strongest next step is to make the viewer drive live state changes: the player enters as an avatar, asks or acts, agents update attention/trust/action in response, and the simulator writes an intervention trace that can be replayed and ablated.

## Artifacts

- [script](../experiments/ssrm_3d_deep_time_playable_bridge.py)
- [viewer](../visualizations/ssrm_3d_deep_time_playable_bridge.html)
- [evaluation CSV](../artifacts/ssrm_3d_deep_time_playable_bridge_eval.csv)
- [verdict CSV](../artifacts/ssrm_3d_deep_time_playable_bridge_verdict.csv)
- [results JSON](../artifacts/ssrm_3d_deep_time_playable_bridge_results.json)
- [avatar agents JSON](../artifacts/ssrm_3d_deep_time_playable_bridge_avatar_agents.json)
- [trace JSON](../artifacts/ssrm_3d_deep_time_playable_bridge_trace.json)
