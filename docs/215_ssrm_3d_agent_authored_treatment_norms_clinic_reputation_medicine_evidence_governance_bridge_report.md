# Report 215: SSRM-3D Agent-Authored Treatment Norms, Clinic Reputation, Medicine Evidence Ledgers, and Multi-Agent Care Governance Bridge

## Purpose

Report 215 moves clinic care from private plans into public multi-agent governance. The target is that agents can author treatment norms, attach medicine evidence, vote, preserve minority notes, update clinic reputation, defer weak norms, and inspect care governance without leaking private workspace state.

This is a deterministic treatment-norm substrate only. It does not claim real medicine, real care, real consent, subjective suffering, subjective consciousness, moral patienthood, or complete artificial life.

## What changed

The bridge adds:

- agent-authored treatment norm proposals
- public medicine evidence ledger with outcomes, side effects, consent state, boundaries, and confidence
- norm-to-evidence traceability
- multi-agent votes with adoption, abstention, and deferral
- minority notes instead of forced consensus
- clinic reputation channels for consent respect, side-effect honesty, stock reliability, follow-up reliability, boundary respect, and evidence transparency
- a deferred separate-cup norm because Milo's consent evidence is weak
- refusal privacy as an adopted treatment norm
- public/private boundary preservation
- frequency and flower-ring governance rhythm
- browser replay of care governance

## Deterministic scenario

The run includes six norm proposals and twelve evidence cases.

- Ari authors no-sedation-before-repair and stockout-disclosure norms.
- Fay authors bitter-herb-hosting-check and separate-cup cough norms.
- Milo authors route-edge-care and refusal-privacy norms.
- The separate-cup norm is deferred because Milo refused cup replacement and the consent evidence is not strong enough.
- Refusal privacy is adopted so care refusals can update safety ledgers without becoming public shame evidence.

## Metrics

| Metric | Value |
| --- | ---: |
| care_governance_readiness | 0.935365 |
| governance_events | 6 |
| evidence_cases | 12 |
| treatment_norms | 6 |
| agent_authored_norm_rate | 1.000000 |
| medicine_evidence_ledger_integrity | 1.000000 |
| evidence_to_norm_traceability | 1.000000 |
| multi_agent_governance_participation | 1.000000 |
| norm_adoption_rate | 0.833333 |
| deferred_norm_honesty | 1.000000 |
| minority_record_integrity | 1.000000 |
| clinic_reputation_update_rate | 1.000000 |
| mean_clinic_reputation_score | 0.715833 |
| consent_norm_preservation | 1.000000 |
| side_effect_evidence_binding | 0.416667 |
| stockout_evidence_traceability | 1.000000 |
| privacy_refusal_norm_present | 1.000000 |
| public_private_boundary_score | 1.000000 |
| frequency_flower_governance_rhythm | 1.000000 |
| browser_governance_replay_available | 1.000000 |

The weak channels are intentional. Side-effect evidence binding is only `0.416667` because not all evidence cases involve side effects. Clinic reputation is `0.715833` because governance improves transparency but does not magically repair stock reliability or follow-up reliability.

## Ablations

| Ablation | Readiness loss |
| --- | ---: |
| no_agent_authored_norms | 0.320000 |
| no_evidence_ledger | 0.300000 |
| no_clinic_reputation | 0.240000 |
| no_multi_agent_governance | 0.230000 |
| no_deferred_norm_trace | 0.160000 |
| no_side_effect_evidence | 0.150000 |
| no_refusal_privacy_norm | 0.120000 |
| no_frequency_flower_governance_rhythm | 0.055000 |

The largest loss comes from removing agent-authored norms and evidence ledgers. Without those, clinic governance becomes authority assertion instead of inspectable care practice.

## Artifacts

- `artifacts/ssrm_3d_agent_authored_treatment_norms_clinic_reputation_medicine_evidence_governance_bridge_events.csv`
- `artifacts/ssrm_3d_agent_authored_treatment_norms_clinic_reputation_medicine_evidence_governance_bridge_treatment_norms.csv`
- `artifacts/ssrm_3d_agent_authored_treatment_norms_clinic_reputation_medicine_evidence_governance_bridge_medicine_evidence_ledger.csv`
- `artifacts/ssrm_3d_agent_authored_treatment_norms_clinic_reputation_medicine_evidence_governance_bridge_clinic_reputation.csv`
- `artifacts/ssrm_3d_agent_authored_treatment_norms_clinic_reputation_medicine_evidence_governance_bridge_governance_votes.csv`
- `artifacts/ssrm_3d_agent_authored_treatment_norms_clinic_reputation_medicine_evidence_governance_bridge_agent_governance.csv`
- `artifacts/ssrm_3d_agent_authored_treatment_norms_clinic_reputation_medicine_evidence_governance_bridge_results.json`
- `artifacts/ssrm_3d_agent_authored_treatment_norms_clinic_reputation_medicine_evidence_governance_bridge_state.json`
- `artifacts/ssrm_3d_agent_authored_treatment_norms_clinic_reputation_medicine_evidence_governance_bridge_verdict.csv`
- `visualizations/ssrm_3d_agent_authored_treatment_norms_clinic_reputation_medicine_evidence_governance_bridge.html`

## Run command

```bash
python3 -m experiments.ssrm_3d_agent_authored_treatment_norms_clinic_reputation_medicine_evidence_governance_bridge --seed 20260828
```

Observed output:

```text
module_verdict pass
care_governance_readiness 0.935365
governance_events 6
evidence_cases 12
treatment_norms 6
norm_adoption_rate 0.833333
mean_clinic_reputation_score 0.715833
next_gate playable public health governance with outbreaks, quarantine consent, clinic appeals, and community trust recovery
```

## Honest limitation

This report proves deterministic clinic-governance wiring, not real medical authority. Evidence confidence is scripted, votes are deterministic, and reputation is only a functional score. The deferred separate-cup norm is the important result: multi-agent care governance must preserve dissent and weak consent evidence rather than forcing clean policy.

## Next gate

The next gate is playable public health governance with outbreaks, quarantine consent, clinic appeals, and community trust recovery.
