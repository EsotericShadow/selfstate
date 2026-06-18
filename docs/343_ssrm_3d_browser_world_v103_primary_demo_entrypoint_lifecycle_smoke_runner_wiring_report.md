# Report 343: SSRM-3D Browser World v103 Primary Demo Entrypoint Lifecycle Smoke Runner Wiring

## Purpose

Report 343 wires the reusable Report 342 lifecycle smoke runner into the primary playable demo entrypoint. The launcher, manual playtest script, and v63 generator now all point future handoff changes at one maintained smoke command rather than encouraging another detached lifecycle report.

## What changed

- Added a visible `Maintained lifecycle smoke runner` section to the primary demo launcher.
- Added the runner command, Report 342 doc link, results link, and manifest link to the launcher.
- Added `MP-13` to the manual playtest path and recorder/defect step list.
- Updated the v63 entrypoint generator so regenerated launchers preserve the wiring.
- Added a deterministic verifier that fails if command, policy, artifact links, manual step, generator constants, or runner manifest alignment disappear.

## Wired command

`python3 -m experiments.ssrm_3d_browser_world_v102_primary_demo_lifecycle_smoke_runner`

## Runner phases retained

- `closed_origin_tab_continuity`
- `cross_tab_prepared_resume_visible`
- `hard_reload_continuity`
- `repaired_continue_return_refresh`
- `stale_reprepare_repair`
- `stale_supersession_calibration`

## Metrics

- verdict: `pass`
- readiness: `1.000`
- weakest_channel_score: `1.000`
- runner_evidence_score: `1.000`
- entrypoint_wiring_score: `1.000`
- manual_path_score: `1.000`
- generator_durability_score: `1.000`
- consolidation_policy_score: `1.000`
- runner_index_score: `1.000`
- claim_hygiene_score: `1.000`
- runner_phase_coverage_score: `1.000`
- runner_weakest_channel_score: `1.000`
- criterion_count: `15`

## Criteria

- PASS `runner_artifacts_available_and_passing` (runner evidence): Report 342 runner results and manifest exist and the runner verdict is pass.
- PASS `runner_command_matches_manifest` (runner evidence): Entrypoint wiring uses the same command as the Report 342 runner manifest.
- PASS `runner_phase_coverage_retained` (runner evidence): The wired runner still covers fresh, stale, repair, and post-repair lifecycle phases.
- PASS `launcher_exposes_visible_smoke_section` (entrypoint wiring): Primary demo launcher exposes a visible lifecycle-smoke section with command and policy.
- PASS `launcher_links_runner_artifacts` (entrypoint wiring): Primary demo launcher links the Report 342 doc, results artifact, and runner manifest.
- PASS `launcher_hero_has_runner_action` (entrypoint wiring): Launcher hero exposes the smoke runner next to the manual playtest script.
- PASS `manual_playtest_has_mp13_runner_step` (manual path): Manual playtest script adds MP-13 for the maintained lifecycle smoke runner.
- PASS `manual_playtest_lists_runner_artifacts` (manual path): Manual playtest script lists the Report 342 doc, results, and manifest artifacts.
- PASS `generator_preserves_runner_constants` (generator durability): The v63 entrypoint generator defines reusable smoke-runner constants.
- PASS `generator_preserves_required_mp13` (generator durability): The v63 generator includes MP-13 as a required manual step.
- PASS `generator_generates_smoke_section` (generator durability): The v63 generator emits the visible lifecycle-smoke section and command binding.
- PASS `policy_blocks_lifecycle_report_sprawl` (consolidation policy): Launcher, manual, generator, and runner manifest all direct future work toward one maintained gate.
- PASS `experiment_index_includes_wiring_report` (runner index): The experiment runner index includes the Report 343 verifier module.
- PASS `future_browser_e2e_boundary_preserved` (claim hygiene): The wiring remains honest that this is source/artifact wiring, not a live browser E2E proof.
- PASS `claim_boundary_preserved` (claim hygiene): Boundary rejects hosted URL, live browser automation, production persistence, consciousness, moral patienthood, complete engine, and finished gameplay claims.

## Boundary

- entrypoint wiring and deterministic source verification only
- no hosted URL claim
- no live browser automation claim
- no production persistence claim
- no autonomous natural-language claim
- no subjective-consciousness claim
- no moral-patienthood claim
- no complete 3D engine claim
- no finished gameplay claim

## Interpretation

This is a small but direct consolidation step: the playable entrypoint now tells reviewers and future maintainers which lifecycle smoke gate protects the handoff path. It does not prove a hosted URL, live browser automation, production persistence, autonomous resident conversation, subjective consciousness, moral patienthood, complete 3D engine, or finished gameplay.

## Next gate

post-343: make the smoke-runner wiring actionable from the playable demo by adding a lightweight browser-visible preflight/status panel that explains when the runner was last regenerated and what lifecycle phase would block release
