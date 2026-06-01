# SSRM-3D Social Pressure Report

## Question

Does the SSRM-3D track start to satisfy Gate 3: real social pressure?

This precursor gives other agents persistent identities, resource needs, trust toward the tested agent, and role policies:

- helper;
- trader;
- opportunist;
- deceiver.

The tested agent is not rewarded for "being social." Candidate policies are selected by episode return, then re-evaluated with identity memory, social self-state, and shared-tool access ablated.

## Why This Matters

The previous SSRM-3D social stage had a simple competitor. That was not enough to test whether selfhood becomes socially relevant.

Gate 3 requires pressure where the tested agent must model itself as something remembered by others: vulnerable, reputable, helpful, exploitable, trusted, or untrusted. This precursor keeps the claim narrow:

> Social self-state is useful only when other agents have persistent identity, memory, needs, and policies that make the tested agent's continuity socially consequential.

## Command

```bash
python3 experiments/ssrm_3d_social_pressure.py --train-episodes 64 --eval-episodes 96 --candidate-count 160 --seed 20260611
```

## Results

| Scenario | Pressure | Selected policy | Selected reward | No-social reward | Social gain | Identity loss | Self-state loss | Tool loss | Verdict |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 0 | Visible resource control | `no_social_baseline` | 166.000 | 166.000 | 0.000 | 0.000 | 0.000 | 0.000 | Social model rejected in the control. |
| 1 | Cooperative reputation repair | `candidate_123` | 184.594 | 135.188 | 49.406 | 25.688 | 49.031 | 16.594 | Identity, reputation, and social self-state improve repair/route support. |
| 2 | Opportunist vulnerability | `candidate_68` | 140.771 | 90.000 | 50.771 | 12.667 | 65.188 | 1.677 | Modeling own vulnerability prevents exploitation. |
| 3 | Deceptive route identity | `full_social_identity` | 196.000 | 115.573 | 80.427 | 68.917 | 28.000 | 0.000 | Persistent identity separates reliable and deceptive agents. |
| 4 | Shared tool trust conflict | `candidate_9` | 165.375 | -36.000 | 201.375 | 102.292 | 198.727 | 121.365 | Trust and social self-state protect shared-tool coordination. |

All five verdict rows pass the precursor criteria.

## Interpretation

This is a partial Gate 3 pass.

The positive result:

- social machinery is rejected in the visible-resource control;
- social policies are selected only when helper, trader, opportunist, deceiver, or shared-tool pressure exists;
- removing identity memory damages cooperation, deception resistance, and shared-tool trust;
- removing social self-state damages vulnerability handling, reputation-sensitive repair, and commitment completion;
- removing shared-tool access produces a specific failure in the shared-tool conflict stage.

The limit:

- policies are return-selected from candidate social-control policies, not learned end-to-end in the SSRM-3D controller;
- social agents use simple role policies, not open-ended communication or learned deception;
- reputation and trust are small scalar memories, not rich social models;
- this does not prove that social selfhood is necessary in general.

## Gate 3 Status

Gate 3 moves from open to partial.

The current evidence supports this narrower claim:

> When other agents remember, help, exploit, deceive, trade, or sabotage, it becomes useful for the tested agent to track itself as a continuing social object with vulnerability, reputation, and obligations.

It does not yet support the stronger claim:

> Learned embodied agents naturally converge on social self-representation across open-ended societies.

## Visualization

Open the trace visualization through a local server:

```bash
python3 -m http.server 8765
```

Then open, using the port you served from:

```text
http://127.0.0.1:8765/visualizations/ssrm_3d_social_pressure.html
```

The visualization replays `artifacts/ssrm_3d_social_pressure_trace.json`, showing the tested agent path, other agents, resources, hidden resource, shelter, shared tools, current event, reputation, and social memory.

## Stronger Next Test

The next version should move social behavior into learned controllers:

- train the controller with other agents that have persistent memory and needs;
- remove candidate social policies;
- allow repeated interaction across episodes so reputation has longer continuity;
- add communication, deception, refusal, shared tools, resource conflict, and repair requests;
- ablate identity memory, self-state, attention mixing, continuity memory, tool access, and LLM social reasoning separately.

That is the real Gate 3 to Gate 4 bridge.

## Long-Run Social Ecology

[Report 67](67_ssrm_3d_social_ecology_report.md) implements the narrow costly-communication precursor implied by this section.

The clean social experiment should not reward talking, chatting, bonding, or friendship directly.

Communication should have a cost:

- time;
- attention;
- energy;
- exposure risk;
- missed resource opportunities.

A signal counts only if transferring information is cheaper than rediscovering it. Useful early signals should be grounded in jobs like hazard warning, resource direction, repair request, damaged-self disclosure, trust warning, blocked-route notice, cache location, coordination request, or refusal.

Names should become useful only when identity history matters. A name is a compression shortcut for a persistent social history: who helped, lied, repaired, stole, traded, sabotaged, or kept commitments. If agents interact once, names should not help. If agents persist and remember, names can become control-relevant.

The expected progression is:

- signals;
- shared meanings;
- identity labels;
- requests;
- warnings;
- promises;
- gossip;
- teaching;
- play;
- humour;
- ritualized bonding.

Each step has to earn itself. Warnings count when they prevent harm. Promises count when future cooperation matters. Gossip counts when information about absent agents improves future decisions. Small talk counts only if low-cost contact maintains trust or lowers uncertainty. Lying should be treated as a dangerous instrumental policy that may emerge if manipulating another agent's belief improves short-term outcome.

The long-run question:

> Do agents invent social structure because it helps preserve future options?

A stronger ecology would track trust clusters, role specialization, retaliation, favour trading, avoidance, dependency, repair relationships, deception arms races, and shared infrastructure. The deepest social-self test is whether an agent starts modeling itself as something other agents model: reliable, dangerous, repair-worthy, deceptive, useful, vulnerable, or committed.

## Artifacts

- [experiment script](../experiments/ssrm_3d_social_pressure.py)
- [visualization](../visualizations/ssrm_3d_social_pressure.html)
- [evaluation CSV](../artifacts/ssrm_3d_social_pressure_eval.csv)
- [policy-selection CSV](../artifacts/ssrm_3d_social_pressure_policy_selection.csv)
- [summary CSV](../artifacts/ssrm_3d_social_pressure_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_social_pressure_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_social_pressure_trace.json)
- [trace JS fallback](../artifacts/ssrm_3d_social_pressure_trace.js)
- [JSON results](../artifacts/ssrm_3d_social_pressure_results.json)
