# SSRM-3D Return-Selected Hidden-Regime Controller Report

## Question

Report 96 improved hidden-regime response with a learned option head, but it still used a fixed action-bias setting. This report asks whether closed-loop validation return can select a better controller setting before held-out evaluation.

The narrow question is:

```text
Can validation return choose a better option-action bias for a learned hidden-regime controller, while preserving the 12h gate and improving held-out hidden-regime response?
```

## What changed

The controller is the same option-gated neural controller family from Report 96:

- `option_frame`
- `option_gru`

The new step is return selection:

1. Train the option-gated neural controller from designed hidden-regime traces.
2. Run closed-loop validation worlds with several option-bias values.
3. Select the bias with the best validation objective.
4. Evaluate the selected controller on separate held-out worlds.
5. Compare against fixed-bias GRU, frame model, reactive survival-only control, and ablations.

The model still receives symptom/state streams, not hidden regime labels.

## What this does not claim

This is not proof of consciousness. It is not open-ended civilization. It is not gradient deep reinforcement learning.

It is return-shaped policy selection: validation return chooses the action-bias setting for a learned controller.

## Canonical command

```bash
python3 experiments/ssrm_3d_return_selected_hidden_regime_controller.py --train-seeds 20260718,20260719,20260720,20260721,20260722,20260723,20260724,20260725 --tune-seeds 20260808,20260809,20260810,20260811,20260812 --eval-seeds 20260813,20260814,20260815,20260816,20260817 --bias-candidates 0.70,1.00,1.35,1.70,2.10 --hours 16 --step-hours 0.08 --population 10 --epochs 100 --hidden-size 56 --device auto --trace-seed 20260813
```

## Bias Selection

| option bias | validation score | response | targeted response | objective | selected |
|---:|---:|---:|---:|---:|---|
| 0.70 | 0.760 | 0.836 | 0.575 | 0.906 | true |
| 1.00 | 0.748 | 0.843 | 0.514 | 0.890 | false |
| 1.35 | 0.723 | 0.815 | 0.514 | 0.862 | false |
| 1.70 | 0.720 | 0.805 | 0.525 | 0.859 | false |
| 2.10 | 0.713 | 0.778 | 0.545 | 0.850 | false |

The selected option bias is `0.70`.

## Canonical result

The return-selected controller passes the defined Report 97 gate:

- return-selected GRU score: `0.766`;
- fixed-bias GRU score: `0.720`;
- option frame score: `0.753`;
- reactive survival-only score: `0.336`;
- gain over fixed bias: `0.045`;
- gain over frame: `0.012`;
- gain over reactive: `0.430`;
- no major hidden regime before `12h`: `1.000`;
- hidden regime active after `12h`: `1.000`;
- response score: `0.839`;
- targeted response rate: `0.616`.

The verdict is:

```text
supports_return_selection = true
supports_ablation_specificity = true
verdict = pass
```

## Ablations

| ablation | score loss | response loss | inference loss |
|---|---:|---:|---:|
| `regime_signal` | 0.118 | 0.181 | 0.005 |
| `infrastructure` | 0.310 | 0.344 | 0.009 |
| `social_culture` | -0.002 | 0.000 | -0.007 |
| `body` | 0.213 | 0.255 | 0.007 |

Positive:

- removing regime signal now hurts total score and response;
- removing infrastructure strongly hurts total score and response;
- removing body state strongly hurts total score and response;
- return-selected GRU beats the fixed-bias GRU and the frame model on held-out worlds.

Remaining weakness:

- social/culture ablation is still not stable; it does not meaningfully reduce score.

## Trace checkpoints

The return-selected GRU trace for held-out seed `20260813` uses the `tool_fatigue` hidden regime:

| checkpoint | active | alive | last option | dominant belief | inference | response | targeted response | architecture | tool design | knowledge transfer |
|---|---|---:|---|---|---:|---:|---:|---:|---:|---:|
| `1h` | false | 10 | `infrastructure` | `tool` | 0.078 | 0.334 | 0.000 | 0.381 | 0.160 | 0.000 |
| `6h` | false | 10 | `social` | `tool` | 0.119 | 0.383 | 0.000 | 0.565 | 0.275 | 0.827 |
| `12h` | false | 10 | `social` | `food` | 0.048 | 0.838 | 0.000 | 0.591 | 0.978 | 0.827 |
| `12.5h` | false | 10 | `social` | `food` | 0.046 | 0.845 | 0.000 | 0.595 | 1.000 | 0.827 |
| `14.5h` | true | 10 | `tool` | `food` | 0.092 | 0.840 | 0.478 | 0.603 | 1.000 | 0.827 |
| `16h` | true | 10 | `tool` | `tool` | 0.186 | 0.840 | 0.668 | 0.603 | 1.000 | 0.827 |

## Interpretation

This is the strongest learned hidden-regime result in the repo so far.

It does not prove consciousness or open-ended selfhood. It does show a more serious scientific shape:

- agents develop for 12h before major hidden-regime pressure;
- hidden regimes activate after the gate;
- a learned controller acts closed-loop;
- validation return selects a better policy setting;
- held-out performance improves over fixed bias, frame model, and reactive control;
- regime-signal, infrastructure, and body ablations create specific failures.

The next threshold is stronger return-trained control: optimize model parameters from simulated return, not only select a policy setting after imitation training.

## Artifacts

- [script](../experiments/ssrm_3d_return_selected_hidden_regime_controller.py)
- [training CSV](../artifacts/ssrm_3d_return_selected_hidden_regime_controller_training.csv)
- [bias selection CSV](../artifacts/ssrm_3d_return_selected_hidden_regime_controller_bias_selection.csv)
- [evaluation CSV](../artifacts/ssrm_3d_return_selected_hidden_regime_controller_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_return_selected_hidden_regime_controller_summary.csv)
- [ablation CSV](../artifacts/ssrm_3d_return_selected_hidden_regime_controller_ablations.csv)
- [verdict CSV](../artifacts/ssrm_3d_return_selected_hidden_regime_controller_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_return_selected_hidden_regime_controller_trace.json)
- [results JSON](../artifacts/ssrm_3d_return_selected_hidden_regime_controller_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_return_selected_hidden_regime_controller_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_return_selected_hidden_regime_controller_results.js)
