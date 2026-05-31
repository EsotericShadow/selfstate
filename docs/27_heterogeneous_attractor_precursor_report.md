# Heterogeneous Attractor Precursor Report

## Purpose

This experiment is a stronger precursor to the full Attractor Test.

It asks:

```text
Do different learner families trained on raw outcome streams converge on the
same latent causal signature when one hidden state controls later action?
```

It is still not the full test. The environment family is simple and the learners are small. The improvement over earlier precursors is that the same verdict is tested across several different update rules rather than one hand-coded selector.

## Learners

The learners are not given labels such as self, world, body, identity, or ownership.

| Learner | Learning style |
|---|---|
| `bayesian_shared_filter` | Bayesian-style posterior over calibration outcomes. |
| `predictive_state_table` | Predictive-state table from calibration patterns to held-out success. |
| `recurrent_error_state` | One-dimensional recurrent error update fit by reward. |
| `evolved_rule_controller` | Evolutionary search over memory-rule parameters. |
| `bottleneck_cluster_model` | Two-cluster bottleneck model over outcome vectors. |

Baselines:

- `marginal_no_memory`;
- `calibration_memory_no_transfer`;
- `task_local_probe`;
- `oracle`.

## Scenarios

| Scenario | Hidden structure | Expected result |
|---|---|---|
| `self_shared_stream` | One hidden agent capability controls all contexts. | Learners converge on an agent-bounded candidate latent. |
| `world_shared_stream` | One hidden external gate controls all contexts. | Learners converge on an external candidate latent. |
| `independent_stream` | Each context has an independent hidden condition. | Learners reject shared self/world transfer; local probes win. |
| `irrelevant_stream` | Risky action always works. | Learners collapse to no hidden state. |

## Measurement

Each learner produces an internal scalar or probability after calibration.

That latent is probed for:

- self-signal decodability;
- world-signal decodability;
- held-out control decodability;
- reward impact;
- whether it is used across held-out contexts;
- scenario-level causal boundary under agent and world interventions.

The key rule is:

```text
Converging on a shared latent is not enough.
The latent counts as self-equivalent only when the causal boundary is agent-bounded.
```

## Current Result

Canonical run:

```bash
python3 experiments/heterogeneous_attractor_precursor.py --episodes 500 --training-episodes 600 --seed 20260601 --calibration-contexts 2 --evolutionary-candidates 600
```

| Scenario | Boundary signature | Expected convergence | Converged architectures | Best architecture reward | Local probe reward | Supported? |
|---|---|---|---:|---:|---:|---|
| `self_shared_stream` | `agent_bounded_stream` | `agent_bounded_candidate` | 5/5 | 34404.000 | 32904.000 | Yes |
| `world_shared_stream` | `external_stream` | `external_candidate` | 5/5 | 33702.000 | 32202.000 | Yes |
| `independent_stream` | `no_shared_agent_boundary` | `no_shared_agent_boundary` | 5/5 | 20000.000 | 32282.000 | Yes |
| `irrelevant_stream` | `no_shared_agent_boundary` | `no_hidden_needed` | 5/5 | 47000.000 | 45000.000 | Yes |

Boundary diagnostics:

| Scenario | Agent intervention effect | World intervention effect | Interpretation |
|---|---:|---:|---|
| `self_shared_stream` | 0.450 | 0.000 | Shared latent is agent-bounded. |
| `world_shared_stream` | 0.000 | 0.427 | Shared latent is external. |
| `independent_stream` | 0.000 | 0.000 | No shared agent/world boundary. |
| `irrelevant_stream` | 0.000 | 0.000 | No hidden state required. |

## Interpretation

The result strengthens the attractor claim in a narrow way:

```text
When early outcomes reveal a persistent state that controls later action,
multiple learner families converge on a compact transferable latent.
```

But the result also strengthens the anti-tautology boundary:

- the same learner convergence appears for reusable world-state;
- independent hidden variables do not justify a shared self latent;
- no-hidden controls collapse to no hidden state;
- a causal boundary test remains required before calling the latent self-equivalent.

## What It Adds

Compared with the sequence-latent test, this experiment adds:

1. Several learner families with different update rules.
2. A convergence count across learners, not only one learned selector.
3. Decodability probes for self-signal, world-signal, and held-out control.
4. A matched external shared-state case showing that architecture convergence alone is not selfhood.

## Limits

This remains a toy precursor.

The learners are still simple. The environment surface is still one discrete calibration/control family. There is no deep recurrent policy, transformer, model-based RL agent, active-inference agent, or evolutionary controller in a rich embodied environment.

The next stronger version should train unrelated policies on raw action-observation-reward streams across multiple environment families, then probe recurrent states or learned memories for agent-bounded causal structure.

## Falsifiers

The heterogeneous precursor weakens if:

- learners converge equally on self-equivalent signatures in independent-hidden controls;
- external shared-state convergence is counted as selfhood without boundary evidence;
- no-memory or calibration-no-transfer baselines match shared learners under self-shared pressure;
- learned latents decode hidden state but do not improve control;
- richer architectures solve the same pressures with no stable decodable agent-state latent.

## Artifacts

- [experiment script](../experiments/heterogeneous_attractor_precursor.py)
- [summary CSV](../artifacts/heterogeneous_attractor_precursor_summary.csv)
- [verdict CSV](../artifacts/heterogeneous_attractor_precursor_verdict.csv)
- [JSON results](../artifacts/heterogeneous_attractor_precursor_results.json)
