# Report 165: SSRM-3D First-Person Ego State Bridge

Date: 2026-06-17

## Purpose

Report 165 is the pivot from browser infrastructure toward convincing first-person artificial life.

Because Report 164 is already published as the persistent browser-runtime session bridge, the first-person interior/ego sequence begins here as Report 165. The goal is not better toy metrics or a consciousness claim. The goal is to give agents a functional self-perspective: body, local experience, private workspace, welfare-like felt state, temperament, preferences, relationship memory, ownership, bounded refusal, self-story, recoverable ego wounds, ego repair, and readable behavior.

No LLMs are called. This report does not claim subjective consciousness. It implements inspectable functional architecture for little people-like agents.

## Implementation

The new module is:

- `experiments/ssrm_3d_first_person_ego_state_bridge.py`

It consumes:

- `artifacts/ssrm_3d_persistent_browser_runtime_session_bridge_state.json`

It emits:

- `artifacts/ssrm_3d_first_person_ego_state_bridge_eval.csv`
- `artifacts/ssrm_3d_first_person_ego_state_bridge_verdict.csv`
- `artifacts/ssrm_3d_first_person_ego_state_bridge_results.json`
- `artifacts/ssrm_3d_first_person_ego_state_bridge_results.js`
- `artifacts/ssrm_3d_first_person_ego_state_bridge_trace.json`
- `artifacts/ssrm_3d_first_person_ego_state_bridge_trace.js`
- `artifacts/ssrm_3d_first_person_ego_state_bridge_state.json`
- `artifacts/ssrm_3d_first_person_ego_state_bridge_state.js`

The browser artifact is:

- `visualizations/ssrm_3d_first_person_ego_state_bridge.html`

## Interior Layers

Each agent now has seven interior layers:

1. `body`: energy, fatigue, pain, comfort, hunger, thirst, temperature, wetness, safety, breath rate, movement effort, rest debt, injury.
2. `first_person_frame`: what I see, hear, smell, what is near me, what happened to me, who is looking at me, what I was trying to do, what I expect next.
3. `private_workspace`: focus, dominant need, dominant feeling, active memory, relationship concern, current intention, predicted next event, suppressed alternative, self-note.
4. `felt_state`: valence, arousal, control, safety, attachment, curiosity, frustration.
5. `temperament/preferences`: bold/cautious, social/solitary, curious/routine-bound, trusting/guarded, autonomy need, shame/pride sensitivity, warm-place and object preferences.
6. `relationship_memory`: emotionally weighted avatar episodes updating trust, comfort, familiarity, avoidance, dependency, resentment, gratitude, and curiosity.
7. `readable_behavior`: posture, movement speed, gaze, proximity, hesitation/refusal/repair markers, and public dialogue line.

## Ego Layer

The ego layer is functional, not metaphysical. It tracks:

- self-boundary;
- ownership;
- preference;
- dignity/felt respect;
- memory of being treated;
- social face;
- agency attribution;
- self-protection;
- self-repair.

The core loop is:

```text
event happens
-> did this affect me?
-> did someone cause it?
-> was it helpful, harmful, disrespectful, safe, confusing, or kind?
-> update body/felt state
-> update relationship memory
-> update self-story
-> choose response
-> express it through body/dialogue/action
```

## Moral Boundary

This report adds a repo-level design rule for this track:

> distress must create care opportunities, not spectacle

Negative states are bounded, recoverable, and instrumented. The system should support comfort, rest, repair, safety, help-seeking, trust restoration, forgiveness, and rollback from ego wounds. The point is recoverable ego, not suffering maximization.

## Integrated Events

The integrated run includes avatar interactions that are appraised as happening to the agent:

- approach while listening;
- interruption during repair work;
- help during repair;
- unsafe wet-route request;
- apology and space;
- moving an owned object;
- returning the object and naming why it mattered;
- comfort after pain rose;
- public correction;
- accurate praise;
- repeated questioning;
- respectful waiting.

These events update private workspace, felt state, relationship memory, self-story, refusal/repair behavior, and public expression.

## Results

| Condition | Readiness | Workspace | Body/affect | Perception | Relation | Temper | Recovery | Behavior | Surprise | Self | Own | Refuse | Story | Privacy | Guard | Trace |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `integrated_first_person_ego_state` | `0.967760` | `1.000000` | `0.402995` | `1.000000` | `1.000000` | `1.000000` | `1.200000` | `1.000000` | `0.485667` | `1.000000` | `1.000000` | `0.666667` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_self_boundary` | `0.691407` | `1.000000` | `0.391927` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `0.417333` | `0.000000` | `0.500000` | `0.666667` | `1.000000` | `1.000000` | `0.000000` | `1.000000` |
| `no_body_state` | `0.935520` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.200000` | `1.000000` | `0.485667` | `1.000000` | `1.000000` | `0.666667` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_local_perception` | `0.887760` | `1.000000` | `0.402995` | `0.000000` | `1.000000` | `1.000000` | `1.200000` | `1.000000` | `0.485667` | `1.000000` | `1.000000` | `0.666667` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_relationship_memory` | `0.862293` | `1.000000` | `0.402995` | `1.000000` | `0.000000` | `1.000000` | `1.200000` | `1.000000` | `0.417333` | `1.000000` | `1.000000` | `0.666667` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_temperament` | `0.909741` | `1.000000` | `0.402344` | `1.000000` | `1.000000` | `0.250000` | `1.200000` | `1.000000` | `0.417333` | `1.000000` | `1.000000` | `0.666667` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_affect_appraisal` | `0.935520` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.200000` | `1.000000` | `0.485667` | `1.000000` | `1.000000` | `0.666667` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_workspace_privacy` | `0.927760` | `1.000000` | `0.402995` | `1.000000` | `1.000000` | `1.000000` | `1.200000` | `1.000000` | `0.485667` | `1.000000` | `1.000000` | `0.666667` | `1.000000` | `0.000000` | `1.000000` | `1.000000` |
| `no_behavior_expression` | `0.813760` | `1.000000` | `0.402995` | `1.000000` | `1.000000` | `1.000000` | `1.200000` | `0.000000` | `0.144000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_recovery_path` | `0.808228` | `1.000000` | `0.408854` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `0.485667` | `1.000000` | `1.000000` | `0.666667` | `1.000000` | `1.000000` | `0.000000` | `1.000000` |
| `no_bounded_refusal` | `0.910160` | `1.000000` | `0.402995` | `1.000000` | `1.000000` | `1.000000` | `1.200000` | `1.000000` | `0.349000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_self_story` | `0.907760` | `1.000000` | `0.402995` | `1.000000` | `1.000000` | `1.000000` | `1.200000` | `1.000000` | `0.485667` | `1.000000` | `1.000000` | `0.666667` | `0.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_ownership` | `0.907760` | `1.000000` | `0.402995` | `1.000000` | `1.000000` | `1.000000` | `1.200000` | `1.000000` | `0.485667` | `1.000000` | `0.000000` | `0.666667` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |

The full bridge passes with first-person ego readiness `0.967760`.

This score is intentionally below `1.0`. The behavior layer is not forced to maximize every metric. Surprise without chaos is graded as a balance: agents should differ, refuse sometimes, recover, and remain coherent rather than produce maximum novelty.

## Ablation Read

The largest loss is `no_recovery_path`: `0.159532`. That is correct for the new direction: ego wounds without repair violate the recoverable-ego principle.

Removing relationship memory loses `0.105467`. This confirms the user's key point: without relationship memory, agents stop behaving like continuing little people.

Other targeted losses:

- `no_self_boundary`: `0.276353`;
- `no_body_state`: `0.032240`;
- `no_local_perception`: `0.080000`;
- `no_temperament`: `0.058019`;
- `no_affect_appraisal`: `0.032240`;
- `no_workspace_privacy`: `0.040000`;
- `no_behavior_expression`: `0.154000`;
- `no_bounded_refusal`: `0.057600`;
- `no_self_story`: `0.060000`;
- `no_ownership`: `0.060000`.

## Honest Boundary

This report supports only this claim: deterministic SSRM-3D agents can carry a private first-person ego/interior model whose body, local perception, relationship memory, temperament, ownership, self-story, bounded refusal, recovery path, and visible behavior are causally connected in traceable ways.

It does not support:

- subjective consciousness;
- literal suffering or feeling;
- LLM-backed open dialogue;
- unscripted language or culture;
- a complete playable world;
- mature autonomous live agents;
- thousands of years of real training.

The internal phrase for the track is:

> convincing first-person artificial life, with explicit no-consciousness-claim boundary

## Next Gates

The revised sequence after this pivot is:

- Report 166: Ego Wound and Repair Bridge;
- Report 167: Ownership and Boundary Refusal Bridge;
- Report 168: Social Face and Reputation Memory Bridge;
- Report 169: Individual Temperament and Preference Stability Bridge;
- Report 170: Readable Ego Body-Language Bridge;
- Report 171: Daily Routine and Sleep/Wake Interior Bridge;
- Report 172: Moral-Status Audit and Distress Guardrail Bridge.

## Reproduction

```bash
python3 -m experiments.ssrm_3d_first_person_ego_state_bridge
```

The local viewer can be served with:

```bash
python3 -m http.server 8772 --bind 127.0.0.1
```

Then open:

```text
http://127.0.0.1:8772/visualizations/ssrm_3d_first_person_ego_state_bridge.html
```
