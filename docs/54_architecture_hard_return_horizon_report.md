# Architecture Hard-Return Horizon Report

## Purpose

This experiment follows report 53.

The hard-return audit showed that realized task return alone keeps controls clean but does not produce strict architecture-wide recovery of the self and detachable boundary signatures at horizon 8. This sweep asks whether longer temporal dependence repairs that failure.

The audit is deliberately bounded. It uses a smaller optimizer budget than report 53 so that the question is:

> Does horizon pressure improve hard-return boundary discovery under the same objective?

not:

> Can unlimited search eventually find the boundary?

## Question

Does increasing horizon make hard realized-return optimization converge on the expected boundary signatures without a smooth expected-return surrogate?

## Design

For each horizon in `2,4,8,16`, each scenario, and each architecture, the experiment:

1. optimizes recurrent weights from Gaussian starts;
2. ranks candidates only by realized recurrent training return;
3. selects restarts only by realized recurrent training return;
4. selects among recurrent, local-probe, greedy, and safe policies by realized return;
5. applies the same end-to-end boundary classifier used in reports 48 to 53.

No source-direction seeds, smooth expected-return surrogate, or boundary-aware restart selection is used.

## Command

```bash
python3 experiments/architecture_hard_return_horizon_sweep.py --horizons 2,4,8,16 --episodes 180 --training-episodes 240 --seed 20260603 --evidence-samples 9 --cue-accuracy 0.85 --iterations 8 --population 120 --restarts 5 --initial-std 1.4
```

## Current Result

| Scenario | Convergence by horizon | Strict at any horizon | Result |
|---|---|---|---|
| `self_persistent_boundary` | `2:0/3;4:1/3;8:1/3;16:1/3` | No | Horizon improves only to partial self-boundary convergence. |
| `detachable_tool_world` | `2:0/3;4:1/3;8:1/3;16:1/3` | No | Horizon improves only to partial detachable-boundary convergence. |
| `passive_world_boundary` | `2:0/3;4:3/3;8:3/3;16:3/3` | Yes | Horizon recovers passive external recurrence. |
| `independent_hidden` | `2:3/3;4:3/3;8:3/3;16:3/3` | Yes | Controls reject shared recurrence. |
| `irrelevant_control` | `2:3/3;4:3/3;8:3/3;16:3/3` | Yes | Controls reject hidden state. |

## Interpretation

Longer horizon helps hard-return optimization find useful recurrent structure, but it does not solve the boundary-discovery problem for self and detachable-tool regimes.

The important distinction is:

- passive external recurrence becomes easy under longer horizon;
- controls remain clean;
- self and detachable boundary signatures still do not become architecture-wide.

So horizon pressure is real but insufficient under this objective. The result strengthens the negative lesson from report 53:

> Task reward and temporal pressure can favor recurrence without forcing the causal boundary abstraction needed to distinguish self-equivalent state from other useful hidden state.

Report 55 tests a different objective-only learner. Sampled-return perturbation updates still leave all shared regimes only partially convergent. Report 56 then shows that stochastic policy-gradient credit assignment can recover the missing boundary signatures in this toy benchmark.

## Falsifiers And Strengtheners

The limitation weakens if:

- larger hard-return budgets produce strict self and detachable convergence across horizons;
- richer recurrent architectures recover the missing boundary effects under hard return;
- online RL discovers the same boundary signatures without the smooth surrogate.

The current theory strengthens if:

- hard-return learners continue to need causal boundary tests even as horizon increases;
- soft/model-based objectives recover the missing self/tool signatures while hard return remains partial;
- richer environments reproduce the distinction between useful hidden-state control and boundary-equivalent self-state.

## Artifacts

- [experiment script](../experiments/architecture_hard_return_horizon_sweep.py)
- [summary CSV](../artifacts/architecture_hard_return_horizon_summary.csv)
- [verdict CSV](../artifacts/architecture_hard_return_horizon_verdict.csv)
- [JSON results](../artifacts/architecture_hard_return_horizon_results.json)
