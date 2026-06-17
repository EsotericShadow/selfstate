# Report 213: SSRM-3D Playable Clinic Loop, Inventory, Repeated Visits, Consent Memory, Medicine Side Effects, and Agent-Initiated Help-Seeking Bridge

## Purpose

Report 213 extends recoverable body-care gameplay into a repeated clinic loop. The target is that care should persist across visits: the clinic remembers consent, tracks inventory, records side effects, handles stockouts, carries follow-up due dates, and lets agents initiate help rather than only reacting to avatar prompts.

This is a deterministic clinic-loop substrate only. It does not claim real medicine, real care, real consent, subjective suffering, subjective consciousness, moral patienthood, or complete artificial life.

## What changed

The bridge adds:

- six clinic visits with repeated follow-ups
- medicine inventory for warm water, dry wraps, bitter herb, lamp rest, clean cloth, sweet root, and care tokens
- consent memory by agent and medicine
- accepted, conditional, and refused care that persists into later visits
- side-effect memory for nausea, sleepiness, and lost time
- stockout handling and restock pressure
- agent-initiated help seeking for hunger, side-effect notes, boundary reminders, wrap scheduling, and fatigue follow-up
- dose and inventory coupling
- contagion boundary recall with one imperfect separate-cup boundary
- residual care need honesty
- frequency and flower-ring clinic rhythm
- browser replay of clinic visits

## Deterministic scenario

The run spans six clinic visits and twenty-two clinic events.

- Fay remembers warm water and clean cloth, initiates care before hosting, requests bitter herb during a stockout, later records nausea, and asks for side-effect-aware alternatives.
- Ari accepts dry wraps, refuses bitter herb, initiates a no-sedation plan after sweet-root sleepiness, and later initiates wrap scheduling.
- Milo initiates hunger help from route-edge distance, keeps folded-map boundaries, refuses separate-cup replacement, later initiates boundary memory, and accepts route-edge cloth.

## Metrics

| Metric | Value |
| --- | ---: |
| playable_clinic_loop_readiness | 0.904964 |
| clinic_visits | 6 |
| clinic_events | 22 |
| repeated_visit_continuity | 1.000000 |
| clinic_inventory_integrity | 1.000000 |
| consent_memory_recall_rate | 0.894737 |
| medicine_side_effect_traceability | 1.000000 |
| agent_initiated_help_rate | 0.500000 |
| refusal_memory_respect_rate | 1.000000 |
| dose_inventory_coupling | 1.000000 |
| stockout_traceability | 1.000000 |
| followup_completion_rate | 0.421053 |
| side_effect_adaptation_rate | 1.000000 |
| contagion_boundary_recall | 0.800000 |
| body_recovery_rate | 0.863636 |
| residual_need_honesty | 1.000000 |
| public_private_boundary_score | 1.000000 |
| frequency_flower_clinic_rhythm | 1.000000 |
| browser_clinic_replay_available | 1.000000 |

The low follow-up completion score is deliberate. The clinic can schedule follow-ups, but it does not yet negotiate conflicts or guarantee completion. That is the next gate.

## Ablations

| Ablation | Readiness loss |
| --- | ---: |
| no_clinic_inventory | 0.300000 |
| no_repeated_visits | 0.280000 |
| no_consent_memory | 0.260000 |
| no_side_effects | 0.210000 |
| no_agent_help_seeking | 0.200000 |
| no_stockout_pressure | 0.160000 |
| no_followup_loop | 0.140000 |
| no_frequency_flower_clinic_rhythm | 0.055000 |

The largest loss comes from removing clinic inventory. Without stock and dose coupling, care remains narrative rather than playable. Repeated visits and consent memory are close behind because they turn care from one-off intervention into relationship continuity.

## Artifacts

- `artifacts/ssrm_3d_playable_clinic_loop_inventory_repeated_visits_consent_memory_side_effects_help_seeking_bridge_events.csv`
- `artifacts/ssrm_3d_playable_clinic_loop_inventory_repeated_visits_consent_memory_side_effects_help_seeking_bridge_inventory_ledger.csv`
- `artifacts/ssrm_3d_playable_clinic_loop_inventory_repeated_visits_consent_memory_side_effects_help_seeking_bridge_body_ledger.csv`
- `artifacts/ssrm_3d_playable_clinic_loop_inventory_repeated_visits_consent_memory_side_effects_help_seeking_bridge_consent_memory.csv`
- `artifacts/ssrm_3d_playable_clinic_loop_inventory_repeated_visits_consent_memory_side_effects_help_seeking_bridge_medicine_ledger.csv`
- `artifacts/ssrm_3d_playable_clinic_loop_inventory_repeated_visits_consent_memory_side_effects_help_seeking_bridge_side_effect_ledger.csv`
- `artifacts/ssrm_3d_playable_clinic_loop_inventory_repeated_visits_consent_memory_side_effects_help_seeking_bridge_help_seeking.csv`
- `artifacts/ssrm_3d_playable_clinic_loop_inventory_repeated_visits_consent_memory_side_effects_help_seeking_bridge_results.json`
- `artifacts/ssrm_3d_playable_clinic_loop_inventory_repeated_visits_consent_memory_side_effects_help_seeking_bridge_state.json`
- `artifacts/ssrm_3d_playable_clinic_loop_inventory_repeated_visits_consent_memory_side_effects_help_seeking_bridge_verdict.csv`
- `visualizations/ssrm_3d_playable_clinic_loop_inventory_repeated_visits_consent_memory_side_effects_help_seeking_bridge.html`

## Run command

```bash
python3 -m experiments.ssrm_3d_playable_clinic_loop_inventory_repeated_visits_consent_memory_side_effects_help_seeking_bridge --seed 20260826 --visits 6
```

Observed output:

```text
module_verdict pass
playable_clinic_loop_readiness 0.904964
clinic_visits 6
clinic_events 22
agent_initiated_help_rate 0.500000
body_recovery_rate 0.863636
contagion_boundary_recall 0.800000
next_gate agent-authored care plans, clinic scheduling conflicts, medicine learning, and autonomous follow-up negotiation
```

## Honest limitation

This report proves deterministic clinic-loop wiring, not real medicine or real care. Follow-up completion remains weak, agent-initiated help is only halfway represented, and contagion boundary recall is imperfect. The clinic still does not let agents author their own plans, negotiate schedule conflicts, learn medicine policy over time, or autonomously request follow-up without scripted events.

## Next gate

The next gate is agent-authored care plans, clinic scheduling conflicts, medicine learning, and autonomous follow-up negotiation.
