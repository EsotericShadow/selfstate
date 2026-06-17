# Report 193: SSRM-3D Multi-week Apprenticeship, Skill Transfer, and Tool-specialization Career Bridge

## Summary

Report 193 extends settlement scheduling into persistent careers. Agents now form multi-week apprenticeships, receive mentors, practice skills, transfer knowledge, specialize around tools, stabilize career identity, record teaching lineage, improve craft quality, fit project roles, grow autonomy, balance fatigue against learning, bind careers to schedule memory, attach career rhythm to frequency/flower nodes, and export browser replay packets.

This is deterministic functional career substrate. It is not subjective vocation, real labor, subjective obligation, subjective consciousness, moral patienthood, or complete 3D gameplay.

## Why this report exists

Report 192 gave agents settlement work schedules: roles, rest/care balance, promises, project dependencies, repair/gather/teach/care rotation, conflict resolution, adaptation, and social obligation memory. But a world that feels lived-in needs more than rotating tasks. Agents should become differentiated workers with histories of practice, tools they know, mentors they learned from, and career identities that persist across weeks.

Report 193 adds that layer. Ari, Fay, and Milo now carry persistent specialties, tool affinity, mentor/apprentice relations, teaching lineage, and career memories derived from prior settlement schedules.

## Implementation

The benchmark lives in:

- `experiments/ssrm_3d_multi_week_apprenticeship_skill_transfer_tool_career_bridge.py`
- `visualizations/ssrm_3d_multi_week_apprenticeship_skill_transfer_tool_career_bridge.html`

It consumes the Report 192 state artifact:

- `artifacts/ssrm_3d_agent_led_settlement_work_social_project_schedule_bridge_state.json`

For each deterministic week and agent tick, the loop performs:

1. initializes careers from Report 192 roles and schedule memories
2. assigns mentor/apprentice edges in a stable teaching ring
3. selects role-fitting or stretch skills for practice
4. applies deliberate practice and mentor transfer gains
5. updates tool affinity and tool lineage marks
6. improves craft quality through tool familiarity
7. grows apprentice autonomy when skill crosses a practical threshold
8. balances fatigue during repeated learning
9. stores career identity and career memories
10. exports privacy-preserving replay packets with public skill, tool, mentor, and lineage state

## Metrics

The benchmark reports:

- `multi_week_apprenticeship_rate`
- `mentor_assignment_rate`
- `skill_practice_rate`
- `skill_transfer_rate`
- `tool_specialization_rate`
- `career_identity_stability_rate`
- `teaching_lineage_rate`
- `craft_quality_improvement_rate`
- `project_role_fit_rate`
- `apprentice_autonomy_growth_rate`
- `fatigue_learning_balance_rate`
- `schedule_memory_binding_rate`
- `frequency_flower_career_rhythm_rate`
- `browser_career_replay_rate`
- `privacy_preservation_rate`
- `trace_integrity`
- `apprenticeship_career_readiness`

## Deterministic run

Command:

```bash
python3 -m experiments.ssrm_3d_multi_week_apprenticeship_skill_transfer_tool_career_bridge
```

Observed output:

```text
module_verdict pass
apprenticeship_career_readiness 0.992500
career_events 24
no_apprenticeship_loss 0.700000
no_skill_transfer_loss 0.090000
no_tool_specialization_loss 0.080000
```

## Artifacts

Generated artifacts:

- `artifacts/ssrm_3d_multi_week_apprenticeship_skill_transfer_tool_career_bridge_eval.csv`
- `artifacts/ssrm_3d_multi_week_apprenticeship_skill_transfer_tool_career_bridge_verdict.csv`
- `artifacts/ssrm_3d_multi_week_apprenticeship_skill_transfer_tool_career_bridge_results.json`
- `artifacts/ssrm_3d_multi_week_apprenticeship_skill_transfer_tool_career_bridge_results.js`
- `artifacts/ssrm_3d_multi_week_apprenticeship_skill_transfer_tool_career_bridge_trace.json`
- `artifacts/ssrm_3d_multi_week_apprenticeship_skill_transfer_tool_career_bridge_trace.js`
- `artifacts/ssrm_3d_multi_week_apprenticeship_skill_transfer_tool_career_bridge_state.json`
- `artifacts/ssrm_3d_multi_week_apprenticeship_skill_transfer_tool_career_bridge_state.js`

## Interpretation

The pass means career differentiation is now causal rather than decorative:

- removing apprenticeship loses `0.700000`
- removing skill transfer loses `0.090000`
- removing tool specialization loses `0.080000`
- career identity, teaching lineage, schedule-memory binding, craft quality, autonomy, fatigue balance, replay, privacy, and frequency/flower rhythm remain explicit channels

This is still a deterministic seed. It does not prove open-ended vocational emergence or subjective selfhood. It gives the playable world a stronger substrate for agents who have histories, specialties, tools, teachers, and work identities.

## Boundary

The bridge uses functional career variables only. It does not imply that agents experience vocation, pride, duty, work, exploitation, or moral status. Tool specialization is simulated artificial-life behavior, not real labor. The browser viewer is a replayable apprenticeship substrate, not a complete 3D world.

## Next gate

The next useful gate is guild memory, craft standards, certification, and intergenerational tool inheritance: agents should preserve standards, evaluate work quality, pass named tools and craft marks across cohorts, and remember who is trusted for which craft.
