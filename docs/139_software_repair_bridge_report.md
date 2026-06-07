# Programmable Repair Bridge / WrongFix Arena Spec

## Question

Report 138 showed that short consequence-aware sequence planning can solve the
72h readiness world while planner-free GRU imitation still fails.

This report asks the first software-facing bridge question:

```text
Can the same weakest-channel repair idea be expressed as a structured
software-repair benchmark where visible tests can pass for the wrong reason?
```

The narrow software version is:

```text
The best repair is not necessarily the repair that makes the visible test pass.
The best repair is the one that protects the weakest required correctness
channel.
```

## What Changed

This report adds a small deterministic package:

- `experiments/software_repair_bridge/models.py`
- `experiments/software_repair_bridge/task_bank.py`
- `experiments/software_repair_bridge/evaluator.py`
- `experiments/software_repair_bridge/critics.py`
- `experiments/software_repair_bridge/artifacts.py`
- `experiments/software_repair_bridge/benchmark.py`

The task bank contains `15` structured software-repair tasks. Each task has:

- a bug report;
- a visible failure;
- a hidden cause;
- required correctness channels;
- plausible candidate repairs;
- visible and hidden test outcomes;
- regression, root-cause, API/contract, security, maintainability,
  performance, and reviewability scores;
- an expected best repair;
- a plain explanation.

## What This Does Not Claim

This is not real repo coding.

It does not call an LLM, edit external repositories, run real hidden tests, or
prove that SelfState improves frontier coding agents.

It is a structured bridge: the same consequence/weakest-channel principle used
in the readiness and coupled-crisis planners is mapped into a software-shaped
repair arena.

## Canonical Command

```bash
python3 -m experiments.software_repair_bridge.benchmark
```

## Baselines

The benchmark compares five deterministic policies:

| Policy | Selection rule |
|---|---|
| `visible_test_only` | Pick the first repair that passes the visible test. |
| `root_cause_first` | Pick the highest root-cause score. |
| `min_channel_critic` | Pick the repair with the strongest weakest required correctness channel. |
| `weighted_quality_critic` | Pick the repair with the best weighted channel average. |
| `oracle` | Pick the expected best repair. |

## Result

The minimum-channel critic passes the bridge condition against the visible-test
baseline.

| Policy | Visible pass | Hidden pass | Wrong fix | Root-cause repair | Regression avoided | Weakest channel | Oracle match | Mean quality |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `min_channel_critic` | `1.000` | `1.000` | `0.000` | `1.000` | `1.000` | `0.864` | `1.000` | `0.946` |
| `oracle` | `1.000` | `1.000` | `0.000` | `1.000` | `1.000` | `0.864` | `1.000` | `0.946` |
| `root_cause_first` | `1.000` | `0.867` | `0.200` | `1.000` | `0.800` | `0.708` | `0.800` | `0.889` |
| `visible_test_only` | `1.000` | `0.067` | `1.000` | `0.200` | `0.000` | `0.012` | `0.000` | `0.488` |
| `weighted_quality_critic` | `1.000` | `1.000` | `0.000` | `1.000` | `1.000` | `0.864` | `1.000` | `0.946` |

The verdict row records:

```text
hidden_pass_gain = 0.933333
wrong_fix_reduction = 1.000000
root_cause_gain = 0.800000
weakest_channel_gain = 0.852000
supports_programmable_repair_bridge = true
verdict = pass
```

## Interpretation

This is a positive bridge result, but only at the structured benchmark level.

The visible-test baseline passes every visible test and still selects the wrong
repair on every task. That is the intended WrongFix Arena shape: a shallow green
test can hide root-cause, hidden-test, regression, API, security,
maintainability, performance, or review risk.

The minimum-channel critic avoids that failure by asking which required channel
is weakest for each repair. It chooses the repair that preserves the most fragile
correctness surface, not just the most visible one.

Root-cause-first also fails on some tasks. That matters because a repair can
identify the broad cause but still be unacceptable if it creates high regression
risk, poor performance, bad deployment safety, or weak reviewability.

The weighted-quality critic also matches the oracle in this small task bank.
That is useful but not decisive. The next stronger software bridge should use
larger randomized tasks where channel weights, visible-test temptation, and
hidden-risk composition vary across seeds.

## Why It Connects To Report 138

Report 138 says consequence-aware planning works in the readiness world while
standalone imitation fails.

Report 139 translates that into software:

- visible tests are the short-term reward;
- hidden tests, regression risk, API safety, security, maintainability,
  performance, and reviewability are the delayed consequence channels;
- a wrong fix is a repair that wins the visible channel while damaging the
  weakest required channel;
- a useful software critic should preserve the weakest required correctness
  channel before trusting apparent success.

## Next Step

Do not claim real coding-agent improvement yet.

The next credible step is a dynamic WrongFix generator:

- randomize task templates and hidden-cause surfaces;
- make visible tests passable by several wrong repairs;
- add held-out task families;
- add executable toy repos only after the structured arena stays clean;
- then compare an LLM/code-agent baseline against the same baseline wrapped by a
  repair critic.

## Artifacts

- [package](../experiments/software_repair_bridge/)
- [evaluation CSV](../artifacts/software_repair_bridge_eval.csv)
- [summary CSV](../artifacts/software_repair_bridge_summary.csv)
- [verdict CSV](../artifacts/software_repair_bridge_verdict.csv)
- [results JSON](../artifacts/software_repair_bridge_results.json)
