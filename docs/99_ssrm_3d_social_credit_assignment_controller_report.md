# SSRM-3D Social Credit-Assignment Controller Report

## Question

Report 98 showed that hidden social/culture regimes were present, but the learned controller still relied on broad social habits. This report makes the pressure sharper by adding mutually exclusive opportunity costs.

The narrow question is:

```text
Can a learned closed-loop controller choose the right social repair action after a delayed hidden social shock, when choosing the wrong repair consumes the recovery window?
```

## What changed

The experiment keeps the 12h development gate and option-gated learned-controller family, but adds a credit-assignment layer:

- `trust_repair` needs mediation;
- `convention_repair` needs teaching/convention repair;
- `coalition_repair` needs mediation;
- `teacher_replacement` needs teaching;
- `rumor_correction` needs investigation first, then mediation.

The model does not receive those variant names. It sees only embodied state, world state, social/culture state, noisy symptoms, memory, time, and previous action.

Wrong post-shock repair actions now have opportunity costs. For example, teaching while coalition repair is needed can let social inequality worsen, and mediating while teacher replacement is needed can let knowledge transfer decay.

## What this does not claim

This is not proof of consciousness. It is not open-ended governance or culture. It is not full deep reinforcement learning.

It is a learned controller test that asks whether current imitation-plus-return-selection machinery can solve a harder social credit-assignment problem.

## Canonical command

```bash
python3 experiments/ssrm_3d_social_credit_assignment_controller.py --train-seeds 20260838,20260839,20260840,20260841,20260842,20260843,20260844,20260845 --tune-seeds 20260848,20260849,20260850,20260851,20260852 --eval-seeds 20260853,20260854,20260855,20260856,20260857 --bias-candidates 0.50,0.70,1.00,1.35,1.70 --hours 16 --step-hours 0.08 --population 10 --epochs 110 --hidden-size 64 --device auto --trace-seed 20260853
```

## Bias Selection

| option bias | validation score | response | targeted repair | opportunity | objective | selected |
|---:|---:|---:|---:|---:|---:|---|
| 0.50 | 0.623 | 0.688 | 0.365 | 0.400 | 0.801 | false |
| 0.70 | 0.625 | 0.691 | 0.365 | 0.400 | 0.803 | false |
| 1.00 | 0.622 | 0.681 | 0.385 | 0.400 | 0.801 | false |
| 1.35 | 0.677 | 0.784 | 0.368 | 0.400 | 0.871 | false |
| 1.70 | 0.713 | 0.845 | 0.412 | 0.438 | 0.924 | true |

The selected option bias is `1.70`.

## Canonical result

The result is a completed negative result:

- return-selected credit GRU score: `0.703`;
- fixed-bias GRU score: `0.644`;
- option frame score: `0.538`;
- reactive survival-only score: `0.222`;
- gain over reactive: `0.481`;
- no major hidden regime before `12h`: `1.000`;
- hidden regime active after `12h`: `1.000`;
- credit response score: `0.843`;
- targeted repair rate: `0.287`;
- wrong repair rate: `0.713`;
- opportunity score: `0.303`.

The verdict is:

```text
supports_credit_assignment_controller = false
supports_social_culture_ablation = false
verdict = failed
```

This script exits successfully because the experiment completed and recorded a falsifying result. The verdict field, not the process code, carries the claim status.

## Ablations

| ablation | score loss | response loss | targeted loss | opportunity loss | culture loss |
|---|---:|---:|---:|---:|---:|
| `regime_signal` | 0.078 | 0.328 | -0.113 | -0.097 | -0.082 |
| `social_culture` | -0.050 | -0.050 | -0.372 | -0.364 | -0.001 |
| `memory` | 0.076 | 0.321 | -0.113 | -0.097 | -0.082 |
| `body` | 0.053 | 0.320 | -0.092 | -0.092 | -0.078 |

Positive:

- the environment now imposes real opportunity cost for wrong social repair;
- the learned GRU beats reactive, frame, and fixed-bias controls;
- regime-signal, memory, and body ablations reduce score or response;
- the trace exposes concrete wrong-action behavior.

Failure:

- targeted repair is only `0.287`;
- wrong repair is `0.713`;
- opportunity score falls to `0.303`;
- removing social/culture state improves score, response, targeted repair, and opportunity score in this run.

That means the current learned policy is not using social/culture state correctly. It is still finding shortcuts or unstable broad action habits.

## Variant boundary

| variant | full score | full response | full targeted | full wrong | social/culture ablated score | social/culture ablated response | social/culture ablated targeted | social/culture ablated wrong |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_repair` | 0.769 | 0.963 | 0.385 | 0.615 | 0.865 | 1.000 | 0.980 | 0.020 |
| `convention_repair` | 0.689 | 0.900 | 0.039 | 0.961 | 0.697 | 0.930 | 0.256 | 0.744 |
| `coalition_repair` | 0.815 | 1.000 | 0.961 | 0.039 | 0.865 | 1.000 | 1.000 | 0.000 |
| `teacher_replacement` | 0.649 | 0.821 | 0.049 | 0.951 | 0.474 | 0.536 | 0.073 | 0.927 |
| `rumor_correction` | 0.592 | 0.530 | 0.000 | 1.000 | 0.860 | 1.000 | 0.983 | 0.017 |

The failure is not uniform. The learned controller handles `coalition_repair`, struggles badly with `teacher_replacement` and `rumor_correction`, and the social/culture ablation behaves better on several mediation-style cases.

## Trace failure

The canonical trace uses `teacher_replacement`.

At `12h`, before the hidden shock, the agent population has survived and developed:

- alive: `10`;
- teaching: `0.920`;
- culture memory: `0.934`;
- knowledge transfer: `0.716`.

After the hidden teacher-replacement shock, the target repair is `teach`, but the learned GRU keeps selecting tool/infrastructure actions:

| checkpoint | target | last action | targeted repair | wrong repair | opportunity loss | response |
|---|---|---|---:|---:|---:|---:|
| `12.5h` | `teach` | `redesign_tools` | 0.100 | 0.900 | 0.046 | 0.864 |
| `14.5h` | `teach` | `redesign_tools` | 0.081 | 0.919 | 0.639 | 0.875 |
| `16h` | `teach` | `construct` | 0.049 | 0.951 | 1.000 | 0.821 |

That is the falsifier in plain terms: the model had a high-level response score, but it spent the scarce post-shock recovery window on the wrong repair class.

## Interpretation

Report 99 is valuable because it makes the next bottleneck concrete.

The earlier social/culture tests showed that social state mattered in broad terms. This test asks whether the controller can separate specific social repair actions under opportunity cost. It cannot yet.

The next threshold is not more social labels. It is stronger credit assignment:

- train from return or actor-critic feedback, not only imitation;
- make wrong repairs produce delayed but specific downstream failures;
- require per-variant targeted repair stability;
- compare against policies with explicit social-causal memory;
- ablate social/culture state after the learned policy has demonstrated stable variant-specific repair.

## Artifacts

- [script](../experiments/ssrm_3d_social_credit_assignment_controller.py)
- [training CSV](../artifacts/ssrm_3d_social_credit_assignment_controller_training.csv)
- [bias selection CSV](../artifacts/ssrm_3d_social_credit_assignment_controller_bias_selection.csv)
- [evaluation CSV](../artifacts/ssrm_3d_social_credit_assignment_controller_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_social_credit_assignment_controller_summary.csv)
- [variant summary CSV](../artifacts/ssrm_3d_social_credit_assignment_controller_variant_summary.csv)
- [ablation CSV](../artifacts/ssrm_3d_social_credit_assignment_controller_ablations.csv)
- [verdict CSV](../artifacts/ssrm_3d_social_credit_assignment_controller_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_social_credit_assignment_controller_trace.json)
- [results JSON](../artifacts/ssrm_3d_social_credit_assignment_controller_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_social_credit_assignment_controller_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_social_credit_assignment_controller_results.js)
