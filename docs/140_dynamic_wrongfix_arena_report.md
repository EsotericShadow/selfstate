# Programmable Repair Bridge / Dynamic WrongFix Arena

## Question

Can the WrongFix arena be made realistic and adversarial enough that a shallow visible-test benchmark no longer dominates, without claiming a real LLM or repo coding result?

This report tests a deterministic, seeded software-repair benchmark where correctness is multi-channel and tradeoffs are explicitly exposed.

## What Changed

This report adds a dynamic benchmark variant under:

- `experiments/software_repair_bridge/dynamic_benchmark.py`
- `artifacts/software_repair_dynamic_eval.csv`
- `artifacts/software_repair_dynamic_summary.csv`
- `artifacts/software_repair_dynamic_verdict.csv`
- `artifacts/software_repair_dynamic_results.json`

The generator creates at least 100 tasks deterministically from seeded templates.
It covers these task types:

- auth/session
- cache invalidation
- migration/backfill
- async race conditions
- flaky timing
- API compatibility
- security validation
- query injection
- path traversal
- money/rounding
- timezone serialization
- dependency upgrade
- event listener/resource leak
- frontend state/reducer
- performance/N+1
- inventory/transactional
- logging/observability misdiagnosis

Each task has explicit family labels, difficulty tiers, held-out family flags, noisy bug lines, and irrelevant signal lines.

Policies in this report:

- `visible_test_only`
- `root_cause_first`
- `min_channel_critic`
- `weighted_quality_critic`
- `conservative_review_critic`
- `risk_tolerant_shipper`
- `oracle`

## What This Does Not Claim

This is not real external repository repair.

It does not run LLMs, does not edit repositories, and does not prove frontier coding-agent improvement.

It is a structured benchmark bridge that tests if calibrated repair judgment can survive visible-test ambiguity, noisy signals, and multi-channel risk tradeoffs.

## Canonical Command

```bash
python3 -m experiments.software_repair_bridge.dynamic_benchmark
```

(Deterministic by default with seed `14022026`, `120` seeded tasks, and `5` deterministic false-positive calibration tasks for `125` total tasks.)

## Result

`weighted_quality_critic` is selected by the best-policy check and improves hidden, wrong-fix, root-cause, and regression outcomes over `visible_test_only` while staying within false-positive/overblocking thresholds.

| Policy | Visible pass | Hidden pass | Wrong fix | Root-cause repair | Regression avoided | Weakest channel | Oracle match | Mean quality |
|---|---:|---:|---:|---:|---:|---:|---:|---:
| `visible_test_only` | `1.000` | `0.344` | `0.864` | `0.240` | `0.360` | `0.060022` | `0.136` | `0.631` |
| `root_cause_first` | `0.840` | `0.976` | `0.208` | `0.984` | `0.824` | `0.134015` | `0.792` | `0.818` |
| `min_channel_critic` | `0.880` | `1.000` | `0.328` | `0.824` | `0.824` | `0.163007` | `0.672` | `0.818` |
| `weighted_quality_critic` | `0.840` | `1.000` | `0.008` | `0.968` | `1.000` | `0.118217` | `0.992` | `0.853` |
| `conservative_review_critic` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `0.000` |
| `risk_tolerant_shipper` | `1.000` | `0.840` | `0.320` | `0.864` | `0.704` | `0.137453` | `0.680` | `0.780` |
| `oracle` | `0.840` | `1.000` | `0.000` | `0.968` | `1.000` | `0.118663` | `1.000` | `0.853` |

The `verdict` row records:

```text
visible_hidden_pass_rate = 0.344
best_hidden_pass_rate = 1.000
wrong_fix_reduction = 0.856
visible_wrong_fix_rate = 0.864
visible_root_cause_repair_rate = 0.240
best_root_cause_repair_rate = 0.968
visible_regression_avoidance_rate = 0.360
best_regression_avoidance_rate = 1.000
visible_weakest_channel_score = 0.060022
best_weakest_channel_score = 0.118217
false_positive_rate = 0.0
overblocking_rate = 0.0
underblocking_rate = 0.008
meets_thresholds = true
verdict = pass
```

## Interpretation

This is a stronger bridge pass than Report 139:

- `visible_test_only` regularly picks wrong, risky fixes (`wrong_fix_rate = 0.864`).
- `min_channel_critic` improves hidden pass but still over-accepts for this harder distribution.
- `weighted_quality_critic` wins the aggregate objective and dominates the visible baseline on the requested success metrics with calibrated false-positive control (`0.0`).
- `conservative_review_critic` demonstrates the paranoia boundary by blocking every task and failing the calibrated-governance gate.
- The held-out family split keeps a separate realism channel, and task-level seeds/tiers preserve deterministic but non-trivial variability.

This does not claim real repo repair automation quality or frontier coding-agent gains. It claims only that a dynamic, noisy, multi-channel software-shaped benchmark can expose and rank realistic repair judgment behavior.

## Artifacts

- [package](../experiments/software_repair_bridge/)
- [evaluation CSV](../artifacts/software_repair_dynamic_eval.csv)
- [summary CSV](../artifacts/software_repair_dynamic_summary.csv)
- [verdict CSV](../artifacts/software_repair_dynamic_verdict.csv)
- [results JSON](../artifacts/software_repair_dynamic_results.json)
