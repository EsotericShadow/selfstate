# Hidden Viability Survival Report

## Purpose

This experiment tests self as a long-horizon control variable.

The agent can earn external reward by working, but working consumes hidden energy and damages hidden integrity. Rest and repair preserve future ability to act. Exact internal state is only available through an inspect action, and symptom signals arrive late.

The question is:

> Does tracking "my future internal state" improve survival and reward when future outcomes depend on hidden viability variables?

## Command

```bash
python3 experiments/hidden_viability_survival.py --episodes 500 --seed 20260530 --horizon 80
```

Outputs:

- `artifacts/hidden_viability_summary.csv`
- `artifacts/hidden_viability_results.json`

## Agents

| Agent | Description |
|---|---|
| task-only world reward | Always works. No internal-state model. |
| fixed schedule memory | Uses a pre-set work/rest/repair rhythm. No internal-state observations. |
| symptom reactive | Reacts only to late low-energy or low-integrity signals. |
| self-state ablation | Inspects and estimates internal state, but policy cannot use the estimate. |
| persistent self-state | Maintains energy/integrity estimates and uses them to choose work/rest/repair/inspect. |
| oracle self-state | Knows true energy, integrity, and current hidden dynamics. |

## Results

| Scenario | Agent | Survival | Steps | Reward | Total value |
|---|---|---:|---:|---:|---:|
| low stress | task-only world reward | 1.000 | 80.000 | 798.934 | 798.934 |
| low stress | persistent self-state | 1.000 | 80.000 | 674.900 | 674.900 |
| energy stress | task-only world reward | 0.000 | 10.388 | 93.649 | -6.351 |
| energy stress | fixed schedule memory | 0.000 | 56.360 | 379.327 | 279.327 |
| energy stress | symptom reactive | 1.000 | 80.000 | 435.842 | 435.842 |
| energy stress | self-state ablation | 0.000 | 11.338 | 93.136 | -6.864 |
| energy stress | persistent self-state | 1.000 | 80.000 | 558.387 | 558.387 |
| energy stress | oracle self-state | 1.000 | 80.000 | 610.000 | 610.000 |
| damage stress | task-only world reward | 0.000 | 17.260 | 153.100 | 53.100 |
| damage stress | fixed schedule memory | 0.000 | 68.988 | 451.526 | 351.526 |
| damage stress | symptom reactive | 1.000 | 80.000 | 464.844 | 464.844 |
| damage stress | self-state ablation | 0.000 | 19.260 | 153.100 | 53.100 |
| damage stress | persistent self-state | 1.000 | 80.000 | 575.560 | 575.560 |
| damage stress | oracle self-state | 1.000 | 80.000 | 640.000 | 640.000 |
| combined drift | task-only world reward | 0.000 | 18.818 | 165.365 | 65.365 |
| combined drift | fixed schedule memory | 1.000 | 80.000 | 560.000 | 560.000 |
| combined drift | symptom reactive | 0.172 | 55.786 | 336.136 | 253.336 |
| combined drift | self-state ablation | 0.000 | 20.610 | 163.363 | 63.363 |
| combined drift | persistent self-state | 1.000 | 80.000 | 539.955 | 539.955 |
| combined drift | oracle self-state | 1.000 | 80.000 | 586.760 | 586.760 |

## Interpretation

This supports self as control variable under hidden internal-state pressure.

In low stress, self-state is unnecessary and costly. The task-only agent survives and earns more reward than the persistent self-state policy because inspection and conservative maintenance waste actions.

In energy and damage stress, the persistent self-state policy survives all episodes and earns substantially more total value than task-only, fixed schedule, symptom-reactive, and self-state-ablation policies.

The ablation is the causal check. It inspects and estimates energy/integrity, but cannot use those estimates for action. Under energy, damage, and combined stress, it dies in every episode. That means the value is not merely in observing internal state; it is in using persistent internal-state estimates for control.

The combined-drift scenario preserves an important alternative. A conservative fixed schedule survives and earns slightly more value than the inspecting self-state policy. This shows explicit self-state is not universally necessary. A pre-baked rhythm can solve a predictable viability regime, though it fails under pure energy and damage stress where the self-state policy succeeds.

## Current Claim Update

The evidence now supports a conditional claim:

> A self-equivalent control variable becomes useful when future reward and survival depend on hidden internal viability variables whose state must be preserved through time.

It does not support the stronger claim:

> Every long-horizon adaptive system must explicitly represent itself.

The stronger claim remains open because fixed schedules, symptom policies, and future learned predictive-state systems may solve some viability problems without a separable self abstraction.

## Next Step

The next pressure to test is coherence and identity continuity:

- interrupt an agent mid-plan;
- corrupt or compress memory;
- resume under changed internal state;
- measure whether a persistent self/commitment index improves continuation without contradiction.
