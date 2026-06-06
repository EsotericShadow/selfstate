# SSRM-3D Learned Multi-Day Maturation Controller Report

## Question

Report 103 made the 72h maturation world measurable, but the integrated controller was still hand-designed. This report asks whether a learned neural controller can act closed-loop in that same multi-day world.

The narrow question is:

```text
Can a neural action selector trained from maturation traces preserve the 12h shock gate, survive post-gate shocks, develop tools/buildings, transmit knowledge, and beat reactive control when its own actions feed back into the world?
```

## What Changed

This experiment trains two action selectors from teacher traces generated in the Report 103 maturation world:

- `frame_mlp`: sees the current observation frame only;
- `gru`: sees the same observation stream with recurrent state.

Evaluation is closed loop. The model chooses each living agent's action, then those actions change future resources, health, infrastructure, tools, culture, births, and recovery.

The observation vector includes:

- agent body and capability state;
- time and 12h gate state;
- resources;
- infrastructure;
- tools;
- social/culture variables;
- environmental pressure;
- previous action.

No condition label is supplied to the learned controller.

## What This Does Not Claim

This is supervised imitation from a designed controller. It is not deep reinforcement learning. It is not open-ended civilization. It is not evidence of subjective consciousness.

## Canonical Command

```bash
python3 experiments/ssrm_3d_learned_multiday_maturation_controller.py --train-seeds 20260911,20260912,20260913,20260914,20260915,20260916 --eval-seeds 20260921,20260922,20260923,20260924,20260925 --hours 72 --step-hours 0.10 --population 14 --epochs 42 --hidden-size 64 --device auto --trace-seed 20260921
```

## Canonical Result

The learned GRU preserves the long-run development behavior:

- GRU maturation score: `1.000`;
- frame MLP score: `0.847`;
- designed-controller score: `1.000`;
- reactive score: `0.462`;
- GRU gain over reactive: `0.538`;
- GRU gain over frame: `0.153`;
- shock-gate pass rate: `1.000`;
- post-gate shock rate: `1.000`;
- alive at `12h`: `14.0`.

The model was trained on `70,827` action steps. Training accuracy is low in ordinary classifier terms (`0.263` for GRU), but closed-loop return is high because the learned policy recovers the broad action schedule well enough to keep the society developing.

## Ablation Boundary

The strong claim still fails:

| Ablation | Score loss |
|---|---:|
| `body` | `0.284` |
| `infrastructure` | `0.285` |
| `tools` | `0.195` |
| `social_culture` | `0.000` |
| `environment` | `0.018` |
| `previous_action` | `0.000` |

This means the learned controller clearly uses body, infrastructure, and tool channels, but it does not yet show clean dependence on social/culture state, environmental state, or previous-action history. The recurrent controller beats the frame model, but the recurrence is not yet proven to rely on the previous-action channel.

The verdict is:

```text
supports_learned_maturation_control = true
supports_recurrent_advantage = true
supports_ablation_specificity = false
verdict = partial_or_failed
```

## Interpretation

This is a real step toward the requested long-running simulation:

- actions are selected by a learned neural model;
- the learned actions run closed-loop for 72h;
- the 12h major-shock gate still holds;
- post-gate shocks happen;
- the world still develops architecture, tools, births, and knowledge transfer;
- the GRU beats both reactive control and frame-only learned control.

But it is not the final target. The next stronger version needs return-trained control or actor-critic training inside the maturation world, not only imitation. It also needs harder social/environmental tests where social culture, weather, contamination, route danger, and prior action cannot be ignored without visible failure.

## Artifacts

- [script](../experiments/ssrm_3d_learned_multiday_maturation_controller.py)
- [training CSV](../artifacts/ssrm_3d_learned_multiday_maturation_training.csv)
- [evaluation CSV](../artifacts/ssrm_3d_learned_multiday_maturation_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_learned_multiday_maturation_summary.csv)
- [ablation CSV](../artifacts/ssrm_3d_learned_multiday_maturation_ablations.csv)
- [verdict CSV](../artifacts/ssrm_3d_learned_multiday_maturation_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_learned_multiday_maturation_trace.json)
- [results JSON](../artifacts/ssrm_3d_learned_multiday_maturation_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_learned_multiday_maturation_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_learned_multiday_maturation_results.js)
