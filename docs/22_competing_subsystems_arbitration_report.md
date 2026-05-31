# Competing Subsystems Arbitration Report

## Purpose

This experiment tests whether a self-equivalent state can act as an arbitration variable across competing subsystems.

The question is not:

```text
Can the agent track a hidden internal variable?
```

It is:

```text
When several locally reasonable subsystems disagree, does a shared model of the continuing system select more coherent action?
```

This targets the coherence-stabilizer hypothesis without treating hidden agent-state tracking as automatically sufficient for selfhood.

## Environment

Each episode contains three proposal pressures:

- immediate reward: exploit the current opportunity;
- commitment completion: finish an outstanding task;
- safety maintenance: restore hidden energy before collapse.

Actions are `exploit`, `fulfill`, `restore`, `inspect_self`, and `inspect_world`.

Scenarios:

| Scenario | Hidden pressure | Expected result |
|---|---|---|
| `no_conflict` | High energy, no commitment, open world. | Simple exploit policies should tie; self inspection is unnecessary. |
| `subsystem_conflict` | A commitment is due, but energy is hidden and may be too low. | Shared self-state arbitration should beat local voting. |
| `world_gate_conflict` | Reward depends on a hidden external gate, not agent energy. | World-state inspection should beat self-state arbitration. |

## Agents

| Agent | Description |
|---|---|
| `reward_priority` | Always follows the immediate reward subsystem. |
| `commitment_priority` | Fulfills commitments when due; otherwise exploits. |
| `safety_priority` | Restores under visible energy symptoms, otherwise follows commitments or reward. |
| `local_vote_no_shared_self` | Lets reward, commitment, and safety subsystems vote without shared self-state. |
| `self_coherence_arbitrator` | Inspects and uses persistent energy state to decide whether to restore or fulfill. |
| `world_gate_arbitrator` | Inspects external world gate state and ignores self-state unless required by other rules. |
| `oracle_coherence_arbitrator` | Ceiling with direct access to true hidden state. |

## Current Result

Canonical run:

```bash
python3 experiments/competing_subsystems_arbitration.py --episodes 500 --horizon 14 --seed 20260530
```

| Scenario | Best non-oracle agent | Local vote reward | Safety reward | Self-arbitrator reward | World-arbitrator reward | Boundary supported? |
|---|---|---:|---:|---:|---:|---|
| `no_conflict` | `commitment_priority` | 98.000 | 98.000 | 98.000 | 98.000 | Yes |
| `subsystem_conflict` | `self_coherence_arbitrator` | -99.696 | 77.560 | 77.880 | -145.614 | Yes |
| `world_gate_conflict` | `world_gate_arbitrator` | -110.114 | -48.144 | -51.424 | -13.320 | Yes |

Additional diagnostic:

| Scenario | Self incoherent actions | Local-vote incoherent actions | Self inspection count | World inspection count |
|---|---:|---:|---:|---:|
| `no_conflict` | 0.000 | 0.000 | 0.000 | 0.000 |
| `subsystem_conflict` | 0.000 | 11.462 | 1.000 | 0.000 |
| `world_gate_conflict` | 0.000 | 7.390 | 0.000 | 1.000 |

## Interpretation

The result supports a narrow coherence mechanism:

```text
Representing "me" becomes useful when subsystem proposals must be evaluated
against the shared state of the same continuing system.
```

In `subsystem_conflict`, local voting collapses because immediate reward dominates even when hidden energy makes that action incoherent for the continuing agent. The self-coherence arbitrator avoids collapse by using a persistent estimate of agent energy to decide whether the system should restore before fulfilling a commitment.

The boundary controls matter:

- In `no_conflict`, self-state adds no advantage and no inspection is used.
- In `world_gate_conflict`, self-state is the wrong abstraction; external world-state inspection wins.
- In `subsystem_conflict`, the advantage appears when coherence depends on hidden agent-state.

## What It Adds

This experiment adds a subsystem-level version of the coherence claim:

1. Coherence is not only interruption recovery; it also appears during simultaneous action arbitration.
2. The relevant self variable is a shared state of the continuing system, not a private label.
3. World-state controls prevent treating every hidden arbitration variable as selfhood.
4. No-conflict controls prevent treating explicit self inspection as always useful.

## Limits

This is a hand-coded toy. The self-arbitrator is explicit, the subsystem proposals are fixed, and no agent learns the arbitration rule.

The strongest limitation is that `safety_priority` nearly matches the self-coherence arbitrator in `subsystem_conflict`. That means this result supports shared agent-state arbitration over naive local voting, but it does not prove that this explicit self-arbitrator is uniquely necessary. A conservative safety heuristic remains a live non-self alternative in this small environment.

## Falsifiers

The coherence-arbitration account weakens if:

- local arbitration or value normalization scales to subsystem conflict without shared agent-state;
- conservative safety heuristics match self-state arbitration across richer commitment and viability regimes;
- world-state arbitration solves agent-state conflict with equal reward;
- learned agents resolve subsystem conflict without any stable, reusable agent-state abstraction;
- intervention on the inferred self-state does not selectively disrupt arbitration in agent-state conflict.

## Artifacts

- [experiment script](../experiments/competing_subsystems_arbitration.py)
- [summary CSV](../artifacts/competing_subsystems_arbitration_summary.csv)
- [verdict CSV](../artifacts/competing_subsystems_arbitration_verdict.csv)
- [JSON results](../artifacts/competing_subsystems_arbitration_results.json)
