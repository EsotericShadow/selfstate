# Architecture Policy-Gradient Seed Sweep Report

## Purpose

This experiment audits report 56.

The policy-gradient learner recovered strict boundary convergence for one seed. That is useful evidence, but it leaves a direct robustness question:

> Does the result survive independent seeds?

This sweep repeats the same learner across five seeds and reports strict convergence by seed. It does not average away failed cells.

## Question

Is stochastic policy-gradient boundary discovery seed-stable across recurrent architectures?

## Design

For each seed in `20260605,20260606,20260607,20260608,20260609`, each scenario, and each recurrent architecture, the experiment:

1. trains the same stochastic recurrent policy-gradient learner used in report 56;
2. selects restarts by sampled validation return;
3. selects among recurrent, local-probe, greedy, and safe policies by realized return;
4. applies the same end-to-end boundary classifier;
5. reports architecture convergence per seed and strict-seed counts per scenario.

The support criterion is deliberately conservative:

- shared regimes must recover more than half of all architecture-seed cells and at least one strict seed;
- controls must remain strict in every seed.

## Command

```bash
python3 experiments/architecture_policy_gradient_seed_sweep.py --seeds 20260605,20260606,20260607,20260608,20260609 --episodes 200 --training-episodes 400 --validation-episodes 240 --batch-episodes 128 --horizon 8 --evidence-samples 9 --cue-accuracy 0.85 --epochs 32 --restarts 5 --temperature 1.8 --learning-rate 0.12 --lr-decay 0.96 --initial-std 0.8 --finite-diff-epsilon 0.02 --max-grad-norm 4.0
```

## Current Result

| Scenario | Convergence by seed | Strict seeds | Seed-sweep result |
|---|---|---:|---|
| `self_persistent_boundary` | `20260605:3/3;20260606:3/3;20260607:2/3;20260608:2/3;20260609:2/3` | 2/5 | Partial shared robustness. |
| `detachable_tool_world` | `20260605:3/3;20260606:3/3;20260607:2/3;20260608:1/3;20260609:3/3` | 3/5 | Partial shared robustness. |
| `passive_world_boundary` | `20260605:3/3;20260606:2/3;20260607:2/3;20260608:3/3;20260609:3/3` | 3/5 | Partial shared robustness. |
| `independent_hidden` | `20260605:3/3;20260606:3/3;20260607:3/3;20260608:3/3;20260609:3/3` | 5/5 | Stable rejection of shared recurrence. |
| `irrelevant_control` | `20260605:3/3;20260606:3/3;20260607:3/3;20260608:3/3;20260609:3/3` | 5/5 | Stable rejection of hidden state. |

Total architecture-seed convergence:

| Scenario | Converged cells |
|---|---:|
| `self_persistent_boundary` | 12/15 |
| `detachable_tool_world` | 12/15 |
| `passive_world_boundary` | 13/15 |
| `independent_hidden` | 15/15 |
| `irrelevant_control` | 15/15 |

## Interpretation

This is mixed evidence.

The positive part is important: policy-gradient learning repeatedly discovers the expected boundary signatures in most shared architecture-seed cells, and both controls remain perfectly clean across all five seeds.

The negative part is equally important: strict architecture-wide convergence is not seed-stable. Report 56 should not be read as proving that policy-gradient learning inevitably discovers the self/tool/passive boundary. It shows recoverability under sampled-return credit assignment. Report 57 shows that recoverability is still sensitive to seed and architecture.

The current claim should therefore be:

> Policy-gradient credit assignment can recover self-equivalent boundary structure under sampled return, but the result is not yet a seed-stable attractor law.

Report 58 tests whether that instability is a budget artifact. It finds that larger budgets repair self-persistent and passive-world seed stability while keeping controls clean, but detachable-tool recurrence remains partial.

## Falsifiers And Strengtheners

The attractor claim weakens if:

- wider seed sweeps reduce shared-regime convergence toward chance or local-probe behavior;
- controls begin producing false self/tool boundary positives;
- richer non-self baselines match the same performance and boundary behavior.

The attractor claim strengthens if:

- larger policy-gradient budgets make strict convergence seed-stable;
- actor-critic or model-based learners recover the same boundary more reliably;
- the same seed-stability appears across body, viability, frame, and continuity task surfaces.

## Artifacts

- [experiment script](../experiments/architecture_policy_gradient_seed_sweep.py)
- [summary CSV](../artifacts/architecture_policy_gradient_seed_sweep_summary.csv)
- [verdict CSV](../artifacts/architecture_policy_gradient_seed_sweep_verdict.csv)
- [JSON results](../artifacts/architecture_policy_gradient_seed_sweep_results.json)
