# Report 211: SSRM-3D Seasonal Body Ecology, Illness Risk, Communal Care, and Market-Relationship Stress Bridge

## Purpose

Report 211 extends the needs marketplace into seasonal body ecology. The target is that market pressure should affect bodies and relationships, not just prices and ledgers. Wetness, cold, hunger, fatigue, illness risk, symptoms, communal care, care capacity, market stress, and relationship strain now persist across a seasonal arc.

This is a deterministic body-ecology substrate only. It does not claim real illness, real care, subjective suffering, subjective consciousness, moral patienthood, or complete artificial life.

## What changed

The bridge adds:

- four seasonal body regimes: wet chill, cold scarcity, thaw sickness, and dry recovery
- body state ledgers for hunger, warmth deficit, wetness, fatigue, illness risk, symptoms, and pain
- season drift that raises or lowers body pressures
- illness-risk coupling from wetness, warmth deficit, hunger, and market stress
- communal care events with care capacity costs
- hunger/warmth tradeoffs under market pressure
- delayed care that helps only partially
- body-limit refusal that preserves autonomy
- market stress that damages relationships
- partial relationship repair rather than automatic forgiveness
- bounded negative-state rules so illness and symptoms do not spiral indefinitely
- residual distress honesty so incomplete recovery remains visible
- frequency and flower-ring body rhythm
- browser replay of body ecology and relationship stress

## Deterministic scenario

The run spans seventy-two days and twenty-four body ecology events.

- Ari gets wet during route work, receives care, develops wrist ache after repeated wet labor, refuses night labor, and partially recovers in dry season.
- Fay chooses food over heat, develops a cough, spends care capacity helping others, recovers after protected low-light nights, and hosts a care meal that helps warmth but costs energy.
- Milo carries debt-linked hunger and avoidance, gets food help, chooses food debt over warmth, receives archive draft care, partially repairs relationship damage, and ends with residual debt-linked stress.

## Metrics

| Metric | Value |
| --- | ---: |
| seasonal_body_ecology_readiness | 0.934694 |
| body_ecology_days | 72 |
| body_ecology_events | 24 |
| seasonal_exposure_binding | 1.000000 |
| illness_risk_traceability | 1.000000 |
| hunger_warmth_tradeoff_rate | 1.000000 |
| communal_care_response_rate | 0.800000 |
| care_capacity_pressure_traceability | 1.000000 |
| market_stress_relationship_binding | 1.000000 |
| relationship_repair_rate | 0.285714 |
| illness_recovery_rate | 1.000000 |
| bounded_negative_state_score | 1.000000 |
| residual_distress_honesty | 1.000000 |
| body_state_trace_integrity | 1.000000 |
| public_private_boundary_score | 1.000000 |
| frequency_flower_body_rhythm | 1.000000 |
| browser_body_ecology_replay_available | 1.000000 |

The low relationship repair score is deliberate. Body and market stress now create real continuity pressure: not every tension event repairs within the same seasonal arc. This is a useful failure mode because it forces the next gate toward player-intervention triage and consent-aware care.

## Ablations

| Ablation | Readiness loss |
| --- | ---: |
| no_body_state | 0.330000 |
| no_illness_risk | 0.260000 |
| no_communal_care | 0.240000 |
| no_market_relationship_stress | 0.210000 |
| no_hunger_warmth_tradeoffs | 0.180000 |
| no_care_capacity | 0.150000 |
| no_bounded_recovery | 0.120000 |
| no_frequency_flower_body_rhythm | 0.055000 |

The largest loss comes from removing body state. Without body state, illness and care reduce to narrative flags. Removing illness risk, communal care, or market relationship stress also removes the main bridge from economy into embodied little-person continuity.

## Artifacts

- `artifacts/ssrm_3d_seasonal_body_ecology_illness_care_market_relationship_bridge_events.csv`
- `artifacts/ssrm_3d_seasonal_body_ecology_illness_care_market_relationship_bridge_body_ledger.csv`
- `artifacts/ssrm_3d_seasonal_body_ecology_illness_care_market_relationship_bridge_care_ledger.csv`
- `artifacts/ssrm_3d_seasonal_body_ecology_illness_care_market_relationship_bridge_illness_ledger.csv`
- `artifacts/ssrm_3d_seasonal_body_ecology_illness_care_market_relationship_bridge_relationship_stress.csv`
- `artifacts/ssrm_3d_seasonal_body_ecology_illness_care_market_relationship_bridge_results.json`
- `artifacts/ssrm_3d_seasonal_body_ecology_illness_care_market_relationship_bridge_state.json`
- `artifacts/ssrm_3d_seasonal_body_ecology_illness_care_market_relationship_bridge_verdict.csv`
- `visualizations/ssrm_3d_seasonal_body_ecology_illness_care_market_relationship_bridge.html`

## Run command

```bash
python3 -m experiments.ssrm_3d_seasonal_body_ecology_illness_care_market_relationship_bridge --seed 20260824 --days 72
```

Observed output:

```text
module_verdict pass
seasonal_body_ecology_readiness 0.934694
body_ecology_days 72
body_ecology_events 24
communal_care_response_rate 0.800000
relationship_repair_rate 0.285714
illness_recovery_rate 1.000000
next_gate recoverable body-care gameplay with player interventions, contagion boundaries, medicine practice, and consent-aware triage
```

## Honest limitation

This report proves deterministic body-ecology wiring, not real embodiment. Agents do not experience actual hunger, cold, illness, pain, care, or relationship distress. Care is still scripted and not player-driven. Relationship repair is weak by design in this run, which means the next step must expose care intervention to playable avatar action with consent-aware triage rather than silently repairing everything.

## Next gate

The next gate is recoverable body-care gameplay with player interventions, contagion boundaries, medicine practice, and consent-aware triage.
