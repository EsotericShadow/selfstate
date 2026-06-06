# SSRM-3D Return-Selected Multi-Day Maturation Controller Report

## Question

Report 104 showed that a GRU imitation controller can run the 72h maturation world closed-loop, but it was still selected by supervised action copying. This report adds a small return-selected layer around that GRU.

The narrow question is:

```text
Can closed-loop validation return select a pressure-router setting that preserves 72h maturation and improves dependence on social/environmental pressure channels?
```

## What Changed

The experiment keeps the Report 104 GRU controller, then evaluates candidate pressure routers on validation worlds.

Each router adds action-logit bias from sensed pressure:

- social pressure biases `social_repair` and `teach`;
- environmental pressure biases `sanitize`, `treat`, and `scout`;
- infrastructure pressure biases `construct`;
- tool pressure biases `improve_tools`;
- teaching pressure biases `teach` and `learn`.

The selected router is then evaluated on held-out seeds.

This is return selection, not deep reinforcement learning. The controller still starts from supervised imitation. The selection step is closed-loop because candidate routers are chosen by how the world develops after their actions feed back into the simulation.

## What This Does Not Claim

This does not prove open-ended civilization, subjective consciousness, or fully autonomous discovery of social/environmental concepts. The pressure router is still a designed adapter around a learned model.

## Canonical Command

```bash
python3 experiments/ssrm_3d_return_selected_multiday_maturation_controller.py --train-seeds 20260911,20260912,20260913,20260914,20260915,20260916 --tune-seeds 20260931,20260932,20260933 --eval-seeds 20260941,20260942,20260943,20260944,20260945 --hours 72 --step-hours 0.10 --population 14 --epochs 42 --hidden-size 64 --device auto --trace-seed 20260941
```

## Router Selection

Validation return selected:

```text
selected_router = social_env
```

The selected router had:

- social bias: `1.55`;
- environment bias: `1.45`;
- infrastructure bias: `0.75`;
- tool bias: `0.70`;
- teaching bias: `1.20`;
- validation score: `1.000`;
- validation births: `5.333`;
- selection objective: `1.108`.

## Held-Out Result

On held-out seeds:

- selected score: `1.000`;
- base GRU score: `1.000`;
- designed-controller score: `1.000`;
- frame score: `0.771`;
- reactive score: `0.462`;
- gain over frame: `0.229`;
- gain over reactive: `0.538`;
- gap to designed: `0.000`;
- shock-gate pass rate: `1.000`;
- post-gate shock rate: `1.000`;
- alive at `12h`: `14.0`.

The return-selected router preserves the long-run development pattern, but it does not improve total score over the already-saturated base GRU.

## Ablation Boundary

The strong pressure-ablation claim still fails:

| Ablation | Total score loss |
|---|---:|
| `body` | `0.030` |
| `infrastructure` | `0.312` |
| `tools` | `0.002` |
| `social_culture` | `0.000` |
| `environment` | `0.000` |
| `previous_action` | `0.000` |

There are local development losses under some masks, but total maturation score remains saturated under social/culture and environment ablations. That means the current world still allows compensating routes around those channels.

The verdict is:

```text
supports_return_selection = true
supports_pressure_ablation_specificity = false
verdict = partial_or_failed
```

## Interpretation

This report makes one useful move:

- the learned controller is no longer accepted only because it imitates the teacher;
- a router is selected by closed-loop validation outcome;
- the selected router generalizes to held-out 72h worlds and preserves the 12h shock gate.

But it also exposes the next bottleneck clearly:

```text
The maturation world is still too forgiving for social/culture and environment channels.
```

If the agent can ignore those channels and still reach full maturation score, the world is not yet forcing realistic enough adaptation. The next stronger benchmark should add social/environmental shocks that cannot be solved by generic building/tool/teaching routines:

- contagious misinformation or trust breakdown that blocks cooperation unless social repair is targeted;
- weather/resource regimes that change locally and punish stale environmental sensing;
- tool and building failures whose cause is ambiguous between weather, misuse, disease, and social neglect;
- migration or quarantine decisions where social trust and environmental evidence must be combined.

## Artifacts

- [script](../experiments/ssrm_3d_return_selected_multiday_maturation_controller.py)
- [training CSV](../artifacts/ssrm_3d_return_selected_multiday_maturation_training.csv)
- [selection CSV](../artifacts/ssrm_3d_return_selected_multiday_maturation_selection.csv)
- [evaluation CSV](../artifacts/ssrm_3d_return_selected_multiday_maturation_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_return_selected_multiday_maturation_summary.csv)
- [ablation CSV](../artifacts/ssrm_3d_return_selected_multiday_maturation_ablations.csv)
- [verdict CSV](../artifacts/ssrm_3d_return_selected_multiday_maturation_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_return_selected_multiday_maturation_trace.json)
- [results JSON](../artifacts/ssrm_3d_return_selected_multiday_maturation_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_return_selected_multiday_maturation_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_return_selected_multiday_maturation_results.js)
