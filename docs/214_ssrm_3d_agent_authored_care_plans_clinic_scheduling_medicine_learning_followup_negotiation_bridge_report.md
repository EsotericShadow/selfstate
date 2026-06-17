# Report 214: SSRM-3D Agent-Authored Care Plans, Clinic Scheduling Conflicts, Medicine Learning, and Autonomous Follow-Up Negotiation Bridge

## Purpose

Report 214 extends the playable clinic loop so agents author their own care plans instead of only receiving clinic actions. The target is that agents can specify preferred care windows, refused medicines, acceptable boundaries, scheduling constraints, learned side effects, and follow-up negotiation terms.

This is a deterministic care-plan substrate only. It does not claim real medicine, real care, real consent, subjective suffering, subjective consciousness, moral patienthood, or complete artificial life.

## What changed

The bridge adds:

- agent-authored care plans for Ari, Fay, and Milo
- consent-memory binding into authored plans
- side-effect-aware medicine learning
- autonomous follow-up requests
- scheduling conflict detection
- negotiated counter-times
- unresolved follow-up honesty when an agent rejects a counter-time
- plan-respected completion checks
- boundary term recall for wrist touch, hosting, cup refusal, and map-line distance
- medicine learning updates for sweet root, bitter herb, clean cloth, and lamp rest
- public/private boundary preservation
- frequency and flower-ring care-plan rhythm
- browser replay of care-plan negotiation

## Deterministic scenario

The run spans twenty-four care-plan steps.

- Ari authors a no-sedation wrist plan, requests dawn dry-wrap care, learns to avoid sweet root before repair work, rejects one counter-time, and leaves one follow-up unresolved.
- Fay authors a low-light nausea-safe plan, accepts a schedule counter-time, learns bitter herb should be conditional after nausea, and revises the plan to check hosting before herb offers.
- Milo authors a route-edge distance plan, requests care without prompting, negotiates a dusk counter-time, and preserves cloth/cup/map boundaries separately.

## Metrics

| Metric | Value |
| --- | ---: |
| care_plan_negotiation_readiness | 0.908333 |
| care_plan_steps | 24 |
| agent_authored_plan_rate | 1.000000 |
| plan_consent_memory_binding | 1.000000 |
| side_effect_learning_rate | 0.750000 |
| scheduling_conflict_detection | 1.000000 |
| schedule_conflict_resolution_rate | 0.666667 |
| autonomous_followup_request_rate | 1.000000 |
| negotiated_followup_success_rate | 0.666667 |
| followup_completion_rate | 0.833333 |
| plan_respect_rate | 1.000000 |
| boundary_term_recall_rate | 0.875000 |
| medicine_learning_update_rate | 0.833333 |
| unresolved_conflict_honesty | 1.000000 |
| public_private_boundary_score | 1.000000 |
| frequency_flower_care_plan_rhythm | 1.000000 |
| browser_care_plan_replay_available | 1.000000 |

The weak scheduling channels are intentional. Ari rejects one counter-time because it would break his inventory order, and the clinic leaves the follow-up unresolved rather than forcing care. That is the correct failure mode for agent-authored plans.

## Ablations

| Ablation | Readiness loss |
| --- | ---: |
| no_agent_authored_plans | 0.330000 |
| no_scheduling_conflicts | 0.260000 |
| no_consent_memory_binding | 0.240000 |
| no_medicine_learning | 0.220000 |
| no_autonomous_followup | 0.200000 |
| no_unresolved_conflict_trace | 0.120000 |
| no_boundary_term_recall | 0.110000 |
| no_frequency_flower_care_plan_rhythm | 0.055000 |

The largest loss comes from removing agent-authored plans. Without them, the clinic remains avatar-centered. Scheduling conflicts and consent-memory binding are next because they determine whether care plans actually constrain the clinic.

## Artifacts

- `artifacts/ssrm_3d_agent_authored_care_plans_clinic_scheduling_medicine_learning_followup_negotiation_bridge_events.csv`
- `artifacts/ssrm_3d_agent_authored_care_plans_clinic_scheduling_medicine_learning_followup_negotiation_bridge_care_plans.csv`
- `artifacts/ssrm_3d_agent_authored_care_plans_clinic_scheduling_medicine_learning_followup_negotiation_bridge_schedule_ledger.csv`
- `artifacts/ssrm_3d_agent_authored_care_plans_clinic_scheduling_medicine_learning_followup_negotiation_bridge_medicine_learning.csv`
- `artifacts/ssrm_3d_agent_authored_care_plans_clinic_scheduling_medicine_learning_followup_negotiation_bridge_followup_negotiation.csv`
- `artifacts/ssrm_3d_agent_authored_care_plans_clinic_scheduling_medicine_learning_followup_negotiation_bridge_conflict_ledger.csv`
- `artifacts/ssrm_3d_agent_authored_care_plans_clinic_scheduling_medicine_learning_followup_negotiation_bridge_results.json`
- `artifacts/ssrm_3d_agent_authored_care_plans_clinic_scheduling_medicine_learning_followup_negotiation_bridge_state.json`
- `artifacts/ssrm_3d_agent_authored_care_plans_clinic_scheduling_medicine_learning_followup_negotiation_bridge_verdict.csv`
- `visualizations/ssrm_3d_agent_authored_care_plans_clinic_scheduling_medicine_learning_followup_negotiation_bridge.html`

## Run command

```bash
python3 -m experiments.ssrm_3d_agent_authored_care_plans_clinic_scheduling_medicine_learning_followup_negotiation_bridge --seed 20260827 --steps 24
```

Observed output:

```text
module_verdict pass
care_plan_negotiation_readiness 0.908333
care_plan_steps 24
agent_authored_plan_rate 1.000000
schedule_conflict_resolution_rate 0.666667
followup_completion_rate 0.833333
next_gate agent-authored treatment norms, clinic reputation, medicine evidence ledgers, and multi-agent care governance
```

## Honest limitation

This report proves deterministic care-plan negotiation wiring, not real medicine, consent, or care. Agents author plans from scripted state, scheduling negotiation is bounded, medicine learning is rule-based, and one follow-up remains unresolved. The next step needs clinic reputation, evidence ledgers, and multi-agent care governance so care norms can be inspected publicly instead of living only inside individual plans.

## Next gate

The next gate is agent-authored treatment norms, clinic reputation, medicine evidence ledgers, and multi-agent care governance.
