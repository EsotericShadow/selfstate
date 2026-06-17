# Report 171: SSRM-3D Daily Routine Sleep-Wake Bridge

## Purpose

Report 171 adds time continuity to the little-people interior stack. Report 170 made private state readable through body language. This report asks whether those agents can persist through repeated days with routine, rest debt, sleep, recovery, place return, social return, interruption consequences, memory rehearsal, and frequency rhythm.

The goal is not to claim subjective consciousness. The goal is functional first-person continuity: an agent should not only look tired or guarded in a single moment. It should have a day, accumulate costs, recover through rest, return to familiar places, rehearse memory, and wake with continuity.

## Architecture

The bridge consumes the Report 170 readable body-language state and adds a deterministic day loop:

```text
Report 170 body-language state
        |
        v
circadian phase clock
        |
        v
sleep pressure + rest debt + body recovery
        |
        v
routine memory + place return + social return
        |
        v
interruption consequence + recovery
        |
        v
dream-like memory rehearsal
        |
        v
frequency/flower phase alignment
        |
        v
replayable daily trace
```

Each agent receives a `daily_state` object with:

- `energy`
- `fatigue`
- `rest_debt`
- `comfort`
- `sleep_pressure`
- `current_place`
- `routine_memory`
- `dream_rehearsal`
- `interruption_ledger`
- `frequency_history`
- `flower_history`
- `self_time_story`

The daily trace records public behavior and continuity markers while keeping private workspace content hidden.

## Day phases

The deterministic day uses eight phases:

- `deep_sleep`
- `dawn_wake`
- `morning_work`
- `midday_social`
- `afternoon_explore`
- `evening_return`
- `night_ritual`
- `sleep_onset`

The phase loop is intentionally small, but it gives later browser agents a stable spine for routines, fatigue, social return, interruption, recovery, and ritual.

## Frequency and flower-cycle layer

This report adds a first explicit daily frequency rhythm:

- breath-rate-derived baseline
- circadian sine modulation
- flower-node harmonic modulation
- sleep-phase downshift
- deterministic `FLOWER_NODES` cycle

The flower cycle is not treated as proof of consciousness or physics. It is a symbolic/structural rhythm layer that can later bind place, ritual, body state, music/sound, and group mood into a coherent simulation grammar.

## Conditions

The integrated condition is:

- `integrated_daily_routine_sleep_wake`

Ablations remove one mechanism at a time:

- `no_circadian_clock`
- `no_body_recovery`
- `no_routine_memory`
- `no_place_affinity`
- `no_social_return`
- `no_interrupt_consequence`
- `no_dream_rehearsal`
- `no_replay_continuity`
- `no_frequency_phase`
- `no_sleep_safety_guard`

The important test is whether removing time structure, recovery, or continuity makes the agents collapse back into momentary animated state.

## Metrics

The benchmark reports:

- `circadian_phase_binding`
- `sleep_pressure_coupling`
- `rest_recovery_rate`
- `routine_completion_rate`
- `place_return_rate`
- `social_return_rate`
- `interruption_consequence_rate`
- `dream_memory_rehearsal_rate`
- `wake_transition_stability`
- `fatigue_boundedness_rate`
- `frequency_rhythm_coherence`
- `flower_cycle_alignment`
- `privacy_preservation_rate`
- `replay_continuity_rate`
- `trace_integrity`
- `daily_routine_sleep_wake_readiness`

The metric weights are normalized to sum to `1.0`. An initial local draft produced a score above `1.0`; that was corrected before publication and the artifacts were regenerated.

## Results

The deterministic run produced:

| Metric | Value |
| --- | ---: |
| `module_verdict` | `pass` |
| `daily_routine_sleep_wake_readiness` | `0.935797` |
| `no_circadian_clock_loss` | `0.133102` |
| `no_body_recovery_loss` | `0.067477` |

Interpretation:

- The bridge supports daily routine and sleep-wake continuity.
- Circadian structure is meaningfully load-bearing.
- Body recovery is load-bearing, but less dominant than the clock/routine layer.
- The score is lower than the more mechanical browser/session gates because this is a harder artificial-life claim: time continuity must coordinate body cost, recovery, place, social rhythm, memory, and trace replay.

## Moral boundary

The moral boundary remains explicit:

- no subjective-consciousness claim
- no suffering-maximization objective
- sleep is a care/recovery path, not punishment
- distress and fatigue must stay bounded and recoverable
- interruption creates consequences, not irreversible damage
- private workspace remains private unless expressed through behavior

## Artifacts

- `artifacts/ssrm_3d_daily_routine_sleep_wake_bridge_eval.csv`
- `artifacts/ssrm_3d_daily_routine_sleep_wake_bridge_verdict.csv`
- `artifacts/ssrm_3d_daily_routine_sleep_wake_bridge_results.json`
- `artifacts/ssrm_3d_daily_routine_sleep_wake_bridge_results.js`
- `artifacts/ssrm_3d_daily_routine_sleep_wake_bridge_trace.json`
- `artifacts/ssrm_3d_daily_routine_sleep_wake_bridge_trace.js`
- `artifacts/ssrm_3d_daily_routine_sleep_wake_bridge_state.json`
- `artifacts/ssrm_3d_daily_routine_sleep_wake_bridge_state.js`
- `visualizations/ssrm_3d_daily_routine_sleep_wake_bridge.html`

## Command

```bash
python3 -m experiments.ssrm_3d_daily_routine_sleep_wake_bridge
```

## Verdict

Report 171 supports a deterministic daily routine sleep-wake bridge. The agents now have a repeated day loop with body cost, rest recovery, place return, social return, interruption consequence, dream-like memory rehearsal, frequency rhythm, flower-cycle alignment, privacy preservation, and replay continuity.

The next gate is learned reactions from repeated user interaction: agents should change future behavior after repeated avatar contact while remaining bounded, recoverable, inspectable, and non-random.
