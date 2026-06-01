# SSRM-3D Dependent Care Report

## Question

Does a fragile companion create persistent control pressure without turning the simulation into reproduction or roleplay?

Report 74 puts dependent care after structured perception, sleep/rest, illness/sanitation, weather/exposure, tool/shelter degradation, social trust/contracts, predator/threat agents, resource ecology, injury/disability adaptation, and development/skill learning. This experiment asks whether dependent state, identity memory, protection, resource sharing, repair, teaching, shelter coordination, promise keeping, social trust, priority arbitration, and continuity become useful only when another persistent agent changes future options.

The test is narrow:

> Care machinery should be rejected in a no-dependent control, but selected when fragile-companion viability creates protection, resource, repair, teaching, promise, social, priority, or restore-time consequences.

This is not dependent psychology or reproduction. It tests caregiving as delayed control pressure.

## Command

```bash
python3 experiments/ssrm_3d_dependent_care.py --train-episodes 72 --eval-episodes 96 --seed 20260630 --candidate-count 7
```

## Mechanisms

| Mechanism | Control role |
|---|---|
| dependent state | tracks dependent health, energy, skill, safety, and trust |
| identity memory | binds care history to a persistent fragile companion |
| protection planning | spends present action budget to reduce dependent hazard risk |
| resource sharing | trades self/resource margin against dependent viability |
| repair care | reduces future burden from dependent damage |
| teaching support | improves dependent future competence at immediate cost |
| shelter coordination | moves the pair toward lower exposure |
| promise commitment | preserves social access when care promises matter |
| social trust | changes future cooperation and help access |
| priority arbitration | delays work when care, resource, stress, or safety conflicts dominate |
| continuity memory | preserves dependent state, identity, promises, shelter, trust, and teaching history after restore |

## Conditions

| Condition | Meaning |
|---|---|
| `full_control` | intact dependent-care control |
| `no_dependent_state` | removes dependent health/energy/skill/safety/trust tracking |
| `no_identity_memory` | removes persistent dependent identity and care history |
| `no_protection_planning` | removes active dependent protection |
| `no_resource_sharing` | removes resource allocation to the dependent |
| `no_repair_care` | removes dependent repair action |
| `no_teaching_support` | removes dependent teaching action |
| `no_shelter_coordination` | removes pair-level shelter movement |
| `no_promise_commitment` | removes care-promise maintenance |
| `no_social_trust` | removes social trust/access updates |
| `no_priority_arbitration` | removes sacrifice/priority arbitration |
| `no_continuity` | removes restore-time dependent-care continuity |
| `self_only_baseline` | acts as if no dependent exists |
| `omniscient_care_control` | upper-bound care control |

## Results

Loss values are mean reward loss from the selected `full_control` policy.

| Scenario | Selected policy | dependent | identity | protect | share | repair | teach | shelter | promise | social | priority | continuity | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `no_dependent_control` | `self_only_baseline` | 0.025 | 0.009 | 0.041 | 0.020 | 0.036 | 0.027 | 0.016 | 0.023 | 0.001 | 0.026 | -0.006 | care rejected |
| `fragile_companion_protection` | `protection_shelter_planner` | 484.087 | 295.909 | 599.068 | -0.015 | -0.002 | 0.007 | 125.565 | 0.007 | -0.003 | 431.560 | -0.022 | protection pressure |
| `resource_sharing_tradeoff` | `sharing_priority_planner` | 259.806 | 86.216 | 0.017 | 612.181 | 0.009 | 0.022 | -0.009 | 0.027 | 0.003 | 421.475 | 0.001 | sharing pressure |
| `repair_teaching_burden` | `repair_teaching_planner` | 380.224 | 303.193 | 0.004 | 0.001 | 504.185 | 170.123 | 0.009 | -0.004 | -0.001 | 435.318 | -0.001 | repair/teaching pressure |
| `promise_trust_care` | `promise_trust_planner` | 212.964 | 172.500 | -0.010 | 417.565 | -0.004 | -0.001 | -0.028 | 200.500 | 190.581 | 438.243 | -0.024 | promise/trust pressure |
| `restore_dependent_continuity` | `continuity_care_planner` | 512.835 | 107.396 | 412.598 | 431.583 | 361.288 | 94.711 | 76.102 | 112.653 | 111.195 | 393.748 | 88.752 | restore pressure |

All six verdict rows pass `supports_dependent_care_precursor=True`.

## Interpretation

This result supports the eleventh pressure-layer step at precursor level:

- care machinery is rejected when there is no dependent agent;
- dependent state matters when another persistent agent's viability changes future options;
- identity memory matters when care history belongs to a particular companion;
- protection, shelter, sharing, repair, and teaching matter only under matching asymmetric needs;
- promises and social trust become care-relevant when neglect changes future access;
- priority arbitration matters when immediate work conflicts with another agent's survival or trust;
- continuity matters when restore can erase dependent state, promises, shelter, trust, teaching, or social history.

The anti-overclaim boundary is:

> Dependent care is not selfhood. It becomes relevant to selfhood only when the agent must model another persistent vulnerable agent as a control variable that changes its own future options, obligations, trust, resource use, and continuity.

## Limits

- Candidate policies are supplied and return-selected.
- Care dynamics are abstract control variables, not caregiving psychology.
- The selected planner is not an online RL agent discovering care from scratch.
- This does not yet include irreversible loss, loss-response control state, or permanent relationship/tool/shelter loss.

## Follow-Up

The direct follow-up is now implemented in [report 86](86_ssrm_3d_irreversible_loss_report.md). It adds irreversible loss:

- agents, tools, shelters, memories, and relationships can be permanently lost;
- risk policy should change when recovery is impossible;
- loss-response or caution-like control state should be testable only as attention/risk/memory arbitration, not subjective feeling;
- ablations should separate loss memory, value-at-risk, replacement feasibility, social loss, tool/shelter loss, and continuity.

## Visualization

Serve the repo root and open:

```text
http://127.0.0.1:8765/visualizations/ssrm_3d_dependent_care.html
```

The page replays the `promise_trust_care` trace with dependent health, energy, skill, safety, trust, resource level, shelter safety, promise standing, social access, actions, and ablation outcomes.

## Artifacts

- [experiment script](../experiments/ssrm_3d_dependent_care.py)
- [visualization](../visualizations/ssrm_3d_dependent_care.html)
- [evaluation CSV](../artifacts/ssrm_3d_dependent_care_eval.csv)
- [policy-selection CSV](../artifacts/ssrm_3d_dependent_care_policy_selection.csv)
- [summary CSV](../artifacts/ssrm_3d_dependent_care_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_dependent_care_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_dependent_care_trace.json)
- [JSON results](../artifacts/ssrm_3d_dependent_care_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_dependent_care_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_dependent_care_results.js)
