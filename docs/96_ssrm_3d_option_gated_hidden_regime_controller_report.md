# SSRM-3D Option-Gated Hidden-Regime Controller Report

## Question

Report 95 proved a learned controller could act closed-loop, but the ablation result was weak. This report asks whether adding a learned response-option head makes the hidden-regime controller more causally sensitive to regime signals.

The narrow question is:

```text
Can an option-gated neural controller use symptom/history streams to improve closed-loop hidden-regime response while preserving the 12h development gate?
```

## What changed

The controller now predicts two things from the same observation stream:

- an action;
- a response option.

The response options are:

- `survival`
- `water`
- `weather`
- `food`
- `tool`
- `social`
- `infrastructure`
- `teaching`

The option prediction biases action selection during closed-loop evaluation. For example, a `tool` option biases toward tool redesign, inspection, construction, and teaching. A `water` option biases toward filtering, quarantine, water collection, and inspection.

The model still does not receive a hidden regime label as input.

## What this does not claim

This is not proof of consciousness. It is not open-ended civilization. It is not return-trained deep reinforcement learning. The option groups are designed affordances, not discovered concepts.

This is a cleaner learned closed-loop precursor than Report 95, not a solved selfhood or civilization result.

## Canonical command

```bash
python3 experiments/ssrm_3d_option_gated_hidden_regime_controller.py --train-seeds 20260718,20260719,20260720,20260721,20260722,20260723,20260724,20260725 --eval-seeds 20260803,20260804,20260805,20260806,20260807 --hours 16 --step-hours 0.08 --population 10 --epochs 100 --hidden-size 56 --device auto --trace-seed 20260803
```

## Training

| architecture | action accuracy | option accuracy | loss | device | parameters |
|---|---:|---:|---:|---|---:|
| `option_frame` | 0.337 | 0.461 | 4.645 | `mps` | 7,748 |
| `option_gru` | 0.354 | 0.471 | 4.580 | `mps` | 20,964 |

## Canonical result

The option-gated GRU gets a partial result:

- option GRU score: `0.729`;
- option frame score: `0.794`;
- reactive survival-only score: `0.336`;
- option GRU gain over reactive: `0.393`;
- option GRU gain over frame: `-0.065`;
- no major hidden regime before `12h`: `1.000`;
- hidden regime active after `12h`: `1.000`;
- option GRU inference score: `0.222`;
- option GRU response score: `0.800`;
- option GRU targeted response rate: `0.554`.

Compared with Report 95, the GRU improves:

- long-horizon score: `0.687` to `0.729`;
- response score: `0.690` to `0.800`;
- targeted response rate: `0.371` to `0.554`.

The verdict is:

```text
supports_option_gated_learning_precursor = true
supports_ablation_specificity = false
verdict = partial
```

## Ablations

The ablations are more informative than Report 95, but still not a full pass:

| ablation | score loss | response loss | inference loss |
|---|---:|---:|---:|
| `regime_signal` | 0.059 | 0.111 | -0.005 |
| `infrastructure` | 0.271 | 0.301 | 0.021 |
| `social_culture` | -0.011 | -0.022 | -0.003 |
| `body` | 0.097 | 0.187 | -0.008 |

Positive:

- removing regime signal now hurts total score and response;
- removing infrastructure strongly hurts total score and response;
- removing body state hurts response.

Negative:

- social/culture ablation is still not clean;
- inference loss is not regime-signal-specific;
- the frame model still beats the recurrent model.

## Trace checkpoints

The option-GRU trace for held-out seed `20260803` uses the `tool_fatigue` hidden regime:

| checkpoint | active | alive | last option | dominant belief | inference | response | targeted response | architecture | tool design | knowledge transfer |
|---|---|---:|---|---|---:|---:|---:|---:|---:|---:|
| `1h` | false | 10 | `infrastructure` | `tool` | 0.078 | 0.334 | 0.000 | 0.381 | 0.160 | 0.000 |
| `6h` | false | 10 | `social` | `tool` | 0.121 | 0.371 | 0.000 | 0.563 | 0.258 | 0.843 |
| `12h` | false | 10 | `social` | `food` | 0.066 | 0.472 | 0.000 | 0.563 | 0.416 | 0.843 |
| `12.5h` | false | 10 | `social` | `food` | 0.058 | 0.487 | 0.000 | 0.563 | 0.437 | 0.843 |
| `14.5h` | true | 10 | `tool` | `food` | 0.080 | 0.557 | 0.300 | 0.563 | 0.571 | 0.843 |
| `16h` | true | 10 | `tool` | `tool` | 0.165 | 0.802 | 0.415 | 0.563 | 0.895 | 0.843 |

## Interpretation

This is real progress over Report 95 but still not the endpoint.

The option head gives the learned controller a better way to route pressure into action. It improves hidden-regime response and makes regime-signal removal matter. That is the right direction for a scientific simulation: the environment changes, symptoms matter, and removing those symptom/history channels causes a measurable response failure.

The remaining weakness is just as important. The frame model still scores higher, and the social/culture ablation is not stable. That means the current recurrent state is not yet a clean learned integration mechanism.

The next gate is return-trained control or model-based policy improvement, not more visual detail.

## Artifacts

- [script](../experiments/ssrm_3d_option_gated_hidden_regime_controller.py)
- [training CSV](../artifacts/ssrm_3d_option_gated_hidden_regime_controller_training.csv)
- [evaluation CSV](../artifacts/ssrm_3d_option_gated_hidden_regime_controller_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_option_gated_hidden_regime_controller_summary.csv)
- [ablation CSV](../artifacts/ssrm_3d_option_gated_hidden_regime_controller_ablations.csv)
- [verdict CSV](../artifacts/ssrm_3d_option_gated_hidden_regime_controller_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_option_gated_hidden_regime_controller_trace.json)
- [results JSON](../artifacts/ssrm_3d_option_gated_hidden_regime_controller_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_option_gated_hidden_regime_controller_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_option_gated_hidden_regime_controller_results.js)
