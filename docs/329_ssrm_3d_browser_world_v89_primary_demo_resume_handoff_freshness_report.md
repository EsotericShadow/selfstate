# Report 329: SSRM-3D Browser World v89 Primary Demo Resume Handoff Freshness

## Purpose

Report 329 continues the cold one-URL handoff hardening after Report 328. The pre-patch reload/resume run found a concrete drift: after `Resume demo`, refreshed shell evidence pointed at the new resume launch handoff, but the visible prepared outside-review handoff payload still referenced the older clean launch handoff with no stale-payload warning.

The launcher now computes `handoffPayloadFreshnessState` for any visible prepared handoff payload. When refreshed shell evidence, recorder counts, or launch handoff state no longer match the prepared payload, the preview stays inspectable but is marked stale and tells the reviewer to re-run `Prepare outside-review handoff`.

## Boundary

Deterministic browser-local resume handoff freshness only; no LLM calls, no subjective consciousness, no autonomous natural language, no moral patienthood, no production persistence, no complete 3D engine, and no finished gameplay claim. Freshness warnings are review evidence hygiene, not external validation or evidence of inner experience.

## Pre-patch blocker

- After Resume demo, refreshed shell evidence points at the resume launch handoff while the visible prepared handoff payload still points at the older clean launch, with no stale-payload warning.

## What changed

- Added `handoffPayloadFreshnessState(payload)` to the primary launcher.
- `renderOutsideReviewHandoffPreview` now adds `previewFreshness` while preserving the exported payload fields at top level.
- `renderOutsideReviewEvidence` refreshes the handoff preview freshness when shell evidence changes.
- Stale previews now show an actionable warning: `Re-run Prepare outside-review handoff`.
- Verified in browser that reload plus resume exposes clean-vs-resume handoff drift as stale, keeps payload contents inspectable, and produces no console errors.

## Metrics

| Metric | Value |
|---|---:|
| readiness | 1.000000 |
| weakest_channel_score | 1.000000 |
| freshness_source_score | 1.000000 |
| browser_stale_warning_score | 1.000000 |
| console_errors | 0 |
| criterion_count | 10 |

## Browser evidence

- resume_stale_warning_visible: `True`
- preview_freshness_marks_stale: `True`
- detects_handoff_kind_mismatch: `True`
- original_payload_still_inspectable: `True`
- prior_completion_not_broken: `True`
- console_errors: `0`
- stale warning evidence: `Prepared handoff payload is stale: launch handoff changed, launch kind changed. Re-run Prepare outside-review handoff.`
- freshness evidence: `{"boundary":"outside-review-handoff-freshness-public-local-only","currentHandoffKind":"resume","currentHandoffRecordedAt":"2026-06-18T09:01:04.757Z","currentManualRecordCount":1,"currentReplayRows":16,"fresh":false,"mismatches":["launch handoff changed","launch kind changed"],"payloadHandoffKind":"clean","payloadHandoffRecordedAt":"2026-06-18T09:01:01.738Z","payloadManualRecordCount":1,"payloadReplayRows":16}`
- mismatch evidence: `payload=clean; current=resume; mismatches=launch handoff changed|launch kind changed`
- payload evidence: `hasShellEvidence=true; hasCompletion=true; hasFreshness=true`

## Criteria

| Channel | Passed | Score | Evidence |
|---|---:|---:|---|
| pre_patch_resume_stale_payload_found | True | 1.000 | After Resume demo, refreshed shell evidence points at the resume launch handoff while the visible prepared handoff payload still points at the older clean launch, with no stale-payload warning. |
| freshness_source_generated | True | 1.000 | launcher generator and emitted JS contain handoff payload freshness detection |
| browser_resume_stale_warning_visible | True | 1.000 | Prepared handoff payload is stale: launch handoff changed, launch kind changed. Re-run Prepare outside-review handoff. |
| browser_preview_freshness_marks_stale | True | 1.000 | {"boundary":"outside-review-handoff-freshness-public-local-only","currentHandoffKind":"resume","currentHandoffRecordedAt":"2026-06-18T09:01:04.757Z","currentManualRecordCount":1,"currentReplayRows":16,"fresh":false,"mismatches":["launch handoff changed","launch kind changed"],"payloadHandoffKind":"clean","payloadHandoffRecordedAt":"2026-06-18T09:01:01.738Z","payloadManualRecordCount":1,"payloadReplayRows":16} |
| browser_detects_handoff_kind_mismatch | True | 1.000 | payload=clean; current=resume; mismatches=launch handoff changed|launch kind changed |
| browser_original_payload_still_inspectable | True | 1.000 | hasShellEvidence=true; hasCompletion=true; hasFreshness=true |
| browser_reload_resume_console_clean | True | 1.000 | browser console error count was 0 |
| prior_completion_not_broken | True | 1.000 | ready=true; fresh=true |
| stale_warning_actionable | True | 1.000 | stale warning tells reviewers the exact recovery action |
| boundary_preserved | True | 1.000 | Deterministic browser-local resume handoff freshness only; no LLM calls, no subjective consciousness, no autonomous natural language, no moral patienthood, no production persistence, no complete 3D engine, and no finished gameplay claim. Freshness warnings are review evidence hygiene, not external validation or evidence of inner experience. |

## Verdict

`pass`

## Next gate

post-329: continue reload/resume review hardening by checking whether a stale handoff can be safely re-prepared after resume without losing recorder, checklist, or shell evidence continuity
