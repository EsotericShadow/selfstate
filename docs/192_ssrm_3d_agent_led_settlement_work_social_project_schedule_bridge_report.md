# Report 192: SSRM-3D Agent-led Settlement Work, Social Obligation, and Project Schedule Bridge

## Summary

Report 192 extends seasonal logistics into settlement-level work scheduling. Agents now coordinate seasonal work plans, role assignments, rest and care balance, promise obligations, project dependencies, repair/gather/teach/care rotation, conflict resolution, schedule adaptation, fatigue guardrails, social obligation memory, logistics dependency binding, seasonal project progress, frequency/flower work rhythms, and browser replay.

This is a deterministic settlement-schedule substrate. It is not subjective obligation, subjective suffering, subjective consciousness, moral patienthood, real labor, or complete 3D gameplay.

## Why this report exists

Report 191 gave agents seasonal stock planning for food, water, shelter, and medicine. But stock planning alone does not make a settlement feel inhabited. A convincing artificial-life settlement needs work to be distributed through roles, promises, social obligations, rest constraints, and project dependencies.

Report 192 adds that layer. The agents now schedule who repairs, gathers, teaches, cares, rests, keeps promises, resolves conflict, and advances settlement projects under seasonal pressure.

## Implementation

The benchmark lives in:

- `experiments/ssrm_3d_agent_led_settlement_work_social_project_schedule_bridge.py`
- `visualizations/ssrm_3d_agent_led_settlement_work_social_project_schedule_bridge.html`

It consumes the Report 191 state artifact:

- `artifacts/ssrm_3d_agent_led_seasonal_logistics_stock_planning_bridge_state.json`

For each deterministic day and agent tick, the loop performs:

1. selects the current seasonal context
2. assigns work from agent role, season, fatigue, promises, project dependencies, and stock constraints
3. adapts schedules for storm/cold pressure and fatigue guardrails
4. applies work effects to fatigue, social debt, promises, stocks, teaching credit, and project progress
5. records social obligation memory
6. binds work choices back to prior logistics memories and available stocks
7. exports replay packets with public task, role, project, stock, and fatigue state
8. hides private task preference and fatigue projection unless privacy is ablated

## Metrics

The benchmark reports:

- `seasonal_work_schedule_rate`
- `role_assignment_rate`
- `rest_care_balance_rate`
- `promise_obligation_rate`
- `project_dependency_rate`
- `repair_gather_teach_balance_rate`
- `conflict_resolution_rate`
- `schedule_adaptation_rate`
- `fatigue_guardrail_rate`
- `social_obligation_memory_rate`
- `logistics_dependency_binding_rate`
- `seasonal_project_progress_rate`
- `frequency_flower_schedule_rhythm_rate`
- `browser_schedule_replay_rate`
- `privacy_preservation_rate`
- `trace_integrity`
- `settlement_schedule_readiness`

## Deterministic run

Command:

```bash
python3 -m experiments.ssrm_3d_agent_led_settlement_work_social_project_schedule_bridge
```

Observed output:

```text
module_verdict pass
settlement_schedule_readiness 0.963148
schedule_events 54
no_seasonal_schedule_loss 0.522593
no_project_dependencies_loss 0.130370
no_social_obligation_memory_loss 0.070000
```

## Artifacts

Generated artifacts:

- `artifacts/ssrm_3d_agent_led_settlement_work_social_project_schedule_bridge_eval.csv`
- `artifacts/ssrm_3d_agent_led_settlement_work_social_project_schedule_bridge_verdict.csv`
- `artifacts/ssrm_3d_agent_led_settlement_work_social_project_schedule_bridge_results.json`
- `artifacts/ssrm_3d_agent_led_settlement_work_social_project_schedule_bridge_results.js`
- `artifacts/ssrm_3d_agent_led_settlement_work_social_project_schedule_bridge_trace.json`
- `artifacts/ssrm_3d_agent_led_settlement_work_social_project_schedule_bridge_trace.js`
- `artifacts/ssrm_3d_agent_led_settlement_work_social_project_schedule_bridge_state.json`
- `artifacts/ssrm_3d_agent_led_settlement_work_social_project_schedule_bridge_state.js`

## Interpretation

The pass means settlement work scheduling is now causal rather than decorative:

- removing seasonal scheduling produces the largest loss: `0.522593`
- removing project dependencies loses `0.130370`
- removing social obligation memory loses `0.070000`
- logistics dependency binding, adaptation, fatigue guardrails, role assignment, rest/care balance, promises, conflict resolution, replay, privacy, and frequency/flower rhythm remain explicit channels

Two implementation corrections happened during this report:

- The first draft treated adaptation as only rare emergency switching. The final model scores adaptation as both explicit storm/cold replanning and continuous season-aware scheduled work.
- A passing run initially produced readiness above `1.0` because the weights summed above one. The final weights reduce non-gate-heavy role, rest/care, repair/gather/teach, and replay weights so readiness is bounded at `0.963148`.

## Boundary

The bridge uses functional schedule variables only. It does not imply that agents experience subjective duty, work, suffering, or moral status. Work rotation is simulated artificial-life behavior, not real labor. The browser viewer is a replayable schedule substrate, not a complete 3D world.

## Next gate

The next useful gate is multi-week apprenticeship, skill transfer, and tool-specialization careers: agents should develop persistent specialties, teach skills, inherit craft practices, and become differentiated workers over longer time horizons.
