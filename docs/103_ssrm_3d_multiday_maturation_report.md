# SSRM-3D Multi-Day Maturation Report

## Question

Report 93 verified a 14.5h long-horizon gate. This report extends that track into a 72h accelerated world so development has time to appear before major shocks dominate.

The narrow question is:

```text
Can a population run for at least 12 simulated hours before any major shock, then keep maturing across several days through building, tool improvement, environmental pressure, births, teaching, risk memory, and post-gate shocks?
```

## What Changed

This is a modular headless verifier, split into:

- `experiments/ssrm_maturation/models.py`: shared data types;
- `experiments/ssrm_maturation/environment.py`: weather, ecology, disease, resource migration, shocks, pressure;
- `experiments/ssrm_maturation/agents.py`: lifecycle, action choice, reproduction, teaching, skill change;
- `experiments/ssrm_maturation/metrics.py`: summaries and verdict logic;
- `experiments/ssrm_maturation/artifacts.py`: CSV/JSON/JS output;
- `experiments/ssrm_maturation/benchmark.py`: episode orchestration;
- `experiments/ssrm_3d_multiday_maturation.py`: CLI wrapper.

The environment adds:

- 72h accelerated runs;
- 12h minimum major-shock gate;
- shocks spaced across later multi-hour windows;
- day/night, seasonal heat/cold, rainfall, wind, visibility;
- route hazards, predators, disease, contamination, resource migration, depletion, soil pressure;
- building systems: shelter, architecture, waterworks, granary, paths, garden, sanitation;
- tool systems: tools, workshop, fire control, tool tiers;
- social/culture systems: trust, conflict, symbols, culture;
- lineage: births, children, aging, inherited traits, teaching-dependent knowledge transfer.

## What This Does Not Claim

This is not proof of consciousness. It is not open-ended civilization. It is not a trained deep-RL policy. It is a designed pressure verifier that checks whether the requested long-run mechanics are now present and ablatable.

## Canonical Command

```bash
python3 experiments/ssrm_3d_multiday_maturation.py --seeds 20260901,20260902,20260903,20260904,20260905 --hours 72 --step-hours 0.10 --population 14 --trace-seed 20260901
```

## Conditions

- `integrated_maturation`
- `reactive_survival_only`
- `no_teaching_lineage`
- `no_risk_memory`
- `no_infrastructure_memory`
- `no_tool_improvement`
- `no_social_learning`
- `no_environmental_sensing`

## Canonical Result

The integrated condition passes the 12h development window and multi-day maturation gate:

- shock-gate pass rate: `1.000`;
- post-gate shock rate: `1.000`;
- mean alive at `12h`: `14.0`;
- mean final alive: `17.2`;
- mean births: `3.2`;
- mean deaths: `0.0`;
- mean architecture tier: `4.0`;
- mean tool tier: `4.0`;
- mean knowledge transfer: `1.000`;
- mean adaptation evidence: `1.000`;
- mean maturation score: `0.999`.

The verdict is:

```text
supports_12h_development_window = true
supports_multiday_maturation = true
supports_ablation_specificity = true
verdict = pass
```

## Ablation Boundary

The important result is not only that the integrated condition survives. It is that the controls damage the intended channel:

| Ablation | Main loss |
|---|---:|
| `reactive_survival_only` | maturation loss `0.536` |
| `no_teaching_lineage` | knowledge-transfer loss `1.000` |
| `no_risk_memory` | recovery loss `0.165` |
| `no_infrastructure_memory` | architecture-delta loss `1.000` |
| `no_tool_improvement` | tool-system loss `1.674` |
| `no_social_learning` | culture/symbol loss `1.415` |
| `no_environmental_sensing` | maturation loss `0.215` |

Several ablations still keep bodies alive. That is expected. The target here is not raw survival; it is survival plus maturation, architecture, tools, transmission, culture, and post-shock recovery.

## Trace Checkpoints

The trace for seed `20260901` records fixed checkpoints from `0h` to `72h`. It is visualized in:

- [multi-day maturation viewer](../visualizations/ssrm_3d_multiday_maturation.html)

The viewer shows the 12h shock gate, post-gate shocks, population growth, births/deaths, infrastructure tiers, tool tiers, culture/symbol growth, and pressure variables.

## Interpretation

This is a stronger match to the requested long-running world than Report 93:

- major shocks do not happen before the 12h development window;
- agents can develop buildings and tools over days;
- births and inherited state exist as costly lifecycle pressure;
- teaching is required for knowledge transfer;
- environmental sensing affects maturation under changing ecology;
- infrastructure memory and tool improvement are separately ablatable.

It is still not the final goal. The next serious step is to move this maturation world into learned closed-loop control:

- no condition labels;
- randomized held-out worlds;
- policy/value models trained by return;
- multi-day traces with richer counterfactual interventions;
- live viewer driven by model actions rather than replay frames.

## Artifacts

- [script](../experiments/ssrm_3d_multiday_maturation.py)
- [package](../experiments/ssrm_maturation/)
- [evaluation CSV](../artifacts/ssrm_3d_multiday_maturation_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_multiday_maturation_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_multiday_maturation_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_multiday_maturation_trace.json)
- [results JSON](../artifacts/ssrm_3d_multiday_maturation_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_multiday_maturation_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_multiday_maturation_results.js)
