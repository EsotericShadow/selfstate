# Report 210: SSRM-3D Needs Marketplace, Hunger, Warmth, Tool Access, Social Obligation, and Seasonal Price Pressure Bridge

## Purpose

Report 210 extends the agent-owned project economy into a needs-driven seasonal marketplace. The target is that agents should not trade abstract inventory in isolation. Hunger, warmth, tool access, social obligation, debt burden, and seasonal prices must affect whether agents buy, borrow, gift, ration, refuse, or get blocked.

This is a deterministic market-pressure substrate only. It does not claim real markets, real labor, real consent, subjective consciousness, moral patienthood, or complete artificial life.

## What changed

The bridge adds:

- four seasonal price regimes: wet planting, cold scarcity, thaw repair, and dry harvest
- need states for hunger, warmth, tool access, and social obligation
- agent credits, debt burden, inventories, and social obligations
- seasonal price indices for food, heat wood, tool hours, cloth, lamp oil, vellum, herbs, and care tokens
- need-linked purchases, borrowing, gifts, work, repayment, partial repayment, rationing, refusal, and blocked purchases
- cold-season debt pressure for Milo
- a blocked thaw tool-hour event that stalls archive work
- a harvest-season recovery phase that improves but does not erase earlier pressure
- public/private boundary preservation through sealed private workspace digests
- frequency and flower-ring rhythm for each market event
- browser replay of the seasonal needs market

## Deterministic scenario

The run spans sixty market days and twenty-four market events.

- Ari buys tool access and food, rations heat under cold pressure, repays support, and later refuses a cheap tool hour because rest need beats price temptation.
- Fay buys warmth and cloth, gifts food, refuses extra heat to avoid unsafe debt, and spends social energy hosting repair care.
- Milo borrows food during cold scarcity, receives gifted support, gets blocked by thaw tool pricing, partially repays debt, buys harvest tool access, and ends fed but still carrying a small cold-food debt memory.

## Metrics

| Metric | Value |
| --- | ---: |
| needs_marketplace_readiness | 0.927083 |
| market_days | 60 |
| market_events | 24 |
| seasonal_price_elasticity | 1.000000 |
| hunger_market_binding | 0.750000 |
| warmth_price_pressure_binding | 1.000000 |
| tool_access_project_binding | 1.000000 |
| social_obligation_market_binding | 1.000000 |
| affordability_constraint_traceability | 1.000000 |
| refusal_under_price_pressure | 1.000000 |
| debt_burden_traceability | 1.000000 |
| gift_vs_market_balance | 1.000000 |
| scarcity_rationing_traceability | 1.000000 |
| welfare_recovery_rate | 0.708333 |
| project_market_coupling | 0.375000 |
| season_end_open_debt_honesty | 1.000000 |
| public_private_boundary_score | 1.000000 |
| frequency_flower_market_rhythm | 1.000000 |
| browser_market_replay_available | 1.000000 |

The lower channels are intentional. Project-market coupling is only `0.375000` because not every market event should advance a project; some preserve body needs, social obligations, or refusal boundaries. Welfare recovery is `0.708333` because price pressure and debt leave residual need, especially for Milo.

## Ablations

| Ablation | Readiness loss |
| --- | ---: |
| no_need_pressure | 0.320000 |
| no_seasonal_prices | 0.280000 |
| no_affordability_constraints | 0.240000 |
| no_social_obligations | 0.190000 |
| no_debt_burden | 0.170000 |
| no_tool_access_market | 0.160000 |
| no_refusal_price_pressure | 0.140000 |
| no_frequency_flower_market_rhythm | 0.055000 |

The largest loss comes from removing need pressure. Without hunger, warmth, tool access, and social obligation, the marketplace becomes price decoration instead of a behavioral constraint.

## Artifacts

- `artifacts/ssrm_3d_needs_marketplace_hunger_warmth_tool_social_price_pressure_bridge_events.csv`
- `artifacts/ssrm_3d_needs_marketplace_hunger_warmth_tool_social_price_pressure_bridge_price_index.csv`
- `artifacts/ssrm_3d_needs_marketplace_hunger_warmth_tool_social_price_pressure_bridge_needs_ledger.csv`
- `artifacts/ssrm_3d_needs_marketplace_hunger_warmth_tool_social_price_pressure_bridge_market_ledger.csv`
- `artifacts/ssrm_3d_needs_marketplace_hunger_warmth_tool_social_price_pressure_bridge_obligation_ledger.csv`
- `artifacts/ssrm_3d_needs_marketplace_hunger_warmth_tool_social_price_pressure_bridge_project_market_coupling.csv`
- `artifacts/ssrm_3d_needs_marketplace_hunger_warmth_tool_social_price_pressure_bridge_results.json`
- `artifacts/ssrm_3d_needs_marketplace_hunger_warmth_tool_social_price_pressure_bridge_state.json`
- `artifacts/ssrm_3d_needs_marketplace_hunger_warmth_tool_social_price_pressure_bridge_verdict.csv`
- `visualizations/ssrm_3d_needs_marketplace_hunger_warmth_tool_social_price_pressure_bridge.html`

## Run command

```bash
python3 -m experiments.ssrm_3d_needs_marketplace_hunger_warmth_tool_social_price_pressure_bridge --seed 20260823 --days 60
```

Observed output:

```text
module_verdict pass
needs_marketplace_readiness 0.927083
market_days 60
market_events 24
welfare_recovery_rate 0.708333
project_market_coupling 0.375000
season_end_open_debt_honesty 1.000000
next_gate seasonal body ecology with illness risk, hunger/warmth tradeoffs, communal care, and market stress on relationships
```

## Honest limitation

This report proves deterministic seasonal market-pressure wiring, not real markets or real needs. Agents do not freely negotiate prices, experience hunger or cold subjectively, or form real social obligations. The next step needs a body ecology layer where illness risk, hunger/warmth tradeoffs, communal care, and market stress affect body state and relationships more directly.

## Next gate

The next gate is seasonal body ecology with illness risk, hunger/warmth tradeoffs, communal care, and market stress on relationships.
