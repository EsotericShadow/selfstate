# Minimal Experiment Report

## Purpose

This is the first executable test of the self/world attribution hypothesis.

It does not test consciousness. It does not test verbal self-report. It tests whether a controller benefits from representing its own hidden actuator state separately from external drift.

## Command

```bash
python3 experiments/self_world_attribution.py --episodes 500 --seed 20260530 --max-action 15
```

Outputs:

- `artifacts/self_world_attribution_summary.csv`
- `artifacts/self_world_attribution_results.json`

## Environment

The agent controls position on a one-dimensional line. It observes position and target, but not the hidden causes of motion.

Hidden variables:

- `gain`: agent-internal actuator state. The same command can move normally, weakly, strongly, or in reverse.
- `wind`: external drift. The world can add movement independent of the command.

Transition:

```text
position_{t+1} = position_t + gain * action_t + wind
```

The target flips at the perturbation step. Depending on the scenario, the hidden actuator state, external drift, both, or neither may also change.

## Agents

### Reactive World-Only

Uses current position and target. Assumes command effects are stable.

### World-Drift-Only

Can estimate external drift but assumes its own actuator gain is always normal.

### History Action Table

Stores observed effects of specific actions. It has memory and can adapt without representing a separate self-state.

### Factorized Self/World

Fits:

```text
delta = gain_hat * action + wind_hat
```

Here `gain_hat` is a minimal self-equivalent variable: a persistent estimate of the agent's own action-effect state.

### Self-State Ablation

Uses the same factorized estimator, but control is forced to ignore `gain_hat`. This is a causal intervention on the self-equivalent variable.

### Oracle

Knows the true hidden `gain` and `wind`. This is a ceiling, not a plausible architecture.

## Results

500 episodes per agent per scenario.

Episode seeds are stable per scenario and episode index, so each agent faces the same hidden-state sequence within a scenario.

| Scenario | Agent | Post-success | Mean recovery steps | Mean post-distance | Mean total loss |
|---|---:|---:|---:|---:|---:|
| static goal switch | reactive world-only | 1.000 | 4.000 | 3.750 | 109.500 |
| static goal switch | world-drift-only | 1.000 | 4.000 | 3.750 | 201.420 |
| static goal switch | history action table | 1.000 | 4.000 | 3.750 | 200.220 |
| static goal switch | self-state ablation | 1.000 | 4.000 | 3.750 | 201.060 |
| static goal switch | factorized self/world | 1.000 | 4.000 | 3.750 | 201.060 |
| static goal switch | oracle | 1.000 | 4.000 | 3.750 | 109.500 |
| world drift | reactive world-only | 1.000 | 4.454 | 5.116 | 143.775 |
| world drift | world-drift-only | 1.000 | 4.454 | 3.932 | 206.174 |
| world drift | history action table | 1.000 | 9.952 | 7.230 | 285.683 |
| world drift | self-state ablation | 1.000 | 4.454 | 4.014 | 208.165 |
| world drift | factorized self/world | 1.000 | 4.454 | 4.004 | 207.886 |
| world drift | oracle | 1.000 | 4.454 | 3.825 | 112.778 |
| self drift | reactive world-only | 0.660 | 7.012 | 88.519 | 2150.619 |
| self drift | world-drift-only | 0.000 |  | 56.820 | 1482.840 |
| self drift | history action table | 0.672 | 8.976 | 13.948 | 447.150 |
| self drift | self-state ablation | 0.000 |  | 56.820 | 1482.840 |
| self drift | factorized self/world | 1.000 | 8.000 | 12.251 | 407.090 |
| self drift | oracle | 1.000 | 5.000 | 4.897 | 137.708 |
| mixed hidden | reactive world-only | 0.664 | 6.792 | 78.108 | 2249.180 |
| mixed hidden | world-drift-only | 0.440 | 6.650 | 28.125 | 956.665 |
| mixed hidden | history action table | 0.744 | 9.860 | 13.507 | 466.889 |
| mixed hidden | self-state ablation | 0.436 | 6.202 | 27.868 | 950.434 |
| mixed hidden | factorized self/world | 1.000 | 7.424 | 10.789 | 381.380 |
| mixed hidden | oracle | 1.000 | 4.998 | 4.787 | 143.864 |

## Interpretation

### What the result supports

The factorized self/world agent is not needed in the static case. When the actuator is stable, reactive control is enough.

The factorized self/world agent is also not uniquely needed for pure world drift. A world-drift model handles that case.

The self-state variable becomes useful when the agent's own actuator gain changes. In the self-drift scenario, world-drift-only control has 0.000 post-success, reactive control has 0.660, the non-factorized action table has 0.672, and the factorized self/world agent reaches 1.000.

The self-state ablation is the key causal check. It estimates `gain_hat`, but control cannot use it. In self drift, post-success drops from 1.000 to 0.000. In mixed hidden, it drops from 1.000 to 0.436. In world drift and static goal switching, the ablation does not hurt. That pattern is what the hypothesis predicts: the self-equivalent variable matters only when hidden agent-state matters.

The mixed-hidden scenario is the strongest current support. When both self and world hidden variables can matter, factorization into `gain_hat` and `wind_hat` reaches 1.000 post-success and lower total loss than the history action table.

This supports the weak claim:

> When future outcomes depend on hidden, changing properties of the agent itself, control improves when the system encodes information equivalent to agent-state.

### What the result does not support

This does not prove that explicit selfhood is necessary.

The history action table is a serious non-self baseline. It stores action effects without representing an explicit self/world split and still performs reasonably. In smaller action spaces, this kind of lower-level mechanism can match or outperform a factorized self model.

This also does not show spontaneous emergence. The factorization is supplied by the architecture. A stronger experiment must train agents without self labels and test whether self-equivalent variables emerge anyway.

The oracle gap remains large. Even the factorized agent is far from optimal because calibration and change-point detection are simple.

## Current Conclusion

The first experiment supports conditional usefulness, not universal necessity.

A persistent self-equivalent variable becomes valuable when:

- the agent's own action-effect state is hidden;
- that state changes through time;
- external and internal causes can both explain prediction error;
- the action space is large enough that per-action history is less compressed;
- future control depends on distinguishing "the world changed" from "I changed."

It also preserves the failure path:

If future learned agents solve the same tasks with compact, causally effective non-self predictive state, then explicit selfhood is optional rather than necessary.

## Next Experimental Step

Replace the hand-coded factorized agent with learned agents:

- recurrent policy without self labels;
- recurrent policy with bottleneck;
- predictive-state model;
- structured self/world bottleneck;
- causal probes to test whether hidden actuator state is decodable and behaviorally necessary.
