# Report 332: SSRM-3D Browser World v92 Primary Demo Readable Handoff Restart Bridge

## Purpose

Report 332 fixes the next restart-friction defect in the consolidated primary demo. Report 331 proved that a re-prepared `resume` handoff persists after another launcher reload, but the visible status line still only said `Outside-review handoff payload visible below.` The `resume` binding was present in the raw JSON, so a cold reviewer had to inspect JSON for a critical restart fact.

The primary launcher now renders a concise readable handoff summary whenever the prepared payload is fresh. The summary names freshness, launch kind, checklist completion, shell evidence readiness, recorder/export evidence, and the next action. The raw JSON preview remains visible and now includes `previewReadableSummary` alongside `previewFreshness`.

## Boundary

Deterministic browser-local readable handoff restart bridge only; no LLM calls, no subjective consciousness, no autonomous natural language, no moral patienthood, no production persistence, no complete 3D engine, and no finished gameplay claim. This is local review UX and evidence readability hygiene, not external validation or evidence of inner experience.

## Pre-patch blocker

- persisted re-prepared handoff requires raw JSON inspection for at least one reviewer-critical fact
- visible non-JSON handoff text does not say the payload is resume-bound

## What changed

- Added `readableHandoffSummary(payload, freshness)` to the primary launcher and generator.
- Fresh prepared handoffs now show a readable status line such as: `Outside-review handoff ready: fresh resume handoff; checklist 7/7; shell evidence reviewer pass seen / receipt 9/9 / replay export ready; recorder 1 manual record(s) / export ready; next action: inspect or download Prepared outside-review handoff.`
- Stale prepared handoffs now explain payload kind versus current shell kind, for example: `Prepared handoff payload is stale: launch handoff changed, launch kind changed. Payload is clean while current shell is resume. Re-run Prepare outside-review handoff.`
- Raw JSON preview remains available and includes both `previewFreshness` and `previewReadableSummary`.

## Metrics

| Metric | Value |
|---|---:|
| readiness | 1.000000 |
| weakest_channel_score | 1.000000 |
| pre_patch_readable_score | 0.833333 |
| post_patch_readable_score | 1.000000 |
| visible_restart_fact_score | 1.000000 |
| json_audit_preservation_score | 1.000000 |
| console_errors | 0 |
| criterion_count | 15 |

## Browser evidence summary

- stale_warning_mentions_payload_and_current_kinds: `True`
- visible_summary_mentions_fresh: `True`
- visible_summary_mentions_resume: `True`
- visible_summary_mentions_checklist: `True`
- visible_summary_mentions_recorder: `True`
- visible_summary_mentions_shell_evidence: `True`
- visible_summary_mentions_next_action: `True`
- visible_summary_complete_without_json: `True`
- raw_json_preview_still_available: `True`
- preview_readable_summary_exported: `True`
- no_console_errors: `True`

## Persisted visible summary after reload

```text
Outside-review handoff ready: fresh resume handoff; checklist 7/7; shell evidence reviewer pass seen / receipt 9/9 / replay export ready; recorder 1 manual record(s) / export ready; next action: inspect or download Prepared outside-review handoff.
```

## Criteria

| Channel | Passed | Score | Evidence |
|---|---:|---:|---|
| report_331_reload_persistence_gate_passed | True | 1.000 | Report 331 verdict=pass weakest=1.0 |
| pre_patch_readability_defect_found | True | 1.000 | persisted re-prepared handoff requires raw JSON inspection for at least one reviewer-critical fact; visible non-JSON handoff text does not say the payload is resume-bound |
| readable_summary_source_generated | True | 1.000 | primary launcher generator and emitted JS contain readableHandoffSummary and exported previewReadableSummary |
| stale_warning_explains_payload_and_current_kinds | True | 1.000 | Prepared handoff payload is stale: launch handoff changed, launch kind changed. Payload is clean while current shell is resume. Re-run Prepare outside-review handoff. |
| visible_summary_mentions_fresh | True | 1.000 | Outside-review handoff ready: fresh resume handoff; checklist 7/7; shell evidence reviewer pass seen / receipt 9/9 / replay export ready; recorder 1 manual record(s) / export ready; next action: inspect or download Prepared outside-review handoff. |
| visible_summary_mentions_resume | True | 1.000 | Outside-review handoff ready: fresh resume handoff; checklist 7/7; shell evidence reviewer pass seen / receipt 9/9 / replay export ready; recorder 1 manual record(s) / export ready; next action: inspect or download Prepared outside-review handoff. |
| visible_summary_mentions_checklist | True | 1.000 | Outside-review handoff ready: fresh resume handoff; checklist 7/7; shell evidence reviewer pass seen / receipt 9/9 / replay export ready; recorder 1 manual record(s) / export ready; next action: inspect or download Prepared outside-review handoff. |
| visible_summary_mentions_recorder | True | 1.000 | Outside-review handoff ready: fresh resume handoff; checklist 7/7; shell evidence reviewer pass seen / receipt 9/9 / replay export ready; recorder 1 manual record(s) / export ready; next action: inspect or download Prepared outside-review handoff. |
| visible_summary_mentions_shell_evidence | True | 1.000 | Outside-review handoff ready: fresh resume handoff; checklist 7/7; shell evidence reviewer pass seen / receipt 9/9 / replay export ready; recorder 1 manual record(s) / export ready; next action: inspect or download Prepared outside-review handoff. |
| visible_summary_mentions_next_action | True | 1.000 | Outside-review handoff ready: fresh resume handoff; checklist 7/7; shell evidence reviewer pass seen / receipt 9/9 / replay export ready; recorder 1 manual record(s) / export ready; next action: inspect or download Prepared outside-review handoff. |
| visible_summary_complete_without_json | True | 1.000 | readableScore=1 checks={'hasReadableAction': True, 'hasReadableChecklist': True, 'hasReadableFresh': True, 'hasReadableRecorder': True, 'hasReadableResume': True, 'hasReadableShell': True} |
| raw_json_preview_still_available | True | 1.000 | {'boundary': 'outside-review-handoff-freshness-public-local-only', 'currentHandoffKind': 'resume', 'currentHandoffRecordedAt': '2026-06-18T09:19:02.691Z', 'currentManualRecordCount': 1, 'currentReplayRows': 16, 'fresh': True, 'mismatches': [], 'payloadHandoffKind': 'resume', 'payloadHandoffRecordedAt': '2026-06-18T09:19:02.691Z', 'payloadManualRecordCount': 1, 'payloadReplayRows': 16} |
| preview_readable_summary_exported | True | 1.000 | Outside-review handoff ready: fresh resume handoff; checklist 7/7; shell evidence reviewer pass seen / receipt 9/9 / replay export ready; recorder 1 manual record(s) / export ready; next action: inspect or download Prepared outside-review handoff. |
| browser_console_clean | True | 1.000 | consoleErrors=0 messages=[] |
| boundary_preserved | True | 1.000 | Deterministic browser-local readable handoff restart bridge only; no LLM calls, no subjective consciousness, no autonomous natural language, no moral patienthood, no production persistence, no complete 3D engine, and no finished gameplay claim. This is local review UX and evidence readability hygiene, not external validation or evidence of inner experience. |

## Verdict

`pass`

## Next gate

post-332: run a cold reviewer restart from the readable handoff card and verify the reviewer can continue using visible controls/status text only, without raw JSON or localStorage inspection
