# Report 304: SSRM-3D Browser World v64 Primary Demo Manual Playtest Hardening

Report 304 uses the Report 303 primary demo path as intended: run the manual playtest against the real browser surface, find a concrete defect, patch the maintained shell, and record before/after evidence. It does not add another simulation organ.

## Result

- Verdict: `pass`
- Readiness: `0.954133`
- Mean channel score: `0.989333`
- Weakest channel: `single_internal_playtest_not_external_user` at `0.872`
- Runtime defects reproduced: `1`
- Runtime defects fixed: `1`
- Primary demo URL: `http://127.0.0.1:8765/visualizations/ssrm_3d_browser_world_primary_demo/index.html`
- Target shell URL: `http://127.0.0.1:8765/visualizations/ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html?reset=1&source=primary-demo-v63`

## Defect found

Before the patch, `saveWorld` wrote the live world key and `restoreWorld` reloaded that same key. After saving at avatar `x=214`, moving west to `x=180`, restore stayed at `x=180`. That failed the manual-playtest rollback expectation.

## Fix

- Added SAVE_SNAPSHOT_KEY to the maintained v61 shell generator.
- Changed reset behavior to clear the saved snapshot alongside world, replay, QA, and export keys.
- Changed saveWorld to write an explicit rollback snapshot instead of only rewriting live STATE_KEY.
- Changed restoreWorld to restore from the saved snapshot and report the snapshot key in replay payload.
- Changed runSaveRestoreSmoke to mutate after snapshot and verify rollback, not just storage round trip.
- Added the saved snapshot key to v61 and primary-demo QA manifests.

## After-fix browser evidence

- Save point: avatar `x=214`, payload `{'saved': True, 'snapshotKey': 'ssrm_v61_app_shell_saved_snapshot'}`
- Mutation point: avatar `x=180`
- Restore point: avatar `x=214`, payload `{'restored': True, 'snapshotKey': 'ssrm_v61_app_shell_saved_snapshot'}`
- Smoke hook: `{'hook': 'runSaveRestoreSmoke', 'pass': True, 'rollbackTested': True, 'room': 'arrival court'}`
- Export point: `{'bytes': 2454, 'prepared': True, 'rows': 12}`
- Resume point: replay rows `13`, latest event `exportReplay`
- Console errors: `0`

## Manual sequence exercised

| # | Event |
| --- | --- |
| 1 | openPrimaryDemo |
| 2 | launchCleanDemo |
| 3 | enterWorld |
| 4 | moveEast |
| 5 | moveNorth |
| 6 | talkBounded |
| 7 | askSchedule |
| 8 | borrowTool |
| 9 | returnTool |
| 10 | waitOffscreen |
| 11 | saveWorld |
| 12 | moveWest |
| 13 | restoreWorld |
| 14 | runPlaytestChecklist |
| 15 | runStateBoundaryAudit |
| 16 | runSaveRestoreSmoke |
| 17 | exportReplay |
| 18 | resumeDemo |

## Criteria

| Criterion | Passed | Evidence |
| --- | --- | --- |
| source_v61_shell_regenerated | True | Report 301/v61 regenerated with 10 state-boundary rules |
| source_v63_primary_demo_passed | True | Report 303 primary-demo package still passes with 12 manual steps |
| primary_demo_launcher_opened | True | http://127.0.0.1:8765/visualizations/ssrm_3d_browser_world_primary_demo/index.html |
| clean_launch_targets_maintained_shell | True | http://127.0.0.1:8765/visualizations/ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html?reset=1&source=primary-demo-v63 |
| manual_spine_completed | True | 18 primary-demo/manual actions including exportReplay and resumeDemo |
| rollback_defect_reproduced_before_fix | True | before fix: save x=214, mutate x=180, restore stayed x=180 |
| rollback_fixed_after_patch | True | after fix: save x=214, mutate x=180, restore returns x=214 |
| smoke_hook_tests_real_rollback | True | runSaveRestoreSmoke payload pass=true and rollbackTested=true |
| snapshot_key_documented_in_manifests | True | saved snapshot key appears in v61 state-boundary rules and primary-demo state keys |
| resume_keeps_state_after_export | True | resume path reopens shell with replay rows and latest exportReplay event |
| no_console_errors_after_fix | True | fresh after-fix browser tab reported 0 console errors |
| single_internal_playtest_not_external_user | True | one internal browser manual-playtest pass, not an outside user cohort |

## Honest limit

The weakest channel is `single_internal_playtest_not_external_user`. This was one internal browser manual-playtest pass, not an external user cohort or production-readiness claim.

## Boundary

Primary-demo browser manual-playtest hardening over the deterministic maintained v61 shell only; no new simulation organ, no LLM call, no subjective consciousness, no real consent, no autonomous natural language, no moral patienthood, no production persistence, no finished gameplay, no complete 3D engine, and no metaphysical frequency claim.

## Next gate

post-304: keep the primary demo as the only review surface, add a tiny in-page defect ledger/manual pass recorder, and continue hardening defects found through the same primary-demo path.
