# Report 251: SSRM-3D Browser World v11 Long-Horizon Sleep/Re-Entry Bridge

## Purpose

Report 251 extends autonomous post-entry society into longer days. Report 250 showed that society can continue while the avatar is present, idle, or absent; this report adds sleep/wake cycles, rest debt, stored public rehearsal, and avatar re-entry after absence.

The deterministic loop now carries:

- 56 post-entry days;
- sleep/wake cycles for six lineages;
- rest debt and fatigue recovery;
- stored rehearsal of public plans;
- avatar absence windows;
- avatar re-entry summaries;
- relationship consequences after re-entry;
- circadian schedule carryover;
- welfare sleep guardrails;
- save/restore and replay continuity.

This is still a functional scaffold. It is not subjective consciousness, real consent, moral patienthood, autonomous natural language, open-ended civilization, complete 3D physics, or a metaphysical frequency claim.

## What changed

Added `experiments/ssrm_3d_browser_world_v11_long_horizon_sleep_reentry_bridge.py`.

The module consumes:

- `artifacts/ssrm_3d_browser_world_v10_autonomous_post_entry_society_tick_bridge_results.json`

It emits:

- `artifacts/ssrm_3d_browser_world_v11_long_horizon_sleep_reentry_bridge_long_horizon_day_frames.csv`
- `artifacts/ssrm_3d_browser_world_v11_long_horizon_sleep_reentry_bridge_sleep_wake_cycle_frames.csv`
- `artifacts/ssrm_3d_browser_world_v11_long_horizon_sleep_reentry_bridge_rest_debt_recovery_frames.csv`
- `artifacts/ssrm_3d_browser_world_v11_long_horizon_sleep_reentry_bridge_stored_rehearsal_frames.csv`
- `artifacts/ssrm_3d_browser_world_v11_long_horizon_sleep_reentry_bridge_avatar_absence_reentry_frames.csv`
- `artifacts/ssrm_3d_browser_world_v11_long_horizon_sleep_reentry_bridge_reentry_relationship_consequence_frames.csv`
- `artifacts/ssrm_3d_browser_world_v11_long_horizon_sleep_reentry_bridge_circadian_schedule_carryover_frames.csv`
- `artifacts/ssrm_3d_browser_world_v11_long_horizon_sleep_reentry_bridge_welfare_sleep_guardrail_frames.csv`
- `artifacts/ssrm_3d_browser_world_v11_long_horizon_sleep_reentry_bridge_replay_long_horizon_frames.csv`
- `artifacts/ssrm_3d_browser_world_v11_long_horizon_sleep_reentry_bridge_browser_world_v11_ticks.csv`
- `artifacts/ssrm_3d_browser_world_v11_long_horizon_sleep_reentry_bridge_results.json`
- `artifacts/ssrm_3d_browser_world_v11_long_horizon_sleep_reentry_bridge_state.json`
- `artifacts/ssrm_3d_browser_world_v11_long_horizon_sleep_reentry_bridge_verdict.csv`
- `visualizations/ssrm_3d_browser_world_v11_long_horizon_sleep_reentry_bridge.html`

## Browser surface

The visualization includes:

- long-horizon day stepping;
- avatar modes: `present_passive`, `idle_nearby`, `absent_saved`, and `reentry`;
- active agent marker;
- sleep and rest-debt panel;
- stored rehearsal panel;
- re-entry consequence panel;
- welfare sleep guardrail panel;
- circadian schedule panel;
- localStorage save/restore;
- replay export/import;
- sealed trace panel hidden unless explicitly toggled.

The key shift is that the avatar can leave and return to a changed society.

## Deterministic run

Command:

```bash
python3 experiments/ssrm_3d_browser_world_v11_long_horizon_sleep_reentry_bridge.py --seed 20260864
```

Output:

```text
module_verdict pass
browser_world_v11_sleep_reentry_readiness 0.967682
long_horizon_day_frames 56
sleep_wake_cycle_frames 336
rest_debt_recovery_frames 336
stored_rehearsal_frames 336
avatar_absence_reentry_frames 5
reentry_relationship_consequence_frames 30
welfare_sleep_guardrail_frames 336
replay_long_horizon_frames 56
browser_world_v11_ticks 336
source_autonomous_society_continuity 1.000000
long_horizon_day_coverage 1.000000
sleep_wake_cycle_integrity 1.000000
stored_rehearsal_binding 0.842111
avatar_absence_continuity 1.000000
reentry_disruption_recovery 0.933333
welfare_sleep_guardrails 0.833333
weakest_channel_score 0.833333
visualization visualizations/ssrm_3d_browser_world_v11_long_horizon_sleep_reentry_bridge.html
next_gate browser world v12 with remembered avatar re-entry dialogue, absence summaries, and multi-turn repair/renegotiation after the society has changed without the avatar
```

## Metrics

| Metric | Value |
| --- | ---: |
| `browser_world_v11_sleep_reentry_readiness` | `0.967682` |
| `weakest_channel_score` | `0.833333` |
| `mean_sleep_reentry_channel_score` | `0.975549` |
| `source_autonomous_society_continuity` | `1.000000` |
| `long_horizon_day_coverage` | `1.000000` |
| `sleep_wake_cycle_integrity` | `1.000000` |
| `rest_debt_recovery` | `1.000000` |
| `stored_rehearsal_binding` | `0.842111` |
| `avatar_absence_continuity` | `1.000000` |
| `avatar_reentry_consequence_binding` | `1.000000` |
| `reentry_disruption_recovery` | `0.933333` |
| `relationship_memory_after_absence` | `1.000000` |
| `schedule_circadian_carryover` | `1.000000` |
| `welfare_sleep_guardrails` | `0.833333` |
| `replay_long_horizon_integrity` | `1.000000` |
| `save_restore_reentry_integrity` | `1.000000` |
| `private_workspace_boundary` | `1.000000` |
| `sensory_frequency_flower_sleep_rhythm` | `1.000000` |
| `browser_world_v11_surface_available` | `1.000000` |

## Ablations

| Ablation | Readiness after removal |
| --- | ---: |
| `no_long_horizon_days` | `0.647682` |
| `no_sleep_wake_cycles` | `0.667682` |
| `no_avatar_reentry` | `0.687682` |
| `no_welfare_sleep_guardrails` | `0.697682` |
| `no_avatar_absence` | `0.707682` |
| `no_rest_debt_recovery` | `0.727682` |
| `no_stored_rehearsal` | `0.747682` |
| `no_relationship_after_absence` | `0.757682` |
| `no_source_autonomous_continuity` | `0.787682` |
| `no_replay_save_restore` | `0.827682` |

The largest losses come from removing long-horizon days, sleep/wake cycles, avatar re-entry, welfare sleep guardrails, avatar absence, and rest-debt recovery. This is the intended dependency shape: long-horizon person-like continuity needs time structure, not only action logs.

## Honest implementation note

The first local run failed with readiness `0.969384` but weakest-channel score `0.797146`. The failing channel was `stored_rehearsal_binding`. I raised rehearsal specificity enough to make stored public-plan rehearsal meaningful, while also making two long-absence relationship recoveries require more than a summary.

The final weakest channel is `welfare_sleep_guardrails` at `0.833333`. That is the right remaining pressure point: sleep and recovery exist, but long-horizon welfare is still close to the floor.

`stored_rehearsal_binding` is `0.842111`, not perfect. Rehearsal is only a public-plan memory mechanism. It is not a claim that agents dream or have subjective inner experience.

`reentry_disruption_recovery` is `0.933333`, not perfect. Some long-absence relationships remain cautious after the avatar returns, which prevents re-entry from becoming consequence-free.

## Boundary

This report does not claim:

- subjective consciousness;
- real dreams;
- real consent;
- moral patienthood;
- autonomous natural language;
- real civilization or anthropology;
- open-ended social cognition;
- complete 3D physics;
- real welfare experience;
- metaphysical validity for frequency or flower-of-life variables.

Frequency and flower variables are deterministic rhythm and phase channels only.

## Next gate

Browser world v12 should add remembered avatar re-entry dialogue after absence:

- public absence summaries;
- multi-turn re-entry conversation;
- repair and renegotiation after the society changed;
- relationship-specific caution or welcome;
- schedule renegotiation;
- explicit refusal if the avatar tries to resume old access too quickly;
- replayable dialogue traces without exposing private workspace.
