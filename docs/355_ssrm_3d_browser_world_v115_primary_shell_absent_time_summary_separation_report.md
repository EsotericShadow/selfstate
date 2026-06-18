# Report 355: Browser World v115 Primary Shell Absent-Time Summary Separation

Report 355 keeps the integration work inside the maintained v61 shell. Report 354 made offscreen resident activity create a persistent cross-resident obligation; this report adds a small visible absent-time summary that separates avatar-caused absence from resident-caused offscreen changes before the player chooses which obligation to handle.

Boundary: Browser-local absent-time summary separation over the maintained v61 shell only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, production persistence, hosted URL proof, complete 3D engine, finished gameplay, or metaphysical claim.

## Result

Verdict: `pass`
Readiness: `1.000`
Weakest channel score: `1.000`
Criteria passed: `17 / 17`

## Browser-smoke evidence

- Maintained shell URL: `http://127.0.0.1:8775/visualizations/ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html`
- Before summary: `No absent-time summary yet.`
- After summary: `Phase: before-obligation-choice
Avatar-caused: avatar chose Wait offscreen at replay row 1; avatar did not choose the new obligation target
Resident-caused: Fay changed Milo's obligation while avatar absent; milo-offscreen-water-jars is open / offscreen-pending
Before choosing: Milo obligation is selectable before resolve/defer; schedule pending; debt outstanding`
- After reload summary: `Phase: before-obligation-choice
Avatar-caused: avatar chose Wait offscreen at replay row 1; avatar did not choose the new obligation target
Resident-caused: Fay changed Milo's obligation while avatar absent; milo-offscreen-water-jars is open / offscreen-pending
Before choosing: Milo obligation is selectable before resolve/defer; schedule pending; debt outstanding`
- Obligation list before choice: `milo-offscreen-water-jars: open / offscreen-pending / Milo offscreen obligation open from Fay: inspect leaking water jars`
- Console errors: `0`

## Criteria

| Criterion | Score | Evidence |
| --- | ---: | --- |
| `report_354_offscreen_gate_passing` | `1.0` | Report 354 verdict=pass weakest=1.0 |
| `source_exposes_absent_time_summary` | `1.0` | app.js exposes absentTimeSummary state, render, update, and boundary |
| `visible_absent_time_panel_wired` | `1.0` | index.html exposes Absent time dashboard panel |
| `wait_offscreen_updates_summary_before_log` | `1.0` | waitOffscreen updates summary before replay log |
| `browser_smoke_artifact_exists` | `1.0` | artifacts/ssrm_3d_browser_world_v115_primary_shell_absent_time_summary_separation_browser_smoke.json |
| `browser_smoke_used_maintained_shell` | `1.0` | http://127.0.0.1:8775/visualizations/ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html |
| `before_offscreen_summary_empty` | `1.0` | No absent-time summary yet. |
| `summary_separates_avatar_caused_changes` | `1.0` | Phase: before-obligation-choice
Avatar-caused: avatar chose Wait offscreen at replay row 1; avatar did not choose the new obligation target
Resident-caused: Fay changed Milo's obligation while avatar absent; milo-offscreen-water-jars is open / offscreen-pending
Before choosing: Milo obligation is selectable before resolve/defer; schedule pending; debt outstanding |
| `summary_separates_resident_caused_changes` | `1.0` | Phase: before-obligation-choice
Avatar-caused: avatar chose Wait offscreen at replay row 1; avatar did not choose the new obligation target
Resident-caused: Fay changed Milo's obligation while avatar absent; milo-offscreen-water-jars is open / offscreen-pending
Before choosing: Milo obligation is selectable before resolve/defer; schedule pending; debt outstanding |
| `summary_marks_before_obligation_choice` | `1.0` | phase=before-obligation-choice text=Phase: before-obligation-choice
Avatar-caused: avatar chose Wait offscreen at replay row 1; avatar did not choose the new obligation target
Resident-caused: Fay changed Milo's obligation while avatar absent; milo-offscreen-water-jars is open / offscreen-pending
Before choosing: Milo obligation is selectable before resolve/defer; schedule pending; debt outstanding |
| `summary_links_to_visible_obligation` | `1.0` | summary obligation=milo-offscreen-water-jars list=milo-offscreen-water-jars: open / offscreen-pending / Milo offscreen obligation open from Fay: inspect leaking water jars |
| `summary_links_to_schedule_and_debt_status` | `1.0` | summary={'phase': 'before-obligation-choice', 'hasAvatar': True, 'hasResident': True, 'hasBeforeChoosing': True, 'obligationId': 'milo-offscreen-water-jars', 'actor': 'Fay', 'target': 'Milo', 'scheduleQueueStatus': 'pending', 'debtLedgerStatus': 'outstanding'} schedule=milo-offscreen-water-jars: pending / Milo schedule pending: offscreen obligation: inspect leaking water jars debt=milo-offscreen-water-jars: outstanding / debt 3 / Milo debt outstanding: 3 after offscreen-resident-action |
| `summary_survives_reload` | `1.0` | Phase: before-obligation-choice
Avatar-caused: avatar chose Wait offscreen at replay row 1; avatar did not choose the new obligation target
Resident-caused: Fay changed Milo's obligation while avatar absent; milo-offscreen-water-jars is open / offscreen-pending
Before choosing: Milo obligation is selectable before resolve/defer; schedule pending; debt outstanding |
| `replay_logs_absent_summary` | `1.0` | waitOffscreenReplayHasAbsentSummary=True summaryReloaded=True |
| `browser_console_clean` | `1.0` | console error count=0 |
| `experiment_index_includes_report_355` | `1.0` | scripts/run_experiments.py includes Report 355 module |
| `claim_boundary_preserved` | `1.0` | Browser-local absent-time summary separation over the maintained v61 shell only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, production persistence, hosted URL proof, complete 3D engine, finished gameplay, or metaphysical claim. |

## Honest interpretation

This improves readability of offscreen life: the player can see what they caused by waiting separately from what residents did while absent. It remains deterministic browser-local UI/state, not subjective experience, autonomous language, production persistence, hosted gameplay, or a complete 3D engine.

## Next gate

post-355: add one bounded player choice from the absent-time summary that selects whether to handle the avatar-caused thread or the resident-caused offscreen thread first, then prove the unchosen thread remains pending
