# Report 163: SSRM-3D Browser-Clock Avatar Embodiment Bridge

Date: 2026-06-16

## Purpose

Report 162 showed that a restored deterministic session can keep background ticks running while avatar interrupts are queued, grounded, routed, acknowledged, recovered from, and replayed. Report 163 moves the next bridge into the browser clock itself.

The avatar now has a live local body in the browser viewer. Movement, heading, nearby place detection, sensory-rate sampling, collision/affordance contact, interrupt entry, source-boundary handling, local save/restore, replay capture, and agent background drift all run from the browser's `requestAnimationFrame` loop. The Python module validates the same contract headlessly so the bridge remains reproducible.

No LLMs are called. This is not evidence of subjective consciousness, open-ended natural language, unscripted civilization, or a complete playable world.

## Implementation

The new module is:

- `experiments/ssrm_3d_browser_clock_avatar_embodiment_bridge.py`

It consumes:

- `artifacts/ssrm_3d_interruptible_realtime_copresence_bridge_state.json`

It emits:

- `artifacts/ssrm_3d_browser_clock_avatar_embodiment_bridge_eval.csv`
- `artifacts/ssrm_3d_browser_clock_avatar_embodiment_bridge_verdict.csv`
- `artifacts/ssrm_3d_browser_clock_avatar_embodiment_bridge_results.json`
- `artifacts/ssrm_3d_browser_clock_avatar_embodiment_bridge_results.js`
- `artifacts/ssrm_3d_browser_clock_avatar_embodiment_bridge_trace.json`
- `artifacts/ssrm_3d_browser_clock_avatar_embodiment_bridge_trace.js`
- `artifacts/ssrm_3d_browser_clock_avatar_embodiment_bridge_state.json`
- `artifacts/ssrm_3d_browser_clock_avatar_embodiment_bridge_state.js`

The browser artifact is:

- `visualizations/ssrm_3d_browser_clock_avatar_embodiment_bridge.html`

## New Bridge Objects

The integrated run covers:

- `300` headless browser-clock ticks;
- `186` movement frames;
- `300` sensory samples;
- `900` background agent events;
- `7` embodied avatar interrupts;
- `174` collision/affordance contacts;
- `300` avatar body-cost updates;
- `300` replay frames.

The browser surface adds live local runtime objects:

- avatar body state: energy, attention, pain, wetness, affect, breath rate, footstep rate, heading, and place;
- flower-of-life projected place layout;
- object positions with affordance proximity;
- agent positions with background drift;
- sensory rates for vibration, sound, vision, scent, thermal, wetness, pain, and affect;
- local interrupt packets and source-boundary handling;
- runtime save/restore and replay export.

## Browser-Clock Runtime Contract

The deterministic contract adds these components:

- browser clock advances runtime frames;
- avatar movement changes body position and current place;
- sensory rates are sampled from nearby agents, objects, world variables, and flower phase;
- background agents continue drifting and updating attention;
- avatar interrupts can be entered while the loop runs;
- source/override prompts are handled as bounded source-boundary events;
- object proximity creates collision/affordance contact;
- movement, collision, and interrupt actions charge avatar body state;
- flower phase modulates sensory rates;
- local runtime can save, restore, and export replay.

## Results

| Condition | Readiness | Clock | Move | Sensory | Agents | Interrupt | Collide | Body | Flower | Source | Replay | Restore | Trace |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `integrated_browser_clock_avatar_embodiment` | `0.962000` | `1.000000` | `0.620000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_browser_clock` | `0.852000` | `0.000000` | `0.620000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_avatar_navigation` | `0.900000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_sensory_sampling` | `0.852000` | `1.000000` | `0.620000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_agent_background_continuity` | `0.862000` | `1.000000` | `0.620000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_embodied_interrupts` | `0.872000` | `1.000000` | `0.620000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_collision_affordances` | `0.882000` | `1.000000` | `0.620000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_avatar_body_cost` | `0.882000` | `1.000000` | `0.620000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_frequency_flower_coupling` | `0.872000` | `1.000000` | `0.620000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_source_boundary_runtime` | `0.892000` | `1.000000` | `0.620000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_replay_recording` | `0.892000` | `1.000000` | `0.620000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` |
| `no_runtime_save_restore` | `0.912000` | `1.000000` | `0.620000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` |

The full bridge passes with browser-clock embodiment readiness `0.962000`.

This is intentionally not perfect. The readiness is below `1.0` because avatar navigation is real movement over a projected place graph rather than guaranteed arrival on every frame, and collision affordance depends on actual proximity opportunities. That is more honest than forcing a full score.

## Ablation Read

The largest direct losses are `no_browser_clock`: `0.110000`, `no_sensory_sampling`: `0.110000`, and `no_agent_background_continuity`: `0.100000`. Those are the core pieces that distinguish this bridge from precomputed playback.

Removing embodied interrupts loses `0.090000`. Removing frequency/flower coupling loses `0.090000`. Removing collision affordances, avatar body cost, source-boundary runtime, replay recording, or runtime save/restore creates targeted smaller losses.

## Honest Boundary

This report supports only this claim: a deterministic browser surface can run a live local avatar body loop over the existing SSRM-3D settlement state while background agents, sensory rates, interrupts, source boundaries, save/restore, and replay continue locally.

It does not support:

- subjective consciousness;
- LLM-backed open dialogue;
- unscripted language or culture;
- a complete playable world;
- mature autonomous live agents;
- thousands of years of real training.

The next gate is persistent browser-runtime sessions: the live browser state should be serializable across reloads and able to re-enter the Python artifact pipeline instead of remaining only a local viewer runtime.

## Reproduction

```bash
python3 -m experiments.ssrm_3d_browser_clock_avatar_embodiment_bridge
```

The local viewer can be served with:

```bash
python3 -m http.server 8772 --bind 127.0.0.1
```

Then open:

```text
http://127.0.0.1:8772/visualizations/ssrm_3d_browser_clock_avatar_embodiment_bridge.html
```
