# Report 336: SSRM-3D Browser World v96 Primary Demo Closed-Origin-Tab Handoff Continuity Bridge

## Purpose

Report 336 turns the Report 335 cross-tab continuity gate into a tab-lifecycle independence gate. One browser tab prepares the visible fresh `resume` handoff, then that preparing tab is closed. A second fresh tab opens the primary launcher URL directly, sees the same prepared handoff card, clicks the visible continue action, returns to the launcher, refreshes shell evidence, and keeps the same visible handoff timestamp.

This did not add another simulation surface. The maintained v61 app shell and primary launcher remain the only exercised browser-world path.

## Boundary

Deterministic browser-local closed-origin-tab handoff continuity bridge only; no LLM calls, no subjective consciousness, no autonomous natural language, no moral patienthood, no production persistence, no complete 3D engine, and no finished gameplay claim. This is local tab-lifecycle handoff hygiene and visible review continuity, not external validation or evidence of inner experience.

## Browser evidence

- Original tab prepared a fresh `resume` handoff.
- The preparing tab was closed before the fresh tab opened the launcher URL.
- Fresh launcher tab rendered the same prepared handoff card from visible page state.
- Fresh tab exposed `Continue from prepared resume handoff` and `Download prepared outside-review handoff JSON`.
- Continue reached the maintained reviewer shell with reviewer landing and `Run reviewer pass` visible.
- Return to launcher was visible after the continued session.
- Refreshing shell evidence preserved the fresh resume classification.
- Original, fresh-tab, and after-return visible handoff timestamps matched.
- Browser console errors: `0`.
- Evidence uses visible status/actions plus the visible handoff preview JSON; it does not read raw storage keys.

## Metrics

| Metric | Value |
| --- | ---: |
| `readiness` | `1.0` |
| `weakest_channel_score` | `1.0` |
| `closed_origin_continuity_score` | `1.0` |
| `tab_independence_score` | `1.0` |
| `cross_tab_continue_score` | `1.0` |
| `timestamp_match_score` | `1.0` |
| `post_return_freshness_score` | `1.0` |
| `visible_no_storage_score` | `1.0` |
| `console_errors` | `0` |
| `criterion_count` | `16` |

## Criteria

| Channel | Passed | Score | Evidence |
| --- | --- | ---: | --- |
| `report_335_cross_tab_gate_passed` | `True` | `1.0` | Report 335 verdict=pass weakest=1.0 |
| `closed_origin_source_still_present` | `True` | `1.0` | generator, emitted JS, and emitted HTML retain prepared handoff continue/download machinery |
| `original_tab_prepared_fresh_resume_before_close` | `True` | `1.0` | kind=resume fresh=True status=Outside-review handoff ready: fresh resume handoff; checklist 7/7; shell evidence reviewer pass seen / receipt 9/9 / replay export ready; recorder 0 manual record(s) / export missing; next action: click Continue from prepared resume handoff, or download Prepared outside-review handoff JSON. |
| `original_preparing_tab_closed` | `True` | `1.0` | originalTabId=6 closed=True |
| `fresh_tab_after_close_shows_prepared_handoff` | `True` | `1.0` | kind=resume status=Outside-review handoff ready: fresh resume handoff; checklist 7/7; shell evidence reviewer pass seen / receipt 9/9 / replay export ready; recorder 0 manual record(s) / export missing; next action: click Continue from prepared resume handoff, or download Prepared outside-review handoff JSON. |
| `fresh_tab_after_close_status_fresh_resume` | `True` | `1.0` | Outside-review handoff ready: fresh resume handoff; checklist 7/7; shell evidence reviewer pass seen / receipt 9/9 / replay export ready; recorder 0 manual record(s) / export missing; next action: click Continue from prepared resume handoff, or download Prepared outside-review handoff JSON. |
| `fresh_tab_after_close_controls_available` | `True` | `1.0` | Continue from prepared resume handoffDownload prepared outside-review handoff JSON |
| `fresh_tab_after_close_visible_handoff_timestamp_matches_original` | `True` | `1.0` | original=2026-06-18T09:46:18.251Z fresh=2026-06-18T09:46:18.251Z |
| `fresh_tab_after_close_payload_timestamp_matches_original` | `True` | `1.0` | original=2026-06-18T09:46:18.251Z fresh=2026-06-18T09:46:18.251Z |
| `fresh_tab_after_close_continue_reaches_shell` | `True` | `1.0` | url=http://127.0.0.1:8798/visualizations/ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html?source=primary-demo-v63 reviewer=True runPass=True |
| `fresh_tab_after_close_return_to_launcher_visible` | `True` | `1.0` | http://127.0.0.1:8798/visualizations/ssrm_3d_browser_world_primary_demo/index.html#outsideReviewChecklist |
| `fresh_tab_after_close_refresh_keeps_handoff_fresh` | `True` | `1.0` | Outside-review handoff ready: fresh resume handoff; checklist 7/7; shell evidence reviewer pass seen / receipt 9/9 / replay export ready; recorder 0 manual record(s) / export missing; next action: click Continue from prepared resume handoff, or download Prepared outside-review handoff JSON. |
| `fresh_tab_after_close_after_return_timestamp_unchanged` | `True` | `1.0` | original=2026-06-18T09:46:18.251Z after=2026-06-18T09:46:18.251Z |
| `browser_evidence_uses_visible_or_preview_state` | `True` | `1.0` | browser evidence compares visible status/actions and visible handoff preview JSON, not raw storage keys |
| `browser_console_clean` | `True` | `1.0` | consoleErrors=0 messages=[] |
| `boundary_preserved` | `True` | `1.0` | Deterministic browser-local closed-origin-tab handoff continuity bridge only; no LLM calls, no subjective consciousness, no autonomous natural language, no moral patienthood, no production persistence, no complete 3D engine, and no finished gameplay claim. This is local tab-lifecycle handoff hygiene and visible review continuity, not external validation or evidence of inner experience. |

## Verdict

`pass` with `16/16` criteria passing.

This is a consolidation proof, not a new frontier claim. It says the current primary demo handoff can be recovered through visible UI surfaces even after the tab that prepared it is closed, and that the checked continue-return path does not silently mutate the prepared timestamp.

## Next gate

post-336: verify the closed-origin-tab handoff path after a hard reload of the fresh tab, so visible handoff continuity survives a page lifecycle restart as well as preparing-tab closure
