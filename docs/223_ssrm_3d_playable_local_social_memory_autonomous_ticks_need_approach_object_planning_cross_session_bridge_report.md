# Report 223: SSRM-3D playable local social memory loop with autonomous ticks, need-driven approach/avoidance, object planning, and cross-session continuity

## Status

Pass. The deterministic bridge generated a playable browser loop where agents tick between player inputs, appraise needs, approach or avoid the avatar, plan around objects, persist relationship memory, save/restore cross-session state, and keep private workspaces sealed.

This is not LLM dialogue, open-ended planning, subjective consciousness, real consent, suffering, or moral patienthood.

## Purpose

Report 222 made player interaction stateful: trust, memory, object consequences, refusals, and save/restore persisted locally. Report 223 gives agents their own deterministic tick loop. They now move and react between player actions based on needs, trust, boundary pressure, object plans, and remembered treatment.

The shift is from stateful response to autonomous local social motion.

## Files

- `experiments/ssrm_3d_playable_local_social_memory_autonomous_ticks_need_approach_object_planning_cross_session_bridge.py`
- `visualizations/ssrm_3d_playable_local_social_memory_autonomous_ticks_need_approach_object_planning_cross_session_bridge.html`
- `artifacts/ssrm_3d_playable_local_social_memory_autonomous_ticks_need_approach_object_planning_cross_session_bridge_agents.csv`
- `artifacts/ssrm_3d_playable_local_social_memory_autonomous_ticks_need_approach_object_planning_cross_session_bridge_need_appraisals.csv`
- `artifacts/ssrm_3d_playable_local_social_memory_autonomous_ticks_need_approach_object_planning_cross_session_bridge_approach_avoidance.csv`
- `artifacts/ssrm_3d_playable_local_social_memory_autonomous_ticks_need_approach_object_planning_cross_session_bridge_object_plans.csv`
- `artifacts/ssrm_3d_playable_local_social_memory_autonomous_ticks_need_approach_object_planning_cross_session_bridge_relationship_continuity.csv`
- `artifacts/ssrm_3d_playable_local_social_memory_autonomous_ticks_need_approach_object_planning_cross_session_bridge_cross_session_snapshots.csv`
- `artifacts/ssrm_3d_playable_local_social_memory_autonomous_ticks_need_approach_object_planning_cross_session_bridge_autonomous_ticks.csv`
- `artifacts/ssrm_3d_playable_local_social_memory_autonomous_ticks_need_approach_object_planning_cross_session_bridge_results.json`
- `artifacts/ssrm_3d_playable_local_social_memory_autonomous_ticks_need_approach_object_planning_cross_session_bridge_state.json`
- `artifacts/ssrm_3d_playable_local_social_memory_autonomous_ticks_need_approach_object_planning_cross_session_bridge_verdict.csv`

## Deterministic run

```bash
python3 experiments/ssrm_3d_playable_local_social_memory_autonomous_ticks_need_approach_object_planning_cross_session_bridge.py --seed 20260836
```

Output:

```text
module_verdict pass
local_social_memory_autonomous_loop_readiness 0.919167
agents 4
need_appraisals 24
approach_avoidance_decisions 24
object_plans 4
relationship_continuity_records 4
cross_session_snapshots 4
autonomous_ticks 24
autonomous_agent_tick_rate 1.000000
object_plan_completion_rate 0.500000
cross_session_relationship_continuity 0.750000
weakest_channel_score 0.500000
visualization visualizations/ssrm_3d_playable_local_social_memory_autonomous_ticks_need_approach_object_planning_cross_session_bridge.html
next_gate playable local 3D autonomous social ecology with multi-agent interaction, shared object negotiation, social contagion, and durable relationship histories
```

## Playable loop controls

Open the generated HTML file in a browser.

- `Advance one autonomous tick` moves each agent once from its current needs.
- `Run / pause auto ticks` lets the local loop advance without repeated clicks.
- `Respect nearest boundary` softens cautious agents and updates local state.
- `Intrude near archive` raises Nian's boundary pressure and persists that memory.
- `Save` writes the cross-session state to browser `localStorage`.
- `Restore` reloads the saved relationship state.
- `Export` serializes the state when browser clipboard support is available.

## Autonomous loop objects

| Object | Function |
| --- | --- |
| `AgentLoopState` | Tracks position, trust, boundary pressure, social/rest/object/autonomy needs, target object, current memory, visible behavior, sealed workspace digest, frequency, and flower node. |
| `NeedAppraisal` | Records each tick's dominant need, need score, body cost, relationship modifier, object modifier, tendency, and sealed private appraisal digest. |
| `ApproachAvoidanceDecision` | Records whether the agent approaches, avoids, plans around an object, or holds position, with movement vector and coherence. |
| `ObjectPlan` | Records object goal, permission requirement, steps, completion state, debt effect, fallback, and sealed private reason digest. |
| `RelationshipContinuity` | Records pre-session memory, tick memory, post-restore memory, trust before/after, continuity, and boundary persistence. |
| `CrossSessionSnapshot` | Records localStorage save targets, exported state notes, memory counts, and restore verification. |
| `AutonomousTick` | Records each local tick action, target, trust/boundary delta, object-plan progress, memory write flag, frequency, and flower node. |

The integrated loop is:

```text
local timer tick
-> agent need appraisal
-> approach / avoid / object-plan / rest decision
-> local movement
-> memory write when meaningful
-> object plan progress
-> relationship continuity update
-> save/restore across sessions
```

## Scenario coverage

The generated scenario includes:

- `4` local agents: Fayen, Ariq, Nian, and Roka.
- `24` need appraisals across six ticks.
- `24` approach/avoidance/object-plan decisions.
- `4` object plans.
- `4` relationship continuity records.
- `4` cross-session snapshots.
- `24` autonomous tick records.

## Metrics

| Metric | Score |
| --- | ---: |
| local_social_memory_autonomous_loop_readiness | `0.919167` |
| autonomous_agent_tick_rate | `1.000000` |
| need_appraisal_binding | `1.000000` |
| approach_avoidance_coherence | `0.958333` |
| need_driven_motion_binding | `1.000000` |
| object_planning_traceability | `1.000000` |
| object_plan_completion_rate | `0.500000` |
| object_plan_progress_rate | `0.750000` |
| cross_session_relationship_continuity | `0.750000` |
| memory_persistence_rate | `1.000000` |
| boundary_refusal_persistence | `1.000000` |
| relationship_repair_after_restore | `1.000000` |
| cross_session_snapshot_integrity | `1.000000` |
| private_workspace_boundary_score | `1.000000` |
| frequency_flower_tick_rhythm | `1.000000` |
| browser_social_memory_loop_available | `1.000000` |
| weakest_channel_score | `0.500000` |
| mean_social_loop_channel_score | `0.930556` |

## Ablations

| Ablation | Readiness after removal |
| --- | ---: |
| no_browser_loop | `0.579167` |
| no_autonomous_ticks | `0.599167` |
| no_cross_session_continuity | `0.619167` |
| no_need_appraisal | `0.649167` |
| no_approach_avoidance | `0.669167` |
| no_memory_persistence | `0.669167` |
| no_object_planning | `0.679167` |
| no_boundary_persistence | `0.719167` |
| no_private_boundary | `0.749167` |
| no_frequency_flower_rhythm | `0.839167` |

Browser loop, autonomous ticks, cross-session continuity, need appraisal, approach/avoidance, memory persistence, and object planning dominate because they make the scene behave between player actions rather than merely respond to clicks.

## Honest interpretation

The bridge passes, but it is not open-ended agency.

Object plan completion is only `0.500000`: Fayen's herb plan and Ariq's stone plan complete, Nian's archive-flap plan is blocked by boundary, and Roka's reed plan remains partial. Cross-session relationship continuity is `0.750000`, because Roka restores cautious distance and incomplete trust repair rather than becoming fully continuous and warm. Approach/avoidance coherence is `0.958333`, with one deliberate conflict where Roka hesitates between social need and autonomy need.

This is the right kind of imperfection. Autonomous social life should contain blocked plans, partial repair, hesitation, and boundary persistence.

## Boundary

This report proves deterministic wiring for local autonomous social ticks inside an artificial-life benchmark. It does not prove real consciousness, real consent, subjective feeling, suffering, moral patienthood, or general-purpose autonomous reasoning.

The frequency and flower-of-life overlays are inspectable rhythm and phase scaffolds for the simulation. They are not metaphysical evidence.

## Next gate

Report 224 should add a playable local 3D autonomous social ecology with multi-agent interaction, shared object negotiation, social contagion, and durable relationship histories.
