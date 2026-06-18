# Report 303: SSRM-3D Browser World v63 Primary Demo Entrypoint Manual Playtest Package

Report 303 is a consolidation gate. It packages the maintained v61 app shell as the stable primary browser-world demo entrypoint and adds a manual playtest script. It does not add another world organ.

## Result

- Verdict: `pass`
- Readiness: `0.951273`
- Mean channel score: `0.987818`
- Weakest channel: `manual_playtest_not_external_cohort` at `0.866`
- Primary demo URL: `http://127.0.0.1:8765/visualizations/ssrm_3d_browser_world_primary_demo/index.html`
- Target shell: `../ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html`
- Source browser QA: `artifacts/ssrm_3d_browser_world_v62_app_shell_direct_browser_qa_results.json` verdict `pass`

## Why this exists

The browser-world line was at risk of becoming a pile of bridge artifacts. The practical next step is one stable URL-style place to start, with a repeatable manual script, while preserving the single maintained shell that Report 302 directly browser-tested.

## Manual playtest script

| Step | Action | Expected evidence |
| --- | --- | --- |
| MP-01 | Start a local server from the repo root with python3 -m http.server 8765 --bind 127.0.0.1. | Primary demo launcher opens at the localhost URL. |
| MP-02 | Open the primary demo launcher and read the boundary before launching. | Boundary says deterministic browser-local shell and no consciousness/LLM/product claim. |
| MP-03 | Launch a clean session using the Clean demo button. | The maintained v61 shell opens with ?reset=1 and a primary-demo source tag. |
| MP-04 | Enter the world and move at least twice. | Room/status fields update and replay rows increase. |
| MP-05 | Talk through the bounded phrase control, then ask schedule. | Resident memory/schedule fields update without open-ended chat claims. |
| MP-06 | Borrow and return the awning tool. | Debt increases, then returns to zero while trust repairs partially. |
| MP-07 | Wait offscreen, then inspect schedule/progress again. | Progress changes while the avatar is idle/absent. |
| MP-08 | Save, move/change state, then restore. | Saved avatar/resident values return after a deliberate post-save mutation and restore. |
| MP-09 | Run the built-in playtest checklist. | Checklist reports 10 checks and all pass. |
| MP-10 | Run state-boundary, save/restore smoke, and Audit after rollback hooks. | The audit-after-rollback row passes with rollbackTested, smokePass, and auditPass all true. |
| MP-11 | Export replay from the UI. | A prepared replay export link appears and export bytes are nonzero. |
| MP-12 | Close the shell, reopen the primary launcher, then use Resume demo. | The resumed shell keeps persisted world state unless Clean demo is used. |

## Packaging criteria

| Criterion | Passed | Evidence |
| --- | --- | --- |
| source_v61_shell_present | True | visualizations/ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html |
| source_v62_browser_qa_passed | True | Report 302 direct browser QA verdict pass with 0 console errors |
| stable_primary_entrypoint_declared | True | http://127.0.0.1:8765/visualizations/ssrm_3d_browser_world_primary_demo/index.html |
| manual_playtest_script_complete | True | 12 required manual playtest steps |
| outside_review_checklist_present | True | 7 outside-review handoff items |
| one_shell_policy_preserved | True | ../ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html |
| scope_boundary_visible_before_launch | True | launcher includes explicit boundary section |
| qa_manifest_handoff_present | True | handoff state key listed in QA manifest |
| runner_registered | True | experiments/ssrm_3d_browser_world_v63_primary_demo_entrypoint_manual_playtest_package.py |
| source_evidence_retained | True | Report 302 browser evidence retained with 10 QA passes |
| manual_playtest_not_external_cohort | True | manual script is ready, but no outside cohort has run it |

## Scope guards

- Only the primary demo launcher is new; gameplay still lives in the maintained v61 app shell.
- The manual script uses Report 302 browser evidence as the baseline, not as a substitute for future human playtests.
- The launcher gives clean and resume paths so persistence bugs can be reproduced rather than hidden.
- The boundary remains visible before launch and inside the shell.
- Future browser-world work should patch this shell unless a defect proves a new surface is necessary.

## Honest limit

The weakest channel is `manual_playtest_not_external_cohort`. That cap is intentional: this report makes the demo easier to launch and manually review, but it is not an outside playtest cohort, a finished game, a production deployment, or a consciousness claim.

## Boundary

Primary demo packaging for the deterministic browser-local maintained app shell only; no new simulation organ, no LLM call, no subjective consciousness, no real consent, no autonomous natural language, no moral patienthood, no production persistence, no finished gameplay, no complete 3D engine, and no metaphysical frequency claim.

## Next gate

post-303: use the stable primary demo entrypoint for all browser-world work, run the manual playtest script against real defects, and harden the same shell before adding any new world-system report.
