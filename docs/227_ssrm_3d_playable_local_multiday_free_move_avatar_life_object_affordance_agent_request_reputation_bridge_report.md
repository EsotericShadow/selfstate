# Report 227: SSRM-3D Playable Local Multi-Day Free-Move Avatar Life, Object Affordance, Agent Request, and Reputation Bridge

## Status

Pass.

Report 227 extends Report 226 from avatar participation traces into a multi-day free-move avatar-life slice. The browser artifact now supports keyboard movement, action stepping, agent proximity, object affordance display, agent-initiated requests, persistent public reputation, save/restore, and cross-day snapshots.

This is deterministic functional scaffolding. It is not a consciousness claim, not real consent, not subjective suffering, not moral patienthood, not LLM dialogue, not open-ended social cognition, not full physics, and not complete gameplay.

## Purpose

Report 226 proved that avatar actions could alter trust, object state, access, debt, and later public memory. Report 227 asks whether that can feel more like living in the world across days rather than triggering isolated scenario cards.

The tested loop is:

```text
free-move avatar frame
-> collision or boundary check
-> sensory/body feedback
-> nearby object affordance lattice
-> cooperative task participation
-> agent-initiated request
-> public reputation update
-> cross-day saved snapshot
-> browser restore/replay
```

The key shift is that agents can now ask the avatar for help. The avatar is no longer only choosing from its own action list.

## Implementation

The deterministic module is:

```text
experiments/ssrm_3d_playable_local_multiday_free_move_avatar_life_object_affordance_agent_request_reputation_bridge.py
```

The browser visualization is:

```text
visualizations/ssrm_3d_playable_local_multiday_free_move_avatar_life_object_affordance_agent_request_reputation_bridge.html
```

Generated artifacts:

```text
artifacts/ssrm_3d_playable_local_multiday_free_move_avatar_life_object_affordance_agent_request_reputation_bridge_agents.csv
artifacts/ssrm_3d_playable_local_multiday_free_move_avatar_life_object_affordance_agent_request_reputation_bridge_movement_frames.csv
artifacts/ssrm_3d_playable_local_multiday_free_move_avatar_life_object_affordance_agent_request_reputation_bridge_object_affordances.csv
artifacts/ssrm_3d_playable_local_multiday_free_move_avatar_life_object_affordance_agent_request_reputation_bridge_task_participations.csv
artifacts/ssrm_3d_playable_local_multiday_free_move_avatar_life_object_affordance_agent_request_reputation_bridge_agent_requests.csv
artifacts/ssrm_3d_playable_local_multiday_free_move_avatar_life_object_affordance_agent_request_reputation_bridge_reputation_events.csv
artifacts/ssrm_3d_playable_local_multiday_free_move_avatar_life_object_affordance_agent_request_reputation_bridge_saved_snapshots.csv
artifacts/ssrm_3d_playable_local_multiday_free_move_avatar_life_object_affordance_agent_request_reputation_bridge_life_play_ticks.csv
artifacts/ssrm_3d_playable_local_multiday_free_move_avatar_life_object_affordance_agent_request_reputation_bridge_results.json
artifacts/ssrm_3d_playable_local_multiday_free_move_avatar_life_object_affordance_agent_request_reputation_bridge_state.json
artifacts/ssrm_3d_playable_local_multiday_free_move_avatar_life_object_affordance_agent_request_reputation_bridge_verdict.csv
```

## Scenario coverage

The generated multi-day life slice contains:

| Element | Count |
| --- | ---: |
| Agents | 5 |
| Free-move frames | 12 |
| Object affordance records | 8 |
| Task participations | 6 |
| Agent-initiated requests | 8 |
| Reputation events | 6 |
| Saved snapshots | 4 |
| Life play ticks | 36 |

The four-day slice covers reed lane return, bridge arc repair, water pause recovery, archive threshold, public ledger, care bell timing, shade-frame debt, and the tied learner bundle boundary.

## New channels

### Free movement

The module generates deterministic movement frames across four days. Each frame binds avatar coordinates, movement input, place, collision state, nearest agent, nearest object, sensory packet, body cost, frequency, and flower node.

Collision states include:

```text
clear
boundary_slow
routine_hold
threshold_stop
circle_edge
```

This keeps free movement from becoming permissionless trespass. Movement can stop or slow at social boundaries.

### Richer object affordances

Object records now expose affordance lists, allowed actions, denied actions, permission lattices, wear, material value, debt risk, reversible actions, and saved state keys.

Objects include:

| Object | Affordance principle |
| --- | --- |
| loose reed cuttings | loose-only consent after asking |
| tied learner reed bundle | child-work boundary, access can stay closed |
| chalk boundary cord | repair tool allowed outside reed lane |
| public knot board | public object-only knots, no private body reasons |
| archive flap | threshold object controlled by Nian |
| water cups | care routine help cannot cancel rest |
| shade frame beam | scarce timber with public debt |
| public posture bell | timing signal, not pain disclosure |

The object layer is better than Report 226 but still shallow. The weakest channel is object affordance depth.

### Agent-initiated requests

Agents now initiate requests toward the avatar:

```text
Fayen: Can you carry the cups and leave the pause quiet?
Ariq: Hold the chalk cord, but keep Roka's lane open.
Nian: Say the knot line back before Noro writes it.
Roka: Stand on the blue stone if you want to watch the tied bundle.
Noro: Read your debt line before you ask for another beam.
```

Each request includes urgency, consent context, avatar options, selected response, response quality, trust delta, boundary delta, and saved memory.

### Persistent reputation UI

Public reputation is represented as UI-visible state, not private mind-reading. Reputation events include axis, before/after score, public label, access effect, UI marker, and restore persistence.

Examples:

```text
careful helper
work-accountable
privacy learner
debt visible
boundary-tested
loose-reed trusted
```

Reputation changes access. It does not expose private workspace contents.

### Saved snapshots

Saved snapshots bind avatar position, object state digest, relationship digest, reputation digest, pending requests, restore expectation, restore integrity, frequency, and flower node.

Four snapshots cover day 1 through day 4 and keep open debts visible after restore.

## Metrics

Run command:

```bash
python3 experiments/ssrm_3d_playable_local_multiday_free_move_avatar_life_object_affordance_agent_request_reputation_bridge.py --seed 20260840
```

Run output:

```text
module_verdict pass
playable_multiday_avatar_life_readiness 0.929458
agents 5
movement_frames 12
object_affordances 8
task_participations 6
agent_requests 8
reputation_events 6
saved_snapshots 4
life_play_ticks 36
free_move_place_coverage 1.000000
object_affordance_depth 0.604167
object_permission_lattice_resolution 1.000000
agent_initiated_request_coverage 1.000000
persistent_reputation_ui_integrity 1.000000
save_restore_integrity 0.935000
weakest_channel_score 0.604167
visualization visualizations/ssrm_3d_playable_local_multiday_free_move_avatar_life_object_affordance_agent_request_reputation_bridge.html
next_gate playable local 3D continuous life loop with real-time free movement, agent-initiated interruptions, deeper affordance lattice, and multi-day autonomous background ticks
```

Metric table:

| Metric | Score |
| --- | ---: |
| playable_multiday_avatar_life_readiness | 0.929458 |
| mean_life_channel_score | 0.939430 |
| weakest_channel_score | 0.604167 |
| free_move_place_coverage | 1.000000 |
| free_move_day_coverage | 1.000000 |
| collision_boundary_binding | 1.000000 |
| sensory_body_feedback_binding | 1.000000 |
| object_affordance_depth | 0.604167 |
| object_permission_lattice_resolution | 1.000000 |
| object_state_persistence | 1.000000 |
| task_participation_completion | 0.813333 |
| task_gate_binding | 1.000000 |
| agent_initiated_request_coverage | 1.000000 |
| request_response_quality | 0.865000 |
| request_memory_traceability | 1.000000 |
| persistent_reputation_ui_integrity | 1.000000 |
| cross_day_reputation_persistence | 0.631667 |
| save_restore_integrity | 0.935000 |
| cross_day_snapshot_coverage | 1.000000 |
| private_workspace_boundary_score | 1.000000 |
| frequency_flower_life_rhythm | 1.000000 |
| browser_free_move_life_available | 1.000000 |

## Ablations

| Ablation | Readiness |
| --- | ---: |
| no_browser_free_move | 0.589458 |
| no_free_move_frames | 0.629458 |
| no_reputation_ui | 0.639458 |
| no_object_affordances | 0.649458 |
| no_agent_initiated_requests | 0.659458 |
| no_saved_snapshots | 0.679458 |
| no_permission_lattice | 0.709458 |
| no_sensory_body_feedback | 0.759458 |
| no_frequency_flower_rhythm | 0.849458 |

The largest drops come from removing the browser free-move loop, free-move frames, reputation UI, object affordances, agent-initiated requests, and saved snapshots. That matches the intended direction: the world becomes more convincing when movement, requests, objects, reputation, and persistence all bind together.

## Honest interpretation

This is progress, not completion.

Object affordance depth is only `0.604167`. The system has richer object records, but it still lacks a deep general affordance lattice with compositional use, tool substitution, failure states, per-agent skills, and material transformations.

Task participation completion is `0.813333`. The avatar can help, but tasks remain partially scripted and some work stays conditional or partial.

Cross-day reputation persistence is `0.631667`. Public reputation persists and affects access, but it is not yet a high-resolution social memory system.

Save/restore integrity is `0.935000`. Persistence is good, but it is still structured snapshot replay rather than a continuous background world.

## Boundary

This report does not claim:

- subjective consciousness
- real consent
- subjective suffering
- moral patienthood
- LLM dialogue
- open-ended social cognition
- full 3D physics
- complete object economy
- complete gameplay
- metaphysical significance from frequencies or flower nodes

Frequencies and flower nodes remain timing and phase scaffolds only.

## Next gate

The next gate is a playable local 3D continuous life loop with real-time free movement, agent-initiated interruptions, a deeper affordance lattice, and multi-day autonomous background ticks.
