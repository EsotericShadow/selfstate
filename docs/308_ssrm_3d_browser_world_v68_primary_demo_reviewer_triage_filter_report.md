# Report 308: SSRM-3D Browser World v68 Primary Demo Reviewer Triage Filter

## Purpose

Report 308 keeps consolidation pressure on the single playable browser-world surface. It adds a reviewer-facing filter dashboard for the browser-local manual defect ledger created in Reports 305-307, so a real playtest can separate open, resolved, watch, minor, and blocking issues without forking the demo or hiding defects in prose.

This is not a new simulation organ. It is a usability and evidence-inspection hardening pass for the primary demo path.

## Boundary

Deterministic browser-local reviewer workflow only: no LLM calls, no subjective consciousness, no autonomous natural language, no moral patienthood, no production persistence, no finished gameplay claim, and no claim that a filtered defect ledger proves agent interiority.

## What changed

- The primary demo launcher now loads `triage_filters.js` after `demo.js`.
- The manual recorder UI now exposes all/open/resolved status filters.
- The defect ledger view now exposes severity filtering for watch/minor/blocking defects.
- The dashboard reads the same `ssrm_primary_demo_defect_ledger` key as the recorder and persists reviewer filter state in `ssrm_primary_demo_defect_filter_state`.
- Defect notes and resolution notes are escaped before display.
- Counts show filtered, total, open, resolved, and blocking-open defects.

## Metrics

| Metric | Value |
|---|---:|
| readiness | 1.000000 |
| weakest_channel_score | 1.000000 |
| source_static_pass_rate | 1.000000 |
| review_filter_coverage | 1.000000 |
| browser_workflow_score | 1.000000 |
| criterion_count | 15 |

## Browser evidence

Direct browser workflow pass: `True`; console errors: `0`; status filter evidence: `{'open_summary': '1/2 shown | open 1 | resolved 1 | blocking open 1', 'open_filter_only_showed_blocking_open': True, 'resolved_summary': '1/2 shown | open 1 | resolved 1 | blocking open 1', 'resolved_filter_only_showed_minor_resolved': True}`; severity filter evidence: `{'blocking_summary': '1/2 shown | open 1 | resolved 1 | blocking open 1', 'blocking_filter_only_showed_blocking_defect': True, 'watch_summary': '0/2 shown | open 1 | resolved 1 | blocking open 1', 'watch_filter_showed_empty_state': True}`.

## Criteria

| Channel | Passed | Score | Evidence |
|---|---:|---:|---|
| single_primary_surface | True | 1.000 | primary launcher still targets the maintained v61 shell rather than a forked world |
| visible_boundary | True | 1.000 | launcher boundary remains visible before play |
| recorder_schema_retained | True | 1.000 | manual recorder and Report 307 resolution fields remain in the primary demo script |
| triage_script_bound | True | 1.000 | primary demo loads a separate reviewer filter script after the recorder script |
| status_filter_paths | True | 1.000 | all/open/resolved filter paths are present in generated markup and script |
| severity_filter_paths | True | 1.000 | severity filtering supports watch, minor, and blocking categories |
| persistent_filter_state | True | 1.000 | reviewer filter preference persists in browser-local storage |
| shared_defect_ledger | True | 1.000 | filters read the same ledger key used by the manual recorder |
| record_resolve_refresh | True | 1.000 | dashboard refreshes after recording and resolving defects |
| escaped_ledger_rendering | True | 1.000 | defect notes and resolution text are escaped before rendering |
| count_dashboard | True | 1.000 | summary shows filtered count, open count, resolved count, and blocking-open count |
| empty_state | True | 1.000 | filter dashboard has a clear empty state |
| qa_manifest_survives | True | 1.000 | generated QA manifest still advertises triage fields from Report 307 |
| generated_readme_boundary | True | 1.000 | generated demo README keeps the local primary-demo boundary visible |
| direct_browser_workflow | True | 1.000 | browser workflow_pass=True console_errors=0 |

## Verdict

`pass`

The report should only be treated as passed when the direct browser workflow evidence is present. Static source checks are useful, but this specific report is about a visible reviewer workflow.

## Next gate

post-308: use the filtered ledger during a full manual playtest pass, then fix one blocking defect in the maintained shell only if the ledger shows a reproducible issue
