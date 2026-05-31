# Hidden-State Boundary Attack

## The Attack

The current theory risks collapsing into:

```text
Systems with useful hidden variables benefit from tracking useful hidden variables.
```

That is too weak. It makes selfhood nearly tautological and fails to separate:

- hidden world-state tracking;
- hidden internal-state tracking;
- generic recurrent memory;
- agent-state modeling;
- selfhood.

The corrected theory must treat hidden-state tracking as a broader class. Selfhood is only one narrower solution inside that class.

## Replacement Claim

Hidden-state tracking becomes self-equivalent only when the tracked variable is:

1. agent-bounded: it belongs to the controlled system rather than only the external world;
2. persistent: it carries causal information across more than one observation/action cycle;
3. action-mediated: it changes what the same action does, or what actions remain available;
4. control/value relevant: policy quality, future options, or viability depend on it;
5. counterfactually agentic: intervening on the variable changes what this system can do or what its actions mean;
6. integrated: the same variable is reused across prediction, control, adaptation, or memory rather than isolated in one local predictor.

Continuity and ownership add a stronger identity-like layer:

7. continuity-indexed: it links past, present, and projected future states as states of the same continuing controlled process.

The minimal self-equivalent threshold is criteria 1-6. Criterion 7 is not required for simple sensorimotor selfhood, but it is required for identity-like selfhood.

## Boundary Ladder

| Tier | Representation | Example | Counts as selfhood? |
|---|---|---|---|
| 0 | Hidden external state | Weather, terrain, market regime | No. This is world modeling. |
| 1 | Generic hidden internal variable | Local cache, unused diagnostic bit | No. Internal location is not enough. |
| 2 | Passive internal-state tracker | Fatigue sensor used only for report prediction | No, unless it affects control/value. |
| 3 | Agent-state controller | Actuator gain, damage, energy, sensor reliability | Minimal self-equivalent. |
| 4 | First-person control frame | Counterfactuals over what this system can do next | Stronger self-equivalent. |
| 5 | Continuity/identity self | Owner/epoch/commitment index across interruption | Identity-like self. |
| 6 | Narrative or phenomenal self | Reportable autobiography or experience | Not tested here. |

The theory should not infer selfhood from tiers 0-2. Those are hidden-state mechanisms. They become evidence for selfhood only when the same latent participates in tier 3 or above.

## Why This Avoids Tautology

The claim is no longer:

```text
Hidden variables are useful, therefore self exists.
```

The claim becomes:

```text
When the hidden variable is a persistent state of the controlled system,
and future action, value, or coherence depends on it,
optimization should favor a reusable agent-state abstraction.
```

That abstraction is self-equivalent only because it answers action-centered questions:

- What can this system do now?
- What will happen if this system acts?
- What will this system be able to do later?
- Which prior commitments belong to this continuing system?
- Which prediction errors came from the world, and which came from changed agent-state?

## Positive And Negative Controls

### Negative Control A: Hidden World Variable

If a hidden external variable improves prediction or control, that supports hidden world modeling, not selfhood.

Example: wind affects movement. A wind posterior may be useful, but it is not a self-model unless it is bound to the agent's action interface, such as a worn sail or damaged actuator.

### Negative Control B: Internal But Control-Irrelevant Variable

If an internal variable is persistent and hidden but does not affect action, future options, reward, viability, or continuity, tracking it is not selfhood.

Example: a diagnostic counter improves self-report accuracy but never changes policy or future control.

### Negative Control C: Generic Memory

If raw history or recurrent state performs equally well with no decodable, stable, causally active agent-state factor, the self-attractor claim weakens.

### Positive Control A: Action-Effect State

If a hidden variable changes what actions do, and intervention on that variable changes predicted control, it passes the minimal self-equivalent threshold.

Example: actuator gain, body damage, sensor calibration, or current competence.

### Positive Control B: Future Viability State

If actions must regulate future internal state to preserve future options, self-state becomes a long-horizon control variable.

Example: energy, fatigue, damage, toxicity, or thermal state.

### Positive Control C: Continuity Index

If an agent must decide which past commitments, memories, or goals still belong to the same continuing process, the representation becomes identity-like.

Example: owner/current-epoch/pending-status metadata after interruption.

## Falsifiable Boundary Tests

A variable should not be counted as self-equivalent unless these probes succeed:

1. Boundary probe: does the variable describe the controlled system rather than only the external environment?
2. Action probe: does changing it alter action effects, available actions, or action costs?
3. Value probe: does using it improve reward, survival, transfer, or recovery?
4. Counterfactual probe: can the system answer what would happen if its own state were different?
5. Integration probe: is the same variable reused across more than one prediction/control problem?
6. Ablation probe: does removing or randomizing it selectively harm tasks that require agent-state but not tasks that only require world-state?
7. Continuity probe: for identity-like selfhood, does it distinguish current own commitments from stale, foreign, duplicated, or contradictory records?

## New Falsifiers Introduced By The Attack

The selfhood claim weakens if:

- hidden external variables produce the same claimed advantages and were misclassified as self-state;
- hidden internal variables improve passive prediction but not control, value, adaptation, or continuity;
- generic recurrent memory solves scaled drift, viability, and interruption tasks with no decodable agent-bound latent;
- isolated internal trackers solve local tasks but do not integrate across prediction, action, viability, or memory;
- self-labeled variables improve performance only by adding capacity, not by carrying agent-bounded causal information;
- interventions on the proposed self-variable do not change action-centered counterfactuals.

## Revised Minimal Mechanism

The smallest non-conscious self-equivalent is not:

```text
persistent hidden state
```

It is:

```text
agent-bounded persistent state
+ action-conditioned prediction
+ control/value dependence
+ counterfactual intervention sensitivity
+ cross-task reuse
```

For identity-like selfhood, add:

```text
continuity index over owned past, present, and future states
```

## Consequence For The Research Program

The evidence standard must separate three questions:

1. Does hidden-state tracking help?
2. Is the hidden state internal to the controlled system?
3. Does it function as a reusable agent-state abstraction for action, value, adaptation, or continuity?

Only the third question is evidence for selfhood. The first is ordinary latent-state modeling. The second is agent-state tracking. The third is where "hidden internal variable tracking" becomes computational selfhood.

## Current Stress Evidence

The architecture hard-return and online-return audits make this boundary operational. They show that objective-only return training can select useful recurrent or local hidden-state strategies while still failing strict self/tool boundary convergence. That is exactly the distinction this attack requires:

- high return is not enough;
- recurrence is not enough;
- hidden-state usefulness is not enough;
- the learned state must pass the persistent agent-boundary intervention test.

In the current online return-learner audit, independent-hidden and irrelevant controls remain clean, but self, detachable, and passive shared regimes are only 1/3 convergent across recurrent architectures. The policy-gradient learner then recovers 3/3 convergence in those shared regimes while keeping the same controls clean. The policy-gradient seed sweep adds that this recovery is not automatically seed-stable: controls remain clean, but shared-regime strict convergence appears in only some seeds. The policy-gradient budget sweep repairs seed stability for self-persistent and passive-world recurrence, but detachable-tool recurrence remains partial. The Torch actor-critic learner then recovers strict self, detachable, and passive signatures across `RNN`, `GRU`, and `LSTM` actor-critics while independent-hidden and irrelevant controls still reject shared recurrence or hidden state. Together, the results keep the hidden-state loophole explicit: sampled return can shape self-equivalent boundary structure, but only when the learner actually passes the causal boundary test, and detachable external action effects remain a distinct boundary problem until the actor-critic result survives seed and environment sweeps.

The SSRM-3D precursor adds a second boundary: the LLM is not the self. The persistent self-equivalent state is the realtime control workspace that estimates viability, integrity, mobility, uncertainty, commitments, and attention priorities. The language module receives a compressed packet and recommends; reflex, arbiter, and motor layers still control the organism. This prevents the experiment from replacing the hidden-state loophole with a language-controller loophole.

The SSRM-3D recurrent-observer precursor adds a third boundary: the measured self-state does not have to be the hand-built workspace. Recurrent observers trained on embodied traces recover hidden energy, integrity, mobility, and sensor capability. Stage 0 remains only body-state decodability with little recurrent advantage; stages 1-6 show stronger recurrent self-state recovery and future-viability sensitivity to self-state edits. This still does not prove selfhood, but it blocks the simple objection that the SSRM-3D result is only a named internal variable table.

The SSRM-3D learned-controller precursor adds a fourth boundary: learned policy state, not just observer state, carries self-state under pressure. Recurrent controllers trained without self labels strongly beat frame-only controllers in stages 1-6 and contain decodable energy, integrity, mobility, and sensor capability. The action-edit swing remains weak, so the result blocks the "observer only" objection but keeps the causal-editability loophole open.
