# Report 309: SSRM-3D Browser World v69 Primary Demo Full Manual Pass

## Purpose

Report 309 uses the Report 308 filtered ledger during a full primary-demo manual pass. The first pass found a real evidence defect in the maintained shell: QA hooks executed, but the visible QA panel only said `10 checks` or `1 checks`, so the manual script could not see `all pass`, `rollbackTested`, `smokePass`, or `auditPass` evidence.

The repair is deliberately narrow: keep the same maintained v61 shell and render detailed QA summaries in the visible QA panel. No new simulation organ was added.

## Boundary

Deterministic browser-local full manual pass and maintained-shell QA evidence repair only; no LLM calls, no subjective consciousness, no autonomous natural language, no moral patienthood, no production persistence, no complete 3D engine, and no finished gameplay claim.

## What changed

- Added `formatQAResults()` to the v61 app-shell generator.
- Regenerated the maintained v61 shell so `qaOut` shows `N checks / all pass` plus per-hook fields.
- Re-ran the primary-demo manual flow through MP-12 in the browser.
- Recorded MP-09 and MP-10 as resolved defects in the browser-local filtered ledger.

## Metrics

| Metric | Value |
|---|---:|
| readiness | 1.000000 |
| weakest_channel_score | 1.000000 |
| full_manual_pass_rate | 1.000000 |
| pre_fix_defect_count | 2 |
| resolved_defect_count | 2 |
| console_errors | 0 |
| criterion_count | 10 |

## Manual pass evidence

| Step | Passed | Evidence summary |
|---|---:|---|
| MP-01 | True | primary demo launcher opened on clean local origin |
| MP-02 | True | boundary visible before launching shell |
| MP-03 | True | clean launch opened maintained v61 shell with reset and source tags |
| MP-04 | True | movement changed visible room/status and replay rows increased |
| MP-05 | True | bounded talk changed resident memory and schedule remains visible |
| MP-06 | True | borrow increased debt; return restored debt baseline and trust repaired partially |
| MP-07 | True | offscreen wait changed resident progress without avatar command |
| MP-08 | True | restore returned saved room and memory after deliberate mutation |
| MP-09 | True | visible checklist QA text now reports 10 checks and all pass |
| MP-10 | True | visible rollback audit QA text exposes rollbackTested/smokePass/auditPass |
| MP-11 | True | replay export link prepared with nonzero object URL and replay rows |
| MP-12 | True | resume launch reopened persisted shell state without reset |

## Resolved defects

| Step | Severity | Status | Note |
|---|---|---|---|
| MP-09 | blocking | resolved | Checklist QA output did not visibly say all pass; fixed by formatQAResults. |
| MP-10 | blocking | resolved | Rollback audit QA output hid rollbackTested/smokePass/auditPass; fixed by formatQAResults. |

## Criteria

| Channel | Passed | Score | Evidence |
|---|---:|---:|---|
| single_primary_surface_retained | True | 1.000 | primary demo still launches the maintained v61 app shell |
| qa_visible_summary_source | True | 1.000 | v61 generator and generated app both render detailed QA summaries |
| qa_all_pass_wording | True | 1.000 | QA panel can visibly show all-pass status, not only raw check count |
| qa_detail_wording | True | 1.000 | QA panel can expose per-hook fields such as rollbackTested/smokePass/auditPass |
| pre_fix_defect_captured | True | 1.000 | browser pass captured the pre-fix QA visibility defects before repair |
| full_manual_pass_complete | True | 1.000 | post-fix browser pass reported 12/12 manual steps passing |
| ledger_used_for_resolution | True | 1.000 | filtered ledger records MP-09 and MP-10 as resolved and verifies open/resolved filters |
| qa_output_proves_checklist | True | 1.000 | post-fix visible checklist text contains 10 checks and all pass |
| qa_output_proves_rollback_audit | True | 1.000 | post-fix visible rollback-audit text exposes rollbackTested, smokePass, and auditPass |
| console_clean | True | 1.000 | browser console error count was 0 |

## Verdict

`pass`

Report 309 is a consolidation repair, not a capability claim. The meaningful result is that the primary demo can now visibly prove the full manual pass, including the previously opaque QA hooks.

## Next gate

post-309: keep using the primary demo as the one playable surface; next hardening should add a reviewer-readable session transcript/checkpoint view only if the next full pass shows the current replay/debug layer is still too opaque
