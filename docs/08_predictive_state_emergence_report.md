# Predictive-State Emergence Report

## Purpose

The first two experiments still supplied relatively structured candidate forms. This experiment removes explicit self and world variables from the learner.

The learner only builds a predictive state:

```text
action -> expected effect
```

Then post-hoc probes ask whether hidden agent-state and external state are decodable from that predictive state, and causal ablations test whether the decoded components matter for control.

## Command

```bash
python3 experiments/predictive_state_emergence.py --episodes 500 --seed 20260530 --max-action 15 --calibration-samples 7 --control-horizon 10
```

Outputs:

- `artifacts/predictive_state_probe_summary.csv`
- `artifacts/predictive_state_control_summary.csv`
- `artifacts/predictive_state_emergence_results.json`

## Learner

For each post-perturb episode, the learner observes calibration pairs:

```text
action, observed_delta
```

It creates counterfactual predictions for the full action range. This vector is the learned predictive state. It is not labeled as self, world, body, actuator, gain, or wind.

Probe latents:

- `constant`: no predictive state;
- `mean_effect`: average predicted effect;
- `three_predictions`: predicted effects for negative, zero, and positive actions;
- `full_predictions`: predicted effects for the full action range.

## Decodability Results

Train/test split: 400/100 episodes per scenario.

| Scenario | Latent | Target | Test MAE | R2 | Baseline MAE |
|---|---|---|---:|---:|---:|
| self drift | constant | gain | 0.870 | -0.000 | 0.870 |
| self drift | mean effect | gain | 0.870 | -0.000 | 0.870 |
| self drift | three predictions | gain | 0.000 | 1.000 | 0.870 |
| self drift | full predictions | gain | 0.000 | 1.000 | 0.870 |
| mixed hidden | constant | gain | 0.770 | -0.007 | 0.770 |
| mixed hidden | mean effect | gain | 0.769 | -0.005 | 0.770 |
| mixed hidden | three predictions | gain | 0.000 | 1.000 | 0.770 |
| mixed hidden | full predictions | gain | 0.000 | 1.000 | 0.770 |
| world drift | constant | wind | 1.506 | -0.007 | 1.506 |
| world drift | mean effect | wind | 0.000 | 1.000 | 1.506 |
| mixed hidden | constant | wind | 1.061 | -0.009 | 1.061 |
| mixed hidden | mean effect | wind | 0.000 | 1.000 | 1.061 |

Blank R2 values in the CSV indicate no target variance, for example wind in the pure self-drift scenario.

## Control Ablation Results

| Scenario | Policy | Success | Mean final distance | Mean total loss |
|---|---|---:|---:|---:|
| static goal switch | no-state identity | 1.000 | 0.000 | 16.500 |
| static goal switch | full predictive state | 1.000 | 0.000 | 16.500 |
| world drift | no-state identity | 1.000 | 1.518 | 31.395 |
| world drift | self-component ablation | 1.000 | 0.000 | 18.445 |
| world drift | world-component ablation | 1.000 | 1.518 | 31.395 |
| world drift | full predictive state | 1.000 | 0.000 | 18.445 |
| self drift | no-state identity | 0.698 | 54.540 | 367.012 |
| self drift | self-component ablation | 0.698 | 54.540 | 367.012 |
| self drift | world-component ablation | 1.000 | 0.000 | 25.136 |
| self drift | full predictive state | 1.000 | 0.000 | 25.136 |
| mixed hidden | no-state identity | 0.572 | 47.241 | 319.254 |
| mixed hidden | self-component ablation | 0.744 | 46.397 | 314.276 |
| mixed hidden | world-component ablation | 1.000 | 1.168 | 32.879 |
| mixed hidden | full predictive state | 1.000 | 0.000 | 24.781 |

`self-component ablation` forces the action-effect slope back to the fixed-body assumption while retaining estimated external bias. `world-component ablation` removes external bias while retaining the learned action-effect slope.

## Interpretation

This is stronger than the representation-search result in one important respect: the learner is not selecting a model named `self_gain`. It is learning action-conditioned predictions. A self-equivalent variable is then decodable from the shape of those predictions.

The critical pattern:

- mean effect decodes external drift but not actuator gain;
- three counterfactual action predictions decode actuator gain perfectly in self-drift and mixed-hidden scenarios;
- ablating the action-effect component reproduces no-state behavior in self drift;
- keeping the action-effect component while removing world bias preserves self-drift control.

This supports:

> A self-equivalent state can emerge as the action-contingent component of a predictive state.

It does not require a symbolic self-object. It only requires that the system predict how its own actions will change future observations.

## Limits

This remains a toy linear environment. The predictive state is interpretable because the action/effect function is simple.

The result does not show phenomenal consciousness, subjective continuity, narrative identity, or human-like selfhood.

It also does not prove universal necessity. In static and pure world-drift cases, simpler representations remain sufficient.

## Next Step

Increase pressure toward a persistent self:

- add hidden viability variables such as energy, damage, fatigue, and repair;
- make those variables evolve across long horizons;
- require the agent to choose information-gathering actions when it is uncertain about its own state;
- test whether predictive-state variables remain stable across tasks and not only within one action-effect episode.
