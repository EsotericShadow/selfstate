# Report 216: SSRM-3D playable public health governance, outbreak quarantine, appeals, and trust recovery bridge

## Status

Pass. The deterministic bridge generated a playable public-health governance substrate with outbreak signals, noisy-signal rejection, reversible quarantine or spacing policies, consent records, care access during restriction, clinic appeals, privacy and stigma guardrails, trust recovery, frequency/flower timing, and browser replay.

This is not real medicine, epidemiology, public-health authority, real consent, subjective suffering, consciousness, or moral patienthood.

## Purpose

Report 215 made clinic treatment norms inspectable: agents could author norms, bind them to evidence, vote, defer weak-consent norms, preserve refusal privacy, and update clinic reputation. Report 216 moves that clinic governance into messier playable public health.

The target is a small first-person artificial-life world where agents can live through outbreak-like uncertainty without the system becoming a command-and-control toy. Restrictions must be evidence-linked, reversible, appealable, privacy-preserving, and socially repairable.

## Files

- `experiments/ssrm_3d_playable_public_health_governance_outbreak_quarantine_appeals_trust_recovery_bridge.py`
- `visualizations/ssrm_3d_playable_public_health_governance_outbreak_quarantine_appeals_trust_recovery_bridge.html`
- `artifacts/ssrm_3d_playable_public_health_governance_outbreak_quarantine_appeals_trust_recovery_bridge_events.csv`
- `artifacts/ssrm_3d_playable_public_health_governance_outbreak_quarantine_appeals_trust_recovery_bridge_outbreak_ledger.csv`
- `artifacts/ssrm_3d_playable_public_health_governance_outbreak_quarantine_appeals_trust_recovery_bridge_quarantine_consent.csv`
- `artifacts/ssrm_3d_playable_public_health_governance_outbreak_quarantine_appeals_trust_recovery_bridge_appeals_ledger.csv`
- `artifacts/ssrm_3d_playable_public_health_governance_outbreak_quarantine_appeals_trust_recovery_bridge_trust_recovery.csv`
- `artifacts/ssrm_3d_playable_public_health_governance_outbreak_quarantine_appeals_trust_recovery_bridge_public_health_policy.csv`
- `artifacts/ssrm_3d_playable_public_health_governance_outbreak_quarantine_appeals_trust_recovery_bridge_replay.json`
- `artifacts/ssrm_3d_playable_public_health_governance_outbreak_quarantine_appeals_trust_recovery_bridge_results.json`
- `artifacts/ssrm_3d_playable_public_health_governance_outbreak_quarantine_appeals_trust_recovery_bridge_state.json`
- `artifacts/ssrm_3d_playable_public_health_governance_outbreak_quarantine_appeals_trust_recovery_bridge_verdict.csv`

## Deterministic run

```bash
python3 experiments/ssrm_3d_playable_public_health_governance_outbreak_quarantine_appeals_trust_recovery_bridge.py --seed 20260829
```

Output:

```text
module_verdict pass
public_health_governance_readiness 0.888849
outbreak_signals 8
public_health_policies 3
quarantine_consent_records 8
appeals 4
appeal_resolution_rate 0.750000
community_trust_recovery_rate 0.734200
weakest_channel_score 0.600000
visualization visualizations/ssrm_3d_playable_public_health_governance_outbreak_quarantine_appeals_trust_recovery_bridge.html
next_gate playable community-scale crisis governance with resource triage, rumor dynamics, restorative appeals, and long-term trust memory
```

## Public-health object loop

The bridge adds explicit objects rather than a single score pass.

| Object | Function |
| --- | --- |
| `OutbreakSignal` | Captures local symptom/contact/uncertainty signals, false positives, irrelevant failing signals, evidence strength, public summary, sealed private digest, vibration rate, and flower node. |
| `PolicyProposal` | Captures reversible spacing or quarantine-like restrictions, evidence links, rollback condition, care-access plan, review cadence, public message, minority note, frequency, and flower node. |
| `ConsentRecord` | Captures agent-specific consent, conditional consent, refusal, boundary, accommodation, pressure score, punishment flag, dignity preservation, sealed workspace flag, and trust delta. |
| `AppealRecord` | Captures appeal basis, requested change, evidence gap, reviewer set, decision, resolution state, rollback adjustment, minority note, dignity, and trust delta. |
| `TrustRecoveryRecord` | Captures social damage, repair action, trust before/after, unresolved debt, relationship memory, and visible behavior. |
| `EventRecord` | Binds the public event, private digest, body effect, trust effect, containment effect, readable marker, frequency, and flower phase. |
| `ReplayFrame` | Converts governance events into browser-readable first-person replay frames with avatar position, panel focus, private boundary, frequency overlay, and flower overlay. |

The integrated loop is:

```text
browser tick
-> local sensory/public-health sample
-> outbreak signal object
-> noisy or false-positive review
-> reversible policy proposal
-> quarantine or spacing consent record
-> care-access preservation
-> appeal review
-> rollback or adjustment
-> trust recovery memory
-> visible behavior marker
-> replay frame
```

## Scenario coverage

The generated scenario includes:

- `4` agents: Ari, Fay, Milo, and Nia.
- `8` outbreak signals, including real-looking clusters, false positives, and irrelevant failing signals.
- `3` reversible public-health policies.
- `8` quarantine or spacing consent records, including conditional consent and refusal.
- `4` appeals, with `3` resolved and `1` deferred.
- `5` trust-recovery records.
- `28` replayable governance events.

The design keeps refusals playable. Milo can refuse a route restriction without punishment. Nia can defer privacy-sensitive publication without private-workspace leakage. Fay can appeal because a technically reasonable shared-cup pause damages attachment rituals. Ari can demand an urgent repair lane so public-health governance does not break infrastructure maintenance.

## Metrics

| Metric | Score |
| --- | ---: |
| public_health_governance_readiness | `0.888849` |
| outbreak_signal_detection | `0.600000` |
| irrelevant_signal_rejection | `1.000000` |
| quarantine_consent_integrity | `1.000000` |
| care_access_under_restriction | `1.000000` |
| appeal_review_rate | `1.000000` |
| appeal_resolution_rate | `0.750000` |
| privacy_stigma_guardrail | `0.875000` |
| community_trust_recovery_rate | `0.734200` |
| refusal_without_punishment_rate | `1.000000` |
| evidence_policy_traceability | `1.000000` |
| outbreak_containment_traceability | `0.678571` |
| minority_objection_traceability | `1.000000` |
| public_private_boundary_score | `1.000000` |
| frequency_flower_public_health_rhythm | `1.000000` |
| browser_public_health_replay_available | `1.000000` |
| policy_rollback_readiness | `1.000000` |
| noisy_signal_honesty | `1.000000` |
| weakest_channel_score | `0.600000` |
| mean_governance_channel_score | `0.909185` |

## Ablations

| Ablation | Readiness after removal |
| --- | ---: |
| no_quarantine_consent | `0.568849` |
| no_outbreak_signal_ledger | `0.598849` |
| no_appeals | `0.618849` |
| no_privacy_stigma_guardrail | `0.638849` |
| no_care_access_plan | `0.648849` |
| no_trust_recovery | `0.668849` |
| no_noisy_signal_honesty | `0.708849` |
| no_frequency_flower_rhythm | `0.808849` |
| no_browser_replay | `0.828849` |

Consent and outbreak ledgers dominate because restrictions without consent or evidence become brittle and socially unsafe. Appeals, privacy/stigma guardrails, care access, and trust recovery are also high-impact because they keep restrictions playable instead of coercive.

## Honest interpretation

The bridge passes, but it is not clean.

Signal detection is only `0.600000`, because the simulation deliberately includes weak or ambiguous signals. Containment traceability is `0.678571`, because not every event directly improves containment. Appeal resolution is `0.750000`, because Nia's privacy appeal remains deferred until another sensory sample arrives. Trust recovery is `0.734200`, because social repair is partial and unresolved debt remains.

That is the point. Public-health governance should not look perfect in a little-people world. A playable agent society needs evidence, consent, refusal, appeal, care access, rollback, and recovery loops, not just restriction success.

## Boundary

This report proves deterministic wiring for public-health-like governance inside an artificial-life benchmark. It does not prove real medical judgment, real public-health validity, real consent, subjective feeling, suffering, consciousness, or moral patienthood.

The frequency and flower-of-life overlays are inspectable rhythm/phase scaffolds for the simulation. They are not metaphysical evidence.

## Next gate

Report 217 should add playable community-scale crisis governance with resource triage, rumor dynamics, restorative appeals, and long-term trust memory. The next bridge should test what happens when public-health rules compete with scarce supplies, inaccurate rumors, role reputation, and delayed social repair.
