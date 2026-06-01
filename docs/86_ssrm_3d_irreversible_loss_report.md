# SSRM-3D Irreversible Loss Report

## Question

Does permanent loss create persistent control pressure beyond ordinary maintenance, risk avoidance, or roleplay?

Report 74 puts irreversible loss after structured perception, sleep/rest, illness/sanitation, weather/exposure, tool/shelter degradation, social trust/contracts, predator/threat agents, resource ecology, injury/disability adaptation, development/skill learning, and dependent care. This experiment asks whether loss memory, value-at-risk estimation, replacement modeling, caution control, tool/shelter/relationship preservation, memory backup, loss response, and continuity become useful only when future option space can be permanently reduced.

The test is narrow:

> Loss machinery should be rejected in a reversible-wear control, but selected when tools, shelters, relationships, memories, or option space can be permanently lost.

This is not grief simulation. A loss-response or caution-like state is treated only as an affective control summary that changes attention, risk tolerance, memory salience, and replanning.

## Command

```bash
python3 experiments/ssrm_3d_irreversible_loss.py --train-episodes 72 --eval-episodes 96 --seed 20260701 --candidate-count 7
```

## Mechanisms

| Mechanism | Control role |
|---|---|
| loss memory | tracks what is gone, nearly lost, or no longer safe to assume |
| value at risk | estimates future-option value exposed by the current action |
| replacement model | distinguishes replaceable wear from irreplaceable loss |
| caution control | lowers risk after high value-at-risk or loss pressure |
| tool preservation | protects critical tools before repair is no longer possible |
| shelter preservation | protects safe shelter before exposure becomes permanent |
| relationship preservation | protects helper/trust access before social loss is permanent |
| memory backup | preserves route, hazard, commitment, and loss history |
| loss response | replans after loss pressure changes the future option landscape |
| continuity memory | keeps lost assets, memories, relationships, and options lost after restore |

## Conditions

| Condition | Meaning |
|---|---|
| `full_control` | intact irreversible-loss control |
| `no_loss_memory` | removes record of permanent and near-loss events |
| `no_value_at_risk` | removes estimation of future-option exposure |
| `no_replacement_model` | removes replaceability and fallback modeling |
| `no_caution_control` | removes risk-threshold adjustment under loss pressure |
| `no_tool_preservation` | removes critical-tool preservation |
| `no_shelter_preservation` | removes shelter-preservation action |
| `no_relationship_preservation` | removes helper/trust preservation |
| `no_memory_backup` | removes archive/route/commitment backup |
| `no_loss_response` | removes replanning after permanent-loss pressure |
| `no_continuity` | removes restore-time loss continuity |
| `reckless_reversible_baseline` | acts as if all wear is reversible |
| `omniscient_loss_control` | upper-bound loss-aware control |

## Results

Loss values are mean reward loss from the selected `full_control` policy.

| Scenario | Selected policy | loss memory | value risk | replacement | caution | tool | shelter | relationship | memory backup | loss response | continuity | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `reversible_wear_control` | `reckless_reversible_baseline` | 0.032 | 0.003 | 0.022 | -0.015 | 0.019 | -0.035 | 0.012 | -0.007 | -0.033 | -0.017 | loss rejected |
| `irreplaceable_tool_shelter_loss` | `tool_shelter_guardian` | 128.341 | 330.463 | 129.856 | 104.588 | 264.846 | 257.853 | 0.012 | 0.007 | 0.014 | 0.005 | tool/shelter pressure |
| `permanent_relationship_loss` | `relationship_guardian` | 135.502 | 383.127 | -0.029 | 140.853 | -0.076 | -0.044 | 375.862 | -0.002 | 204.641 | -0.039 | relationship pressure |
| `memory_archive_permanent_loss` | `memory_backup_planner` | 144.196 | 378.156 | 135.422 | -0.033 | 0.004 | 0.008 | 0.005 | 378.569 | -0.016 | -0.019 | memory pressure |
| `cascading_loss_response` | `loss_response_planner` | 224.112 | 398.528 | 138.861 | 245.995 | 294.805 | 291.608 | 315.824 | 0.062 | 515.322 | 0.017 | cascade pressure |
| `restore_irreversible_loss_continuity` | `continuity_loss_planner` | 143.293 | 388.843 | 122.712 | 165.360 | 231.072 | 227.891 | 254.365 | 257.698 | 243.092 | 708.354 | restore pressure |

All six verdict rows pass `supports_irreversible_loss_precursor=True`.

## Interpretation

This result supports the twelfth pressure-layer step at precursor level:

- irreversible-loss machinery is rejected when damage is reversible and replaceable;
- loss memory matters when the agent must remember what can no longer be assumed available;
- value-at-risk matters when current actions expose future option space;
- replacement modeling matters when some losses can only be partially compensated;
- caution control matters when permanent loss should change risk tolerance;
- tool, shelter, relationship, and memory preservation matter only under matching loss surfaces;
- loss response matters when one permanent loss changes later planning;
- continuity matters when restore could incorrectly resurrect lost tools, shelters, relationships, memories, or options.

The anti-overclaim boundary is:

> Irreversible loss is not selfhood. It becomes relevant to selfhood only when the tested agent must model permanent changes to its own future option space, obligations, social access, memory state, or continuity.

## Limits

- Candidate policies are supplied and return-selected.
- Loss dynamics are abstract control variables, not grief, psychology, or ethics.
- The selected planner is not an online RL agent discovering loss preservation from scratch.
- The successful trace mostly avoids permanent loss; the strongest visible failures are in ablation outcomes.
- This does not yet test learned affective control state in the full SSRM-3D learned controller.

## Next Test

The next pressure-layer step should add affective control state as a narrow, ablatable control summary:

- fear, stress, trust, frustration, affiliation, curiosity, shame/guilt analogues, and loss-response state should only count when they change attention, risk tolerance, approach/avoidance, communication, memory salience, rest safety, repair/help-seeking, or trust updates;
- each state needs a no-job control where it is rejected;
- ablations should separate affective summaries from ordinary hidden-state tracking, scripted personality, and subjective-emotion claims.

## Visualization

Serve the repo root and open:

```text
http://127.0.0.1:8765/visualizations/ssrm_3d_irreversible_loss.html
```

The page replays the `cascading_loss_response` trace with tool integrity, shelter safety, relationship trust, memory integrity, option space, value at risk, replacement feasibility, caution state, actions, and ablation outcomes.

## Artifacts

- [experiment script](../experiments/ssrm_3d_irreversible_loss.py)
- [visualization](../visualizations/ssrm_3d_irreversible_loss.html)
- [evaluation CSV](../artifacts/ssrm_3d_irreversible_loss_eval.csv)
- [policy-selection CSV](../artifacts/ssrm_3d_irreversible_loss_policy_selection.csv)
- [summary CSV](../artifacts/ssrm_3d_irreversible_loss_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_irreversible_loss_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_irreversible_loss_trace.json)
- [JSON results](../artifacts/ssrm_3d_irreversible_loss_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_irreversible_loss_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_irreversible_loss_results.js)
