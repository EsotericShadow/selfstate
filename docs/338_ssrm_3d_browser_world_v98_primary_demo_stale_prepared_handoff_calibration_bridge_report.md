# Report 338: SSRM-3D Browser World v98 Primary Demo Stale Prepared-Handoff Calibration Bridge

## Purpose

Report 338 verifies calibrated freshness judgment rather than preserving every prepared handoff as usable forever. The browser proof prepares a visible fresh `resume` handoff, then launches a newer `clean` shell handoff. The old prepared payload remains downloadable for review, but the launcher must classify it as stale, name the mismatches, block the continue action, and preserve that stale classification after reload.

This did not add another simulation surface. The maintained v61 app shell and primary launcher remain the only exercised browser-world path, and no app-source patch was needed for the final passing proof.

## Boundary

Deterministic browser-local stale prepared-handoff calibration bridge only; no LLM calls, no subjective consciousness, no autonomous natural language, no moral patienthood, no production persistence, no complete 3D engine, and no finished gameplay claim. This is local launcher freshness judgment and review-handoff hygiene, not external validation or evidence of inner experience.

## Browser evidence

- Prepared baseline was a fresh `resume` handoff.
- A newer `clean` shell handoff superseded the prepared payload.
- Shell evidence refreshed to the newer clean handoff while the prepared payload stayed the older resume handoff.
- Visible status rendered `Prepared handoff payload is stale...` with named mismatches.
- Visible preview JSON marked `fresh: false` and named `launch handoff changed`.
- Stale actions blocked `Continue from prepared...` and kept the download action available.
- Reload preserved the stale classification, prepared timestamp, and newer shell timestamp.
- Browser console errors: `0`.
- Evidence uses visible status/actions plus the visible handoff preview JSON; it does not read raw storage keys.

## Metrics

| Metric | Value |
| --- | ---: |
| `readiness` | `1.0` |
| `weakest_channel_score` | `1.0` |
| `stale_calibration_score` | `1.0` |
| `stale_action_block_score` | `1.0` |
| `stale_review_evidence_score` | `1.0` |
| `supersession_score` | `1.0` |
| `reload_survival_score` | `1.0` |
| `timestamp_separation_score` | `1.0` |
| `visible_no_storage_score` | `1.0` |
| `console_errors` | `0` |
| `criterion_count` | `17` |

## Criteria

| Channel | Passed | Score | Evidence |
| --- | --- | ---: | --- |
| `report_337_hard_reload_gate_passed` | `True` | `1.0` | Report 337 verdict=pass weakest=1.0 |
| `stale_calibration_source_still_present` | `True` | `1.0` | generator, emitted JS, and emitted HTML retain stale prepared-handoff status/action machinery |
| `prepared_resume_was_fresh_before_supersede` | `True` | `1.0` | kind=resume fresh=True status=Outside-review handoff ready: fresh resume handoff; checklist 7/7; shell evidence reviewer pass seen / receipt 9/9 / replay export ready; recorder 0 manual record(s) / export missing; next action: click Continue from prepared resume handoff, or download Prepared outside-review handoff JSON. |
| `superseding_shell_handoff_created` | `True` | `1.0` | url=http://127.0.0.1:8800/visualizations/ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html?reset=1&source=primary-demo-v63 reviewer=True |
| `shell_evidence_refreshed_to_newer_clean_handoff` | `True` | `1.0` | prepared=2026-06-18T09:57:56.291Z current=2026-06-18T09:57:57.404Z kind=clean |
| `prepared_payload_not_overwritten_by_refresh` | `True` | `1.0` | prepared=2026-06-18T09:57:56.291Z stalePayload=2026-06-18T09:57:56.291Z kind=resume |
| `stale_status_visible_after_supersede` | `True` | `1.0` | Prepared handoff payload is stale: launch handoff changed, launch kind changed, shell replay rows changed. Payload is resume while current shell is clean. Re-run Prepare outside-review handoff. |
| `freshness_preview_marks_payload_stale` | `True` | `1.0` | previewFresh=False |
| `freshness_preview_names_mismatch` | `True` | `1.0` | ['launch handoff changed', 'launch kind changed', 'shell replay rows changed'] |
| `stale_actions_block_continue` | `True` | `1.0` | Re-prepare before continuing from this handoff.Download prepared outside-review handoff JSON |
| `download_remains_available_for_stale_review` | `True` | `1.0` | Re-prepare before continuing from this handoff.Download prepared outside-review handoff JSON |
| `stale_state_survives_launcher_reload` | `True` | `1.0` | Prepared handoff payload is stale: launch handoff changed, launch kind changed, shell replay rows changed. Payload is resume while current shell is clean. Re-run Prepare outside-review handoff. |
| `stale_reload_keeps_prepared_timestamp` | `True` | `1.0` | prepared=2026-06-18T09:57:56.291Z reload=2026-06-18T09:57:56.291Z |
| `stale_reload_keeps_newer_shell_timestamp` | `True` | `1.0` | afterSupersede=2026-06-18T09:57:57.404Z reload=2026-06-18T09:57:57.404Z |
| `browser_evidence_uses_visible_or_preview_state` | `True` | `1.0` | browser evidence compares visible status/actions and visible handoff preview JSON, not raw storage keys |
| `browser_console_clean` | `True` | `1.0` | consoleErrors=0 messages=[] |
| `boundary_preserved` | `True` | `1.0` | Deterministic browser-local stale prepared-handoff calibration bridge only; no LLM calls, no subjective consciousness, no autonomous natural language, no moral patienthood, no production persistence, no complete 3D engine, and no finished gameplay claim. This is local launcher freshness judgment and review-handoff hygiene, not external validation or evidence of inner experience. |

## Verdict

`pass` with `17/17` criteria passing.

This is a consolidation proof, not a frontier claim. It shows that the current primary launcher can distinguish valid continuity from stale continuity: old review payloads remain inspectable, but continuing from them is blocked until the reviewer prepares a fresh handoff.

## Next gate

post-338: verify stale prepared handoff repair by re-preparing after supersession, so reviewers can recover from a stale payload and regain a fresh continue action without losing visible mismatch history
