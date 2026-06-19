# Report 363: SSRM-3D Scheduled Anomaly Investigation Bridge

Report 363 moves anomaly discovery out of a panel-only loop and into the maintained shell's resident schedule/resource economy. Residents now plan investigation slots around ordinary work, scarce materials, fear, trust, and social disagreement. Execution can run a resident-owned test, delay work, consume resources, preserve a failed test, refuse, or defer.

Boundary: Browser-local scheduled anomaly investigation only; residents may schedule, defer, refuse, or run anomaly tests around ordinary work and scarce materials, but this is deterministic per seed and remains no LLM call, no autonomous natural language, no subjective consciousness, no real science, no real consent, no moral patienthood, no production persistence, no hosted URL proof, no complete 3D engine, no finished gameplay, and no hard-coded technology tree.

## Result

Verdict: `pass`
Readiness: `1.000`
Weakest channel score: `1.000`
Criteria passed: `19 / 19`

## Browser-smoke evidence

- Maintained shell URL: `http://127.0.0.1:8765/visualizations/ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html?reset=1&report=363&anomalySeed=36231`
- Schedule summary: `5 slots / 2 tests / 2 refusals / 2 work delays`
- Schedule panel: `Schedule seed: 36231
Boundary: browser-local-scheduled-anomaly-investigation-only
Resources before: {"water":12,"fiber":10,"wood":17,"care":6}
Resources now: {"water":11,"fiber":9,"wood":16,"care":4}
Material scarcity blocks: 0
Ordinary work delayed: 2
Refusals/deferments: 2

Scheduled slots:
dawn work block Ari: test_anomaly / work=repair awning / belief=roof-snap / cost=fiber:0,wood:1,care:1,water:1 / fear=0.12 / trust=0.584 / pressure=0.12 / status=test completed / reason=curiosity and available materials beat ordinary work
midday work block Fay: argue_before_test / work=sort herbs / belief=quiet sting-warning-craft / cost=fiber:0,wood:2,care:0,water:1 / fear=0.42 / trust=0.631 / pressure=0.48 / status=deferred by disagreement / reason=social disagreement delays the test
rain pause Milo: argue_before_test / work=carry water / belief=quiet sting-warning / cost=fiber:0,wood:2,care:0,water:1 / fear=0.28 / trust=0.483 / pressure=0.48 / status=deferred by disagreement / reason=social disagreement delays the test
evening repair Sera: test_anomaly / work=dry cloaks / belief=smoke warning / cost=fiber:1,wood:0,care:1,water:0 / fear=0.26 / trust=0.54 / pressure=0.12 / status=failed test preserved / reason=curiosity and available materials beat ordinary work
market gossip Tovan: test_anomaly / work=map safe route / belief=safe-gap / cost=fiber:1,wood:1,care:0,water:0 / fear=0.42 / trust=0.51 / pressure=0.12 / status=planned / reason=curiosity and available materials beat ordinary work

Execution log:
AIS-01 Ari: Ari delayed repair awning, spent scheduled materials, and got loose fiber jumped after rubbing
AIS-02 Fay: Fay kept sort herbs ahead of anomaly testing because social disagreement delays the test
AIS-03 Milo: Milo kept carry water ahead of anomaly testing because social disagreement delays the test
AIS-04 Sera: Sera delayed dry cloaks, spent scheduled materials, and got smoke appeared and the test was stopped`
- Console errors: `0`

## Criteria

| Criterion | Score | Evidence |
| --- | ---: | --- |
| `report_362_anomaly_gate_passing` | `1.0` | Report 362 verdict=pass weakest=1.0 |
| `source_exposes_schedule_state` | `1.0` | app.js exposes scheduled anomaly investigation state/render/boundary |
| `source_plans_and_runs_schedule` | `1.0` | app.js plans and executes resident schedule slots |
| `visible_schedule_panel_wired` | `1.0` | index.html exposes schedule controls and panel |
| `runner_includes_report_363` | `1.0` | scripts/run_experiments.py includes Report 363 module |
| `schedule_competition_binding` | `1.0` | metric=1.0 |
| `resource_scarcity_binding` | `1.0` | metric=1.0 |
| `fear_trust_social_pressure_binding` | `1.0` | metric=1.0 |
| `resident_chosen_test_binding` | `1.0` | metric=1.0 |
| `ordinary_work_tradeoff` | `1.0` | metric=1.0 |
| `refusal_or_defer_preservation` | `1.0` | metric=1.0 |
| `scheduled_failure_preservation` | `1.0` | metric=1.0 |
| `not_panel_only_loop` | `1.0` | metric=1.0 |
| `schedule_replay_integrity` | `1.0` | metric=1.0 |
| `browser_smoke_artifact_exists` | `1.0` | artifacts/ssrm_3d_browser_world_v123_scheduled_anomaly_investigation_bridge_browser_smoke.json |
| `browser_schedule_competition_visible` | `1.0` | Schedule seed: 36231
Boundary: browser-local-scheduled-anomaly-investigation-only
Resources before: {"water":12,"fiber":10,"wood":17,"care":6}
Resources now: {"water":11,"fiber":9,"wood":16,"care":4}
Material scarcity blocks: 0
Ordinary work delayed: 2
Refusals/deferments: 2

Scheduled slots:
dawn work block Ari: test_anomaly / work=repair awning / belief=roof-snap / cost=fiber:0,wood:1,care:1,water:1 / fear=0.12 / trust=0.584 / pressure=0.12 / status=test completed / reason=curiosity and available materials beat ordinary work
midday work block Fay: argue_before_test / work=sort herbs / belief=quiet sting-warning-craft / cost=fiber:0,wood:2,care:0,water:1 / fear=0.42 / trust=0.631 / pressure=0.48 / status=deferred by disagreement / reason=social disagreement delays the test
rain pause Milo: argue_before_test / work=carry water / belief=quiet sting-warning / cost=fiber:0,wood:2,care:0,water:1 / fear=0.28 / trust=0.483 / pressure=0.48 / status=deferred by disagreement / reason=social disagreement delays the test
evening repair Sera: test_anomaly / work=dry cloaks / belief=smoke warning / cost=fiber:1,wood:0,care:1,water:0 / fear=0.26 / trust=0.54 / pressure=0.12 / status=failed test preserved / reason=curiosity and available materials beat ordinary work
market gossip Tovan: test_anomaly / work=map safe route / belief=safe-gap / cost=fiber:1,wood:1,care:0,water:0 / fear=0.42 / trust=0.51 / pressure=0.12 / status=planned / reason=curiosity and available materials beat ordinary work

Execution log:
AIS-01 Ari: Ari delayed repair awning, spent scheduled materials, and got loose fiber jumped after rubbing
AIS-02 Fay: Fay kept sort herbs ahead of anomaly testing because social disagreement delays the test
AIS-03 Milo: Milo kept carry water ahead of anomaly testing because social disagreement delays the test
AIS-04 Sera: Sera delayed dry cloaks, spent scheduled materials, and got smoke appeared and the test was stopped |
| `browser_execution_tradeoff_visible` | `1.0` | Schedule seed: 36231
Boundary: browser-local-scheduled-anomaly-investigation-only
Resources before: {"water":12,"fiber":10,"wood":17,"care":6}
Resources now: {"water":11,"fiber":9,"wood":16,"care":4}
Material scarcity blocks: 0
Ordinary work delayed: 2
Refusals/deferments: 2

Scheduled slots:
dawn work block Ari: test_anomaly / work=repair awning / belief=roof-snap / cost=fiber:0,wood:1,care:1,water:1 / fear=0.12 / trust=0.584 / pressure=0.12 / status=test completed / reason=curiosity and available materials beat ordinary work
midday work block Fay: argue_before_test / work=sort herbs / belief=quiet sting-warning-craft / cost=fiber:0,wood:2,care:0,water:1 / fear=0.42 / trust=0.631 / pressure=0.48 / status=deferred by disagreement / reason=social disagreement delays the test
rain pause Milo: argue_before_test / work=carry water / belief=quiet sting-warning / cost=fiber:0,wood:2,care:0,water:1 / fear=0.28 / trust=0.483 / pressure=0.48 / status=deferred by disagreement / reason=social disagreement delays the test
evening repair Sera: test_anomaly / work=dry cloaks / belief=smoke warning / cost=fiber:1,wood:0,care:1,water:0 / fear=0.26 / trust=0.54 / pressure=0.12 / status=failed test preserved / reason=curiosity and available materials beat ordinary work
market gossip Tovan: test_anomaly / work=map safe route / belief=safe-gap / cost=fiber:1,wood:1,care:0,water:0 / fear=0.42 / trust=0.51 / pressure=0.12 / status=planned / reason=curiosity and available materials beat ordinary work

Execution log:
AIS-01 Ari: Ari delayed repair awning, spent scheduled materials, and got loose fiber jumped after rubbing
AIS-02 Fay: Fay kept sort herbs ahead of anomaly testing because social disagreement delays the test
AIS-03 Milo: Milo kept carry water ahead of anomaly testing because social disagreement delays the test
AIS-04 Sera: Sera delayed dry cloaks, spent scheduled materials, and got smoke appeared and the test was stopped |
| `browser_console_clean` | `1.0` | console error count=0 |
| `claim_boundary_preserved` | `1.0` | Browser-local scheduled anomaly investigation only; residents may schedule, defer, refuse, or run anomaly tests around ordinary work and scarce materials, but this is deterministic per seed and remains no LLM call, no autonomous natural language, no subjective consciousness, no real science, no real consent, no moral patienthood, no production persistence, no hosted URL proof, no complete 3D engine, no finished gameplay, and no hard-coded technology tree. |

## Honest interpretation

This remains deterministic browser-local scaffolding. The non-toy movement is integration: anomaly testing now competes with ordinary resident life and resources, so investigation can be delayed, refused, or failed instead of advancing through a scripted panel path.

## Next gate

post-363: make scheduled anomaly investigation create longer-run relationship consequences when residents disagree about risk, resource use, or whether ordinary work should be delayed
