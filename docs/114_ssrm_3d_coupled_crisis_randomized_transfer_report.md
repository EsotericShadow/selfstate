# SSRM-3D Coupled Crisis Randomized-Transfer Report

## Question

Report 113 showed that separate learned environmental and social action heads can pass the stricter coupled-crisis gate when a validation-selected joint coordinator keeps both repair channels active.

This report tests the next weakness:

```text
Does that joint-arbitration controller survive randomized post-12h crisis timing, ordering, repetition, and initial world pressure?
```

The goal is to move the 12h+ development world away from one fixed crisis schedule. No major crisis is allowed before the 12h development gate, but after that gate each seed gets a different sequence of repeated crises across a 96h run.

## What Changed

This benchmark reuses the Report 113 controller family and changes the world wrapper:

- simulated duration extends from `72h` to `96h`;
- crisis schedules are randomized per seed instead of fixed at 14h, 27h, 42h, and 57h;
- crisis order and repetition vary across train, tune, and eval seeds;
- evaluation seeds average `5.8` post-gate crises each;
- initial food, water, medicine, shelter, architecture, tools, sanitation, trust, conflict, contamination, disease, route hazard, resource migration, and predator pressure vary by seed;
- learned inputs still do not receive active crisis profile labels.

The test keeps the same bounded discipline as Report 113. It is allowed to fail if the selected coordinator only works on the standard schedule.

## What This Does Not Claim

This is not actor-critic reinforcement learning, policy-gradient training, open-ended civilization, subjective consciousness, or a production software controller.

It is a randomized-transfer stress test for a structured learned-coordination precursor.

## Canonical Command

```bash
python3 experiments/ssrm_3d_coupled_crisis_randomized_transfer_controller.py --train-seeds 20260911,20260912,20260913,20260914,20260915,20260916 --tune-seeds 20261111,20261112,20261113 --eval-seeds 20261121,20261122,20261123,20261124,20261125 --hours 96 --step-hours 0.10 --population 14 --epochs 42 --hidden-size 64 --action-epochs 64 --action-hidden-size 64 --joint-candidates 0.00:0.00:0.00,0.10:0.10:0.70,0.12:0.12:0.80,0.14:0.14:0.90,0.16:0.14:1.00,0.14:0.16:1.00,0.18:0.16:1.10,0.16:0.18:1.10,0.20:0.18:1.20 --device auto --trace-seed 20261121
```

## Result

Validation selects:

```text
selected_router = social_first
selected_env_quota = 0.14
selected_social_quota = 0.14
selected_coordinator_strength = 0.90
mean_eval_crisis_count = 5.8
```

Held-out randomized evaluation:

| Controller | Total score | Crisis score | Resolved rate | Coupled response |
|---|---:|---:|---:|---:|
| joint-arbitration GRU | `0.849` | `0.706` | `0.967` | `0.965` |
| return-selected GRU | `0.512` | `0.000` | `0.067` | `0.055` |
| base GRU | `0.344` | `0.000` | `0.000` | `0.000` |
| designed | `0.755` | `0.521` | `1.000` | `0.000` |
| frame MLP | `0.284` | `0.000` | `0.000` | `0.000` |
| reactive | `0.095` | `0.000` | `0.000` | `0.000` |

As in Report 113, `coupled_response` measures simultaneous environmental/social response within the crisis window. The designed controller resolves crises through its scripted threshold path without optimizing that overlap metric, so its resolved rate can be high while coupled response is `0.000`.

The important transfer gains over the return-selected GRU are:

```text
total score gain = 0.337
crisis score gain = 0.706
resolved-rate gain = 0.900
coupled-response gain = 0.910
```

The verdict is:

```text
supports_randomized_transfer = true
supports_social_environment_dependency = true
verdict = pass
```

## Randomized Schedule Boundary

Held-out eval schedules:

| Seed | Crisis count | First crisis | Last crisis | Profile sequence |
|---:|---:|---:|---:|---|
| `20261121` | `6` | `15.985h` | `77.641h` | quarantine, storm, quarantine, storm, quarantine, contaminated water |
| `20261122` | `5` | `15.283h` | `77.612h` | storm, quarantine, contaminated water, route migration, storm |
| `20261123` | `6` | `17.134h` | `87.749h` | storm, contaminated water, quarantine, route migration, quarantine, route migration |
| `20261124` | `6` | `15.120h` | `82.375h` | quarantine, contaminated water, route migration, storm, contaminated water, quarantine |
| `20261125` | `6` | `13.720h` | `79.563h` | contaminated water, route migration, storm, quarantine, contaminated water, storm |

This is still not arbitrary open-world crisis generation. It is a controlled transfer step: the crisis families are known, but timing, order, repetition, and initial world pressure vary by seed.

## Selection Boundary

The no-coordinator baseline is rejected under randomized tuning:

| Env quota | Social quota | Strength | Tune total | Tune crisis | Tune resolved | Tune coupled | Selected |
|---:|---:|---:|---:|---:|---:|---:|---|
| `0.00` | `0.00` | `0.00` | `0.520` | `0.000` | `0.056` | `0.027` | no |
| `0.10` | `0.10` | `0.70` | `0.803` | `0.590` | `0.867` | `0.835` | no |
| `0.12` | `0.12` | `0.80` | `0.807` | `0.598` | `0.867` | `0.856` | no |
| `0.14` | `0.14` | `0.90` | `0.873` | `0.734` | `1.000` | `0.958` | yes |
| `0.16` | `0.14` | `1.00` | `0.869` | `0.728` | `1.000` | `0.958` | no |
| `0.14` | `0.16` | `1.00` | `0.861` | `0.711` | `0.933` | `0.946` | no |
| `0.18` | `0.16` | `1.10` | `0.855` | `0.697` | `0.933` | `0.958` | no |
| `0.16` | `0.18` | `1.10` | `0.859` | `0.707` | `0.933` | `0.946` | no |
| `0.20` | `0.18` | `1.20` | `0.870` | `0.729` | `1.000` | `0.957` | no |

## Ablation Boundary

The transfer pass depends on both repair channels:

| Ablation | Crisis loss | Coupled response loss |
|---|---:|---:|
| `social_culture` | `0.706` | `0.965` |
| `environment` | `0.706` | `0.965` |
| `previous_action` | `0.473` | `0.403` |
| `tools` | `0.465` | `0.389` |
| `body` | `0.211` | `0.133` |
| `infrastructure` | `0.688` | `0.651` |

The social/environment result is the key gate. Removing either channel collapses crisis score and coupled response while the 12h shock gate remains intact.

## Interpretation

This report strengthens the long-horizon simulation track in a specific way:

```text
The joint-arbitration bridge does not only work on the fixed Report 113 schedule. It transfers to randomized post-12h crisis timing and order over a 96h run.
```

That moves the benchmark closer to the requested world shape: agents get time to develop before major shocks, then face repeated varying pressure that requires adaptation, infrastructure, tools, teaching, and social coordination.

The claim remains bounded. The controller still uses structured action heads and validation-selected quotas. The next step is consequence-trained policy learning where the policy learns the allocation rule directly from outcomes rather than from a fixed coordinator.

## Next Step

The next benchmark should reduce structural help further:

- train a decentralized actor-critic or model-based policy over the 96h randomized-transfer world;
- keep randomized schedules, initial pressure, and held-out seeds;
- add randomized crisis family composition, not only timing and order;
- require action allocation to emerge from learned policy/value state rather than quota candidates;
- add counterfactual traces for overfocus, delayed repair, and wrong-channel repair;
- connect the resulting policy to the physics kernel and live viewer as an open simulation controller.

## Artifacts

- [script](../experiments/ssrm_3d_coupled_crisis_randomized_transfer_controller.py)
- [schedule CSV](../artifacts/ssrm_3d_coupled_crisis_randomized_transfer_schedule.csv)
- [base training CSV](../artifacts/ssrm_3d_coupled_crisis_randomized_transfer_base_training.csv)
- [action training CSV](../artifacts/ssrm_3d_coupled_crisis_randomized_transfer_action_training.csv)
- [router selection CSV](../artifacts/ssrm_3d_coupled_crisis_randomized_transfer_router_selection.csv)
- [joint selection CSV](../artifacts/ssrm_3d_coupled_crisis_randomized_transfer_joint_selection.csv)
- [evaluation CSV](../artifacts/ssrm_3d_coupled_crisis_randomized_transfer_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_coupled_crisis_randomized_transfer_summary.csv)
- [ablation CSV](../artifacts/ssrm_3d_coupled_crisis_randomized_transfer_ablations.csv)
- [verdict CSV](../artifacts/ssrm_3d_coupled_crisis_randomized_transfer_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_coupled_crisis_randomized_transfer_trace.json)
- [results JSON](../artifacts/ssrm_3d_coupled_crisis_randomized_transfer_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_coupled_crisis_randomized_transfer_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_coupled_crisis_randomized_transfer_results.js)
