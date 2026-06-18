# Report 344: SSRM-3D Browser World v104 Primary Demo Lifecycle Preflight Status Panel

## Purpose

Report 344 makes the Report 343 smoke-runner wiring actionable from the primary playable launcher. The launcher now exposes a lightweight preflight/status panel with runner freshness, release-blocking phase, lifecycle phase coverage, and claim boundary text.

## What changed

- Added a browser-visible `Lifecycle release preflight` panel to the primary launcher.
- Shows runner freshness from Report 342 results and Report 343 wiring evidence.
- Shows `Blocking lifecycle phase: none` only because the current runner and wiring artifacts pass.
- Lists all fresh, stale, repair, and post-repair lifecycle phases with pass status.
- Updated the manual playtest script and v63 entrypoint generator so the panel survives regeneration.
- Emitted a compact preflight packet for the next export/copy gate.

## Preflight packet

- command: `python3 -m experiments.ssrm_3d_browser_world_v102_primary_demo_lifecycle_smoke_runner`
- freshness: `Report 342 runner results pass; Report 343 entrypoint wiring pass`
- blocking_phase: `none`
- boundary: `Lifecycle preflight is artifact-backed by Report 342 runner results and Report 343 entrypoint wiring evidence; it is not a live hosted browser E2E claim.`

## Lifecycle phase statuses

- `cross_tab_prepared_resume_visible`: pass
- `closed_origin_tab_continuity`: pass
- `hard_reload_continuity`: pass
- `stale_supersession_calibration`: pass
- `stale_reprepare_repair`: pass
- `repaired_continue_return_refresh`: pass

## Metrics

- verdict: `pass`
- readiness: `1.000`
- weakest_channel_score: `1.000`
- artifact_freshness_score: `1.000`
- phase_coverage_score: `1.000`
- entrypoint_panel_score: `1.000`
- manual_path_score: `1.000`
- generator_durability_score: `1.000`
- calibration_score: `1.000`
- preflight_packet_score: `1.000`
- claim_hygiene_score: `1.000`
- blocking_phase_count: `0`
- phase_count: `6`
- criterion_count: `15`

## Criteria

- PASS `runner_results_available_and_passing` (artifact freshness): Report 342 runner results exist, pass, and retain full weakest-channel score.
- PASS `wiring_results_available_and_passing` (artifact freshness): Report 343 wiring results exist, pass, and retain full weakest-channel score.
- PASS `runner_manifest_phase_set_matches_panel` (phase coverage): Report 342 manifest phase coverage matches the phase set exposed by the preflight panel.
- PASS `launcher_has_preflight_panel` (entrypoint panel): Primary launcher has visible preflight panel, source marker, freshness text, blocking phase, and boundary text.
- PASS `launcher_lists_all_preflight_phases` (entrypoint panel): Primary launcher lists all lifecycle phases with pass status labels.
- PASS `launcher_still_exposes_runner_command_and_policy` (entrypoint panel): Preflight panel remains attached to the Report 342 runner command and report-sprawl policy.
- PASS `manual_documents_preflight_status` (manual path): Manual playtest script documents runner freshness, blocking phase, and boundary semantics.
- PASS `manual_lists_all_preflight_phases` (manual path): Manual playtest script lists every phase shown in the preflight panel.
- PASS `generator_preserves_preflight_constants` (generator durability): v63 generator defines preflight freshness, blocking phase, and boundary constants.
- PASS `generator_emits_preflight_panel` (generator durability): v63 generator emits the browser-visible preflight panel and source marker.
- PASS `generator_emits_all_phase_rows` (generator durability): v63 generator preserves every preflight phase row.
- PASS `preflight_blocking_phase_is_calibrated` (calibration): Blocking phase is none only because the runner and wiring verifier artifacts both pass.
- PASS `preflight_packet_is_exportable_artifact` (preflight packet): Report 344 emits a compact preflight packet suitable for future browser export/copy wiring.
- PASS `experiment_index_includes_preflight_report` (runner index): Experiment runner index includes the Report 344 verifier module.
- PASS `claim_boundary_preserved` (claim hygiene): Boundary rejects hosted URL, live browser automation, production persistence, consciousness, moral patienthood, complete engine, and finished gameplay claims.

## Boundary

- browser-visible source/status panel verification only
- artifact-backed freshness only
- no live hosted URL claim
- no live browser automation claim
- no production persistence claim
- no autonomous natural-language claim
- no subjective-consciousness claim
- no moral-patienthood claim
- no complete 3D engine claim
- no finished gameplay claim

## Interpretation

This turns the smoke-runner link from passive documentation into an operational status surface inside the launcher. It is still artifact-backed status, not a live hosted browser E2E proof, production persistence proof, autonomous conversation proof, subjective-consciousness claim, moral-patienthood claim, complete engine, or finished gameplay.

## Next gate

post-344: add a local browser action that can copy/export the lifecycle preflight packet from the launcher so outside reviewers can attach one compact smoke-status receipt to vertical-slice feedback
