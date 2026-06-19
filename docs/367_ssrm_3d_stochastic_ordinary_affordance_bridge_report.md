# Report 367: SSRM-3D Stochastic Ordinary Affordance Bridge

Report 367 attaches stochastic history influence to ordinary play affordances. Normal `Offer help`, `Talk`, `Ask schedule`, and movement can now be biased by recovered, pending, or stabilized stochastic recovery history instead of requiring the reviewer to press a dedicated history panel button.

Boundary: Browser-local stochastic ordinary-affordance influence only. Recovered, pending, and stabilized stochastic history can bias normal actions such as Offer help, Talk, Ask schedule, and Movement while preserving source choice IDs, recovery paths, no-permanent-penalty flags, and no-LLM/no-consciousness boundaries.

## Result

Verdict: `pass`
Readiness: `1.000`
Weakest channel score: `1.000`
Criteria passed: `19 / 19`

## Browser-smoke evidence

- Maintained shell URL: `http://127.0.0.1:8765/visualizations/ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html?reset=1&report=367`
- Normal influence summary: `4 normal actions / 2 bounded blocks / 1 movement biases`
- Normal influence excerpt: `Boundary: browser-local-stochastic-ordinary-affordance-only; no LLM call, no subjective consciousness, no moral patienthood
Policy: stochastic history may bias ordinary actions, but normal play keeps source IDs and recovery paths visible
Source history choices: 2

Normal action records:
SOA-01 Ari: talkBounded / decision=bounded_refusal_until_recovery / outcome=pending recovery creates bounded caution / blocked=false / moveScale=1 / source=SHC-01 / permanentPenalty=false
SOA-02 Ari: askSchedule / decision=bounded_refusal_until_recovery / outcome=pending recovery creates bounded caution / blocked=true / moveScale=1 / source=SHC-01 / permanentPenalty=false
SOA-03 Ari: offerHelp / decision=bounded_refusal_until_recovery / outcome=pending recovery creates bounded caution / blocked=true / moveScale=1 / source=SHC-01 / permanentPenalty=false
SOA-04 Ari: moveEast / decision=bounded_refusal_until_recovery / outcome=pending recovery creates bounded caution / blocked=false / moveScale=0.5 / source=SHC-01 / permanentPenalty=false

Source ledger:
SOA-01: SHC-01 -> talkBounded
SOA-02: SHC-01 -> askSchedule
SOA-03: SHC-01 -> offerHelp
SOA-04: SHC-01 -> moveEast`
- Console errors: `0`

## Criteria

| Criterion | Score | Evidence |
| --- | ---: | --- |
| `report_366_history_gate_passing` | `1.0` | Report 366 verdict=pass weakest=1.0 |
| `source_declares_ordinary_boundary` | `1.0` | app.js declares ordinary-affordance influence state |
| `source_normal_actions_call_influence` | `1.0` | normal shell actions call stochastic history influence |
| `visible_ordinary_panel_wired` | `1.0` | index.html exposes normal influence panel and controls |
| `runner_includes_report_367` | `1.0` | scripts/run_experiments.py includes Report 367 module |
| `ordinary_action_binding` | `1.0` | metric=1.0 |
| `offer_help_influence` | `1.0` | metric=1.0 |
| `talk_influence` | `1.0` | metric=1.0 |
| `schedule_influence` | `1.0` | metric=1.0 |
| `movement_influence` | `1.0` | metric=1.0 |
| `bounded_refusal_blocks_help` | `1.0` | metric=1.0 |
| `source_link_integrity` | `1.0` | metric=1.0 |
| `no_permanent_penalty` | `1.0` | metric=1.0 |
| `not_panel_only_loop` | `1.0` | metric=1.0 |
| `browser_surface_wired` | `1.0` | metric=1.0 |
| `browser_smoke_artifact_exists` | `1.0` | artifacts/ssrm_3d_browser_world_v127_stochastic_ordinary_affordance_bridge_browser_smoke.json |
| `browser_ordinary_influence_visible` | `1.0` | Boundary: browser-local-stochastic-ordinary-affordance-only; no LLM call, no subjective consciousness, no moral patienthood
Policy: stochastic history may bias ordinary actions, but normal play keeps source IDs and recovery paths visible
Source history choices: 2

Normal action records:
SOA-01 Ari: talkBounded / decision=bounded_refusal_until_recovery / outcome=pending recovery creates bounded caution / blocked=false / moveScale=1 / source=SHC-01 / permanentPenalty=false
SOA-02 Ari: askSchedule / decision=bounded_refusal_until_recovery / outcome=pending recovery creates bounded caution / blocked=true / moveScale=1 / source=SHC-01 / permanentPenalty=false
SOA-03 Ari: offerHelp / decision=bounded_refusal_until_recovery / outcome=pending recovery creates bounded caution / blocked=true / moveScale=1 / source=SHC-01 / permanentPenalty=false
SOA-04 Ari: moveEast / decision=bounded_refusal_until_recovery / outcome=pending recovery creates bounded caution / blocked=false / moveScale=0.5 / source=SHC-01 / permanentPenalty=false

Source ledger:
SOA-01: SHC-01 -> talkBounded
SOA-02: SHC-01 -> askSchedule
SOA-03: SHC-01 -> offerHelp
SOA-04: SHC-01 -> moveEast |
| `browser_normal_actions_visible` | `1.0` | Boundary: browser-local-stochastic-ordinary-affordance-only; no LLM call, no subjective consciousness, no moral patienthood
Policy: stochastic history may bias ordinary actions, but normal play keeps source IDs and recovery paths visible
Source history choices: 2

Normal action records:
SOA-01 Ari: talkBounded / decision=bounded_refusal_until_recovery / outcome=pending recovery creates bounded caution / blocked=false / moveScale=1 / source=SHC-01 / permanentPenalty=false
SOA-02 Ari: askSchedule / decision=bounded_refusal_until_recovery / outcome=pending recovery creates bounded caution / blocked=true / moveScale=1 / source=SHC-01 / permanentPenalty=false
SOA-03 Ari: offerHelp / decision=bounded_refusal_until_recovery / outcome=pending recovery creates bounded caution / blocked=true / moveScale=1 / source=SHC-01 / permanentPenalty=false
SOA-04 Ari: moveEast / decision=bounded_refusal_until_recovery / outcome=pending recovery creates bounded caution / blocked=false / moveScale=0.5 / source=SHC-01 / permanentPenalty=false

Source ledger:
SOA-01: SHC-01 -> talkBounded
SOA-02: SHC-01 -> askSchedule
SOA-03: SHC-01 -> offerHelp
SOA-04: SHC-01 -> moveEast |
| `browser_console_clean` | `1.0` | console error count=0 |

## Honest interpretation

This is still bounded browser-local scaffolding, but it is a material integration step: stochastic history now changes normal affordances the user already presses. It keeps source IDs and no-permanent-penalty flags, so the behavior is less scripted without becoming opaque or punitive.

## Next gate

post-367: make ordinary-affordance influence persist across save/restore and return sessions, then surface it through resident body language instead of only text panels
