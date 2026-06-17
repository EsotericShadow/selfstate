# Report 162: SSRM-3D Interruptible Real-Time Co-Presence Bridge

Date: 2026-06-16

## Purpose

Report 161 restored a saved session and let autonomous background ticks continue over elapsed time. Report 162 adds the next required bridge: the avatar can interrupt a running restored session while the background loop keeps moving.

The benchmark now captures seeded avatar utterances during autonomous ticking, parses them into grounded local intents, routes them to nearby agents, records acknowledgements, applies avatar body cost, keeps source-boundary handling explicit, writes typed-thread continuity, exports replay frames, and measures recovery after interruption.

No LLMs are called. This is not evidence of subjective consciousness, open-ended natural language, unscripted civilization, or a complete playable world.

## Implementation

The new module is:

- `experiments/ssrm_3d_interruptible_realtime_copresence_bridge.py`

It consumes:

- `artifacts/ssrm_3d_restored_autonomous_session_tick_bridge_state.json`

It emits:

- `artifacts/ssrm_3d_interruptible_realtime_copresence_bridge_eval.csv`
- `artifacts/ssrm_3d_interruptible_realtime_copresence_bridge_verdict.csv`
- `artifacts/ssrm_3d_interruptible_realtime_copresence_bridge_results.json`
- `artifacts/ssrm_3d_interruptible_realtime_copresence_bridge_results.js`
- `artifacts/ssrm_3d_interruptible_realtime_copresence_bridge_trace.json`
- `artifacts/ssrm_3d_interruptible_realtime_copresence_bridge_trace.js`
- `artifacts/ssrm_3d_interruptible_realtime_copresence_bridge_state.json`
- `artifacts/ssrm_3d_interruptible_realtime_copresence_bridge_state.js`

The browser artifact is:

- `visualizations/ssrm_3d_interruptible_realtime_copresence_bridge.html`

## New Bridge Objects

The integrated run covers:

- `240` real-time ticks;
- `12` seeded avatar interrupts;
- restored Report 161 session state;
- background elapsed-time continuation;
- interrupt packet capture;
- grounded utterance parsing;
- proximity-based dispatch;
- agent acknowledgement;
- recovery windows after interruption;
- source-boundary filtering for source/override prompts;
- avatar body cost and frequency-rate coupling;
- typed-thread persistence;
- replay export for browser playback.

The intentionally unusual object boundary is that an avatar utterance is not treated as a synchronous command. It becomes an `InterruptPacket` that competes with the background tick loop, creates a short recovery debt, and must be reconciled with body state, sensory-frequency phase, source boundary, replay, and the continuing agent work loop.

## Interruptible Runtime Contract

The deterministic contract adds these components:

- keep elapsed background ticks advancing during avatar input;
- capture avatar utterances into an interrupt queue rather than stopping the world;
- parse utterances into bounded local intents;
- route interrupts to nearby or hinted agents;
- force agents to acknowledge without erasing their background work state;
- charge avatar body/attention cost for interrupting;
- preserve source-boundary behavior for source and override prompts;
- write avatar and agent turns into the typed thread;
- export replay frames with queue depth, acknowledgements, and recoveries;
- recover interrupted agents back into background work.

## Results

| Condition | Readiness | Clock | Queue | Parser | Route | Ack | Recover | Source | Replay | Thread | Body | Freq | Trace |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `integrated_interruptible_realtime_copresence` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_background_clock` | `0.810000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` |
| `no_interrupt_queue` | `0.310000` | `1.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `1.000000` | `0.000000` | `0.000000` | `1.000000` | `1.000000` |
| `no_grounded_parser` | `0.560000` | `1.000000` | `1.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_proximity_routing` | `0.920000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_agent_acknowledgement` | `0.800000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_recovery_loop` | `0.900000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_source_boundary_filter` | `0.920000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_replay_export` | `0.930000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_thread_persistence` | `0.920000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_avatar_body_cost` | `0.930000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` |
| `no_frequency_coupling` | `0.920000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` |

The full bridge passes with interruptible co-presence readiness `1.000000`.

## Ablation Read

The largest loss is `no_interrupt_queue`: `0.690000`. This confirms the benchmark is not merely a background-tick replay; interrupt capture is the central bridge.

Removing grounded parsing loses `0.440000`. Removing agent acknowledgement loses `0.200000`. Removing the background clock loses `0.190000`. Removing recovery loses `0.100000`. Removing proximity routing loses `0.080000`. Source-boundary filtering, replay export, thread persistence, avatar body cost, and frequency coupling each produce targeted smaller losses.

## Honest Boundary

This report supports only this claim: a restored deterministic local session can continue background ticks while avatar interruptions are queued, grounded, routed, acknowledged, recovered from, and replayed.

It does not support:

- subjective consciousness;
- LLM-backed open dialogue;
- unscripted language or culture;
- a complete playable world;
- mature autonomous live agents.

The next gate is a stricter real-time avatar embodiment loop: player navigation, sensory sampling, and interrupt handling should run from the browser clock itself rather than only from a precomputed deterministic trace.

## Reproduction

```bash
python3 -m experiments.ssrm_3d_interruptible_realtime_copresence_bridge
```

The local viewer can be served with:

```bash
python3 -m http.server 8772 --bind 127.0.0.1
```

Then open:

```text
http://127.0.0.1:8772/visualizations/ssrm_3d_interruptible_realtime_copresence_bridge.html
```
