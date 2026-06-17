# Report 145: SSRM-3D Autonomous Live Agent Loop Bridge

## Purpose

Report 144 moved from scripted intervention buttons to typed embodied avatar input, but its benchmark still depended on deterministic input rows. Report 145 adds the next bridge: mature agents continue ticking autonomously in a local live loop even when the player does nothing.

The bridge loads the Report 142 avatar-entry packets and the Report 144 embodied-input state, then runs a multi-rate scheduler. Each scheduled agent tick reads sensory pressure, updates an internal workspace, chooses an autonomous action, changes body/affect state, affects world variables, can exchange a native token with another agent, and leaves a replay trace. Sparse avatar interrupts are still available, but they are no longer the only source of behavior.

This is still not subjective consciousness, not LLM-backed open dialogue, not unscripted civilization emergence, and not a complete playable world.

## What changed

- Added `experiments/ssrm_3d_autonomous_live_agent_loop_bridge.py`.
- Added autonomous multi-rate agent ticks over sensory channels: visual, audio, olfactory, thermal, wetness, pain, affect, and vestibular.
- Added live actions: forage water, repair tool, warm shelter, scout route, watch weather, comfort neighbor, teach token, clean camp, and rest body.
- Added internal workspace updates, body/fatigue/pain dynamics, social token exchange, world degradation and repair, sparse player interrupts, and replay traces.
- Added `visualizations/ssrm_3d_autonomous_live_agent_loop_bridge.html`, a browser loop with start/pause/step controls and avatar interrupts.

## Conditions

| Condition | Readiness | Action rate | Perception | Workspace | Social | World update | Player response | Multi-rate | Homeostasis | Trace |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `integrated_autonomous_live_loop` | `0.857642` | `0.562500` | `1.000000` | `0.990826` | `0.615741` | `0.752315` | `1.000000` | `0.937500` | `0.963143` | `1.000000` |
| `no_autonomous_scheduler` | `0.228280` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `1.000000` | `0.000000` | `0.478498` | `1.000000` |
| `no_internal_workspace` | `0.716887` | `0.562500` | `1.000000` | `0.000000` | `0.592593` | `0.817130` | `1.000000` | `0.881944` | `0.930705` | `1.000000` |
| `no_sensory_bus` | `0.703614` | `0.562500` | `0.000000` | `0.990826` | `0.453704` | `1.000000` | `1.000000` | `0.562500` | `0.806598` | `1.000000` |
| `no_social_exchange` | `0.796068` | `0.562500` | `1.000000` | `0.990826` | `0.000000` | `0.752315` | `1.000000` | `0.937500` | `0.963143` | `1.000000` |
| `no_world_consequences` | `0.678589` | `0.562500` | `1.000000` | `0.990826` | `0.490741` | `0.000000` | `1.000000` | `0.645833` | `0.468323` | `1.000000` |
| `no_player_interrupts` | `0.739539` | `0.562500` | `1.000000` | `1.000000` | `0.615741` | `0.756944` | `0.000000` | `0.937500` | `0.963274` | `1.000000` |
| `no_persistent_trace` | `0.787642` | `0.562500` | `1.000000` | `0.990826` | `0.615741` | `0.752315` | `1.000000` | `0.937500` | `0.963143` | `0.000000` |

## Verdict

The integrated condition reaches autonomous-live readiness `0.857642`. It passes this bounded bridge gate with autonomous action rate `0.562500`, perception update rate `1.000000`, workspace tick rate `0.990826`, social exchange rate `0.615741`, world-state update rate `0.752315`, player interrupt response rate `1.000000`, multi-rate synchrony `0.937500`, world homeostasis `0.963143`, and trace completeness `1.000000`.

Ablations reduce readiness:

| Ablation | Readiness loss |
|---|---:|
| `no_autonomous_scheduler` | `0.629362` |
| `no_internal_workspace` | `0.140755` |
| `no_sensory_bus` | `0.154028` |
| `no_social_exchange` | `0.061574` |
| `no_world_consequences` | `0.179053` |
| `no_player_interrupts` | `0.118103` |
| `no_persistent_trace` | `0.070000` |

`supports_autonomous_live_agent_loop_bridge = true`.

`supports_subjective_consciousness = false`.

`supports_llm_open_dialogue = false`.

`supports_complete_playable_world = false`.

`supports_unscripted_civilization = false`.

## Interpretation

Report 145 changes the shape of the playable-world bridge. Before this report, behavior was driven by scripted interventions or typed benchmark rows. Now agents have a deterministic autonomous loop:

```text
multi-rate scheduler -> sensory pressure -> internal workspace -> autonomous action -> body/social/world update -> replay trace
```

That is closer to the requested live-agent direction because the player can enter a world where agents are already doing things. It is still only a bridge. The action policy is hand-built, the language exchange is token-grounded but not generative, and civilization does not emerge unscripted inside the live loop. The next gates are richer affordance objects, persistent agent-to-agent tasks, learned interpretation/planning, and longer unsupervised continuation before avatar entry.

## Artifacts

- `artifacts/ssrm_3d_autonomous_live_agent_loop_bridge_eval.csv`
- `artifacts/ssrm_3d_autonomous_live_agent_loop_bridge_verdict.csv`
- `artifacts/ssrm_3d_autonomous_live_agent_loop_bridge_results.json`
- `artifacts/ssrm_3d_autonomous_live_agent_loop_bridge_trace.json`
- `artifacts/ssrm_3d_autonomous_live_agent_loop_bridge_state.json`
- `artifacts/ssrm_3d_autonomous_live_agent_loop_bridge_results.js`
- `artifacts/ssrm_3d_autonomous_live_agent_loop_bridge_trace.js`
- `artifacts/ssrm_3d_autonomous_live_agent_loop_bridge_state.js`
- `visualizations/ssrm_3d_autonomous_live_agent_loop_bridge.html`

## Reproduction

```bash
python3 -m experiments.ssrm_3d_deep_time_playable_bridge
python3 -m experiments.ssrm_3d_live_avatar_intervention_bridge
python3 -m experiments.ssrm_3d_embodied_avatar_input_bridge
python3 -m experiments.ssrm_3d_autonomous_live_agent_loop_bridge
```
