# SSRM-3D Environment-Readiness Maturation Report

## Question

The live open-emergence sandbox now contains slower world pressures: fuel
stores, seed banks, building and tool blueprints, forecast memory,
apprenticeship, pest pressure, and structural strain.

This report asks the narrower evidence question:

```text
Can those readiness pressures run as a headless 72h benchmark, preserve the
12h no-major-shock development window, survive post-gate shocks, and expose
specific ablation losses for each preparation channel?
```

## What Changed

This is a standalone verifier:

- `experiments/ssrm_3d_environment_readiness_maturation.py`

It mirrors the new browser-sandbox readiness layer in a deterministic,
multi-seed, headless benchmark. The environment includes:

- `72h` accelerated worlds;
- no major shocks before `12h`;
- post-gate shocks after the development window;
- weather, temperature, visibility, disease, contamination, route hazard,
  resource migration, and depletion;
- food, water, materials, shelter, architecture, tools, workshop, waterworks,
  granary, paths, garden, sanitation, and fire control;
- slow preparation state: fuel reserve, seed bank, building blueprints, tool
  blueprints, forecast memory, and apprenticeship;
- stress channels: pest pressure and structural strain;
- abstract reproduction, children, teaching, knowledge transfer, aging, and
  death.

## What This Does Not Claim

This is not proof of consciousness. It is not open-ended civilization. It is
not a trained deep-RL agent. It is a designed pressure verifier that makes the
latest long-horizon sandbox mechanics measurable and ablatable.

The result is best read as:

```text
The richer world-readiness layer is now evidence-bearing in a headless verifier.
It is not yet a learned open simulation.
```

## Canonical Command

```bash
python3 experiments/ssrm_3d_environment_readiness_maturation.py --seeds 20261201,20261202,20261203,20261204,20261205 --hours 72 --step-hours 0.10 --population 14 --trace-seed 20261201
```

## Conditions

- `integrated_readiness`
- `reactive_immediate_needs`
- `no_seed_bank`
- `no_blueprints`
- `no_forecast_memory`
- `no_apprenticeship`
- `no_pest_control`
- `no_structural_repair`

## Canonical Result

The integrated condition passes the 12h development window and readiness gate:

- shock-gate pass rate: `1.000`;
- post-gate shock rate: `1.000`;
- mean alive at `12h`: `14.0`;
- mean final alive: `16.8`;
- mean births: `2.8`;
- mean deaths: `0.0`;
- mean readiness at `12h`: `0.411`;
- mean final readiness: `1.000`;
- mean pest pressure: `0.000`;
- mean structural strain: `0.000`;
- mean architecture delta: `0.860`;
- mean tool-system delta: `1.364`;
- mean knowledge transfer: `1.000`;
- mean maturation score: `0.999`.

The verdict is:

```text
supports_12h_development_window = true
supports_environment_readiness = true
supports_ablation_specificity = true
verdict = pass
```

## Ablation Boundary

The important nuance is that several ablations remain alive because the world
has redundant survival routes. The claim is not that every removed channel
causes extinction. The claim is that the specific preparation channel becomes
measurably absent or uncontrolled.

| Condition | Mean maturation | Main loss |
|---|---:|---:|
| `reactive_immediate_needs` | `0.071` | maturation loss `0.928`; final alive `0.0` |
| `no_seed_bank` | `0.998` | seed-bank channel loss `1.000` |
| `no_blueprints` | `0.951` | blueprint channel loss `1.000` |
| `no_forecast_memory` | `0.991` | forecast-memory channel loss `1.000` |
| `no_apprenticeship` | `0.970` | apprenticeship channel loss `1.000`; knowledge transfer `0.000` |
| `no_pest_control` | `1.000` | pest pressure rises from `0.000` to `0.993` |
| `no_structural_repair` | `0.996` | structural strain rises from `0.000` to `1.000` |

That is a bounded positive result, but it also exposes the next weakness:
single-channel ablations can leave total survival high. The next learned
controller must be judged on whether those channels matter to policy choices,
not only whether the designed verifier can track them.

## Interpretation

Report 135 strengthens the long-running world track in three ways:

- the browser sandbox readiness variables now have a headless verifier;
- the 12h development window is preserved across five seeds;
- post-gate shocks test accumulated preparation rather than immediate reaction.

It also keeps the claim boundary clear:

- readiness channels are designed state variables;
- actions are chosen by a hand-written benchmark policy;
- the benchmark does not use scenario labels in a learned controller because it
  is not yet a learned controller;
- the result does not solve Reports 123-134's learned-transfer bottleneck.

## Next Step

The next serious step is to move the readiness state into learned closed-loop
control:

- train on randomized readiness worlds;
- evaluate on held-out maps and shock schedules;
- remove direct pressure labels from model inputs;
- compare recurrent, world-only, self-state, and memory/controller variants;
- ablate readiness channels at evaluation;
- measure whether the learned policy actually uses preparation state to survive
  delayed shocks and repair cascades.

## Artifacts

- [script](../experiments/ssrm_3d_environment_readiness_maturation.py)
- [evaluation CSV](../artifacts/ssrm_3d_environment_readiness_maturation_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_environment_readiness_maturation_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_environment_readiness_maturation_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_environment_readiness_maturation_trace.json)
- [results JSON](../artifacts/ssrm_3d_environment_readiness_maturation_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_environment_readiness_maturation_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_environment_readiness_maturation_results.js)
