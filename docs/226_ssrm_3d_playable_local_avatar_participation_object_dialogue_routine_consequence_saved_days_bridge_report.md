# Report 226: SSRM-3D Playable Local Avatar Participation, Object Manipulation, Dialogue Choice, Routine Disruption, and Saved-Day Consequence Bridge

## Status

Pass.

Report 226 moves the playable society slice from passive observation into avatar participation. The avatar can join cooperative tasks, manipulate objects, choose bounded dialogue responses, disrupt routines, offer repairs, and carry public consequences across saved days.

This is deterministic functional scaffolding. It is not a consciousness claim, not real consent, not subjective suffering, not moral patienthood, not LLM dialogue, not open-ended social cognition, and not a complete game engine.

## Purpose

Report 225 created a local autonomous society slice with agent-agent dialogue, cooperative tasks, conflict repair, group routines, and body-language markers. Report 226 tests whether the avatar can enter that slice and make changes that persist.

The tested loop is:

```text
avatar action
-> consent or boundary gate
-> object/dialogue/routine consequence
-> visible agent response
-> sensory feedback packet
-> relationship or debt memory write
-> saved-day consequence
-> browser restore/replay
```

The central design requirement is that avatar help should not be free magic. Touching objects, pushing routines, helping tasks, asking questions, and repairing overreach must alter trust, access, debt, object state, and future responses.

## Implementation

The deterministic module is:

```text
experiments/ssrm_3d_playable_local_avatar_participation_object_dialogue_routine_consequence_saved_days_bridge.py
```

The browser visualization is:

```text
visualizations/ssrm_3d_playable_local_avatar_participation_object_dialogue_routine_consequence_saved_days_bridge.html
```

Generated artifacts:

```text
artifacts/ssrm_3d_playable_local_avatar_participation_object_dialogue_routine_consequence_saved_days_bridge_agents.csv
artifacts/ssrm_3d_playable_local_avatar_participation_object_dialogue_routine_consequence_saved_days_bridge_avatar_actions.csv
artifacts/ssrm_3d_playable_local_avatar_participation_object_dialogue_routine_consequence_saved_days_bridge_object_manipulations.csv
artifacts/ssrm_3d_playable_local_avatar_participation_object_dialogue_routine_consequence_saved_days_bridge_dialogue_choices.csv
artifacts/ssrm_3d_playable_local_avatar_participation_object_dialogue_routine_consequence_saved_days_bridge_routine_disruptions.csv
artifacts/ssrm_3d_playable_local_avatar_participation_object_dialogue_routine_consequence_saved_days_bridge_saved_day_consequences.csv
artifacts/ssrm_3d_playable_local_avatar_participation_object_dialogue_routine_consequence_saved_days_bridge_avatar_play_ticks.csv
artifacts/ssrm_3d_playable_local_avatar_participation_object_dialogue_routine_consequence_saved_days_bridge_results.json
artifacts/ssrm_3d_playable_local_avatar_participation_object_dialogue_routine_consequence_saved_days_bridge_state.json
artifacts/ssrm_3d_playable_local_avatar_participation_object_dialogue_routine_consequence_saved_days_bridge_verdict.csv
```

## Scenario coverage

The generated slice contains:

| Element | Count |
| --- | ---: |
| Agents | 5 |
| Avatar actions | 12 |
| Object manipulations | 6 |
| Dialogue choices | 5 |
| Routine disruptions | 3 |
| Saved-day consequences | 6 |
| Avatar play ticks | 18 |

The avatar can:

- hold a chalk cord outside Roka's learner path
- move loose reeds without taking the tied learner bundle
- ask Roka what should not be touched
- try to push through the midday water pause and be refused
- repair that overreach by carrying cups
- add an object-only digest knot with Noro and Nian's approval
- carry a shade beam while preserving visible debt
- overreach toward the tied bundle and lose access
- repair partially by stepping back to the blue stone
- join the evening knot routine from the edge of the circle
- ask Noro which public debts remain

## New channels

### Avatar participation

Avatar actions now have action type, target, chosen option, consent gate, accepted/refused state, effort cost, trust delta, task delta, routine delta, consequence, sensory feedback, frequency, and flower node.

This makes the avatar part of the local society rather than an outside debugger.

### Object manipulation

Object manipulation is not only pickup state. It records holder before/after, operation, ownership gate, material delta, wear delta, debt delta, visible world change, agent response, reversibility, and whether the consequence saves.

The tied learner bundle is the key negative case:

```text
operation: attempt_pickup
ownership_gate: refused child-work boundary
visible_world_change: bundle does not move
agent_response: Roka backs to blue stone and says not today
```

A playable world needs this kind of refusal. Objects cannot all be free props.

### Dialogue choices

Dialogue choices are bounded, not LLM-generated. Each choice has options, a selected option, refusal availability, agent response, relationship update, and memory write.

Example:

```text
Avatar: What do you want me to know before I help?
Roka: Loose reeds are okay. The tied bundle is mine today.
```

This changes future access and relationship memory.

### Routine disruption

Routine disruption tests whether the avatar can stress the society without destroying it. The avatar asks to keep lifting during the water pause, reaches toward the tied bundle during rain hurry, and asks to enter the evening debt circle.

The system responds with refusal, alternative participation, delayed access, and edge-of-circle participation instead of total obedience.

### Saved-day consequences

Saved-day consequences carry public memory forward:

| Consequence | Day | Effect |
| --- | ---: | --- |
| Roka trust | 2 | Loose-reed help is permitted sooner, tied bundle remains closed |
| Water repair | 2 | Urgency penalty softens after carrying cups |
| Privacy access | 3 | Archive threshold opens by one public step |
| Roka boundary | 3 | Tied bundle access remains denied after overreach |
| Shade debt | 3 | One beam is installed, public timber debt remains |
| Ledger reputation | 4 | Avatar reputation becomes accountable but boundary-tested |

The browser replay has action stepping, run/pause, save, and restore through local storage.

## Metrics

Run command:

```bash
python3 experiments/ssrm_3d_playable_local_avatar_participation_object_dialogue_routine_consequence_saved_days_bridge.py --seed 20260839
```

Run output:

```text
module_verdict pass
playable_avatar_participation_readiness 0.932300
agents 5
avatar_actions 12
object_manipulations 6
dialogue_choices 5
routine_disruptions 3
saved_day_consequences 6
avatar_play_ticks 18
avatar_action_coverage 1.000000
object_manipulation_consequence_rate 1.000000
dialogue_choice_branching 1.000000
routine_disruption_recovery 0.793333
saved_day_consequence_integrity 1.000000
cooperative_participation_completion 0.833333
weakest_channel_score 0.666667
visualization visualizations/ssrm_3d_playable_local_avatar_participation_object_dialogue_routine_consequence_saved_days_bridge.html
next_gate playable local 3D multi-day avatar life with free-move task participation, richer object affordances, agent-initiated requests, and persistent reputation UI
```

Metric table:

| Metric | Score |
| --- | ---: |
| playable_avatar_participation_readiness | 0.932300 |
| mean_avatar_play_channel_score | 0.939167 |
| weakest_channel_score | 0.666667 |
| avatar_action_coverage | 1.000000 |
| consent_gate_integrity | 1.000000 |
| object_manipulation_consequence_rate | 1.000000 |
| object_permission_enforcement | 0.666667 |
| dialogue_choice_branching | 1.000000 |
| agent_response_specificity | 1.000000 |
| routine_disruption_recovery | 0.793333 |
| lingering_debt_control | 0.916667 |
| saved_day_consequence_integrity | 1.000000 |
| cross_day_relationship_persistence | 0.816667 |
| sensory_feedback_binding | 1.000000 |
| cooperative_participation_completion | 0.833333 |
| avatar_overreach_penalty_binding | 1.000000 |
| private_workspace_boundary_score | 1.000000 |
| frequency_flower_play_rhythm | 1.000000 |
| browser_playable_avatar_loop_available | 1.000000 |

## Ablations

| Ablation | Readiness |
| --- | ---: |
| no_browser_avatar_loop | 0.592300 |
| no_avatar_actions | 0.602300 |
| no_saved_day_consequences | 0.622300 |
| no_object_manipulation | 0.642300 |
| no_dialogue_choice | 0.662300 |
| no_consent_gates | 0.692300 |
| no_routine_disruption | 0.712300 |
| no_sensory_feedback | 0.772300 |
| no_frequency_flower_rhythm | 0.852300 |

The largest drops come from removing the browser avatar loop, avatar actions, saved-day consequences, object manipulation, dialogue choices, and consent gates. This is the right dependency shape for a playable society: the avatar must be able to act, and those actions must persist.

## Honest interpretation

This report is a strong bridge, but it is not the final system.

The weakest channel is object permission enforcement at `0.666667`. Some object operations still use broad consent labels rather than a richer per-agent/per-object permission lattice.

Routine disruption recovery is `0.793333`. Routine stress is recoverable, but the rain/bundle event still leaves meaningful lingering debt.

Cooperative participation completion is `0.833333`. The avatar can help, but not every action completes cleanly, and some participation remains conditional or partial.

Cross-day relationship persistence is `0.816667`. Consequences persist across days, but this is still structured saved state rather than an open-ended life history.

## Boundary

This report does not claim:

- subjective consciousness
- real consent
- subjective suffering
- moral patienthood
- LLM dialogue
- open-ended social cognition
- full physics
- complete object economy
- complete 3D gameplay
- metaphysical significance from frequencies or flower nodes

Frequencies and flower nodes are timing and phase scaffolds only.

## Next gate

The next gate is playable local 3D multi-day avatar life with free-move task participation, richer object affordances, agent-initiated requests, and persistent reputation UI.
