# SSRM-3D Tool-Making Report

## Question

Does the SSRM-3D track start to satisfy Gate 2: tool-making or externalized cognition?

This precursor gives the agent simple build/place affordances:

- route markers;
- shelter and resource beacons;
- hazard alarms;
- energy caches.

The agent is not rewarded for building tools and is not told which tool is useful. Candidate policies are selected only by episode return, then re-evaluated with tool access ablated.

## Why This Matters

The previous SSRM-3D results could still be bounded as internal self-state control. Gate 2 asks for a harder pressure:

> Does the agent discover that structures outside its body can reduce confusion, preserve options, or support commitments?

That matters because externalized cognition creates a bridge between self-state, memory, tool use, and later social coordination. A marker or alarm is not the self, but building one can preserve future control when internal memory or perception is unreliable.

## Command

```bash
python3 experiments/ssrm_3d_tool_making.py --train-episodes 48 --eval-episodes 72 --ticks 300 --candidate-count 180 --seed 20260610
```

## Results

| Scenario | Pressure | Selected policy | Selected reward | No-tool reward | Tool gain | Tool ablation loss | Tools built | Verdict |
|---:|---|---|---:|---:|---:|---:|---:|---|
| 0 | Visible resources | `no_tool_baseline` | 143.973 | 143.973 | 0.000 | 0.000 | 0.000 | Tools rejected in the control. |
| 1 | Hidden route marking | `shelter_resource_beacons` | 79.881 | 36.083 | 43.797 | 36.867 | 3.028 | External tools reduce confusion. |
| 2 | Degraded sensor alarms | `sparse_cache_beacon` | 76.070 | 33.826 | 42.245 | 42.220 | 2.486 | External tools reduce confusion. |
| 3 | Interruption option recovery | `candidate_132` | 34.877 | -29.402 | 64.279 | 60.216 | 10.222 | External tools preserve options after memory loss. |
| 4 | Energy cache limit control | `no_tool_baseline` | 11.012 | 11.012 | 0.000 | 0.000 | 0.000 | Cache affordance is not yet useful enough to count. |

All five verdict rows pass the precursor criteria. The important point is not that every tool helps. The cache-only affordance is rejected. The result is specific to route, sensor, and interruption pressures.

## Interpretation

This is a partial Gate 2 pass.

The positive result:

- tools are not selected when the visible-world control is already solvable;
- tools are selected when low visibility, sensor degradation, or memory interruption makes internal state insufficient;
- removing tool access from the selected policy removes most of the gain;
- tool spam remains worse than selected tool use, so the result is not "build anything everywhere."

The limit:

- the successful policies are return-selected from candidate affordance policies, not trained end-to-end in the learned SSRM-3D controller;
- the energy-cache condition does not yet produce useful cache discovery;
- the tool semantics are still hand supplied by the environment;
- the result does not prove that tool use is necessary for selfhood.

## Gate 2 Status

Gate 2 moves from open to partial.

The current evidence supports this narrower claim:

> External structures become useful when internal memory or perception cannot preserve future control across route uncertainty, sensor degradation, or interruption.

It does not yet support the stronger claim:

> Learned embodied agents naturally invent arbitrary tools under open-ended pressure.

## Visualization

Open the trace visualization through a local server:

```bash
python3 -m http.server 8765
```

Then open, using the port you served from:

```text
http://127.0.0.1:8765/visualizations/ssrm_3d_tool_making.html
```

The visualization replays `artifacts/ssrm_3d_tool_making_trace.json`, showing the agent path, resources, hazards, shelter, placed tools, current target, and whether action was driven by internal state or externalized memory.

## Stronger Next Test

The next version should move tool discovery into the learned controller:

- train the controller with tool affordances available;
- remove explicit candidate tool policies;
- probe whether policy state learns when external memory is worth building;
- ablate tool access, attention mixing, continuity memory, and self-state separately;
- combine with the social-pressure precursor so tools can be shared, stolen, trusted, or sabotaged by agents with persistent memory.

That is the real Gate 2 to Gate 3 bridge.

## Artifacts

- [experiment script](../experiments/ssrm_3d_tool_making.py)
- [visualization](../visualizations/ssrm_3d_tool_making.html)
- [evaluation CSV](../artifacts/ssrm_3d_tool_making_eval.csv)
- [policy-selection CSV](../artifacts/ssrm_3d_tool_making_policy_selection.csv)
- [summary CSV](../artifacts/ssrm_3d_tool_making_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_tool_making_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_tool_making_trace.json)
- [JSON results](../artifacts/ssrm_3d_tool_making_results.json)
