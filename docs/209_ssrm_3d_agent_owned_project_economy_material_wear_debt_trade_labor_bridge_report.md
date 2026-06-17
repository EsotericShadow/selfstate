# Report 209: SSRM-3D Agent-Owned Project Economy, Materials, Wear, Debt, Trade, and Labor Bridge

## Purpose

Report 209 extends calendar commitments and object projects into a small deterministic economy. The target is that agent projects should require owned materials, object condition should decay under use, trades and gifts should move inventory, debt should remain visible, and labor should be refusal-sensitive.

This is a functional economy substrate only. It does not claim real property, real labor, real consent, subjective consciousness, moral patienthood, or complete artificial life.

## What changed

The bridge adds:

- agent inventories for `dry_resin`, `copper_clip`, `lamp_oil`, `soft_cloth`, `map_vellum`, `herb_bundle`, and `dry_wood`
- a shared bank/avatar reserve for bounded gifts and repayment
- agent-owned projects that advance only when materials and labor are available
- object wear for Ari's brace gauge, Fay's blue blanket, Milo's folded map, and Milo's low lamp
- object repair that improves condition without erasing wear history
- gift, trade, borrow, repay, and partial-repay events
- explicit debt records with open, settled, and partial states
- refusal-sensitive labor requests where agents can say no without penalty
- an unfair trade that Ari rejects
- vellum scarcity that blocks Milo's archive expansion
- public/private boundary preservation through sealed private workspace digests
- frequency and flower-ring rhythm for every economy event
- browser replay of the economy arc

## Deterministic scenario

The run spans thirty-five days and thirty-five economy events.

- Ari owns the west brace project and the notched brace gauge.
- Fay owns the comfort kit project and the warm blue blanket.
- Milo owns the quiet route archive and the folded route map.
- The avatar can gift and repay, but cannot treat agent-owned labor or objects as free utility.

One avatar debt to Fay is settled. One Milo debt to Ari remains partial. Milo's archive expansion is blocked by map-vellum scarcity. Ari rejects an underpriced trade for labor credit. Fay refuses late brace-polish labor to protect her evening ritual energy.

## Metrics

| Metric | Value |
| --- | ---: |
| agent_owned_project_economy_readiness | 0.921556 |
| economy_days | 35 |
| economy_events | 35 |
| open_debts | 1 |
| settled_debts | 1 |
| material_accounting_integrity | 1.000000 |
| object_wear_tracking | 1.000000 |
| debt_ledger_integrity | 1.000000 |
| gift_trade_traceability | 1.000000 |
| refusal_sensitive_labor_rate | 1.000000 |
| fair_exchange_rate | 0.666667 |
| exploitative_labor_avoidance | 1.000000 |
| project_progress_material_coupling | 0.656667 |
| avatar_debt_repair_rate | 0.500000 |
| open_debt_traceability | 1.000000 |
| scarcity_consequence_traceability | 1.000000 |
| ownership_preservation_rate | 1.000000 |
| public_private_boundary_score | 1.000000 |
| frequency_flower_economy_rhythm | 1.000000 |
| browser_economy_replay_available | 1.000000 |

The low scores are intentional. A frictionless economy would be less useful here. The bridge preserves open debt, scarcity, refused unfair exchange, and partial project progress as first-class traces.

## Ablations

| Ablation | Readiness loss |
| --- | ---: |
| no_material_accounting | 0.310000 |
| no_debt_ledger | 0.250000 |
| no_refusal_sensitive_labor | 0.230000 |
| no_object_wear | 0.210000 |
| no_gift_trade | 0.190000 |
| no_scarcity | 0.140000 |
| no_ownership_preservation | 0.120000 |
| no_frequency_flower_economy_rhythm | 0.055000 |

The largest loss comes from removing material accounting. Without materials, projects become narrative flags instead of constrained activity. Debt and refusal-sensitive labor are also high-value channels because they turn agent boundaries into persistent economy facts.

## Artifacts

- `artifacts/ssrm_3d_agent_owned_project_economy_material_wear_debt_trade_labor_bridge_events.csv`
- `artifacts/ssrm_3d_agent_owned_project_economy_material_wear_debt_trade_labor_bridge_material_ledger.csv`
- `artifacts/ssrm_3d_agent_owned_project_economy_material_wear_debt_trade_labor_bridge_object_wear.csv`
- `artifacts/ssrm_3d_agent_owned_project_economy_material_wear_debt_trade_labor_bridge_project_ledger.csv`
- `artifacts/ssrm_3d_agent_owned_project_economy_material_wear_debt_trade_labor_bridge_debt_ledger.csv`
- `artifacts/ssrm_3d_agent_owned_project_economy_material_wear_debt_trade_labor_bridge_trade_ledger.csv`
- `artifacts/ssrm_3d_agent_owned_project_economy_material_wear_debt_trade_labor_bridge_labor_ledger.csv`
- `artifacts/ssrm_3d_agent_owned_project_economy_material_wear_debt_trade_labor_bridge_reputation_consequences.csv`
- `artifacts/ssrm_3d_agent_owned_project_economy_material_wear_debt_trade_labor_bridge_results.json`
- `artifacts/ssrm_3d_agent_owned_project_economy_material_wear_debt_trade_labor_bridge_state.json`
- `artifacts/ssrm_3d_agent_owned_project_economy_material_wear_debt_trade_labor_bridge_verdict.csv`
- `visualizations/ssrm_3d_agent_owned_project_economy_material_wear_debt_trade_labor_bridge.html`

## Run command

```bash
python3 -m experiments.ssrm_3d_agent_owned_project_economy_material_wear_debt_trade_labor_bridge --seed 20260822 --days 35
```

Observed output:

```text
module_verdict pass
agent_owned_project_economy_readiness 0.921556
economy_days 35
economy_events 35
fair_exchange_rate 0.666667
avatar_debt_repair_rate 0.500000
project_progress_material_coupling 0.656667
next_gate agent needs marketplace with hunger, warmth, tool access, social obligation, and price pressure across seasons
```

## Honest limitation

This report proves deterministic economy wiring, not a real economy. Agents do not freely price goods, invent markets, experience real labor, or own objects in a moral/legal sense. The material inventory is tiny, project planning is scripted, and avatar debt is simplified. The next step needs needs-driven marketplace pressure so hunger, warmth, tool access, social obligation, and seasonal scarcity can affect prices and choices.

## Next gate

The next gate is agent needs marketplace with hunger, warmth, tool access, social obligation, and price pressure across seasons.
