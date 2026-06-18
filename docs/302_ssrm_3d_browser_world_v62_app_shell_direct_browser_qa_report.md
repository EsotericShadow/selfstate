# Report 302: SSRM-3D Browser World v62 App-Shell Direct Browser QA

## Purpose

Report 302 executes the post-301 gate: direct browser QA against the maintained v61 app shell. This is not another simulation organ. It records actual localhost browser evidence, fixes runtime defects found during the pass, and keeps the next work focused on the single playable shell.

## Browser QA setup

- Served repo locally at `http://127.0.0.1:8765/`.
- Opened `visualizations/ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html?reset=1&qa=302c` in the in-app browser.
- Used real UI buttons identified by `data-action` attributes.
- Collected evidence from the visible DOM trace, QA manifest, playtest checklist, replay panel, prepared replay export link, and browser console logs.

## Runtime fixes made during QA

1. Added the missing `Ask schedule` button for the existing `askSchedule` action.
2. Changed replay export so it prepares a localStorage-backed replay payload and visible link instead of forcing an unsupported browser download event.
3. Changed state-boundary audit to inspect a sanitized public-state projection so audit payloads do not poison later audits with forbidden-key names.
4. Added a `?reset=1` clean-start path for repeatable browser QA.

## Result

- Command: `python3 -m experiments.ssrm_3d_browser_world_v62_app_shell_direct_browser_qa`
- Seed: `20270630`
- Verdict: `pass`
- Readiness: `0.952000`
- Mean channel score: `0.988000`
- Weakest channel: `single_browser_run_not_playtest_cohort` at `0.868000`

## Evidence counts

| Evidence | Count |
| --- | ---: |
| Clicked UI actions | 17 |
| Interesting replay events | 13 |
| Runtime fixes | 4 |
| QA rows | 10 |
| QA passes | 10 |
| Replay rows | 20 |
| Resident count | 6 |
| Console errors | 0 |

## Browser QA channels

| Channel | Score |
| --- | ---: |
| `source_v61_continuity` | `1.000000` |
| `localhost_app_opened` | `1.000000` |
| `core_action_sequence_completed` | `1.000000` |
| `ask_schedule_runtime_control_present` | `1.000000` |
| `playtest_checklist_passed` | `1.000000` |
| `state_boundary_audit_passed` | `1.000000` |
| `save_restore_smoke_passed` | `1.000000` |
| `visible_consequence_loop_exercised` | `1.000000` |
| `replay_export_prepared_without_download` | `1.000000` |
| `no_console_errors` | `1.000000` |
| `single_browser_run_not_playtest_cohort` | `0.868000` |


## Key browser evidence

- `Ask schedule` button count: `1`.
- Playtest checklist: `10` / `10` pass.
- State-boundary audits: `[True, True]`.
- Forbidden private/LLM keys in visible world trace: `privateWorkspace=False`, `subjectiveFeeling=False`, `llmTranscript=False`.
- Replay export: latest event `exportReplay`, prepared `True`, bytes `3589`.
- Browser console errors: `0`.

## Honest limitation

The weakest channel is `single_browser_run_not_playtest_cohort` at `0.868000`. That cap is intentional. Report 302 proves one direct automated browser pass, not an external user playtest cohort or production readiness. The next work should package the app shell as the primary demo entry point and continue fixing defects found in that shell.

## Artifacts

- `experiments/ssrm_3d_browser_world_v62_app_shell_direct_browser_qa.py`
- `artifacts/ssrm_3d_browser_world_v62_app_shell_direct_browser_qa_results.json`
- `artifacts/ssrm_3d_browser_world_v62_app_shell_direct_browser_qa_state.json`
- `artifacts/ssrm_3d_browser_world_v62_app_shell_direct_browser_qa_summary.csv`
- `artifacts/ssrm_3d_browser_world_v62_app_shell_direct_browser_qa_verdict.csv`
- `artifacts/ssrm_3d_browser_world_v62_app_shell_direct_browser_qa_criteria.csv`
- `artifacts/ssrm_3d_browser_world_v62_app_shell_direct_browser_qa_click_sequence.csv`
- `artifacts/ssrm_3d_browser_world_v62_app_shell_direct_browser_qa_browser_evidence.json`

## Boundary

Direct browser QA evidence over the deterministic browser-local v61 app shell only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, production persistence, finished gameplay, complete 3D engine, or metaphysical frequency claim.

## Next gate

post-302 hardening: package the maintained app shell as the primary demo entry point, add a minimal manual playtest script, and reduce future work to defects found in the single playable shell before adding any new generated report organs.
