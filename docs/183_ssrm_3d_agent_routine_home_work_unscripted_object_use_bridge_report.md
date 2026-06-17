# Report 183: SSRM-3D Agent Routine, Home, Work Project, and Unscripted Object Use Bridge

## Purpose

Report 183 moves beyond scripted interaction and continuity ledgers. Report 182 showed that objects, promises, missed obligations, repair, and relationship continuity can persist across days. This report asks whether agents can choose routine actions from local state: home place, time phase, need pressure, work projects, object affordances, route access, frequency/flower coupling, rest recovery, and relationship carryover.

This is an autonomous routine substrate. It does not claim complete gameplay, subjective consciousness, moral patienthood, natural language emergence, or free will.

## Architecture

The bridge consumes the Report 182 continuity state:

```text
object / promise / relationship continuity
        |
        v
agent homes
        |
        v
routine clock phases
        |
        v
work projects
        |
        v
need-pressure scoring
        |
        v
object-affordance selection
        |
        v
route movement
        |
        v
frequency + flower coupling
        |
        v
rest recovery + social-continuity bias
        |
        v
browser-local autonomy replay
```

The default deterministic run uses:

- `5` simulated local days
- `6` routine ticks per day
- `3` agents
- `90` autonomy events
- persistent homes for `Ari`, `Fay`, and `Milo`
- one work project per agent
- scored action candidates instead of a fixed interaction script
- object use selected through routine policy and affordance match
- replay frames for every autonomy event

## Routine phases

Each simulated day uses six phases:

- `dawn_home`
- `morning_work`
- `midday_care`
- `afternoon_work`
- `dusk_social`
- `night_rest`

The phases bias action scores but do not fully determine actions. The selected action also depends on need levels, project progress, object affordance, route availability, and relationship carryover.

## Agent profiles

The integrated run assigns each agent a home and project:

- `Ari`: home `hearth_vale`, project `repair_clay_latch`, work object `clay_patch_kit`
- `Fay`: home `moss_hollow`, project `dry_moss_bedding`, work object `dry_cloak`
- `Milo`: home `stone_ridge`, project `ridge_warning_watch`, work object `signal_shell`

Agents can choose among actions such as:

- `home_tend`
- `rest`
- `care_drink`
- `social_check`
- `explore_safety`
- `work_project`

The selected action is the highest-scoring candidate under the integrated condition. Ablations remove the relevant mechanism and measure the resulting loss.

## Browser surface

The browser artifact is:

- `visualizations/ssrm_3d_agent_routine_home_work_unscripted_object_use_bridge.html`

It loads generated JS artifacts and lets the user:

- apply autonomy events one at a time
- watch agents move between places on the settlement graph
- inspect the chosen action and candidate count
- see needs mutate over time
- track work-project progress
- see object holders and routine-use counts change
- save, restore, and reset local browser routine state

The viewer is a deterministic local autonomy replay surface. It is not a complete game engine.

## Conditions

The integrated condition is:

- `integrated_agent_routine_home_work_unscripted_object_use`

Ablations remove one mechanism at a time:

- `no_home_binding`
- `no_routine_clock`
- `no_work_projects`
- `no_need_driven_selection`
- `no_unscripted_object_use`
- `no_object_persistence`
- `no_place_traversal`
- `no_frequency_flower_coupling`
- `no_social_continuity`
- `no_rest_recovery`
- `no_replay_timeline`
- `no_privacy_filter`

The critical ablations are home binding, routine clock, work projects, need-driven selection, unscripted object use, route traversal, and rest recovery. Agents do not yet feel alive if they only wait for scripted user events; they need ongoing local routines and object use driven by their own state.

## Metrics

The benchmark reports:

- `home_place_binding_rate`
- `routine_clock_progression_rate`
- `work_project_progress_rate`
- `need_driven_action_selection_rate`
- `unscripted_object_use_rate`
- `persistent_object_state_rate`
- `place_traversal_rate`
- `frequency_flower_coupling_rate`
- `social_continuity_modulation_rate`
- `rest_recovery_rate`
- `browser_autonomy_tick_rate`
- `replay_timeline_integrity_rate`
- `privacy_preservation_rate`
- `trace_integrity`
- `routine_autonomy_readiness`

Metric weights are normalized to sum to `1.0`.

## Results

The deterministic run produced:

| Metric | Value |
| --- | ---: |
| `module_verdict` | `pass` |
| `routine_autonomy_readiness` | `1.000000` |
| `simulated_days` | `5` |
| `autonomy_events` | `90` |
| `no_work_projects_loss` | `0.100889` |
| `no_need_driven_selection_loss` | `0.166667` |
| `no_unscripted_object_use_loss` | `0.204222` |

Interpretation:

- Homes are load-bearing.
- The routine clock is load-bearing.
- Work projects are load-bearing.
- Need-driven action selection is load-bearing.
- Object use is selected by policy, not by replaying the Report 181/182 user interaction script.
- Rest recovery and project work mutate agent state over time.
- The browser viewer can replay local autonomy ticks while preserving explicit claim boundaries.

## Moral and claim boundary

This report keeps the boundary explicit:

- no subjective-consciousness claim
- no moral-patienthood claim
- no complete-3D-world claim
- no complete-playable-world claim
- no natural-language-emergence claim
- unscripted policy is not a free-will claim
- need-driven choice is not subjective feeling
- agent routines are not moral patienthood
- private workspace is not exposed as a debug shortcut

## Artifacts

- `artifacts/ssrm_3d_agent_routine_home_work_unscripted_object_use_bridge_eval.csv`
- `artifacts/ssrm_3d_agent_routine_home_work_unscripted_object_use_bridge_verdict.csv`
- `artifacts/ssrm_3d_agent_routine_home_work_unscripted_object_use_bridge_results.json`
- `artifacts/ssrm_3d_agent_routine_home_work_unscripted_object_use_bridge_results.js`
- `artifacts/ssrm_3d_agent_routine_home_work_unscripted_object_use_bridge_trace.json`
- `artifacts/ssrm_3d_agent_routine_home_work_unscripted_object_use_bridge_trace.js`
- `artifacts/ssrm_3d_agent_routine_home_work_unscripted_object_use_bridge_state.json`
- `artifacts/ssrm_3d_agent_routine_home_work_unscripted_object_use_bridge_state.js`
- `visualizations/ssrm_3d_agent_routine_home_work_unscripted_object_use_bridge.html`

## Command

```bash
python3 -m experiments.ssrm_3d_agent_routine_home_work_unscripted_object_use_bridge
```

## Verdict

Report 183 supports a deterministic agent routine, persistent home, work project, and unscripted object-use seed over the Report 182 continuity layer. Agents now act over time from homes, routine phases, needs, work projects, object affordances, route movement, frequency/flower coupling, rest recovery, and relationship carryover.

The next gate is agent-local planning with interruptions, project dependencies, and emergent cooperation: routines should start producing multi-step local plans that can be interrupted, resumed, coordinated with other agents, and revised when objects or needs change.
