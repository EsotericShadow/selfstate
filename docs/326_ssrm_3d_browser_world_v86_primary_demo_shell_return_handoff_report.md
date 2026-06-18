# Report 326: SSRM-3D Browser World v86 Primary Demo Shell Return Handoff

## Purpose

Report 326 fixes a cold-reviewer comprehension defect found by running the Report 325 next gate against the actual primary-demo path. After `Run reviewer pass`, the maintained shell showed `PASSABLE_REVIEW_PATH` and an `ALL_PASS` receipt, but it did not provide an obvious way back to the launcher checklist and handoff export area. A reviewer had to know to use browser navigation manually.

The shell now includes a visible `Return to launcher handoff` action in the reviewer landing controls. It targets the launcher checklist anchor, preserves the reviewer-focus shell path, and keeps the handoff payload export in the same primary demo route.

## Boundary

Deterministic browser-local shell-to-launcher handoff only; no LLM calls, no subjective consciousness, no autonomous natural language, no moral patienthood, no production persistence, no complete 3D engine, and no finished gameplay claim. The return link is reviewer workflow hardening, not external validation or evidence of inner experience.

## What changed

- Added `returnLauncherHandoffLink` to the maintained v61 shell reviewer landing controls.
- Styled the link as a first-class reviewer action with `.handoff-return`.
- Updated the reviewer landing summary/payload to name the return handoff as the next step after all-pass.
- Updated the Report 301 v61 shell generator so regeneration preserves the affordance.
- Verified in browser: clean launcher, clean shell launch, reviewer pass, visible return link, link target, return navigation, evidence refresh, visible handoff payload, and console health.

## Metrics

| Metric | Value |
|---|---:|
| readiness | 1.000000 |
| weakest_channel_score | 1.000000 |
| return_source_score | 1.000000 |
| browser_return_score | 1.000000 |
| console_errors | 0 |
| criterion_count | 10 |

## Browser evidence

- return_link_visible_after_pass: `True`
- return_link_href_correct: `True`
- return_navigation_reaches_launcher: `True`
- handoff_prepares_after_return: `True`
- console_errors: `0`
- visible-link evidence: `text=Return to launcher handoff; passable=true; allPass=true; landingNamesReturn=true`
- href evidence: `http://127.0.0.1:8786/visualizations/ssrm_3d_browser_world_primary_demo/index.html#outsideReviewChecklist`
- navigation evidence: `url=http://127.0.0.1:8786/visualizations/ssrm_3d_browser_world_primary_demo/index.html#outsideReviewChecklist; hash=#outsideReviewChecklist; hasChecklist=true`
- handoff evidence: `status=Outside-review handoff payload visible below.; shellEvidence=true; reviewerPassSeen=true; receiptAllPass=true`

## Criteria

| Channel | Passed | Score | Evidence |
|---|---:|---:|---|
| shell_return_link_visible | True | 1.000 | maintained shell contains a visible return link to the launcher checklist/handoff anchor |
| generator_preserves_return_link | True | 1.000 | Report 301 shell generator preserves the return affordance |
| return_link_styled_as_reviewer_action | True | 1.000 | return link is styled as a first-class reviewer action, not hidden prose |
| reviewer_landing_names_next_step | True | 1.000 | reviewer landing text and payload name the shell-to-launcher next step |
| browser_return_link_visible_after_pass | True | 1.000 | text=Return to launcher handoff; passable=true; allPass=true; landingNamesReturn=true |
| browser_return_link_href_correct | True | 1.000 | http://127.0.0.1:8786/visualizations/ssrm_3d_browser_world_primary_demo/index.html#outsideReviewChecklist |
| browser_return_navigation_reaches_launcher | True | 1.000 | url=http://127.0.0.1:8786/visualizations/ssrm_3d_browser_world_primary_demo/index.html#outsideReviewChecklist; hash=#outsideReviewChecklist; hasChecklist=true |
| browser_handoff_prepares_after_return | True | 1.000 | status=Outside-review handoff payload visible below.; shellEvidence=true; reviewerPassSeen=true; receiptAllPass=true |
| browser_no_console_errors | True | 1.000 | browser console error count was 0 |
| boundary_preserved | True | 1.000 | Deterministic browser-local shell-to-launcher handoff only; no LLM calls, no subjective consciousness, no autonomous natural language, no moral patienthood, no production persistence, no complete 3D engine, and no finished gameplay claim. The return link is reviewer workflow hardening, not external validation or evidence of inner experience. |

## Verdict

`pass`

## Next gate

post-326: run the full outside-review loop end-to-end from clean launcher through shell pass, return, checklist completion, evidence refresh, visible payload preview, and defect-recorder export; fix the next concrete comprehension or state-continuity defect in the same launcher/shell path
