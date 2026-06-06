# SSRM-3D Social Repair Critic Controller Report

## Question

Report 99 failed because the learned controller responded broadly to hidden social shocks but often chose the wrong repair class.

This follow-up asks:

```text
Can a learned repair critic improve social credit assignment by biasing inspect, teach, and mediate actions under the same hidden-variant, no-label opportunity-cost world?
```

## What changed

The experiment keeps the Report 99 world and imports its machinery instead of rebuilding the environment.

New component:

- a GRU repair critic trained on the same observation traces;
- repair classes: `none`, `inspect`, `teach`, `mediate`;
- repair-bias selection by closed-loop validation return;
- no hidden credit-variant label in model input;
- same held-out seeds and ablations as Report 99.

The critic does not replace the base controller. It biases the base option-gated GRU only when social-credit symptoms indicate that repair selection matters.

## What this does not claim

This is not proof of social understanding, consciousness, open-ended civilization, or full deep reinforcement learning.

It is a targeted controller test for one failure: wrong social repair under opportunity cost.

## Canonical command

```bash
python3 experiments/ssrm_3d_social_repair_critic_controller.py --device auto
```

## Repair bias selection

| repair bias | validation score | response | targeted repair | wrong repair | opportunity | objective | selected |
|---:|---:|---:|---:|---:|---:|---:|---|
| 0.00 | 0.713 | 0.845 | 0.412 | 0.588 | 0.438 | 0.922 | false |
| 0.75 | 0.716 | 0.849 | 0.412 | 0.588 | 0.442 | 0.925 | false |
| 1.25 | 0.718 | 0.851 | 0.414 | 0.586 | 0.445 | 0.929 | false |
| 1.75 | 0.727 | 0.868 | 0.424 | 0.576 | 0.463 | 0.947 | false |
| 2.50 | 0.731 | 0.870 | 0.435 | 0.565 | 0.484 | 0.959 | false |
| 3.50 | 0.737 | 0.873 | 0.443 | 0.557 | 0.499 | 0.970 | true |

Selected repair bias: `3.50`.

## Canonical result

The result is a completed failed result with useful improvement:

- repair critic score: `0.744`;
- Report 99 baseline score: `0.703`;
- fixed-bias GRU score: `0.644`;
- option frame score: `0.538`;
- reactive score: `0.222`;
- gain over Report 99 baseline: `0.042`;
- credit response score: `0.895`;
- targeted repair rate: `0.402`;
- wrong repair rate: `0.598`;
- opportunity score: `0.485`;
- no major hidden regime before `12h`: `1.000`;
- hidden regime active after `12h`: `1.000`.

The verdict is:

```text
supports_repair_critic_controller = false
supports_social_culture_ablation = false
verdict = failed
```

## What improved

Compared with Report 99:

| Metric | Report 99 | Report 101 | Change |
|---|---:|---:|---:|
| score | 0.703 | 0.744 | +0.042 |
| targeted repair | 0.287 | 0.402 | +0.116 |
| wrong repair | 0.713 | 0.598 | -0.116 |
| opportunity | 0.303 | 0.485 | +0.182 |
| response | 0.843 | 0.895 | +0.052 |

This shows that a repair critic can move the controller in the right direction.

## Why it still fails

The strong claim still fails because the repair is not stable or causally clean:

- targeted repair remains below the `0.42` threshold;
- wrong repair remains above the `0.58` threshold;
- removing social/culture state improves score, response, targeted repair, and opportunity in aggregate;
- `rumor_correction` still collapses in the full model;
- several mediation-style variants perform better under social/culture ablation, which means the learned dependency is still unstable.

## Ablations

| ablation | score loss | response loss | targeted loss | opportunity loss | culture loss |
|---|---:|---:|---:|---:|---:|
| `regime_signal` | 0.120 | 0.380 | 0.002 | 0.085 | -0.041 |
| `social_culture` | -0.028 | -0.038 | -0.252 | -0.197 | -0.000 |
| `memory` | 0.121 | 0.374 | 0.002 | 0.085 | -0.038 |
| `body` | 0.048 | 0.096 | 0.004 | 0.064 | 0.126 |

Regime signal and memory matter. Social/culture state still does not behave correctly under this learned controller.

## Variant boundary

| variant | full targeted | full wrong | full score | social/culture ablated targeted | social/culture ablated wrong | interpretation |
|---|---:|---:|---:|---:|---:|---|
| `coalition_repair` | 0.961 | 0.039 | 0.815 | 1.000 | 0.000 | strong either way |
| `convention_repair` | 0.273 | 0.727 | 0.764 | 0.256 | 0.744 | weak but slightly better full |
| `teacher_replacement` | 0.393 | 0.607 | 0.787 | 0.153 | 0.847 | full helps |
| `trust_repair` | 0.385 | 0.615 | 0.769 | 0.933 | 0.067 | ablation improves |
| `rumor_correction` | 0.000 | 1.000 | 0.588 | 0.930 | 0.070 | full collapses |

The critic improves the average but not the causal boundary. `rumor_correction` is now the clearest hard case because it requires staged repair: inspect first, then mediate.

## Interpretation

Report 101 is progress, not a pass.

The repair critic shows that adding a learned evaluator over repair actions can improve wrong-repair pressure. But it also shows that imitation-derived repair labels are not enough. The next controller needs return-trained or actor-critic social repair, counterfactual repair traces, and explicit staged-repair credit for cases like rumor correction.

The software and LLM-controller roadmaps should treat this as a warning. A critic that improves average score can still be wrong on the exact causal repair it is supposed to learn.

## Artifacts

- [script](../experiments/ssrm_3d_social_repair_critic_controller.py)
- [base training CSV](../artifacts/ssrm_3d_social_repair_critic_controller_base_training.csv)
- [repair training CSV](../artifacts/ssrm_3d_social_repair_critic_controller_repair_training.csv)
- [base bias selection CSV](../artifacts/ssrm_3d_social_repair_critic_controller_base_bias_selection.csv)
- [repair bias selection CSV](../artifacts/ssrm_3d_social_repair_critic_controller_repair_bias_selection.csv)
- [evaluation CSV](../artifacts/ssrm_3d_social_repair_critic_controller_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_social_repair_critic_controller_summary.csv)
- [variant summary CSV](../artifacts/ssrm_3d_social_repair_critic_controller_variant_summary.csv)
- [ablation CSV](../artifacts/ssrm_3d_social_repair_critic_controller_ablations.csv)
- [verdict CSV](../artifacts/ssrm_3d_social_repair_critic_controller_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_social_repair_critic_controller_trace.json)
- [results JSON](../artifacts/ssrm_3d_social_repair_critic_controller_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_social_repair_critic_controller_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_social_repair_critic_controller_results.js)
