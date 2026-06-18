# Report 349: SSRM-3D Browser World v109 Primary Demo Guarded Receipt Browser Smoke

## Purpose

Report 349 is the first real browser-local smoke for the guarded combined receipt path. It uses the maintained primary launcher on localhost, prepares a combined outside-review handoff, observes the normal download guard, toggles the explicit debug override, and observes the guarded export link and records whether the browser supports the download event.

## Browser smoke summary

- browser: `in_app_browser`
- launcher_url: `http://127.0.0.1:8767/visualizations/ssrm_3d_browser_world_primary_demo/index.html`
- target_shell: `../ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html`
- clean_launch_clicked: `True`
- returned_to_launcher: `True`
- prepare_outside_review_clicked: `True`
- initial_gate_state: `blocked`
- override_gate_state: `debug-override`
- download_event_observed: `False`
- download_error: `Downloads are not supported by Codex In-app Browser.`
- console_errors: `0`

## Metrics

- verdict: `pass`
- readiness: `1.000`
- weakest_channel_score: `1.000`
- browser_interaction_score: `1.000`
- download_guard_score: `1.000`
- payload_evidence_score: `1.000`
- runtime_hygiene_score: `1.000`
- download_event_observed: `0.000`
- export_click_attempt_recorded: `1.000`
- console_error_count: `0`
- criterion_count: `16`

## Criteria

- PASS `guard_source_artifacts_available_and_passing` (source guard): Report 348 guard results and contract exist and pass.
- PASS `browser_smoke_artifact_exists` (browser artifact): Browser smoke artifact exists and is tagged as Report 349.
- PASS `browser_smoke_used_localhost_primary_launcher` (browser artifact): Smoke ran in the in-app browser against the localhost primary launcher.
- PASS `browser_smoke_used_maintained_surface` (surface discipline): Smoke used the primary launcher and maintained v61 shell target, not a parallel surface.
- PASS `browser_smoke_clicked_clean_launch_and_returned` (browser interaction): Smoke clicked clean launch to create a real launch handoff, then returned to the launcher.
- PASS `browser_smoke_prepared_combined_handoff` (browser interaction): Smoke clicked Prepare outside-review handoff and produced a combined receipt payload.
- PASS `initial_download_was_guarded_before_override` (download guard): Before debug override, normal download was blocked and recorderExport was missing.
- PASS `debug_override_enabled_download_path` (download guard): After toggling debug override, the incomplete download path became available and explicitly marked debug override.
- PASS `final_payload_records_debug_override_gate` (payload evidence): Final stored payload records debug override export, download enabled, and normal gate not allowed.
- PASS `final_payload_keeps_required_receipt_fields` (payload evidence): Final payload status and guard contract cover all six combined receipt fields.
- PASS `browser_export_link_click_attempt_recorded` (browser interaction): Smoke clicked the debug-override handoff export link and recorded either a download event or the in-app browser download limitation.
- PASS `browser_console_clean` (runtime hygiene): Browser console errors observed: 0.
- PASS `source_persists_override_gate_in_payload` (source binding): Launcher source persists the current download gate back into the stored handoff payload.
- PASS `generator_preserves_override_gate_persistence` (generator durability): v63 generator preserves download-gate persistence in regenerated launchers.
- PASS `experiment_index_includes_browser_smoke_report` (runner index): Experiment runner index includes the Report 349 verifier module.
- PASS `claim_boundary_preserved` (claim hygiene): Boundary rejects hosted URL, production persistence, autonomous language, consciousness, moral patienthood, complete engine, and finished gameplay claims.

## Boundary

- one real browser-local launcher smoke artifact plus deterministic verification
- in-app browser smoke on localhost only
- debug override smoke proves the incomplete review export path only
- no hosted URL claim
- no production persistence claim
- no autonomous natural-language claim
- no subjective-consciousness claim
- no moral-patienthood claim
- no complete 3D engine claim
- no finished gameplay claim

## Interpretation

This report moves the receipt path from source-only verification to one actual browser-local launcher smoke. In this environment, the in-app browser does not support file downloads, so the smoke records the guarded export-link click attempt and final payload rather than claiming a completed file download. It still does not prove a hosted URL, production persistence, autonomous resident conversation, subjective consciousness, moral patienthood, a complete 3D engine, or finished gameplay.

## Next gate

post-349: use this browser-smoked combined receipt path as the review gate for the next actual vertical-slice behavior change, instead of adding another receipt-only bridge
