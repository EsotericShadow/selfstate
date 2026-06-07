# SSRM-3D Readiness Closed-Loop Recovery Report

## Question

Report 136 showed that a GRU trained only from designed readiness traces could
not own the 72h readiness world. It preserved the 12h shock gate, but all
learned-controller agents died by the end.

This report asks the immediate follow-up:

```text
If the learner acts in the world, creates its own failure states, and those
states are relabeled by the designed readiness controller, does the recovered
GRU survive and maintain readiness over 72h?
```

## What Changed

This report adds:

- `experiments/ssrm_3d_readiness_closed_loop_recovery_controller.py`

The experiment keeps the Report 135/136 world unchanged and adds a recovery
training layer:

- train frame and GRU behavior models from designed readiness traces;
- let the behavior GRU act in recovery worlds;
- collect the learner's visited states rather than only teacher states;
- relabel those states with the designed readiness controller;
- weight recovery examples by survival urgency, readiness deficit, post-gate
  exposure, pest pressure, structural strain, disease, and contamination;
- train a stage-1 recovery GRU;
- let that recovery GRU act in shifted recovery worlds;
- collect and relabel a second recovery pass;
- train a final recovery GRU;
- evaluate designed, reactive, frame, behavior GRU, recovery GRU, and recovery
  ablations on held-out 72h worlds.

Inputs remain observation features from the world: body state, time, resources,
infrastructure, tools, social/culture state, environment state, readiness
channels, and previous action. The learner does not receive a scenario label.

## What This Does Not Claim

This is not deep reinforcement learning. It is not open-ended civilization. It
is not subjective consciousness. It is closed-loop recovery supervision from a
designed teacher.

The result is a meaningful improvement over plain imitation, but it is not a
solved learned readiness controller.

## Canonical Command

```bash
python3 experiments/ssrm_3d_readiness_closed_loop_recovery_controller.py --behavior-train-seeds 20261211,20261212,20261213,20261214,20261215,20261216 --recovery-seeds 20261231,20261232,20261233 --eval-seeds 20261251,20261252,20261253,20261254,20261255 --hours 72 --step-hours 0.10 --population 14 --epochs 52 --recovery-epochs 42 --hidden-size 72 --device cpu --trace-seed 20261251
```

## Training Result

The recovery dataset grows beyond the original teacher traces:

| Pass | Architecture | Train accuracy | Weighted accuracy | Sequences | Steps | Recovery examples |
|---|---|---:|---:|---:|---:|---:|
| `behavior` | `frame_mlp` | `0.251` | `0.251` | `108` | `71936` | `0` |
| `behavior` | `gru` | `0.249` | `0.249` | `108` | `71936` | `0` |
| `recovery_stage_1` | `gru` | `0.343` | `0.517` | `150` | `96165` | `24229` |
| `recovery_final` | `gru` | `0.423` | `0.639` | `192` | `124711` | `52775` |

The first recovery pass is still severe: behavior-GRU rollouts end with `0`
alive in all three recovery seeds. The second pass is better but uneven:
shifted recovery seeds end with `12`, `4`, and `14` alive.

That is the right diagnostic shape. The training is no longer just copying
teacher traces; it is training on the states the learner actually creates.

## Held-Out Result

The final recovery GRU materially improves over Report 136-style behavior
imitation:

| Controller | Maturation | Final alive | Final readiness | Knowledge transfer | Structural strain |
|---|---:|---:|---:|---:|---:|
| `designed` | `1.000` | `17.8` | `1.000` | `1.000` | `0.000` |
| `recovery_gru` | `0.470` | `14.0` | `0.349` | `0.000` | `0.347` |
| `behavior_gru` | `0.212` | `0.0` | `0.406` | `0.000` | `0.737` |
| `frame_mlp` | `0.181` | `0.0` | `0.292` | `0.000` | `0.654` |
| `reactive` | `0.070` | `0.0` | `0.004` | `0.000` | `1.000` |

The recovery GRU:

- keeps the 12h gate intact;
- reaches post-gate shocks in every held-out seed;
- improves maturation score by `0.258` over the behavior GRU;
- improves final alive from `0.0` to `14.0`;
- lowers structural strain from `0.737` to `0.347`;
- still falls far below the designed controller;
- still has `0.000` knowledge transfer;
- still fails clean ablation specificity.

The verdict is:

```text
supports_closed_loop_recovery = false
supports_recurrent_recovery_gain = true
supports_ablation_specificity = false
verdict = partial_or_failed
```

## Ablation Boundary

The recovery GRU ablations are still not clean:

| Ablation | Score loss |
|---|---:|
| `body` | `-0.046` |
| `infrastructure` | `-0.001` |
| `tools` | `-0.070` |
| `social_culture` | `0.010` |
| `environment` | `0.015` |
| `readiness` | `0.008` |
| `previous_action` | `-0.129` |

Negative losses mean the ablated run scored higher than the unablated run. The
social/culture, environment, and readiness channels show small positive losses,
but the body, tools, infrastructure, and previous-action channels are unstable
or inverted.

So the recovery model is not yet a robust causal controller. It learned enough
closed-loop recovery to survive, but not enough to preserve the full designed
readiness behavior or prove stable feature dependence.

## Interpretation

This is progress, not a pass.

Report 136 showed that plain imitation fails completely by the end of the 72h
readiness world. Report 137 shows that training on student-created failure
states can repair the most visible failure: final survival. That matters for
the active project goal because the learned controller can now stay alive long
enough for a multi-day development window under post-gate shocks.

But the deeper goal remains unsolved:

- no births or intergenerational knowledge transfer under the learned recovery
  controller;
- readiness stays far below the designed policy;
- architecture/tool development remains weak;
- several ablations improve the score instead of reducing it;
- the learner is still absorbing teacher corrections rather than optimizing
  downstream multi-step consequences itself.

The next learned-control step should not be another visual layer or another
single-action relabeling pass. It should train a value/process model over
student-created multi-step readiness windows: what happens if the agent spends
the next few actions repairing strain, teaching, scouting, gathering fuel, or
building blueprints?

## Artifacts

- [script](../experiments/ssrm_3d_readiness_closed_loop_recovery_controller.py)
- [training CSV](../artifacts/ssrm_3d_readiness_closed_loop_recovery_training.csv)
- [collection CSV](../artifacts/ssrm_3d_readiness_closed_loop_recovery_collection.csv)
- [evaluation CSV](../artifacts/ssrm_3d_readiness_closed_loop_recovery_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_readiness_closed_loop_recovery_summary.csv)
- [ablation CSV](../artifacts/ssrm_3d_readiness_closed_loop_recovery_ablations.csv)
- [verdict CSV](../artifacts/ssrm_3d_readiness_closed_loop_recovery_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_readiness_closed_loop_recovery_trace.json)
- [results JSON](../artifacts/ssrm_3d_readiness_closed_loop_recovery_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_readiness_closed_loop_recovery_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_readiness_closed_loop_recovery_results.js)
