# SSRM-3D Long-Horizon Adaptation Report

## Question

The live open-emergence sandbox now has a browser-side 12h audit. This report asks whether the same milestone can be verified headlessly across multiple seeds with targeted ablations.

The narrow question is:

```text
Can agents develop for 12 simulated hours before any major shock, survive a post-gate shock, improve infrastructure and tools, accumulate adaptation evidence, and transmit knowledge when the relevant channels are present?
```

## What changed

This is a headless companion to the browser sandbox, not a replacement for the physics kernel.

It adds:

- a 14.5h simulated run with a 12h major-shock gate;
- five deterministic seeds;
- checkpoint tracking at `1h`, `6h`, `12h`, `12.5h`, and `14.5h`;
- slow ecology, contamination, disease strain, route hazard, resource migration, and social pressure;
- infrastructure development: shelter, architecture, waterworks, paths, storage, and garden;
- tool development: tools and tool design;
- risk memory, teaching tradition, and knowledge transfer;
- adaptation evidence and pressure integral;
- targeted ablations.

## What this does not claim

This is not proof of consciousness. It is not open-ended civilization emergence. It is not closed-loop deep reinforcement learning. It is a designed long-horizon pressure verifier.

## Canonical command

```bash
python3 experiments/ssrm_3d_long_horizon_adaptation.py --seeds 20260708,20260709,20260710,20260711,20260712 --hours 14.5 --step-hours 0.05 --population 10 --trace-seed 20260708
```

## Conditions

- `integrated_long_horizon`
- `reactive_survival_only`
- `no_teaching_transmission`
- `no_risk_memory`
- `no_infrastructure_memory`
- `no_tool_improvement`
- `no_adaptive_arbitration`

## Canonical result

The integrated condition passes the long-horizon gate:

- shock-gate pass rate: `1.000`;
- post-gate shock rate: `1.000`;
- mean alive at `12h`: `10.4`;
- mean final alive: `10.6`;
- mean adaptation evidence: `0.636`;
- mean architecture delta: `0.705`;
- mean tool-design delta: `0.787`;
- mean knowledge transfer: `0.874`;
- mean long-horizon score: `0.964`.

The ablations create specific losses:

- reactive survival only: score `0.516`, loss `0.448`;
- no teaching transmission: score `0.784`, knowledge loss `0.967`;
- no risk memory: score `0.918`, post-shock loss `0.086`;
- no infrastructure memory: score `0.684`, development loss `0.420`;
- no tool improvement: score `0.869`, development loss `0.383`;
- no adaptive arbitration: score `0.675`, long-horizon loss `0.289`.

The verdict is:

```text
supports_long_horizon_development = true
supports_ablation_specificity = true
verdict = pass
```

## Trace checkpoints

The integrated trace for seed `20260708` records:

| checkpoint | alive | shocks | food | water | architecture | tool design | teaching | risk memory | adaptation evidence | knowledge transfer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `1h` | 10 | 0 | 0.794 | 0.783 | 0.160 | 0.188 | 0.080 | 0.145 | 0.046 | 0.000 |
| `6h` | 10 | 0 | 0.757 | 0.689 | 0.625 | 0.554 | 0.363 | 0.349 | 0.274 | 0.252 |
| `12h` | 11 | 0 | 0.791 | 0.670 | 0.810 | 0.788 | 0.829 | 0.822 | 0.525 | 0.761 |
| `12.5h` | 11 | 0 | 0.790 | 0.672 | 0.831 | 0.815 | 0.851 | 0.850 | 0.546 | 0.780 |
| `14.5h` | 11 | 1 | 0.792 | 0.660 | 0.901 | 0.945 | 0.966 | 1.000 | 0.637 | 0.882 |

## Interpretation

This is stronger than the browser audit alone because it runs multiple seeds and ablates the channels that should matter:

- without teaching, knowledge transfer collapses;
- without infrastructure memory, architecture and settlement development suffer;
- without tool improvement, tool design stays near zero;
- without risk memory, post-shock performance falls;
- without adaptive arbitration, agents stay alive but lose long-horizon development and knowledge transfer;
- reactive survival can keep bodies alive, but does not build the world.

The key distinction is important: survival alone is not the target. The target is survival plus development, adaptation, memory, transmission, and post-shock function.

## Artifacts

- [script](../experiments/ssrm_3d_long_horizon_adaptation.py)
- [evaluation CSV](../artifacts/ssrm_3d_long_horizon_adaptation_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_long_horizon_adaptation_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_long_horizon_adaptation_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_long_horizon_adaptation_trace.json)
- [results JSON](../artifacts/ssrm_3d_long_horizon_adaptation_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_long_horizon_adaptation_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_long_horizon_adaptation_results.js)

## Next gate

The next serious step is a learned-controller version:

- observations only, no condition labels;
- randomized long-horizon worlds;
- policies trained rather than scripted;
- held-out worlds;
- ablations applied during acting;
- longer generational runs beyond 14.5h.
