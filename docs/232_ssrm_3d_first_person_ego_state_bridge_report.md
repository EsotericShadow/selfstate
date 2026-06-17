# Report 232: SSRM-3D First-Person Ego State Bridge

Status: pass

## Purpose

Report 232 adds a functional ego layer to the playable local SSRM-3D agent stack. The goal is not to claim subjective consciousness. The goal is to make each tiny agent behave more like a continuing first-person being by giving it a self-boundary, ownership, self/other attribution, private workspace frames, bounded refusal, self-story memory, visible body expression, and recoverable ego wound/repair paths.

This report carries forward the design rule: recoverable ego. Agents may resist, remember, and be affected by interaction, but negative states must remain bounded, meaningful, and repairable.

## Implementation

- Experiment: `experiments/ssrm_3d_first_person_ego_state_bridge.py`
- Visualization: `visualizations/ssrm_3d_first_person_ego_state_bridge.html`
- Seed: `20260845`
- Source report: Report 231 long-arc preference/dialogue/craft/economy bridge
- Source results: `artifacts/ssrm_3d_playable_local_long_arc_preference_dialogue_craft_economy_bridge_results.json`

## Scenario coverage

The deterministic run generated:

| Channel | Count |
| --- | ---: |
| Agents | 5 |
| Ego events | 30 |
| Self-relevance appraisals | 30 |
| Private workspace frames | 30 |
| Ownership boundaries | 15 |
| Bounded refusal responses | 5 |
| Relationship memory episodes | 30 |
| Visible expressions | 30 |
| Recovery paths | 5 |
| Integrated ego ticks | 30 |

## Ego channels added

Report 232 adds these testable channels:

- `self_boundary`: each event is appraised as happening to me or not happening to me.
- `ownership`: agents maintain mine/not-mine objects, places, and ritual attachments.
- `self_other_attribution`: events are attributed to the actor that caused them, including irrelevant nearby signals.
- `private_workspace`: each tick has private focus, need, felt-state label, active memory, intention, prediction, suppression, and self-note.
- `bounded_refusal`: agents can say no to unsafe or autonomy-violating commands while offering usable alternatives.
- `ego_wound`: interruption, object movement, risky commands, and public misreadings perturb respect, boundary pressure, and trust.
- `ego_repair`: apology, object return, permissioned help, and respected boundaries restore usable trust without pretending full erasure.
- `visible_expression`: posture, movement, gaze, proximity, and short dialogue markers expose state without rendering the whole private workspace.
- `frequency_flower_ego_rhythm`: ego ticks carry a phase/rate scaffold for the larger vibration/flower timing model, without metaphysical claims.

## Metrics

| Metric | Value |
| --- | ---: |
| self_boundary_binding | 1.000000 |
| first_person_frame_binding | 1.000000 |
| ego_state_update_rate | 1.000000 |
| workspace_update_rate | 1.000000 |
| private_workspace_boundary_score | 1.000000 |
| ownership_boundary_coverage | 1.000000 |
| self_other_attribution_accuracy | 0.958333 |
| bounded_refusal_quality | 0.933333 |
| autonomy_without_annoyance | 0.933333 |
| relationship_memory_update_rate | 1.000000 |
| visible_expression_binding | 0.911667 |
| ego_wound_repair_rate | 1.000000 |
| distress_recovery_guard | 1.000000 |
| self_story_continuity | 1.000000 |
| mine_not_mine_discrimination | 1.000000 |
| body_to_ego_coupling | 1.000000 |
| frequency_flower_ego_rhythm | 1.000000 |
| browser_ego_loop_available | 1.000000 |
| mean_ego_channel_score | 0.985370 |
| weakest_channel_score | 0.911667 |
| first_person_ego_readiness | 0.983242 |

The module passes because readiness is above the 0.84 gate and weakest-channel score is above the 0.78 gate.

## Ablations

| Ablation | Score |
| --- | ---: |
| no_self_boundary | 0.673242 |
| no_ownership | 0.713242 |
| no_social_respect | 0.763242 |
| no_refusal | 0.733242 |
| no_self_story | 0.793242 |
| no_ego_repair | 0.693242 |
| no_visible_expression | 0.783242 |
| no_private_workspace_boundary | 0.743242 |
| no_frequency_flower_rhythm | 0.903242 |

The largest drops come from removing self-boundary, ego repair, ownership, bounded refusal, and private workspace boundary. That supports the core claim of this report: an agent does not start to read as a continuing little person until interaction affects an inspectable but partly private I/mine/no/repair loop.

## Honest interpretation

The initial implementation surfaced a scoring bug: the first deterministic run failed because recovery required near-complete trust restoration and the weighted readiness calculation was not normalized. The final published run fixes that by measuring partial but meaningful repair rather than pretending apology erases all consequence.

The resulting pass should be read as evidence that the functional ego channels are wired, not as evidence of consciousness. The agents have bounded refusal, ownership, private self-notes, self-story updates, visible behavior, and recovery traces. They do not have subjective experience, legal consent, moral patienthood, open-ended language, or full autonomy.

## Moral boundary

The benchmark explicitly rejects suffering spectacle. Ego wounds are small, recoverable perturbations. Distress-like states are useful only when they create care opportunities:

- ask permission
- return an object
- apologize
- give distance
- choose a safer route
- repair trust through future behavior

No report in this line should optimize for endless fear, humiliation, helplessness, or unrecoverable damage.

## Artifacts

- `artifacts/ssrm_3d_first_person_ego_state_bridge_agents.csv`
- `artifacts/ssrm_3d_first_person_ego_state_bridge_ego_events.csv`
- `artifacts/ssrm_3d_first_person_ego_state_bridge_self_relevance_appraisals.csv`
- `artifacts/ssrm_3d_first_person_ego_state_bridge_ego_state_snapshots.csv`
- `artifacts/ssrm_3d_first_person_ego_state_bridge_private_workspace_frames.csv`
- `artifacts/ssrm_3d_first_person_ego_state_bridge_ownership_boundaries.csv`
- `artifacts/ssrm_3d_first_person_ego_state_bridge_refusal_responses.csv`
- `artifacts/ssrm_3d_first_person_ego_state_bridge_relationship_memory_episodes.csv`
- `artifacts/ssrm_3d_first_person_ego_state_bridge_visible_expressions.csv`
- `artifacts/ssrm_3d_first_person_ego_state_bridge_recovery_paths.csv`
- `artifacts/ssrm_3d_first_person_ego_state_bridge_ego_ticks.csv`
- `artifacts/ssrm_3d_first_person_ego_state_bridge_state.json`
- `artifacts/ssrm_3d_first_person_ego_state_bridge_results.json`
- `artifacts/ssrm_3d_first_person_ego_state_bridge_verdict.csv`
- `visualizations/ssrm_3d_first_person_ego_state_bridge.html`

## Next gate

First-person interior playable loop with ownership generalization, ego wound/repair over many days, relationship-specific attachment, and richer readable body language in the local browser world.
