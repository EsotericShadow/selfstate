# Report 341: SSRM-3D Browser World v101 Primary Demo Lifecycle Smoke Contract

## Purpose

Report 341 consolidates the repeated primary-demo handoff lifecycle checks from Reports 335 through 340 into one deterministic smoke contract. This is intentionally not another near-duplicate browser variant. It is the maintained contract future handoff changes should satisfy before new report-specific lifecycle branches are added.

## What changed

- Added a deterministic lifecycle contract generator for the primary demo handoff path.
- Aggregated fresh continuity, closed-origin continuity, hard-reload continuity, stale calibration, stale repair, and repaired continue-return freshness evidence.
- Bound the future smoke surface to visible handoff controls, freshness status, continue/download affordances, shell evidence refresh, and console cleanliness.
- Preserved the claim boundary: browser-local lifecycle hygiene only, with no subjective-consciousness, moral-patienthood, production-persistence, or finished-gameplay claim.

## Lifecycle phases

- Report 335 `cross_tab_prepared_resume_visible`: fresh prepared handoff can be resumed from a second tab -> pass (weakest 1.000, required min 1.000)
- Report 336 `closed_origin_tab_continuity`: closed origin tab does not strand the prepared handoff -> pass (weakest 1.000, required min 1.000)
- Report 337 `hard_reload_continuity`: hard reload keeps the closed-origin handoff visible and usable -> pass (weakest 1.000, required min 1.000)
- Report 338 `stale_supersession_calibration`: stale prepared handoff is recognized as stale instead of blindly trusted -> pass (weakest 1.000, required min 1.000)
- Report 339 `stale_reprepare_repair`: stale mismatch can be repaired by re-preparing a clean handoff -> pass (weakest 1.000, required min 1.000)
- Report 340 `repaired_continue_return_refresh`: repaired clean handoff remains fresh after continue, reviewer pass, return, refresh, and reload -> pass (weakest 1.000, required min 1.000)

## Metrics

- verdict: `pass`
- readiness: `1.000`
- weakest_channel_score: `1.000`
- lifecycle_coverage_score: `1.000`
- stale_repair_coverage_score: `1.000`
- post_repair_use_score: `1.000`
- input_report_pass_rate: `1.000`
- input_weakest_channel_min: `1.000`
- source_binding_score: `1.000`
- console_errors_total: `0`
- criterion_count: `16`

## Criteria

- PASS `report_335_cross_tab_continuity_passed` (fresh continuity): Report 335 fresh cross-tab prepared-resume evidence is present and passing.
- PASS `report_336_closed_origin_tab_continuity_passed` (fresh continuity): Report 336 closed-origin-tab continuity evidence is present and passing.
- PASS `report_337_hard_reload_continuity_passed` (fresh continuity): Report 337 hard-reload continuity evidence is present and passing.
- PASS `report_338_stale_calibration_passed` (stale calibration): Report 338 stale-handoff calibration evidence is present and passing.
- PASS `report_339_stale_repair_passed` (repair path): Report 339 stale-handoff repair evidence is present and passing.
- PASS `report_340_repaired_continue_return_passed` (post-repair use): Report 340 repaired continue-return freshness evidence is present and passing.
- PASS `all_inputs_browser_console_clean` (runtime hygiene): Aggregated browser console errors across input reports: 0.
- PASS `all_inputs_weakest_channel_full` (evidence quality): Minimum input weakest-channel score is 1.000.
- PASS `all_required_metrics_full` (evidence quality): Minimum required metric across lifecycle sources is 1.000.
- PASS `continuity_contract_covers_fresh_path` (contract coverage): Fresh continuity path covers cross-tab, closed-origin, and hard-reload phases.
- PASS `continuity_contract_covers_stale_path` (contract coverage): Stale lifecycle path covers stale calibration and clean reprepare repair.
- PASS `continuity_contract_covers_repair_path` (contract coverage): Repair path includes re-preparing a clean payload after stale mismatch detection.
- PASS `continuity_contract_covers_post_repair_use` (contract coverage): Post-repair path includes actual continue, return, refresh, and reload use.
- PASS `contract_has_single_future_smoke_surface` (maintainability): The contract defines one complete lifecycle surface instead of one-off future variants.
- PASS `source_preserves_primary_demo_controls` (source binding): Primary demo source still exposes the handoff status/action controls required by the contract.
- PASS `boundary_preserved` (claim hygiene): The contract states browser-local/no-consciousness/no-production-persistence boundaries.

## Contract boundary

- browser-local lifecycle contract only
- no LLM calls
- no subjective-consciousness claim
- no moral-patienthood claim
- no production persistence claim
- no complete 3D engine claim
- no finished gameplay claim

## Interpretation

The result says the primary demo has one coherent handoff lifecycle contract spanning fresh, stale, repaired, and post-repair use paths. It does not say the browser world is a finished product. The useful shift is maintenance discipline: future handoff work should run the lifecycle contract instead of adding another isolated report for every tab, reload, or return variant.

## Next gate

post-341: replace one-off lifecycle report generation with a single reusable primary-demo lifecycle smoke runner whenever future handoff changes are made
