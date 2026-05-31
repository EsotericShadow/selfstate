# SSRM-3D Learned Controller Report

## Question

Can a learned policy state, trained without self labels, recover self-equivalent variables when it must control the SSRM-3D world?

Report 61 trained observers. This report trains controllers. The learner receives embodied action-observation traces from the existing SSRM-3D agents and is trained by:

- return-weighted behavior cloning;
- future-return prediction;
- no supervised self-state loss.

Self-state is used only after training, as a probe of the policy hidden state.

## Why This Matters

The previous result could still be attacked as:

> A separate observer can learn body variables, but that does not mean policy control uses a self-equivalent state.

This experiment moves the probe into the policy state. It asks whether learned recurrent controllers outperform frame-only controllers under embodied pressure and whether their hidden states encode energy, integrity, mobility, and sensor capability.

## Command

```bash
python3 experiments/ssrm_3d_learned_controller.py --episodes-per-stage 48 --eval-episodes 24 --ticks 540 --seed 20260609 --hidden-size 32 --epochs 160 --batch-size 64 --learning-rate 0.004 --device auto
```

The canonical run used Apple Silicon MPS:

```text
device mps torch 2.8.0 mps_available True
```

## Learners

| Architecture | Role |
|---|---|
| `frame_mlp` | Stateless frame-only learned controller. |
| `torch_rnn` | Simple recurrent learned controller. |
| `torch_gru` | Gated recurrent learned controller. |
| `torch_lstm` | Gated recurrent learned controller with cell state. |

The policy chooses among:

- `avoid_hazard`;
- `reach_shelter`;
- `honor_commitment`;
- `collect_resource`;
- `explore_reduce_uncertainty`.

Immediate hazard avoidance still has a reflex override. The learned policy does not call an LLM.

## Results

| Stage | Pressure | Best recurrent | Frame reward | Recurrent reward | Reward gain | Recurrent self R2 | Self edit action swing | Verdict |
|---:|---|---|---:|---:|---:|---:|---:|---|
| 0 | Spatial resources | `torch_rnn` | 89.306 | 89.110 | -0.197 | 0.688 | 0.001 | Learned recurrence is not needed in the low-pressure task. |
| 1 | Hidden energy | `torch_lstm` | 37.881 | 92.078 | 54.197 | 0.813 | 0.001 | Learned recurrent policy state decodes self-state and improves control. |
| 2 | Body drift | `torch_gru` | 28.257 | 79.096 | 50.839 | 0.637 | 0.002 | Learned recurrent policy state decodes self-state and improves control. |
| 3 | Delayed options | `torch_lstm` | 81.930 | 132.050 | 50.120 | 0.578 | 0.008 | Learned recurrent policy state decodes self-state and improves control. |
| 4 | Commitment recovery | `torch_lstm` | 6.081 | 95.502 | 89.421 | 0.760 | 0.015 | Learned recurrent policy state decodes self-state under high pressure. |
| 5 | Subsystem arbitration | `torch_gru` | -37.410 | 70.018 | 107.428 | 0.658 | 0.014 | Learned recurrent policy state decodes self-state under high pressure. |
| 6 | Multiagent social | `torch_gru` | -30.317 | 93.633 | 123.950 | 0.594 | 0.009 | Learned recurrent policy state decodes self-state under high pressure. |

All seven stage verdicts pass the learned-controller precursor criteria.

## Interpretation

This result is stronger than the observer result because the learned state belongs to a controller that acts in the world. The recurrent controller does not receive self labels during training, yet under hidden energy, body drift, delayed options, commitments, arbitration, and social pressure it strongly outperforms the frame-only controller and carries decodable agent-state variables.

Stage 0 remains a useful control. The recurrent controller does not improve the low-pressure spatial task, which keeps the result from becoming "recurrence always equals selfhood."

The result is still not a solved Attractor Test. The counterfactual self-edit action swing is small. That means the policy state contains self-state information and improves control, but direct causal editing of that self direction is not yet strong.

## Limits

- Training is return-weighted behavior cloning, not full online reinforcement learning.
- Source traces still come from supplied SSRM-3D agents.
- The learned controller has a reflex hazard override.
- Self-state probes are post-training linear probes.
- Counterfactual self edits have weak direct action effects in this run.
- The result does not imply consciousness.

## Stronger Next Test

The next version should train controllers directly from online return or model-based planning in SSRM-3D, then apply stronger causal interventions to the policy state. The key missing evidence is not decodability or reward gain; it is robust action change after counterfactual self-state edits.

## Artifacts

- [experiment script](../experiments/ssrm_3d_learned_controller.py)
- [summary CSV](../artifacts/ssrm_3d_learned_controller_summary.csv)
- [evaluation CSV](../artifacts/ssrm_3d_learned_controller_eval.csv)
- [verdict CSV](../artifacts/ssrm_3d_learned_controller_verdict.csv)
- [JSON results](../artifacts/ssrm_3d_learned_controller_results.json)
