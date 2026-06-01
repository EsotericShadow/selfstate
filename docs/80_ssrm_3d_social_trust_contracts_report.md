# SSRM-3D Social Trust/Contracts Report

## Question

Do promises and obligations create persistent social control pressure without turning the simulation into roleplay?

Report 74 puts social trust/contracts after structured perception, sleep/rest, illness/sanitation, weather/exposure, and tool/shelter degradation. This experiment asks whether commitment memory, identity memory, communication, trust updates, ownership memory, repair debt, and restore continuity become useful only when they change future access, help, tool use, shelter safety, or social punishment.

The tested claim is narrow:

> Contract machinery should be rejected in a stable visible control, but selected when delayed social consequences change future options.

This is not a society simulation. It tests promises and obligations as control pressure.

## Method

Canonical command:

```bash
python3 experiments/ssrm_3d_social_trust_contracts.py --train-episodes 72 --eval-episodes 96 --seed 20260625 --candidate-count 7
```

The experiment uses return-selected candidate policies over abstract social control state. Policies can use:

| Channel | Role |
|---|---|
| commitment memory | tracks outstanding promises through time |
| identity memory | binds obligations to the correct persistent agent |
| communication action | accepts, warns, shares, returns, or confirms obligations |
| trust update | converts kept or broken commitments into future access predictions |
| ownership memory | tracks borrowed tools and return obligations |
| repair debt memory | tracks assigned shared-shelter maintenance duties |
| continuity memory | preserves outstanding obligations after restore |

Evaluation conditions:

| Condition | Test |
|---|---|
| `full_control` | intact contract control |
| `no_commitment_memory` | removes outstanding-promise memory |
| `no_identity_memory` | removes binding to the right social identity |
| `no_communication_action` | removes costly promise/warning/share/return actions |
| `no_trust_update` | removes future social-consequence updates |
| `no_ownership_memory` | removes borrowed-tool ownership state |
| `no_repair_debt` | removes shared maintenance duty state |
| `no_continuity` | removes restore-time obligation continuity |
| `short_term_selfish` | accepts short-term benefit but breaks costly obligations |
| `omniscient_contract_control` | upper-bound contract control |

## Results

| Scenario | Selected policy | Commitment loss | Identity loss | Communication loss | Trust loss | Ownership loss | Repair-debt loss | Continuity loss | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| `visible_no_contract_control` | `no_contract_baseline` | 0.004 | 0.012 | 0.039 | 0.030 | -0.005 | 0.012 | -0.050 | contracts rejected in visible control |
| `borrowed_tool_return_contract` | `tool_return_contract_keeper` | 353.614 | 371.616 | 353.695 | 286.314 | 286.369 | -0.122 | -0.110 | tool-return contract preserves access |
| `hazard_warning_promise` | `hazard_warning_contract_keeper` | 380.509 | 398.670 | 380.561 | 373.777 | 0.153 | -0.012 | -0.014 | hazard-warning promise preserves help |
| `reciprocal_resource_sharing` | `resource_reciprocity_contract_keeper` | 283.081 | 306.714 | 286.155 | 279.251 | 8.461 | 12.928 | 9.434 | sharing contract buys reciprocity |
| `shared_shelter_repair_contract` | `shelter_repair_contract_keeper` | 376.107 | 394.019 | 376.062 | 369.528 | -0.072 | 369.435 | 0.070 | repair contract preserves infrastructure |
| `restore_contract_continuity` | `continuity_contract_keeper` | 377.231 | 395.139 | 377.089 | 370.076 | 370.464 | 370.371 | 561.503 | restore continuity preserves social access |

All six verdict rows pass `supports_social_trust_contracts_precursor=True`.

Key targeted losses:

- `visible_no_contract_control`: contract machinery is not selected and all ablations have near-zero effect.
- `borrowed_tool_return_contract`: removing commitment, identity, communication, trust update, or ownership causes large loss.
- `hazard_warning_promise`: removing communication, commitment, identity, or trust update causes large loss.
- `reciprocal_resource_sharing`: sharing is costly short-term, but commitment, identity, communication, and trust update preserve future reciprocity.
- `shared_shelter_repair_contract`: repair duty matters only when shared shelter quality depends on remembered obligations.
- `restore_contract_continuity`: restore-time loss of obligations creates the largest targeted failure.

## Interpretation

This result supports the sixth pressure-layer step at precursor level:

- promises are not globally useful;
- communication matters only when it carries a costly obligation or warning;
- identity matters because obligations attach to persistent agents;
- trust update matters because kept or broken commitments change future access;
- ownership matters when borrowed tools must be returned;
- repair debt matters when shared infrastructure has assigned duties;
- continuity matters when restore can erase outstanding obligations.

The boundary remains explicit:

> A promise is not selfhood. Contracts become relevant to selfhood only when the agent must model itself as a continuing social object whose past commitments alter future options.

Some selected policies carry extra channels whose ablations are neutral in that row. Those are not positive evidence for those channels. The evidence comes only from targeted losses in matching regimes.

## Limits

- Candidate policies are supplied and return-selected.
- Social contract dynamics are abstract control variables, not open-ended society.
- Promise types, trust updates, ownership, repair debt, and continuity are designed channels.
- The selected planner is not an online RL agent discovering contracts from scratch.
- This report itself does not include predators, resource ecology, territorial conflict, development, dependent care, or irreversible loss.

## Next Test

The implemented follow-up adds predator/threat agents:

- threats should track sound, scent, weakness, routines, or social disclosure;
- fear-like control state should bias attention, shelter use, stealth, group defense, or alarms;
- ablations should separate threat perception, self-vulnerability state, sound/scent memory, social warning, tool alarm, shelter, and continuity.

Implemented by [report 81](81_ssrm_3d_predator_threat_agents_report.md).

## Visualization

Serve the repo root and open:

```text
http://127.0.0.1:8765/visualizations/ssrm_3d_social_trust_contracts.html
```

The page replays the `shared_shelter_repair_contract` trace with trust, reputation, future access, resources, shelter quality, social penalty, kept/broken commitments, actions, and ablation outcomes.

## Artifacts

- [experiment script](../experiments/ssrm_3d_social_trust_contracts.py)
- [visualization](../visualizations/ssrm_3d_social_trust_contracts.html)
- [evaluation CSV](../artifacts/ssrm_3d_social_trust_contracts_eval.csv)
- [policy-selection CSV](../artifacts/ssrm_3d_social_trust_contracts_policy_selection.csv)
- [summary CSV](../artifacts/ssrm_3d_social_trust_contracts_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_social_trust_contracts_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_social_trust_contracts_trace.json)
- [JSON results](../artifacts/ssrm_3d_social_trust_contracts_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_social_trust_contracts_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_social_trust_contracts_results.js)
