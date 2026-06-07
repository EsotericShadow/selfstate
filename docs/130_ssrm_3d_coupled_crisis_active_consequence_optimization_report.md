# SSRM-3D Coupled Crisis Active Consequence Optimization Report

## Question

Report 129 showed that direct supervised labels from cloned counterfactual
windows still do not transfer into reliable online crisis repair. Validation
selected direct bias `0.0`, and held-out crisis score, resolved rate, and
coupled response all remained `0.000`.

This report tests the next narrower claim:

```text
If the crisis controller is optimized from completed downstream consequences,
can it preserve coupled environmental/social repair after the engineered
weakest-channel planner is removed?
```

The benchmark keeps the hard setting:

- `96h` worlds;
- no major crisis before `12h`;
- randomized post-gate crisis timing, order, repetition, and initial pressure;
- learned base GRU;
- learned environmental and social action heads;
- recurrent consequence-recovery policy;
- delayed active policy-gradient fine-tuning from completed crisis returns;
- learned action-value scoring from consequence-labeled crisis traces;
- targeted social/environment ablations.

This is still bounded evidence. Candidate crisis actions, crisis families,
world variables, and the consequence reward are supplied. It is not open-ended
civilization, subjective consciousness, mature deep reinforcement learning, or
real-world competence.

## Canonical Command

```bash
python3 experiments/ssrm_3d_coupled_crisis_active_consequence_optimization_controller.py --train-seeds 20260911,20260912,20260913 --tune-seeds 20261111,20261112 --eval-seeds 20261121,20261122,20261123 --hours 96 --step-hours 0.10 --population 14 --epochs 14 --hidden-size 48 --action-epochs 18 --action-hidden-size 48 --consequence-epochs 8 --consequence-hidden-size 48 --consequence-return-scale 1.15 --student-iterations 0 --active-epochs 3 --active-learning-rate 0.0018 --active-entropy-coef 0.006 --active-training-bias 0.40 --action-value-epochs 8 --action-value-hidden-size 64 --action-value-learning-rate 0.003 --policy-bias-candidates 0.0,0.40,0.80 --active-bias-candidates 0.0,0.40,0.80 --device auto --trace-seed 20261121
```

## What Changed

Report 130 tests two consequence-driven routes after the Report 129 supervised
label failure.

First, it initializes from the Report 126 consequence-recovery recurrent
policy and fine-tunes it with sampled crisis-window actions. The policy is
updated only after a completed crisis, using reward from downstream coupled
repair, resolved progress, response balance, and damage.

Second, it trains a learned action-value controller on the same
consequence-labeled crisis traces. Instead of imitating one label or accepting
one delayed policy-gradient update, this model scores each candidate crisis
action from state features and completed-window consequence targets, then
chooses the highest-scored action online.

Neither path is a free-form agent. The action vocabulary is supplied, the
environment is still a compact benchmark, and the learned controller is tested
only inside this simulated crisis task.

## Training Result

The behavior-source consequence policy again trains cleanly:

| Metric | Value |
|---|---:|
| source sequences | `114` |
| student sequences | `0` |
| aggregate examples | `143384` |
| consequence train accuracy | `0.994` |
| consequence weighted accuracy | `0.994` |

The delayed active policy-gradient path trains across completed crises, but the
return signal is noisy:

| Metric | Value |
|---|---:|
| active training crises | `57` |
| active mean return | `1.011` |
| return std | `2.686` |
| mean sequence length | `1210.088` |
| selected active bias | `0.0` |

The learned action-value controller fits the consequence targets tightly:

| Metric | Value |
|---|---:|
| value examples | `143384` |
| value epochs | `8` |
| mean target return | `0.353` |
| positive target rate | `0.404` |
| train MAE | `0.253` |
| weighted train MAE | `0.075` |
| selected value bias | `0.0` |

This means the offline consequence signal is learnable. The held-out question
is whether it creates better online control.

## Held-Out Result

| Controller | Total score | Crisis score | Resolved rate | Env response | Social response | Coupled response |
|---|---:|---:|---:|---:|---:|---:|
| designed | `0.830` | `0.694` | `1.000` | `0.720` | `0.660` | `0.451` |
| min-channel planner GRU | `0.529` | `0.020` | `0.411` | `0.410` | `1.000` | `0.410` |
| fixed joint GRU | `0.524` | `0.021` | `0.411` | `0.410` | `1.000` | `0.410` |
| consequence-recovery GRU | `0.520` | `0.000` | `0.356` | `0.355` | `1.000` | `0.355` |
| active consequence-value GRU | `0.501` | `0.000` | `0.244` | `0.210` | `0.420` | `0.081` |
| return-selected GRU | `0.487` | `0.000` | `0.056` | `0.299` | `0.084` | `0.040` |
| active consequence-optimized GRU | `0.484` | `0.000` | `0.067` | `0.299` | `0.094` | `0.060` |
| base GRU | `0.290` | `0.000` | `0.000` | `0.299` | `0.000` | `0.000` |
| frame MLP | `0.287` | `0.000` | `0.000` | `0.299` | `0.000` | `0.000` |
| reactive | `0.090` | `0.000` | `0.000` | `0.280` | `0.000` | `0.000` |

The verdict is:

```text
mean_crisis_count = 5.667
selected_active_bias = 0.0
selected_action_value_bias = 0.0
supports_active_consequence_optimization = false
supports_learned_action_value_control = false
supports_teacher_transfer = false
supports_social_environment_dependency = false
verdict = partial_or_failed
```

## Interpretation

This is a partial negative boundary.

The delayed policy-gradient route is worse than the Report 126
consequence-recovery baseline. It raises some active response over
return-selected, but total score falls to `0.484`, resolved rate stays at
`0.067`, and coupled response is only `0.060`.

The learned action-value route is more useful, but still not enough. It beats
the weak return-selected GRU by `0.014` total score and raises resolved rate
from `0.056` to `0.244`. It also raises coupled response from `0.040` to
`0.081`. But it remains below the consequence-recovery GRU, which reaches
`0.520` total score, `0.356` resolved rate, and `0.355` coupled response.

So the result is not a solved learned crisis controller. It says:

```text
Consequence-value learning helps compared with weak return-selected control,
but this action-level value critic still cannot preserve robust coupled repair
after the structured planner is removed.
```

## Ablation Boundary

The value controller has some social/environment dependence, but it is too weak
to support the strong claim because the base crisis score is already `0.000`.

| Ablation | Total score | Total loss | Crisis score | Coupled response | Coupled loss |
|---|---:|---:|---:|---:|---:|
| none | `0.501` | - | `0.000` | `0.081` | - |
| body | `0.478` | `0.023` | `0.000` | `0.000` | `0.081` |
| infrastructure | `0.410` | `0.091` | `0.000` | `0.000` | `0.081` |
| tools | `0.268` | `0.233` | `0.000` | `0.001` | `0.079` |
| social_culture | `0.473` | `0.028` | `0.000` | `0.000` | `0.081` |
| environment | `0.484` | `0.017` | `0.000` | `0.000` | `0.081` |
| previous_action | `0.520` | `-0.019` | `0.000` | `0.102` | `-0.021` |

Both social/culture and environment ablations remove the value controller's
small coupled response, but the crisis-score gate remains failed. This is a
causal hint, not a strong learned-integration result.

## Boundary

Report 130 rules out a tempting shortcut:

```text
It is not enough to add delayed policy-gradient fine-tuning or a learned
single-action consequence-value scorer on top of the existing recurrent
policy.
```

The next useful step is not another supervised label pass. It is a true
multi-step consequence optimizer: the learned controller must evaluate and
commit to action sequences under its own interventions, with explicit pressure
to keep environmental and social repair active together while minimizing
damage and avoiding one-channel shortcuts.
