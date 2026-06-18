# Report 337: SSRM-3D Browser World v97 Primary Demo Closed-Origin-Tab Hard-Reload Handoff Continuity Bridge

## Purpose

Report 337 turns the Report 336 closed-origin-tab gate into a page-lifecycle restart gate. One browser tab prepares the visible fresh `resume` handoff, then that preparing tab is closed. A second fresh tab opens the primary launcher URL directly, reloads the page, sees the same prepared handoff card, clicks the visible continue action, returns to the launcher, refreshes shell evidence, and keeps the same visible handoff timestamp.

This did not add another simulation surface. The maintained v61 app shell and primary launcher remain the only exercised browser-world path.

## Boundary

Deterministic browser-local closed-origin-tab hard-reload handoff continuity bridge only; no LLM calls, no subjective consciousness, no autonomous natural language, no moral patienthood, no production persistence, no complete 3D engine, and no finished gameplay claim. This is local page-lifecycle handoff hygiene and visible review continuity, not external validation or evidence of inner experience.

## Browser evidence

- Original tab prepared a fresh `resume` handoff.
- The preparing tab was closed before the fresh tab opened the launcher URL.
- Fresh launcher tab rendered the prepared handoff before reload.
- Reloaded fresh launcher tab rendered the same prepared handoff card from visible page state.
- Reloaded tab exposed `Continue from prepared resume handoff` and `Download prepared outside-review handoff JSON`.
- Continue reached the maintained reviewer shell with reviewer landing and `Run reviewer pass` visible.
- Return to launcher was visible after the continued session.
- Refreshing shell evidence preserved the fresh resume classification.
- Original, before-reload, after-reload, and after-return visible handoff timestamps matched.
- Browser console errors: `0`.
- Evidence uses visible status/actions plus the visible handoff preview JSON; it does not read raw storage keys.

## Metrics

| Metric | Value |
| --- | ---: |
| `readiness` | `1.0` |
| `weakest_channel_score` | `1.0` |
| `hard_reload_continuity_score` | `1.0` |
| `tab_independence_score` | `1.0` |
| `reload_survival_score` | `1.0` |
| `cross_tab_continue_score` | `1.0` |
| `timestamp_match_score` | `1.0` |
| `post_return_freshness_score` | `1.0` |
| `visible_no_storage_score` | `1.0` |
| `console_errors` | `0` |
| `criterion_count` | `17` |

## Criteria

| Channel | Passed | Score | Evidence |
| --- | --- | ---: | --- |
| `report_336_closed_origin_gate_passed` | `True` | `1.0` | Report 336 verdict=pass weakest=1.0 |
| `hard_reload_source_still_present` | `True` | `1.0` | generator, emitted JS, and emitted HTML retain prepared handoff continue/download machinery |
| `original_tab_prepared_fresh_resume_before_close` | `True` | `1.0` | kind=resume fresh=True status=Outside-review handoff ready: fresh resume handoff; checklist 7/7; shell evidence reviewer pass seen / receipt 9/9 / replay export ready; recorder 0 manual record(s) / export missing; next action: click Continue from prepared resume handoff, or download Prepared outside-review handoff JSON. |
| `original_preparing_tab_closed` | `True` | `1.0` | originalTabId=7 closed=True |
| `fresh_tab_before_reload_shows_prepared_handoff` | `True` | `1.0` | kind=resume status=Outside-review handoff ready: fresh resume handoff; checklist 7/7; shell evidence reviewer pass seen / receipt 9/9 / replay export ready; recorder 0 manual record(s) / export missing; next action: click Continue from prepared resume handoff, or download Prepared outside-review handoff JSON. |
| `fresh_tab_after_reload_shows_prepared_handoff` | `True` | `1.0` | kind=resume status=Outside-review handoff ready: fresh resume handoff; checklist 7/7; shell evidence reviewer pass seen / receipt 9/9 / replay export ready; recorder 0 manual record(s) / export missing; next action: click Continue from prepared resume handoff, or download Prepared outside-review handoff JSON. |
| `fresh_tab_after_reload_status_fresh_resume` | `True` | `1.0` | Outside-review handoff ready: fresh resume handoff; checklist 7/7; shell evidence reviewer pass seen / receipt 9/9 / replay export ready; recorder 0 manual record(s) / export missing; next action: click Continue from prepared resume handoff, or download Prepared outside-review handoff JSON. |
| `fresh_tab_after_reload_controls_available` | `True` | `1.0` | Continue from prepared resume handoffDownload prepared outside-review handoff JSON |
| `fresh_tab_after_reload_visible_handoff_timestamp_matches_original` | `True` | `1.0` | original=2026-06-18T09:51:06.171Z afterReload=2026-06-18T09:51:06.171Z |
| `fresh_tab_after_reload_payload_timestamp_matches_original` | `True` | `1.0` | original=2026-06-18T09:51:06.171Z afterReload=2026-06-18T09:51:06.171Z |
| `fresh_tab_after_reload_continue_reaches_shell` | `True` | `1.0` | url=http://127.0.0.1:8799/visualizations/ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html?source=primary-demo-v63 reviewer=True runPass=True |
| `fresh_tab_after_reload_return_to_launcher_visible` | `True` | `1.0` | http://127.0.0.1:8799/visualizations/ssrm_3d_browser_world_primary_demo/index.html#outsideReviewChecklist |
| `fresh_tab_after_reload_refresh_keeps_handoff_fresh` | `True` | `1.0` | Outside-review handoff ready: fresh resume handoff; checklist 7/7; shell evidence reviewer pass seen / receipt 9/9 / replay export ready; recorder 0 manual record(s) / export missing; next action: click Continue from prepared resume handoff, or download Prepared outside-review handoff JSON. |
| `fresh_tab_after_reload_after_return_timestamp_unchanged` | `True` | `1.0` | original=2026-06-18T09:51:06.171Z afterReturn=2026-06-18T09:51:06.171Z |
| `browser_evidence_uses_visible_or_preview_state` | `True` | `1.0` | browser evidence compares visible status/actions and visible handoff preview JSON, not raw storage keys |
| `browser_console_clean` | `True` | `1.0` | consoleErrors=0 messages=[] |
| `boundary_preserved` | `True` | `1.0` | Deterministic browser-local closed-origin-tab hard-reload handoff continuity bridge only; no LLM calls, no subjective consciousness, no autonomous natural language, no moral patienthood, no production persistence, no complete 3D engine, and no finished gameplay claim. This is local page-lifecycle handoff hygiene and visible review continuity, not external validation or evidence of inner experience. |

## Verdict

`pass` with `17/17` criteria passing.

This is a consolidation proof, not a new frontier claim. It says the current primary demo handoff can be recovered through visible UI surfaces after preparing-tab closure and launcher reload, and that the checked continue-return path does not silently mutate the prepared timestamp.

## Next gate

post-337: verify stale prepared-handoff calibration when a newer shell handoff supersedes the prepared payload, so continuity rewards freshness judgment rather than preserving stale actions forever
