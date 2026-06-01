# SSRM-3D No-Leak Integration Sweep Report

## Question

Does the Report 69 learned-integration bridge survive when the obvious shortcut is removed?

Report 69 showed that a recurrent controller can use designed tool, social, continuity, and attention packet channels. Its main weakness was that scenario identity and neatly separated pressure rows were still supplied. This follow-up tests the stricter claim:

> With no scenario-id feature, randomized pressure combinations, multiple seeds, and wider margins, a recurrent policy state should still carry the relevant pressure evidence and fail under the matching ablation.

The result is allowed to be negative. A failed strong claim is useful if it narrows exactly where the bridge breaks.

## Method

Canonical command:

```bash
python3 experiments/ssrm_3d_no_leak_integration_sweep.py --seeds 20260615,20260616,20260617,20260618,20260619 --train-episodes 1200 --eval-episodes 400 --epochs 400 --hidden-size 64 --device cpu
```

The experiment keeps the Report 69 packet-controller frame, but changes the pressure surface:

| Change | Purpose |
|---|---|
| no scenario-id feature | prevents the policy from selecting by named row |
| randomized tool, social, and continuity pressure flags | prevents one pressure channel from leaking another |
| integrated rows split by priority metadata | avoids hiding failures inside one aggregate integrated score |
| five seeds | tests stability instead of one canonical pass |
| margin requirements | rejects passes sitting on the threshold |
| zero-exit negative verdict | treats failed support as evidence, not script failure |

The inputs still contain designed feature groups. `case_type` and `priority_group` are evaluation metadata, not policy inputs.

Architectures:

| Architecture | Role |
|---|---|
| `frame_mlp` | Reads the final packet only. |
| `torch_gru` | Integrates early packet evidence through recurrent policy state. |

Post-training ablations zero the tool, social, continuity, or attention channel.

## Results

| Case | Seeds | Support rate | Min gain margin | Min ablation margin | Max irrelevant loss | Verdict |
|---|---:|---:|---:|---:|---:|---|
| `control` | 5/5 | 1.000 | 8.000 | 8.000 | 0.000 | supported |
| `single_tool` | 5/5 | 1.000 | 2.156 | 3.156 | 0.000 | not stable |
| `single_social` | 5/5 | 1.000 | 69.000 | 70.000 | 0.000 | supported |
| `single_continuity` | 5/5 | 1.000 | 69.000 | 70.000 | 0.000 | supported |
| `integrated_tool` | 5/5 | 1.000 | 10.833 | 33.833 | 0.000 | supported |
| `integrated_social` | 4/5 | 0.800 | 75.000 | -1.667 | 0.000 | not stable |
| `integrated_continuity` | 5/5 | 1.000 | 75.000 | 8.250 | 0.000 | supported |

The strong no-leak randomized integration claim is not supported by all verdict rows.

## Interpretation

This is a useful partial negative.

The harder test keeps the control clean and preserves robust bridges for local social, local continuity, integrated tool priority, and integrated continuity priority. That means Report 69 was not pure scenario-id memorization.

But the strong claim still fails:

- `single_tool` supports all five seeds by raw threshold, but its weakest margins are too close to the widened pass line;
- `integrated_social` reaches only `4/5` raw seed support and has a negative relevant-ablation margin;
- the result therefore cannot be called stable no-leak learned integration.

The honest update is:

> Report 69 remains a designed packet bridge. Some learned channel use survives removal of scenario identity and randomized pressure mixing, but stable cross-pressure no-leak integration is not established.

This is stronger evidence discipline than another narrow positive. It identifies exactly where the bridge claim breaks.

## Limits

- This is still packet-level learning, not online embodied RL.
- The packet feature groups are still designed and known for ablation.
- Tool, social, continuity, and attention variables remain hand-specified pressure channels.
- The policy does not invent tools, social codes, commitments, or continuity records.
- Integrated priority metadata is used for reporting and verdict grouping, not as an input feature.
- CPU is used for the canonical deterministic sweep even though GPU/MPS is available.

## Next Test

The next stronger version should move this pressure into the full SSRM-3D learned controller:

- no designed scenario rows;
- online or model-based control in the embodied world;
- learned tool construction rather than tool packet evidence;
- repeated social interaction and deception pressure rather than social packet evidence;
- continuity restore/fork pressure inside the learned policy loop;
- ablations over self-state, learned self-subspace, attention, continuity memory, tool access, and LLM packet stream.

Alternatively, a stricter packet precursor could vary architectures, hide feature-group boundaries from ablation design, hold out pressure combinations, and require seed-stable support on unseen mixes.

## Visualization

Serve the repo root and open:

```text
http://127.0.0.1:8765/visualizations/ssrm_3d_no_leak_integration.html
```

The visualization replays an `integrated_social` trace, including early feature-group activity, recurrent confidence, ablation actions, and the final no-leak verdict table.

## Artifacts

- [experiment script](../experiments/ssrm_3d_no_leak_integration_sweep.py)
- [visualization](../visualizations/ssrm_3d_no_leak_integration.html)
- [evaluation CSV](../artifacts/ssrm_3d_no_leak_integration_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_no_leak_integration_summary.csv)
- [seed verdict CSV](../artifacts/ssrm_3d_no_leak_integration_seed_verdict.csv)
- [verdict CSV](../artifacts/ssrm_3d_no_leak_integration_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_no_leak_integration_trace.json)
- [JSON results](../artifacts/ssrm_3d_no_leak_integration_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_no_leak_integration_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_no_leak_integration_results.js)
