# Report 253: SSRM-3D Browser World v13 Live Re-Entry Choice Branch Bridge

## Purpose

Report 253 makes post-reentry typed choices branch future state.

Report 252 made avatar re-entry conversational. This report adds deterministic typed-choice branches where the avatar can accept a new rule, offer repair work, ask for a public summary, push for old access, or wait and observe. Each choice branches later schedules, access, trust, boundary pressure, welfare notes, and agent-initiated follow-up.

This is still a functional scaffold. It is not subjective consciousness, real consent, moral patienthood, autonomous natural language, open-ended planning, complete 3D physics, or a metaphysical frequency claim.

## What changed

Added `experiments/ssrm_3d_browser_world_v13_live_reentry_choice_branch_bridge.py`.

The module consumes:

- `artifacts/ssrm_3d_browser_world_v12_remembered_reentry_dialogue_bridge_results.json`

It emits:

- `artifacts/ssrm_3d_browser_world_v13_live_reentry_choice_branch_bridge_live_reentry_choice_frames.csv`
- `artifacts/ssrm_3d_browser_world_v13_live_reentry_choice_branch_bridge_branch_future_outcome_frames.csv`
- `artifacts/ssrm_3d_browser_world_v13_live_reentry_choice_branch_bridge_future_schedule_branch_frames.csv`
- `artifacts/ssrm_3d_browser_world_v13_live_reentry_choice_branch_bridge_access_trust_branch_frames.csv`
- `artifacts/ssrm_3d_browser_world_v13_live_reentry_choice_branch_bridge_agent_initiated_followup_frames.csv`
- `artifacts/ssrm_3d_browser_world_v13_live_reentry_choice_branch_bridge_branch_replay_comparison_frames.csv`
- `artifacts/ssrm_3d_browser_world_v13_live_reentry_choice_branch_bridge_browser_world_v13_ticks.csv`
- `artifacts/ssrm_3d_browser_world_v13_live_reentry_choice_branch_bridge_results.json`
- `artifacts/ssrm_3d_browser_world_v13_live_reentry_choice_branch_bridge_state.json`
- `artifacts/ssrm_3d_browser_world_v13_live_reentry_choice_branch_bridge_verdict.csv`
- `visualizations/ssrm_3d_browser_world_v13_live_reentry_choice_branch_bridge.html`

## Browser surface

The visualization includes:

- deterministic post-reentry choice playback;
- a local choice selector;
- branch outcome panel;
- access/trust/boundary panel;
- agent-initiated follow-up panel;
- branch replay comparison panel;
- localStorage save/restore;
- replay export/import;
- sealed trace panel hidden unless explicitly toggled.

The key shift is that dialogue choices now affect future state, not just the current exchange.

## Deterministic run

Command:

```bash
python3 experiments/ssrm_3d_browser_world_v13_live_reentry_choice_branch_bridge.py --seed 20260866
```

Output:

```text
module_verdict pass
browser_world_v13_live_choice_branch_readiness 0.982054
live_reentry_choice_frames 150
branch_future_outcome_frames 450
future_schedule_branch_frames 150
access_trust_branch_frames 150
agent_initiated_followup_frames 132
branch_replay_comparison_frames 150
browser_world_v13_ticks 150
source_reentry_dialogue_continuity 1.000000
live_choice_surface 1.000000
typed_choice_branch_confidence 0.864019
future_schedule_branching 1.000000
access_trust_branching 1.000000
agent_initiated_followup 0.956522
private_workspace_boundary 1.000000
weakest_channel_score 0.864019
visualization visualizations/ssrm_3d_browser_world_v13_live_reentry_choice_branch_bridge.html
next_gate browser world v14 with actual in-browser branch state mutation, user-selected future branches, and persistent agent follow-up after reload
```

## Metrics

| Metric | Value |
| --- | ---: |
| `browser_world_v13_live_choice_branch_readiness` | `0.982054` |
| `weakest_channel_score` | `0.864019` |
| `mean_branch_choice_channel_score` | `0.986195` |
| `source_reentry_dialogue_continuity` | `1.000000` |
| `live_choice_surface` | `1.000000` |
| `typed_choice_branch_confidence` | `0.864019` |
| `future_schedule_branching` | `1.000000` |
| `access_trust_branching` | `1.000000` |
| `bounded_refusal_under_pressure` | `1.000000` |
| `agent_initiated_followup` | `0.956522` |
| `multi_day_branch_persistence` | `1.000000` |
| `replay_branch_integrity` | `1.000000` |
| `save_restore_branch_integrity` | `1.000000` |
| `private_workspace_boundary` | `1.000000` |
| `sensory_frequency_flower_branch_rhythm` | `1.000000` |
| `browser_world_v13_surface_available` | `1.000000` |

## Ablations

| Ablation | Readiness after removal |
| --- | ---: |
| `no_live_choices` | `0.652054` |
| `no_access_trust_branches` | `0.692054` |
| `no_future_schedule_branches` | `0.712054` |
| `no_agent_followup` | `0.732054` |
| `no_typed_choice_parser` | `0.742054` |
| `no_multi_day_persistence` | `0.752054` |
| `no_bounded_refusal` | `0.762054` |
| `no_source_reentry_dialogue` | `0.812054` |
| `no_replay_branch_compare` | `0.832054` |
| `no_frequency_flower_branch_rhythm` | `0.922054` |

The strongest losses come from removing live choices, access/trust branches, future schedules, agent follow-up, typed choice parsing, and multi-day persistence. That is the intended dependency shape: post-reentry dialogue should create branchable future commitments.

## Honest implementation note

The first local run failed with readiness `0.970054` but weakest-channel score `0.800000`. The failing channel was `private_workspace_boundary`. Too many public choice panels repeated wording about sealed work. I changed the public wording to say `public task` instead. The private trace was never exposed, but the language was still too close to the privacy boundary.

The final weakest channel is `typed_choice_branch_confidence` at `0.864019`. That is the correct remaining floor because these are deterministic local parser/template branches, not open-ended language understanding.

`agent_initiated_followup` is `0.956522`, not perfect. Some summary-only branches do not create follow-up yet, so later-day agent initiative remains a real pressure point.

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

Browser world v14 should move from generated branch comparisons to actual in-browser branch state mutation:

- user-selected future branches;
- persistent branch state after reload;
- agent follow-up after reload;
- branch comparison export;
- schedule/access/trust updates driven by selected branch;
- privacy-safe replay.
