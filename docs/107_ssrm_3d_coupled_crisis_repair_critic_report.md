# SSRM-3D Coupled Crisis Repair Critic Report

## Question

Report 106 showed a sharp failure: a learned GRU plus return-selected router can keep a 72h population maturing, but it does not repair coupled crises where environmental damage and social coordination must be handled together.

This report tests the next smallest repair:

```text
Can a learned repair critic around the GRU improve coupled social/environment crisis repair?
```

## What Changed

The benchmark keeps the Report 106 72h coupled-crisis world:

- crises begin only after the 12h development gate;
- each crisis requires environmental response and social coordination;
- the learned controller receives ordinary symptom features, not the active crisis label.

The new component is a small neural repair critic:

- the base frame MLP and GRU are still trained by supervised imitation over 72h maturation traces;
- the pressure router is still selected by closed-loop validation return;
- the repair critic is trained from active-crisis repair targets derived from crisis progress gaps;
- closed-loop validation then selects a repair-bias strength before held-out evaluation.

The critic can bias the GRU toward actions such as `sanitize`, `treat`, `scout`, `construct`, `social_repair`, `teach`, or `learn` when ordinary symptoms imply repair pressure.

## What This Does Not Claim

This is not deep reinforcement learning. The repair critic is supervised and then selected by validation return. It does not update the policy by actor-critic, policy gradient, or model-based return inside the world.

It also does not claim subjective consciousness, open-ended civilization, or real-world competence. It is a bounded test of whether a supervised repair reranker is enough to improve the specific coupled-crisis failure.

## Canonical Command

```bash
python3 experiments/ssrm_3d_coupled_crisis_repair_critic_controller.py --train-seeds 20260911,20260912,20260913,20260914,20260915,20260916 --tune-seeds 20260981,20260982,20260983 --eval-seeds 20261001,20261002,20261003,20261004,20261005 --hours 72 --step-hours 0.10 --population 14 --epochs 42 --hidden-size 64 --repair-epochs 70 --repair-hidden-size 48 --device auto --trace-seed 20261001
```

## Result

The validation sweep selected:

```text
selected_router = social_env
selected_repair_bias = 0.0
```

That means the repair critic was trained and evaluated, but the validation world rejected every nonzero repair-bias setting.

Held-out summary:

| Controller | Total score | Maturation | Crisis score | Resolved rate | Coupled response |
|---|---:|---:|---:|---:|---:|
| designed | `0.878` | `1.000` | `0.747` | `1.000` | `0.514` |
| return-selected GRU | `0.519` | `0.999` | `0.000` | `0.150` | `0.017` |
| repair-critic GRU | `0.518` | `0.997` | `0.000` | `0.150` | `0.017` |
| base GRU | `0.518` | `0.997` | `0.000` | `0.000` | `0.000` |
| frame MLP | `0.330` | `0.635` | `0.000` | `0.000` | `0.000` |
| reactive | `0.240` | `0.462` | `0.000` | `0.000` | `0.000` |

The trained repair critic did not improve the coupled-crisis score. It preserved the same weak crisis behavior as the return-selected GRU because the selected repair bias was zero.

## Training Boundary

The repair critic saw `30243` active-crisis training examples.

```text
train_accuracy = 0.328
weighted_accuracy = 0.330
```

That is weak action prediction for a repair reranker. The failure is not just a threshold issue. The critic does not learn a useful enough repair-action map from supervised labels alone.

## Ablation Boundary

The stronger dependency claim also fails:

| Ablation | Total loss | Crisis loss | Coupled response loss |
|---|---:|---:|---:|
| `social_culture` | `0.000` | `0.000` | `0.017` |
| `environment` | `0.004` | `0.000` | `0.017` |
| `infrastructure` | `0.187` | `0.000` | `0.017` |
| `tools` | `0.008` | `0.000` | `0.017` |
| `body` | `0.009` | `0.000` | `0.010` |
| `previous_action` | `0.000` | `0.000` | `-0.065` |

Since the full repair-critic controller still has `0.000` crisis score, social/culture and environment ablations cannot show a clean crisis-score dependency.

The verdict is:

```text
supports_repair_critic = false
supports_social_environment_dependency = false
verdict = partial_or_failed
```

## Interpretation

This is a useful negative result.

Report 101 showed that a supervised repair critic could improve a narrower social-repair task while still failing the strong claim. Report 107 shows that the same idea does not carry to the 72h coupled social/environment crisis world.

The practical lesson is sharper:

```text
supervised repair labels plus validation-selected bias are not enough for coupled crisis repair
```

The next controller needs outcome-aware learning:

- train from coupled-crisis return or counterfactual outcomes, not only repair labels;
- add a value or critic head that predicts unresolved crisis damage;
- make wrong social-only and wrong environment-only responses consume the recovery window more explicitly;
- train or search over action sequences, not only per-step repair labels;
- evaluate held-out crisis schedules/maps and require social/environment ablations to damage crisis score.

## Artifacts

- [script](../experiments/ssrm_3d_coupled_crisis_repair_critic_controller.py)
- [base training CSV](../artifacts/ssrm_3d_coupled_crisis_repair_critic_base_training.csv)
- [repair training CSV](../artifacts/ssrm_3d_coupled_crisis_repair_critic_repair_training.csv)
- [router selection CSV](../artifacts/ssrm_3d_coupled_crisis_repair_critic_router_selection.csv)
- [repair selection CSV](../artifacts/ssrm_3d_coupled_crisis_repair_critic_repair_selection.csv)
- [evaluation CSV](../artifacts/ssrm_3d_coupled_crisis_repair_critic_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_coupled_crisis_repair_critic_summary.csv)
- [ablation CSV](../artifacts/ssrm_3d_coupled_crisis_repair_critic_ablations.csv)
- [verdict CSV](../artifacts/ssrm_3d_coupled_crisis_repair_critic_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_coupled_crisis_repair_critic_trace.json)
- [results JSON](../artifacts/ssrm_3d_coupled_crisis_repair_critic_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_coupled_crisis_repair_critic_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_coupled_crisis_repair_critic_results.js)
