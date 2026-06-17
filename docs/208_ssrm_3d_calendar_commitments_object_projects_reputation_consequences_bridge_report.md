# Report 208: SSRM-3D Calendar Commitments, Object Projects, and Reputation Consequences Bridge

## Purpose

Report 208 extends long-horizon personality and routine continuity into longer playable arcs. The target is that agents can make dated commitments, maintain object-centered projects, notice missed due windows, narrow or widen avatar access, and preserve reputation consequences across multi-week review.

This is a deterministic bridge. It does not claim real memory, real consent, subjective consciousness, moral patienthood, or complete artificial life.

## What changed

The bridge adds:

- calendar commitments with made days, due days, resolution days, and repair days
- three agent-owned object projects with staged progress
- commitment consequences that affect avatar access
- object ownership preservation during collaboration
- a deliberately missed Fay commitment that lowers trust and narrows access
- partial repair that helps without erasing the miss
- multi-week review where consequences remain visible after the immediate event
- public/private boundary preservation through sealed private workspace digests
- frequency and flower-ring arc rhythm for every commitment event
- browser replay of the commitment, project, and reputation arc

## Deterministic scenario

The run spans twenty-one days, three agents, nine commitments, and three object projects.

- Ari owns the `notched brace gauge` and works on west brace calibration.
- Fay owns the `warm blue blanket` and works on a stove-corner comfort kit.
- Milo owns the `folded route map` and works on a quiet route archive.

Eight commitments are fulfilled cleanly. One Fay check-in commitment is missed, acknowledged, and later partially repaired. The miss remains in her history and in the access state; it is not erased by repair.

## Metrics

| Metric | Value |
| --- | ---: |
| calendar_object_reputation_readiness | 0.969996 |
| arc_days | 21 |
| arc_events | 23 |
| total_commitments | 9 |
| resolved_commitments | 9 |
| calendar_commitment_integrity | 1.000000 |
| commitment_fulfillment_rate | 0.888889 |
| clean_or_repaired_resolution_rate | 1.000000 |
| object_project_continuity | 0.800000 |
| object_ownership_preservation | 1.000000 |
| reputation_consequence_persistence | 1.000000 |
| missed_commitment_penalty_traceability | 1.000000 |
| repair_without_erasure_rate | 1.000000 |
| access_modulation_by_reputation | 1.000000 |
| multi_week_memory_traceability | 0.921053 |
| public_private_boundary_score | 1.000000 |
| frequency_flower_arc_rhythm | 1.000000 |
| browser_arc_replay_available | 1.000000 |

The clean fulfillment rate is intentionally below perfect. The point of the bridge is not to make the avatar flawless. The point is to make missed commitments matter and make repair visible without pretending the miss never happened.

## Ablations

| Ablation | Readiness loss |
| --- | ---: |
| no_calendar | 0.330000 |
| no_reputation_consequences | 0.290000 |
| no_object_projects | 0.270000 |
| no_missed_commitment_penalty | 0.170000 |
| no_ownership_preservation | 0.150000 |
| no_repair_without_erasure | 0.130000 |
| no_multi_week_trace | 0.100000 |
| no_frequency_flower_arc_rhythm | 0.055000 |

The largest losses come from removing calendars, reputation consequences, and object projects. That is the expected result: without these, multi-day life remains conversational rather than project-bearing.

## Artifacts

- `artifacts/ssrm_3d_calendar_commitments_object_projects_reputation_consequences_bridge_events.csv`
- `artifacts/ssrm_3d_calendar_commitments_object_projects_reputation_consequences_bridge_weekly_summary.csv`
- `artifacts/ssrm_3d_calendar_commitments_object_projects_reputation_consequences_bridge_commitment_ledger.csv`
- `artifacts/ssrm_3d_calendar_commitments_object_projects_reputation_consequences_bridge_project_ledger.csv`
- `artifacts/ssrm_3d_calendar_commitments_object_projects_reputation_consequences_bridge_reputation_consequences.csv`
- `artifacts/ssrm_3d_calendar_commitments_object_projects_reputation_consequences_bridge_results.json`
- `artifacts/ssrm_3d_calendar_commitments_object_projects_reputation_consequences_bridge_state.json`
- `artifacts/ssrm_3d_calendar_commitments_object_projects_reputation_consequences_bridge_verdict.csv`
- `visualizations/ssrm_3d_calendar_commitments_object_projects_reputation_consequences_bridge.html`

## Run command

```bash
python3 -m experiments.ssrm_3d_calendar_commitments_object_projects_reputation_consequences_bridge --seed 20260821 --days 21
```

Observed output:

```text
module_verdict pass
calendar_object_reputation_readiness 0.969996
arc_days 21
arc_events 23
commitment_fulfillment_rate 0.888889
clean_or_repaired_resolution_rate 1.000000
next_gate agent-owned project economy with materials, wear, debt, gifts, trade, and refusal-sensitive labor
```

## Honest limitation

This report proves deterministic long-arc continuity wiring, not real social life. The commitments, projects, penalties, and repairs are scripted state transitions. Agents do not freely invent obligations, negotiate real contracts, understand consequences subjectively, or possess moral patienthood. The next step needs material economy and refusal-sensitive labor so projects become physically constrained rather than only calendar-constrained.

## Next gate

The next gate is agent-owned project economy with materials, wear, debt, gifts, trade, and refusal-sensitive labor.
