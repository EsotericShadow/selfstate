# SSRM Physics Kernel

This folder contains the first C++ SSRM-3D physics/sensor kernel.

It is intentionally small and modular. The kernel is not the learned model and it is not the viewer. Its job is to generate deterministic world state, physical pressures, sensor observations, actions, and traces that Python can train against and the browser can replay.

## Modules

| File | Responsibility |
|---|---|
| `include/ssrm_physics/types.hpp` | shared state, zone, weather, object, frame, event, and summary types |
| `include/ssrm_physics/math.hpp` | vector math and small deterministic utility functions |
| `include/ssrm_physics/ablations.hpp` | ablation parsing and helper predicates |
| `include/ssrm_physics/world.hpp` + `src/world.cpp` | deterministic world construction and terrain/environment queries |
| `include/ssrm_physics/sensors.hpp` + `src/sensors.cpp` | physics-derived observation generation |
| `include/ssrm_physics/policy.hpp` + `src/policy.cpp` | teacher and baseline policy decisions |
| `include/ssrm_physics/simulation.hpp` + `src/simulation.cpp` | episode stepping, movement, contact, fatigue, damage, events, and summary metrics |
| `include/ssrm_physics/json_writer.hpp` + `src/json_writer.cpp` | trace serialization |
| `src/main.cpp` | CLI argument parsing and kernel entry point |

## Boundary Rules

- Add new world mechanics in `world.*` only when they change available observations, action effects, cost, risk, or future state.
- Add new perceived signals in `sensors.*`; do not leak scenario labels into learned-controller inputs.
- Add baseline or teacher decisions in `policy.*`; do not put training code in C++.
- Add stepping consequences in `simulation.*`; keep serialization and viewer concerns out of the simulator.
- Keep Python responsible for training, ablations, metrics, manifests, and artifacts.
- Keep the viewer read-only or explicitly replay/intervention-oriented until live closed-loop control is implemented.

## Current Limitation

The current benchmark is offline recurrent decision learning from physics-derived traces. It is not closed-loop deep reinforcement learning yet.
