# SSRM-3D Hidden-Regime Adaptation Report

## Question

Report 93 verified the 12h development gate headlessly. This report asks whether the world can become more scientific by changing its hidden causal rules after that gate while withholding the regime label from the agents.

The narrow question is:

```text
After 12 simulated hours of development, can agents adapt to hidden world-rule changes using symptoms, memory, teaching, reputation/influence, tools, sanitation, and weather perception?
```

## What changed

The benchmark adds five hidden regimes:

- `contaminated_water`: illness and contamination rise from water symptoms;
- `cold_wet_season`: exposure, storms, shelter wear, and route hazard rise;
- `crop_blight`: food reliability falls and garden pressure rises;
- `tool_fatigue`: tools fail faster and material pressure rises;
- `trust_fracture`: trust falls while conflict, inequality, and symbol instability rise.

The agents do not receive these regime names as inputs. They receive noisy symptom channels:

- water illness and contamination;
- weather exposure and storm damage;
- food yield and migration pressure;
- tool breakage and material strain;
- conflict, trust, inequality, and convention instability.

## What this does not claim

This is not proof of consciousness. It is not open-ended civilization. It is not closed-loop deep reinforcement learning. It is a designed hidden-regime pressure verifier.

## Canonical command

```bash
python3 experiments/ssrm_3d_hidden_regime_adaptation.py --seeds 20260713,20260714,20260715,20260716,20260717 --hours 16 --step-hours 0.05 --population 10 --trace-seed 20260713
```

## Conditions

- `integrated_hidden_regime`
- `reactive_survival_only`
- `no_regime_inference`
- `no_teaching_transmission`
- `no_reputation_influence`
- `no_sanitation_memory`
- `no_weather_sensors`
- `no_tool_adaptation`

## Canonical result

The integrated condition passes the hidden-regime gate:

- no major hidden regime before `12h`: `1.000`;
- hidden regime active after `12h`: `1.000`;
- mean alive at `12h`: `10.0`;
- mean final alive: `10.6`;
- mean long-horizon score: `0.773`;
- mean response score: `0.848`;
- mean inference score: `0.205`;
- mean targeted response rate after hidden-regime activation: `0.347`;
- mean architecture delta: `0.799`;
- mean tool-design delta: `0.681`;
- mean knowledge transfer: `1.000`;
- mean symbol convergence: `1.000`.

The verdict is:

```text
supports_hidden_regime_adaptation = true
supports_ablation_specificity = true
verdict = pass
```

## Ablation losses

The losses are deliberately pressure-specific:

- reactive survival only: score loss `0.434`;
- no regime inference: inference loss `0.139`;
- no teaching transmission: culture loss `0.680`;
- no reputation/influence in the trust-fracture regime: response loss `0.468`;
- no sanitation memory in the contaminated-water regime: response loss `0.029`;
- no weather sensors in the cold/wet regime: response loss `0.014`;
- no tool adaptation in the tool-fatigue regime: response loss `0.550`.

## Important nuance

The `no_regime_inference` condition does not collapse in total score. Broad development still helps agents survive and respond generically. What drops is the causal-diagnosis channel: mean inference score falls from `0.205` to `0.067`.

That is the right boundary. This report supports hidden-regime pressure as a testable mechanism, not a claim that diagnosis is already necessary for every kind of survival.

## Trace checkpoints

The integrated trace for seed `20260713` uses the `tool_fatigue` hidden regime:

| checkpoint | active | alive | tool quality | tool design | dominant belief | inference | response | targeted response |
|---|---|---:|---:|---:|---|---:|---:|---:|
| `1h` | false | 10 | 0.465 | 0.160 | `tool` | 0.077 | 0.335 | 0.000 |
| `6h` | false | 10 | 0.521 | 0.270 | `food` | 0.106 | 0.371 | 0.000 |
| `12h` | false | 10 | 0.801 | 0.575 | `food` | 0.053 | 0.577 | 0.000 |
| `12.5h` | false | 10 | 0.832 | 0.607 | `food` | 0.051 | 0.600 | 0.000 |
| `14.5h` | true | 10 | 0.856 | 0.728 | `tool` | 0.103 | 0.663 | 0.413 |
| `16h` | true | 10 | 0.866 | 0.815 | `tool` | 0.204 | 0.705 | 0.410 |

## Interpretation

This adds a more scientific version of "make them wise":

- the world changes after a long development period;
- the change is hidden;
- agents see symptoms, not labels;
- success requires recovery, development, culture, and targeted response;
- ablations remove one causal channel at a time;
- the artifact records both positive and weak boundaries.

The strongest next gate is to move this hidden-regime layer into a learned closed-loop controller with held-out worlds.

## Artifacts

- [script](../experiments/ssrm_3d_hidden_regime_adaptation.py)
- [evaluation CSV](../artifacts/ssrm_3d_hidden_regime_adaptation_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_hidden_regime_adaptation_summary.csv)
- [regime summary CSV](../artifacts/ssrm_3d_hidden_regime_adaptation_regime_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_hidden_regime_adaptation_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_hidden_regime_adaptation_trace.json)
- [results JSON](../artifacts/ssrm_3d_hidden_regime_adaptation_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_hidden_regime_adaptation_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_hidden_regime_adaptation_results.js)
