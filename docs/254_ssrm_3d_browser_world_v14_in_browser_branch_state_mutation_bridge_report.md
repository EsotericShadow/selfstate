# Report 254: SSRM-3D Browser World v14 In-Browser Branch State Mutation Bridge

## Purpose

Report 254 moves from generated branch comparison to actual browser-local branch mutation.

Report 253 generated future branch comparisons for post-reentry choices. This report adds a browser artifact where the selected branch mutates local JSON state, persists through localStorage, restores after a reload-like probe, produces agent follow-up from restored state, supports rollback, and exports replay.

This is still a functional scaffold. It is not subjective consciousness, real consent, moral patienthood, autonomous natural language, open-ended planning, complete 3D physics, or a metaphysical frequency claim.

## What changed

Added `experiments/ssrm_3d_browser_world_v14_in_browser_branch_state_mutation_bridge.py`.

The module consumes:

- `artifacts/ssrm_3d_browser_world_v13_live_reentry_choice_branch_bridge_results.json`

It emits:

- `artifacts/ssrm_3d_browser_world_v14_in_browser_branch_state_mutation_bridge_browser_branch_selection_frames.csv`
- `artifacts/ssrm_3d_browser_world_v14_in_browser_branch_state_mutation_bridge_in_browser_mutable_state_frames.csv`
- `artifacts/ssrm_3d_browser_world_v14_in_browser_branch_state_mutation_bridge_reload_restore_probe_frames.csv`
- `artifacts/ssrm_3d_browser_world_v14_in_browser_branch_state_mutation_bridge_agent_followup_after_reload_frames.csv`
- `artifacts/ssrm_3d_browser_world_v14_in_browser_branch_state_mutation_bridge_schedule_access_trust_mutation_frames.csv`
- `artifacts/ssrm_3d_browser_world_v14_in_browser_branch_state_mutation_bridge_rollback_branch_state_frames.csv`
- `artifacts/ssrm_3d_browser_world_v14_in_browser_branch_state_mutation_bridge_branch_replay_export_frames.csv`
- `artifacts/ssrm_3d_browser_world_v14_in_browser_branch_state_mutation_bridge_browser_world_v14_ticks.csv`
- `artifacts/ssrm_3d_browser_world_v14_in_browser_branch_state_mutation_bridge_results.json`
- `artifacts/ssrm_3d_browser_world_v14_in_browser_branch_state_mutation_bridge_state.json`
- `artifacts/ssrm_3d_browser_world_v14_in_browser_branch_state_mutation_bridge_verdict.csv`
- `visualizations/ssrm_3d_browser_world_v14_in_browser_branch_state_mutation_bridge.html`

## Browser surface

The visualization includes:

- branch selector;
- `apply branch` mutation button;
- localStorage save/restore;
- rollback to preselection state;
- agent follow-up derived from restored branch state;
- replay export/import;
- mutable state panel;
- restore probe panel;
- rollback panel;
- sealed trace panel hidden unless explicitly toggled.

The key shift is that branch state is now mutated inside the browser page rather than only represented by precomputed branch comparison rows.

## Deterministic run

Command:

```bash
python3 experiments/ssrm_3d_browser_world_v14_in_browser_branch_state_mutation_bridge.py --seed 20260867
```

Output:

```text
module_verdict pass
browser_world_v14_in_browser_mutation_readiness 0.989557
browser_branch_selection_frames 150
in_browser_mutable_state_frames 150
reload_restore_probe_frames 150
agent_followup_after_reload_frames 142
schedule_access_trust_mutation_frames 150
rollback_branch_state_frames 150
branch_replay_export_frames 150
browser_world_v14_ticks 150
source_live_choice_branch_continuity 1.000000
in_browser_mutation_surface 1.000000
user_selected_branch_state_mutation 1.000000
local_storage_persistence_integrity 1.000000
reload_restore_branch_survival 1.000000
agent_followup_after_reload 1.000000
typed_selection_confidence 0.869464
weakest_channel_score 0.869464
visualization visualizations/ssrm_3d_browser_world_v14_in_browser_branch_state_mutation_bridge.html
next_gate browser world v15 with multi-agent concurrent branch consequences, branch conflicts, and agent-initiated follow-up arbitration after reload
```

## Metrics

| Metric | Value |
| --- | ---: |
| `browser_world_v14_in_browser_mutation_readiness` | `0.989557` |
| `weakest_channel_score` | `0.869464` |
| `mean_mutation_channel_score` | `0.990676` |
| `source_live_choice_branch_continuity` | `1.000000` |
| `in_browser_mutation_surface` | `1.000000` |
| `user_selected_branch_state_mutation` | `1.000000` |
| `local_storage_persistence_integrity` | `1.000000` |
| `reload_restore_branch_survival` | `1.000000` |
| `agent_followup_after_reload` | `1.000000` |
| `schedule_access_trust_state_mutation` | `1.000000` |
| `rollback_branch_integrity` | `1.000000` |
| `typed_selection_confidence` | `0.869464` |
| `replay_export_integrity` | `1.000000` |
| `save_restore_branch_integrity` | `1.000000` |
| `privacy_safe_mutation` | `1.000000` |
| `sensory_frequency_flower_mutation_rhythm` | `1.000000` |
| `browser_world_v14_surface_available` | `1.000000` |

## Ablations

| Ablation | Readiness after removal |
| --- | ---: |
| `no_in_browser_mutation` | `0.649557` |
| `no_user_selected_branch_state` | `0.679557` |
| `no_local_storage_persistence` | `0.699557` |
| `no_reload_restore` | `0.729557` |
| `no_schedule_access_trust_mutation` | `0.739557` |
| `no_agent_followup_after_reload` | `0.749557` |
| `no_source_live_choice_branch` | `0.829557` |
| `no_rollback` | `0.829557` |
| `no_replay_export` | `0.849557` |
| `no_frequency_flower_mutation_rhythm` | `0.929557` |

The largest losses come from removing in-browser mutation, selected branch state, localStorage persistence, reload restore, schedule/access/trust mutation, and follow-up after reload. That is the intended dependency shape: browser interaction now has persistent local consequences.

## Honest limitations

The weakest channel is `typed_selection_confidence` at `0.869464`. Selection is still deterministic parser/template handling, not open-ended language understanding.

The browser mutates local JSON state. That is stronger than generated branch comparison, but still not a full simulation engine. Follow-up is generated from restored deterministic branch state, not open-ended agency.

This report does not validate browser runtime behavior with a browser automation pass. The artifact contains the mutation, save, restore, rollback, and replay logic; the deterministic module verifies the generated state frames and integrity hashes.

## Boundary

This report does not claim:

- subjective consciousness;
- real consent;
- moral patienthood;
- autonomous natural language;
- real civilization or anthropology;
- open-ended planning;
- complete 3D physics;
- real welfare experience;
- metaphysical validity for frequency or flower-of-life variables.

Frequency and flower variables are deterministic rhythm and phase channels only.

## Next gate

Browser world v15 should add multi-agent concurrent branch consequences:

- multiple selected branches active at once;
- conflicts between branch consequences;
- agent-initiated follow-up arbitration after reload;
- schedule/access/trust conflicts across agents;
- replayable conflict resolution;
- rollback for one branch without deleting unrelated branches.
