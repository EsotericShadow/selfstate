# Report 159: SSRM-3D Interactive Typed Co-presence Bridge

Date: 2026-06-16

## Purpose

Report 158 made the avatar a same-loop perturbation inside nearby agents' deterministic control cycle. Report 159 adds the next required bridge toward a playable world we can talk to: interactive typed co-presence.

The browser now accepts a local typed utterance, parses it deterministically, routes it to nearby agents at the avatar's current place, and mutates agent workspace, social memory, frequency state, world feedback, source boundaries, persistent dialogue thread, and replay export without calling an LLM or regenerating a precomputed benchmark trace.

This is not evidence of subjective consciousness, open-ended natural language, unscripted civilization, or a complete playable world.

## Implementation

The new module is:

- `experiments/ssrm_3d_interactive_typed_copresence_bridge.py`

It consumes:

- `artifacts/ssrm_3d_continuous_copresence_bridge_state.json`

It emits:

- `artifacts/ssrm_3d_interactive_typed_copresence_bridge_eval.csv`
- `artifacts/ssrm_3d_interactive_typed_copresence_bridge_verdict.csv`
- `artifacts/ssrm_3d_interactive_typed_copresence_bridge_results.json`
- `artifacts/ssrm_3d_interactive_typed_copresence_bridge_results.js`
- `artifacts/ssrm_3d_interactive_typed_copresence_bridge_trace.json`
- `artifacts/ssrm_3d_interactive_typed_copresence_bridge_trace.js`
- `artifacts/ssrm_3d_interactive_typed_copresence_bridge_state.json`
- `artifacts/ssrm_3d_interactive_typed_copresence_bridge_state.js`

The browser artifact is:

- `visualizations/ssrm_3d_interactive_typed_copresence_bridge.html`

## New Bridge Objects

The integrated run covers:

- `144` typed turns;
- `153` routed nearby-agent opportunities;
- deterministic local utterance parsing;
- nearby place-based routing;
- local agent response generation;
- workspace-thread writes;
- social-memory updates;
- world-feedback mutation;
- source-boundary refusals for unsafe probes;
- sensory-frequency retuning;
- persistent browser-side thread and replay export.

The viewer contains a client-side runtime contract: typed utterances mutate the loaded browser state rather than asking the Python benchmark to regenerate traces.

## Typed Co-presence Contract

The deterministic contract adds these components:

- local typed input acceptance;
- nearby embodied-agent routing;
- deterministic intent parsing for presence, source question, repair request, token exchange, memory request, frequency tuning, sensory question, and unsafe ungrounded probes;
- agent responses generated from local state and intent templates;
- internal workspace writes;
- social-memory and relation-to-avatar updates;
- world feedback, including a monotonic typed-feedback counter for auditability;
- source-boundary preservation for unsafe ungrounded utterances;
- frequency retuning across vibration, sound, vision, scent, thermal, wetness, pain, and affect;
- persistent typed thread;
- replay export.

## Results

| Condition | Readiness | Input | Routing | Parse | Response | Workspace | Social | World | Source | Frequency | Thread | Replay | Trace |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `integrated_interactive_typed_copresence` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_live_typed_input` | `0.050000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `1.000000` | `1.000000` |
| `no_nearby_agent_routing` | `0.330000` | `1.000000` | `0.000000` | `1.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_deterministic_intent_parser` | `0.230000` | `1.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_agent_response_generation` | `0.900000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_workspace_thread_write` | `0.900000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_social_memory_update` | `0.920000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_world_feedback` | `0.900000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_source_boundary` | `0.900000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_frequency_retuning` | `0.920000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_persistent_thread` | `0.940000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` |
| `no_replay_export` | `0.970000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` |

The full bridge passes with typed co-presence readiness `1.000000`.

## Ablation Read

The largest loss is `no_live_typed_input`: `0.950000`. That is correct: without user text, there is no typed co-presence.

The second-largest loss is `no_deterministic_intent_parser`: `0.770000`; text reaches the system but cannot route into meaningful local action. `no_nearby_agent_routing` loses `0.670000`; parsed text cannot matter if no embodied nearby agent receives it.

Agent response, workspace, world feedback, and source boundary each lose `0.100000`. Social memory and frequency retuning each lose `0.080000`. Persistent thread and replay losses are smaller, but they preserve auditability and user-facing continuity.

## Honest Boundary

This report supports only this claim: the stack now has deterministic interactive typed co-presence where browser-side local text routes to nearby agents and mutates the loaded co-presence runtime.

It does not support:

- subjective consciousness;
- LLM-backed open dialogue;
- unscripted language or culture;
- a complete playable world;
- mature autonomous live agents.

The next gate is persistent unscripted session state: multiple user turns should remain live across browser session time, with agent memories, world feedback, and place state carrying over through a saved/restored local session instead of only a generated artifact state.

## Reproduction

```bash
python3 -m experiments.ssrm_3d_interactive_typed_copresence_bridge
```

The local viewer can be served with:

```bash
python3 -m http.server 8772 --bind 127.0.0.1
```

Then open:

```text
http://127.0.0.1:8772/visualizations/ssrm_3d_interactive_typed_copresence_bridge.html
```
