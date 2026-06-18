# Report 301: SSRM-3D Browser World v61 Vertical Slice App-Shell Hardening

## Purpose

Report 301 moves the post-300 work away from adding more simulation organs and toward hardening the first playable vertical slice into a maintained app shell. It separates the browser artifact into `index.html`, `styles.css`, `app.js`, `playtest_tasks.json`, `qa_manifest.json`, and an operator `README.md` under `visualizations/ssrm_3d_browser_world_v61_vertical_slice_app_shell/`.

This is still deterministic browser-local prototype work. It does not claim subjective consciousness, autonomous natural language, real consent, moral patienthood, production persistence, finished gameplay, a complete 3D engine, or metaphysical frequency.

## Deterministic run

- Command: `python3 -m experiments.ssrm_3d_browser_world_v61_vertical_slice_app_shell_hardening`
- Seed: `20270616`
- Verdict: `pass`
- Readiness: `0.947050`
- Mean channel score: `0.983500`
- Weakest channel: `not_runtime_browser_verified_yet` at `0.862000`

## Evidence counts

| Evidence stream | Count |
| --- | ---: |
| App shell files | 6 |
| Playtest tasks | 10 |
| Mandatory playtest tasks | 9 |
| State boundary rules | 9 |
| Direct QA hooks | 6 |
| Hardening criteria | 8 |
| Generated artifact files | 6 |
| App JavaScript bytes | 13708 |
| App CSS bytes | 2672 |
| App HTML bytes | 3577 |

## Correctness channels

| Channel | Score |
| --- | ---: |
| `source_v60_continuity` | `1.000000` |
| `separate_app_shell_assets` | `1.000000` |
| `playtest_tasks_present` | `1.000000` |
| `direct_qa_hooks_present` | `1.000000` |
| `state_boundaries_documented` | `1.000000` |
| `reduced_artifact_sprawl` | `0.940000` |
| `private_workspace_boundary` | `1.000000` |
| `not_runtime_browser_verified_yet` | `0.862000` |
| `app_shell_file_coverage` | `1.000000` |
| `mandatory_playtest_coverage` | `1.000000` |
| `qa_hook_browser_executable_coverage` | `1.000000` |
| `state_boundary_private_workspace_hidden` | `1.000000` |


## What changed after Report 300

Report 301 does not add weather, lore, rituals, or another agent subsystem. It hardens the vertical slice itself:

1. The playable shell is split into stable files instead of one monolithic generated HTML page.
2. Core state ownership is documented in a QA manifest.
3. User-facing playtest tasks are exported as JSON and CSV.
4. Browser-callable QA hooks are built into `app.js`.
5. Replay, save/restore, state-boundary audit, and playtest checklist hooks write deterministic localStorage results.
6. Replay export is prepared locally in a QA-friendly storage key before any optional download link is used.
7. A `?reset=1` URL path clears app-shell localStorage for repeatable browser QA.
8. The no-LLM/no-consciousness/no-finished-product boundary remains visible in the UI.
9. Generated artifact count is intentionally small compared with the prior large row bundles.

## Honest limitation

The weakest channel is `not_runtime_browser_verified_yet` at `0.862000`. That cap is intentional. Report 301 creates the hooks for direct browser QA, but the browser runtime pass itself is the next gate. It would be dishonest to claim the shell is runtime-verified in-browser from this deterministic generation alone.

## Artifacts

- `experiments/ssrm_3d_browser_world_v61_vertical_slice_app_shell_hardening.py`
- `artifacts/ssrm_3d_browser_world_v61_vertical_slice_app_shell_hardening_results.json`
- `artifacts/ssrm_3d_browser_world_v61_vertical_slice_app_shell_hardening_state.json`
- `artifacts/ssrm_3d_browser_world_v61_vertical_slice_app_shell_hardening_summary.csv`
- `artifacts/ssrm_3d_browser_world_v61_vertical_slice_app_shell_hardening_verdict.csv`
- `artifacts/ssrm_3d_browser_world_v61_vertical_slice_app_shell_hardening_playtest_tasks.csv`
- `artifacts/ssrm_3d_browser_world_v61_vertical_slice_app_shell_hardening_qa_manifest.csv`
- `visualizations/ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html`
- `visualizations/ssrm_3d_browser_world_v61_vertical_slice_app_shell/styles.css`
- `visualizations/ssrm_3d_browser_world_v61_vertical_slice_app_shell/app.js`
- `visualizations/ssrm_3d_browser_world_v61_vertical_slice_app_shell/playtest_tasks.json`
- `visualizations/ssrm_3d_browser_world_v61_vertical_slice_app_shell/qa_manifest.json`
- `visualizations/ssrm_3d_browser_world_v61_vertical_slice_app_shell/README.md`

## Boundary

Deterministic browser-local hardened vertical-slice app shell only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, production persistence, finished gameplay, complete 3D engine, or metaphysical frequency claim.

## Next gate

post-301 direct browser QA pass: open the maintained app shell, execute the built-in playtest checklist, inspect saved localStorage state, export replay, and fix runtime issues before adding any new simulation organs.
