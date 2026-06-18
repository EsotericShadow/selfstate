# Report 350: SSRM-3D Browser World v110 Primary Shell Return-Recognition Vertical Slice

## Purpose

Report 350 is an actual maintained-shell behavior change after the receipt-gate work. Returning to a persisted session and entering again now causes the selected resident to recognize the returning avatar, update public memory/trust/progress, and log continuity evidence.

## What changed

- `enterWorld()` now detects a returning persisted session with prior replay rows.
- The selected resident records `recognized returning avatar ...` in visible memory.
- Trust/progress move slightly through the same public resident mutation path.
- Public `returnContinuity` state records the resident, replay rows before return, memory, tick, and boundary.
- The replay payload records `returningVisit` and `returnContinuity`.
- Report 350 requires the Report 349 browser-smoked combined receipt gate before accepting the behavior.

## Browser smoke summary

- shell_url: `http://127.0.0.1:8768/visualizations/ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html?source=report-350-return`
- selected_resident: `Ari`
- before_memory: `heard bounded phrase greet`
- after_memory: `recognized returning avatar after 2 replay row(s)`
- before_trust: `0.592`
- after_trust: `0.602`
- before_replay_rows: `2`
- after_replay_rows: `3`
- console_errors: `0`

## Metrics

- verdict: `pass`
- readiness: `1.000`
- weakest_channel_score: `1.000`
- review_gate_score: `1.000`
- browser_interaction_score: `1.000`
- visible_consequence_score: `1.000`
- public_state_score: `1.000`
- replay_debug_score: `1.000`
- runtime_hygiene_score: `1.000`
- criterion_count: `12`

## Criteria

- PASS `receipt_gate_browser_smoke_available_and_passing` (review gate): Report 349 browser-smoked combined receipt gate exists and passes before this behavior change is accepted.
- PASS `return_recognition_source_wired` (source behavior): Maintained shell source wires returningVisit recognition, public continuity state, history event, and replay payload.
- PASS `browser_smoke_artifact_exists` (browser artifact): Report 350 browser smoke artifact exists and is tagged correctly.
- PASS `browser_smoke_used_maintained_shell` (surface discipline): Smoke ran in the maintained v61 app shell with no parallel surface.
- PASS `browser_smoke_created_persisted_session_before_return` (browser interaction): Smoke entered the world, talked to a resident, and created visible persisted replay/memory before return.
- PASS `browser_smoke_returned_without_reset` (browser interaction): Smoke navigated back to the maintained shell without reset and added a return entry to replay.
- PASS `resident_recognized_returning_avatar` (visible consequence): Visible resident memory and trust changed after return recognition.
- PASS `return_continuity_public_state_recorded` (public state): Browser smoke observed public returnContinuity state with report marker, resident, and replay row count.
- PASS `return_recognition_replay_logged` (replay/debug): Browser smoke observed an enterWorld replay row with returningVisit true.
- PASS `browser_console_clean` (runtime hygiene): Browser console errors observed: 0.
- PASS `experiment_index_includes_report_350` (runner index): Experiment runner index includes the Report 350 verifier module.
- PASS `claim_boundary_preserved` (claim hygiene): Boundary rejects LLM, consciousness, moral patienthood, autonomous language, production persistence, hosted URL, complete engine, and finished gameplay claims.

## Boundary

- browser-local maintained-shell return-recognition behavior only
- no LLM call
- no subjective-consciousness claim
- no moral-patienthood claim
- no autonomous natural-language claim
- no production persistence claim
- no hosted URL claim
- no complete 3D engine claim
- no finished gameplay claim

## Interpretation

This is a small integrated behavior, not a new organ: the maintained shell now shows resident continuity when a player leaves/resumes and enters again. It still does not prove subjective consciousness, autonomous language, production persistence, a hosted URL, moral patienthood, a complete 3D engine, or finished gameplay.

## Next gate

post-350: expand the return-recognition loop into a visible resident promise/follow-up thread so returning to the world advances one remembered obligation rather than only a greeting memory
