# Sequence Latent Transfer Report

## Purpose

This experiment tests whether an unlabeled sequence latent can be inferred from early outcomes and transferred to held-out contexts.

The question is:

```text
Can a learner use raw calibration outcomes to infer a reusable hidden state,
then apply it to new control contexts without being told "self" or "world"?
```

This is a stronger precursor than one-step bottleneck selection because the learned state must transfer through an episode sequence.

## Environment

Each episode has six contexts. The first two are calibration contexts. The agent observes their risky-action outcomes, then must choose actions in the remaining four held-out contexts.

| Context | Role |
|---|---|
| `goal` | Calibration context. |
| `option` | Calibration context. |
| `commitment` | Held-out transfer context. |
| `adaptation` | Held-out transfer context. |
| `prediction` | Held-out transfer context. |
| `arbitration` | Held-out transfer context. |

The learner receives sequences of context outcomes. It estimates whether the episode contains:

- `shared_sequence_state`;
- `local_context_state`;
- `no_hidden_needed`.

Then a causal boundary probe classifies shared sequence state as agent-bounded, external, or absent.

## Scenarios

| Scenario | Hidden structure | Expected transfer | Expected boundary |
|---|---|---|---|
| `self_shared_sequence` | One hidden agent capability controls all contexts. | Shared sequence state transfers. | `agent_bounded_sequence` |
| `world_shared_sequence` | One hidden external gate controls all contexts. | Shared sequence state transfers. | `external_sequence` |
| `independent_sequence` | Each context has an independent hidden condition. | Local context probes win. | `no_shared_agent_boundary` |
| `irrelevant_sequence` | Risky action always works. | No hidden state needed. | `no_shared_agent_boundary` |

## Agents

| Agent | Description |
|---|---|
| `marginal_no_memory` | Uses training marginal only. |
| `calibration_memory_no_transfer` | Remembers calibration outcomes but does not transfer them to new contexts. |
| `shared_sequence_filter` | Infers one episode-level sequence latent from calibration outcomes. |
| `task_local_probe` | Pays a local probe cost in each held-out context. |
| `learned_sequence_selector` | Chooses shared sequence, local context, or no hidden state from training sequences. |
| `oracle` | Ceiling with true hidden conditions and no probe cost. |

## Current Result

Canonical run:

```bash
python3 experiments/sequence_latent_transfer.py --episodes 500 --training-episodes 500 --seed 20260531 --calibration-contexts 2
```

| Scenario | Learned transfer | Boundary signature | Learned reward | Shared sequence reward | Local reward | Boundary supported? |
|---|---|---|---:|---:|---:|---|
| `self_shared_sequence` | `shared_sequence_state` | `agent_bounded_sequence` | 68.700 | 68.700 | 65.700 | Yes |
| `world_shared_sequence` | `shared_sequence_state` | `external_sequence` | 68.808 | 68.808 | 65.808 | Yes |
| `independent_sequence` | `local_context_state` | `no_shared_agent_boundary` | 64.668 | 18.888 | 64.668 | Yes |
| `irrelevant_sequence` | `no_hidden_needed` | `no_shared_agent_boundary` | 94.000 | 93.000 | 90.000 | Yes |

Transfer diagnostics:

| Scenario | Pairwise agreement | Independent expectation | Interpretation |
|---|---:|---:|---|
| `self_shared_sequence` | 1.000 | 0.503 | Outcomes share one episode state. |
| `world_shared_sequence` | 1.000 | 0.505 | Outcomes share one episode state, but boundary is external. |
| `independent_sequence` | 0.515 | 0.506 | Calibration outcomes do not transfer reliably. |
| `irrelevant_sequence` | 1.000 | 1.000 | All outcomes succeed; no hidden state is needed. |

## Interpretation

The result supports a sequence-transfer version of the attractor claim:

```text
A persistent latent becomes useful when early outcomes reveal a state that
continues to govern later action contexts.
```

But again, transfer is not enough for selfhood. `self_shared_sequence` and `world_shared_sequence` both select `shared_sequence_state` and both get transfer value. Only the causal boundary probe separates agent-state from world-state.

## What It Adds

This experiment adds:

1. Held-out context transfer, not only same-context model selection.
2. A memory/no-transfer baseline showing that storing calibration outcomes is not enough.
3. A shared sequence filter that succeeds only when calibration outcomes reveal a persistent episode state.
4. A causal boundary test showing that reusable sequence latents can be self-like or world-like.

## Limits

The sequence learner is still simple. It detects pairwise outcome agreement and uses a majority filter. It is not a trained neural recurrent model or RL policy. The next stronger test should train unrelated recurrent and predictive-state architectures on raw action-observation-reward streams and probe their internal states.

## Falsifiers

The sequence-transfer account weakens if:

- calibration memory without transfer matches sequence-latent transfer in shared hidden regimes;
- sequence latents transfer equally in independent-hidden regimes;
- external shared sequence latents are counted as self-equivalent without boundary evidence;
- sequence transfer improves prediction but not control;
- richer recurrent agents solve the task without any stable transferable latent.

## Artifacts

- [experiment script](../experiments/sequence_latent_transfer.py)
- [summary CSV](../artifacts/sequence_latent_transfer_summary.csv)
- [verdict CSV](../artifacts/sequence_latent_transfer_verdict.csv)
- [JSON results](../artifacts/sequence_latent_transfer_results.json)
