# Report 158: SSRM-3D Continuous Co-presence Bridge

Date: 2026-06-16

## Purpose

Report 157 made the avatar navigable through places, objects, agents, infrastructure, source overlays, frequency fields, body costs, affordance gates, and replay. Report 158 moves one step closer to the requested live playable world: continuous co-presence.

The avatar is now a same-loop perturbation inside nearby agents' deterministic control cycle. Avatar place and mode can alter nearby agents' autonomous choices, internal workspace updates, social memory, sensory-frequency state, world consequences, source-boundary behavior, and replay events during the same tick.

No LLMs are called. This is not evidence of subjective consciousness, open-ended natural language, unscripted civilization, or a complete playable world.

## Implementation

The new module is:

- `experiments/ssrm_3d_continuous_copresence_bridge.py`

It consumes:

- `artifacts/ssrm_3d_navigable_embodied_presence_bridge_state.json`
- `artifacts/ssrm_3d_autonomous_live_agent_loop_bridge_state.json`
- `artifacts/ssrm_3d_live_dialogue_world_integration_bridge_state.json`

It emits:

- `artifacts/ssrm_3d_continuous_copresence_bridge_eval.csv`
- `artifacts/ssrm_3d_continuous_copresence_bridge_verdict.csv`
- `artifacts/ssrm_3d_continuous_copresence_bridge_results.json`
- `artifacts/ssrm_3d_continuous_copresence_bridge_results.js`
- `artifacts/ssrm_3d_continuous_copresence_bridge_trace.json`
- `artifacts/ssrm_3d_continuous_copresence_bridge_trace.js`
- `artifacts/ssrm_3d_continuous_copresence_bridge_state.json`
- `artifacts/ssrm_3d_continuous_copresence_bridge_state.js`

The browser artifact is:

- `visualizations/ssrm_3d_continuous_copresence_bridge.html`

## New Bridge Objects

The bridge joins three prior layers:

- Report 157 navigable embodied presence;
- Report 145 autonomous live-agent loop state;
- Report 155 live dialogue-world integration.

The integrated run covers:

- `160` co-presence ticks;
- `168` nearby-agent opportunities;
- same-loop avatar perturbation, autonomous action choice, body/frequency coupling, workspace writes, social-memory writes, source-boundary refusals, world mutation, and replay.

## Co-presence Contract

The deterministic contract adds these components:

- avatar perturbation of nearby agents' chosen action compared with their base autonomous action;
- autonomous agent choice inside the same tick, not a display-only trace;
- proximity binding so only nearby embodied agents are eligible for avatar perturbation;
- internal workspace updates with avatar place, mode, chosen action, base action, source boundary, and frequency mean;
- social memory updates and relation-to-avatar changes after local encounters;
- sensory-frequency coupling across vibration, sound, vision, scent, thermal, wetness, pain, and affect;
- world consequences for route confidence, tool integrity, shelter warmth, shared water, council acceptance, avatar trust field, source boundary events, and flower phase;
- source-boundary preservation for unsafe or ungrounded avatar probes;
- replay timeline export for every co-presence tick.

## Results

| Condition | Readiness | Perturb | Choice | Proximity | Workspace | Social | Frequency | World | Source | Response | Replay | Trace |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `integrated_continuous_copresence` | `0.971667` | `0.797619` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_avatar_perturbation` | `0.860000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_autonomous_agent_choice` | `0.323393` | `0.000000` | `0.000000` | `1.000000` | `0.000000` | `0.000000` | `1.000000` | `0.000000` | `0.815476` | `0.000000` | `1.000000` | `1.000000` |
| `no_proximity_binding` | `0.050000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `1.000000` | `1.000000` |
| `no_internal_workspace_update` | `0.861667` | `0.797619` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_social_memory_update` | `0.871667` | `0.797619` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_sensory_frequency_coupling` | `0.871667` | `0.797619` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_world_consequence` | `0.851667` | `0.797619` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_source_boundary_preservation` | `0.876667` | `0.761905` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_replay_timeline` | `0.941667` | `0.797619` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` |

The full bridge passes with continuous co-presence readiness `0.971667`.

## Ablation Read

The largest loss is `no_proximity_binding`: `0.921667`. That is intentional. Without local embodied proximity, the avatar is not present to any specific agent, so perturbation, workspace, social memory, frequency coupling, source boundaries, world consequences, and bidirectional response all collapse.

The second-largest loss is `no_autonomous_agent_choice`: `0.648274`. A world with visible agents but no same-tick agent choice is not live co-presence.

Removing world consequences loses `0.120000`. Removing avatar perturbation loses `0.111667`. Removing internal workspace loses `0.110000`; social memory and sensory-frequency coupling each lose `0.100000`. Source-boundary preservation loses `0.095000`, meaning unsafe probes stop being reliably refused.

The replay ablation is smaller at `0.030000`, but still required for auditability.

## Honest Boundary

This report supports only this claim: the stack now has deterministic same-loop co-presence where avatar movement and mode perturb nearby autonomous agents, and those agents mutate workspace, memory, frequency, source-boundary, response, and world state in the same tick.

It does not support:

- subjective consciousness;
- LLM-backed open dialogue;
- unscripted language or culture;
- a complete playable world;
- mature autonomous live agents.

The next gate is interactive typed co-presence: the browser should let the user type live utterances at a place, route them to nearby agents, and let agent responses feed back into the same co-presence loop without rerunning a precomputed scripted trace.

## Reproduction

```bash
python3 -m experiments.ssrm_3d_continuous_copresence_bridge
```

The local viewer can be served with:

```bash
python3 -m http.server 8772 --bind 127.0.0.1
```

Then open:

```text
http://127.0.0.1:8772/visualizations/ssrm_3d_continuous_copresence_bridge.html
```
