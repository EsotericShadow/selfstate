# Online Predictive Learning Report

## Purpose

This experiment tests whether self-equivalent action-effect state can be learned from prediction error without labels.

The learner observes:

```text
action -> observed effect
```

It does not receive labels such as self, body, actuator, gain, wind, or world drift. It updates predictive parameters online and then uses those parameters for control.

## Command

```bash
python3 experiments/online_predictive_learning.py --episodes 500 --seed 20260530 --max-action 15 --calibration-steps 14 --control-steps 12
```

Outputs:

- `artifacts/online_predictive_learning_summary.csv`
- `artifacts/online_predictive_learning_results.json`

## Models

| Model | Prediction form | Interpretation |
|---|---|---|
| bias-only world | `delta = action + bias` | world-only external drift learner |
| gain-only action effect | `delta = gain * action` | action-effect learner |
| affine predictive state | `delta = gain * action + bias` | learned action-effect plus external-bias state |
| action-table memory | remembered effects for sampled actions | non-parametric memory baseline |

The learned `gain` is not labeled as self. It is only the action-dependent component of a prediction-error learner.

## Results

| Scenario | Model | Policy | Success | Mean final distance | Gain error | Bias error |
|---|---|---|---:|---:|---:|---:|
| static goal switch | affine predictive state | full model | 1.000 | 0.000 | 0.000 | 0.000 |
| world drift | bias-only world | full model | 1.000 | 0.000 | 0.000 | 0.047 |
| world drift | affine predictive state | full model | 1.000 | 0.000 | 0.003 | 0.041 |
| self drift | bias-only world | full model | 0.576 | 64.278 | 0.953 | 2.316 |
| self drift | gain-only action effect | full model | 1.000 | 0.000 | 0.174 | 0.000 |
| self drift | affine predictive state | full model | 0.984 | 0.349 | 0.152 | 0.496 |
| self drift | affine predictive state | action-component ablation | 0.698 | 63.595 | 0.152 | 0.496 |
| mixed hidden | bias-only world | full model | 0.616 | 54.505 | 0.778 | 1.894 |
| mixed hidden | gain-only action effect | full model | 0.972 | 1.118 | 0.146 | 1.011 |
| mixed hidden | affine predictive state | full model | 0.976 | 0.353 | 0.123 | 0.406 |
| mixed hidden | affine predictive state | action-component ablation | 0.732 | 54.105 | 0.123 | 0.406 |

## Interpretation

The bias-only world model succeeds under pure world drift and fails under self drift. It cannot represent changed action-effect state.

The gain-only action-effect model succeeds under self drift. It learns a parameter that is statistically equivalent to hidden actuator/body state, but it is learned only from prediction error.

The affine predictive-state model succeeds in mixed hidden regimes because it can represent both action-effect state and external bias.

The causal ablation is the important check. In self drift, the affine full model succeeds at 0.984 with mean final distance 0.349. Removing the learned action component drops success to 0.698 and raises mean final distance to 63.595, matching no-state identity behavior.

This supports:

> A self-equivalent variable can emerge as the action-dependent component of online prediction-error learning.

It does not require a module named self.

## Limits

This is still a simple linear learner in a simple linear world. It is learned online, but the feature family is still designed.

The result strengthens the implicit-self account more than the explicit-self account. It shows that self-equivalent information can be learned and causally useful without becoming a symbolic self-object.

## Next Step

Replace the linear learners with richer recurrent or model-based agents and test whether the same action-effect, viability, and continuity variables remain decodable and causally necessary.
