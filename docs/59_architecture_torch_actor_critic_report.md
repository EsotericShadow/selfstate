# Architecture Torch Actor-Critic Report

## Purpose

This experiment tests the next pressure point after report 58.

Policy-gradient budget sweeping repaired seed stability for self-persistent and passive-world recurrence, but detachable-tool recurrence remained the hardest boundary. This report replaces the hand-coded finite-difference and score-function toy policies with PyTorch recurrent actor-critic learners and runs them on Apple Silicon MPS when available.

## Question

Can neural recurrent actor-critic learners recover the same causal boundary signatures across architectures while preserving clean controls?

## Design

The experiment trains three recurrent actor-critic architectures:

- `torch_rnn`
- `torch_gru`
- `torch_lstm`

Each learner receives mixed noisy observations, samples a risky/safe action from its actor logit, and updates actor and critic losses from sampled episode return. Restart selection uses sampled validation return. There are no source-direction seeds, smooth expected-return surrogate, self labels, or boundary-aware restart criteria.

After training, the same causal boundary classifier is applied to the trained policy logits under:

- persistent body/action-effect intervention;
- detachable tool intervention;
- passive external recurrence;
- independent hidden-state control;
- irrelevant hidden-state control.

The support criterion is strict: every architecture must match the expected causal signature in each scenario.

## Command

```bash
python3 experiments/architecture_torch_actor_critic.py --episodes 200 --training-episodes 400 --validation-episodes 240 --batch-episodes 512 --seed 20260606 --horizon 8 --evidence-samples 9 --cue-accuracy 0.85 --epochs 300 --restarts 8 --hidden-size 12 --learning-rate 0.02 --entropy-weight 0.0 --value-weight 0.35 --max-grad-norm 2.0 --device mps
```

The canonical manifest uses `--device auto`, which selects MPS when available and CPU otherwise.

## Current Result

| Scenario | Expected signature | Converged architectures | Result |
|---|---|---:|---|
| `self_persistent_boundary` | `end_to_end_persistent_agent_boundary` | 3/3 | Strict actor-critic shared boundary. |
| `detachable_tool_world` | `end_to_end_detachable_external_boundary` | 3/3 | Strict actor-critic shared boundary. |
| `passive_world_boundary` | `end_to_end_passive_external_boundary` | 3/3 | Strict actor-critic shared boundary. |
| `independent_hidden` | `end_to_end_local_probe` | 3/3 | Rejects shared recurrence. |
| `irrelevant_control` | `end_to_end_no_hidden_needed` | 3/3 | Rejects hidden state. |

The run used `torch 2.8.0` with `mps_available=True` and `device_used=mps`.

## Boundary Probe Detail

| Scenario | Architecture | Selected policy | Key causal effect |
|---|---|---|---|
| `self_persistent_boundary` | `torch_rnn` | `recurrent_controller` | Action-0 present effect `4.172`, persistence `1.000`. |
| `self_persistent_boundary` | `torch_gru` | `recurrent_controller` | Action-0 present effect `5.017`, persistence `1.000`. |
| `self_persistent_boundary` | `torch_lstm` | `recurrent_controller` | Action-0 present effect `5.008`, persistence `1.000`. |
| `detachable_tool_world` | `torch_rnn` | `recurrent_controller` | Action-1 present effect `3.848`, persistence `0.000`. |
| `detachable_tool_world` | `torch_gru` | `recurrent_controller` | Action-1 present effect `4.487`, persistence `0.000`. |
| `detachable_tool_world` | `torch_lstm` | `recurrent_controller` | Action-1 present effect `5.200`, persistence `0.000`. |
| `passive_world_boundary` | `torch_rnn` | `recurrent_controller` | Best action-boundary score remains near zero. |
| `passive_world_boundary` | `torch_gru` | `recurrent_controller` | Best action-boundary score remains near zero. |
| `passive_world_boundary` | `torch_lstm` | `recurrent_controller` | Best action-boundary score remains zero. |
| `independent_hidden` | all three | `task_local_probe` | Shared recurrence rejected. |
| `irrelevant_control` | all three | `greedy_no_state` | Hidden state rejected. |

## Interpretation

This is the strongest current positive result in the architecture-boundary stack.

The actor-critic learner recovers the self-persistent, detachable-tool, and passive-world boundary signatures across `torch_rnn`, `torch_gru`, and `torch_lstm`. It also preserves both critical controls: independent hidden variables select local probing, and irrelevant hidden state selects no-hidden greedy action.

This matters for the hidden-state loophole. The result is not "hidden state helps." It is that a neural recurrent learner trained from sampled return can produce policy states that pass the post-training causal boundary test:

- persistent agent-boundary intervention moves the policy in the self case;
- detachable tool intervention moves the policy only in the present tool case;
- passive external recurrence supports recurrent control without action-boundary alignment;
- independent and irrelevant controls reject shared recurrence.

## Limits

The result is still toy-scale:

- binary hidden causes;
- compact mixed observations;
- short horizons;
- simple recurrent networks;
- one canonical seed and one tuned MPS actor-critic budget;
- no richer embodied dynamics, curriculum, or continuous action space.

It strengthens the Attractor Test precursor, but it does not prove a general law of adaptive systems.

## Falsifiers And Strengtheners

The attractor claim weakens if:

- actor-critic seed sweeps lose strict convergence or create control false positives;
- CPU and MPS backends disagree in the causal signatures;
- richer recurrent or transformer policies solve reward while losing the boundary signature;
- richer body, viability, frame, and continuity tasks do not reproduce the pattern.

The attractor claim strengthens if:

- the actor-critic result is seed-stable;
- the same signatures recur across richer environment surfaces;
- causal ablations of learned neural states selectively damage agent-bounded tasks;
- model-based neural agents converge on the same boundary without supplied intervention labels.

## Artifacts

- [experiment script](../experiments/architecture_torch_actor_critic.py)
- [summary CSV](../artifacts/architecture_torch_actor_critic_summary.csv)
- [verdict CSV](../artifacts/architecture_torch_actor_critic_verdict.csv)
- [JSON results](../artifacts/architecture_torch_actor_critic_results.json)
