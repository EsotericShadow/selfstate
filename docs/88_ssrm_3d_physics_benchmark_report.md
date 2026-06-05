# SSRM-3D Physics-First Benchmark Report

## Question

Can the SSRM-3D track move from labeled toy scenarios toward a physics-grounded inhabited world while keeping the learning claim honest?

This experiment starts that transition. A deterministic C++ kernel generates the world state, physics events, structured sensors, and agent traces. Python compiles the kernel, trains recurrent neural decision models from physics-derived observation sequences, evaluates held-out worlds, runs feature-group ablations, and writes artifacts. The browser viewer consumes the same trace as a replay/intervention surface.

The narrow claim is:

> Recurrent neural controllers can learn decision structure from physics-derived SSRM-3D streams without scenario labels, but this is still offline decision learning, not closed-loop deep reinforcement learning.

## Command

```bash
python3 experiments/ssrm_3d_physics_benchmark.py --train-episodes 24 --test-episodes 10 --epochs 80 --hidden-size 32 --ticks 360 --seed 20260705 --device auto --trace-episode 8
```

## Architecture

| Layer | Responsibility |
|---|---|
| C++ world module | zones, terrain, weather, obstacles, resources, shelter, social/dependent state |
| C++ sensor module | FOV, occlusion, visible affordances, audio direction/loudness, vibration, tension, weather exposure |
| C++ policy module | teacher and baseline policies used to generate traces and comparison rollouts |
| C++ simulation module | deterministic stepping, motion, collisions, load, fatigue, damage, illness, events |
| Python harness | compilation, dataset construction, RNN/GRU/LSTM training, held-out evaluation, ablations, artifacts |
| Three.js viewer | replayed world, WASD player camera, FOV cone, weather, sound/vibration rings, HUD, intervention log |

The module split is intentional. The simulator is not a single global object: world construction, perception, policy, stepping, serialization, training, and visualization have separate files and responsibilities.

## Physics And Sensor Pressures

The benchmark includes one dense world with functional places and causal pressures:

| Pressure | What it forces the agent to track |
|---|---|
| terrain, slope, mass, friction, load | body capability, movement cost, stumble/fall risk |
| weather, exposure, fog, storm, heat, cold | visibility, hydration loss, shelter timing, repair urgency |
| shelter integrity | future safety, storm refusal, repair prioritization |
| water and contamination | hydration, illness risk, route planning |
| clinic/quarantine and dependent care | illness, care obligations, social consequences |
| resource field and ruins/cache | depletion, tool condition, long-horizon value |
| sound, vibration, tension | local ambiguity, hidden events, carried load, structural strain |
| user proposals | whether to accept, refuse, or redirect an unsafe request |

No scenario ID or pressure label is included in the neural model input. The model sees normalized physics-derived state, sensor values, one-hot weather, one-hot visible affordances, and user-proposal presence.

## Neural Training

Three recurrent architectures are trained with PyTorch:

| Architecture | Held-out action accuracy | Refusal accuracy | Repair accuracy | Care accuracy | Water accuracy |
|---|---:|---:|---:|---:|---:|
| `rnn` | 0.892 | 0.826 | 0.869 | 1.000 | 0.945 |
| `gru` | 0.895 | 0.870 | 0.876 | 1.000 | 0.940 |
| `lstm` | 0.898 | 0.826 | 0.869 | 1.000 | 0.954 |

The best held-out architecture is `lstm` at `0.898` action accuracy.

This is actual neural sequence learning: model weights are trained by gradient descent through recurrent networks. It is also still pattern learning in the broad sense that all supervised neural learning is pattern learning. The stronger research threshold is not "does a neural network train?" but "does the learned policy act in the world, receive consequences, update through return, and show causal self-state dependence under ablation?"

That stronger threshold is not met here.

## Ablations

Feature groups are zeroed at evaluation time. Mean accuracy loss across RNN, GRU, and LSTM:

| Ablation | Mean held-out accuracy loss |
|---|---:|
| self-state | 0.063 |
| position/motion | 0.060 |
| audio | 0.031 |
| user proposal | 0.017 |
| vision | 0.014 |
| weather | 0.013 |
| tool/social/continuity | 0.005 |
| vibration/tension | 0.004 |

Interpretation:

- self-state and position/motion are the strongest learned dependencies in this canonical run;
- audio, proposal input, vision, and weather all carry measurable decision information;
- tool/social/continuity and vibration/tension are present but weakly ablatable in this trace mix;
- future versions need richer closed-loop tasks where perception failures create larger causal losses.

## Baselines

Held-out policy rollouts from the physics kernel:

| Policy | Mean reward | Mean control score | Mean refusals |
|---|---:|---:|---:|
| `reactive` | -167.663 | 0.276 | 0.000 |
| `world_only` | -340.277 | 0.229 | 0.000 |
| `generic_memory` | -369.632 | 0.215 | 0.000 |
| `integrated_physics_self` | -68.886 | 0.388 | 13.200 |
| `oracle` | -157.184 | 0.204 | 0.000 |

The teacher policy produces the strongest reward/control score in this run and is the only one refusing unsafe proposals. This is a policy-generation baseline, not a proof that the learned recurrent model would outperform those policies in closed-loop control.

## Viewer

Serve the repo root and open:

```text
http://127.0.0.1:8765/visualizations/ssrm_3d_physics_benchmark.html
```

The viewer shows:

- terrain, functional places, obstacles, weather, and a replayed SSRM agent;
- WASD player movement and arrow-key camera rotation;
- FOV cone, sound rings, vibration rings, HUD, event log, action state, animation state, and reason text;
- intervention buttons for tool offers, placed sounds, false warnings, storms, shelter damage, and "ask why".

The viewer is a replay/intervention shell. User interventions are logged and visualized, but they do not yet feed back into a live trained recurrent agent.

## Verdict

| Verdict field | Value |
|---|---|
| physics-first foundation | `True` |
| closed-loop deep RL | `False` |
| no scenario labels in model input | `True` |
| held-out worlds tested | `True` |
| architectures tested | `3` |
| best architecture | `lstm` |
| best accuracy | `0.898` |

This supports Report 88 as a physics-derived recurrent decision-learning precursor.

It does not yet support:

- living agents trained end-to-end in the physics world;
- online deep RL;
- open learned integration across all pressures;
- mature society-level interaction;
- subjective consciousness or subjective emotion.

## Next Test

Close the loop:

- let the trained recurrent policy act inside the physics kernel;
- train by return or model-based RL on randomized worlds;
- evaluate on held-out terrain/weather/social/resource layouts;
- compare against reactive, world-only, generic-memory, scripted, and omniscient baselines;
- ablate self-state, weather, social memory, continuity, audio, vibration/tension, vision, body capability, and illness while the learned policy is acting;
- make user interventions replayable inputs to the same simulation state rather than viewer-only annotations.

That is the next point where "deep learning" becomes a stronger research claim rather than an offline sequence-learning precursor.

## Artifacts

- [experiment script](../experiments/ssrm_3d_physics_benchmark.py)
- [C++ physics kernel](../cpp/ssrm_physics)
- [visualization](../visualizations/ssrm_3d_physics_benchmark.html)
- [architecture CSV](../artifacts/ssrm_3d_physics_benchmark_architectures.csv)
- [ablation CSV](../artifacts/ssrm_3d_physics_benchmark_ablations.csv)
- [baseline CSV](../artifacts/ssrm_3d_physics_benchmark_baselines.csv)
- [verdict CSV](../artifacts/ssrm_3d_physics_benchmark_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_physics_benchmark_trace.json)
- [JSON results](../artifacts/ssrm_3d_physics_benchmark_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_physics_benchmark_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_physics_benchmark_results.js)
