# SSRM-3D Learned Hidden-Regime Controller Report

## Question

Report 94 tested hidden world-rule changes with a designed controller. This report asks whether a neural controller can be trained from symptom histories and then act inside the hidden-regime world.

The narrow question is:

```text
Can an imitation-trained recurrent neural controller act closed-loop for 16 simulated hours, preserve the 12h development gate, survive hidden regime changes, develop tools and infrastructure, and outperform a reactive survival baseline?
```

## What changed

This benchmark adds a learned controller layer on top of the hidden-regime world:

- a `frame_mlp` controller trained from individual observation frames;
- a `gru` controller trained from recurrent observation sequences;
- closed-loop evaluation where model actions modify the future world state;
- held-out seeds covering contaminated water, cold/wet season, crop blight, tool fatigue, and trust fracture;
- observation ablations for symptoms, memory, social/culture, infrastructure, and body state.

The model input does not include a hidden regime label. It sees body state, skill state, resources, infrastructure, social/culture state, symptom channels, memory/culture variables, time features, and previous action.

## What this does not claim

This is not proof of consciousness. It is not open-ended civilization. It is not return-trained deep reinforcement learning. Training is imitation learning from a designed controller.

The evaluation is closed-loop: the learned model acts in the world and its actions change later resources, health, trust, architecture, tools, teaching, and hidden-regime response.

## Canonical command

```bash
python3 experiments/ssrm_3d_learned_hidden_regime_controller.py --train-seeds 20260718,20260719,20260720,20260721,20260722,20260723,20260724,20260725 --eval-seeds 20260783,20260784,20260785,20260786,20260787 --hours 16 --step-hours 0.08 --population 10 --epochs 80 --hidden-size 48 --device auto --trace-seed 20260783
```

## Training

| architecture | train accuracy | loss | device | parameters |
|---|---:|---:|---|---:|
| `frame_mlp` | 0.343 | 1.724 | `mps` | 5,868 |
| `gru` | 0.348 | 1.714 | `mps` | 16,428 |

## Canonical result

The recurrent controller gets a partial result:

- GRU closed-loop score: `0.687`;
- frame MLP closed-loop score: `0.758`;
- reactive survival-only score: `0.336`;
- GRU gain over reactive: `0.351`;
- GRU gain over frame: `-0.071`;
- no major hidden regime before `12h`: `1.000`;
- hidden regime active after `12h`: `1.000`;
- mean alive at `12h`: `10.0`;
- mean final alive: `10.0`;
- GRU inference score: `0.263`;
- GRU response score: `0.690`;
- GRU targeted response rate: `0.371`;
- GRU architecture delta: `0.393`;
- GRU tool-design delta: `0.272`;
- GRU knowledge transfer: `0.880`.

The verdict is:

```text
supports_closed_loop_learning_precursor = true
supports_ablation_specificity = false
verdict = partial
```

## Ablations

The ablations do not support a strong recurrent-integration claim:

| ablation | score loss | response loss | inference loss |
|---|---:|---:|---:|
| `symptoms` | -0.067 | -0.136 | 0.046 |
| `memory` | -0.008 | -0.066 | 0.050 |
| `social_culture` | 0.023 | 0.074 | -0.007 |
| `infrastructure` | 0.107 | 0.262 | -0.023 |
| `body` | -0.010 | 0.088 | -0.004 |

Infrastructure ablation hurts the controller. Social/culture ablation causes a smaller loss. But symptom and memory ablations are not clean: removing them sometimes improves total score because the learned policy falls back into broad construction and teaching behavior.

## Trace checkpoints

The integrated GRU trace for held-out seed `20260783` uses the `tool_fatigue` hidden regime:

| checkpoint | active | alive | dominant belief | inference | response | targeted response | architecture | tool design | knowledge transfer |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| `1h` | false | 10 | `tool` | 0.078 | 0.334 | 0.000 | 0.383 | 0.160 | 0.000 |
| `6h` | false | 10 | `tool` | 0.128 | 0.321 | 0.000 | 0.566 | 0.205 | 0.891 |
| `12h` | false | 10 | `tool` | 0.144 | 0.348 | 0.000 | 0.566 | 0.309 | 0.891 |
| `12.5h` | true | 10 | `tool` | 0.147 | 0.343 | 0.000 | 0.566 | 0.312 | 0.891 |
| `14.5h` | true | 10 | `tool` | 0.239 | 0.325 | 0.308 | 0.566 | 0.357 | 0.891 |
| `16h` | true | 10 | `tool` | 0.369 | 0.287 | 0.243 | 0.566 | 0.360 | 0.891 |

## Interpretation

This is a useful boundary result.

Positive:

- the learned GRU acts closed-loop, not just as a replay;
- it preserves the 12h development gate;
- it survives hidden-regime activation;
- it improves tools and infrastructure;
- it transfers knowledge;
- it beats reactive survival-only control by a wide margin.

Negative:

- the frame MLP is stronger than the GRU in this run;
- training accuracy is low;
- ablations do not prove clean recurrent symptom-memory dependence;
- symptom removal can improve total score through broad construction behavior;
- this is imitation learning, not return-trained deep RL.

The next gate is not more decoration. It is a cleaner learned-controller setup:

- train from return or model-based rollouts, not only imitation;
- separate action heads for survival, construction, teaching, and regime response;
- evaluate longer than 16h with more held-out worlds;
- make symptom and memory ablations pressure-specific by regime;
- compare against frame, recurrent, reactive, designed, and oracle controllers.

## Artifacts

- [script](../experiments/ssrm_3d_learned_hidden_regime_controller.py)
- [training CSV](../artifacts/ssrm_3d_learned_hidden_regime_controller_training.csv)
- [evaluation CSV](../artifacts/ssrm_3d_learned_hidden_regime_controller_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_learned_hidden_regime_controller_summary.csv)
- [ablation CSV](../artifacts/ssrm_3d_learned_hidden_regime_controller_ablations.csv)
- [verdict CSV](../artifacts/ssrm_3d_learned_hidden_regime_controller_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_learned_hidden_regime_controller_trace.json)
- [results JSON](../artifacts/ssrm_3d_learned_hidden_regime_controller_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_learned_hidden_regime_controller_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_learned_hidden_regime_controller_results.js)
