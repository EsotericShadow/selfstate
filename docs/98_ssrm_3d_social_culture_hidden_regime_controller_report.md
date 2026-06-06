# SSRM-3D Social/Culture Hidden-Regime Controller Report

## Question

Report 97 passed its bounded hidden-regime gate, but its social/culture ablation did not matter. This report attacks that weakness directly.

The narrow question is:

```text
Can a learned closed-loop controller handle delayed hidden social/culture regimes without receiving a regime label, and does removing social/culture state cause a specific loss?
```

## What changed

The experiment keeps the 12h development gate and learned option-gated controller family, but changes the hidden regimes.

Instead of mixing water, weather, food, tool, and social regimes, every held-out world receives a hidden social/culture regime after the 12h gate:

- `trust_fracture`;
- `symbol_drift`;
- `coalition_split`;
- `teacher_loss`;
- `rumor_cascade`.

All variants share the same broad social symptom channel. The model does not receive the variant name. Recovery depends on trust, conflict, social inequality, reputation accuracy, symbol convergence, teaching, culture memory, knowledge transfer, and recent world state.

The teacher traces were also corrected after a diagnostic run: post-shock social examples are weighted more heavily, and the random world seed is paired across selected, fixed, frame, and ablated controllers so comparisons are not caused by different sampled worlds.

## What this does not claim

This is not proof of consciousness. It is not open-ended society formation. It is not full deep reinforcement learning.

It is a learned closed-loop controller trained from designed social recovery traces, with return selection over an option-action bias.

## Canonical command

```bash
python3 experiments/ssrm_3d_social_culture_hidden_regime_controller.py --train-seeds 20260818,20260819,20260820,20260821,20260822,20260823,20260824,20260825 --tune-seeds 20260828,20260829,20260830,20260831,20260832 --eval-seeds 20260833,20260834,20260835,20260836,20260837 --bias-candidates 0.70,1.00,1.35,1.70,2.10 --hours 16 --step-hours 0.08 --population 10 --epochs 100 --hidden-size 56 --device auto --trace-seed 20260833
```

## Bias Selection

| option bias | validation score | social response | variant targeted | objective | selected |
|---:|---:|---:|---:|---:|---|
| 0.70 | 0.712 | 0.814 | 0.400 | 0.882 | true |
| 1.00 | 0.712 | 0.814 | 0.400 | 0.882 | false |
| 1.35 | 0.712 | 0.814 | 0.400 | 0.882 | false |
| 1.70 | 0.711 | 0.814 | 0.400 | 0.882 | false |
| 2.10 | 0.711 | 0.814 | 0.400 | 0.881 | false |

The selected option bias is `0.70`.

## Canonical result

The result is a useful partial boundary, not a clean pass:

- return-selected social GRU score: `0.711`;
- fixed-bias GRU score: `0.711`;
- option frame score: `0.708`;
- reactive survival-only score: `0.288`;
- gain over reactive: `0.424`;
- no major hidden regime before `12h`: `1.000`;
- hidden regime active after `12h`: `1.000`;
- social response score: `0.815`;
- variant-targeted response rate: `0.400`.

The verdict is:

```text
supports_social_culture_controller = true
supports_social_culture_ablation = false
verdict = partial
```

## Ablations

| ablation | score loss | social response loss | targeted loss | culture loss |
|---|---:|---:|---:|---:|
| `regime_signal` | 0.029 | 0.003 | 0.000 | -0.002 |
| `social_culture` | 0.026 | -0.049 | 0.058 | 0.170 |
| `memory` | 0.044 | -0.002 | -0.141 | 0.321 |
| `body` | 0.010 | -0.123 | -0.117 | -0.008 |

Positive:

- the learned controller preserves the 12h gate;
- hidden social/culture regimes activate after the gate;
- the learned GRU beats reactive control by `0.424`;
- return selection chooses the best validation bias;
- removing social/culture state reduces total score and culture score;
- removing broader memory reduces total score and knowledge transfer.

Weakness:

- social/culture ablation does not reduce social response score in the canonical held-out set;
- variant-targeted response remains low at `0.400`;
- the controller is still relying on broad social recovery habits rather than cleanly separating all hidden social variants;
- fixed-bias and frame controls remain close to the selected GRU.

## Variant boundary

The held-out variants show the current failure shape:

| variant | full score | full response | full targeted | social/culture ablated score | social/culture ablated response | social/culture ablated targeted |
|---|---:|---:|---:|---:|---:|---:|
| `coalition_split` | 0.651 | 0.718 | 0.000 | 0.716 | 0.916 | 0.535 |
| `rumor_cascade` | 0.646 | 0.723 | 0.000 | 0.762 | 0.956 | 0.513 |
| `symbol_drift` | 0.813 | 0.971 | 1.000 | 0.660 | 0.881 | 0.000 |
| `teacher_loss` | 0.789 | 0.901 | 1.000 | 0.536 | 0.569 | 0.000 |
| `trust_fracture` | 0.658 | 0.762 | 0.000 | 0.753 | 1.000 | 0.660 |

That is not a clean social intelligence result. The controller handles teach-heavy variants better than mediate-heavy variants, and the ablated model can accidentally improve some mediate-heavy cases.

## Interpretation

This report makes the benchmark more scientific by turning "social dynamics" into a falsifiable hidden-regime pressure:

- no social variant labels in model input;
- delayed post-12h activation;
- paired held-out worlds for model comparisons;
- specific ablations for social/culture, memory, regime signal, and body state;
- positive and negative evidence recorded as a completed result.

The main value is the boundary it exposes. Social/culture pressure is now present, but the learned controller has not yet separated mediation regimes from teaching regimes reliably enough. The next threshold is a stronger social credit-assignment benchmark where trust repair, rumor correction, convention repair, teaching, and coalition repair have mutually exclusive opportunity costs.

## Artifacts

- [script](../experiments/ssrm_3d_social_culture_hidden_regime_controller.py)
- [training CSV](../artifacts/ssrm_3d_social_culture_hidden_regime_controller_training.csv)
- [bias selection CSV](../artifacts/ssrm_3d_social_culture_hidden_regime_controller_bias_selection.csv)
- [evaluation CSV](../artifacts/ssrm_3d_social_culture_hidden_regime_controller_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_social_culture_hidden_regime_controller_summary.csv)
- [variant summary CSV](../artifacts/ssrm_3d_social_culture_hidden_regime_controller_variant_summary.csv)
- [ablation CSV](../artifacts/ssrm_3d_social_culture_hidden_regime_controller_ablations.csv)
- [verdict CSV](../artifacts/ssrm_3d_social_culture_hidden_regime_controller_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_social_culture_hidden_regime_controller_trace.json)
- [results JSON](../artifacts/ssrm_3d_social_culture_hidden_regime_controller_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_social_culture_hidden_regime_controller_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_social_culture_hidden_regime_controller_results.js)
