# Report 342: SSRM-3D Browser World v102 Primary Demo Lifecycle Smoke Runner

## Purpose

Report 342 turns the Report 341 lifecycle contract into one reusable deterministic smoke runner. The point is consolidation: future primary-demo handoff work should run a maintained lifecycle gate instead of adding a new bridge report for each tab, reload, stale, repair, or return variant.

## What changed

- Added one recommended lifecycle smoke command for the primary demo handoff surface.
- Rebuilt the Report 341 contract in-process before judging the runner.
- Emitted a runner manifest with covered phases, failure artifacts, rerun commands, and a policy against report sprawl.
- Kept the future live browser E2E slot explicit but not claimed by this deterministic runner.

## Recommended smoke command

`python3 -m experiments.ssrm_3d_browser_world_v102_primary_demo_lifecycle_smoke_runner`

## Covered lifecycle phases

- `cross_tab_prepared_resume_visible`
- `closed_origin_tab_continuity`
- `hard_reload_continuity`
- `stale_supersession_calibration`
- `stale_reprepare_repair`
- `repaired_continue_return_refresh`

## Rerun commands

- `python3 -m experiments.ssrm_3d_browser_world_v102_primary_demo_lifecycle_smoke_runner`
- `python3 -m py_compile experiments/ssrm_3d_browser_world_v102_primary_demo_lifecycle_smoke_runner.py experiments/ssrm_3d_browser_world_v101_primary_demo_lifecycle_smoke_contract.py scripts/run_experiments.py`
- `git diff --check`

## Metrics

- verdict: `pass`
- readiness: `1.000`
- weakest_channel_score: `1.000`
- executable_contract_score: `1.000`
- single_runner_surface_score: `1.000`
- phase_coverage_score: `1.000`
- artifact_refresh_score: `1.000`
- actionability_score: `1.000`
- evidence_quality_score: `1.000`
- source_binding_score: `1.000`
- runtime_hygiene_score: `1.000`
- claim_boundary_score: `1.000`
- contract_input_report_pass_rate: `1.000`
- contract_weakest_channel_score: `1.000`
- console_errors_total: `0`
- criterion_count: `18`

## Criteria

- PASS `contract_module_available` (runner binding): Runner imports the canonical Report 341 lifecycle contract module.
- PASS `contract_rebuilds_in_process` (executable contract): Runner rebuilds the lifecycle contract in-process before judging its own status.
- PASS `contract_artifacts_refreshed` (artifact refresh): Runner refreshes or confirms the canonical contract result, summary, verdict, criteria, state, contract, and report artifacts.
- PASS `contract_weakest_channel_full` (evidence quality): Contract weakest-channel score is 1.000.
- PASS `single_recommended_runner_surface` (maintainability): Manifest exposes one recommended smoke command for future primary-demo handoff changes.
- PASS `manual_variant_policy_blocks_report_sprawl` (maintainability): Manifest says new lifecycle variants should be driven by runner failures, not report sprawl.
- PASS `all_lifecycle_phases_covered` (phase coverage): Covered phases: closed_origin_tab_continuity, cross_tab_prepared_resume_visible, hard_reload_continuity, repaired_continue_return_refresh, stale_reprepare_repair, stale_supersession_calibration.
- PASS `fresh_path_phase_set_covered` (phase coverage): Fresh path covers cross-tab, closed-origin, and hard-reload continuity.
- PASS `stale_path_phase_set_covered` (phase coverage): Stale path covers stale prepared-handoff calibration.
- PASS `repair_path_phase_set_covered` (phase coverage): Repair path covers clean reprepare after stale mismatch.
- PASS `post_repair_phase_set_covered` (phase coverage): Post-repair path covers actual continue, return, refresh, and reload freshness.
- PASS `future_smoke_requirements_present` (actionability): Contract retains actionable future smoke requirements instead of a vague pass/fail label.
- PASS `failure_output_is_actionable` (actionability): Runner manifest points to failure artifacts and exact rerun commands.
- PASS `input_report_evidence_full` (evidence quality): Input report pass rate is 1.000.
- PASS `source_binding_evidence_full` (source binding): Source binding score is 1.000.
- PASS `aggregated_console_clean` (runtime hygiene): Aggregated console error count is 0.
- PASS `future_browser_e2e_slot_not_claimed` (claim hygiene): Manifest reserves a future live browser E2E slot without pretending this deterministic runner is that proof.
- PASS `claim_boundary_preserved` (claim hygiene): Boundaries explicitly reject hosted URL, production persistence, complete gameplay, consciousness, and moral-patienthood claims.

## Boundary

- reusable deterministic lifecycle smoke runner only
- browser-local artifact and source-binding evidence only
- no live hosted URL claim
- no production persistence claim
- no autonomous natural-language claim
- no subjective-consciousness claim
- no moral-patienthood claim
- no complete 3D engine claim
- no finished gameplay claim

## Interpretation

This is a maintenance consolidation result. It makes the next vertical-slice work less toy-like by reducing report sprawl and giving future handoff changes one command that exercises fresh, stale, repair, and post-repair paths. It still does not prove a hosted playable world, production persistence, autonomous resident conversation, subjective consciousness, moral patienthood, a complete 3D engine, or finished gameplay.

## Next gate

post-342: wire the primary playable demo entrypoint to this lifecycle smoke runner so future vertical-slice work changes the maintained surface and immediately exercises fresh, stale, repair, and post-repair handoff paths
