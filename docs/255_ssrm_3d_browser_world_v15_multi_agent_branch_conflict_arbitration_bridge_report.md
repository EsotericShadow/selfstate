# Report 255: SSRM-3D Browser World v15 Multi-Agent Branch Conflict Arbitration Bridge

## Purpose

Report 255 extends Report 254's browser-local branch mutation into multi-agent concurrent branch consequences. The new bridge makes branch futures collide across agents, detects those conflicts, runs deterministic public arbitration, preserves partial rollback isolation, restores conflict state after reload, and exports replayable arbitration traces.

The purpose is not to claim subjective consciousness, real consent, autonomous natural language, moral patienthood, or a complete 3D engine. The purpose is to make the playable browser-world scaffold more life-like by making user-selected futures affect more than one agent at once, while keeping the state transitions inspectable.

## Source dependency

The module consumes:

```text
artifacts/ssrm_3d_browser_world_v14_in_browser_branch_state_mutation_bridge_results.json
```

Report 254 passed with browser-local selected branch mutation, localStorage persistence, reload restore, rollback, replay export, and agent follow-up from restored branch state. Report 255 uses that as the substrate for concurrent branch conflicts.

## Added mechanism

The bridge adds:

- multi-agent concurrent branch groups
- branch conflict detection across schedule, access, trust, route, resource, privacy, and recovery channels
- irrelevant/noisy conflict signals that should not force arbitration
- deterministic public arbitration modes
- agent-initiated follow-up arbitration after reload
- schedule/access/trust mutation from arbitration outcome
- partial rollback isolation, so rolling back one selected branch does not erase another agent's accepted branch
- replay export with pre-conflict state, selected branches, arbitration reason, reload state, rollback state, and deterministic ordering
- browser visualization with localStorage-backed conflict state, reload restore, rollback, and replay export controls

## Run

```bash
python3 -m experiments.ssrm_3d_browser_world_v15_multi_agent_branch_conflict_arbitration_bridge
```

Final verdict:

```text
pass
```

The first local run failed on a generated HTML f-string escape. A later run failed because the follow-up-after-reload metric was denominated against all avatar asks, including frames that were not reload-restored. That metric was narrowed to restored follow-up asks. The arbitration policy still leaves unresolved/repair cases visible; it was not cleaned to all-1.0.

## Counts

| Channel | Count |
|---|---:|
| browser_world_v15_ticks | 168 |
| concurrent_branch_group_frames | 168 |
| branch_conflict_frames | 168 |
| real_conflict_frames | 144 |
| conflict_arbitration_frames | 168 |
| multi_agent_followup_arbitration_frames | 93 |
| schedule_access_trust_conflict_frames | 168 |
| partial_rollback_isolation_frames | 168 |
| arbitration_replay_export_frames | 168 |
| lineages | 6 |

## Metrics

| Metric | Value |
|---|---:|
| browser_world_v15_conflict_arbitration_readiness | 0.925220 |
| weakest_channel_score | 0.856346 |
| mean_conflict_channel_score | 0.963962 |
| source_in_browser_mutation_continuity | 1.000000 |
| multi_agent_concurrency_surface | 0.976190 |
| concurrent_branch_persistence | 0.976190 |
| conflict_detection_rate | 0.951389 |
| arbitration_resolution_rate | 0.875000 |
| followup_arbitration_after_reload | 0.939394 |
| schedule_access_trust_conflict_binding | 1.000000 |
| partial_rollback_isolation | 0.967262 |
| privacy_safe_arbitration | 1.000000 |
| typed_arbitration_confidence | 0.856346 |
| replay_arbitration_integrity | 0.985952 |
| save_restore_multi_branch_integrity | 0.967742 |
| sensory_frequency_flower_conflict_rhythm | 1.000000 |
| browser_world_v15_surface_available | 1.000000 |

The weakest channel is typed arbitration confidence. That is the right boundary: the browser can route deterministic typed arbitration, but it is still parser/template confidence, not open-ended language understanding.

## Ablations

| Ablation | Readiness after ablation | Loss |
|---|---:|---:|
| no_multi_agent_concurrency | 0.595220 | 0.330000 |
| no_conflict_detection | 0.625220 | 0.300000 |
| no_reload_followup | 0.680220 | 0.245000 |
| no_partial_rollback_isolation | 0.700220 | 0.225000 |
| no_schedule_access_trust_binding | 0.720220 | 0.205000 |
| no_privacy_boundary | 0.745220 | 0.180000 |

These ablations make the dependency explicit: if concurrent branches collapse, conflicts are not detected, reload follow-up disappears, partial rollback becomes global revert, public schedule/access/trust mutation is disconnected, or private workspace leaks, the bridge loses its point.

## Browser artifact

The generated browser artifact is:

```text
visualizations/ssrm_3d_browser_world_v15_multi_agent_branch_conflict_arbitration_bridge.html
```

It includes:

- localStorage key `ssrm_browser_world_v15_multi_agent_branch_conflicts`
- run-arbitration tick button
- simulate reload restore button
- rollback selected branch button
- export replay JSON button
- public conflict log
- readiness/weakest/conflict counters

## Artifact set

```text
artifacts/ssrm_3d_browser_world_v15_multi_agent_branch_conflict_arbitration_bridge_concurrent_branch_groups.csv
artifacts/ssrm_3d_browser_world_v15_multi_agent_branch_conflict_arbitration_bridge_branch_conflicts.csv
artifacts/ssrm_3d_browser_world_v15_multi_agent_branch_conflict_arbitration_bridge_conflict_arbitrations.csv
artifacts/ssrm_3d_browser_world_v15_multi_agent_branch_conflict_arbitration_bridge_followup_arbitrations.csv
artifacts/ssrm_3d_browser_world_v15_multi_agent_branch_conflict_arbitration_bridge_schedule_access_trust_conflicts.csv
artifacts/ssrm_3d_browser_world_v15_multi_agent_branch_conflict_arbitration_bridge_partial_rollback_isolations.csv
artifacts/ssrm_3d_browser_world_v15_multi_agent_branch_conflict_arbitration_bridge_arbitration_replay_exports.csv
artifacts/ssrm_3d_browser_world_v15_multi_agent_branch_conflict_arbitration_bridge_browser_ticks.csv
artifacts/ssrm_3d_browser_world_v15_multi_agent_branch_conflict_arbitration_bridge_summary.csv
artifacts/ssrm_3d_browser_world_v15_multi_agent_branch_conflict_arbitration_bridge_verdict.csv
artifacts/ssrm_3d_browser_world_v15_multi_agent_branch_conflict_arbitration_bridge_state.json
artifacts/ssrm_3d_browser_world_v15_multi_agent_branch_conflict_arbitration_bridge_results.json
```

## Interpretation

Report 255 makes the browser-world branch system less single-player. A selected future can now affect several agents, collide with another agent's schedule/access/trust state, survive reload, prompt follow-up arbitration, and be partially rolled back without erasing unrelated accepted futures.

This moves the surface closer to playable little-person dynamics because choices now create social conflict and remembered arbitration. It is still deterministic. The agents do not have subjective experience, real consent, real rights, autonomous natural language, or independent moral status.

## Next gate

Report 256 should move from conflict artifact rows into persistent multi-agent branch conflict gameplay: user decisions should resolve live conflicts across several days, and agents should remember arbitration outcomes in later requests, refusals, access changes, and relationship posture.
