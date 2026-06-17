# Report 149: SSRM-3D Infrastructure Proposal Governance Bridge

## Purpose

Report 148 let agents build and maintain infrastructure, but the project set was still fixed. Report 149 adds the next bridge: agents create infrastructure proposals from route, object, and maintenance pressures, then councils resolve priority conflict under scarce budgets.

This is still deterministic. It is not subjective consciousness, not LLM-backed open dialogue, not a complete playable world, and not unscripted civilization emergence.

## What changed

- Added `experiments/ssrm_3d_infrastructure_proposal_governance_bridge.py`.
- Added agent-created proposals derived from route pressure, object pressure, and maintenance debt.
- Added council arbitration over conflicting proposals.
- Added scarce material budgets and overreach rejection.
- Added maintenance-debt servicing.
- Added native-token grounding for governance proposals.
- Added fairness rotation across roles.
- Added outcome feedback into routes, objects, projects, and agent governance memory.
- Added `visualizations/ssrm_3d_infrastructure_proposal_governance_bridge.html`, a council/governance viewer.

## Conditions

| Condition | Readiness | Generated | Pressure | Conflict | Budget | Debt | Token | Fairness | Feedback | Complete | Reject overreach | History | Trace |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `integrated_infrastructure_proposal_governance` | `0.921374` | `1.000000` | `0.299004` | `0.465278` | `1.000000` | `0.862745` | `1.000000` | `0.910448` | `1.000000` | `1.000000` | `0.441558` | `1.000000` | `1.000000` |
| `no_agent_created_proposals` | `0.080000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `1.000000` |
| `no_conflict_priority_arbitration` | `0.868325` | `1.000000` | `0.333248` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `0.944444` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` |
| `no_scarce_budget` | `0.327016` | `1.000000` | `0.470160` | `0.000000` | `0.000000` | `0.000000` | `1.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `0.000000` | `1.000000` |
| `no_maintenance_debt` | `0.833741` | `1.000000` | `0.288875` | `0.479167` | `1.000000` | `0.000000` | `1.000000` | `0.927536` | `1.000000` | `1.000000` | `0.373333` | `1.000000` | `1.000000` |
| `no_cultural_language_grounding` | `0.848481` | `1.000000` | `0.307166` | `0.458333` | `1.000000` | `0.952381` | `0.000000` | `0.939394` | `1.000000` | `1.000000` | `0.551282` | `1.000000` | `1.000000` |
| `no_fairness_rotation` | `0.858141` | `1.000000` | `0.303863` | `0.437500` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `0.592593` | `1.000000` | `1.000000` |
| `no_outcome_feedback` | `0.681599` | `1.000000` | `0.470160` | `0.375000` | `1.000000` | `0.000000` | `1.000000` | `0.925926` | `0.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_trace_replay` | `0.841374` | `1.000000` | `0.299004` | `0.465278` | `1.000000` | `0.862745` | `1.000000` | `0.910448` | `1.000000` | `1.000000` | `0.441558` | `1.000000` | `0.000000` |

## Verdict

The integrated condition reaches proposal-governance readiness `0.921374`. It passes this bounded gate with proposal generation `1.000000`, pressure grounding `0.299004`, conflict resolution `0.465278`, scarce-budget allocation `1.000000`, maintenance-debt service `0.862745`, cultural token grounding `1.000000`, fairness rotation `0.910448`, outcome feedback `1.000000`, accepted completion `1.000000`, overreach rejection `0.441558`, governance-history persistence `1.000000`, and trace completeness `1.000000`.

Ablations reduce readiness or remove their required direct channel:

| Ablation | Readiness loss |
|---|---:|
| `no_agent_created_proposals` | `0.841374` |
| `no_conflict_priority_arbitration` | `0.053049` |
| `no_scarce_budget` | `0.594358` |
| `no_maintenance_debt` | `0.087633` |
| `no_cultural_language_grounding` | `0.072893` |
| `no_fairness_rotation` | `0.063233` |
| `no_outcome_feedback` | `0.239775` |
| `no_trace_replay` | `0.080000` |

`supports_infrastructure_proposal_governance_bridge = true`.

`supports_subjective_consciousness = false`.

`supports_llm_open_dialogue = false`.

`supports_complete_playable_world = false`.

`supports_unscripted_civilization = false`.

## Interpretation

Report 149 changes infrastructure from fixed projects into governed choices. The added loop is:

```text
route/object/maintenance pressure -> agent-created proposal -> native-token grounding -> council conflict -> scarce budget allocation -> accepted/rejected outcome -> route/object/project feedback -> governance memory
```

This matters for the larger playable-world goal because civilization needs prioritization, not only construction. Agents must decide what not to build, who receives resources, which maintenance debt is serviced, and how role fairness is preserved over time.

This remains a bridge. The proposal generator is deterministic, councils are scored rather than learned, and language grounding uses existing native-token mappings rather than open dialogue. The next gates are learned proposal generation, persistent political factions, agent disagreement over values, and avatar questioning of governance histories.

## Artifacts

- `artifacts/ssrm_3d_infrastructure_proposal_governance_bridge_eval.csv`
- `artifacts/ssrm_3d_infrastructure_proposal_governance_bridge_verdict.csv`
- `artifacts/ssrm_3d_infrastructure_proposal_governance_bridge_results.json`
- `artifacts/ssrm_3d_infrastructure_proposal_governance_bridge_trace.json`
- `artifacts/ssrm_3d_infrastructure_proposal_governance_bridge_state.json`
- `artifacts/ssrm_3d_infrastructure_proposal_governance_bridge_results.js`
- `artifacts/ssrm_3d_infrastructure_proposal_governance_bridge_trace.js`
- `artifacts/ssrm_3d_infrastructure_proposal_governance_bridge_state.js`
- `visualizations/ssrm_3d_infrastructure_proposal_governance_bridge.html`

## Reproduction

```bash
python3 -m experiments.ssrm_3d_deep_time_playable_bridge
python3 -m experiments.ssrm_3d_live_avatar_intervention_bridge
python3 -m experiments.ssrm_3d_embodied_avatar_input_bridge
python3 -m experiments.ssrm_3d_autonomous_live_agent_loop_bridge
python3 -m experiments.ssrm_3d_affordance_object_ecology_bridge
python3 -m experiments.ssrm_3d_place_navigation_object_bridge
python3 -m experiments.ssrm_3d_agent_made_infrastructure_bridge
python3 -m experiments.ssrm_3d_infrastructure_proposal_governance_bridge
```
