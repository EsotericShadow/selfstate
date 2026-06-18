# Report 322: SSRM-3D Browser World v82 Primary Demo Actionable Landing Failures

## Purpose

Report 322 makes the reviewer landing useful when the integrated receipt is not passing yet. Instead of only showing `READY_FOR_RUN`, the landing now maps each failing public receipt field to a concrete recovery action and can convert the current failure set into blocking observation rows.

This is consolidation of the review workflow in the maintained playable shell, not a new simulation branch.

## Boundary

Deterministic browser-local landing-failure actionability only; no LLM calls, no subjective consciousness, no autonomous natural language, no moral patienthood, no production persistence, no complete 3D engine, and no finished gameplay claim. The failure map is reviewer guidance over public receipt state, not autonomous debugging or hidden cognition.

## What changed

- Added a field-level `Actionable failure map` to the reviewer landing output.
- Added recovery guidance for entry, schedule, debt, offscreen life, trust repair, resident social memory, public history, replay export, and resume snapshot fields.
- Added `Audit failures`, which records the current failing receipt fields as blocking receipt observations and switches observation triage to the blocking filter.
- Preserved reviewer-focus mode and optional deep-panel reveal, so actionability does not force reviewers into the debug surface.
- Verified clean failure guidance, blocking observation creation, all-pass guidance after reviewer pass, deep-panel reveal after audit, resume actionability, and console cleanliness in browser.

## Metrics

| Metric | Value |
|---|---:|
| readiness | 1.000000 |
| weakest_channel_score | 1.000000 |
| failure_action_map_score | 1.000000 |
| browser_audit_score | 1.000000 |
| console_errors | 0 |
| criterion_count | 10 |

## Browser evidence

- ready_failure_map_pass: `True`
- audit_blocks_failures_pass: `True`
- pass_clears_failure_map_pass: `True`
- deep_toggle_after_audit_pass: `True`
- resume_actionability_pass: `True`
- console_errors: `0`
- ready evidence: `Reviewer landing: READY_FOR_RUN | Boundary: deterministic browser-local public state only; no consciousness, no autonomous language, no moral patienthood. | Focus mode: core panels only | Core path: boundary -> Run reviewer pass -> session transcript -> integrated receipt -> observation triage | Receipt: 0/9 pass | Observation triage: 0 observations / active filter all | Missing reviewer-pass events: runContinuityLoop, generateScenarioReceipt | Actionable failure map: | FIX entry_and_movement: Click Enter or use Run reviewer pass to establish avatar entry. Current evidence: avatar entered the maintained shell | FIX schedule_visibility: Ask schedule or run the reviewer pass so the selected resident schedule is public. Current evidence: selected resident schedule was queried and remains visible | FIX debt_consequence: Borrow/return or run the reviewer pass to create a visible debt/trust consequence. Current evidence: debt/trust consequence happened before bounded repair | FIX offscreen_life: Use Wait offscreen or run the reviewer pass to advance resident progress while absent. Current evidence: offscreen resident progress advanced during the loop`
- audit evidence: `Observation triage filter: blocking | Counts: total 9 | open 9 | watch 0 | minor 0 | blocking 9 | resolved 0 | Visible rows: 9 | landing-block-2 | open | blocking | schedule_visibility | receipt=FAIL | landing-block-3 | open | blocking | debt_consequence | receipt=FAIL | landing-block-4 | open | blocking | offscreen_life | receipt=FAIL | landing-block-5 | open | blocking | recoverable_trust_repair | receipt=FAIL | landing-block-6 | open | blocking | resident_social_memory | receipt=FAIL / transcript=t0 arrival court / Ari: audited landing failures=9 blockingRows=9`
- pass evidence: `Reviewer landing: PASSABLE_REVIEW_PATH | Boundary: deterministic browser-local public state only; no consciousness, no autonomous language, no moral patienthood. | Focus mode: deep panels visible | Core path: boundary -> Run reviewer pass -> session transcript -> integrated receipt -> observation triage | Receipt: 9/9 pass | Observation triage: 9 observations / active filter all | Missing reviewer-pass events: none | Actionable failure map: | All receipt fields currently pass. Keep deep panels optional unless a reviewer wants trace detail. | Deep diagnostics: visible for trace, checkpoints, history, and QA manifest / receipt=Integrated scenario receipt: ALL_PASS (9/9)`
- deep toggle evidence: `body= trace=block transcriptTail=t0 arrival court / Ari: audited landing failures=9 blockingRows=9 | t1 arrival court / Ari: deep panels visible=true`
- resume evidence: `body=reviewer-focus trace=none landing=Reviewer landing: PASSABLE_REVIEW_PATH | Boundary: deterministic browser-local public state only; no consciousness, no autonomous language, no moral patienthood. | Focus mode: core panels only | Core path: boundary -> Run reviewer pass -> session transcript -> integrated receipt -> observation triage | Receipt: 9/9 pass | Observation triage: 9 observations / active filter all | Missing reviewer-pass events: none | Actionable failure map: | All receipt fields currently pass. Keep deep panels optional unless a reviewer wants trace detail. triage=Observation triage filter: all | Counts: total 9 | open 9 | watch 0 | minor 0 | blocking 9 | resolved 0 | Visible rows: 9 | landing-block-2 | open | blocking | schedule_visibility | receipt=FAIL`

## Criteria

| Channel | Passed | Score | Evidence |
|---|---:|---:|---|
| failure_action_map_generated | True | 1.000 | reviewer landing failure map is generated from the maintained source and present in app.js |
| audit_failures_action_present | True | 1.000 | landing panel includes an Audit failures action wired to app logic |
| blocking_observation_route | True | 1.000 | failure audit records current failing receipt fields as blocking observations and opens the blocking triage filter |
| deep_panels_preserved | True | 1.000 | optional diagnostics remain hidden by default but revealable on demand |
| browser_ready_failure_map | True | 1.000 | Reviewer landing: READY_FOR_RUN | Boundary: deterministic browser-local public state only; no consciousness, no autonomous language, no moral patienthood. | Focus mode: core panels only | Core path: boundary -> Run reviewer pass -> session transcript -> integrated receipt -> observation triage | Receipt: 0/9 pass | Observation triage: 0 observations / active filter all | Missing reviewer-pass events: runContinuityLoop, generateScenarioReceipt | Actionable failure map: | FIX entry_and_movement: Click Enter or use Run reviewer pass to establish avatar entry. Current evidence: avatar entered the maintained shell | FIX schedule_visibility: Ask schedule or run the reviewer pass so the selected resident schedule is public. Current evidence: selected resident schedule was queried and remains visible | FIX debt_consequence: Borrow/return or run the reviewer pass to create a visible debt/trust consequence. Current evidence: debt/trust consequence happened before bounded repair | FIX offscreen_life: Use Wait offscreen or run the reviewer pass to advance resident progress while absent. Current evidence: offscreen resident progress advanced during the loop |
| browser_audit_blocks_failures | True | 1.000 | Observation triage filter: blocking | Counts: total 9 | open 9 | watch 0 | minor 0 | blocking 9 | resolved 0 | Visible rows: 9 | landing-block-2 | open | blocking | schedule_visibility | receipt=FAIL | landing-block-3 | open | blocking | debt_consequence | receipt=FAIL | landing-block-4 | open | blocking | offscreen_life | receipt=FAIL | landing-block-5 | open | blocking | recoverable_trust_repair | receipt=FAIL | landing-block-6 | open | blocking | resident_social_memory | receipt=FAIL / transcript=t0 arrival court / Ari: audited landing failures=9 blockingRows=9 |
| browser_pass_clears_failure_map | True | 1.000 | Reviewer landing: PASSABLE_REVIEW_PATH | Boundary: deterministic browser-local public state only; no consciousness, no autonomous language, no moral patienthood. | Focus mode: deep panels visible | Core path: boundary -> Run reviewer pass -> session transcript -> integrated receipt -> observation triage | Receipt: 9/9 pass | Observation triage: 9 observations / active filter all | Missing reviewer-pass events: none | Actionable failure map: | All receipt fields currently pass. Keep deep panels optional unless a reviewer wants trace detail. | Deep diagnostics: visible for trace, checkpoints, history, and QA manifest / receipt=Integrated scenario receipt: ALL_PASS (9/9) |
| browser_deep_toggle_after_audit | True | 1.000 | body= trace=block transcriptTail=t0 arrival court / Ari: audited landing failures=9 blockingRows=9 | t1 arrival court / Ari: deep panels visible=true |
| browser_resume_actionability | True | 1.000 | body=reviewer-focus trace=none landing=Reviewer landing: PASSABLE_REVIEW_PATH | Boundary: deterministic browser-local public state only; no consciousness, no autonomous language, no moral patienthood. | Focus mode: core panels only | Core path: boundary -> Run reviewer pass -> session transcript -> integrated receipt -> observation triage | Receipt: 9/9 pass | Observation triage: 9 observations / active filter all | Missing reviewer-pass events: none | Actionable failure map: | All receipt fields currently pass. Keep deep panels optional unless a reviewer wants trace detail. triage=Observation triage filter: all | Counts: total 9 | open 9 | watch 0 | minor 0 | blocking 9 | resolved 0 | Visible rows: 9 | landing-block-2 | open | blocking | schedule_visibility | receipt=FAIL |
| console_clean | True | 1.000 | browser console error count was 0 |

## Verdict

`pass`

The result keeps the claim narrow: it improves reviewer workflow over deterministic public browser state. It does not claim subjective consciousness, autonomous debugging, moral status, production readiness, complete gameplay, or a complete 3D engine.

## Next gate

post-322: make the reviewer-first shell more handoff-ready by packaging the launcher, landing, manual script, receipt, observation triage, and boundary into one outside-review checklist
