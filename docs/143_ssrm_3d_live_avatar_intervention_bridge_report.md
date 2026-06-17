# SSRM-3D Live Avatar Intervention Bridge Report

## Question

Can the mature deep-time agent packets from Report 142 become stateful avatar-interaction objects, where player speech/actions update agent workspace, trust, language grounding, sensory-rate resonance, world state, and replayable intervention traces?

This report is a bridge toward the larger playable-world goal. It moves from static avatar-entry packets to deterministic player intervention sessions.

## What changed

This report adds:

- `experiments/ssrm_3d_live_avatar_intervention_bridge.py`
- `visualizations/ssrm_3d_live_avatar_intervention_bridge.html`
- `artifacts/ssrm_3d_live_avatar_intervention_bridge_eval.csv`
- `artifacts/ssrm_3d_live_avatar_intervention_bridge_verdict.csv`
- `artifacts/ssrm_3d_live_avatar_intervention_bridge_results.json`
- `artifacts/ssrm_3d_live_avatar_intervention_bridge_trace.json`
- `artifacts/ssrm_3d_live_avatar_intervention_bridge_state.json`
- JS mirrors of the results, trace, and final state for the browser viewer.

The benchmark loads the Report 142 avatar-agent packets and runs a deterministic `18`-step avatar session. Player interventions include:

- greeting an agent;
- asking for native-token meaning;
- offering clean water;
- helping repair a cold tool cache;
- comforting an agent who shows pain/fear;
- asking for a trusted storm route;
- placing a new mark for council acceptance;
- asking about wet/cold weather signs;
- promising not to take tools without a return path.

Each intervention records:

- player utterance;
- selected agent;
- native token;
- sensory channel and resonance score;
- trust before/after;
- attention before/after;
- world state before/after;
- agent response;
- replay trace row.

## What this does not claim

This does not prove subjective consciousness.

This does not use LLM-backed dialogue.

This does not yet prove mature live agents, open-ended language, or a complete playable world.

It does prove a narrower bridge: player/avatar actions can now cause deterministic, replayable state changes in mature simulated-agent packets.

## Canonical command

```bash
python3 experiments/ssrm_3d_live_avatar_intervention_bridge.py --seed 20260617 --steps 18
```

## Conditions

- `integrated_live_avatar_session`
- `no_workspace_updates`
- `no_trust_updates`
- `no_sensory_resonance`
- `no_language_grounding`
- `no_world_effects`
- `no_replay_trace`

## Result

The integrated condition reaches:

```text
intervention_readiness = 0.765710
state_change_rate = 0.786057
workspace_update_rate = 1.000000
trust_gain = 0.146257
language_alignment = 1.000000
world_effect_score = 1.000000
sensory_resonance_score = 0.598110
trace_completeness = 1.000000
```

Targeted ablations reduce readiness:

```text
no_workspace_loss = 0.384509
no_trust_loss = 0.118524
no_sensory_loss = 0.253112
no_language_loss = 0.376908
no_world_effect_loss = 0.366388
no_replay_trace_loss = 0.347705
```

Verdict:

```text
supports_stateful_avatar_interaction_bridge = true
supports_subjective_consciousness = false
supports_mature_live_agents = false
verdict = pass
```

## Interpretation

Report 142 made avatar-entry packets inspectable. Report 143 makes them stateful enough for a first interaction bridge: an avatar can speak or act, an agent changes attention/trust/body-affect state, the world changes, and the interaction leaves a trace.

The browser viewer is still local and rule-based. It is not a full game client, not a multi-agent online learner, and not a language model conversation layer. The next gate is a live loop where the player's position, speech, and physical action are first-class simulation inputs, agents respond over time, and the resulting state can be replayed, forked, and ablated.

## Artifacts

- [script](../experiments/ssrm_3d_live_avatar_intervention_bridge.py)
- [viewer](../visualizations/ssrm_3d_live_avatar_intervention_bridge.html)
- [evaluation CSV](../artifacts/ssrm_3d_live_avatar_intervention_bridge_eval.csv)
- [verdict CSV](../artifacts/ssrm_3d_live_avatar_intervention_bridge_verdict.csv)
- [results JSON](../artifacts/ssrm_3d_live_avatar_intervention_bridge_results.json)
- [trace JSON](../artifacts/ssrm_3d_live_avatar_intervention_bridge_trace.json)
- [state JSON](../artifacts/ssrm_3d_live_avatar_intervention_bridge_state.json)
