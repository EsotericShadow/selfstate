# Report 348: SSRM-3D Browser World v108 Primary Demo Combined Receipt Download Guard

## Purpose

Report 348 makes the combined receipt status row enforceable. Normal outside-review handoff download is blocked when required receipt fields are missing, while an explicit debug override can intentionally export an incomplete review packet.

## What changed

- Added `combinedReceiptDebugOverride` and `combinedReceiptDownloadGate` to the launcher.
- Added `combinedReceiptDebugOverrideEnabled()`, `combinedReceiptDownloadGate()`, and `renderCombinedReceiptDownloadGate()`.
- Outside-review handoff payloads now include `combinedReceiptDownloadGate`.
- Normal download creation moved behind `gate.downloadEnabled`; missing fields show a blocked message instead.
- Debug override download uses explicit warning text and `data-combined-receipt-download-gate=debug-override`.
- Manual guidance and the v63 generator preserve the blocked-normal/download-override semantics.

## Required receipt fields

- `defects`
- `lifecyclePreflightPacket`
- `manualRecords`
- `recorderExport`
- `reviewedHandoffCompletion`
- `shellEvidence`

## Metrics

- verdict: `pass`
- readiness: `1.000`
- weakest_channel_score: `1.000`
- artifact_source_score: `1.000`
- entrypoint_controls_score: `1.000`
- browser_behavior_score: `1.000`
- manual_path_score: `1.000`
- generator_durability_score: `1.000`
- guard_contract_score: `1.000`
- normal_download_guarded: `1.000`
- debug_override_count: `1`
- criterion_count: `11`

## Criteria

- PASS `status_row_artifacts_available_and_passing` (artifact source): Report 347 status-row results and contract exist and pass.
- PASS `status_row_source_field_set_complete` (artifact source): Source status-row contract has all required combined receipt fields.
- PASS `launcher_exposes_download_guard_and_debug_override` (entrypoint controls): Primary launcher exposes a download gate status node and explicit incomplete-receipt debug override checkbox.
- PASS `javascript_defines_download_gate_model` (browser behavior): Launcher JS defines debug override, download gate model, renderer, report marker, and boundary.
- PASS `javascript_enforces_download_gate` (browser behavior): Launcher JS stores gate metadata, blocks missing-field downloads, supports explicit debug override, and rerenders on checkbox change.
- PASS `outside_review_export_no_longer_creates_unguarded_download` (browser behavior): Outside-review export no longer appends a download link directly before receipt completeness is rendered.
- PASS `manual_documents_download_guard` (manual path): Manual playtest documentation explains blocked normal download and explicit debug override semantics.
- PASS `generator_preserves_download_guard` (generator durability): v63 generator preserves debug override control, gate behavior, blocked/override branches, event listener, and manual guidance.
- PASS `guard_contract_is_complete` (guard contract): Report 348 emits a guard contract covering the six required receipt fields and explicit debug override.
- PASS `experiment_index_includes_download_guard_report` (runner index): Experiment runner index includes the Report 348 verifier module.
- PASS `claim_boundary_preserved` (claim hygiene): Boundary rejects live browser/download overclaiming, hosted URL, production persistence, autonomous language, consciousness, moral patienthood, complete engine, and finished gameplay claims.

## Boundary

- browser-local combined receipt download guard source verification only
- deterministic source check does not prove live download or checkbox behavior
- debug override is explicit and only for intentionally incomplete review packets
- no live hosted URL claim
- no live browser automation claim
- no production persistence claim
- no autonomous natural-language claim
- no subjective-consciousness claim
- no moral-patienthood claim
- no complete 3D engine claim
- no finished gameplay claim

## Interpretation

This makes the receipt completeness row operational rather than decorative: a missing field blocks normal download. The override is explicit and review/debug-oriented. This remains source-level browser-local verification, not proof of live checkbox/download behavior, hosted URL behavior, production persistence, autonomous conversation, consciousness, moral patienthood, complete engine, or finished gameplay.

## Next gate

post-348: run one real browser-local launcher smoke that prepares a combined receipt, observes the guarded download state, toggles the debug override, and exports the final outside-review handoff JSON without adding a parallel surface
