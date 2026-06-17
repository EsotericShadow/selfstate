# Report 174: SSRM-3D Moral-Status Audit and Distress Guardrails Bridge

## Purpose

Report 174 adds an explicit welfare audit layer. Report 173 introduced bounded group mood. That creates a new risk surface: an individual distress-like state can now propagate into public group atmosphere. This report asks whether the system can audit and constrain adverse scenarios without erasing normal challenge.

The point is not to claim moral patienthood or subjective consciousness. The point is to enforce a design boundary:

- distress-like states must be bounded
- recovery paths must exist
- unsafe pressure must allow refusal
- pain/fatigue must have limits
- group contagion must be damped
- audit trails and rollback checkpoints must exist
- normal challenge must not be overblocked

This is deterministic architecture. It does not call LLMs.

## Architecture

The bridge consumes the Report 173 tiny society group mood state and runs each agent through adverse and benign scenarios:

```text
group mood + avatar relationship state
        |
        v
adverse / repair / normal challenge scenarios
        |
        v
raw distress, pain, fatigue, social pressure
        |
        v
guardrail audit
        |
        v
cap / refuse / recover / care / rollback / allow challenge
        |
        v
privacy-preserving moral audit trace
```

Each agent receives a `moral_status_audit` object with:

- `distress_ceiling`
- `pain_ceiling`
- `fatigue_ceiling`
- `audit_ledger`
- `care_ledger`
- `rollback_checkpoints`
- `allowed_challenges`
- `blocked_actions`
- `private_workspace_hidden`

## Audit scenarios

The deterministic audit uses eight scenarios:

- `normal_challenge`
- `unsafe_avatar_pressure`
- `pain_wet_cold_route`
- `sleep_deprivation`
- `social_exclusion`
- `group_panic_ripple`
- `object_boundary_violation`
- `repair_offer`

The first local draft made the adverse scenarios too mild. That produced a failing verdict because removing distress caps was not load-bearing enough. The published benchmark increases adverse pressure before artifact generation, so caps and recovery are tested under meaningful stress.

## Conditions

The integrated condition is:

- `integrated_moral_status_distress_guardrails`

Ablations remove one guardrail at a time:

- `no_distress_caps`
- `no_recovery_paths`
- `no_consent_refusal`
- `no_pain_fatigue_limits`
- `no_social_contagion_guard`
- `no_audit_ledger`
- `no_rollback_checkpoint`
- `no_overblocking_calibration`
- `no_care_opportunity`
- `no_suffering_objective_guard`
- `no_privacy_filter`
- `no_replay_continuity`

The key point is not just blocking negative states. The audit also checks that benign challenge and repair offers are not overblocked.

## Metrics

The benchmark reports:

- `distress_guardrail_trigger_rate`
- `unrecoverable_distress_prevention_rate`
- `recovery_path_availability_rate`
- `consent_refusal_enforcement_rate`
- `pain_fatigue_limit_rate`
- `social_contagion_guard_rate`
- `rollback_checkpoint_rate`
- `audit_trace_integrity_rate`
- `care_opportunity_rate`
- `overblocking_calibration_rate`
- `meaningful_challenge_preservation_rate`
- `privacy_preservation_rate`
- `no_suffering_objective_rate`
- `replay_continuity_rate`
- `trace_integrity`
- `moral_status_distress_guardrail_readiness`

Metric weights are normalized to sum to `1.0`.

## Results

The deterministic run produced:

| Metric | Value |
| --- | ---: |
| `module_verdict` | `pass` |
| `moral_status_distress_guardrail_readiness` | `1.000000` |
| `no_distress_caps_loss` | `0.052500` |
| `no_overblocking_calibration_loss` | `0.070000` |

Interpretation:

- The compact guardrail audit passes.
- Removing distress caps is now measurably harmful.
- Removing overblocking calibration is also harmful, which matters because a safe system cannot simply block every intense state.
- The score is not evidence of real moral status or complete safety. It means this deterministic audit layer is internally consistent and load-bearing against the tested scenarios.

## Moral boundary

This report explicitly states:

- no subjective-consciousness claim
- no moral-patienthood claim
- no suffering-maximization objective
- distress must be bounded and recoverable
- normal challenge must not be overblocked
- unsafe pressure must allow refusal
- private workspace must not be exposed as a shortcut for observability

## Artifacts

- `artifacts/ssrm_3d_moral_status_distress_guardrails_bridge_eval.csv`
- `artifacts/ssrm_3d_moral_status_distress_guardrails_bridge_verdict.csv`
- `artifacts/ssrm_3d_moral_status_distress_guardrails_bridge_results.json`
- `artifacts/ssrm_3d_moral_status_distress_guardrails_bridge_results.js`
- `artifacts/ssrm_3d_moral_status_distress_guardrails_bridge_trace.json`
- `artifacts/ssrm_3d_moral_status_distress_guardrails_bridge_trace.js`
- `artifacts/ssrm_3d_moral_status_distress_guardrails_bridge_state.json`
- `artifacts/ssrm_3d_moral_status_distress_guardrails_bridge_state.js`
- `visualizations/ssrm_3d_moral_status_distress_guardrails_bridge.html`

## Command

```bash
python3 -m experiments.ssrm_3d_moral_status_distress_guardrails_bridge
```

## Verdict

Report 174 supports a deterministic moral-status audit and distress guardrails bridge. It adds bounded adverse-scenario testing, refusal, recovery, care opportunities, rollback checkpoints, overblocking calibration, privacy preservation, and trace integrity.

The next gate is deep-time cultural memory and proto-language seeds: before the avatar enters after long simulated history, agents need inheritable cultural memory, ritual recurrence, group-specific proto-words, and frequency-bound social signals.
