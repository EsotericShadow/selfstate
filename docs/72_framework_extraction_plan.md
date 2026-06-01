# Framework Extraction Plan

## Purpose

The reusable value of this repo is not one experiment. It is the set of primitives for building agents whose behavior is shaped by persistent state, continuity, attention, arbitration, memory, social pressure, and tool use.

The extraction target is a framework that can power:

- research experiments;
- a 3D live demo;
- a game prototype;
- robotics control surfaces;
- business agents that need persistent commitments and state-grounded refusal.

## Core Package

The first extraction should center on stable primitives:

- `SelfState`
- `WorldState`
- `AgentContinuityRecord`
- `AttentionMixer`
- `Arbiter`
- `EventLog`
- `WorldSnapshot`
- `MultiRateScheduler`

These should be small, testable, and independent of any particular visualization.

## Research Harness

Research-specific tools should sit around the core rather than inside it:

- `AblationHarness`
- `ReplayTimeline`
- `AgentInspector`
- `LLMPacketBoundary`
- seeded scenario generators;
- verdict schemas;
- manifest runner.

The harness should make negative results first-class. A falsified claim should produce a clean verdict artifact, not a process failure.

## Demo Layer

The demo layer should depend on the core and harness, but not define them:

- `LocalSpeechInput`
- `VisitorAvatar`
- `GodModeInterventionLog`
- Three.js renderer;
- inspector panels;
- timeline scrubber;
- ablation toggles.

## Proposed Repository Structure

```text
src/core
src/selfstate
src/continuity
src/attention
src/arbitration
src/memory
src/social
src/tools
src/simulation
src/replay
src/ablations
src/demo
```

## Extraction Order

1. Extract `MultiRateScheduler`, `EventLog`, and `WorldSnapshot`.
2. Extract `AgentContinuityRecord` and restore/fork helpers.
3. Extract `AttentionMixer` and `Arbiter`.
4. Extract `LLMPacketBoundary` as a packet contract, not an LLM dependency.
5. Port one existing SSRM-3D precursor onto the extracted primitives.
6. Build the live demo on the extracted primitives only after the core is usable.

## Design Rules

- Keep language reasoning advisory.
- Keep the arbiter as the action authority.
- Treat user commands as proposals.
- Make ablations easy to run.
- Separate bridge claims from strong integration claims.
- Preserve auditability through event logs and verdict artifacts.

## First Success Condition

The extraction succeeds when one SSRM-3D scenario can be replayed from an event log, restored from a `WorldSnapshot`, inspected through an `AgentContinuityRecord`, and ablated through `AblationHarness` without depending on the current monolithic experiment script.
