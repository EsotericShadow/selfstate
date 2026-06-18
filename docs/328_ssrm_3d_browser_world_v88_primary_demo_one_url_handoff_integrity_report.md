# Report 328: SSRM-3D Browser World v88 Primary Demo One-URL Handoff Integrity

## Purpose

Report 328 runs the cold one-URL outside-review path after Report 327. The flow completed, but the final handoff payload still claimed the hardcoded Report 303 localhost URL on port `8765`, even when the reviewer actually entered through another primary-demo URL. That made exported evidence diverge from the one URL used during review.

The launcher now derives its visible and exported handoff URL from `window.location`, records it in the launch handoff payload, and embeds the current URL in the final outside-review handoff payload.

## Boundary

Deterministic browser-local one-URL handoff integrity only; no LLM calls, no subjective consciousness, no autonomous natural language, no moral patienthood, no production persistence, no complete 3D engine, and no finished gameplay claim. URL integrity is review evidence hygiene, not external validation or evidence of inner experience.

## Pre-patch blocker

- Final handoff payload launchUrl is http://127.0.0.1:8765/visualizations/ssrm_3d_browser_world_primary_demo/index.html, but the cold reviewer URL origin is http://127.0.0.1:8788; the exported evidence diverges from the one URL actually used.

## What changed

- Added `currentLauncherUrl()` and `renderCurrentLauncherUrl()` to the primary launcher.
- The visible handoff panel now exposes the URL actually opened in the browser.
- Launch handoff records now carry `launcherUrl`.
- Outside-review exports now use `launchUrl: currentLauncherUrl()` instead of the old hardcoded port-8765 URL.
- Verified in browser that visible URL, launch-handoff `launcherUrl`, final payload `launchUrl`, reviewed completion, and console health all hold on a non-8765 port.

## Metrics

| Metric | Value |
|---|---:|
| readiness | 1.000000 |
| weakest_channel_score | 1.000000 |
| url_source_score | 1.000000 |
| browser_url_score | 1.000000 |
| console_errors | 0 |
| criterion_count | 10 |

## Browser evidence

- visible_url_matches_current_page: `True`
- payload_launch_url_matches_current_page: `True`
- handoff_launcher_url_matches_current_page: `True`
- completion_still_ready: `True`
- console_errors: `0`
- visible URL evidence: `visible=http://127.0.0.1:8788/visualizations/ssrm_3d_browser_world_primary_demo/index.html; page=http://127.0.0.1:8788/visualizations/ssrm_3d_browser_world_primary_demo/index.html`
- payload URL evidence: `payload=http://127.0.0.1:8788/visualizations/ssrm_3d_browser_world_primary_demo/index.html; page=http://127.0.0.1:8788/visualizations/ssrm_3d_browser_world_primary_demo/index.html`
- handoff launcher URL evidence: `handoff.launcherUrl=http://127.0.0.1:8788/visualizations/ssrm_3d_browser_world_primary_demo/index.html; page=http://127.0.0.1:8788/visualizations/ssrm_3d_browser_world_primary_demo/index.html; status=Last handoff: clean launch from http://127.0.0.1:8788/visualizations/ssrm_3d_browser_world_primary_demo/index.html toward ../ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html at 2026-06-18T08:55:31.885Z.`
- completion evidence: `ready=true; recorderRecordCount=1`

## Criteria

| Channel | Passed | Score | Evidence |
|---|---:|---:|---|
| pre_patch_cold_url_divergence_found | True | 1.000 | Final handoff payload launchUrl is http://127.0.0.1:8765/visualizations/ssrm_3d_browser_world_primary_demo/index.html, but the cold reviewer URL origin is http://127.0.0.1:8788; the exported evidence diverges from the one URL actually used. |
| dynamic_url_source_generated | True | 1.000 | launcher generator and emitted JS derive current URL from the opened page |
| visible_current_url_slot_present | True | 1.000 | handoff panel exposes the URL actually used by the reviewer |
| hardcoded_export_url_removed | True | 1.000 | outside-review export no longer hardcodes port 8765 in JS payloads |
| browser_visible_url_matches_current_page | True | 1.000 | visible=http://127.0.0.1:8788/visualizations/ssrm_3d_browser_world_primary_demo/index.html; page=http://127.0.0.1:8788/visualizations/ssrm_3d_browser_world_primary_demo/index.html |
| browser_payload_launch_url_matches_current_page | True | 1.000 | payload=http://127.0.0.1:8788/visualizations/ssrm_3d_browser_world_primary_demo/index.html; page=http://127.0.0.1:8788/visualizations/ssrm_3d_browser_world_primary_demo/index.html |
| browser_handoff_launcher_url_matches_current_page | True | 1.000 | handoff.launcherUrl=http://127.0.0.1:8788/visualizations/ssrm_3d_browser_world_primary_demo/index.html; page=http://127.0.0.1:8788/visualizations/ssrm_3d_browser_world_primary_demo/index.html; status=Last handoff: clean launch from http://127.0.0.1:8788/visualizations/ssrm_3d_browser_world_primary_demo/index.html toward ../ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html at 2026-06-18T08:55:31.885Z. |
| browser_completion_still_ready | True | 1.000 | ready=true; recorderRecordCount=1 |
| browser_one_url_console_clean | True | 1.000 | browser console error count was 0 |
| boundary_preserved | True | 1.000 | Deterministic browser-local one-URL handoff integrity only; no LLM calls, no subjective consciousness, no autonomous natural language, no moral patienthood, no production persistence, no complete 3D engine, and no finished gameplay claim. URL integrity is review evidence hygiene, not external validation or evidence of inner experience. |

## Verdict

`pass`

## Next gate

post-328: continue the cold one-URL reviewer pass and fix the next place where visible reviewer state, recorder state, shell evidence, and exported handoff payload can drift after reload or resume
