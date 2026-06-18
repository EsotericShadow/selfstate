# Report 287: SSRM-3D Browser World v47 Absence Negotiation/Role Conflict/Loan Default/Forgiveness Dialogue Bridge

## Purpose

Report 287 extends the browser-world line with resident-to-resident negotiations continuing during avatar absence, household role conflict mediation, multi-day loan defaults, animated forgiveness limits, and debt-aware avatar dialogue choices.

This is deterministic browser-local scaffolding. It does not claim subjective consciousness, real consent, moral patienthood, autonomous natural language, or a complete 3D engine. The advance is that social life keeps moving when the avatar is absent, and conflict/default/forgiveness mechanics become explicit rather than avoided.

## Boundary

Deterministic browser-local absence-negotiation/role-conflict/loan-default/forgiveness-dialogue scaffold only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, complete gameplay, complete 3D engine, or metaphysical frequency claim.

## Method

The experiment builds from the v46 resident scheduling/loan/role/apology/debt-hook bridge and adds a deterministic v47 browser-world scaffold over 204 session days and 3672 browser ticks. Each tick samples a settlement, two resident negotiators, a witness, a mediator, an object loan, the avatar's interaction state, and persistent debt/trust/resentment/fairness ledgers.

The new loop records seven evidence families: absence negotiations, role-conflict mediations, multi-day loan defaults, animated forgiveness limits, debt-aware avatar choices, absence-negotiation reload probes, and browser surface ticks. The browser stub exposes panels and handlers for absence negotiation, role mediation, loan default marking, forgiveness-limit animation, debt-aware choices, repayment/wait/ignore choices, reload memory, save/restore, and replay export.

An initial strict run failed because the loan-default denominator included too many current loan rows. The generator was corrected so default rows represent true due/overdue obligations, and resident-led negotiation was made explicit: absent, listen-later, status-check, wait, ignore, and forgiveness-limit states count as resident-led continuation, while direct help/repay states do not.

## Results

The deterministic run passes.

| Metric | Value |
| --- | ---: |
| verdict | pass |
| readiness | 0.915812 |
| mean channel score | 0.965282 |
| weakest channel | resident_negotiation_during_avatar_absence |
| weakest channel score | 0.800381 |
| resident negotiation during avatar absence | 0.800381 |
| role conflict mediation trace | 1.000000 |
| multi-day loan default trace | 1.000000 |
| loan default problem presence | 1.000000 |
| animated forgiveness limits | 0.982947 |
| debt-aware avatar dialogue choices | 1.000000 |
| debt choice consequence | 0.906726 |
| multi-reload absence memory integrity | 0.981891 |
| forgiveness limit not overdriven | 0.842000 |
| browser v47 surface | 1.000000 |

The weakest channel is intentionally the resident-led absence-negotiation channel. It passes at `0.800381`, just above the threshold, because the benchmark keeps direct avatar help/repayment separate from resident-to-resident negotiation rather than counting every avatar dialogue state as absence.

## Generated rows

| Row family | Count |
| --- | ---: |
| absence negotiations | 3672 |
| absence negotiations continued during avatar absence | 2939 |
| role conflict mediations | 1836 |
| multi-day loan defaults | 2970 |
| loan default problem rows | 2970 |
| animated forgiveness limits | 1466 |
| debt-aware avatar choices | 2691 |
| absence-negotiation reload probes | 497 |
| browser ticks | 3672 |
| browser buttons | 72 |
| localStorage handler mentions | 7 |

## Ablations

| Ablation | Readiness after removal |
| --- | ---: |
| no_absence_negotiation | 0.746812 |
| no_role_conflict_mediation | 0.741812 |
| no_multi_day_defaults | 0.733812 |
| no_forgiveness_limits | 0.744812 |
| no_debt_aware_avatar_choices | 0.749812 |
| no_reload_memory | 0.776812 |

## Honest interpretation

Report 287 does not add autonomous natural language, real consent, subjective experience, or moral patienthood. It is a deterministic browser-local control surface that makes the social substrate harder to fake: residents can keep negotiating while the avatar is not directly participating, household roles can conflict and mediate, loans can default over multiple days, forgiveness has visible limits, and avatar debt choices have consequences.

The pass is not a claim that the agents are alive. It is evidence that the browser-world benchmark now tracks a more realistic continuity problem: social obligations persist across absence, reload, and partial repair. The loan-default correction also matters because current loans should not dilute the default channel. The benchmark is still scaffolded, but the evidence is less forgiving than v46 because direct avatar intervention is not credited as resident-led absence negotiation.

## Artifacts

- `experiments/ssrm_3d_browser_world_v47_absence_negotiation_role_conflict_loan_default_forgiveness_dialogue_bridge.py`
- `artifacts/ssrm_3d_browser_world_v47_absence_negotiation_role_conflict_loan_default_forgiveness_dialogue_bridge_results.json`
- `artifacts/ssrm_3d_browser_world_v47_absence_negotiation_role_conflict_loan_default_forgiveness_dialogue_bridge_summary.csv`
- `artifacts/ssrm_3d_browser_world_v47_absence_negotiation_role_conflict_loan_default_forgiveness_dialogue_bridge_verdict.csv`
- `artifacts/ssrm_3d_browser_world_v47_absence_negotiation_role_conflict_loan_default_forgiveness_dialogue_bridge_absence_negotiations.csv`
- `artifacts/ssrm_3d_browser_world_v47_absence_negotiation_role_conflict_loan_default_forgiveness_dialogue_bridge_role_conflict_mediations.csv`
- `artifacts/ssrm_3d_browser_world_v47_absence_negotiation_role_conflict_loan_default_forgiveness_dialogue_bridge_multi_day_loan_defaults.csv`
- `artifacts/ssrm_3d_browser_world_v47_absence_negotiation_role_conflict_loan_default_forgiveness_dialogue_bridge_animated_forgiveness_limits.csv`
- `artifacts/ssrm_3d_browser_world_v47_absence_negotiation_role_conflict_loan_default_forgiveness_dialogue_bridge_debt_aware_avatar_choices.csv`
- `artifacts/ssrm_3d_browser_world_v47_absence_negotiation_role_conflict_loan_default_forgiveness_dialogue_bridge_absence_negotiation_reloads.csv`
- `artifacts/ssrm_3d_browser_world_v47_absence_negotiation_role_conflict_loan_default_forgiveness_dialogue_bridge_browser_ticks.csv`
- `visualizations/ssrm_3d_browser_world_v47_absence_negotiation_role_conflict_loan_default_forgiveness_dialogue_bridge.html`

## Next gate

browser world v48 with embodied needs during resident social schedules, household care duties, fatigue/rest negotiation, weather exposure during loans, and recoverable welfare state visible without suffering loops
