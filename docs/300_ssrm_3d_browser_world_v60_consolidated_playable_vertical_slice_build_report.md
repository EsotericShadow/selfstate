# Report 300: SSRM-3D Browser World v60 Consolidated Playable Vertical Slice Build

## Purpose

Report 300 is the first consolidated playable vertical-slice build. It stops treating arrival, movement, conversation, schedules, debts, offscreen life, memory, consequences, save/restore, and audit replay as separate report organs and puts them into one browser-local artifact.

This is the first point in the sequence where the result is meaningfully closer to something a person can open and try as a tiny living-world prototype. It remains deterministic and browser-local, and it does not claim subjective consciousness, autonomous natural language, moral patienthood, production persistence, complete gameplay, or a complete 3D engine.

## Deterministic run

- Command: `python3 -m experiments.ssrm_3d_browser_world_v60_consolidated_playable_vertical_slice_build`
- Seed: `20270602`
- Verdict: `pass`
- Readiness: `0.949754`
- Mean channel score: `0.989077`
- Weakest channel: `first_vertical_slice_not_outsider_ready_product` at `0.858000`

## Evidence counts

| Evidence stream | Rows |
| --- | ---: |
| Vertical slice session frames | 5400 |
| Playable arrival/movement frames | 5400 |
| Bounded conversation frames | 5400 |
| Schedule/debt/memory frames | 5400 |
| Offscreen return frames | 5400 |
| Visible consequence frames | 5400 |
| Save/restore/audit/replay frames | 5400 |
| Usable interface frames | 5400 |
| Browser ticks | 5400 |
| Browser buttons | 180 |
| Core loop count | 8 |
| Resident count | 6 |

## Correctness channels

| Channel | Score |
| --- | ---: |
| `source_v59_continuity` | `1.000000` |
| `single_artifact_vertical_slice` | `1.000000` |
| `arrival_movement_playability` | `1.000000` |
| `bounded_conversation_schedule_memory_binding` | `1.000000` |
| `schedule_debt_memory_continuity` | `1.000000` |
| `offscreen_life_visible_on_return` | `1.000000` |
| `visible_consequence_recovery_loop` | `1.000000` |
| `save_restore_audit_replay_pipeline` | `1.000000` |
| `usable_interface_surface` | `1.000000` |
| `private_workspace_boundary_preserved` | `1.000000` |
| `browser_control_surface` | `1.000000` |
| `no_llm_no_consciousness_boundary` | `1.000000` |
| `first_vertical_slice_not_outsider_ready_product` | `0.858000` |


## What makes this different from another bridge

Report 300 creates one browser artifact where the user can:

1. Enter the world.
2. Move the avatar by buttons or canvas click.
3. Select and talk to residents through bounded phrase keys.
4. See resident schedules, debts, memory notes, trust, and project progress.
5. Affect trust and debt through help, borrowing, returning, interruption, waiting, and repair.
6. Wait offscreen while residents keep progressing without avatar input.
7. Return and see visible consequences.
8. Save and restore the local world state.
9. Toggle audit/replay and export the replay trace.
10. See the no-LLM/no-consciousness/no-finished-product boundary in the UI.

## Honest limitation

The weakest channel is `first_vertical_slice_not_outsider_ready_product` at `0.858000`. That cap is intentional. This is the first consolidated playable vertical slice, not an outsider-ready product. The next work should harden this one artifact with direct browser QA, cleaner state/assets, playtest tasks, and less generated-report sprawl before adding new organs.

## Artifacts

- `experiments/ssrm_3d_browser_world_v60_consolidated_playable_vertical_slice_build.py`
- `artifacts/ssrm_3d_browser_world_v60_consolidated_playable_vertical_slice_build_results.json`
- `artifacts/ssrm_3d_browser_world_v60_consolidated_playable_vertical_slice_build_state.json`
- `artifacts/ssrm_3d_browser_world_v60_consolidated_playable_vertical_slice_build_summary.csv`
- `artifacts/ssrm_3d_browser_world_v60_consolidated_playable_vertical_slice_build_verdict.csv`
- `artifacts/ssrm_3d_browser_world_v60_consolidated_playable_vertical_slice_build_vertical_slice_session_frames.csv`
- `artifacts/ssrm_3d_browser_world_v60_consolidated_playable_vertical_slice_build_playable_arrival_movement_frames.csv`
- `artifacts/ssrm_3d_browser_world_v60_consolidated_playable_vertical_slice_build_bounded_conversation_frames.csv`
- `artifacts/ssrm_3d_browser_world_v60_consolidated_playable_vertical_slice_build_schedule_debt_memory_frames.csv`
- `artifacts/ssrm_3d_browser_world_v60_consolidated_playable_vertical_slice_build_offscreen_return_frames.csv`
- `artifacts/ssrm_3d_browser_world_v60_consolidated_playable_vertical_slice_build_visible_consequence_frames.csv`
- `artifacts/ssrm_3d_browser_world_v60_consolidated_playable_vertical_slice_build_save_restore_audit_replay_frames.csv`
- `artifacts/ssrm_3d_browser_world_v60_consolidated_playable_vertical_slice_build_usable_interface_frames.csv`
- `artifacts/ssrm_3d_browser_world_v60_consolidated_playable_vertical_slice_build_browser_ticks.csv`
- `visualizations/ssrm_3d_browser_world_v60_consolidated_playable_vertical_slice_build.html`

## Boundary

Deterministic browser-local consolidated playable vertical-slice prototype only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, production persistence, finished gameplay, complete 3D engine, or metaphysical frequency claim.

## Next gate

post-300 hardening: convert the single HTML vertical slice into a maintained app shell with fewer generated report files, direct browser QA, cleaner asset/state boundaries, and user-facing playtest tasks before adding new simulation organs.
